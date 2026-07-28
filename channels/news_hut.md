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
<img src="https://cdn4.telesco.pe/file/O4y7_nVToHYxusaREwx8d8sM7w88xMfGmuipw6sHA4rsD13pkL1H8wz0s-2IEDirmsw4oNLAfBGEm5BxhFL8ArH7jiSRawffylSnKV7F4z885ms-dDmPB5VKZW2TGRlKC7P6W0VhhYhb-fPK4z9Jq2QVGGa0DC0w0iz6oq-rBVIG_5m7R_GrRgSNb3Nm9mhWSmvRZMvJIf6HEJLi20OUMYMiPhVWzQu8894Q9SOLda0nnQftnrMuxEk6AxuspOZm5jgfOCUFWK9Vg9hKz0pm_qF_u8ou-B3rT6DRadscfnnh1aC1OEas5PBmvA3tQr5jaXcH9vrbgLh6pump7ftLjg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 هات نیوز | HotNews</h1>
<p>@news_hut • 👥 143K عضو</p>
<a href="https://t.me/news_hut" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 بدون هیچگونه گرایش و تمایلات سیاسی، همیشه سمت حقیقت و مردم.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-07 00:35:05</div>
<hr>

<div class="tg-post" id="msg-69154">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kR05wUIC_0pcfEDyziHdTodgJN0vO6IyaX2Xk0JuqCuPgcMRC101Wp1qoXB3TM0iFhLiV3lPG1eShI-k_mX9IpcfRMu5B-E2sgr8qSCU8Xd8_7noC95aZW2ajt5zn9Md_FKxAYtJ99PQWqYfjfLJZiG3ZNq_7ryy1eCN0UqlMOgMxJ30QYxjiNU8IvBgccGZ3CSu7q9LR3UMuuZzWuV4GE_rzrXSM-znM-trUCk1qFKbDT2CIrlgxF6TxA8btZHs5okit-AemwbSlCSHliNbJZJaJ-gBnIKTLjlObXZVPjNMfY6BxdMpMxxArlbSdnb3WspIK9G4kO73VsfPLU1l_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
حضور شاهزاده رضا پهلوی در مراسم لیندسی گراهام
@News_Hut</div>
<div class="tg-footer">👁️ 2.78K · <a href="https://t.me/news_hut/69154" target="_blank">📅 00:25 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69153">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2c4805d382.mp4?token=b1ERTCW-BdzyD3P8gcVtcPKScPVz5hpTuRVJYMXKpldd_BqeCtdPGBr-NGrIkb4lmH59cG4b_6i7fWlvO5WJrCiqGXrc2jcS0-m0BTatzE8orHmmemrgESkzy8ErBlCJgifdN1yhEoApJefxnJIW_RXuQhQseAhejG7qBmlHULwQi-PeUHXhqX8CmD2V69mgqU1NTO_ZwV4aL0_sz6rvWcxY3OG9NaZvPG6Exh8XuNN7urzyv4sXvUg4ZTazbxNrD2I7KQXvslbSiV_KDcXZSNkkCJgORk0SeTVPYOVB_uJcmIM-3_KhC069ev5aQKz5nWZXZMeesQt1i3Zx2isLzKFf7mnK_8NJud4_O9DAF6to_fHPHy9bYtDF0NVJtFFycF-nm08yqpBfk8jZz7U5fBD-HnDnJULkjKhbqiO938ZFXd4UGE4konCKSQbnjEXanwy_xPW6qCYMqctb3NDlVvkv38VvV4dYN4VfJlkIErbdC6zJBdLEbVysGT8ESQXFB4_dxEWIeGPmrpOPpgSyr_RpavyEjOAwb9iSPCepdMmoOAtfVt92ZDulcIbVgm5EJWwJ42yCr5KnlVoSG6uhoE8Lq6R9xqGKIyNouKsEMEm-DZWR2RSxUVsZpZgEBXTO3YaU5fvpsJxO9JhbPbQomi6jJQeSdPEdWG0dmevNdvk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2c4805d382.mp4?token=b1ERTCW-BdzyD3P8gcVtcPKScPVz5hpTuRVJYMXKpldd_BqeCtdPGBr-NGrIkb4lmH59cG4b_6i7fWlvO5WJrCiqGXrc2jcS0-m0BTatzE8orHmmemrgESkzy8ErBlCJgifdN1yhEoApJefxnJIW_RXuQhQseAhejG7qBmlHULwQi-PeUHXhqX8CmD2V69mgqU1NTO_ZwV4aL0_sz6rvWcxY3OG9NaZvPG6Exh8XuNN7urzyv4sXvUg4ZTazbxNrD2I7KQXvslbSiV_KDcXZSNkkCJgORk0SeTVPYOVB_uJcmIM-3_KhC069ev5aQKz5nWZXZMeesQt1i3Zx2isLzKFf7mnK_8NJud4_O9DAF6to_fHPHy9bYtDF0NVJtFFycF-nm08yqpBfk8jZz7U5fBD-HnDnJULkjKhbqiO938ZFXd4UGE4konCKSQbnjEXanwy_xPW6qCYMqctb3NDlVvkv38VvV4dYN4VfJlkIErbdC6zJBdLEbVysGT8ESQXFB4_dxEWIeGPmrpOPpgSyr_RpavyEjOAwb9iSPCepdMmoOAtfVt92ZDulcIbVgm5EJWwJ42yCr5KnlVoSG6uhoE8Lq6R9xqGKIyNouKsEMEm-DZWR2RSxUVsZpZgEBXTO3YaU5fvpsJxO9JhbPbQomi6jJQeSdPEdWG0dmevNdvk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
واکنش تند چند آخوند به حسن روحانی
@News_Hut</div>
<div class="tg-footer">👁️ 5.11K · <a href="https://t.me/news_hut/69153" target="_blank">📅 00:16 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69152">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c7a509030f.mp4?token=UNMGwj7gC03ZnQrTg7popXZhrS5AznRUEAZUsrsFWwEZm_SFERCy1wMt_8F_6QAqElBt4F5i3BpNc9QCHEGoqtvKKmNelXRPOCWF66EzuH6QhelvMiPmMDiQjBje3FpHJxa1zldTHGj0D0uUMYLGuhe6Gk-vrp1naegnWYt-T6-dr6lHwZlihTjEG9KK9yePGbw18IEAE2ZM3W7y36RIhqBsnM5aJHzpQr_sDDKmIoyReTKAN7LQeIrErYhIQpvFAzilGLjWTwth9h40ZznnfT0r99ZoP86ld4DPUMT6L4g6c62jBuGzeTqou5fKZCjleyYpUQfHLf-fsgs6yApkjg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c7a509030f.mp4?token=UNMGwj7gC03ZnQrTg7popXZhrS5AznRUEAZUsrsFWwEZm_SFERCy1wMt_8F_6QAqElBt4F5i3BpNc9QCHEGoqtvKKmNelXRPOCWF66EzuH6QhelvMiPmMDiQjBje3FpHJxa1zldTHGj0D0uUMYLGuhe6Gk-vrp1naegnWYt-T6-dr6lHwZlihTjEG9KK9yePGbw18IEAE2ZM3W7y36RIhqBsnM5aJHzpQr_sDDKmIoyReTKAN7LQeIrErYhIQpvFAzilGLjWTwth9h40ZznnfT0r99ZoP86ld4DPUMT6L4g6c62jBuGzeTqou5fKZCjleyYpUQfHLf-fsgs6yApkjg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
دیروز تو مرزداران، یه جرثقیل سقوط کرد و این بلا رو سر ماشین و خونه مردم آورد؛
@News_Hut</div>
<div class="tg-footer">👁️ 9.76K · <a href="https://t.me/news_hut/69152" target="_blank">📅 23:33 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69151">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K7bhz2u6bn17WVsRkXKQIX5wh3hh6Wd_-PgDePYxLlmA9vvmwFfgy0kFA8OKZGAalAkEVcSfSHHvzr78ZfKQDLem7dlS-ejM_JQc0Surzjcq5PibnRF8yBVRV59o1a27lVaPc61OhG7ihVcon48vVW1toHcKtRr6H9YzAfEl4drHg_ZNPIMhbruAzcvB5alol22SwCWL7N1G7wiPONlZb6KcLQvca39DGdut73PVd6M6OdT1qh1ZuxXYxGfk06JQvlBMrUbZAwcer067LF2MH-JZfknGCvg5Nc4HU_GYQEaEcxMOMZrJNcL_bJiBl43_mgjdQuGbQPDHAvl3KIRe8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
⏺
اکسیوس:
دونالد ترامپ، رئیس‌جمهور آمریکا، و بنیامین نتانیاهو، نخست‌وزیر اسرائیل، روز سه‌شنبه در دفتر بیضی‌شکل کاخ سفید دیداری ۹۰ دقیقه‌ای و «سازنده» درباره موضوع ایران داشتند؛ دیداری که در آن هیچ‌گونه نشانه آشکاری از اختلاف دیده نمی‌شد.
- تزیپی هوتوولی، مدیر ارتباطات نتانیاهو، به خبرنگاران گفت: «این ادعا که اسرائیل در حال سوق دادن آمریکا به سمت‌وسویی خاص در مسئله ایران است، صحت ندارد. نخست‌وزیر به رئیس‌جمهور آمریکا نمی‌گوید که چه کاری انجام دهد و او را به هیچ جهتی سوق نمی‌دهد. هر دو طرف خواهان جلوگیری از دستیابی ایران به سلاح‌های هسته‌ای هستند و راه‌های بسیاری برای تحقق این هدف وجود دارد.»
- هوتوولی اظهار داشت که علاوه بر موضوع ایران، ترامپ و نتانیاهو درباره احتمال عادی‌سازی روابط عربستان سعودی با اسرائیل نیز گفتگو کردند؛ اقدامی که ترامپ خواستار آن شده و آن را بخشی از یک توافق هسته‌ای با عربستان دانسته است.
- به گفته هوتوولی، موضوع فروش جنگنده‌های اف-۳۵ آمریکا به ترکیه — که اسرائیل با آن مخالف است — در این دیدار مطرح نشد. همچنین ترامپ از اسرائیل نخواست که نیروهای خود را از مناطق تحت اشغال خارج کند.
@News_Hut</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/news_hut/69151" target="_blank">📅 23:05 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69150">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6524c67cb0.mp4?token=ckZkSNOoKvY2rZG7lu6LEAWnSVmlLh0DwAL6SGH622OkKvGnuR1GtMLhoNpYVtGY4GKQuKknQDZy8swwlSVEGN9q7JedgYBXdjuk_3FOmZPUSu3_D0_C-Y2-XsVHpKzjlKHpVwebeP98q-RN8dR3MNudJlW0keK7uXeTt4i113wBLAN_duULKhiNLGbKlsCWosjXqk8j2r68Jk7zQNTQ_FOFZpOLiWQoN0iTS-P98iiT2Ug78Wyid0aZT7XHc4GybvrRkLDKhc1x3ZnsGB3Lp6KViwmAg8GV2PrIL57nklp_GK2spCHAa2iTsuVFsO1h56_Vx9LCy5-pdHTbt9D_7Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6524c67cb0.mp4?token=ckZkSNOoKvY2rZG7lu6LEAWnSVmlLh0DwAL6SGH622OkKvGnuR1GtMLhoNpYVtGY4GKQuKknQDZy8swwlSVEGN9q7JedgYBXdjuk_3FOmZPUSu3_D0_C-Y2-XsVHpKzjlKHpVwebeP98q-RN8dR3MNudJlW0keK7uXeTt4i113wBLAN_duULKhiNLGbKlsCWosjXqk8j2r68Jk7zQNTQ_FOFZpOLiWQoN0iTS-P98iiT2Ug78Wyid0aZT7XHc4GybvrRkLDKhc1x3ZnsGB3Lp6KViwmAg8GV2PrIL57nklp_GK2spCHAa2iTsuVFsO1h56_Vx9LCy5-pdHTbt9D_7Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
پژمان یکی از شرکت کننده های زگیل ابدی تو صداوسیما:
متاسفانه من اول که رفتم تو برنامه نه میدونستم قراره برم چه برنامه ای نه میدونستم چه برنامه ای هست
من اهل ماجراجویی هستم و دوستم اتیلا منو قرار بود دعوت کنه مسابقه ورزشی ولی ساخته نشد و منو دعوت کرد تو اون برنامه
ولی خب باید تاسف خورد چرا این برنامه رو تو ایران نمیسازن طوری که با قوانین جمهوری اسلامی سازگار باشه
اینطوری فرهنگسازی میشه برای مردم
@News_Hut</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/news_hut/69150" target="_blank">📅 22:27 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69149">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn5.telesco.pe/file/0050768259.mp4?token=olxu8Nrga83Wo7VslO7KmfUNyEXk7WLfV1sEF4J4lyV_y5xa0hUkX9EVuETXuN838Pm3ATpQj-t_JlbOvALbZUUCmC_h9QoZYgU7M7OD-wwPCwmOZWmIKEbgO7sI_y2i0QEe4HJwvz7Iaej7qTQeYidT6ebjdldHd408Vv6rEcqQ0oc9puMOUxa3MdJVHCupIPbDye9Rvq8Dp27RBYJiNdw-BQ6zNupWD8fynLQyvfjsGzwlNrKIYR7RzzJY8H-NzgN_iN7wiei59q00meaJ1uGfovWUrheq4n5VSJwWb5_wXyc2UCSo6I0x_f3YTVnDEt2FGbDwLl_YqYSJjuc9Iw" type="video/mp4">
</video>
<br>
<a href="https://cdn5.telesco.pe/file/0050768259.mp4?token=olxu8Nrga83Wo7VslO7KmfUNyEXk7WLfV1sEF4J4lyV_y5xa0hUkX9EVuETXuN838Pm3ATpQj-t_JlbOvALbZUUCmC_h9QoZYgU7M7OD-wwPCwmOZWmIKEbgO7sI_y2i0QEe4HJwvz7Iaej7qTQeYidT6ebjdldHd408Vv6rEcqQ0oc9puMOUxa3MdJVHCupIPbDye9Rvq8Dp27RBYJiNdw-BQ6zNupWD8fynLQyvfjsGzwlNrKIYR7RzzJY8H-NzgN_iN7wiei59q00meaJ1uGfovWUrheq4n5VSJwWb5_wXyc2UCSo6I0x_f3YTVnDEt2FGbDwLl_YqYSJjuc9Iw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇷🇺
❌
🇺🇦
تصاویر بسیار نادری از به‌کارگیری پهپاد «گربرا-سیکر» (Gerbera-Siker) در نسخه انتحاری هدایت‌شونده آن منتشر شده که انبارهایی را در شهر کرولوتس (Krolevets) در استان سومی اوکراین هدف قرار می‌دهد.
پیش‌تر، پهپادهای «گربرا» عمدتاً به‌عنوان طعمه (Decoy) برای فریب سامانه‌های پدافندی استفاده می‌شدند، اما اکنون از آن‌ها به‌عنوان جایگزینی ارزان‌تر برای پهپادهای «گران» (Geran) نیز استفاده می‌شود.
@News_Hut</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/news_hut/69149" target="_blank">📅 22:27 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69148">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromSnappPay | اسنپ‌پی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WcJRossjPrWCF_2utB-vq8DPX---v9i4samIEGNEWxIeIAn-zXh2XL3l6PLdO8WiFx69-BFkq2WBjUmzwePLgwCBbciH3IXmbpjIovUMl6urt8xChM4oWfgJ5Obm8291G_4lnBqR_auR_oVaobJkOcSsDGErJhqJ89igdfpLCMXr-mu1e2xpK59s2ZO5WSWIkClnBAJhXkYZjxQ9ryrgfzn5FNYbU_vxQVtDR3dYskQ1YVPA2w78x8q70hZdp82eYZanLeKdHBU3WNj0pYZShJ_p6fk_zxyAQ2gFIQUcjoV16J44aPiTrxR1Hcn3qeQ-7aMxXkpXSicSjs6t-WsA3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
از برند‌های محبوبت،با تخفیف و ۴ قسطه خرید کن!
😍
🤔
می‌دونستی می‌تونی از فروشگاه‌های فعال در شبکه‌های اجتماعی مثل اینستاگرام و تلگرام و سایر شبکه‌های اجتماعی، با تخفیف خرید کنی و هزینه‌شو در ۴ قسط با اسنپ‌پی پرداخت کنی؟!
🤩
🤩
کد تخفیف ۳۰۰ هزار تومنی: PAY3SCP
⬅️
از طریق لینک زیر لیست فروشگاه‌های طرف قرارداد با اسنپ‌پی رو ببین:
👇🏻
https://l.snpy.ir/v06dj
https://l.snpy.ir/v06dj</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/news_hut/69148" target="_blank">📅 22:27 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69147">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/04ca836fdf.mp4?token=kqfyNLZz3s8e7SS__MER8a3cWGqbXfw3EVTvou_rT8XTdBAcQqWgsT0Ai9teNV7B2aEQJTXLAjI7dae0gHM5kUHA9RON2AfP296Cj_zj_p8ZzeZ1BININqew7qBPA8AMgptldMTL8gXSdrso4cKPi5jnVq94flk4OPDZazrmXwZ9EbP_XVC6aY5LwYvTRECMRL3L1CRSkMisO95QwngAz2pk-es1rxqto0GBR4uL1L89Chu31vJbLC-Dv2HdctgBP32D5h9BsmY8qVkO79M4cT4QhJvT9eQ2yMbvQ_QKAq5wuDXRidr8q2v8J9ffwaHkNmL01po3xsTCGzQ1TGtAWw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/04ca836fdf.mp4?token=kqfyNLZz3s8e7SS__MER8a3cWGqbXfw3EVTvou_rT8XTdBAcQqWgsT0Ai9teNV7B2aEQJTXLAjI7dae0gHM5kUHA9RON2AfP296Cj_zj_p8ZzeZ1BININqew7qBPA8AMgptldMTL8gXSdrso4cKPi5jnVq94flk4OPDZazrmXwZ9EbP_XVC6aY5LwYvTRECMRL3L1CRSkMisO95QwngAz2pk-es1rxqto0GBR4uL1L89Chu31vJbLC-Dv2HdctgBP32D5h9BsmY8qVkO79M4cT4QhJvT9eQ2yMbvQ_QKAq5wuDXRidr8q2v8J9ffwaHkNmL01po3xsTCGzQ1TGtAWw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇱
نتانیاهو:
من همین الان یک جلسه عالی با رئیس جمهور ترامپ را به پایان رساندم. وقتی می‌گویم عالی، این فقط یک تعریف ساده نیست.
گفتگویی با مشارکت کامل، با حمایت متقابل، با درک هدف مشترک اطمینان از اینکه ایران سلاح هسته‌ای و همچنین اهداف دیگر نخواهد داشت.
یکی از بهترین گفتگوهایی که تا به حال با رئیس جمهور ایالات متحده، دوستمان دونالد ترامپ، داشته‌ام.
تمام تیم ارشد او و همچنین تیم ارشد ما آنجا بودند و در اینجا نیز فرصتی برای تبادل نظر و همچنین هماهنگی مواردی که برای امنیت و آینده کشور اسرائیل مهم هستند، فراهم شد.
@News_Hut</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/news_hut/69147" target="_blank">📅 21:52 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69146">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Qd3VJf2AHOds4t5Y6OqXwn8igGQQjXeC5ulU6ftmOAR7t6pi-tyUEYTf_DqzsjpHhOfVa61WxPM_p_g9-rguNjNqrhlDniKpNL-VA4baS3NUkPuD01P6xKwZ2YoR2yvxrGahVwHmRjvSU9yyZe4KHVljKxkleKR60vRz0Ov3b4TDHV160jq-tfZph4lV7CDTzYxEJ5yQShj6_NGv2RXuPXnbe-qfsi-OH3eUGykmbpVRodx27RKal97SBe-DhgXnEge6iDu1QamrVWy3luXVyPTY8T60_qtN-BkB482o5Ic-nKYaPKleb4BAnvHP4ieVBK88jf6DIBzOCBMs92rQGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
⏺
علی قلهکی: مراقب باشید پاسخِ احتمالی به اوکراین، کل اروپا را همراه با آمریکا علیه ایران بسیج نکند
به یاد داشته باشیم که ایران خبر اصابت کشتی خود را رسانه‌ای نکرد و این کی‌یف بود که خواست آن را منتشر کند! حال به چه علت؛ درگیر کردن اروپا در جنگ با ایران یا پیوند زدن پرونده «جنگ روسیه_اوکراین» با «جنگ ایران_آمریکا»؟ شرایط پیچیده‌ای است
@News_Hut</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/news_hut/69146" target="_blank">📅 21:31 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69145">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">🚨
🇮🇱
یک مقام اسرائیلی:
ترامپ در دیدار خود با نتانیاهو، خواستار خروج اسرائیل از هیچ یک از سرزمین‌های تصرف شده نشد.
@News_Hut</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/news_hut/69145" target="_blank">📅 21:21 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69144">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bT1NRc_RjsXBMseCDrrznSjALBWXozTYvD9dsKPHMQUgAQqK8tLvE2l9nqijdKnHWajGHuSZDAmxLFvu0MUYO46UfMzPMqfwtnX-OF-BbP48ud5qCGpC5v8nnxNV1PY6zwnNcyxch8Nx-ao93ICKONA_iX9tYa6VINHc1SM5LVJSu5DY4gyLa1Om39tfkSHRNJq2MjwKTBly06kahkTOs5CltQwnvNAOc-LiplDsjwG9u6vh5hrMdzMJPt_pdRMpY9FtP-4Zo8AZTbSqWUXs69461c9I5-6pWIyAZf8-q1gmZwxgBwvCmhs3x0DnQrAsjJ0iULsgvOiN2EKmIBoHkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
یحیی سریع، سخنگوی نظامی حوثی‌ها:
نیروهای مسلح یمن نفتکش غزال متعلق به عربستان سعودی را به دلیل نقض ممنوعیت دریانوردی و نادیده گرفتن هشدارها با موشک‌های بالستیک هدف قرار دادند و این نفتکش مجبور به عقب‌نشینی شد.
@News_Hut</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/news_hut/69144" target="_blank">📅 21:14 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69143">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aFoNV80J59si8gH975sWja7wnBr6HdwRB62NoyPe7BHd41oVW-QgUhdAqxhZj-wMkGO7ipw0nLFDjZSLwmIUZgXX19D4euO7LhQm4f89lA61h_lp7gOZXLgSGDrRyV7vv4l8JwEK0mchC0Wnau9M0yH_aMbB0QR1v-cNyHyl541udJVt-vrLgGGW-HckQ-5d94jloK_QUyzimvC8JmkcItXEzi7ABnMuwe4cgkgqCfKJH-5doeGZ0Y0GzrftCJDEnDQSALmbQu8sgRNbyrp8__KHMhHHgPyhouP3WqGlY_KrrugvlwvvNVIbtlewNOfIXPHoHHRtTEgwzrMbKMAnvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✨
آمپول لاغری زیکورپا(
®️
ZCorpa)
؛ وقتی درست لاغر شدن مهم‌تر از کم شدن عدد ترازوئه
در لاغری با آمپول زیکورپای عبیدی، هدف
کاهش توده چربی بدنه، نه از دست دادن عضله
.
📊
مطالعات روی تیرزپاتاید (مولکول موجود در زیکورپا) نشون می‌ده:
✅
منجر به کاهش وزن بالای ۳۰٪ می‌شه
✅
عمده این کاهش وزن توده چربی بدنه و سهم کمتری مربوط به از دست دادن عضله‌س.
✨
برای
شروع لاغری با زیکورپا در کلینیک ویهان
، پزشکان ما به صورت رایگان شما را راهنمایی می‌کنند:
مشاوره پزشکی تزریق زیکورپا
کلینیک ویهان</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/news_hut/69143" target="_blank">📅 21:14 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69142">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">🚨
⁉️
کانال 12 اسرائیل:
دیدار نتانیاهو و ترامپ با حضور تیم‌های گسترده‌ای از هر دو طرف، یک ساعت و پانزده دقیقه به طول انجامید.
یک مقام اسرائیلی مطلع از تدارکات نتانیاهو گفت: «ما در مقطع حساسی قرار داریم.
رئیس‌جمهور ترامپ به‌زودی تصمیم خواهد گرفت که در کدام طرف بایستد و چه مسیری را در پیش گیرد.»
@News_Hut</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/news_hut/69142" target="_blank">📅 20:56 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69141">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W_vpNPdi1bar7Cp9v29IZsx5RAV5K9_3LO7hijc7PXuqaftRfccDZCS2ZTZiJhOJGrM1A9nRpbJ3fIrSMHzagXu8dt1JHnUb9FhGm-i-pN037xsRnUvA5T6kkRCbqBrXV5WAkGiN8N32P7JL86SOCdJZg8Sz_Ai59nYjzLcG1yUg2ZxsP_a-rpJ9eOwk_Nwe-86R_yZN9CS_tkih51jZ94QgOk9qaLvhGfU0eUnV2QZKPP1ykx3OSQY-q9-nNZ8NpsVAl8s2JPmmMUwVrJyliIkjFScpdn9vrcTnhHF1yxMp6GVzeGpIoVy8jbHpYR1yXL_U6j7wqa7_sXQ5nFNoFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇦
آندری سیبیها، وزیر امور خارجه اوکراین:
من با عراقچی، وزیر امور خارجه ایران، برای گفتگویی صریح تماس گرفتم.
من تأکید کردم که هدف ما جلوگیری از تشدید غیرضروری تنش است.
من مجدداً تأکید کردم که تمام اقدامات اوکراین صرفاً با هدف دفاع از کشورمان در برابر تجاوز روسیه انجام می‌شود و هرگز قصد هدف قرار دادن کشتی‌های غیرنظامی یا مردم را نداشته است.
@News_Hut</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/news_hut/69141" target="_blank">📅 20:46 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69140">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/001cd370db.mp4?token=me7a7rdBIhEYdc_qc75hGgenjXYMZbxy1RLWd6zettnmhDrOxeax_XfvHWEhEGysYWebV0nTrNXUIk1YdybXes7UzrQ56LVpt20DDZyDHZ4khjBpX-2OhTYfdAk8k-LnVGe4I_KQ7muQuVdO49CKwdfY9u7cl0adBfD33TioxPLOBh-MQyy2GqoYMOq5EkGW1nPKu8XmimVaCi2rzgGGkpGu8A95fFl50NP4g3WADBqIDSR1Q42vOeBpWRz4QMMz5L9d9iVkdOi33Y2yLhHLmkPDemiCEGk6Z_AGRtbftAxyW9McFg4xJjnagyFcNXuBHIgU4n0ly2xH1y7Wv_YRSQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/001cd370db.mp4?token=me7a7rdBIhEYdc_qc75hGgenjXYMZbxy1RLWd6zettnmhDrOxeax_XfvHWEhEGysYWebV0nTrNXUIk1YdybXes7UzrQ56LVpt20DDZyDHZ4khjBpX-2OhTYfdAk8k-LnVGe4I_KQ7muQuVdO49CKwdfY9u7cl0adBfD33TioxPLOBh-MQyy2GqoYMOq5EkGW1nPKu8XmimVaCi2rzgGGkpGu8A95fFl50NP4g3WADBqIDSR1Q42vOeBpWRz4QMMz5L9d9iVkdOi33Y2yLhHLmkPDemiCEGk6Z_AGRtbftAxyW9McFg4xJjnagyFcNXuBHIgU4n0ly2xH1y7Wv_YRSQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
غریب‌آبادی، معاون وزیر امور خارجه ایران:
ما در ۱۵ روز گذشته هیچ درخواستی برای مذاکره با ایالات متحده ارسال نکرده‌ایم.
برعکس، آمریکایی‌ها خواستار گفتگو با ما شده‌اند.
آن‌ها همچنین پیامی از طریق عمان برای ما فرستادند و اعلام کردند که هیچ‌گونه اقدام نظامی علیه ما انجام نخواهند داد.
@News_Hut</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/news_hut/69140" target="_blank">📅 20:31 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69139">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W5CNlrwVWJWkb-7uhQcbASBHQ3TLpJVpKThZKxyEgm0C5o1arqBT6vA0BwG0MSvbz3mlDU8nIWvKgRPO1u44De7Rvp5nCJc6NPP5yuejFtiDDTezPW8klrzXhOGsrfborG4iFHOqOs_Lu5fCQw1vfd1j8P8wzGCEMIY_YWBiajzYt-93NelY6YiMNBKL6bWRkvTZLpFrPVDuTr2kD0qWBAAlAajxQC3WEYTZXEY4Q9VSih55aBTfEVQuFknsRx2IXQH2BTXT5g11ry8uxKShgI1d6LOcy8IBIiqLq0pSd9R5Ppk_ydcCzpRSh2uX6gkySdxccazQCNVjSXgk37r9kQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
سخنگوی کاخ سفید:
رئیس‌جمهور ترامپ دیدارهای خود در دفتر بیضی‌شکل با رئیس‌جمهور زلنسکی و نخست‌وزیر نتانیاهو را به پایان رساند. هر دو دیدار مثبت و سازنده بودند!
@News_Hut</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/news_hut/69139" target="_blank">📅 20:17 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69138">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4dcd737689.mp4?token=VXFpKoDg_Pl-TY5xwhoNoROekeyW5wiYjC8wUQ6cpQFwPWXnSnCJe81Mmz3uy9-0G_lPCeGj4cY_9Vi-Z06VQYuoQUYYhketzrYSXaKGYdG0s7HX1EO6Akx_1AX6WK8LVfcgLKVwPDwjD64U3fevEZ13J6kdHdcdTjZqG7SLXVuX0J-GusOCz7UsTSX7j5kNozteR7yHKtVixjFFHIDZ2pv30PC9y0nrveqbfuHY6THnZFMU5Os2BqQcqXUZTIRFNzZq27vBnSnSXHEVWgmzW2sVAP629GfHgQXYOWAQ9ANJU9vFh4RjBY-yVsAzLRmoSSYn3MnkNLPer6oSEuPp0w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4dcd737689.mp4?token=VXFpKoDg_Pl-TY5xwhoNoROekeyW5wiYjC8wUQ6cpQFwPWXnSnCJe81Mmz3uy9-0G_lPCeGj4cY_9Vi-Z06VQYuoQUYYhketzrYSXaKGYdG0s7HX1EO6Akx_1AX6WK8LVfcgLKVwPDwjD64U3fevEZ13J6kdHdcdTjZqG7SLXVuX0J-GusOCz7UsTSX7j5kNozteR7yHKtVixjFFHIDZ2pv30PC9y0nrveqbfuHY6THnZFMU5Os2BqQcqXUZTIRFNzZq27vBnSnSXHEVWgmzW2sVAP629GfHgQXYOWAQ9ANJU9vFh4RjBY-yVsAzLRmoSSYn3MnkNLPer6oSEuPp0w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
نایب‌رئیس مجلس:
نباید به ایالات متحده اجازه دهیم هر زمان که مایل است حمله کند و هرگاه با مشکلاتی مواجه شد، عقب‌نشینی نماید.
اصلا نباید با آمریکا وارد آتش‌بس شویم.
آتش‌بس با آمریکا معنایی ندارد.
@News_Hut</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/news_hut/69138" target="_blank">📅 19:55 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69133">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LXAkiY75luyi5wJMK5BHo2Kjwt2EtZRsvBmQtKWwSONFV07v1kXA-l_cF7XKjxHtdve_8rALHV53u0YVqzFV1m1ErggGEJYpuKPKXI2zwyUTL_XhGpIRpvFgtSjNCQoSWjZaMmdRhHsRSP9Ivt4e7NOuHNyN4jv6qTxpSGfcvybyOGkbIVg0LyuKiypNkbSFHAI1zgPB6UAGDaJTV_ltEXBbT2zp1Fqp93283y5aEWwWB8nrhp1X29MvQ8yziXimdYlekxOnnZtqRMBOKbP180Sh3PWu_HcV_lyAi5kRUDuWZEgbFBQmKrXEo45LR6S-1_8OOdT413OYKK_3UtU2XQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GG5IqvMM2cHc4AVjR5ot2hfbSteYgrHZsOE80pMshCKiqcpxz2587sN6TSkswhQ2e0jGhTITgaNxymd2BuGVzyhLgxqLWHlY2JhWSsCFAnK2gdoyR4RyoIs1jD-3H4pArntdO-_0-ck89DXKjUFk90E6KbwMy9d8C0qwroeIWp8ONawPWe0mgYZ_Soe4AJ88KAf2BhvNqkSWQgZomjXS_Ky4Gvjidus_2C6RSW0VSILrC2BA934jW34Z9UCqxFPnuefbWxl1TepCJ6IykDwPoSS0E-dC6hOKHRe7h89gbhZwb0H_vAFMcJFA_5n-sBnk7CERAN3FnKqhHf2-KI3iOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NokYCFgi3cZfUO9EJ-vUh6XiSurSBIVnmvCqjTUInouHcQXswzwMp3THw35X0NlcDXhOlXt48genrQxWoWcTrBNAogX_Y4whI6IQB3xTox8OBZUishnVf84T6ZcWdDI5Xf2btXqZmoPOcoGKswpVHrEVC0-WMMhj_1CjcK16wTRDTWpcey4W7SExv3TYrFVptpjEJigo2icYtuxJndTZ0z0VRB_pAOFsB_mHcEela5GhM0wmKJwDJrBkY3ws1nSjY4Gm6EUGJSzHdV5XsrzkeVKWfw46WbzRE4mqqyOlIQO2MbHvuS4jCY6IPn9K9DkmSusyLPqWzoFXP8szBa8ttw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZGAECeL2tBt-oLCGYrrvaTKpWfPdb2gn1pYVSzbhFKXWhk9p2blQ8keDDGNwTAHNqFLz1PUyj5FpEYL2lFLj-ru1L69wMJbxWx-xY7bXUmwIoSHUHGMBr2_cTusPEXYuO1gZBBbsP2x8rseDP-OyUGfFFCzIHMANgfRpHNL2CQO0qGGyJtabfL-8IletdLyS0TbLBbRYB37oOIiAJ0bzs22rj2og77VZI0IXTZNlWEFQ51DvnHJcnW8_fZBNrRUlezxaK6hyb5zqkhXGTA2vPlBFhR-96VCciSFoO5DKpY51EW-95OalcORFL2vS6BFJBKELawgJ9SST6HjTVmhvEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/phX78U6n2bxjwRoDbD6iqE2mgLc-ZCvaVfvraJFCdjcgwZ1T8obkcDqLq9N4Bxkre9FgPPjYaXSA3paFXoU-6OPu0CzbIsG2WqI4YZkQvwupz5EZ_jZ-WmDfAbdeGex0cpmhqW0HueBTEfhKj8OYOWk-lbfZP3VXN58s_k7whhWKCcIeg3k9mTKirUm0oppr2w64SRVHbXXbmHXkODQzE5c8tuG3JPJCOmaOjEqbNYcJNtmfyS71mWXgZLcnR0HtYmdqJTHlOh_cY_Y2lijbiitCos6vfkfS9WxCc-VAgpM-ki4dvEGQhlR64Zhymc1hMUYZSZ4k-44HrcN52hzoiQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
🇮🇱
🇺🇸
تصاویری از دیدار تیم نتانیاهو و ترامپ در کاخ سفید:
@News_Hut</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/news_hut/69133" target="_blank">📅 19:38 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69131">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cUQZuPUp_u6cDaC8h1PoaT3RD_9woxt3f910SgM3b2w34wVcGa01kijLNkwgLZIdaMVbDqdaaYj_LimZtto00oCovgG8Ngg8mBD5n2CJYUYHt1-kXEuFkiHfpvVB2Xr3bHkPbSE6RX2e7BbatdpwACS-ASHXoA8F0SwGBWTFsZ2IIU3lZB4P_y_NlhlEcx_RxPXFzFNbpITsn71pjZgF1M3vyYxNSzz7xJ2OmFrJlcKDY94heDS7zP3vZVwRwycoxTIofC3VWtamoKxqVL2L5arjip2BOI684wzqksIcfoxLxVbnGY6SL-GH7y_gMabsaCBhJFtbFbuVwFQxCfiZ5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uRp7ufrHeulCktDj6jGZX1nwcqSfP-ySPqORieEtf2lb7uzngO5GKkT8euRoeQ3CF-2-hQifNXb6M6WBH_l6H_XVLDXyi8NVejwFXpwQ4D1zS5C3ibLjzpAuDJDzhQSSe2EPwlXVt8OUWe3M4p0IqU29BKRcJgw4qM9spJVM6QdcjmzmdugvblPITqj9qMQqSnzbZnF08r4eMvFBMHzic7UW3y60hd8lD2m-Rzki3bz7IwA3H93hRjoRWojCk4hkABNlYrAPSO1UH_hoYelPtrC--jpWBpAsT8UkS32dK3susghMEfPuJnouQSRheRLX7298PzdD6zs7C26HoQXJbQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
بنیامین نتانیاهو، نخست وزیر اسرائیل، پیش از دیدار با رئیس جمهور ترامپ در کاخ سفید، با مشاوران خود گفتگو کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/news_hut/69131" target="_blank">📅 19:16 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69130">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6822c0ad1f.mp4?token=v8VhkkP1AKZbkS5owWpsF8BRCC_TfmmM1_22W4wKn5rCHQF74_TgDIPgk66jUBWUDOTwe1looVWfNGrlJSVyvItdELw16espPH850e4uk0YUs_CvFN3HDDdJrdeb4XuQZmhlk2E8yet4vPdCUGUIKoRveB1X6fWqmCUXQspsSLKwTn7Lj3K48oHQA0zfr83NZJOTzDdrBOiTAftf3c1z0-60T0EUgFFIiYcjRszCjcus9ucus0US7y6lU2zGaVoghy58SuNno7gOffOe6Pyt88z3TEFNUtc0sNAxAQ_11n6DSXT73btxUBwthOMYJDS1-SEUOMZDphKFGvL7XGNz2g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6822c0ad1f.mp4?token=v8VhkkP1AKZbkS5owWpsF8BRCC_TfmmM1_22W4wKn5rCHQF74_TgDIPgk66jUBWUDOTwe1looVWfNGrlJSVyvItdELw16espPH850e4uk0YUs_CvFN3HDDdJrdeb4XuQZmhlk2E8yet4vPdCUGUIKoRveB1X6fWqmCUXQspsSLKwTn7Lj3K48oHQA0zfr83NZJOTzDdrBOiTAftf3c1z0-60T0EUgFFIiYcjRszCjcus9ucus0US7y6lU2zGaVoghy58SuNno7gOffOe6Pyt88z3TEFNUtc0sNAxAQ_11n6DSXT73btxUBwthOMYJDS1-SEUOMZDphKFGvL7XGNz2g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
مدیریت بحران تهران: این بلندگوها و سیستم های صوتی که نصب شده آژیر خطر نیست
اینارو نصب کردن برای پخش صدای اذان و ما برنامه ای برای اژیر خطر نداریم!
@News_Hut</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/news_hut/69130" target="_blank">📅 18:51 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69129">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ftwsFxVwleQcskwNppCq4G08gg9wjj0qCQVtJXsHDzwsKP4pXMy7krsjXYvN0iKL91oWJmvzskRsOW9vlpZRE5vkIZ9JVmm5MOt9xZ7MPxDqf84Fr3CXZ8Joyh6iCJTqmJpwBLz9dkV15XvvNc7IbDW6NK0b0BGxTjT-m0Ty4NoarlNu2KtJcl6sMQsnKo7K8y24SOGM1ZDyYj8yXG7NqATPMvrfjPXw3WkKszarh3myJVxWDzDBhl7qdLOyXlkpY8N6i7zh8qvYn4Sr26U0t6WywrJ9nTl9CHhqfL11qxn82aSHjFcsCZckiaOIOon_m1nxz0DSEwf__iq6BsUkzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇱
تصویری از ورود نخست وزیر اسرائیل، بنیامین نتانیاهو به کاخ سفید
@News_Hut</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/news_hut/69129" target="_blank">📅 18:37 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69128">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">🚨
کانال 12 اسرائیل:
دیدار ترامپ و نتانیاهو دور از دوربین‌ها برگزار خواهد شد.
@News_Hut</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/news_hut/69128" target="_blank">📅 18:34 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69127">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">🚨
دیدار ترامپ با زلنسکی پایان یافت؛ دیدار با نتانیاهو در نوبت بعدی است.
@News_Hut</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/news_hut/69127" target="_blank">📅 18:30 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69126">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8339055d6f.mp4?token=pLOV8syThoreSyXQAUwurIp4OBWjwqcq6OJ3vkGVCX7xI4n7E1LxVOLvM1GXDMnflIjHsZ0RuhpHB3ttCEaueaB2aAihFwAofZ3G19TTjl45556EV-cCDAnO5V5oxlfSX594HQq4cOKkZehfXv9jUaZE2wLnQ7_UqTaUG8kgxf9scCSJ03lpgA0kdBgYsdp9jELOQnGyiAiaAdvYeXmASAJox_eKaL3dwPvk_KHKc9qchGzHXOw2bSCdx4Aqdo0gyUARgTg72uXq7lXrQVrQHKywBcRsFDv47p_vGg7929hr9frFBeTg1g-lYwSM8WQsX_-Z1jgsaSUYL1T2d-gpIQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8339055d6f.mp4?token=pLOV8syThoreSyXQAUwurIp4OBWjwqcq6OJ3vkGVCX7xI4n7E1LxVOLvM1GXDMnflIjHsZ0RuhpHB3ttCEaueaB2aAihFwAofZ3G19TTjl45556EV-cCDAnO5V5oxlfSX594HQq4cOKkZehfXv9jUaZE2wLnQ7_UqTaUG8kgxf9scCSJ03lpgA0kdBgYsdp9jELOQnGyiAiaAdvYeXmASAJox_eKaL3dwPvk_KHKc9qchGzHXOw2bSCdx4Aqdo0gyUARgTg72uXq7lXrQVrQHKywBcRsFDv47p_vGg7929hr9frFBeTg1g-lYwSM8WQsX_-Z1jgsaSUYL1T2d-gpIQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇦
🇺🇸
رئیس‌جمهور اوکراین، زلنسکی، امروز صبح به کاخ سفید رفت تا با رئیس‌جمهور ترامپ دیدار کند.
@News_Hut</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/news_hut/69126" target="_blank">📅 18:08 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69125">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/634ef5a127.mp4?token=iZBbDQWr-Cq3xoiYvkPaahd5V80n5x_-4oYdo7ydgcV077oeQcU-hZub3viSak5z2algtZ8Oi4IbiNRaDyK32RhfUnAZ-0BI4XnlytVowiTZiLoxY_aYI4sV17SiURdHcdEXqmb-i37MU0k04eSTc3RbHs-BOsGYICVN79Gi2ValnfHNcPZYEnbRwr4WkiITliRRhIHqH1yPUf70sBfwZts2Pnl7XeiU1Qc-ZGjvt92r6DEZ2MLb2b0pA35c-kLKHUcgdSllzKCKR3YuOLSoJVCDStBht4WU3i8fEDM1VP8-rWq4yqt7w4NJWpcmFnJ2WDy5Xe6KKGAq5YBX7z4eSA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/634ef5a127.mp4?token=iZBbDQWr-Cq3xoiYvkPaahd5V80n5x_-4oYdo7ydgcV077oeQcU-hZub3viSak5z2algtZ8Oi4IbiNRaDyK32RhfUnAZ-0BI4XnlytVowiTZiLoxY_aYI4sV17SiURdHcdEXqmb-i37MU0k04eSTc3RbHs-BOsGYICVN79Gi2ValnfHNcPZYEnbRwr4WkiITliRRhIHqH1yPUf70sBfwZts2Pnl7XeiU1Qc-ZGjvt92r6DEZ2MLb2b0pA35c-kLKHUcgdSllzKCKR3YuOLSoJVCDStBht4WU3i8fEDM1VP8-rWq4yqt7w4NJWpcmFnJ2WDy5Xe6KKGAq5YBX7z4eSA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
سخنگوی قرارگاه خاتم :
هر شرکت یا کشوری که از دارایی‌های بلوکه‌شده ایران پولی دریافت کنه، دیگه اجازه عبور از تنگه هرمز رو نخواهد داشت.
همچنین به ترامپ هشدار میدیم که هر کشوری که از پیشنهاد آمریکا برای استفاده از دارایی‌های ایران استقبال کنه، شناورهاش از این به بعد اجازه تردد از تنگه هرمز رو نخواهند داشت.
@News_Hut</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/news_hut/69125" target="_blank">📅 17:56 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69124">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a9cd6b53c3.mp4?token=MBlN6ms_QQRUs_M25wut96uEaWI_NmEFD1tva9gGZeGI1GDNOB_7NXg04FdUqruiEY68URAZSqDc-n4mgwkaGJHaYouurM6XX8KmWXEdCltRGY7Si49bhkfKa_Tull1XhPW-tmfXl_6_aUtoo-pAeFGuGwrhXwRUaGJ373zk3PRl42VR1VZ1YPLNGSkqqLXcfxaXXYoE120TyUxGuA_X-0R2_q71zRuAUQbsHBEKMRu4vRwI5uZv_dOW7yJVPE25wTbMPMsvrX1y9Gfv6OTNS1sxdsm-NBCDeBrK9UWsG7JFlI0RFjyjlibzHJrtpljGsvhXeQm7053aCg1scaLnPQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a9cd6b53c3.mp4?token=MBlN6ms_QQRUs_M25wut96uEaWI_NmEFD1tva9gGZeGI1GDNOB_7NXg04FdUqruiEY68URAZSqDc-n4mgwkaGJHaYouurM6XX8KmWXEdCltRGY7Si49bhkfKa_Tull1XhPW-tmfXl_6_aUtoo-pAeFGuGwrhXwRUaGJ373zk3PRl42VR1VZ1YPLNGSkqqLXcfxaXXYoE120TyUxGuA_X-0R2_q71zRuAUQbsHBEKMRu4vRwI5uZv_dOW7yJVPE25wTbMPMsvrX1y9Gfv6OTNS1sxdsm-NBCDeBrK9UWsG7JFlI0RFjyjlibzHJrtpljGsvhXeQm7053aCg1scaLnPQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
پرزیدنت ترامپ:
«ما محاصره رو برداشتیم، اما چون اونا توافق رو زیر پا گذاشتن، دوباره محاصره رو برقرار کردیم.
اونا مدام توافق رو نقض می‌کنن. دیگه نمی‌تونیم اجازه بدیم به شکستن توافق‌ها ادامه بدن.»
«ایران تنگه رو کنترل نمی‌کنه؛ ما کنترلش می‌کنیم.
اونا شاید بتونن چند تا مین دریایی بندازن و اوضاع رو به‌هم بریزن، اما کنترل تنگه دست ماست.
حتی یه کشتی هم بدون اینکه ایران جلوش رو بگیره از اونجا رد نشده.»
«وقتی قاسم سلیمانی رو از بین بردم، ضربه بزرگی بهشون وارد شد. به نظرم اگه اون هنوز زنده بود، ایران جور دیگه‌ای عمل می‌کرد. حتی ممکن بود به سلاح هسته‌ای هم رسیده باشن.»
﻿
@News_Hut</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/news_hut/69124" target="_blank">📅 17:38 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69123">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/803209f6c9.mp4?token=DB9cLRFefIRcFusophq65Xz22ou2blueKW8_YLIVgsnsWPkyz7VEAnmV_gx4RFWWyyyiJnzxBfxQlroCMwmGApxx0X1o3UKScGSO_Yw8NfV6AhPV7QEbrbSzx3PgKIcsThRBqhgKJRSXFUyg2WZE-yTSc4ylstTSV9JYgAMSRlYcpRn1ETUlIvl-Zvjj0DX5LBhH2Hpe2_NXdQhdq8OdDocXZTbSFPqugqCLVP4zmNIEZ1apIvFYeL02RZVFHxR0qaO8WQvimY940Y0j2mnJoNSlfTo8FPJPf20ciM8OovwaThfd0_NR6HvI5kFz9NBhJVlluuuK4UuH54E4ANUDQg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/803209f6c9.mp4?token=DB9cLRFefIRcFusophq65Xz22ou2blueKW8_YLIVgsnsWPkyz7VEAnmV_gx4RFWWyyyiJnzxBfxQlroCMwmGApxx0X1o3UKScGSO_Yw8NfV6AhPV7QEbrbSzx3PgKIcsThRBqhgKJRSXFUyg2WZE-yTSc4ylstTSV9JYgAMSRlYcpRn1ETUlIvl-Zvjj0DX5LBhH2Hpe2_NXdQhdq8OdDocXZTbSFPqugqCLVP4zmNIEZ1apIvFYeL02RZVFHxR0qaO8WQvimY940Y0j2mnJoNSlfTo8FPJPf20ciM8OovwaThfd0_NR6HvI5kFz9NBhJVlluuuK4UuH54E4ANUDQg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
پرزیدنت ترامپ:
«اگه من رئیس‌جمهور آمریکا نبودم، امروز دیگه اسرائیل وجود نداشت.»
«اوباما فکر می‌کرد می‌تونه با دادن امتیاز و پول، با ایران دوست بشه؛ اما بعدش رفتن دنبال توسعه برنامه موشکی و هسته‌ای. طی 50 سال گذشته، همه رؤسای جمهور آمریکا یا کشورهای دیگه باید یه کاری می‌کردن، ولی آخرش همیشه این آمریکاست که باید وارد عمل بشه.»
«اونا عملاً قبول کردن که سلاح هسته‌ای نداشته باشن. فقط مونده این توافق رو به‌صورت رسمی نهایی کنیم، اما با اصلش موافقت کردن. چرا نباید موافقت کنن؟»
@News_Hut</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/news_hut/69123" target="_blank">📅 17:36 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69122">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">🚨
🇺🇸
پرزیدنت ترامپ:
«اگه دوباره برگردم و بخوام کار رو تموم کنم، همون‌طور که بعضیا دوست دارن، خیلی راحت می‌تونم تو کمتر از یک ساعت بیشتر پل‌های مهم ایران رو نابود کنم.
ساختن یه پل حدود 10 سال طول می‌کشه. پل‌ها سخت‌ترین زیرساخت برای بازسازین و بعد از اون هم نیروگاه‌ها قرار دارن.
من می‌تونم ظرف یک روز همه نیروگاه‌های برق ایران رو از بین ببرم. اون وقت حدود 91 میلیون نفر بدون برق و بدون پل می‌مونن. برای همین این یه تصمیم خیلی حساسه.
اونا می‌دونن اگه به توافق نرسن، من این کار رو انجام میدم .
پل‌های اصلی واقعاً از بین میرن؛ فکر می‌کنم تو کمتر از دو ساعت بیشتر پل‌های مهم نابود میشن و نیروگاه‌ها هم ظرف یک روز.
ولی اگه بشه از انجام این کار جلوگیری کرد، ترجیح میدم این اتفاق نیفته.»
@News_Hut</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/news_hut/69122" target="_blank">📅 17:33 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69121">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a44e71f50a.mp4?token=DL5h9EQJPyEKJdZWF3Qv-VByX5yBWpfH5rGCkmgF6xThHL_A7qkeDjyjA82ZCQ-2HtL7iGhRAwYv8pcWJ0UmiM6VTQ-CxFwdo9EkvIJmZzni-bCBh447R5UFhWBUF27_vJHOR-0_2ITNp_dkTvQmZe8HL9CD2NnxGC-y9XcqCa47tpw9edERaGe9K2NL4taY9M9xIGKp9jDe86QY6nHqh_5NC40APVtQTjce2H__ImC2Lq5cg4wV_M4FIV8HT74GD8a2Omi-2ScO-NeJfVWKy4juV2ursnMPe4wPCRyyFBOhwcxaZSt_K19eqNPDYaFh2xPNWCtxaPVkGsfzD9HjpgTkuKV37t9AvWA7J1GaFNigv-mBIxcK007_XOud4kgldmUOcvCBVnK_Snr6M5gEPcDyJ_Xd7EDsyhnpVMrPgAls4gl3b9DjVLfcWLmR89ehEKNV9Mmw2oLhB0tuc4mie-zjjHql3iroTU8Al2aVCFF65iWD1HzU5y0rYGerPxWPjrsFoDtcd2wYaZqJluTEpRUyQiYh5fG8pAFguwt1vxNqdfe66_6WTn9munsSjLybOE-lhniyUDGmNVGGTWUsh-6zlPzPLdmGluwtyzANxVHXKL5pKLCCkUuJ-P0BTiKVSWqll56tYwiE-2S2AfLSyG7LorhJ0ctPTSJ66DIjZsU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a44e71f50a.mp4?token=DL5h9EQJPyEKJdZWF3Qv-VByX5yBWpfH5rGCkmgF6xThHL_A7qkeDjyjA82ZCQ-2HtL7iGhRAwYv8pcWJ0UmiM6VTQ-CxFwdo9EkvIJmZzni-bCBh447R5UFhWBUF27_vJHOR-0_2ITNp_dkTvQmZe8HL9CD2NnxGC-y9XcqCa47tpw9edERaGe9K2NL4taY9M9xIGKp9jDe86QY6nHqh_5NC40APVtQTjce2H__ImC2Lq5cg4wV_M4FIV8HT74GD8a2Omi-2ScO-NeJfVWKy4juV2ursnMPe4wPCRyyFBOhwcxaZSt_K19eqNPDYaFh2xPNWCtxaPVkGsfzD9HjpgTkuKV37t9AvWA7J1GaFNigv-mBIxcK007_XOud4kgldmUOcvCBVnK_Snr6M5gEPcDyJ_Xd7EDsyhnpVMrPgAls4gl3b9DjVLfcWLmR89ehEKNV9Mmw2oLhB0tuc4mie-zjjHql3iroTU8Al2aVCFF65iWD1HzU5y0rYGerPxWPjrsFoDtcd2wYaZqJluTEpRUyQiYh5fG8pAFguwt1vxNqdfe66_6WTn9munsSjLybOE-lhniyUDGmNVGGTWUsh-6zlPzPLdmGluwtyzANxVHXKL5pKLCCkUuJ-P0BTiKVSWqll56tYwiE-2S2AfLSyG7LorhJ0ctPTSJ66DIjZsU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
پرزیدنت ترامپ:
«ایران دیگه نیروی دریایی درست‌وحسابی نداره، نیروی هواییش هم نداره و ارتشش هم ضربه سنگینی خورده.
اگه توافق نکنن، دوباره اقدام نظامی رو از سر می‌گیرم و کار رو تموم می‌کنم.
می‌تونم تو کمتر از یک ساعت بیشتر پل‌های مهمشون رو نابود کنم و ظرف یک روز هم همه نیروگاه‌های برقشون رو از بین ببرم. این رو هم توی مذاکرات بهشون گفتم.»
بازسازی پل‌ها سال‌ها طول می‌کشه؛ خودم سال‌ها تو کار ساخت‌وساز بودم و خوب می‌دونم.»
@News_Hut</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/news_hut/69121" target="_blank">📅 17:32 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69120">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7b8f908317.mp4?token=cuJf6AxFFFx1K_ROVcXbKYB2CrU12Hjbp7YofL96hEoKRDUzPiaJTdYePPbSpgX3VMWrE0iNqF2ZfkpyNKR5uJ5KoF2Lhq2VC6dJkJlkUhvedBz6NZPlmG3P1AoNmzYABBX5ETpcaZC0yKS5PvV6S9U3m03ZE2YJLnbSQaEWyV4hFdrBP29aDMy5yuwDN_1Wr-Sb3_lQii2NNLURn1maMVJsSGgc1oRr0SsTi2uSweTM7y0AUcxvpUXANxdn-_mRdA4rzYcQbHvKdzR3vVHCGNKKqdh5Af-mPlw_HhQst3wvqdV_ADXi5km3_g28yax0ePLfSp9cyaeiNX9B0rhLI7s_-I9Fkdo6cWfg3QKPoJFejiE1bsP75fhrYJZq-bGFwcDQLrzWwpM5J6om5Ca8Lh4j0RGP0w83X0qojQ9pFe68wXEbJuHBAcrErkstWLe5Ax175bbj7u--lhqNxH_wdxKHEUpagtDE3xKz2t0Z_bQIPZPqPXzZE70Q86llcoOZ2F29foXSsd1Z2lIJrIzfUDna5__sPmkS3aVbT1hoIz8kdN5CInKGQw8zhq5oCnnnx6K1MO81Xoxtpk-zzn4d8am7PK-PCSlTUV1rngfjTH5_1oklnCrt7Vf5Lx0QleJVRGcFNg1_beonjXyHsMdQcybQXDWY0iSACzjEyoavTpc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7b8f908317.mp4?token=cuJf6AxFFFx1K_ROVcXbKYB2CrU12Hjbp7YofL96hEoKRDUzPiaJTdYePPbSpgX3VMWrE0iNqF2ZfkpyNKR5uJ5KoF2Lhq2VC6dJkJlkUhvedBz6NZPlmG3P1AoNmzYABBX5ETpcaZC0yKS5PvV6S9U3m03ZE2YJLnbSQaEWyV4hFdrBP29aDMy5yuwDN_1Wr-Sb3_lQii2NNLURn1maMVJsSGgc1oRr0SsTi2uSweTM7y0AUcxvpUXANxdn-_mRdA4rzYcQbHvKdzR3vVHCGNKKqdh5Af-mPlw_HhQst3wvqdV_ADXi5km3_g28yax0ePLfSp9cyaeiNX9B0rhLI7s_-I9Fkdo6cWfg3QKPoJFejiE1bsP75fhrYJZq-bGFwcDQLrzWwpM5J6om5Ca8Lh4j0RGP0w83X0qojQ9pFe68wXEbJuHBAcrErkstWLe5Ax175bbj7u--lhqNxH_wdxKHEUpagtDE3xKz2t0Z_bQIPZPqPXzZE70Q86llcoOZ2F29foXSsd1Z2lIJrIzfUDna5__sPmkS3aVbT1hoIz8kdN5CInKGQw8zhq5oCnnnx6K1MO81Xoxtpk-zzn4d8am7PK-PCSlTUV1rngfjTH5_1oklnCrt7Vf5Lx0QleJVRGcFNg1_beonjXyHsMdQcybQXDWY0iSACzjEyoavTpc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
پرزیدنت ترامپ:
«ما دقیقاً می‌دونیم تو تأسیسات هسته‌ای پیک‌اکس چه خبره؛ از حفاری‌ها، تونل‌ها و جاده‌های جدیدش هم خبر داریم.
این اصلاً مشکل بزرگی نیست. بی‌بی مدام این موضوع رو به من میگه، چون می‌خواد همچنان تو این قضیه نقش داشته باشه. اگه به توافق نرسیم، پیک‌اکس رو از بین می‌بریم؛ اونم خیلی راحت.»
@News_Hut</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/news_hut/69120" target="_blank">📅 17:31 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69119">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/825bd1594a.mp4?token=o-3NujBurP5G3n-chU6SA1qhwbDNQ9ndMUqDTa36MFfCCJOQWJGJWlN0shz4V_dvxp2C4hGVprSK8uI5hLK1hA9kcmURlELouRUbc6ZpwVEeTEXQckVqh_apgnImwc1qlG5297r80reCQiKWNh9Ds2OgrdqWJHhOvyhvYD-gdFwpVI_CmbZ3naMpHYyB2cwVUMCU8zNXlKi3fo9jnV4Mf0zji_rh6dviDUdKC_srMFcUzHUM5glHQKZ5blUL7T-Z9XmNsIY9HisKlziej7xnAkF4Vmop-NHb_NdtZYvx7x1ba3PG1eVYWM6s3RAf03FP9zELIxyBkSeqBedyUSkpHZ1EFwTrtpxoEJwbL4nAZJq52YwzKd19qhr2VJp69u5ezCL0uhlJVeUBNeTjIsw2Zc01ItIDBYn8l6qGbBXJLRtz40Et5q6wPTV9-qQTYaTMaYPoBSRSIHmfEg0IymrZdRG3uveuzBMZqD-pT0Y4fgmKXV2haehHTqK_0u3zn8Mbgx77mCmiMqEeC_YtHSUI-E18ZE8_RUvSS3s_W23N2SIXAxyNmE4WluglDLUvyGvn_zquMx5Uef9nFUfnfMRtKHmdDfnFW3iT5HlmZr9-GSgTjf9sMEKiBsFc5xKMiGYZvN3D8bENfpusrRg5sO_KHBmoj6WO1WZ-XeMwHNAt-Cc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/825bd1594a.mp4?token=o-3NujBurP5G3n-chU6SA1qhwbDNQ9ndMUqDTa36MFfCCJOQWJGJWlN0shz4V_dvxp2C4hGVprSK8uI5hLK1hA9kcmURlELouRUbc6ZpwVEeTEXQckVqh_apgnImwc1qlG5297r80reCQiKWNh9Ds2OgrdqWJHhOvyhvYD-gdFwpVI_CmbZ3naMpHYyB2cwVUMCU8zNXlKi3fo9jnV4Mf0zji_rh6dviDUdKC_srMFcUzHUM5glHQKZ5blUL7T-Z9XmNsIY9HisKlziej7xnAkF4Vmop-NHb_NdtZYvx7x1ba3PG1eVYWM6s3RAf03FP9zELIxyBkSeqBedyUSkpHZ1EFwTrtpxoEJwbL4nAZJq52YwzKd19qhr2VJp69u5ezCL0uhlJVeUBNeTjIsw2Zc01ItIDBYn8l6qGbBXJLRtz40Et5q6wPTV9-qQTYaTMaYPoBSRSIHmfEg0IymrZdRG3uveuzBMZqD-pT0Y4fgmKXV2haehHTqK_0u3zn8Mbgx77mCmiMqEeC_YtHSUI-E18ZE8_RUvSS3s_W23N2SIXAxyNmE4WluglDLUvyGvn_zquMx5Uef9nFUfnfMRtKHmdDfnFW3iT5HlmZr9-GSgTjf9sMEKiBsFc5xKMiGYZvN3D8bENfpusrRg5sO_KHBmoj6WO1WZ-XeMwHNAt-Cc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🌐
هزار سال ایستادگی،
نامی در میراث جهان
قلعه الموت، افتخاری دیگر برای ایران.
@News_Hut</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/news_hut/69119" target="_blank">📅 16:53 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69117">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NfSisRu_CVcbkehBG-05bzOea3UAMXFgmk0-TG6NoBtKUHZVJlhCT42iMFXIQiA6XCYiw3mAyfvTCIvanZqFUHlWvxBYhj8w7GGyGaCzvJ5P6wzJpgqsQCgs6NB3cbhngTtss6LpjArXPZ4gTl8reKNA38TVQnl6rtEY5DkMr1hlvBw-7EfcFte2txRQHcEXgUqQuQ43TA0KJIB4ASSfEtFMjWp5zHMItThSk7Yyzw-SCXxub7afuJWYAE-UmckGKTJRIIKHyczo-87YbJvd1UqnW81Z7g3M9jSs8L2Je1TfoydLcgipYi-0yPIajqJvhr0lZ_TnScv17AvTHHNKZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QSkE2kE7qlMjRdjfEgisSSdCaa-EHu6EU_btOfZqkvCoIwRSxicrBrx7pAvaTkE0aqvGP0retqy84pjm-_X1vBHBvCC7o73ttxNcq1BueLVzOyn14_NhpfgDKWnEbuM5cFw_Zs7SCTsSLQCk1kdre9g6sWK4H_YRvfFCxJgWHxS_gLvT-XJwGIT3GvB4DPlTHyILd0CiriCI_lCQxEFIySUWfEYEzrltFFQS0MO1msEKNWFqL6L9q2NCW22Mz_XvM6261_kbVgnk1uj_IqdBIFTX8-1znZQ1I4ARaGTDpqoW30-4y_RUHLq345ldjb641SgPBl7_SIdMBmM69mEQLw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
🇺🇦
❌
🇷🇺
اوکراین بیش از ۳۹۰ پهپاد را در طول شب در منطقه مسکو به پرواز درآورد، که به نظر می‌رسد تلاش دیگری برای حمله به مراکز لجستیکی Wildberrys باشد، اما در واقع به جای دیگری اصابت کردند.
در Kaledino در نزدیکی Podolsk، یک پهپاد باعث آتش‌سوزی بزرگی در یک انبار لجستیک شخص ثالث به مساحت ۱۸۳۰۰ متر مربع شد که به Auchan، Magnit و سایر زنجیره‌ها خدمات ارائه می‌داد، درست در کنار یکی از بزرگترین مراکز Wildberrys که به گفته Wildberrys به طور عادی فعالیت می‌کند.
در Chekhov، یک پهپاد دیگر به طبقات بالای یک ساختمان مسکونی برخورد کرد و به بالکن‌ها و دو آپارتمان آسیب رساند، اما هیچ آسیبی گزارش نشده است. بقایای جداگانه باعث آتش‌سوزی تایر در یک کارخانه بازیافت لاستیک شد.
@News_Hut</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/news_hut/69117" target="_blank">📅 16:15 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69116">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/0df10b659f.mp4?token=IQFo6mlY1PNsYr3UpCX26EGHTq12xUUwNpRWX0CfRxvpype_qR9R4yXiSpnPYnImvpPkqJx_eP1K43iW1czLxAisbs7BN9o60Smc1pkXgy7kwX1U0ew2vU0rY1iJicQ0nXCcJ09fBA2DMRpD3dQRPNNAMo7K6h5mdAaaiflusjb8PF_fiGOwRjrslQGrwHYo8_2xBAtXJ_fvlPPk8BwDa0J64Xn_nqNg5Hg1vE9vzPRzZCK-ISBotXZsUF6OUEiIzrFittDuMAYglKwteFsSai312bDHQ0rccNdPQWubTDOWJUE99ZexiJl6zMytDQcOFURgi71pBd317Mwfb_iCToi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/0df10b659f.mp4?token=IQFo6mlY1PNsYr3UpCX26EGHTq12xUUwNpRWX0CfRxvpype_qR9R4yXiSpnPYnImvpPkqJx_eP1K43iW1czLxAisbs7BN9o60Smc1pkXgy7kwX1U0ew2vU0rY1iJicQ0nXCcJ09fBA2DMRpD3dQRPNNAMo7K6h5mdAaaiflusjb8PF_fiGOwRjrslQGrwHYo8_2xBAtXJ_fvlPPk8BwDa0J64Xn_nqNg5Hg1vE9vzPRzZCK-ISBotXZsUF6OUEiIzrFittDuMAYglKwteFsSai312bDHQ0rccNdPQWubTDOWJUE99ZexiJl6zMytDQcOFURgi71pBd317Mwfb_iCToi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
بخشی از صحبت های دیروز ترامپ در میشیگان به زیر‌نویس فارسی:
@News_Hut</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/news_hut/69116" target="_blank">📅 15:29 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69115">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/200b5b3122.mp4?token=rYBjWzqCYKmuLM_4Sdj3V3DCHmByPxOnQxaVWKwYHBfWZf8pPIYWeeBU2dWrOpGXA-TrDaQ9U0AjGwuNh8zs5DIBcAS5uhx-ovW1l-d7kIUOlx2MzUnhdJrI4sg-zqMF_PLApvKcVXUAV_LVMh_vYH89iHrKfuFayTeafxvmH4v7sV3qmbSpbdI9Efe8VPmvxKFcGANJ0m4O9sn2XHWj_EETz2G6kvIPszlB6iaE95mbRBi1MlE8NwcN2lZILBEuIGta53GSwZ2CrOY3J_gbq81dRFLw3qe0mqY6onEopDchx2ad7tNK94jdK3bB_lN-pqLfsATat5jmCgYiN12K1w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/200b5b3122.mp4?token=rYBjWzqCYKmuLM_4Sdj3V3DCHmByPxOnQxaVWKwYHBfWZf8pPIYWeeBU2dWrOpGXA-TrDaQ9U0AjGwuNh8zs5DIBcAS5uhx-ovW1l-d7kIUOlx2MzUnhdJrI4sg-zqMF_PLApvKcVXUAV_LVMh_vYH89iHrKfuFayTeafxvmH4v7sV3qmbSpbdI9Efe8VPmvxKFcGANJ0m4O9sn2XHWj_EETz2G6kvIPszlB6iaE95mbRBi1MlE8NwcN2lZILBEuIGta53GSwZ2CrOY3J_gbq81dRFLw3qe0mqY6onEopDchx2ad7tNK94jdK3bB_lN-pqLfsATat5jmCgYiN12K1w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
مراد ویسی تحلیلگر ارشد اینترنشنال:
جمهوری اسلامی فهمیده که ممکنه آمریکا و اسرائیل یه حمله شدید انجام بدن و همه مقامات رو ترور کنن.
بعدش مردم بریزن توی خیابون و انقلاب کنن، برای همین از قصد داره معترضین رو توی ملأعام اعدام میکنه که باعث ایجاد ترس بین مردم بشه.
@News_Hut</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/news_hut/69115" target="_blank">📅 14:50 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69114">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0c00215915.mp4?token=p8C0Dn6-reMIAThUc173hNsbjXCH21qIg-lHQp-Mb9-GJosDHo4O9kUhow-0liu9O74QQAdgKWrVbsb5w6gwArdxYWMnRhNWL42yVY8t0CmrvyDAxlWZSMvn7MxKkXAehBHOdEUuXW7ZTrSfje8bCqXivmLxC0USRGv-CBwsLHBahgVj1PxU1U4RMLt4p76zP8CZk7DTwAxI2-QDUitAJNIi1CJQD97GyBy_jQG49xGKwhw6SfNhTZZN_tu2LP6NFJrvcU8u9u4yPcVGIRmIwoaNnOahTfFE7JS6jr3mhpVGkvkohZZ87uTDuTcmcsnIEPn_NTDxCAYqk1V36o-KeA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0c00215915.mp4?token=p8C0Dn6-reMIAThUc173hNsbjXCH21qIg-lHQp-Mb9-GJosDHo4O9kUhow-0liu9O74QQAdgKWrVbsb5w6gwArdxYWMnRhNWL42yVY8t0CmrvyDAxlWZSMvn7MxKkXAehBHOdEUuXW7ZTrSfje8bCqXivmLxC0USRGv-CBwsLHBahgVj1PxU1U4RMLt4p76zP8CZk7DTwAxI2-QDUitAJNIi1CJQD97GyBy_jQG49xGKwhw6SfNhTZZN_tu2LP6NFJrvcU8u9u4yPcVGIRmIwoaNnOahTfFE7JS6jr3mhpVGkvkohZZ87uTDuTcmcsnIEPn_NTDxCAYqk1V36o-KeA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
مهاجرانی، سخنگوی دولت:
تو بنزین سهمیه‌ای فعلا تغییر قیمت نداریم، ولی هر وقت تصمیمی بگیریم، شفاف به مردم اعلام میکنیم و اونا هم همراهی میکنن.
فقط مقدار سهمیه دوم بنزنین (3,000 تومنی) از 70 لیتر به 50 لیتر تبدیل شده که اونم بخاطر حمله دشمن به مخزن انبار نفت‌مونه.
@News_Hut</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/news_hut/69114" target="_blank">📅 14:14 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69113">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fd184b2451.mp4?token=J-fR-GJSY4YCZSZwNPiUU-QuzLIT2aNzKGB0GOSjg4wcp2Jkvqu_S7gpsOXmR8lxOOaeLm29BXozlS1ntd-uiVybChrGfTxSpOS1EF7j85S_w3jgABHVPF_2FQqBPeAMDyk4DsEy6x26_DvSiljLTzZ6LaP2oSx48M-FtzLiJU74SrjChkBnis4Cx0-ZMSFKcie54L8K-4TL_ddT6jIxakwRvMXeIIkXU55W9YAPE2Gj10pS1vSzCgrIAqvMpFNPjqgKCNaiB6yK6CVZR37G8Wn8o41rkwoju7Yd4vKd0M98VzFa48RO5pjUS3lZJEm-HJkWkYFk75bFvvhsPhffvw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fd184b2451.mp4?token=J-fR-GJSY4YCZSZwNPiUU-QuzLIT2aNzKGB0GOSjg4wcp2Jkvqu_S7gpsOXmR8lxOOaeLm29BXozlS1ntd-uiVybChrGfTxSpOS1EF7j85S_w3jgABHVPF_2FQqBPeAMDyk4DsEy6x26_DvSiljLTzZ6LaP2oSx48M-FtzLiJU74SrjChkBnis4Cx0-ZMSFKcie54L8K-4TL_ddT6jIxakwRvMXeIIkXU55W9YAPE2Gj10pS1vSzCgrIAqvMpFNPjqgKCNaiB6yK6CVZR37G8Wn8o41rkwoju7Yd4vKd0M98VzFa48RO5pjUS3lZJEm-HJkWkYFk75bFvvhsPhffvw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇱
اسرائیل کاتس، وزیر دفاع اسرائیل:
نتانیاهو به دستاوردی رسید که چرچیل نتوانست به آن دست یابد.
او ترامپ را با ما همراه کرد تا به ایران حمله کنیم؛
بدین ترتیب، پیش از وقوع یک «پرل هاربر» دیگر، ایالات متحده را به اقدام نظامی واداشت.
@News_Hut</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/news_hut/69113" target="_blank">📅 13:42 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69112">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/136b2d25c6.mp4?token=HMNUyehVpOQCEudyiJ8_XbiyIa_YPkLuBNyaQlDmB5SaBRJbe2Hod-b7aW-woZTxDLaRVsVjfCyc_Au1zI9DrKl6O-AW08lLjgUH_jWFhhJsXg_UM6EJeWdsx0toNuymEjH3-5ZADgj1d212AAG0X3k407ZiEDOVJT0jVlApMOuhS_xvtrPYmg0UoFHDVLjL04gX2c8Y36xxvJ7LAslLrPlOS1eBE2DIxrgFnks4_QDX0QAoEM8-i9SXmbG2__iEl_4aQG42GtR_FHW1jw1ZGnBj6wMHQ6i4HGrHDSa-3XmbLgmLkvbA8k0K66TCsytbEyC2eTUlT7mEPRBirpOxKg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/136b2d25c6.mp4?token=HMNUyehVpOQCEudyiJ8_XbiyIa_YPkLuBNyaQlDmB5SaBRJbe2Hod-b7aW-woZTxDLaRVsVjfCyc_Au1zI9DrKl6O-AW08lLjgUH_jWFhhJsXg_UM6EJeWdsx0toNuymEjH3-5ZADgj1d212AAG0X3k407ZiEDOVJT0jVlApMOuhS_xvtrPYmg0UoFHDVLjL04gX2c8Y36xxvJ7LAslLrPlOS1eBE2DIxrgFnks4_QDX0QAoEM8-i9SXmbG2__iEl_4aQG42GtR_FHW1jw1ZGnBj6wMHQ6i4HGrHDSa-3XmbLgmLkvbA8k0K66TCsytbEyC2eTUlT7mEPRBirpOxKg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇱
اسرائیل کاتس، وزیر دفاع اسرائیل:
ما بسیار مشتاقیم که به تأسیسات انرژی ایران حمله کنیم.
ایالات متحده در حال حاضر با این کار موافقت نمی‌کند، زیرا نگران است که ایران به کشورهای همسایه حمله کرده و موجب بروز بحران جهانی نفت شود.
@News_Hut</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/news_hut/69112" target="_blank">📅 13:28 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69111">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">🚨
🇮🇱
کاتس، وزیر دفاع اسرائیل، به شبکه ۱۴:
جنگنده‌های آمریکایی برای انجام حملاتی در ایران از پایگاه‌هایی در اسرائیل به پرواز درمی‌آیند و ایران نیز از این موضوع آگاه است.
@News_Hut</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/news_hut/69111" target="_blank">📅 13:12 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69110">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">‼️
❌
آی‌24نیوز:
طی 48ساعت گذشته حدود ۲۰ پهپاد توسط شبه‌نظامیان مورد حمایت جمهوری اسلامی در عراق به سمت اسرائیل، اردن و عربستان سعودی شلیک شد.
@News_Hut</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/news_hut/69110" target="_blank">📅 12:39 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69109">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b2c6cefb08.mp4?token=gSD69lCKsr2O6Btz1aPPNfan2A7NLq5L1tpNavkSTwH7udm2FXnYRveNSWP5bS2_uQJUNHBKxdFDVq2lTShLrUUoOtcVGx9R9meIn5IbaLTFI6rBIPTfXU_NU2zdv9yJt4DmrkRveUdjoj8RJ6Cz_QXbRqDfV71EIwY0j8l0USD9N8J6jzqpE3rEJe9U33tM3IhFH_j_XH2ox_c2bgV6C57CBjG0_IyM_YijA8ozONTD6lhS9uHSMN-Vz-FiFIW4nFHX4VIBXNiTwoO9ZB51uuvpxAqj4lO9TMJewsIZ4o9mtnmdZwFo8rirNswYQJPvHuXfjU-nG8FjlXUldRTe1w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b2c6cefb08.mp4?token=gSD69lCKsr2O6Btz1aPPNfan2A7NLq5L1tpNavkSTwH7udm2FXnYRveNSWP5bS2_uQJUNHBKxdFDVq2lTShLrUUoOtcVGx9R9meIn5IbaLTFI6rBIPTfXU_NU2zdv9yJt4DmrkRveUdjoj8RJ6Cz_QXbRqDfV71EIwY0j8l0USD9N8J6jzqpE3rEJe9U33tM3IhFH_j_XH2ox_c2bgV6C57CBjG0_IyM_YijA8ozONTD6lhS9uHSMN-Vz-FiFIW4nFHX4VIBXNiTwoO9ZB51uuvpxAqj4lO9TMJewsIZ4o9mtnmdZwFo8rirNswYQJPvHuXfjU-nG8FjlXUldRTe1w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇺🇦
گویا زلنسکی هم در آمریکا حضور داره و قراره با ترامپ دیدار داشته باشه.
@News_Hut</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/news_hut/69109" target="_blank">📅 12:33 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69107">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/d48P3TgLqBJgGm8wEEgWTYOGrB1Z3nY6J1jJpVU7ufJGLNVGnTAS4Q8aurPV7e6MaK32dmD2V7PqFUq7PycCQFoRSvjajHoVrQ2tQX3ymmfUqHDqrQXudiMg9L8R_p36ZmEKqFsiiy8sb-jTGpgVgjFL2x8imTAVaUtd0mRSNNtm6Eu9QjaD2KjTBLwVFQ6ebY5pOo7idzfFRo3piKNRsojkeMDNG8kW-B0i02L_pgm7z0xC-YtaAIL9uFa-LBL-7oZPcumxHTZY0Uc6a7nlxUtRdx-EFUsnYJnq-cY6EevGkZevXteSsf0nviasxEe3UEv7eiShyhKbhxZhZx5nvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/U5P-6-9phKJ3rz-pFtbTbooyAYb5GW5P_E4GhQkIQMuk2-FSaHIanO4JJnf5Jr1n82XhehyhhsitkSMi9q_gOE_SVF7JuJpVuckmIaF0QTQL302GkEgAMql_k4cz3xdS6Fo3rUOXdQkHKV0T-rTq4RSE4ddfvSkdSUKHYz7sx5zDxRVmUBmMVK49pNbV1wd7Aac_Jy2C_4VAOJQQ3ur1S7UMpb4O5F7bP5T7hvN6GmUDUTJ8irwINwxN9cEe8NdnvE1W0a5L8PM02c0OGiCiJuJgidaIeusNZALcpbon6MRK1w_c5hrH5MeExQHWllVW8DqRzFCAgYCPYkeQPOhZ_A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
تو‌ جلدی که مجله اکونومیست از سال 2026 منتشر کرده بود؛
زلنسکی
🇺🇦
درحالی که دوربین دستشه، داره به یه کشتی ایرانی نگاه میکنه!
@News_Hut</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/news_hut/69107" target="_blank">📅 12:14 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69106">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1f0b26c19f.mp4?token=oycoAKqsGyNTT9TsWQhDDOQfWmJq2gvT-8JQdsF8w6UGkTzua9AmpZ2CL1JkpQO4DIYB8JX-SJUcpWmNDFL_HLWjpDJIeNnk_zSV6EvHGd5U2TCo5PpgTPA02_wNKhIFgmPrm1wQcxjA3dpZidTnnM2Bv_ViGoGI-vhJC30ErFbOC5m2jxrFwSHVYwLUXwgO34IXUoTX4qdmIHOrfG26a-NuykMTDjuta1TiO4zWzyU1aHZMsqZuh3IizIPbmA15LjuCg5GzYBcdxSubWr2RVP3Di6dTkqi71HuOdxgO8VxtC4oNK45XjxwQ7DNrTjCslk6AKnIGmNe_olwNnri2Lg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1f0b26c19f.mp4?token=oycoAKqsGyNTT9TsWQhDDOQfWmJq2gvT-8JQdsF8w6UGkTzua9AmpZ2CL1JkpQO4DIYB8JX-SJUcpWmNDFL_HLWjpDJIeNnk_zSV6EvHGd5U2TCo5PpgTPA02_wNKhIFgmPrm1wQcxjA3dpZidTnnM2Bv_ViGoGI-vhJC30ErFbOC5m2jxrFwSHVYwLUXwgO34IXUoTX4qdmIHOrfG26a-NuykMTDjuta1TiO4zWzyU1aHZMsqZuh3IizIPbmA15LjuCg5GzYBcdxSubWr2RVP3Di6dTkqi71HuOdxgO8VxtC4oNK45XjxwQ7DNrTjCslk6AKnIGmNe_olwNnri2Lg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇱
ساعاتی پیش بی‌بی‌نتانیاهو به واشنگتن رسید.
@News_Hut</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/news_hut/69106" target="_blank">📅 11:50 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69105">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e0eb0677cd.mp4?token=HKQFMRWyJ5EYGsg260nhRP3LSDI0lLqIbVGcJONL5SL0AuuPYKzpU56sz6-k01nSILbWBeY3DfQjmXLdhe08o84vWIHce72bn3LtV-fvAYR27pWfi-wK58VVX5QaN4YXxLXBbajsAj81oRoGv0nKncrgENnZTkO4kL7U40bGKKVt6oH6JsfFWLD_2fdS0gA9WtUCs71XQvU4HWvkdYturJdWOePnsia9sZ82uGdrRZWTxxaQFtFznx9x0Wgi4_dOny1UJu9v6N9YRCwDC1d-5g7lTwbjZZb12UbNLyA5oWj858B_d-7qwm-eWYgEs9x4rTAogHon63l3-5Up_6Avy30qKgB_Qfcb5Je_TVUKoQJkFyItKVl9qsfMFzAlo9dJJFVq1QQNL6Xd1XwCwCAoA5utA9wcEFs5jNTx39f1I_MrG48xIgd0_LxeHKjQ31FYUic_6vB7ZETMVbvN4He3HwUCOjqZGm1BHrIBVWuAcT0suzdKtL5yUcOQwUfC5MJtx6Spx4B_tvUvbbCHqZwgH46vbftUpN-wjGx98IJPxExJ1OOTy7SWdok4C2BmCaFGTO-BJJIHrKAYypPbqHg6IbhUGn8DVQGF9D5QzRAR6UjkmAdvdNlb-2MhmmnhoCx6jNuYJS6QsBFZpqdTzmI876WExyEcLTxYRnMJsFKiFsk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e0eb0677cd.mp4?token=HKQFMRWyJ5EYGsg260nhRP3LSDI0lLqIbVGcJONL5SL0AuuPYKzpU56sz6-k01nSILbWBeY3DfQjmXLdhe08o84vWIHce72bn3LtV-fvAYR27pWfi-wK58VVX5QaN4YXxLXBbajsAj81oRoGv0nKncrgENnZTkO4kL7U40bGKKVt6oH6JsfFWLD_2fdS0gA9WtUCs71XQvU4HWvkdYturJdWOePnsia9sZ82uGdrRZWTxxaQFtFznx9x0Wgi4_dOny1UJu9v6N9YRCwDC1d-5g7lTwbjZZb12UbNLyA5oWj858B_d-7qwm-eWYgEs9x4rTAogHon63l3-5Up_6Avy30qKgB_Qfcb5Je_TVUKoQJkFyItKVl9qsfMFzAlo9dJJFVq1QQNL6Xd1XwCwCAoA5utA9wcEFs5jNTx39f1I_MrG48xIgd0_LxeHKjQ31FYUic_6vB7ZETMVbvN4He3HwUCOjqZGm1BHrIBVWuAcT0suzdKtL5yUcOQwUfC5MJtx6Spx4B_tvUvbbCHqZwgH46vbftUpN-wjGx98IJPxExJ1OOTy7SWdok4C2BmCaFGTO-BJJIHrKAYypPbqHg6IbhUGn8DVQGF9D5QzRAR6UjkmAdvdNlb-2MhmmnhoCx6jNuYJS6QsBFZpqdTzmI876WExyEcLTxYRnMJsFKiFsk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تسنیم این فیلمو راجب
ملانیا زن ترامپ
منتشر کرده تا اگه کسی قصد ترورش رو داشت از این اطلاعات استفاده کنه
🙂
@News_Hut</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/news_hut/69105" target="_blank">📅 11:15 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69104">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/76bcf42cd4.mp4?token=AP46AGqu_URVCNVPpCp2us5U7jrRZPYeZlWdqdlJZyyXqqhT5K8EaAc4cC2-1Su-MFu1bIfx9AqtiZFgB6E0Fm4nLbCwyGHJ-03Fqb7ECg2kOvFfeX0ptCTUuJAxRFDR1oqj0lauQlvwpqf6hdhDBqzY2FQB-QVhEivr4PWju0DmLh6eTBz094-UwsQJ0cYftCI7LBLmBZs5SR4Z1Pk_a1ZJtmr2nNBWtXwCPFlmgTCxgWLoh2_YPxyUT4TVDZ0Z8QAPL72kXfQF0Y4z5IFoFohHcUKfjq_JPlZvaohKkbmYKe0Vp7A7C3JL-Lk7ReQyTzd-lTNgYNdSocg5ZUe2Eg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/76bcf42cd4.mp4?token=AP46AGqu_URVCNVPpCp2us5U7jrRZPYeZlWdqdlJZyyXqqhT5K8EaAc4cC2-1Su-MFu1bIfx9AqtiZFgB6E0Fm4nLbCwyGHJ-03Fqb7ECg2kOvFfeX0ptCTUuJAxRFDR1oqj0lauQlvwpqf6hdhDBqzY2FQB-QVhEivr4PWju0DmLh6eTBz094-UwsQJ0cYftCI7LBLmBZs5SR4Z1Pk_a1ZJtmr2nNBWtXwCPFlmgTCxgWLoh2_YPxyUT4TVDZ0Z8QAPL72kXfQF0Y4z5IFoFohHcUKfjq_JPlZvaohKkbmYKe0Vp7A7C3JL-Lk7ReQyTzd-lTNgYNdSocg5ZUe2Eg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
مجری :
کراش فوتبالی تو دوران نوجوونی داشتی؟
⏺
غزاله اکرمی، بازیگر :
آره ، غلامرضا عنایتی
خیلی زیاد دوستش داشتم ، نمی‌دونم واقعا چرا به شدت روش کراش بودم!
@News_Hut</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/news_hut/69104" target="_blank">📅 10:30 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69103">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eme_K7EcSy3S4waHFMZvXTtEu4mOGWTjXcToQOCbL3xoUDbWVvXg8lrdzR0_Bd5kbH17ouTOcwBGligJs-OrNAYSrx6Wztl27T43vlfMOjiXHCjw8Y1xwOIRdSxpLcUvbWklaFwA1kADTTOGUgri7yzMv0PVFgeQvT-2U2ADT-hYIryBi7okpTaJVT0vIFZbxRfBOPdFblgVviwysiAmv4EpHI-p-hTw4rqIwyrdDbyUuE_yg7rZfzURML29uNSgeC1PklnrkOxJ14vnhlfSsK96IhGtj1NCapWFBbZep_Iw2AgUg3TFrW0bQA166fFiPjzYGUzry5QKFQ_Zy3Bhpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به کشاورز زمین داد، چریک شد!
به زن‌ هویت داد، آنارشیست شد!
به کارگر سهام داد، کمونیست شد!
به هنرمند اعتبار داد، توده‌ای شد!
به مسلمان حرمت داد، تروریست شد!
به دانشجو بورسیه داد، مارکسیست شد!
به اقلیت حقوق برابر داد، جدایی‌طلب شد!
@News_Hut</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/news_hut/69103" target="_blank">📅 10:04 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69102">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b88a652ec4.mp4?token=Tu0r1z4YuAHz7AMO-GnZb-nFSpehsEaPJHjmShXEmGDQM2s9A9X7k8Z7GrAR4u30l9xJXEQWntwk24eSh__u0XYRGGYhrHex_zwvWUCtHsMgaEyffrwSTB2cN3kHODFDc366zHVcSdKn8REesVd9zjt6PzIpfFOjMoFACnpW70rHqn2jrHH8u3ftyc6GqW5M7YdIYLoft6FDlqzzBMwSvzyMN-LBxJCQod94ZfAzBsHRv7kBu2bBrfJGDM4bXSETY7IV2p4iP_Rn4Mq77yaJlO57OnSMLXSJOv63NYezlFFKeP0i0u2mWDKW564oIsjahj_XHDVUK8iDpd89DS2cUg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b88a652ec4.mp4?token=Tu0r1z4YuAHz7AMO-GnZb-nFSpehsEaPJHjmShXEmGDQM2s9A9X7k8Z7GrAR4u30l9xJXEQWntwk24eSh__u0XYRGGYhrHex_zwvWUCtHsMgaEyffrwSTB2cN3kHODFDc366zHVcSdKn8REesVd9zjt6PzIpfFOjMoFACnpW70rHqn2jrHH8u3ftyc6GqW5M7YdIYLoft6FDlqzzBMwSvzyMN-LBxJCQod94ZfAzBsHRv7kBu2bBrfJGDM4bXSETY7IV2p4iP_Rn4Mq77yaJlO57OnSMLXSJOv63NYezlFFKeP0i0u2mWDKW564oIsjahj_XHDVUK8iDpd89DS2cUg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏸
ارزیابی رابرت پپ از سناریوی ورود نیروهای تفنگدار دریایی (Marines) به سواحل جنوبی برای تصرف محدود نقاط بنادر و عواقب آن.
@News_Hut</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/news_hut/69102" target="_blank">📅 09:15 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69099">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jdsbe81osTFb4pOrF4_Uo6icxw-Q09sFiWXlnPoajV_h0TDHeDQNoX5k8rZPDljX5bDu9Qy2--x0RoxUVlJULqhSzd54MhIJvcYKp2biD8L7n6XnvAEXpTKA--U3p8IgT2xRAFNO9pMEOUXPbmLjb42yJy1D_jG8AmzdO9TRxk6S4JH3yBC3ptHRjvnj1HKk-FZBoST-yVCC37fxCKefLxSumde51pChikq97NSTRkx7V2IEcC49bOswwRjskatp5LNEV_U8Uhh02wKywJ0Yl5xaY-yM3FQ10KVZ0fp235DRAhXCgaQahwf4Yf-mjtl_yrd-JZhwhBE8S1WVEUxFag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PMjM-qCDSCDoAAvWSIOzOuchlUMo25O2F5EYCbXoSIzX6-peOSiywf5KV8WuMb4DjBhSovjQp0HmAMyCyAiWhW9U6lj-8PeGNCWY4aVqt5BBWnBYVIdMid3cufYiNdqBle0_yImu9_fnoZMeS5zBA8Qnqe5y1k-hdydPlQ7esy11go31bbYLssm_ssDSf8XaIJpdm99TtjNxyIsxCJLaN3ZE6yUQ_3ZiScTey0S3hRZH0diRcrWvSrXXCLJxcpXszwxE6zqAZwrErypbzenTk7JS48UolhSMWjamY47GnFCMHxVmwGiaIXTBnYrNeMyBSwqlfzmDpVCItBaprksHwQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">یادتان گرامی جانفدایان میهن
🖤
@News_Hut</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/news_hut/69099" target="_blank">📅 05:56 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69098">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">#رسمی؛ جمهوری اسلامی دقایقی پیش، پس از اذان صبح، ابوالفضل سپاهی، علیرضا سپاهی و امیرحسین صفری را اعدام کرد.  @HutNewsPlus</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/news_hut/69098" target="_blank">📅 05:56 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69097">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">#رسمی
؛ جمهوری اسلامی دقایقی پیش، پس از اذان صبح، ابوالفضل سپاهی، علیرضا سپاهی و امیرحسین صفری را اعدام کرد.
@HutNewsPlus</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/news_hut/69097" target="_blank">📅 05:17 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69096">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">متاسفم برا یه عده که ذره‌ای شعور ندارن و چند ساعته مدام در حال پخش انواع فیک نیوز هستند، بهتون کاپ طلا می‌دن که خبریو زودتر منتشر کنید؟!
#hjAly‌</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/news_hut/69096" target="_blank">📅 05:10 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69095">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e9f40f91b5.mp4?token=t0pfMHe3qxmUuP4AaJoWAy4hPHhas8qRD5hnFl-aXcF3HnO4AVNa9BT3UrB43e5jAeHX_m_ZhqiZYmBWMgobTqJza7JwVvIo2v9eImcReGLuT9wRnQ_e2MGyLzBdDZmLUYtLnxc2bcnQrTF5uvCU76Mx1L7NHyX8PcT7eJvUwCKA8spthdxTm8hCzD14ozZh8kRBqGDkQcTAEy6ZUgkOO4zDuxs717O2Ganuz58Ulthukc2lWMbta0Z8rXfVCGIwPPx__9_gpXrb37Ai9-0tO2kOq7_ueE2WvhbFotnUHNbr63EhbT_AQhwKM3GZLUhBy0wYkoZH1lB-2JGkaWahsw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e9f40f91b5.mp4?token=t0pfMHe3qxmUuP4AaJoWAy4hPHhas8qRD5hnFl-aXcF3HnO4AVNa9BT3UrB43e5jAeHX_m_ZhqiZYmBWMgobTqJza7JwVvIo2v9eImcReGLuT9wRnQ_e2MGyLzBdDZmLUYtLnxc2bcnQrTF5uvCU76Mx1L7NHyX8PcT7eJvUwCKA8spthdxTm8hCzD14ozZh8kRBqGDkQcTAEy6ZUgkOO4zDuxs717O2Ganuz58Ulthukc2lWMbta0Z8rXfVCGIwPPx__9_gpXrb37Ai9-0tO2kOq7_ueE2WvhbFotnUHNbr63EhbT_AQhwKM3GZLUhBy0wYkoZH1lB-2JGkaWahsw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مردم دارن شعار سر میدن
@News_Hut</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/news_hut/69095" target="_blank">📅 04:22 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69094">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">دفتر رضا پهلوی از جامعه جهانی خواسته هرچه زودتر برای جلوگیری از اعدام معترضان در اصفهان وارد عمل بشن!  @News_Hut</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/news_hut/69094" target="_blank">📅 04:14 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69093">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">دفتر رضا پهلوی از جامعه جهانی خواسته هرچه زودتر برای جلوگیری از اعدام معترضان در اصفهان وارد عمل بشن!
@News_Hut</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/news_hut/69093" target="_blank">📅 04:13 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69092">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">لحظه‌ی اذان صبح و آماده‌سازیِ شرایط اعدام، در میدان علیخانی اصفهان</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/news_hut/69092" target="_blank">📅 04:06 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69091">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">باز می‌گن چرا مردم ایران دین‌زده شدن، شما یه نگا به کشورای عربی بندازین، مردم، حاکمانشون رو می‌پرستن، بعد این شیعه های مفتخورِ بی‌همه‌چیزِ خرافاتی، جوونای مملکت رو دارن تو ملا عام اعدام می‌کنند به بهانه ها و دروغ های مختلف، همونطور که ۱۴۰۰ ساله چیزی بجز دروغ…</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/news_hut/69091" target="_blank">📅 03:29 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69090">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">باز می‌گن چرا مردم ایران دین‌زده شدن، شما یه نگا به کشورای عربی بندازین، مردم، حاکمانشون رو می‌پرستن، بعد این شیعه های مفتخورِ بی‌همه‌چیزِ خرافاتی، جوونای مملکت رو دارن تو ملا عام اعدام می‌کنند به بهانه ها و دروغ های مختلف، همونطور که ۱۴۰۰ ساله چیزی بجز دروغ و خرافات ندارن به مردم بگن
#hjAly‌</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/news_hut/69090" target="_blank">📅 03:27 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69089">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/780d746559.mp4?token=mSkzEhSABWdEM_JA9ytoenYkS9Bk__N1wKJf8sFVV_Vt5vlMFaXGezRQEDCF9zs1v9A34OOXitysC1cF2-eZ08DjTdYWbsMYLFH_2xtf6-4SKclVq8ZjWV74ZBJrdiM1u0CaQroU7lLqcMzMAGuAcI7m0JL6H4vEMaf3Os9iPKtAv2PXUJoEjiCq1ARcM5m_CsKiislyKz_5ScsDXyF0LrEPqqkyjW117x2FYcoCk4gDnCUYvf_of99TWpvDSbC5mHfzZbir8EVIIzqjop2-bebL62Cbztoo0RsGhQ1i3hSsIdwGDn2vUj_8z3RguGQmMU3pmzT8ads4aq6qKte3Eg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/780d746559.mp4?token=mSkzEhSABWdEM_JA9ytoenYkS9Bk__N1wKJf8sFVV_Vt5vlMFaXGezRQEDCF9zs1v9A34OOXitysC1cF2-eZ08DjTdYWbsMYLFH_2xtf6-4SKclVq8ZjWV74ZBJrdiM1u0CaQroU7lLqcMzMAGuAcI7m0JL6H4vEMaf3Os9iPKtAv2PXUJoEjiCq1ARcM5m_CsKiislyKz_5ScsDXyF0LrEPqqkyjW117x2FYcoCk4gDnCUYvf_of99TWpvDSbC5mHfzZbir8EVIIzqjop2-bebL62Cbztoo0RsGhQ1i3hSsIdwGDn2vUj_8z3RguGQmMU3pmzT8ads4aq6qKte3Eg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">میدان علیخانی اصفهان
@News_Hut</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/news_hut/69089" target="_blank">📅 02:40 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69084">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TwZ1ut7hiU8yPZigZN2sK7PrmH57oV88HzPWIrbl-s7yHbxk8tX8E5Ct9EUH6pDNbJswLoZDsYtWZSgnNdvNmBtoG6IZ9ZOsPQKIVdR9VssMfpP4l0wc-JtdHxIra73wv4_evHiRVjtooo3SWi9uvR4hJIhX4nwjO48HuQN15x6zp_UBJbQAFEvjKLMjzJD9Mlyhs-T424cwv8o1keo1aebyUX7D86CZ9Yyute2fWWeh393OjaJwNz4x901MxSi_wvrLGRqmxEp_kVXqDEBPxyXSzezDr39ytM3aPIkh_RLLtl4kA84eAgu3pMnBu_VscdHdjNSzU5EKiSoWRjddqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DAr2nRxfc7vMZuqm5DJB3HXdHZtbTsGtpybdaQr644A-Ct7X6WESJQ-38jTOdfMvo_23ixK6olInLYsseqkr3SLkseeqkBorsOprt9QUjacNtvDFlVrUddDLxAIgbW4oyz5qF-6HPD1YvS8ts7RFhHsGDGJrgzgJQZv9Dx4t7nXGoPfeOUR43hxPcCHSIYGqjH9TUpWNYxhx0pyeycU3wMswqfNSNhLzF2jj0pRRAA0GLfZ9fOXagL9aibfKZNvs5LRx4ts_1yNoxlEIQUMWIc0xnUgEpa3HNi89JmDfdKhOlQl58jMjRrEVhpNSOnMRP5adp0VttXXeQ6doR5LMXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FV-Zwv0kk1y4xAiQDiUf2FBk81pogelKZZTwR20s6ffDg93ixXqFaa59yQ1drISwib0R1KCdRvMysy2yqK6topJh7ITigNZq22_MoOQGqAovFj5gQXMqrV3WqlVrEPllVXma_RZm0-z8t11-DBgmWGw-RVUlO4MXIbVFzqUD6qpfwkp9SNq0y7lAOcIZgbNjDrigdD8_R0jjnor7h_GJoQk3lVXXLIBt5KaAddgutM5H0t9dyPEZeCnd7Lv8B9iiDxEJWvLPLrVl28wD1B-mNbltErIxTg49pXMWjIZW4N7V2gwWp3E93wRJblMM9ASMcAQv0CudaOGCwHJei9Igew.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/491b6de7b5.mp4?token=HtRlTIrvN1rm4vy5zUdkXQ-R_xLA4wSd-o5p5m4YvkL-5YT9Wn8lqnWSqTMNCRjlSza88O-XDNyfcwzBo6_eRW4pjVij2VQWPCU3DQRg3M0HYpeWSPis5uvP6_cK1LPKUHjFVW5YoYUaquA6byd_2RvcBqls2T67yrUVDUFfQfp2FC_rSSj7kgrzPEkitLN91l3MT6d7S_7ADzNRAsHQ3_KwAtv6ui7cZp2BRGbJXW118pBk_WpHffEDNH6ug__dYbZV0Z7M6MGX5bqGHabh6eBk3lV-1anaP0mJG_Aj7FVhPZewVy58htHt4euVQtePm4-WiQAXjmslKHMFgf4LSA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/491b6de7b5.mp4?token=HtRlTIrvN1rm4vy5zUdkXQ-R_xLA4wSd-o5p5m4YvkL-5YT9Wn8lqnWSqTMNCRjlSza88O-XDNyfcwzBo6_eRW4pjVij2VQWPCU3DQRg3M0HYpeWSPis5uvP6_cK1LPKUHjFVW5YoYUaquA6byd_2RvcBqls2T67yrUVDUFfQfp2FC_rSSj7kgrzPEkitLN91l3MT6d7S_7ADzNRAsHQ3_KwAtv6ui7cZp2BRGbJXW118pBk_WpHffEDNH6ug__dYbZV0Z7M6MGX5bqGHabh6eBk3lV-1anaP0mJG_Aj7FVhPZewVy58htHt4euVQtePm4-WiQAXjmslKHMFgf4LSA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بامداد سه‌شنبه؛ تصاویر از وضعیت میدان علیخانی اصفهان
@News_Hut</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/news_hut/69084" target="_blank">📅 02:05 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69083">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b7f398a76c.mp4?token=PXqGEegw0KwJ2Vn9vckfGH88ALDpROxm3KY2Yw35UVmhvnFV4bMfteeFkFZ_FSl-Ei6UNCMjQPv5WFCvI3X5OBH5PEN34iipYWVg4wJ4bDAN7qUZhEqdUHUBdQqlIA4DK7LoDln5CRYFOhiLM72mIZ7R6bszBbI6K3okUnABXZ3Xe9edtnjWmgkLURTsCnINbNx0pPncsDsgU0mx8IaD24smIkcc3mWm0qMP06emt4b3RmfUeVhsBT3gPfBMnUV-RUQ9vFzYfr1Ue1hwQoViXN50p-SIdaOQdH1BiuqAaqMP3NzDgCNHD3Sn93VygsybJCExsVynDMTgNg0jK0mS8w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b7f398a76c.mp4?token=PXqGEegw0KwJ2Vn9vckfGH88ALDpROxm3KY2Yw35UVmhvnFV4bMfteeFkFZ_FSl-Ei6UNCMjQPv5WFCvI3X5OBH5PEN34iipYWVg4wJ4bDAN7qUZhEqdUHUBdQqlIA4DK7LoDln5CRYFOhiLM72mIZ7R6bszBbI6K3okUnABXZ3Xe9edtnjWmgkLURTsCnINbNx0pPncsDsgU0mx8IaD24smIkcc3mWm0qMP06emt4b3RmfUeVhsBT3gPfBMnUV-RUQ9vFzYfr1Ue1hwQoViXN50p-SIdaOQdH1BiuqAaqMP3NzDgCNHD3Sn93VygsybJCExsVynDMTgNg0jK0mS8w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">داربست رو نصب کردن و جرثقیل هم آوردن و متاسفانه با اذان صبح، این جوونا اعدام میشن
🖤
طبق گزارش شما مردم وقتی میرن میدون علیخانی و می بینن مامورا اسلحه دارن، جرعت نمی کنن کاری کنن و فقط نگاه میکنن.
@News_Hut</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/news_hut/69083" target="_blank">📅 01:32 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69082">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/316f36114d.mp4?token=lwm93q2ndqWQpoxfEVJhljb3DVHQifPgJWFM57Dh-YLScrFKdEY72pxooSMFVy7yZDq1_Jgrs5ifyLJ-s7_l_BNs8dDHfUtBv0g7KfPSVnCzeYoodVb5eVpHAbc28sV-Xw8WjRoXWHWw22jkOVqZhxLFYgw4vjGRvPjjgk2GfD-IWmSeHZeyaoSLu9IFJ57w4quKRTQr9T97gDDXsyZj7b6UKyOcFha2FT9XSd_U_SjL4A-uVaw-B_Y8PGLLHa26xgq21-_MGWonh5r3WXXNsUEbbVxSeviyc_tVvIbLhGgrF5PUOquU4Bk-iHX3u4iCJ74VMsTEG3LzDCKPinQIVw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/316f36114d.mp4?token=lwm93q2ndqWQpoxfEVJhljb3DVHQifPgJWFM57Dh-YLScrFKdEY72pxooSMFVy7yZDq1_Jgrs5ifyLJ-s7_l_BNs8dDHfUtBv0g7KfPSVnCzeYoodVb5eVpHAbc28sV-Xw8WjRoXWHWw22jkOVqZhxLFYgw4vjGRvPjjgk2GfD-IWmSeHZeyaoSLu9IFJ57w4quKRTQr9T97gDDXsyZj7b6UKyOcFha2FT9XSd_U_SjL4A-uVaw-B_Y8PGLLHa26xgq21-_MGWonh5r3WXXNsUEbbVxSeviyc_tVvIbLhGgrF5PUOquU4Bk-iHX3u4iCJ74VMsTEG3LzDCKPinQIVw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">از آمار تا پیش‌بینی
https://t.me/+L5I8ulM6jEc2YmE0</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/news_hut/69082" target="_blank">📅 01:32 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69081">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J84g1aICR-lrIoEXUU6sl3m0acx7vUKSiBzM1MqrsE43MrmCD-eFy2BBvi7MnTQS1WAUoXYXyJJEvsO_dDH--hA2RGHfuDsLhEp6vJSpZ5xOXTDoyQCTJ74iyN2wSLdyWMauKOLmUJR77zfB8FLb7TapWV6hNA8Dt1-o2HzdTBmMCMAayCSq8N_Di-YTxtoBgSSAV3CKZzZK6XNNqpRVUSp2C9h3S3NRB8Vf6DjpmHx1SHwP1PSrBxOGdDJ_fD7RyRUffX3TBKrHhSwqUWE-8a2aMhTZaX126PkPU26lXwCYjTeT7Kg0VZU3atEJb8v0qnILDjSr5iQFYNJ8bI2_2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بنر نصب شده توی میدان علیخانی اصفهان:
«هیچ جرمی از نگاه قانون پنهان نمیمونه، دیر یا زود عدالت اجرا میشه»
@News_Hut</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/news_hut/69081" target="_blank">📅 01:20 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69079">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OGWo0JlzgoUEcnlV2gVrzU8PO-saVYe-C4P2xdCBbF5mlcT8nCGTPDGfDB6FnpSyomnIGaBa2XjghEx7b4oTL1oBq1AR-3Ucsl7ZBafw-37Snpf0jzlrLUUOFmUXFRtI4oiM3cfHjrKu5wtdnLwHsMWxy1tsaLfVlCicjL8CalyqMHp20xCC8dxMs2sGw0kk0MdzV_VIlEtQGGZyvrZil53VQT1DhJ7nM6ECcnJOzcsAA9vEGorHpFGb8Ffszzh4HSY_jKnvDCLeE72TnaQtVsUcGWtPQ1rhYu-dHzPWZYjYNillD9KL_UKa34eLpMhNhiq53mMlUu-vdbh4C1UOyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/h0qcTfOmO165BHiV8_adTcGVr6s6bSjrQMKPOz2a9Q8VastQMGs2hHgXHoKiQnhe1YEe-GI4BE4H5WA7eDpiztvK1seZmUy9blFPMsQSBlSmODxDveFGIOnTc6W-k1aj3hheIi9fEvYva62-dZ0dpn5QBn-0zRr8Etm6tCPSKsqhfH314ST6vrcj0qJEM3GICNO-Bz9OzVQa7_Cu4yZ790L7wBuM0DGEiWsAbar79uNWgngJqAZh3LvG0SVRdGHrowlZcthyZOlM53w-FLzoxxKdHgUht2u5h2_6x8S53K0IdoMcITgQWeqjTtJEKngxkLnwgR-dIR5JFKTIw76AIQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">طبق گزارش ها
توی میدان علیخانی اصفهان داربست نصب کردن و جو به شدت امنیتی شده؛
طبق گزارشات ابوالفضل سپاهی، علیرضا سپاهی و امیرحسین صفری از معترضان دی‌ماه و پرونده میدان علیخانی اصفهان به انفرادی منتقل شدن و قراره توی ملاعام اعدام بشن!
طبق گزارش ها این سه عزیز آخرین دیدارشون رو با خونواده هاشون داشتن
🖤
@News_Hut</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/news_hut/69079" target="_blank">📅 01:05 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69078">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3738c7aef1.mp4?token=nM2gN_dp3jJeurAaawiVkAxg3hC3i6Q28XbkuI3yA56wkCZQgde5Me-if7RYmB5qzPDGUkDDhS1Bb5rVSpOWmoZm9QnBpLYAwk68Svk3-pXlXzLmU6kTnirbckZgy2xML64g6oQcy7WDD5ROmLLcvvQEhBLnYSrUqWLWI9owQUDYJcTPWk6G5mm6UjTwv2liFgD8Sg457PZustZ2ZZFDqUKd0oPBYZARDuPVSsJ2oqdJT13KFWlCWwOgNIxjN57MGT8kv0s0Rj51uzyn6lMKR3ordfupqD5Roh_MjyUwl5qt-fwVhwQqTgVFMrUUm8gcrLMW56Hd6VfnpAwFGWUYjg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3738c7aef1.mp4?token=nM2gN_dp3jJeurAaawiVkAxg3hC3i6Q28XbkuI3yA56wkCZQgde5Me-if7RYmB5qzPDGUkDDhS1Bb5rVSpOWmoZm9QnBpLYAwk68Svk3-pXlXzLmU6kTnirbckZgy2xML64g6oQcy7WDD5ROmLLcvvQEhBLnYSrUqWLWI9owQUDYJcTPWk6G5mm6UjTwv2liFgD8Sg457PZustZ2ZZFDqUKd0oPBYZARDuPVSsJ2oqdJT13KFWlCWwOgNIxjN57MGT8kv0s0Rj51uzyn6lMKR3ordfupqD5Roh_MjyUwl5qt-fwVhwQqTgVFMrUUm8gcrLMW56Hd6VfnpAwFGWUYjg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
پرزیدنت ترامپ:
همان اتفاقی که در ونزوئلا رخ داد، در ایران هم در حال وقوع است.
مردم فقط آن را نمی‌بینند.
نمی‌توانی به آن‌ها رشوه بدهی؛ باید شکستشان بدهی. و ما داریم حسابی آن‌ها را درهم می‌کوبیم.
مذاکرات دوستانه‌ای در جریان است. ایران می‌گوید: «خواهش می‌کنم، خواهش می‌کنم، محاصره‌ای در کار نباشد.»
سوخت برای مدتی پایین آمد. بعد، آن‌ها درست رفتار نکردند و من مجبور شدم برگردم. حالا دوباره دارند درست رفتار می‌کنند.
هرگاه کسی جلو آمد و پرسید: «چرا داریم این کار را می‌کنیم؟» فقط بگویید: «چون نمی‌توانیم اجازه دهیم ایران به سلاح هسته‌ای دست یابد.» خیلی ساده است. همین و بس؛ دیگر نیازی نیست چیزی بگویید.
@News_Hut</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/news_hut/69078" target="_blank">📅 00:01 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69076">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J-mlBoBg7LGd_WfyZ_qanIgn8flJfRQvXavUyTpRXkqdnoY1Hn4CivYriHBm7jwwQvVtRV4vZ4yzJzztp0UeRp1l6HOt2mjlaGJLHjrmSviVLvDSDTMv-YTWCRv_iWy8rEMmKsSFMwfNnZfsrJo4JOqr8TB388Ms3fv8CcvOrSVcW2BMlOsoOeOX-D-KJPMVEcPueUfHlAk3QUn78QaMFQhiLoIRml6oDoKUfp8CMP_rrHDXfcA01IFvbJNfQaIbSP4-mAhBPTrfQ0VyWoY9WWaZOJyHbhOi1tmneJXqWTKihaurGyi7pngan5pKr2NOW4Y4FQTjgJ0A2khphOsxRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
کانال 12 اسرائیل: دونالد ترامپ، رئیس‌جمهور آمریکا، روز دوشنبه در مصاحبه‌ای با شبکه ۱۲ اعلام کرد که تصمیم گرفته است حملات آمریکا علیه ایران را به تعویق بیندازد تا فرصتی دوباره برای مذاکره فراهم شود؛ با این حال تأکید کرد که در صورت شکست تلاش‌های دیپلماتیک، ممکن است دستور انجام اقدام نظامی شدیدتری را صادر کند.
- ترامپ در این مصاحبه گفت که ایالات متحده در حال انجام «مذاکراتی بسیار عمیق با ایران» است.
- ترامپ افزود: «اگر این مذاکرات به نتیجه نرسد، ما به اقدام نظامی قاطع بازخواهیم گشت.»
- رئیس‌جمهور توضیح داد که با درخواست میانجی‌هایی که از او خواسته بودند فرصتی برای مذاکره قائل شود، موافقت کرده است.
- وقتی از او پرسیده شد که تا چه مدت حاضر است به تلاش‌های دیپلماتیک فرصت دهد، پاسخ داد: «مدت زیادی نه. یا کارها سریع پیش می‌رود، یا اصلاً اتفاقی نخواهد افتاد.»
- ترامپ گفت که روز جمعه تصمیم به تعویق حملات گرفته است، زیرا کشورهایی که میان ایالات متحده و ایران قرار دارند و همچنین سایر کشورهای خاورمیانه، از او خواسته بودند فرصت دیگری برای مذاکره بدهد. (این کشورها و افراد شامل عمان، قطر، پاکستان، مصر و همچنین نمایندگان ترامپ، استیو ویتکاف و جرد کوشنر بودند.)
@News_Hut</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/news_hut/69076" target="_blank">📅 23:35 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69075">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">🚨
قرارگاه مرکزی خاتم‌الانبیا:
آمریکا در تداوم شرارت و ناامنی در منطقه و به دنبال اجرای محاصره غیرقانونی دریایی ایران، طی سه روز گذشته اقدام به تهدید شناورها و کشتی های تجاری و نفتکش ایران در آب های ساحلی و سرزمینی کشور ما نموده است.
هشدار می‌دهیم این اقدام آمریکا به منزله توسعه جنگ در منطقه تلقی می گردد و همانطور که نیروهای مسلح جمهوری اسلامی ایران در میدان عمل ثابت نمودند هرگونه تهدید و شرارت ارتش تروریست آن کشور را بی پاسخ نمی گذارند و با آن برخورد خواهند نمود.
@News_Hut</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/news_hut/69075" target="_blank">📅 22:43 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69074">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b46871a0cc.mp4?token=kXWrTwjTpthxxmIwUKqe_uEulUj6dNGeZonOEznTuy8WF6pnRd4grx4zr_cXVo_BXrYPzVABTQUSdrHVDwj70-S4A0_WLkR3qBCV7Whcn_YyeOH1Xkl5vHxe62V2Z-VWQUww-C-raN15e3D331aP5t7PANmY75aQWWctkMzuF3iNJoG4fas1ihAp48ihqlTs3wmIZpCZD-Jdadw5gSKQxykh7EwAexrMY7uwp5GqCy8iBzeYFRTSColEFlESrzgD7JxwNLBwKVDTiqhEm5ktr7qDLMJGl-flyFUViDQjwGg1uKtK8CFCaTgCrHDgEDl7druA8ksvAI9g9mVaMy2onTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b46871a0cc.mp4?token=kXWrTwjTpthxxmIwUKqe_uEulUj6dNGeZonOEznTuy8WF6pnRd4grx4zr_cXVo_BXrYPzVABTQUSdrHVDwj70-S4A0_WLkR3qBCV7Whcn_YyeOH1Xkl5vHxe62V2Z-VWQUww-C-raN15e3D331aP5t7PANmY75aQWWctkMzuF3iNJoG4fas1ihAp48ihqlTs3wmIZpCZD-Jdadw5gSKQxykh7EwAexrMY7uwp5GqCy8iBzeYFRTSColEFlESrzgD7JxwNLBwKVDTiqhEm5ktr7qDLMJGl-flyFUViDQjwGg1uKtK8CFCaTgCrHDgEDl7druA8ksvAI9g9mVaMy2onTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
زنده یاد مانوک خدابخشیان:
هر کس رفت سراغ s400 روسی, یعنی کارش تمومه!
@News_Hut</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/news_hut/69074" target="_blank">📅 22:30 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69073">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from𝗔𝗱𝗺𝗶𝗻 VPN</strong></div>
<div class="tg-text">💎
فرم نتیجه دقیق رایگان با ضرایب بالا
💎
بهشت سنگین زنا و افراد کم موجودی
👍
https://t.me/+LVbtmWdHFTdmN2Rk</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/news_hut/69073" target="_blank">📅 22:23 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69072">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from𝗔𝗱𝗺𝗶𝗻 VPN</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U4riG3zLdtgDnb3-dXMNNV8WLPLmJi92ewO5jONtSCKRs3ule5pO9dyMUmpGLPmyc9yPOR5q0SWlvOqA6M06sRLzDc0rx8cP86XRJAUSknZ8L27e0oLIOySZ2nKcaNKDR4OhxMSvhLuJ_LCp9E0nAbG2gCe34JNK80duXGospZt4UPcWycayc26rgN4e4S8wc5GHUbmGrCHl_AodHY5C5OknkV5X6O_Qo2omPlUp2OjQxLje1Lb9jv6dR0J46aTvquRh2mgVe8y8VA95TUfutWetLdUzXZfF6PzgwzAuaUqVS_F3C4OAzvUeDKNFIhaef42CwTkJB1FpHeYZ8svxyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💎
فرم نتیجه دقیق رایگان با ضرایب بالا
💎
بهشت سنگین زنا و افراد کم موجودی
👍
https://t.me/+LVbtmWdHFTdmN2Rk</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/news_hut/69072" target="_blank">📅 22:23 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69069">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d4dc96cd73.mp4?token=bI1b31KWJncwIJhg7K85gJA7AQxS52qpPI7qZ5d2DUPRO0ysAV-7h6uj3kJHjMz0zInPM-sYZgYJwpCCWnDjSvbTcoFUcaCeETon04FNf8u0mhCp7_aAXR4DTv6mS0j2N_bZpBLNl4wvPvAD_N9zG0Vm2x_O3-_-XAH0BeEli3lzmz0e3u5wioZ8MvGdKV0Aa3RDRu--4r4ojPjYtbRQ1gDpqtZ-qfrZ4-HfUeTAUqBe7tdgk7eaccGXJIid9QQlDkZISQ0BDfZK8-rkcjgHCDAyGQ-JJdgq42apDKiTS239cGtK5PldT45OBMguAGuPjUfaNWwa6Rio3AtYVPcTgQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d4dc96cd73.mp4?token=bI1b31KWJncwIJhg7K85gJA7AQxS52qpPI7qZ5d2DUPRO0ysAV-7h6uj3kJHjMz0zInPM-sYZgYJwpCCWnDjSvbTcoFUcaCeETon04FNf8u0mhCp7_aAXR4DTv6mS0j2N_bZpBLNl4wvPvAD_N9zG0Vm2x_O3-_-XAH0BeEli3lzmz0e3u5wioZ8MvGdKV0Aa3RDRu--4r4ojPjYtbRQ1gDpqtZ-qfrZ4-HfUeTAUqBe7tdgk7eaccGXJIid9QQlDkZISQ0BDfZK8-rkcjgHCDAyGQ-JJdgq42apDKiTS239cGtK5PldT45OBMguAGuPjUfaNWwa6Rio3AtYVPcTgQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
⏺
حسن روحانی درباره اعتراضات دانشجویی تیر ۱۳۸۲ (17خرداد 1392):
آقای قالیباف من دلم خیلی نمی‌خواست بگم، ولی شما من رو ناچار کردی. شما می‌گفتی دانشجوها بیان تا ما گازانبری برنامه داریم تا تمام کنیم.
ما می‌گفتیم راه این نیست که ما مجوز بدیم بعد بیاییم گازانبری این‌ها را دستگیر کنیم.
@News_Hut</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/news_hut/69069" target="_blank">📅 22:01 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69068">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1ab4cc3c2d.mp4?token=ZnBe7sYYlaYL3cnGvxMRD8BM-9uDGxZUcetz8iW9ePml55gN2nqs2GE4eZckM54lTgAwUkODzHAKWfC6ii-YWqdDz191ZtWFhPeFBPW_S6o0xwRMcnwQVsNHRHznMUGUeuCBdsQhc7sXL6MpARJZIyH54zvyKN4Lc1DHGhMyj5qRZEsQjm1QOPT83x6zilY5s_hr8UBPQY6Y6-KvALUhaKB8YT6o6dCOp4IsoYZ5Fqp58buZAyAx9VqKWrp0h0uY8GBtofi2GTRZcczOviM9XkpTOABlMiZhALmNrzYSmlBDKct106ERnJCbehdD7kz0W8cs1-rydiscQnqH0XQB7VCdoQgct435eWLVUMQ-QQPHswv1_SS6PF60K3VyRqfHrEWwqJ2NeTUTIbaZq0GizfsqcsVxDsr00soHlHl3lrPzxfrs4wS5XNzAKxvMl4xGDoiCPVL7gRt6ltXnfPmpNYtxpcbsWmYLOtdl2F0WsvOuu1oPOlK2hCJ_WMMI1LUz3R0_iezJ5VbeHhx7hHRQflk6NDGtsBX8kAu7D2xMwotbxL4bWYiVg9FcVYrvlGCaanNkVOpkCTWs-KM9lxkMLFIho6T1gei-AZJ8UYvn8fNYXCTY8QocJ0eIIKETDb_H1F4p3ObvPp8gT1dbbPjL7qmTM92_frdZ-p3hvilFlzk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1ab4cc3c2d.mp4?token=ZnBe7sYYlaYL3cnGvxMRD8BM-9uDGxZUcetz8iW9ePml55gN2nqs2GE4eZckM54lTgAwUkODzHAKWfC6ii-YWqdDz191ZtWFhPeFBPW_S6o0xwRMcnwQVsNHRHznMUGUeuCBdsQhc7sXL6MpARJZIyH54zvyKN4Lc1DHGhMyj5qRZEsQjm1QOPT83x6zilY5s_hr8UBPQY6Y6-KvALUhaKB8YT6o6dCOp4IsoYZ5Fqp58buZAyAx9VqKWrp0h0uY8GBtofi2GTRZcczOviM9XkpTOABlMiZhALmNrzYSmlBDKct106ERnJCbehdD7kz0W8cs1-rydiscQnqH0XQB7VCdoQgct435eWLVUMQ-QQPHswv1_SS6PF60K3VyRqfHrEWwqJ2NeTUTIbaZq0GizfsqcsVxDsr00soHlHl3lrPzxfrs4wS5XNzAKxvMl4xGDoiCPVL7gRt6ltXnfPmpNYtxpcbsWmYLOtdl2F0WsvOuu1oPOlK2hCJ_WMMI1LUz3R0_iezJ5VbeHhx7hHRQflk6NDGtsBX8kAu7D2xMwotbxL4bWYiVg9FcVYrvlGCaanNkVOpkCTWs-KM9lxkMLFIho6T1gei-AZJ8UYvn8fNYXCTY8QocJ0eIIKETDb_H1F4p3ObvPp8gT1dbbPjL7qmTM92_frdZ-p3hvilFlzk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❓
توضیحاتی درباره کوه کلنگ و چگونگی نفوذ به تاسیسات آن.
@News_Hut</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/news_hut/69068" target="_blank">📅 21:15 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69067">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3cf7ba0e57.mp4?token=pH1PhoKmzbFXkV8CYCAS7u9rFgpqtl1Fz_O9BT1ny8jUFnD3AQVSJWdUn2aOveZgNxRWdktzPd7ldbzPffjrMew0afikoXvnFJ_w4yB6AfYmAUxTRT5NeNrkEYM3v29u859wsM9nJhfLIatCz0-lKOPAnEI8UO2oDmx9K3WYpz3PDQ9QIYVX2h4WLYywq9n9sAGjUc8at3VwVB6dUfVepE-arvE1mxvjJ2Uurm0FR2z_wplCWBVhBbYsrY_SVBeQPaaEo27a4H16cHWENcHid2Lce8QVJ0JK54PGw_5d5bPv7HdB3Wgyamy12sbsxtX8XsdcnyesNX9YqXt99LGJDg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3cf7ba0e57.mp4?token=pH1PhoKmzbFXkV8CYCAS7u9rFgpqtl1Fz_O9BT1ny8jUFnD3AQVSJWdUn2aOveZgNxRWdktzPd7ldbzPffjrMew0afikoXvnFJ_w4yB6AfYmAUxTRT5NeNrkEYM3v29u859wsM9nJhfLIatCz0-lKOPAnEI8UO2oDmx9K3WYpz3PDQ9QIYVX2h4WLYywq9n9sAGjUc8at3VwVB6dUfVepE-arvE1mxvjJ2Uurm0FR2z_wplCWBVhBbYsrY_SVBeQPaaEo27a4H16cHWENcHid2Lce8QVJ0JK54PGw_5d5bPv7HdB3Wgyamy12sbsxtX8XsdcnyesNX9YqXt99LGJDg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
خبرنگار:
آیا نتانیاهو می‌خواهد که شما با ایران به توافق برسید، یا می‌خواهد به حملات خود ادامه دهید؟
🇺🇸
رئیس‌جمهور ترامپ:
«بی‌بی» عالی بوده است. [قدرت] ایران به ۸ درصدِ آنچه چهار ماه پیش بود، رسیده است.
@News_Hut</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/news_hut/69067" target="_blank">📅 20:46 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69066">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/73754cc159.mp4?token=BPut1sMyCG4V2Z4GjGkBcjcNg8GbsDxn9tLDW-xZGVt2HxBK94Xo6LxhmEZYaQr11J9rN-SvXwzbVUhSpJlKErY4Cs20NpZjLeYJnKPxrIH04Bl06T3COnxt_y58a5QzKrJjaWaZi34RzI04p6ixO4ghCwdOyWnPc9lpCL7qgMY394HivQOqbkld9riwP2iQZ_gJpwMdvlELWmP96Eq2YdyZiRtimXHSjBd9my6u1GGL5LGL74sH4K6crgeqxNHl0VZ4Lty5ymL9vlcTRlXjwnneCHsBaSHDo3kbTJX89dYkWv2Uixsyxc0uoCQuBKA9Y13bY2j9fLsKVM5p2a1S_A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/73754cc159.mp4?token=BPut1sMyCG4V2Z4GjGkBcjcNg8GbsDxn9tLDW-xZGVt2HxBK94Xo6LxhmEZYaQr11J9rN-SvXwzbVUhSpJlKErY4Cs20NpZjLeYJnKPxrIH04Bl06T3COnxt_y58a5QzKrJjaWaZi34RzI04p6ixO4ghCwdOyWnPc9lpCL7qgMY394HivQOqbkld9riwP2iQZ_gJpwMdvlELWmP96Eq2YdyZiRtimXHSjBd9my6u1GGL5LGL74sH4K6crgeqxNHl0VZ4Lty5ymL9vlcTRlXjwnneCHsBaSHDo3kbTJX89dYkWv2Uixsyxc0uoCQuBKA9Y13bY2j9fLsKVM5p2a1S_A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
خبرنگار:
درباره جنگ با ایران، از توصیه‌هایی که هگست در ابتدای کار به شما داد و نتیجه‌ای که داشت، ناامید شدید؟
🇺🇸
ترامپ:
نه، اون کارش رو عالی انجام داده.
ما ارتش ایران رو نابود کردیم.
اونا می‌خوان مذاکره کنن و ما هم داریم مذاکره می‌کنیم.
این احتمال وجود داره که به توافق برسیم.
اگه اون کاری که ما انجام دادیم نبود،
الان اصلاً حاضر نمی‌شدن با ما حرف بزنن.
هم از طریق واسطه‌ها و هم مستقیم،
خودشون درخواست دیدار دادن.
الان هم داریم مذاکره می‌کنیم و امیدوارم اتفاقات خوبی بیفته.
امروز قیمت نفت هم حسابی افت کرد.
مذاکرات خوب پیش میره و
احتمال زیادی هست که نتیجه مثبتی داشته باشه.
اما اگه توافقی حاصل نشه،
برمی‌گردیم به همون کاری که دو روز پیش انجام می‌دادیم.
🎙
خبرنگار:
شما و نتانیاهو درباره ایران هم‌نظر هستید؟
🇺🇸
ترامپ:
یه اختلاف‌نظر کوچیک بینمون هست،
ولی در کل تقریباً هم‌نظر هستیم.
ایران توی 14 روز گذشته ضربه سنگینی خورده.
اونا خیلی محترمانه از ما خواستن که
«لطفاً حملات رو متوقف کنید، بیاید مذاکره کنیم.»
الان دقیقاً توی همین مرحله هستیم؛ باید ببینیم آخرش چی میشه.
@News_Hut</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/news_hut/69066" target="_blank">📅 20:22 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69065">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TbWtomm7Bz7xNZnAsB8k0bnS2kUdgOJ_PgQOOcy4DYAzyKy3UlC5RN-L66uI2HvBWqD-fVb9ZiOfwi71W81ntwYvkh3lRQOn3T-SehViZG9Dc8J-NLBDuPo4SLieBPvV_EqFCLV84pw0PpAQ0m8IwK25SQ1Xsu2KDLgz5paAqDHDhqMdGXLrmlQvjKtnHCus3uw_gA0LMvB3j3DG8YKjoiD9-9Ivg_G1KrD4vJah7wSJQ3Vl4sykc9dCwMDhtyhp1QWN_7HEEtybqK0WGB9JzJF1TZv1z003kBC9k_2ngT7s_KW1TbKa4rfcdOBM4_KaVdfexc2z7u9eV9k8N9kViw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇺🇦
وزیر امور خارجه اوکراین:
تهدیدهای ایران غیرموجه و بی‌اساس است. رژیم تهران شریک مستقیم تجاوز روسیه به اوکراین است و با تأمین تسلیحاتی که از سال ۲۰۲۲ تاکنون موجب مرگ اوکراینی‌ها شده، به جنگ جنایتکارانه مسکو دامن می‌زند.
ایران هیچ جایگاهی برای وانمود کردن به اینکه قربانی است ندارد، چه رسد به اینکه بخواهد تهدیدهای خود را با استنادهای مضحک به منشور سازمان ملل توجیه کند.
ایران همچنین با این اظهارات تلاش می‌کند تا توجه‌ها را از اقدامات تروریستی روسیه علیه کشتی‌های غیرنظامی در دریای سیاه — که امنیت غذایی جهانی را تهدید می‌کند — منحرف سازد؛ اما در این کار موفق نخواهد شد.
حملات روسیه به آزادی کشتیرانی در کانون توجه نشست اضطراری امروز شورای امنیت سازمان ملل قرار خواهد داشت و ما انتظار واکنش‌های قاطع جامعه جهانی را داریم.
@News_Hut</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/news_hut/69065" target="_blank">📅 20:02 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69064">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9ec0fc6074.mp4?token=LAhberVkGoEOoiubvoMLpgKrHDYVFrhHhWlsvi02BNjFTaSoiCll2_7xYlbzD74vStsLa501CqLE6i4f14MFtft0rPWULCaacpxKKzxd36jRMEXPnlLXWaggrBVn7FhBJ-93I5c8aZXQCQIUs1tANFzOioWFqaspVfrF8dpeLClqnlHuOJ1j8vbXzhthkzC0b2z7vQhLhm-RymvVNDNvVrImIq1iMLvxTAwWFNTHtTqo5jubGp4t7ghMFgU3BP8Sq4X8cXCkPAQQ91kj5_eU41AXTUP31YJJs-um8S2XXyRwVeSIENzWKqT9iFwaJ6WpbKk5biZGe1rSkCq2JbXTLw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9ec0fc6074.mp4?token=LAhberVkGoEOoiubvoMLpgKrHDYVFrhHhWlsvi02BNjFTaSoiCll2_7xYlbzD74vStsLa501CqLE6i4f14MFtft0rPWULCaacpxKKzxd36jRMEXPnlLXWaggrBVn7FhBJ-93I5c8aZXQCQIUs1tANFzOioWFqaspVfrF8dpeLClqnlHuOJ1j8vbXzhthkzC0b2z7vQhLhm-RymvVNDNvVrImIq1iMLvxTAwWFNTHtTqo5jubGp4t7ghMFgU3BP8Sq4X8cXCkPAQQ91kj5_eU41AXTUP31YJJs-um8S2XXyRwVeSIENzWKqT9iFwaJ6WpbKk5biZGe1rSkCq2JbXTLw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
محمدباقر قالیباف، (اردیبشهت 1392):
در اعتراضات کوی دانشگاه عکس‌ام روی موتور با چوب هست. جایی که لازم بوده چوب بزنیم کف خیابون چوب می‌زدیم. افتخارمون هم هست.
در شورای امنیت گفتم هرکسی بخواد بیاد کوی، منِ قالیباف لوله‌شون می‌کنم جمع‌شون می‌کنم.
محکم وایسادم مجوز تیراندازی در کوی رو گرفتم.
@News_Hut</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/news_hut/69064" target="_blank">📅 19:25 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69063">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">🚨
🚨
🇺🇸
پرزیدنت ترامپ به کانال12 اسرائیل: اگه مذاکرات با ایران جواب نده، دوباره حمله می‌کنیم
«الان داریم مذاکرات خیلی جدی و عمیقی با ایران انجام می‌دیم، ولی اگه به نتیجه نرسه، دوباره دست به یه اقدام نظامی خیلی سنگین می‌زنیم.
زیاد هم به دیپلماسی فرصت نمیدم؛ یا خیلی زود به نتیجه می‌رسه، یا کلاً بی‌خیالش می‌شیم.
همه کسایی که توی مذاکرات با ایران درگیرن ازم خواستن حمله نکنم. مدام می‌گفتن: "شلیک نکن."
برای همین تصمیم گرفتم فعلاً حملات آمریکا رو متوقف کنم و یه فرصت دیگه به دیپلماسی بدم.
به نظرم ایرانی‌ها می‌خوان به توافق برسن و منم قبول کردم حملات رو فعلاً متوقف کنم، چون نه چیزی برای از دست دادن هست، نه چیزی برای به دست آوردن.»
@News_Hut</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/news_hut/69063" target="_blank">📅 18:47 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69060">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0b8aee1d66.mp4?token=RLGUczDz2anBTq3U2w2AJcD_SQSMZYD60Ciq7KppuVky_6FjDFP92-klUmOdGVJCMw1lQJQQo4ArC8xe9tCwJqeIcD-i1O-7VNEI4-PZBtHQXIzBn4YejvV4Z5NQ4N49gW7WzahuK1JWU4H2yYOsLLZAO371Z2PlT1EG4Lp6hCUDD2tk7kIXUI2bD_UN9RqGsb1IsRGkTc-GpkHI94VW8MBnAtc8kxQjTB1tIEXATKzN-rrzjDnmHIltpH74bB9pR3ShYSNi_o2nPjV9sGjsy4M7XOCiAhdADeMvqiGJC16XV4iI4YQwDntuVmfNwNraxCIk84Q9cup385yzWC2s7SSXlLPmQ5eD78_292d_4F-le1W87PXNghr3F7ekfhwaPHApd1FyFzHqi-jEreh_8fTT7NF0JPSi5EymtcZxwzFjFfBRdx1lYxm1U4zgcQ_vjKtzkiCPptdVLNuOCyP9yfaSlUGOqI1ilKNfkgMqvW1WCbFLcT7R3IOBflnJgwOiKY4OJBDTBXrbWILq1OYa0TCMaxBKZeEgJOilonRLC7Q0iAa_WHTapqe0ipK6Q9DA3KO687_HJhM94uEfwMQU4rLwzhxgTJYUBSvRYanSjycGUvJbPkqiMcftB5gNpOu4xbUqVTbUFxwUtAqxHikDvKvxHbx0wUNB8gpBrpWfwk8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0b8aee1d66.mp4?token=RLGUczDz2anBTq3U2w2AJcD_SQSMZYD60Ciq7KppuVky_6FjDFP92-klUmOdGVJCMw1lQJQQo4ArC8xe9tCwJqeIcD-i1O-7VNEI4-PZBtHQXIzBn4YejvV4Z5NQ4N49gW7WzahuK1JWU4H2yYOsLLZAO371Z2PlT1EG4Lp6hCUDD2tk7kIXUI2bD_UN9RqGsb1IsRGkTc-GpkHI94VW8MBnAtc8kxQjTB1tIEXATKzN-rrzjDnmHIltpH74bB9pR3ShYSNi_o2nPjV9sGjsy4M7XOCiAhdADeMvqiGJC16XV4iI4YQwDntuVmfNwNraxCIk84Q9cup385yzWC2s7SSXlLPmQ5eD78_292d_4F-le1W87PXNghr3F7ekfhwaPHApd1FyFzHqi-jEreh_8fTT7NF0JPSi5EymtcZxwzFjFfBRdx1lYxm1U4zgcQ_vjKtzkiCPptdVLNuOCyP9yfaSlUGOqI1ilKNfkgMqvW1WCbFLcT7R3IOBflnJgwOiKY4OJBDTBXrbWILq1OYa0TCMaxBKZeEgJOilonRLC7Q0iAa_WHTapqe0ipK6Q9DA3KO687_HJhM94uEfwMQU4rLwzhxgTJYUBSvRYanSjycGUvJbPkqiMcftB5gNpOu4xbUqVTbUFxwUtAqxHikDvKvxHbx0wUNB8gpBrpWfwk8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
دیروز بعد از 25 سال، قلعه‌ی الموتِ قزوین با رای مثبت داوران یونسکو، ثبت جهانی شد؛
قدمت این بنا برمیگرده به 1100 سال پیش، دوره‌ی دیلمیان، که ازش به عنوان یه مرکز استراتژیک استفاده میکردن.
سال 654 هجری‌قمری، حین حمله‌ی مغول، هلاکوخان دستور میده که این بنا رو به همراه کتابخونه‌ی ارزشمندش به آتیش بکشن.
امروز فقط خرابه‌هایی از دیوارها و پایه‌های قلعه مونده، ولی هنوز هم به عنوان یه جاذبه تاریخی-طبیعی خیلی معروفه.
قلعه الموت 30 اُمین اثر ایران تو میراث جهانی یونسکوئه.
@News_Hut</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/news_hut/69060" target="_blank">📅 18:14 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69059">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1028348d85.mp4?token=CSSw0JuZZoGivAq_Du3m30UBqxQ0GD8DeGxFZ0Uz7JwEx_pi-0JtTgsdt5DHn5YNfcVegmtY_XU0UDx1GC8qHKvPeS9jLXFtsG2uZlTTIn6xT1LVqkezZv3oDQb4HK89dxxEnLRnuiEdQW13kqfXTEgqLdioGX_F_-bN09ILtMtPHLRjJ7FxcJJpebem2HdbpdshcGNbFas83J-kHl1flGBvVxUuMYnmU2eGDw0eO2nch4crBWruOag9Ty1HPvzDM-SMalJdNLH2bGA1i7sm6HqsMNjHVicYYgndp4GziD0MTdBqygIFAlmfvYRRHNinJKere7LFqJxuZmQ7mf5T55Tw3Q4TJwjxluMR8wpmipiAGB3y8Kq45zs2t_m75PnrzhBQpSOvtPlYOedE9xEp-rh78rTmHD_rakYb9W20RNB6_P1Y483K8TwwJol0FANLkzyq2W3dKa_UHjcEgQhFUCTe8JKNqbqrQRRJOcVqAPLl086xoECtRB3WXewmbbgVGlKztD0XThZ8PQpIl6e0Nl-eX3mYm2xr2M2BEEdfiRmtSUdAEwjHLZb59Lh_StmzzhY7z3D1kOqrkNxCa5ukSDYLzQ_REF37QpEDXmCfrMOgmUX-WVrHnRJGF98b5nVhQjiWWWj3Uvg-wl5PTHUsrEihuFYw-tpC2j8eRnNJPFA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1028348d85.mp4?token=CSSw0JuZZoGivAq_Du3m30UBqxQ0GD8DeGxFZ0Uz7JwEx_pi-0JtTgsdt5DHn5YNfcVegmtY_XU0UDx1GC8qHKvPeS9jLXFtsG2uZlTTIn6xT1LVqkezZv3oDQb4HK89dxxEnLRnuiEdQW13kqfXTEgqLdioGX_F_-bN09ILtMtPHLRjJ7FxcJJpebem2HdbpdshcGNbFas83J-kHl1flGBvVxUuMYnmU2eGDw0eO2nch4crBWruOag9Ty1HPvzDM-SMalJdNLH2bGA1i7sm6HqsMNjHVicYYgndp4GziD0MTdBqygIFAlmfvYRRHNinJKere7LFqJxuZmQ7mf5T55Tw3Q4TJwjxluMR8wpmipiAGB3y8Kq45zs2t_m75PnrzhBQpSOvtPlYOedE9xEp-rh78rTmHD_rakYb9W20RNB6_P1Y483K8TwwJol0FANLkzyq2W3dKa_UHjcEgQhFUCTe8JKNqbqrQRRJOcVqAPLl086xoECtRB3WXewmbbgVGlKztD0XThZ8PQpIl6e0Nl-eX3mYm2xr2M2BEEdfiRmtSUdAEwjHLZb59Lh_StmzzhY7z3D1kOqrkNxCa5ukSDYLzQ_REF37QpEDXmCfrMOgmUX-WVrHnRJGF98b5nVhQjiWWWj3Uvg-wl5PTHUsrEihuFYw-tpC2j8eRnNJPFA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیو وایرال شده از یه هموطنمون که برق خونش رفته و کولر ماشین وصل کرده تو خونش
🙁
@News_Hut</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/news_hut/69059" target="_blank">📅 17:29 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69058">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G-RCOzvWw3Cp0z9lugb8O0eAG4D51l9jWw1aI1WWxg2smdrc2nj2hqHlOyA9c3R9SDZB3PhpymS9WbrfL6FZ11bq-eruoJKN9cJ2H0iUraN0s7Bdgt_rmEpXNB2gcm6yTX6-42l5jNf4USa6iY-omU9MLpuwvKMLOKv_QKp-NTCjXNDdUiZAmpK-AH-e4vbOCnIx8f6E4tw7h5NQmDgpx9gJmzZu8pDyNskb1flKCSudP-gVWqDr9WQ1rVBtoHeR0FPIwMN8_RyN5033Ion0IM_2tnhWVSghTFntLfDIWyeLbhXIi3xC49wvRQODZWsR-RI1Y0E6oN7fHfEvWyymPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇮🇷
قالیباف خطاب به مردم آمریکا:
دلتان برای قیمت فعلی بنزین تنگ می شود.
بنزین در آستانه لیتری ۱۰ تومان
!
@News_Hut</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/news_hut/69058" target="_blank">📅 17:15 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69057">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k2iigQYqUVVxqxOP7CNZw-c69IfYePqQZtVCGh6zq7bo0WNyM6HcW1VxEkc5F-tUEBiBu97k4_6rY6eZjnX-rFTTtLhsN3gQz8NzgruoeoaBfJK4mVfB9_OE7-dCKrSa0mMNjyOaiQOF4jFaryx-tPxafz46ilpu2NqbNw4C7GW-pKo7--0-sDrXP3pjjPfFXBenPUWvIS14ur5cwfnI311GJrQ0D677iv7K38B7SvycTasNYKOlYThc3cv_4rnAQDSg75qkfoOpzuH4qHo0PNxctYf5yhaXEpG1n0hIs7HSv6zzhPstxd8EERu_jjDsMCJiv4S-U6t6dR_BArhvZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⭕️
همشهری:
سران قوا با بنزین ۱۰ هزار تومانی برای «سهمیه سوم» موافقت کردند.
درحال حاضر، سهمیه سوم بنزین با قیمت ۵۰۰۰ تومان عرضه می شود.
@News_Hut</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/news_hut/69057" target="_blank">📅 16:50 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69056">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FKp4zNa2TYV6x_M-4PCadriT9Ko0RSgM-DUl3RbfNznrEHD4zbB_Cpf-Qhd6jlLOPCSayGI74a3QGvKpExOlHT3sZKCivJdxReo6RfZj1NzO-dqKUPhh30AvzbWoDiEFB_MbZIPygADmeuU8JZA6UVUVck4FK_11-ElA5wYHb8OZ8IS9EftusdkWo9SnfPVFhFGrg3asotFH4gx2WASOwvLbauue0kaCyZJ-VzP81WG1Pl-BWqyLoip5iLdwu53kUo3ngFtresb025AqNWY9vYGnylGvrxK6MqQKtvOmWRzVQv783Q2ctMXWbTr_qb-DpqogHB7aa83JdEg49f2pZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇸🇦
وزارت دفاع عربستان سعودی:
رهگیری و انهدام تعدادی پهپاد که از خاک عراق آمده بودند.
@News_Hut</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/news_hut/69056" target="_blank">📅 16:27 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69055">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/69d958cc0a.mp4?token=goQyKVyMOvk6z-2_jDOLvZKgX-pbym5WbMOsubmriW-vlJZxkuLocXpt_v1ujWkz3EifYfXAkYYM_-Ve2g9KYEjBqPOifvuadl0QnDLG-M4jLSYzjU3QGoaA93RtlKl3WfnEXB3qamqLhEopVuNShU0ol8_wfdF03xULAJjHV5p-Oj57nNefbU7n3wA2c8pcfTGCxOqv0HD1Xa8pGuOe4ShAJsV4dU0nMkqUdX1v7mYDJigdvyb5bIkKri-lrwNdWFnjCg4P4tDgTE87Rwi70G-Uv6BUkidQvee8riQPNJGISX3PHLqdyT95ZZyBEf_HwRgaIhXi1-MeMdbyDEPgSg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/69d958cc0a.mp4?token=goQyKVyMOvk6z-2_jDOLvZKgX-pbym5WbMOsubmriW-vlJZxkuLocXpt_v1ujWkz3EifYfXAkYYM_-Ve2g9KYEjBqPOifvuadl0QnDLG-M4jLSYzjU3QGoaA93RtlKl3WfnEXB3qamqLhEopVuNShU0ol8_wfdF03xULAJjHV5p-Oj57nNefbU7n3wA2c8pcfTGCxOqv0HD1Xa8pGuOe4ShAJsV4dU0nMkqUdX1v7mYDJigdvyb5bIkKri-lrwNdWFnjCg4P4tDgTE87Rwi70G-Uv6BUkidQvee8riQPNJGISX3PHLqdyT95ZZyBEf_HwRgaIhXi1-MeMdbyDEPgSg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">برخورد صاعقه به موشک چينى در لحظه پرتاب‌
👀
@News_Hut</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/news_hut/69055" target="_blank">📅 16:15 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69054">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e50eb610c7.mp4?token=MQevLwuiELwI3e1AOyt68yH49zCV2_Lg-w44i_f0B_QRvq9-U1uQhYsXRtwBEkzQLW5VBbr2pNkZwKoLNFgSGIp4hfUDGCSCN0hwgqx1YnGP8p1ImTGt6Q3df5f5GW6EvyLwBws3b4ZRhhUmMWnmtl8slvzcRaazbyuubk4k3EIBcbEg8WHG7y0kCEaUBwdE20FQBPSU_BxgrBwFopjTIHlIcvFyRc82XXF1cqBs2wofZFTUW3uFp7Ei0NAId3H90tNXmYlSu4GHBVlDpLY6T6iSRt-uEYAfIrn2te-AYlicncAytBRU7WpAjzwEBvInDUfmNDkiGiwk_Ij4_nHtiQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e50eb610c7.mp4?token=MQevLwuiELwI3e1AOyt68yH49zCV2_Lg-w44i_f0B_QRvq9-U1uQhYsXRtwBEkzQLW5VBbr2pNkZwKoLNFgSGIp4hfUDGCSCN0hwgqx1YnGP8p1ImTGt6Q3df5f5GW6EvyLwBws3b4ZRhhUmMWnmtl8slvzcRaazbyuubk4k3EIBcbEg8WHG7y0kCEaUBwdE20FQBPSU_BxgrBwFopjTIHlIcvFyRc82XXF1cqBs2wofZFTUW3uFp7Ei0NAId3H90tNXmYlSu4GHBVlDpLY6T6iSRt-uEYAfIrn2te-AYlicncAytBRU7WpAjzwEBvInDUfmNDkiGiwk_Ij4_nHtiQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇱
نخست‌وزیر نتانیاهو:
من در راه واشنگتن برای دیدار با دوستمان، دونالد ترامپ، رئیس جمهور ایالات متحده هستم.
این هشتمین دیدار من با او از زمان انتخابش به عنوان رئیس جمهور است، بیش از هر رهبر بین‌المللی دیگر. این یک امتیاز بزرگ است، اما همچنین یک مسئولیت بزرگ است.
بر اساس تجربه من به عنوان نخست وزیر، باید در این دوران پیچیده با عزم و اراده قوی و خرد فراوان عمل کرد.
ما تمام موضوعات دستور کار را که در صدر آنها ایران قرار دارد، مورد بحث قرار خواهیم داد.
@News_Hut</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/news_hut/69054" target="_blank">📅 15:13 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69053">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">🚨
🇮🇷
اسماعیل بقایی سخنگوی وزارت خارجه:
«در حال حاضر هیچ مذاکره‌ای با ایالات متحده نداریم و به هیچ آتش‌بسی تعهد نداریم.»
@News_Hut</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/news_hut/69053" target="_blank">📅 14:51 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69052">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JKt2I1YESKqaKvthm5vHLAShTCwIbGwb1U6KVW_Ehyv4pRYES0p_uGZhlxaLZHxmtOsz1v39FjYrE81gJiuTIcDOo6OSyVdyuzwUKI5HErq5hSLyBxiv3UczQJ99cjz-2cXmqZbLrjY67Cf4rlKawh3Q2GnAuBdrx0CQ_yOWoFmgWf0rgOkYrmF0TDb3G9fs57iwdY6yOo5XPtrv6BqU4COF_uBI575T-aD61CYBkuXvj0i07tovhfK64BN3yRrFvvjs-SfzveX-CXjCfABga05FlWCBP_-u13KuMVsnZYrFU2PTLXqVe5WQ6F53L-wYUEpZ619-xj5irDnZ8EL89w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇱
🇮🇱
🇺🇸
هواپیمای نتانیاهو عازم واشنگتن شد!
@News_Hut</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/news_hut/69052" target="_blank">📅 14:17 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69051">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nOXOxuLx8MUakmMwhMKZ4-asQPxz-lO3MdMD6WW1NZ2Ly7jANDP1nj8pAvwQnFghDRZBAcVRC9PXAmAJ012OUnM2XSzG8sxRQswsELyl0YXh65ZTKZrKyYgj2fyTp_eXjHdGA3VW0qL3R8EQRrwAtt45Sur_ancgeIT1LsUX1LKQIo7i1BSBPOA84g76ovS_xM7YWqvbyL6Qq9-WrEqZiJSFxDus1TRjgQ4kbIZC5uCX8VJP7FR11_d58n32o0SweO964_XM4rJrRk8HwyH0NLlpkO9M0ZaCMd4CrX8hJwy6LUHXXkfGNxsiQEcdUFAakSL4EI-kx4AkzRGLePVJ8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
کروز AGM-129؛ موشک کروز پنهانکاری که از «بالا» نامرئی بود
موشک کروز هسته‌ای AGM-129 Advanced Cruise Missile (ACM) یکی از پیشرفته‌ترین تسلیحات دوران جنگ سرد بود؛ سلاحی که بسیاری آن را «یک هواپیمای رادارگریز بدون خلبان» می‌دانند. طراحی این موشک به‌گونه‌ای انجام شده بود که از زوایای بالا کمترین بازتاب راداری را داشته باشد؛ به همین دلیل ظاهر آن برای بسیاری شبیه یک هواپیمای وارونه به نظر می‌رسید.
برخلاف موشک‌های کروز متداول، سکان عمودی AGM-129 به سمت پایین قرار داشت، ورودی هوای موتور در زیر بدنه تعبیه شده بود و خروجی موتور نیز به‌گونه‌ای طراحی شده بود که امضای حرارتی و راداری آن از دید هواپیماهای آواکس و جنگنده‌های رهگیر شوروی تا حد امکان کاهش یابد. این طراحی نتیجه تغییر تهدیدات دهه ۱۹۸۰ و ظهور رادارهای «نگاه به پایین، شلیک به پایین» بود.
این موشک با بردی بیش از ۳۲۰۰ کیلومتر، سرعت نزدیک به صوت و سرجنگی هسته‌ای W80، از سامانه‌های ناوبری پیشرفته شامل ناوبری اینرسی، تطبیق عوارض زمین (TERCOM)، لیزر داپلر و حسگر LADAR بهره می‌برد که امکان پرواز دقیق و پنهان در ارتفاع پایین را فراهم می‌کرد. AGM-129 تنها توسط بمب‌افکن B-52 Stratofortress حمل می‌شد و هر فروند B-52 توان حمل ۲۰ فروند از این موشک را داشت.
با وجود فناوری بسیار پیشرفته، هزینه بالای نگهداری، کاهش تهدیدات پس از پایان جنگ سرد و تمرکز آمریکا بر جنگ‌های ضدتروریسم باعث شد این موشک بین سال‌های ۲۰۰۷ تا ۲۰۱۲ از خدمت خارج و تمامی نمونه‌های عملیاتی آن منهدم شوند. امروزه آمریکا برای جایگزینی آن در حال توسعه موشک هسته‌ای پنهانکار LRSO است؛ برنامه‌ای که میلیاردها دلار هزینه خواهد داشت.
@News_Hut</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/news_hut/69051" target="_blank">📅 13:34 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69050">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IYib3wJbOYLRoh-JZFMjMDeiYa5fXOwZ35nhduzR964Q0JzdUUmOtSj4xQFd3sk9xEECF4csGwvELXC2IOyZq9eSwernTZnQHPwuV3nZcHoY7wyk57GmDhRYnPZbroczPYFihcjMlNetGQxjhCI8lCrMK-PyX9t7t4jQCgZ5q0OC7yUZIJtVbFhK4lH-ag98YeWCRcIRl6QcxKoV_u3e7JFortLNYtU9SiwVQx909CtTbzBBGy6quPEN3241N61ScU3MlusZMtkZhW98yCbrZq0idzp1qiNGbehQQSXn4J5cVZC35jL4hyupqEx5u6AcZq2xE9ttn1vLwmsw6Id6tg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
👑
شاهزاده رضا پهلوی:
چهل و شش سال از درگذشت پدرم می‌گذرد، اما او امروز زنده‌ترین چهره سیاسی در پیشگاه تاریخ و دل ایرانیان است.
شعله عشق ملت ایران به او روز به روز بلندتر و فروزان‌تر می‌شود. همان‌طور که جاویدنام مجیدرضا رهنورد به نیابت از میلیون‌ها جوان ایرانی نوشت: «نسلی عاشقت شد، که تو را هرگز ندید».
پدرم با تمام وجود، عاشقِ ایران بود. قلب او با طبیعت این خاک می‌تپید و باریدن باران بر دشت‌های ایران، برایش بهترین و زیباترین خبر بود.
او در ۲۲ سالگی، کشور را در شرایط دشوار اشغال متفقین تحویل گرفت و با تکیه بر میهن‌پرستی، ایران را به سوی دروازه‌های تمدن بزرگ هدایت کرد. اگر فاجعه ۵۷، مسیر تاریخ ما را منحرف نمی‌کرد، ایران امروز یکی از درخشان‌ترین قطب‌های رفاه و توسعه در جهان بود.
هم‌میهنانم، اگر به راه او باور داریم، مسئولیت بزرگی بر دوش ماست. برای وفاداری به نگاه او، ما باید ایران را از این فرقه تبهکار پس بگیریم و آن را دوباره بسازیم.
پاینده ایران
@News_Hut</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/news_hut/69050" target="_blank">📅 12:59 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69049">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/743c9eadbb.mp4?token=Mn3Ggr_TR9jLyIBMNmx_FnUHtmSknp_gQaCfeI5dCNH47rvmKYgxpVnW4plwOTRsBorIWqvxMA-tJVTYvjhkxK9nfnFgOfVMLRkuIzH8IxyiJ6Px1G-0V3OPE4BMYqmXbtanJoRODaQV9q5Fq7ALm2R7-AR3UnnMoVllAT80hOg_9S5OwOWzwsFfejmrj-Hv29XY0Ft-2HPQY7ClR3_xIr_CH2ceWu4bp6js-mtE4uAzBW7bLFKQnz4P8zqgI29JaWHumwTa9k5rcpXMKizKGyuO2qEH6ruO6sTSzjO1mGENx-1oScVkRmwu-c1AXCZHHOILLbBdommoHl9cwrrCnou_mLEeQm2naeugA0RKzqpVI4i-j5WdW4CG2LpQPlZpDSRoVimhURfibYQ7OIlc8y53jzdadNtEF6AVFEywsFKh0sMQcn7UoGZTtN4iAwTzWz68njwuTt6lgqnWffBlAQn5YRPAfWuNsbmmIt1FLV7sQiJIn-RMGVEPHpyIkvEt97UnllxnkfzPGAhqKKoVHAJUjDp5vzj2RKxIGBSPPUJNjTSsbZ_AMI_fg1Ft8P30W6FMWNM3EKUY2aFTGxtIJLrSLzfmYCPlUDZvRov4js0dvWEHWoQU4O5BPY9mU5tgvdA27GQeF3IZeLxzvM1m1QpV3cblmYUsdcKQO0kl7ig" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/743c9eadbb.mp4?token=Mn3Ggr_TR9jLyIBMNmx_FnUHtmSknp_gQaCfeI5dCNH47rvmKYgxpVnW4plwOTRsBorIWqvxMA-tJVTYvjhkxK9nfnFgOfVMLRkuIzH8IxyiJ6Px1G-0V3OPE4BMYqmXbtanJoRODaQV9q5Fq7ALm2R7-AR3UnnMoVllAT80hOg_9S5OwOWzwsFfejmrj-Hv29XY0Ft-2HPQY7ClR3_xIr_CH2ceWu4bp6js-mtE4uAzBW7bLFKQnz4P8zqgI29JaWHumwTa9k5rcpXMKizKGyuO2qEH6ruO6sTSzjO1mGENx-1oScVkRmwu-c1AXCZHHOILLbBdommoHl9cwrrCnou_mLEeQm2naeugA0RKzqpVI4i-j5WdW4CG2LpQPlZpDSRoVimhURfibYQ7OIlc8y53jzdadNtEF6AVFEywsFKh0sMQcn7UoGZTtN4iAwTzWz68njwuTt6lgqnWffBlAQn5YRPAfWuNsbmmIt1FLV7sQiJIn-RMGVEPHpyIkvEt97UnllxnkfzPGAhqKKoVHAJUjDp5vzj2RKxIGBSPPUJNjTSsbZ_AMI_fg1Ft8P30W6FMWNM3EKUY2aFTGxtIJLrSLzfmYCPlUDZvRov4js0dvWEHWoQU4O5BPY9mU5tgvdA27GQeF3IZeLxzvM1m1QpV3cblmYUsdcKQO0kl7ig" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
ایلان ماسک : در سال ۲۰۳۶ پول دیگه اهمیتی نخواهد داشت.
پول رو برای چی می‌خوای؟ برای کالا و خدمات: غذا، مسکن، حمل‌ونقل، سرگرمی.
اگر ربات‌ها و هوش مصنوعی بیشتر از اون چیزی که هر انسانی بتونه مصرف کنه، کالا و خدمات تولید کنن، دیگه به پول نیازی نداری.
@News_Hut</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/news_hut/69049" target="_blank">📅 12:00 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69048">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">و همچنین یادمون نره طبق اطلاعات موجود، آمریکا همچنان به تاسیسات زیرزمینی هسته‌ای ایران حمله نکرده، یعنی اورانیوم ها همچنان در دست ایران هستند، اون فتوای پدر بود که گفت بمب اتم نخواهیم ساخت، ولی الان مملکت افتاده دست پسر و تندرو های سپاه، پس آمریکا حتماً این رو در نظر داره اگه نیروی پیاده نظام برای نابودی تاسیسات هسته‌ای وارد نشه، ممکنه از طرف مجتبی خامنه‌ای با یک سورپرایز مواجه بشن!</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/news_hut/69048" target="_blank">📅 11:18 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69047">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D_uGoG-dIB-stK3orujLCEaEPZfv6xVdWu4iOCmCjnG4xlYmT0Pa-rRYNmP3nQ9qUDAJpLyXa2EVpOMPxdOH07ShXWjvFEDcKcYXds85315883tjFHlJqBoLJTlroWCnrASn1tFs0OnQamKdsErRobpPeno5p6fniCqQ7U8x1Kxju5Zhv0kJM5eBuyeK3VofuGu5cPx3Kds9JaDeLCFQOgl2oEzZ-zXN3C666X6B7TyyLWlr94Fa4I8NmKvqinxy7KPUOtL8d7hFWF6YN19Lw2Xrf2MT3SPAj8ViTb0emb3n8ZR_YAiM4piJE3GI-9H2IamqPeCP4MGECrSYRJ6iNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
🇺🇸
وال استریت ژورنال:ترامپ حملات به ایران را متوقف کرد؛ در حالی که مقامات در حال بررسی کاهش ذخایر سامانه‌های پدافند هوایی هستند.
ترامپ برنامه‌های مربوط به یک عملیات هوایی گسترده ایالات متحده علیه ایران را متوقف کرده است؛ این در حالی است که مقامات، مسیر دیپلماسی را دنبال می‌کنند و نگرانی‌ها پیرامون کاهش ذخایر موشک‌های پدافند هوایی آمریکا را مورد ارزیابی قرار می‌دهند.
با وجود اینکه ارتش برای انجام حملاتی که می‌توانست تا دو هفته به طول انجامد آماده شده بود، اجرای این عملیات به تعویق افتاد.
در حالی که ترامپ تأکید دارد ذخایر تسلیحاتی آمریکا همچنان بیش از حدِ نیاز است، میان فرماندهان نظامی در خصوص اینکه آیا کاهش موجودی موشک‌های رهگیر «پاتریوت» خطری جدی محسوب می‌شود یا خیر، اختلاف نظر وجود دارد.
@News_Hut</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/news_hut/69047" target="_blank">📅 11:15 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69046">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f112ef275e.mp4?token=cwTGlhaBJ179oMkKntMLaZtBO8tpfdcLFiyJWTeYlds79R1HLAb10JA2HXmfMpb_vhXJVzH4A8cN8io_uW0C3BQXOIbvpjEqyyumT_Z4mTAfJOyIaABMpTo2sl3R9i_XYFeDClj5umDwFNgg330zlyUYIhOn-hq5CoDdn-CZx03ZvCNhNGWTZWxcA1dYDKknnZ7Wk1nJ-xIB9cvpSPVPO6bA05ykrx1sAL0HD0eQHCdYwmStGA_0FflduFyXMGX0inh58PB7k0n7GK1PLpadmdQBSrLqU7cS11xDOlS8zP6BHYODX00TAICP2r879pLNuRCU2-E_jwT8Or6la6yPfA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f112ef275e.mp4?token=cwTGlhaBJ179oMkKntMLaZtBO8tpfdcLFiyJWTeYlds79R1HLAb10JA2HXmfMpb_vhXJVzH4A8cN8io_uW0C3BQXOIbvpjEqyyumT_Z4mTAfJOyIaABMpTo2sl3R9i_XYFeDClj5umDwFNgg330zlyUYIhOn-hq5CoDdn-CZx03ZvCNhNGWTZWxcA1dYDKknnZ7Wk1nJ-xIB9cvpSPVPO6bA05ykrx1sAL0HD0eQHCdYwmStGA_0FflduFyXMGX0inh58PB7k0n7GK1PLpadmdQBSrLqU7cS11xDOlS8zP6BHYODX00TAICP2r879pLNuRCU2-E_jwT8Or6la6yPfA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
در ۲۹ دسامبر ۲۰۲۵، خودروی آنتونی جاشوا در نیجریه با یک کامیون تصادف کرد. در این سانحه، سینا غمی، مربی آمادگی جسمانی و دوست نزدیک او، جان باخت. جاشوا پس از ۲۰۸ روز دوری از رینگ، با آهنگ «نقاب» از سیاوش قمیشی به یاد دوست از دست‌رفته‌اش بازگشت و در یک کامبک احساسی دوباره وارد رینگ شد.
@News_Hut</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/news_hut/69046" target="_blank">📅 10:32 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69045">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D3R2NrssRT-b-ojWfmvQc1yqJykBPMJSsgRDyhi6Axn_X6-hYhlqDmW5NEWfWt3cW28dSK8dsNLnGkDDMiRmnPTirJ4ccnVcUNWXllQ34JBsWYreuIDlOiZwLZZzcU4W3xV_ZXioVgMw1uJnAX-AawKgGcIw3jxo9fJhe-Ld6Ojs-7cHHJ3IYegNHQGptkz0Phf7_X4BELoyqMeZrPerR3H3RKDIaIRgM072VdW-fUtCZhL-x6Ih1xKpfK0rJ5wz1TrdrNCVO2PNXr5bhSe59Ldzk8OBSf0wGAY4LzFmT7JO8JFkFH3K-EO_hSQ2PolZCAPYZwhoYOoJML-OqclOBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
دوش پرتاب میثاق ۲ / ۳ دست نیروهای رژیم جمهوری اسلامی:
⏺
نقاط ضعف میثاق-۲ و میثاق-۳:
برد و ارتفاع درگیری محدود
وابستگی به خط دید و اپراتور
آسیب‌پذیری بالای نیروی شلیک‌کننده
محدودیت در برابر اهداف سریع و مانوردهنده
عملکرد ضعیف‌تر در شرایط بد جوی
محدودیت در مقابله با پهپادهای کوچک و کم‌حرارت
ناتوانی در درگیری هم‌زمان با چند هدف
تعداد مهمات همراه محدود
فاقد سامانه دید حرارتی/شبانه پیشرفته برای کشف مستقل اهداف در تاریکی
@News_Hut</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/news_hut/69045" target="_blank">📅 10:01 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69042">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/mvsWHPUgVh24fJoQZtL3C0rUl0BWVyxws8S-eAeAdIHkXqdUfqK8VYTHx0RZDSdiKZLXu7oeJKpuZUZMOQQVAx0K4T3Pf-vL0KR2xpwaOnNStvDvYBxfe9hRKOTe61M6ZiEuqGbw8mwSRRqDePmRGI6xm-Kd4fG3yH5_r2HGbNUNq2hgf-D-pHBp8kIgqC8U41bJIpZTEGytVL1T8VhnAEhMsFt6BbFqDXrV6GzcwmVenlPsYMXXESPH1ldYx3CtwZElE1bOOZqAteipuwyJDuWK3fD9-5EmzSBhnUwANPfZo_89aHVpf9TV0VsBa9dxNORUVqu4MQFNuOBglFJa2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/XdooBemyMmlI-ahD5bO_YAC7O8w1sba890sq9KvO0DFvXwJSEfRM9Oqvf66o7LhBV2s2r_Fiug9zoF75dpFwMA8usePKw4LOquzUV6DNy8TeR8YATKQJhNIGvSY1Tecu42zdgvZAur4il-Q5ApJ-_lnYI80meiNqiCr_0Kd91C3z7FEAXsXbEq7HOUksmjhceneDrBoRwwV_5hSUJNHolilGbj-ToI_8l-EpVndMGCteYifLrwB1FmSxNddZtN4EUgzBo4r3jF3R7aEdpxZ4i5oXLg7Hsgw7Yvo67gjp0RGv3B38NRt6TS5XVMwFfQCb4BpWyvR2easJiyzuUS6q0A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/23b96717f5.mp4?token=WICax4ntFpnnDZ3W_uCKbqZSw6k6iRNP2COrfsTWcfhb0kQc_uVNGP-rYsBRdR_ciwO3HEx4nMNjQ942Zg7OVbIZjwRMkhv1wX_NELiYt8RckCdalG6AIXFcM51hCzK97bJ9ViseitSXYrwNigG26aXIfcKjjbooVleSesBI_P-bIVx48J9HachiyAAclKTy_gBER0zWDJ79nqa0-NEV9SZXPIe6h14my-wlg9WPwqrGAlIFzLV00Z6YeU0AwXzqDrKBvngw6JazCq3EZlUhTuSBCPWzw84qInjtZ3FOpmlMuknfFcZEAtMH1VczKiEdYyvntbVJSIcBeMoJup3MIw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/23b96717f5.mp4?token=WICax4ntFpnnDZ3W_uCKbqZSw6k6iRNP2COrfsTWcfhb0kQc_uVNGP-rYsBRdR_ciwO3HEx4nMNjQ942Zg7OVbIZjwRMkhv1wX_NELiYt8RckCdalG6AIXFcM51hCzK97bJ9ViseitSXYrwNigG26aXIfcKjjbooVleSesBI_P-bIVx48J9HachiyAAclKTy_gBER0zWDJ79nqa0-NEV9SZXPIe6h14my-wlg9WPwqrGAlIFzLV00Z6YeU0AwXzqDrKBvngw6JazCq3EZlUhTuSBCPWzw84qInjtZ3FOpmlMuknfFcZEAtMH1VczKiEdYyvntbVJSIcBeMoJup3MIw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👑
🤴
امروز ۵ ام مرداد، سالروز درگذشت محمدرضا شاه پهلویه.
@News_Hut</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/news_hut/69042" target="_blank">📅 09:15 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69041">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OVF2Llm8HgnjXYqUkH9Lom7qn18pbOkyk6iQjhmRQxRCKlfW-GUIWPqzIS0bz5kWpIO56PbqV0adUiDqlN6tczsj8xC-6H6dcdubpQXaF8nqMyFCRz74ORhhyCMccjq-adJxDW6VpdlkuBdfWTFG0gz7-U-zBWLZ7UchdSgqBfit73tLkpnrAH8TcSbGU9g0vgSiniLDOQoSQhULm7d-zETWRarrd6q6LKmIOw903oQZ-hNBsmiYtaHltkt2n725d5XQ5sxXjljRN14ONc3-d7UOiArVdqUrkThD0lhsXvE6kWpISYfl0lP7UWWfZunQdNmYyWR-JWvDHbbse6yX9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
ابراهیم عزیزی رئیس کمیسیون امنیت ملی : هر حمله‌ای به ایران همیشه هزینه داشته و امروز هم همینطوره. آمریکا و اسرائیل این موضوع رو خوب می‌دونن.
اوکراین هم ممکنه به‌زودی بفهمه که ایران هیچ اقدامی رو بی‌پاسخ نمی‌ذاره.
فهرست اونایی که درباره ایران اشتباه محاسبه کردن، هر روز داره طولانی‌تر می‌شه.
@News_Hut</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/news_hut/69041" target="_blank">📅 01:46 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69040">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EEMGOTUuy3TJiyIqgkkVPqNmMrBWxXJDwHFs9JRkCrpJRiInZ-yXiquoOhwhZ4xfy1KBFdAUFLA1VKJXhGM0hGxiP7bga1Xi500G45-BmxT7-_n45ORpTfOAXvqJ2woqIT8mOCDNFbX1gVRoSLoWeVFEHQTDsWnEdCiskhPbMATVntnWAwj06ztJMko0ePyuXNYVxMq072dk2vophcckPuB56pwqb14eAsgYiNu5IMhWSPVwnpPUNPDJVW2lB8x_yo95ZQ29Evni5k_lgwfGQ1yNRsCfbLt36oFdGHC1w8Q-ervCBzGKwpSHHdm9A3KTuWnySvAi_N1XBE_7JDgEmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
ترامپ آمار تلفات نظامی در دوران ریاست‌جمهوری خودش رو با رؤسای‌جمهور دیگه مقایسه میکنه.
@News_Hut</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/news_hut/69040" target="_blank">📅 00:50 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69037">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SEW1t_7m9TmJAFBXCc0_pkmP6m76e1rBuRyVHu49NdeIjiDdVf-sKzb-NTKDX1VuodTd_1xJ5Qg9gv-6qbRE_wgJ0qCjhqEMf83zdxkCFCa3vL5S8jZ_ChK4XtKc2Xmdy1pYQ7XxOFNYhVs78u8VbD8-TfbisxSMEdoe1l88agNxgrI_CL9pMnULPvH8QRu0GT-QwAZSob9ttMeklCF3B0KMNASF96GOpkhKSI-dO-VfjwyG9hXW8Q5aHHWIVdKzwOq0M5yO2wXs5ebM199aVY_IzyT2nqW3sGN3l75lyhqwu3ySPKFldcD8D9NUZZ9XDI0_JD0jvKSdn547cNVHtg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/O535EIYf84lJdVs_mF7cMnRc8TAUYd5O55R_dqm7Se9hssbninqpQ6s4PJfCHm7ghsn-1rPqwOFBNuLYsHE8ZX6MHmO3Zx6bOBkvVA7kjVr6Hgk-OA8Q2R3b0s1Z_qOQV4D60CXtYh3QuXYUDCF17HjM1StabCbvnI3cVeQsnmcTMGeaZF_jt6VfyinqvCLBqQYHI45ezjV_TpJXdFjNHrm-Elu2aLxHedToMgeM2N2lHFpd_5xdqSb5n0QxqW-Uk-tZYdLbPwAX3-FSDPflMm2GmNYZCuFdVEtZl2g8ifeG4FPtP_jiAOMMmDEo0bT-b9aUUn58w2myxPF_alBE9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vx6icn5Q4lnVJlK7mKR3nLzNnApu2CokKIg9P-ibmCauROKJMKw97vYJRUvNwMlzieXp8iQqI79b7RhJ3RTMIclvDaN589tsE7gho5eyRvp1yQlEnLHDUMSBDqp3VKBEMXNMpNkiCdOUeHD_giCvXP00phEu0uMwtL4Cx4h-YNsYa9HuPpI4ka6pj3YE5VufjT23tI8AcEmTAKXhTwYS1J54HlMTJO36QbHWG-TrB1rvo1gdytTZSwjJ16LqhJKbXw56z9L5t1uVKNvcGE0X0YIgPicnPM7EB6B8h4A6klSElrpzUhkyx4LEHEohW9NRdOfN2EM5_tM7nWP9Uyx9eQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇺🇸
ترامپ در تروث:
- به طرح اعتماد کنید
- وحشت در واشنگتن
- آمریکا بازگشته است
@News_Hut</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/news_hut/69037" target="_blank">📅 00:36 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69034">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SsOhMS4dd43ezGrXyOIXv5Hv75Cc3zNGbPGuHlaGLKuNDca2x486wKGhG5QyxEFiOeAOi_ANAranFayrpNC2iKpqptVTPuiw8ajoAxjIsEojwaMLmoiYyLQ0MH0WHMnhFKkseSFUmRefUIRWIv9nH5EhNu6vBfVj2fI6I9AJlohIqbX3iYY-OfrqmqInInG7NO-RZzacm3Y_CEwrXzUxav2sv8AU628H0pyRVpGjDm1jYHr0rikwaAt5LNCDB88aguySjBITOLE2VUOebfqnlB1cYSMgufN1-2Gx5ohyTiUrN9Ejj_RMZhbah5MrL0y1AE2S_F2Kfbo3YgZctcRbkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uHEajGyjxyisWOylUGZjOnVz1lIuBYK95aHUw6ArxdcNfgGxG9fbYF2FGlMxw600qpJyYPcocxV73JwECVOjCUQAmnjQae7387u8yANLqSQNBK0aH7w_dJSPevKUYfypTzhEypxJ_IeMQSxCkbK8zWYMT_7Byr7mbcKXiwDoIQ1yVb3Bm6ItYSWBveU59ZszyCNAI-BBup-70P0tuoUqbi-fI856AQZF_WuYQapYvlleth_WhdjjNZf4FtX0yEqW5XKltHRDGi9ynhLhZYRuBJKATXhiNFo2S9tlU6egNRovS1SJY2qNumcn9Id5ZVaS5cTmy7IjCmo03jCgVXlkYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/h3IHjwcYQNQD88zOWlyRgJo_20lnWKNLvkvkctNZ4K6K9LvMKuaSd0YqXnPZAxfXg7ziGSAf5aptKAUYRF4w1HnBvJWkNagI0TczlDPMepYvR3r2t8p21vXwQdorzBBmdU1scQxmztL5UN0_D3CtGlUYnQJ8bgsoBEJbkud9DjcOcEOsocwtiVYt9Si7lHnfUH-ST0uA35HW4Cyz4tBvtckQdjbgW4urwEP-U4xM_jzf1vC2H1BLSmdhDC8k9Lin5SulyzT2bRW9MpzHIH-KfS_HtzknJ80ca0LEJ3n0fT8Ks_MSU7HyLvCOXbEK9pdj6oDsKeANdAz0B1no6jTWVQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">املاکیه دلقک
😂
@News_Hut</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/news_hut/69034" target="_blank">📅 00:24 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69032">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oLTbbtInDUey_6Q_IMDaBb6bAppyDzFG_tmjME1sYdwX_u0amIthupo9AAccmuZUjbB1zR9kYjf6xuUs1yKOUCVfkaZWNIlUWIzHyLE8X3TXSRA8YzYaGLaqjb-aQgg62_T09kqPCzRX2f4zFm2IM4l9CiuHTaZsbSqQ1pQJA7p0XYbuEHdjcJlRxZoAslRMt-bfBX5Aa1L2JN81vbWwVYKnLoO8Sw4mm36pD1rcqDosGgms1GzQpuSXmecwK2FQYEob9_Ey_7Vu7vAUxvu7DC3Cg53froymBXT_NradS1NTsb93YpV1FbCXZnc610L_dkXIKeZNpA1JTsw380mpIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/W4ljuuOWaIG9EoxmjdCjWeyipZHhlTFD0vjumbN7w989uD2YJqK2vtCywPVQS0xoSKw0htUIgdufrwfdvFxEAoSGy_ezJZ9jwdvLKCDxeK24nGAAVG4QiVjpfzD_jKrEkmovw5EnHzwOdmhsLu0zozq2MylBULUPDO2LKdCqzBeenzWxnNXOe6N7lFKHdrwVI5-WmHXSRH_iiJnDdDHCv_DHYoa5GFqAL2vHI7x4mmGGnVYdssl44xKdVB6WVSr7-hk-z21NYDYQ0udAxVS14WAbC3AtszRcUsGxpJ5gxYVTsmW23jIg-kiJH6gtAQOxtgT6FXhdBXypZZdSF19rKQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
🇺🇸
همچنان ترامپ
@News_Hut</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/news_hut/69032" target="_blank">📅 00:17 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69031">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">رفتیم تو 05/05/05 برنامتون چیه؟
🧐
#hjAly‌</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/news_hut/69031" target="_blank">📅 00:00 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69028">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/o7HaKlR9Uylafvil7hTQRBn_9IKtDF3cg_996lO8Dr6PDXySaUbZUeeI699T5b14sche8_3822EzhtyITmRS-7ceN9Ph25I-83oKU1ilMh1oYZlQsjWNUA9nJLltscXhDZjhhTQ479xcqraO7Ay6104eZO-Ncm1YMVVEf-d545B_k8toDZpnbsog_k1tBlntBlgGZTvamH6kV_qUh4MmmzP2GRwdf5lonzsEruSInOMAIVlaRiGYPLCdS-ZoroG6GY4lm1FkstF5xqajnZ-R8fRl0YfdSpbv-TVdZ21QI6vxkFO5oDrr3oPmKMmsbGjUjUsyYNLHl6OM55yy6-2JmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nSNrlCegVn4frW1ofXVZ9X9rzjbvPz2BNY3UqxrJiID8Tn01ExACXiAFxuZ-yR7z-lcAhbErwzkZLZMiM3ivB-7r8Wb-QYrPf_07tmEcn91U-yUoZhKj_KYdvbVmGtGfOIAkPNW1fxssZSFWhMaS2-Nx97CkN8g8OxzcvsII8ASTdnEqf8nptBaWOwZ_MT1Qjy7A09pFcShWu12Iw05AsUki0qQzjeyORB91I1q5D67665UAXk0UlmWNi0jp3nYMr3nmLeSXr4cnO2wSWr9zxBb0BfD7FN4Kre0NwMMGEWVuv-ZZQOu5BzkeWDfEf88qostj6fpbB6l1CSddx_wdHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/R4x_dZtKBozlDiV2b-6w1Zu3-POJjVrwsZVefOeucWkyubaKKL3fPiWNQWtVuRU4xd_e-KkNagn_fCvmxLVFbm2FamsVcFm-clrqhNon8MsUrtWmmgcNv9WjAhZKRNuemz3ElLp5bQq8KOOQFjLsDRCf2naoHIRI3SVBmjxlL3-1V4UgHS1Esxff39Jbpt4PMJFccin7N8mnpVrYKwUhzqnZ4iYKoErLIz_N_vcaNWfIHl4V_0673vHkM8lVKAJUt0H4OMWIune-Ms5TCwHG5u7sBL_DwCzYknNMuUn4TdbyusSrdQiFag31udmj7MJKY-kaAPSqjaNOhrnLqsAt0A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
🇺🇸
تصاویر دیگری که ترامپ در تروث سوشال منتشر کرده!
@News_Hut</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/news_hut/69028" target="_blank">📅 23:28 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69027">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">🚨
تصویری که ترامپ منتشر کرد: حمله به خارک  @News_Hut</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/news_hut/69027" target="_blank">📅 23:27 · 04 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
