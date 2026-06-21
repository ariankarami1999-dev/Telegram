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
<img src="https://cdn4.telesco.pe/file/O1ufRcbpQuYmcEa_PWk8cWFAOxOdfa-dHNLw0QOpTEz4L00tD9Sy-ssiK_KdfWVQ5PzVQH8AUO8nM-umZ5h1Qdgrukb9a2Tb5gJnGMtZftCqRhnDQ4g8b1MeUJwI7OGuHnk4bM7dRPgcjZCxIQjo1PIQFuLj9fJxs7cYRFGzR_3iMW3Ng3oea7bPVYI24lzsKEeEJSNoUj5JZ3Lb4oHDMtJIr2ijSNp85Puu_nqL2lBQ3kUbSwHGK44UBDMH8SLiiku1oBFkXmnPNNiZq8zLeYZjF117xWQMiTmZ87YLTpG4FYjGj7ZjK3VpCfAsl0jTWtXt_-WJYeSJt2UlshduJA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Persiana Soccer</h1>
<p>@persiana_Soccer • 👥 313K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@ads_Persianaaپیج اینستاگرام:Instagram.com/Persiana_Soccer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-01 01:19:55</div>
<hr>

<div class="tg-post" id="msg-24030">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/77de046aa0.mp4?token=Ux0iVJ-cGlfIVfnE5zO6HVLr8VxLDUUePhOMzNoVlJuxP1BHiQMmbZfzsau24je7VPNW9agZ8Czd_Idw9G-CV1XjxVv3SRaIx5jjW7KNlN9GIjOnpBAxu3J-2uF1hNxcIfFeExozIf0FGkv_qzlaKcafcpxd5jA6cIJzi7kgE-RarlL82U4XyX2JOSpY45yA8X3QB9gI2hqjuYkJOuLRGg61lbHiKhV3M8oHbmxc9Dmr7QlFl5n9bmizpSDHirfWF2EzZFi_lQWz3I_4eJpAP8L7AZv5Lbhtplg3kyoIjL-cW7znbMddY7fG67MmWHRDifcS8Uug1WJQWA1SAwKWbw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/77de046aa0.mp4?token=Ux0iVJ-cGlfIVfnE5zO6HVLr8VxLDUUePhOMzNoVlJuxP1BHiQMmbZfzsau24je7VPNW9agZ8Czd_Idw9G-CV1XjxVv3SRaIx5jjW7KNlN9GIjOnpBAxu3J-2uF1hNxcIfFeExozIf0FGkv_qzlaKcafcpxd5jA6cIJzi7kgE-RarlL82U4XyX2JOSpY45yA8X3QB9gI2hqjuYkJOuLRGg61lbHiKhV3M8oHbmxc9Dmr7QlFl5n9bmizpSDHirfWF2EzZFi_lQWz3I_4eJpAP8L7AZv5Lbhtplg3kyoIjL-cW7znbMddY7fG67MmWHRDifcS8Uug1WJQWA1SAwKWbw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
فیروزکریمی‌پیشکسوت‌فوتبال: بیرانوند درتاریخ بی‌نظیر است ولی لطف کند کمی تنگ تر از این باشد. این چیزی که ما دیدیم خیلی هم تنگ نبود واقعا.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 1.01K · <a href="https://t.me/persiana_Soccer/24030" target="_blank">📅 01:19 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24029">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iQGjXLVMo99Hh9dzqGQc3hYKW1CRQ-oO14AuDnHmZvPdHIEuKOesqqoxssGgGswTX7qg3giCz_vqNdpdzd6fk04XzOcXhWZzXdutEIOTU2GtkP89yRiUbQR-zoQClkYSpuC18GSoNSObyLjNHYqEwULfn7HXPsMWviOB0yw1o5rJQFI2R5E03mXwWgyPJMSGT264P7AnnggUnXLlcEsXhQjEnQkI6nXcf3TiqHRAll9t0BXgfQhCV16fhYNsjvnGrX_AWc3MQCYv_5JUmUvdo8IVoaqp3yPUT3Ray7C4QWzv7oEgQLQIG6MZ2viGWtxHAU9-lUzVUaUCACLLXX01Rw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته‌دوم جام جهانی 2026؛ دشت یک امتیازی شاگردان امیرقلعه‌نویی مقابل ستارگان فوتبال بلژیک درشب درخشش‌علیرضا بیرانوند؛ سوفاسکور بهترین بازیکن زمین رو بیرو معرفی کرد.
🇮🇷
ایران
0️⃣
-
0️⃣
بلژیک
🇧🇪
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/persiana_Soccer/24029" target="_blank">📅 00:47 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24028">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dSthk7jnKtPoNB0hqhDl4eC2tu2v97eQvwdYEJlwU0rDNtQ_trbehlgSz0C7912Chq_X9g8CvpWkNVKeSwOw_KQ3PypVenIO3fwBXjZTaF1_Q_zSa3pSL5tlSo4uUaAtx_jhqp-qXZZ-0HFgTvLCuQSwlLFFaLa20X7IlORhXIta54eC8tE0v0sG8m7LkqlLfAZ_4UZK3Ggu_aH2LccCeFi1JgCFg4-hhfHpTttVyvEq6u6C8SqsuXYoyFctPQHOuE-ZwI8_VVvlqzjAGYf7gZNCkketjG9V8i-jgVXTKsZR1ZHOtw8oWHpOki2JdhkelV9fVl8vN0hLI7plKlc4_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته‌دوم جام جهانی 2026؛ دشت یک امتیازی شاگردان امیرقلعه‌نویی مقابل ستارگان فوتبال بلژیک درشب درخشش‌علیرضا بیرانوند؛ سوفاسکور بهترین بازیکن زمین رو بیرو معرفی کرد.
🇮🇷
ایران
0️⃣
-
0️⃣
بلژیک
🇧🇪
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/persiana_Soccer/24028" target="_blank">📅 00:36 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24027">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k8-yrOtaOn_BAJwErm00_V4T6fIB4OFgLBGLC4DXMKFVFACVvBMbpY2c1GamV8lYMv7z1azQoFjm_xwz3oErdjov7cnPzwg2ZvmQaKRAQnW8fQ04zHnfkp1p5miw4KFjSv0kXjy9sntXg4B_4i8Gp57zMKWDQ5fvWBuYL_PHRU4Dps6dOW1cLRdTKydxeueSLbs6hlbsWYQHLBhK32rFLujGvQ-YCKAbF9ivgAQEDT2QqoTlNOqnmdqG3U3ztWSCgCQ0ZXLfKaNqYbSzcBKD1OGUGJmxCzkKqKcVEpyGNZmIXtAf_DzG0MuEwyaKoyFE6CQlo2AjCW8TH2f_X2mSkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👤
یک واکنش دیدنی دیگر از بیرانوند که دروازه تیم ایران را از فروپاشی نجات داد؛ تمجید رسانه تاچ‌ لاین انگلیس از دروازه‌بان ایران: علی بیرانوند مقابل بلژیک بهترین بازی‌ دوران حرفه‌ای خود را انجام می‌دهد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/persiana_Soccer/24027" target="_blank">📅 00:32 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24026">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/54539b7e86.mp4?token=Sdy80QrTC0Ez6bJfTKOZkWiGgHTcJzHDAMo3I4-odfiPiAwxxTKJbF5OXKLZjyvOlrNq_VHs7aWrSIWfIC-5Vy6ghB_r-jx3bt79C8zKpOlsf3kKkvl-QjhELmvqCl5EZ0H3nYG2Vz0ZUqecVPM97Hi04DZPT_FstS4vOjo_xoon3yCnTdY8LeO5sofvhdHZlRuR80kskCwwyqwj90u6Sj6U7B2OKc7pfGb1kDTk6BO63hZb0omAeFgJjQzFK0IiIy-sW9DHaLNXGSc4fCIOB2eeAKwVaZrF4LJRZi_6hbN36xnjXYZvqSuRi8BY8yrH_EkFvNuGVuM3c9BwCkTg1Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/54539b7e86.mp4?token=Sdy80QrTC0Ez6bJfTKOZkWiGgHTcJzHDAMo3I4-odfiPiAwxxTKJbF5OXKLZjyvOlrNq_VHs7aWrSIWfIC-5Vy6ghB_r-jx3bt79C8zKpOlsf3kKkvl-QjhELmvqCl5EZ0H3nYG2Vz0ZUqecVPM97Hi04DZPT_FstS4vOjo_xoon3yCnTdY8LeO5sofvhdHZlRuR80kskCwwyqwj90u6Sj6U7B2OKc7pfGb1kDTk6BO63hZb0omAeFgJjQzFK0IiIy-sW9DHaLNXGSc4fCIOB2eeAKwVaZrF4LJRZi_6hbN36xnjXYZvqSuRi8BY8yrH_EkFvNuGVuM3c9BwCkTg1Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👤
سیو عجیب و غریب و استثنایی علیرضا بیرانوند که میتونه کاندید بهترین سیو جام جهانی 2026 بشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/persiana_Soccer/24026" target="_blank">📅 00:25 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24025">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/94db339245.mp4?token=MyrudlKgLRNofOv58K94VaL5UCT84CeqHncLrdes4Qb6DjFmbFaYgJbjDPEPu4c0cBb9vkmNkyM38yqQjeFIjTp7ot_t8eQDWXrLfQE1JJO1RUopqolyNpiB5n1UgHvS5I1AXdvKPgBXAns6dp-6DkBXXkmSCMS3UZqNixDWROlKGEtZbh-Yd-aq3itfcob78PNE6g7ITAk3PjPn_Y43PYeVM7z7bBA1v4UpJmmD0j55hUMUBUQ46EqIoXGdhfnlzrn3ZP7xbx3w77u58C4CYYNheHeJcCorPDw85--p9a34N_41lFPSqoFm4X3uzOYf9RnHahLFqCGl5NpWJJdeRg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/94db339245.mp4?token=MyrudlKgLRNofOv58K94VaL5UCT84CeqHncLrdes4Qb6DjFmbFaYgJbjDPEPu4c0cBb9vkmNkyM38yqQjeFIjTp7ot_t8eQDWXrLfQE1JJO1RUopqolyNpiB5n1UgHvS5I1AXdvKPgBXAns6dp-6DkBXXkmSCMS3UZqNixDWROlKGEtZbh-Yd-aq3itfcob78PNE6g7ITAk3PjPn_Y43PYeVM7z7bBA1v4UpJmmD0j55hUMUBUQ46EqIoXGdhfnlzrn3ZP7xbx3w77u58C4CYYNheHeJcCorPDw85--p9a34N_41lFPSqoFm4X3uzOYf9RnHahLFqCGl5NpWJJdeRg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📊
نمرات بازیکنان ایران
🆚
بلژیک در پایان نیمه اول بازی؛ علی بیرو دومین بازیکن برتر زمین.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/persiana_Soccer/24025" target="_blank">📅 00:07 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24023">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/r3wkFRVkqH53mcQZXWYGwXxPSfbqob86661dnQTNkE_YT46CA54SwiHe3GIhyrGxzYnQxuuTkwuZOL6y8UP7FyVuUsvbkCk7roQ5cAdbf-8iWmCshOLpqGyZbLYzWM_RVe5EyPLaTUO-UqQ-5u2Ss9b1HEUSVqPpmvK_Sv1P6ZfOHM9R1eytpB7JriS5EATan0FUVU--evX6Yp-ycX5TcSLAu63eZHfB9xRa8XVIgnr1qBGpQRDN_kMHB1Doc3ANzGihfVcmzPnJnTLBm6R1hSdKX8hllt0GhUrkXJevuf4GKIdHmQoqOiAzsnUmirwb5cUFWNYUaymIfvw0cLO7bw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/C6bhAp_T_TwEweUZSlV7VAWOfv6H8BwueXhuFL0csQiWN8C3DMviJHxRTlC4-1aC91T5Reob_Htdbbz19rLUSoENAxQUelTaSBKIoJOtgV1N07J-UAlXd-0y1JebmCKflaKjAylMSKqzxNJC6ANKHQpoSBBeo3yltRBSVJzgQH9thxlUuOyAF7aLOiUOQfsfl9MfO9V0PfOAE01VNogKNY5-0Us74tJlxWs-7zjS_g9ZS5c8ZxofXmLEZMgBRevCt3M-H7CqszbBe-rG9zJA2TrYtCNu78IHdRi9irJZnzN2B2l6gPOSpb4Wurzbo9qalfosHpibENiNS3cOWhiboQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📊
آمار نیمه اول دیدار امشب دوتیم ایران
🆚
بلژیک در هفته دوم رقابت های جام جهانی 2026
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/persiana_Soccer/24023" target="_blank">📅 23:37 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-24022">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MUiWelg0YhRalCbBH4aAy9bEeTKLj6Kef4lxeWS66MNZPYLn0w1-7D4eIw__eG1ijliQ6xbCygRbDaMONGEuZGAx2WghP3ZGLySjQqOxD-u0U96SnZpl-OqNuYPTmd999ANtpCuhuOLUArU5u7402vib3irgzUkWFyQxBPNuDx3YWA06gXuZUCSXcDMz6E043UeutoM_7lQufVf0LTSJzXbQL05dHrVLIzOxdeQgVQyeeRBpRqwPMGSdmpmvjHuvi7D3YE6CmtV8JOtijmjXEbvKf2LQODoaxb3ok0FUUWrzNROJrxhYgO7e2-daxM9WC5gxHdla-7x1JZQBt55DMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
👤
امیرقلعه‌نویی این تاکتیک تیم کومان در جام جهانی 2022 که منجر به گل شد رو برای شاگرداش گذاشته اما غافل‌ازاینکه‌باسن طارمی توافساید بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/persiana_Soccer/24022" target="_blank">📅 23:26 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-24021">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a43b24a8b3.mp4?token=e_yuVDcAqjnxjdBpLMWbx-rC0L1wVcPhkIkIyTep16o59ctKTemduSNbgMUWOyZy6dXM1sKDsMvaZv3aIFkSymEWRGkAkRMkVNBWe8IGb6lFktq9otJvaQvs27X5geiAurvxh_7_rzSdd759Ewv0W8wkZkTgSfC3Oe6xRnjvF5ZwbcLOmPJuIQDwz54JaSk_Bz4VtZkAv95rznxkcUg8bFCaI0QmLqKk0qauSvgZKyol1NufdynVLX5fpXq6srIe4LHtluikqiJzkXr3Xw1fUfYB_JWrAgLM5I-S32WWTIfwlWHTs3TwUtUyvMQAq7q8bzKQ8I6vIV_xyU728L-FCg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a43b24a8b3.mp4?token=e_yuVDcAqjnxjdBpLMWbx-rC0L1wVcPhkIkIyTep16o59ctKTemduSNbgMUWOyZy6dXM1sKDsMvaZv3aIFkSymEWRGkAkRMkVNBWe8IGb6lFktq9otJvaQvs27X5geiAurvxh_7_rzSdd759Ewv0W8wkZkTgSfC3Oe6xRnjvF5ZwbcLOmPJuIQDwz54JaSk_Bz4VtZkAv95rznxkcUg8bFCaI0QmLqKk0qauSvgZKyol1NufdynVLX5fpXq6srIe4LHtluikqiJzkXr3Xw1fUfYB_JWrAgLM5I-S32WWTIfwlWHTs3TwUtUyvMQAq7q8bzKQ8I6vIV_xyU728L-FCg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
👤
گل‌اول‌ایران به بلژیک توسط مهدی طارمی در دقیقه 27 مسابقه که‌افساید مهدی طارمی گرفته شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/persiana_Soccer/24021" target="_blank">📅 23:22 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-24020">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d61647a74d.mp4?token=H3jmLqwIpJt29ow-hSTf7SHyCgZCSjI9HZhg83cdPkd5wRFraPBgF3NtIeNJtupR3392GB8aNRi6JJ0qZVm2Fq_2-QmoROhpVgPwKnO3uGWA0N_uwnYlyH1QohkvrD8YR0oHtFn6BzTESrojo8ODYqn2TR-geZpgpvWGmzfM_11t88V5BUrusBwWJ3smhUV-pvDzqbFBiWq1zJGNfDwodhGC91a86P2P4_K0b8Ccnoc0AL3uZ4oxmczRXiGhsaFFrp0oVZuvcQMKFIQ49pRSzp_W_hSllUMyG0dQyKk1cl_Wzpb3UaJsw6Ww-pbydDNMf7WrR5mK2MZ3dIPZUpOhUQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d61647a74d.mp4?token=H3jmLqwIpJt29ow-hSTf7SHyCgZCSjI9HZhg83cdPkd5wRFraPBgF3NtIeNJtupR3392GB8aNRi6JJ0qZVm2Fq_2-QmoROhpVgPwKnO3uGWA0N_uwnYlyH1QohkvrD8YR0oHtFn6BzTESrojo8ODYqn2TR-geZpgpvWGmzfM_11t88V5BUrusBwWJ3smhUV-pvDzqbFBiWq1zJGNfDwodhGC91a86P2P4_K0b8Ccnoc0AL3uZ4oxmczRXiGhsaFFrp0oVZuvcQMKFIQ49pRSzp_W_hSllUMyG0dQyKk1cl_Wzpb3UaJsw6Ww-pbydDNMf7WrR5mK2MZ3dIPZUpOhUQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
هفته‌دوم‌جام‌جهانی2026؛شماتیک‌ترکیب ایران برای دیدار مقابل بلژیک؛ ساعت 22:30 از پرشیانا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/persiana_Soccer/24020" target="_blank">📅 22:59 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-24019">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tw8JzAB-1XDZkSYVKsCiUtzZNPISxJYX3yJGURv3Ec7-2VVRcH2LREsM6lrHkLhsrA-kVuQY7PbjZ3SDPXZ0uC3QyRQm1UB3kfg3dvdM5J5YRltstR1VsL-vyScz3u1Djq7ieAu544I4OpuQ2Tc4fCkTG4-4HaDXXRrTtpv0Ks2Qh8co3EUybtu1ruVsbTZbj_yAzTgzgPTcyOYoBGgs7Dpkxq3pr3Za5KFxAUTTBU3T_whBTAeesDgjZJsv_DBtKWvDiIBSTok2frn-LSYKGNiGGS5MyHmwxfQ5Kn9u33V3fy6KHIxY87IUQiNVHBtyTMd9tqfBv2aQbC4kmmF9Vg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇧🇪
شماتیک‌ترکیب‌بلژیک‌برای بازی امشب با ایران؛ درحالی روملو لوکاکو و تروسارد به بازی رسیدند که سرمربی بلژیک گفته بود ناراحتی دارند و احتمالا در ترکیب‌ نیستن. احتمالا خواسته به ژنرال رکب بزنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/persiana_Soccer/24019" target="_blank">📅 22:24 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-24018">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GRMh5tNaBVQCWUN6cwYqwljKp4l7mprSEoPCu1nwSMkUV1uMIb8TGuIFfzG65G3snCSopS0Hh0fRD0-cFSTAazRR4ePOtDhHmqiy2r2Z5TLLHjAxBCCIfb9rZCUO1C93ydndVqW_RhhvzLG7MzhvXN1UyKBbBTrfb5rQVHiDFCBRSaRflHkGAvBPXWmeYeevzrx7hZ_eoU03uOoYueJEbS1KkbE1mZnE1jzpQaVea5Hg51sAyBurkByKzea9tNC2ayprHDPKLCLTyJYR4wSbLMh0QDTTCyKjf4lipCQMCKMY8I3eU4cIitJksaei0j_QYyZ1Si6SPBXXt8ns3miaIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
پیمان حدادی مدیرعامل تیم پرسپولیس: تا پس‌فردا بین اوسمارویرا و دراگان اسکوچیچ یکی رو بعنوان سرمربی فصل جدید انتخاب خواهیم کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/persiana_Soccer/24018" target="_blank">📅 22:03 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-24017">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/llTXIT1pvfy3MAw2p-Y4RLXCvY9jQazxGdt-F2DcauijCQ2NNw5EkwoRwL8ZB5urwbnKGEHfSRSNIBD6dCcAEPwtQEZom0oA-4GCXLDEjdX-pb0wr2IW8jXh9gB2e3xQTM6i4HuIYm7oZPkLluTUXPLO9wkSrJZvCwvLTPLLc2eEaAu4FbqeZuXQfmfQWontirGIOAF6My-wxoXEG_98LNuJYE3E9r1O8DYSSqXHbrD6ug7-85Pwo0qEz-uHTusbr5PnzCX5fNqf6k7eMy_0hkhgOR1opVWr57gsG95xRPasRtk7TzSE4I_3aIKls3X5APOy4jLukq4HFadBlOwBzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
هفته دوم جام جهانی؛ پیروزی پرگل و شیرین لاروخا در گام دوم رقابت‌ها مقابل عربستان سعودی.
🇪🇸
اسپانیا
4️⃣
-
0️⃣
عربستان
🇸🇦
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 30.4K · <a href="https://t.me/persiana_Soccer/24017" target="_blank">📅 21:51 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-24016">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">⚽️
هفته دوم جام جهانی؛ پیروزی پرگل و شیرین لاروخا در گام دوم رقابت‌ها مقابل عربستان سعودی.
🇪🇸
اسپانیا
4️⃣
-
0️⃣
عربستان
🇸🇦
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/persiana_Soccer/24016" target="_blank">📅 21:42 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-24015">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Sz65atmRdD5vbUpowLYaTqNXI1vJm9dMBfAwyhCu08n8a3tnwSD_VF7SoIxgaqdk90atdj6Ytt0kfgPDGsidec0L-KSkT5pRgU3oT_K9w8SGUsiXpK4MPtf3f73OmYW-xu3H5QJ3zoSu5MnfYnJsW-bdyaIdXdZ3as6ewPaPb3rKFD7W5rZGthxtcFh7lggFrqTx1ZbUXuDdvcNaK44llomotJYFwdImuBhM5Zrt_UCT5e7S6aZC278spaf75K-JRXBPDjnFrypdflHaRMbmU3qQUJXDN4snyv_0JvAT87JPK3eM5S_nqSdTG9Ye2mccQAsAcNKF_UpGxvQfrO2sag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
هفته‌دوم‌جام‌جهانی2026؛ شماتیک ترکیب تیم ملی اسپانیا برای دیدار با عربستان؛ ساعت 19:30
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 31K · <a href="https://t.me/persiana_Soccer/24015" target="_blank">📅 21:33 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-24014">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NqYRlyxnZuxIWipmQDitmrxbOUyB95U2uJ1Gvw2t_qQDLECEycQrAqyhBUIOf19_uSAZpEkvIANbreYtKbToStMd6jTLD8FtBZarVw9EKbCplC_EOJxi656nUGnC018ArkEvnMECQcTRsEVG4KejV7WlRbCWCzCfUY5t9842vUIgoUVEevgrTBMECOJWclUcLm6ptHo50YFzk9Fd9-Xk6UnROa_deBRtZjxENyT6dm9fMyEp5nAGjbA9dBntKIOfzsaOKNe_T_v343LE2Rt-gcUULxE28_JBcnVZwAxvEc62oQDzrkt-F2jWt01D8L5fPTqgGwfUPjfbAdQ7pWIHuw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته‌دوم‌جام‌جهانی2026؛شماتیک‌ترکیب ایران برای دیدار مقابل بلژیک؛ ساعت 22:30 از پرشیانا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 32K · <a href="https://t.me/persiana_Soccer/24014" target="_blank">📅 21:14 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-24013">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bgZcCZKpl0Zcpxajrx0b8YnFbrBQ6FhYpHQqQ9bX2rZYUC0uT-PBiSP_NAHtRjTnF4yR6lfp1AQ-aKm3PFeeHmox929BJDcRcMwUEXsrEAjL4LYAcCleEGkwv3htLmCpru0f5GnbPhiZDA3nfkpuH9CTeHFRYKzgeiYPvX8B9GihFh-9V4fXnIRrOAECMM1g8DNvh7Z8-DSqGi3FnMQ_nUfbegWWiKVWzgeIQfDYMEpi6-klvpea-xec-lZ9jL3YJB6RfLUs6yW7kSNxFIiD50uu1Xow6eOrC5rh7YyiPdQqEr9BVJRMph7N_nNXIVgi_QnWrv0WT1ptYVPQiB3HCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته‌دوم‌جام‌جهانی2026؛شماتیک‌ترکیب ایران برای دیدار مقابل بلژیک؛ ساعت 22:30 از پرشیانا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 31.9K · <a href="https://t.me/persiana_Soccer/24013" target="_blank">📅 21:09 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-24012">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qaLd5bBTLsRFKJm417fi92tR3D5sFbFfjWPdTJKA0aYvuVw_HUIR6zq09dMz-WO0eIiHG0M_zSBrftNsS4ZVAxG_7Eae0TfxK81zmnO7F1IDyn-nZIbaTfEJfkKbKfR3WglMPhCBPxS86ZsM5Q6pZJClS45iTdGfzlYiE3QoPUCOuIkVjoKza5XuRFrlvQxMlShcRc62TzBAt31PDxsv2N2gu_PRCoKCJcSWplkm_3X4KrrkxEg0YYEwxllEVUQn3juihIn3FLWS2AAHxpZ5-2HrxGI5L8bqBZLE7jbDHB8qPDsQW2myrekp0z72_srAhg3_625IQT7-5zPYMad_WQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته‌دوم‌جام‌جهانی2026
؛شماتیک‌ترکیب ایران برای دیدار مقابل بلژیک؛ ساعت 22:30 از پرشیانا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/persiana_Soccer/24012" target="_blank">📅 21:05 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-24011">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LxxPZzaHIYU4Yp-d-fN6K_3DquGY89GquBF3XHz6DqCzUVn5iRz5p9KVwwsFawvVc485jmQEjwak9MzUXVdgK4BSEWfihzv-YRC4EZsf1JmwVwT7QHRbSQ95fv3AjZwax-UvqZ1Z9K0j8WLjQfIFTU8N6iOYRKb1H8R8TUujJDYJ_ZCRLN5dzpDMaeaifXZ7z37m4anI6cQ1bd4Caw92zbPBfdZ9vu59GMsjE1lmOvlghQSYLKmOVKs_50daEBTt5ne0-n4fsW2xsz5Ix7J3Ad87aqi2GRsKnDOQ38Scr4Ny2LQg09lGkltWXssPHJIJSaeaUY9msPdBbx7WtFMi6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی؛خواستیم‌بعدِ بازی امشب ایران با بلژیک جزئیات‌مذاکرات‌روبگیم اما رسانه‌های دولتی نزدیک به پیمان حدادی جزئیاتش رو منتشر کردند.
‼️
دراگان‌اسکوچیچ درمذاکرات‌امروزخود با باشگاه پرسپولیس دوشرط‌سخت گذاشته است که یخورده مدیران باشگاه رو برای عقد قرارداد…</div>
<div class="tg-footer">👁️ 31.2K · <a href="https://t.me/persiana_Soccer/24011" target="_blank">📅 21:05 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-24010">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBetegram</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BigB6YD9Xk7OMp_9TiMtv3R8j4jmV7UNjCRURXUhjmmtjtWkx0vGRVWmFiVx8kAqcSBj8XfR9MR5HdkfcQUxzHklia22YbfKBe-c1PvRP3EQ1ZoU_gPzi1mQi_bce6nKUFfP2Pz05XKQnGiXF1Y5jgYcSlMn2hzDda2Hgf7wuTfHQLY2B4UG56mac3BF7uJeGZ590XY-lVQ_8IeLn3qF43tPWx-qsBsKdzqasc2GaK9ctG_skdz5PweusENRwpd5WdmtKmBD5JOT-FH3w2-PTFcNbjVQ4r6MEiIqWav8nXJz-ytUpLXCCK3or6gUun3xGZ5CKofuXiOZGRfglbWs4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚔️
🇮🇷
یوز ایرانی vs
🇧🇪
شیطان اروپا
🔥
تاریخ‌سازی ایران یا بازگشت قدرت بلژیک
📅
۳۱ شهریور
⏰
۲۲:۳۰
🇮🇷
ایران در ۷ حضور جام جهانی هنوز به مرحله حذفی نرسیده، اما این دوره یکی از بهترین فرصت‌های تاریخش برای صعود است.
🇧🇪
بلژیک پس از حذف غیرمنتظره در دوره قبل، به دنبال بازگشت به جمع مدعیان فوتبال جهان است.
🏆
یک نبرد سرنوشت‌ساز؛ آغاز یک تاریخ جدید یا احیای قدرت غول اروپا
🚀
بتگرام در تمام مسابقات جام جهانی ۲۰۲۶ همراه شماست؛
با پوشش کامل بازی‌ها، آپشن‌های متنوع و هیجان لحظه‌به‌لحظه رقابت‌ها.
👉
🌐
🚀
betegram.com/affiliates?btag=3_l7
🔥
⚽</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/persiana_Soccer/24010" target="_blank">📅 21:05 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-24009">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YptYxQpyCTfb9qgOkdid2FaQrFb2bajWwZ7qnqGCzdyokkGlJ_BkTeEQ_q_fXm6GVDPPyTS9ncGT1icCh4kBx9-Adn8Lp8mZvySXAarXix_nzX2-rjen480Qc6ZZqWhfLyezL79njR16pGwOt15qqDyxjii_OT41HlTtBvZO9wvXrjsilgk-TGhX3gDlz8P3_NdE5EaIhSW8OPbADajYkK4AzSehoxxZ1VuuTyH967f1hjByMqSevM0jkhI-I61j-Med1P-iCDKa9kbEgdXzaoUFTFsj7E-nenYXeaj14v-cbL6Joka0zrFS67WKyolTMmffjwDqiTswK5_XMIJojg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی؛همانطورکه‌بعنوان اولین رسانه خبر ازمذاکرات محمد دانشگر با باشگاه تراکتور دادیم و صبح نیز درباره پیشنهاد مالی این بازیکن خبر دادیم دقایقی قبل تراکتور موافقت خود را با این آفر اعلام کرد و دانشگر به زودی راهی دفتر محمدرضا زنوزی خواهد شد تا قرارداد دوساله…</div>
<div class="tg-footer">👁️ 33.5K · <a href="https://t.me/persiana_Soccer/24009" target="_blank">📅 20:44 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-24008">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Vvu1ctKdB1iJ1wcan4tKyPYfIYgKsJu8l1pPaH5SnvF7g-QU60YQMR90_j4bz5z1XfI3noN5YMJAYdpbPT4XYI5VkDam9zehCjEhX4sm_yHIeVBw9r0FI-2d3_eFQGNEzs9-846Ey5EuUx10JorwYT4oBAnVcIoW81Da0J6myHHJIxbwctoHPetmxEOesO9yIq9LQ5wjpBPGZNct1sMgSLdoxaBnNo81vQI7XkeL-3_NQDC-245to0bBKmPQBxflZwypPCl2SN-ZiUZv2jqPyOLyZatmp_2H0EtBMlebX7ojgBVUMAT3bU4ZsRS4MG45bhhu38L2F-Mdi3h9tQyUeg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
هلدینگ خلیج فارس و باشگاه استقلال برای پرونده بازشدن پنجره نقل و انتقالاتی آبی‌ها روی هم 850 هزار دلار هزینه کرده اند. وکیل ایتالیایی آبی‌ها هم‌امروز ظهر ایمیل جدید به باشگاه فرستاده و گفته شما تموم کارهای‌نقل‌وانتقالاتی‌خودتون روانجام بدید فیفا پنجره نقل‌وانتقالاتی…</div>
<div class="tg-footer">👁️ 33.9K · <a href="https://t.me/persiana_Soccer/24008" target="_blank">📅 20:27 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-24007">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IfOxCtAxVzgCbeCGsl1sZfmfXUmU7tQj75uTLOyfYC81caz844KXn1y0KfrLH8G9UGYs5ChLstO_pM1B9nghWeHkK5Z9EQUHM707ZvZ_lS91LfGw2lPzauZE7SDPP7oninkXd3LMMzzny2a9SCd-ez0v7WYCj3zx1HUSxGesCmNJF0miA4X5HVL4-QdnorVqBeuhbJVC-YTM0Qg4RmTl6mvLwO0l1T7iSI9pgXKPRH5GjRAvjdmqq6asVzjfPGfUx_PgUyY_rgBjnDcVIzT5Tg7x9iATPLJz2NRmNw59GGI9xsiTaF9qOtOQ6dvckF2U_g7KvOkM0RKPo5Spo8BUpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🟡
👤
قرارداد محمد محبی با باشگاه روستوف روسیه به پایان رسیده و با توجه به اینکه برای تمدید قراردادش‌اقدام‌نشد او بازیکن آزاد بشمار خواهد امد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.3K · <a href="https://t.me/persiana_Soccer/24007" target="_blank">📅 20:03 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-24005">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/efcjH-uRP03GZm5m8l5IBT1qX3y1HVz5Oe2TuYsAwPwfBVJiF-rkE68f9lFghe_L1EskGmIMfibfOjrD5kvFM7mG_yACQbtvIsiLfv7QGbu4Nj0o1peCmP4_LK1wOY1f1qdqE-WABEIpXNd8aieDMSweJ-efVTCDp6DsQTnR374H5F3GQmVlr6cdP9P1uTLm1PWetGeosvuUECHM5hUHuT-VCknW4eVLjZwQIXPL5SuFP3LxLYmlWPdft4t70Sfz-Ea3CacNN7g9Dx2WkB30OrDar8puVi_yj36neyxiRHsOVKiVrtHN3mdMSsC0uriI9-HAZujJb3X5JjosNA7LTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی؛ جلسه‌مدیران باشگاه پرسپولیس با اسکوچیچ و نماینده‌اش‌دقایقی قبل‌درترکیه به پایان رسید. پیگیری خواهیم کرد نتیجه جلسه رو تا پایان امشب بعد بازی ایران اطلاع رسانی خواهیم کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.7K · <a href="https://t.me/persiana_Soccer/24005" target="_blank">📅 19:35 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-24004">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WR6ow-P2pAWUuSeuYJTudLIMSjuZCYRKibElrmwr3-b0E2buX4jmWU3i9ZyfNsnawDedIrBkskFpcx71w0gP99SoLmb9Kjgc1Ilp--R65io2LL06K6slBqbqUflA01okimj1NstmN5OFnDjkudYj0OtFSIXApX_Ft0l7a9WeTgrS9b7qKtuZO8KRw9t2GEtW6k9ioyhzDXYcYvIdMFSBkObSMxO7GncjmQnx9Xlwblps8U-xBW_fovbf62oWhFKS7lK2Pshfn_iVZlFitX0acP3F1Ijv0CTEm93VLiX5A3VHB-3XA-U-V4gih14C73XlnDMm-PVek9LQO8vsjxIelw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی؛ محمد دانشگر در مذاکرات خود را بامدیران‌باشگاه‌تراکتور برای دو فصل حضور در این تیم خواستار 190 میلیارد تومان ناقابل شده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.1K · <a href="https://t.me/persiana_Soccer/24004" target="_blank">📅 19:25 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-24003">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/UyRpP-2QcjZEmWwH-3tQ0MAw_efZAn2Qt89mn_OTk8mWQIPDfYfJc3Csr5xsMXAMANS2S0LT2sLwLGpsHTdwpgh0U0zmax_vXP-_GaLHw2pRYPF475D8nukaZFuWr57LZXRiDNAi76gQErFwfn3CbSOxRMgdFoHDosUntbBWYhbzlCBbXwiO0iSvNdzBGJL2mcF7Y3jNFVrA-9DE3j7Hfyhm_n_E35UcoQTpB1-OS9hOO6JKF232w0bZzkJ1VBi-_O7igXapRoLhjqiIXT2W1JsI-Vfw_iFX29d5DNA9XUnvPYMvPDVQhtPjd2t68XscY9fZVRcpkhubslLOaW4E7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇳🇴
کشور نروژ اعلام کرده هر کی تو روز عرضه بازی GTA6، بچه بدنیا بیاره، یه‌نسخه‌رایگان از بازی بهش میدن. وقتی‌نمونده اگه نسخه رایگان میخوای، همین الان پستوبفرست‌براش تاکارای اداری‌شو انجام بدین.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.4K · <a href="https://t.me/persiana_Soccer/24003" target="_blank">📅 19:25 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-24002">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Wz5ap9ca4OCwoQ-BhzDYaKTJZTJ7rk5Juc329ZoNjaof58Wx5fgOC3xqXplnpB2qBgD1KlaaG7j0gL8N0dq539xATJ5WP6MvNfGNkvblbNiG-IVDZXQZjQFCmZjo5jBAEAXdU9MqQyFmNfQBDvAYNuPYod5a-wU2xHLuHRCz1mam7iX_3CGRrBovWnAvYgud-FdXr6VDOgBOMTzUw0fgrORcj8iVDfdTNBGDmSWr6OM1z55zcLdcEJeWDGqioJ8ZMHP91-9NhxxCtezD6gqc8FptMH3KB2Uae2zObGCOWn4iTu5KPjDHIpM6qhJqNHPlwC4r_eYjYfFfYs27ausmBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تا
😄
😄
😄
😃
دلار درآمد با معرفی دوستات
🤝
بامعرفی‌هرکدوم از دوستات به وینرو میتونی تا
🤩
🤩
🤩
🤩
دلار درآمد داشته باشی
💰
🔝
فقط کافیه دوستتو به وینرو دعوت کنی و کسب درآمد کنی
این‌پاداش‌پول‌نقده و لحظه‌ای به حسابت واریز میشه و به صورت آنی میتونی برداشتش کنی
💰
💣
بالاترین بونوس‌ها فقط در سایت وینرو
پیش بینی کن و برنده شو
🎯
📺
تلویزیون لایو برای پوشش بازی ها
🛍
بالاترین ضرایب ممکن
💰
expert tips bets
راستی با اولین واریزت هم میتونی تا ۲۰۰ درصد شارژ اضافه از ما هدیه بگی
🔤
Winro.io
معتبرترین سایت ایران
🔤
Winro.io
کلیک کن و درآمد کسب کن
📱
کانال اخبار و هدایــا g31
🌟
📱
@winro_io</div>
<div class="tg-footer">👁️ 35.1K · <a href="https://t.me/persiana_Soccer/24002" target="_blank">📅 19:25 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-24001">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BaQ4-fooJkt5cf1-FqOV5FQGaFbslMOFxXojAklS2eqgWTHNeEPFtfoIk2oesARByZ9Dfx40mrL148qezgZj38pBn8Pwf1TYH4kopV32hY8RiscLq6Ktw_DkXwmWvTIBVOYjuoBZN5chCJnWNHlQWGqwp0KGHnr1YV7FlP9SuiT-jkckFNkdYSSI-NXH2rmScDkqJ0XOfdfLykUvW3YZaZdqHh_eQWsKDttC67ewMUnhltmy5Zu9MqQkx0BHkfl6UhC_5JzG2E12sxOWobvvLFjXcSRTt0X0Y8pccbPM5Si3gMdAStC3NTgO_Um9DDNYGg11p-m2rwAAGdatuhzp-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سیاست باشگاه استقلال در این پنجره نقل و انتقالات جذب بازیکنان جوان ایرانی</div>
<div class="tg-footer">👁️ 36.5K · <a href="https://t.me/persiana_Soccer/24001" target="_blank">📅 18:55 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-24000">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sq8-9Xhd3PiQZIoVUq3BjhZKXpQQggyhwiIiV_Se7GQmAlwyES5NRKwPUKQzImMKBJh9az2twss2PhTM9uBdS_c2_VV7wxiyLtTf9Om7qeXOuOe_33O5NlPdGehHfrjaRxmVuP9y4yUBjzL36I3TXIOx5-uovTuUwf60Mr8tc9IrrrLCPyEOEXrc9B-15TAfcF6dGtAP7lv4uv1M6s8alQlalNr5pChCcbun6fGWSI98Iql3XqgZo31tJsYCBEY9w6oa5pyjkDwSJCZs0OwB0AKJ7mUk4jIk7yjWevZ_DWrS07HWwIk2G2pmSLZGP2wRapiezvlHfNbn4-7P4b1ekg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
رکوردجهان توسط یک مرد اهل جزیره کوچک کم جمعیت‌در دریای‌کارائیب‌شکسته شد؛ الوی روم دروازه بان 37 ساله کوراسائو در بازی دیشب مقابل اکوادور موفق‌به‌ثبت 15 سیو شد و رکورد بیشترین سیو در 90 دقیقه‌یک بازی جام جهانی رو شکست!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37K · <a href="https://t.me/persiana_Soccer/24000" target="_blank">📅 18:44 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23999">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fe31d4a415.mp4?token=Gwv9g5vwN7uaOmMD-JYvtnXr_KpsHO-dj4BUk5-CYucPOH2DVv1qoqOlbXvslNtTuW5zjkiqJZEf1LBFRYPjQk65_7cudTTPXMD1g2GWuNcc-bm26OFDImjWsPPgj9SVXN-HWDXW4gAZWoFOzMFJwHxZ8ZcnonabeLuDsQDttdx6_YY42s7djv7KH2VVyyPe3JvYMXwyQhaX9one-hHmWa-WvhTGKJsoA4ki3FJyV3pQQeEZDVeeqD19YstudOaSRpPJYh_LD14l1e9Sp3hmkucQHonnbZhbEOU2ciWqvG8_fgSnVZcGymeJ_1odYDme8DRlK9uKYHuAbDdFYlUNgw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fe31d4a415.mp4?token=Gwv9g5vwN7uaOmMD-JYvtnXr_KpsHO-dj4BUk5-CYucPOH2DVv1qoqOlbXvslNtTuW5zjkiqJZEf1LBFRYPjQk65_7cudTTPXMD1g2GWuNcc-bm26OFDImjWsPPgj9SVXN-HWDXW4gAZWoFOzMFJwHxZ8ZcnonabeLuDsQDttdx6_YY42s7djv7KH2VVyyPe3JvYMXwyQhaX9one-hHmWa-WvhTGKJsoA4ki3FJyV3pQQeEZDVeeqD19YstudOaSRpPJYh_LD14l1e9Sp3hmkucQHonnbZhbEOU2ciWqvG8_fgSnVZcGymeJ_1odYDme8DRlK9uKYHuAbDdFYlUNgw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
بعدِضربه‌موزی‌شکل؛ و حالا ضربه پنبه‌ای
😕
😂
رونمایی سرهنگ علیفر از دیگر نوع ضربه در فوتبال
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.8K · <a href="https://t.me/persiana_Soccer/23999" target="_blank">📅 18:19 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23998">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TLw7tRCiA34Z53npyIbruRCAPXaB-Qa88r3k4n5dtOzUtbMkbhnI1gsCuQFSADWRJnvFm9nyhUSnv7eFNwH4DDaMXgtciND3O2Fp9NQbgqsd9kzvknED52a9PVW1nIH2ueMKalJJXm15qtSC7fiRjhhA3oLpJP-LRqEWW9ZqT5a58iU6yW8refQhGv5UOUtG1rOySq1kwFGGybRKac9nZtRqqjKx9c9GYGtpD6yUjFgzT5JBqSW-4MgswpyuGNaLWSAvdiWQf9FK1P0hgW9UUdYy2zAq2WHyl6lm6KHbfo0qlEVxvI-LUXHsn4FFChN5MiMFcnTrcbl1PipH4u5oJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
#تکمیلی؛ باتوجه‌به‌تعدادسوالات زیادی که درباره آخرین وضعیت نیمکت‌پرسپولیس پرسیدین لازمه در این باره به یه جمع بندی برسیم؛ امروز پرسپولیس با اسکوچیچ مذاکرات نهایی روانجام‌میده اگه به توافق کامل‌برسند بر سرجزئیات قرارداد امضا میشه اگه به توافق نرسند اوسمار…</div>
<div class="tg-footer">👁️ 40.2K · <a href="https://t.me/persiana_Soccer/23998" target="_blank">📅 18:05 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23997">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N6qLibO7UkNqsAfO0zKMQz1rvxP1pALSmkqjuMK8X18kAryFMmAJmdQhMzIji4mpef0iUv59XWprMXxEzA4YfTU2mhalBtV7WfIvsPUoYxiX2grMq14IKNFC6vGGS7Fi_vy7Eb1GPw5z-3pLTYJQkyAn_pfPgyqOD-qkkv7GdSF-sywcTwgzEABcVm8AQu_Y2xDd26nxxkfpBOrvDzVOZ6G1tvIzWrLcX7tpxoebZGcFK9-yPC_Al20xYTqdMXEYgDEi3iCSDpKCpPtCvdMiH-lucWyrtRMx5oe6WFc4do7MZcCL8Akt9oA15oNUucEorxI0ZbaxutQn3beOSJLlTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
هفته‌دوم‌جام‌جهانی2026
؛ شماتیک ترکیب تیم ملی اسپانیا برای دیدار با عربستان؛ ساعت 19:30
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.4K · <a href="https://t.me/persiana_Soccer/23997" target="_blank">📅 17:55 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23996">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lQir_6GEV1gpNzxzHMd3-LFgYUaxNp9bgQrBl3m6L-s4QUip7UJoabkWrVkPCpNBWyrw2yBf9POLLhx73QquFhZ1clYEv5jiuH-41ymb0r2Zsq0jK1lNw2IplqOdbN4WeedSs1RIM-rcOVM336oQ0mJlyiqqEUPFJDys9doGZhV18eGlK8VsgLOseEazRxHf19sVAQ2Cdi5IT-0lTdL9v3dItdMdxmz9r0HGh0PUJkIubDRHdEhVUBGNAP6qfxow1O7zTwUKCRX7u-SweuXP-P9Rg8ZOutqdAu2FTwVQdq8MG0zlDR_DH6fhZdvnb2A8i6XsUZ9UjFcPifdL13fsQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
‏این‌داستان: امباپه‌‌کم‌عقل؛
رابطه‌ی کیلیان امپابه ستاره فرانسوی رئال مادرید با دوست دخترش، استر اکسپوزیتو باروشدن‌خیانت امباپه‌ کم عقل تموم شد.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.6K · <a href="https://t.me/persiana_Soccer/23996" target="_blank">📅 17:53 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23995">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tlUXFXRTCZGWFOfkQG1eMMxrm8gkXr2PwsJ46bcxF4jLVKvyNpfIbHI0Vc46LzZYcy9-SxjqJtsr9Og3WM07V8jSvFIBz6mnVO5C8zdpKsrDzeaW-zUk_RQYcKC065BNMV4LUSMnfbi1S5Prl9WmD35uRHFjVPXtu7hJ1qR2WBQQtlol5cN6RNHAsWfj4v_jb-aCuOW1wkAblqRIzJvs3BeJ-Dt30XrkcSAm1IKAX_kx-i7l3EuZOZ0Ud6CAU1_5RDhP9fAdQ17ALES5heL6e1Xi0uQ-VoDo3Ju0S7vuvOan9l4kD1FL-M3gutIsKzrQqFpku6FiW6n5LCjk-CBN5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
#تکمیلی؛ تاجرنیا امروز صبح در تماس با سهراب بختیاری زاده سرمربی جدید استقلال گفته درصورت موافقت او سریعا با گابریل پین قرارداد امضا خواهد کرد. بختیاری‌زاده علاقمند به مربیان ترکیه‌ای است و احتمال داره دستیار دومش هم اهل این کشور باشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.3K · <a href="https://t.me/persiana_Soccer/23995" target="_blank">📅 17:43 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23994">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e1N616fbdVmnzzseFgvu2n5cPjGlizCWazq1de1KZG8dr-VVDrymqZpnl0REBci45b_2e-MI2nsokwJqlnNCsmnId72_p4nIBjqD6GsLE0PZPYYMF56pzmjBi7r3JWmfcoCEWvm8YK4wZarVwC30SSrE5kzDvgyo-DXCMnazapIcFM2rKJdQ8GbklEy7UGCRyRyfTHbaj46GvS2tzczSwXGOXHd0kAdkPl-SuZUya3JtnqgPNX9P6xFGdL7qbBIcnGFixGVKdmF6dA8yvm9SuJafnAkN9GAqTQoWYlzV-ckyNSULu6BtOlOGpJCQwBJYm_fervBTwpBfCiE5eEix5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
🇺🇸
جی دی ونس معاون اول ترامپ: باز شدن تنگه هرمز و پایان دادن به برنامه هسته‌‌ای ایران؛ این کارها قبلا انجام شدند! سوال اینه که ما اکنون چقدر می‌توانیم باهم به‌موفقیت برسیم. آیا میتونیم روابط درخاورمیانه را بطور دائم و همیشگی تغییر دهیم، یا به‌انجام کارها…</div>
<div class="tg-footer">👁️ 39.6K · <a href="https://t.me/persiana_Soccer/23994" target="_blank">📅 17:18 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23993">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/420ab2f182.mp4?token=HUF0w8xIGLAA6330ru9JMNwuCHYAreS9yu7mcFRrClymGzVQbaKJho-l6YQ-78pqrhqPeoOZXZTZ1iBHnmItRyVGxrbWUu_rw1iRGjL2xuiso2CwCQefFUtRVAH3WrI12G4H9TK5yUDb-6aSdjMz1nfzHLhlrKzBTLYjgFpwjc_NhEcOvhZWoRmFJbwAsa_26fSqhNzCYtoAKfVkwLmg_BhKzNosnf7Ubf1nAV0mT7jQgxsFdH-PK84eXjZORC8zk9ajbsWwb72j6ahPS53vh_ITSg7u2k8GygUnxJKPzIs1zRdiEiBHwIQJ3MAIeySQKe_wbj_DdHjGIUYn4zwc4A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/420ab2f182.mp4?token=HUF0w8xIGLAA6330ru9JMNwuCHYAreS9yu7mcFRrClymGzVQbaKJho-l6YQ-78pqrhqPeoOZXZTZ1iBHnmItRyVGxrbWUu_rw1iRGjL2xuiso2CwCQefFUtRVAH3WrI12G4H9TK5yUDb-6aSdjMz1nfzHLhlrKzBTLYjgFpwjc_NhEcOvhZWoRmFJbwAsa_26fSqhNzCYtoAKfVkwLmg_BhKzNosnf7Ubf1nAV0mT7jQgxsFdH-PK84eXjZORC8zk9ajbsWwb72j6ahPS53vh_ITSg7u2k8GygUnxJKPzIs1zRdiEiBHwIQJ3MAIeySQKe_wbj_DdHjGIUYn4zwc4A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
باز هم ژاپن و باز هم ماجرای عبور کردن یا نکردن تمام توپ از تمام خط؛ توپی که بصورت میلی متری از روی خط دروازه برگشت داده شد یادآور وضعیتیه که این تیم چهار سال قبل مقابل تیم اسپانیا داشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.6K · <a href="https://t.me/persiana_Soccer/23993" target="_blank">📅 17:05 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23992">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YuWO4QBIn8piKxdlBwryzEkk73S-5NXorVN_g56kGr_nd3FZQqjDFeR_qDt3aW6h_pD1fpdAhTmd4gjU1gusA4ySbjrjS4TdPK4UKDNeHP2qv9Lp7VpNYnPlTeIQiVs2Y3jaIEshL6hfqZsRtuBSkgK-UdzCdRn-AYy6rsbRwuKris8ejvX504fKiIUPjanMiJEVKWPIo3HPNUa6u3Zcvm-YAsi0liAbE87Tq8mzybo1PW8BdjC39yEnuhhdtv8AYNKYOKM8wL3KM_eZEk8WsN7BEi8cSDTBQUAkjhsimPlCXCkZnpL0Ifo4T3K8gKm7cRTSXvnNerl38hL-B7sLaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
#تکمیلی؛ وکیل ایتالیایی باشگاه استقلال به علی تاجرنیا رئیس هیات‌مدیره آبی‌پوشان اعلام کرده که فعالیت‌نقل‌وانتقالاتی خود را شروع کنند و دغدغه پنجره رونداشته باشند فیفا بزودی‌پنجره روباز میکنه.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 40.2K · <a href="https://t.me/persiana_Soccer/23992" target="_blank">📅 17:00 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23991">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b889f1521d.mp4?token=ZI5_aU6ERReAnNDY29Gf7JGdMP0jr6hln5OL-GrRS-vwOwwHmh9-QTBjBnLpC-Tw5khVMAT5XQUEEt_OnYCsiQ6M4g93A7eFgS3br7DLUOGylvGAmwGoR-pw-EOdOk7vI7yJlx0tsKnu69bOciAavYdUuapyG07SJPCiv4s5OItgq0dZ4qStwmRcxb1g89gx5EUMjqYHrny1K-nv5jArFR7PDKd0zKYelzkZNrIB_hXIips2N1qqn8QfQgofV86LRUFllLw2WTuQUsaug4K_FT-mGT7NHCXq50tpD5y9hQ9r4CUyZWb-kT951X1NM3_Qe6FhWSeJrSaO3yfrP1ryCw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b889f1521d.mp4?token=ZI5_aU6ERReAnNDY29Gf7JGdMP0jr6hln5OL-GrRS-vwOwwHmh9-QTBjBnLpC-Tw5khVMAT5XQUEEt_OnYCsiQ6M4g93A7eFgS3br7DLUOGylvGAmwGoR-pw-EOdOk7vI7yJlx0tsKnu69bOciAavYdUuapyG07SJPCiv4s5OItgq0dZ4qStwmRcxb1g89gx5EUMjqYHrny1K-nv5jArFR7PDKd0zKYelzkZNrIB_hXIips2N1qqn8QfQgofV86LRUFllLw2WTuQUsaug4K_FT-mGT7NHCXq50tpD5y9hQ9r4CUyZWb-kT951X1NM3_Qe6FhWSeJrSaO3yfrP1ryCw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
دهنت سرویس ابوطالب
؛ فیروز کریمی‌ رو دعوت کرده گذاشته رو دورتند آخرشم خدافظی کرد و تموم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.3K · <a href="https://t.me/persiana_Soccer/23991" target="_blank">📅 16:51 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23990">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P3qaxn9Kj6T_SEh3QI881GfZee97oILLJhr9uTpNB86EwfZoSsS7ZornEPLMYziT_syACUEg2UY9W4F1z4Il9icethf8qUQwgb1uIXkgIlMgTEd0Vwj2xWJGetBVdl36CzV173KisJKZSijpaOTb8fHk-iwW1HyQyaHvQvyb62Dh8WTsT-y4QvGsL7iU0Kf3foR6MIS_kOgOhovSp5oWPz6xd9LTzku8_fH5NzsK-bJxiE3-bj5xOcZWbz0KPpvKUDBGX0RTJeqeNcQcwsc8soPNfUXoacqffSVSLsBBxpSg12WahMT8894yYQAfM8NUB2AT3u6hjEYfK0zTTxoqMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
🇺🇸
جی دی ونس معاون اول ترامپ:
باز شدن تنگه هرمز و پایان دادن به برنامه هسته‌‌ای ایران؛ این کارها قبلا انجام شدند! سوال اینه که ما اکنون چقدر می‌توانیم باهم به‌موفقیت برسیم. آیا میتونیم روابط درخاورمیانه را بطور دائم و همیشگی تغییر دهیم، یا به‌انجام کارها به روش‌قدیمی‌ برگردیم که ترجیح ما نیست‌ اما مطمئنا چیزیه که می‌تواند اتفاق بیفتد.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.7K · <a href="https://t.me/persiana_Soccer/23990" target="_blank">📅 16:36 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23989">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1c577c16fe.mp4?token=u6GmKuv9O1Jx4Sy1eCA4QjiirLsFepKdgPtB-VIIg1C_WgVZjiCZgyA6inEHoMHFuZEBWmCvVYvmFrEIevpPVJ3MNJoLB1ZNnb-uQYnQxirnsKEYUYIgqJjzBlIqyQjqzyEybvki4Y6TazySDaoTcw_LpsfxFuiJeR60PhDLuSkmgdYIzLOGSCRGos2Q9oQV3hWXtKwmc6A-1yacho_gCO_EUG3AheXs13R5-f0i7a_Vl4YWa-wQJNK6_c7JGeSmIXRZLqBBvgFJWauBjJKWrgM46RWh22vNTwNlFVE_nmajIPpZQcQflogt2shR-lFnhpqOzX8hJ2_-K2YZb2l8XA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1c577c16fe.mp4?token=u6GmKuv9O1Jx4Sy1eCA4QjiirLsFepKdgPtB-VIIg1C_WgVZjiCZgyA6inEHoMHFuZEBWmCvVYvmFrEIevpPVJ3MNJoLB1ZNnb-uQYnQxirnsKEYUYIgqJjzBlIqyQjqzyEybvki4Y6TazySDaoTcw_LpsfxFuiJeR60PhDLuSkmgdYIzLOGSCRGos2Q9oQV3hWXtKwmc6A-1yacho_gCO_EUG3AheXs13R5-f0i7a_Vl4YWa-wQJNK6_c7JGeSmIXRZLqBBvgFJWauBjJKWrgM46RWh22vNTwNlFVE_nmajIPpZQcQflogt2shR-lFnhpqOzX8hJ2_-K2YZb2l8XA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ساعت‌داوربازی پاراگوئه دزدیده شد!
در جریان یک مسابقه‌فوتبال درپاراگوئه یکی از بازیکنان، ساعت هوشمندداور راکه درگیرودار نیمه اول بر زمین افتاده بود، برداشت‌به‌مچ‌خود بست و  در نهایتاز زمین خارج شد.  بااین‌حال در نیمه دوم ساعت دوباره به مچ داور بازگشته بود، اما نحوه پس گرفتن آن مشخص نیست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.4K · <a href="https://t.me/persiana_Soccer/23989" target="_blank">📅 16:23 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23988">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fpehE7gVD72gc_GC3TnrRPazBjYyavhVsQ6NaAZuXdq7yL3JY9nFwft0c6O938gnpWG65yZTF42TIFvUYFiqUFbU5Dzk8FFD_VScEvPVLsvuV8rWzaAL1YZ6fBRTA_oZz6j6-9I4D3DN5ncu0fk2KALSkj4hhhUNzYoZc3enVvR8OPOFcH_IKJ6vSF6BFKfexC5hk_0Zs5RFnfKJDwBL5au1D1lQYNHawa2EwVCR49KieElvHLF2YIFZkQPFe4w95n90qoYfoeWVdV37BdOXwndhHJOKcO7MNHgKifsbUDMxdk3muwG_Y5gMKJJb1VOMwvotOVvM99-ggEisCtVQmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇫🇷
🇫🇷
خوزه فلیکس دیاز: بعداز توافق شخصی فلورنتینو پرز با انزو فرناندز؛ کاماوینگا و شوامنی دو گزینه پرز برای جدایی‌از رئال مادریده. شانس جدایی کاماوینگا بیشتراز شوامنی است. درباره فده والورده پرز گفته او فروشی نیس بهش هم فکر کنید.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.2K · <a href="https://t.me/persiana_Soccer/23988" target="_blank">📅 16:17 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23987">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pHfgW_7S7cAroy5oqrgpB9wK2-pyPSNYjE2b7Ddi7Ae3mxQS98qql-ouByEMdUEKrpKEPaneMYR3lxuQMKoQlDp6wrpQRyaZGE2VECQj4P30euOFuv3mdyKQ79wFzXDKYiI4QMZ0Wo8T31tNszTjQ82KkNshZY_3eV0wSByuErD5ADKeX0A34sr3EVJTU1VCc0YY9SlHUAk4nym1JQ_Q9H_kunzgCVdoXV3_EBXoodUDDQRQ4V4CJVFUMVcvM9zx46tZbMmePQ9egsG1G-2xI7Hl0TuLzvKuvbVsU_HI_1vj9IZvckpy-CWekIZXGRm2_GSCgu68dIgB45hSmlF6VQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
مصاحبه‌قدیمی کوکوریا در سال 2019: حاضرم موهام رو که علاقه زیادی بهشون دارم از ته بزنم ولی هیچوقت تحت هیچ شرایطی به رئال مادرید نروم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.4K · <a href="https://t.me/persiana_Soccer/23987" target="_blank">📅 15:56 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23986">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f8dba54f8d.mp4?token=Uzr3IrTfID43fkLZHxFKxLuo3lE1NGwIlqFFAHee6wK48wF07XvHISPen_pPd0A_2jr6NAL2NG_goR-rt4ioMK0KW2fkzEMmKmdxR50Ix9dvv9uQF1YepQnGr62LfmOEGZE35DN9oR1dS4IrvzzyKJxAxFavwt1pIVt0gMcaqfY04I7vwT6ssMjjWmmOwqdC05KJBVcVSNqMzMzdtTTtbY2zs4wONP_QoK62u3Xain2tvqQFx_CseA4YUsuIiy3PZKqkGcIO4j04JVAl1Ywsc4zTGARx8UT6SGTPYnzF9e-bgsA-LFSNnKGehp87319-_pTRSd4E0GZGwe_fvZKyMg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f8dba54f8d.mp4?token=Uzr3IrTfID43fkLZHxFKxLuo3lE1NGwIlqFFAHee6wK48wF07XvHISPen_pPd0A_2jr6NAL2NG_goR-rt4ioMK0KW2fkzEMmKmdxR50Ix9dvv9uQF1YepQnGr62LfmOEGZE35DN9oR1dS4IrvzzyKJxAxFavwt1pIVt0gMcaqfY04I7vwT6ssMjjWmmOwqdC05KJBVcVSNqMzMzdtTTtbY2zs4wONP_QoK62u3Xain2tvqQFx_CseA4YUsuIiy3PZKqkGcIO4j04JVAl1Ywsc4zTGARx8UT6SGTPYnzF9e-bgsA-LFSNnKGehp87319-_pTRSd4E0GZGwe_fvZKyMg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
سرهنگ علیفر: از اونجااصلا نمیشه گل‌زد؛ واکنش صادقانه آیاسه یوئدا بازیکن ژاپن به علیفر
😂
😂
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.9K · <a href="https://t.me/persiana_Soccer/23986" target="_blank">📅 15:38 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23985">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bTgrSJhrsfsY2NnarsaBA9ia_2WS-3avXB0A8zlcNNux-l6bHdOosMcrE7kzFYU4u7jCCRGwqNd5KJ3Lj93togFdCw9Jm56dSQfHY_vWDcggue0L7ONk33dgMZXenN-0tQ4roKOccxMendd8CJYg-eA8WhXuYuO7qdqGxfJtjXDgZ74rDsFoyHtNaV6MirN868qaokypyaW4JHDvEx13HsyBZr637rsLyj0nYKzYjDV0knATImodGN074PSQipYB-3K3rc1KUKc5NB1GW7Tw9tTjD1cmdZqGeM_UhTEL9FlKnz1U5i2nPg_XMlyjPp39qqZuPk5utlSlBS7ChAjfbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته دوم جام جهانی 2026؛ آتش بازی سامورائی ها مقابل شاگردان هروه رنار + جدول رده بندی گروه F در پایان هفته دوم رقابت‌ها
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.8K · <a href="https://t.me/persiana_Soccer/23985" target="_blank">📅 15:36 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23984">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c4e6bc8b00.mp4?token=WKmhXB1u7QkBZQLBlmQb737RCuIVMWs4NwEhFWYOfQZ35VbHUYXnhKpkeol7NRJjARh-oXAQpu34KWCfGjIwUtjtPNI3uKmaCJ8wxeDd1W-2cnIjZtOPp0jWxCg-3DLAnYxozfhYVrU3wJ6a4iToaUcEO7Z-FOBkD9gkD2PD7p9aPDc0UnzlBcrQIrShlb4BwQh7jt4qNnP928uYkqY6HNQ7h1OluAiGmqoag20_AW3qwOj1b1OM3jja9AbbWbMpoBGh3GWkgM5cXB58qzvpEQo9otVl0KEtlltOB1naQYYSRQXGi3ITJr1A1x5m4Ks-OryWGph7gOdZmh9HAp_Y8Y5ecCaHNQB8dsGVHSppgFznjxJYeKZDeX_xnutWVrGFzuBgyiiVkfdQvi4X3Uoqyj7bcCCmOmsbYmo3sfQXaT5P6vNBKfw15XokzGv-z_tsfNr1O2-KrCZVgiWG6WUhdvsdZlZutk8N6j2b_eDfGVtQjqAD-MYvYGeUixFViEHN6wRdGuTYVgb8w5wlYz21FJ95VvwfMom0JfkxeT8MWTvAQAOPOQMgSSLyvzUhniA91Z_dDXFsWZQqHztGtqfAwBufISrEMBOg35SI_CITHpJOPwNSZddTxa1blNDPZA8Ocaylz0ZMM6GQ_KyZTXPexAePf4_CmSbLir3A2l3a4_E" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c4e6bc8b00.mp4?token=WKmhXB1u7QkBZQLBlmQb737RCuIVMWs4NwEhFWYOfQZ35VbHUYXnhKpkeol7NRJjARh-oXAQpu34KWCfGjIwUtjtPNI3uKmaCJ8wxeDd1W-2cnIjZtOPp0jWxCg-3DLAnYxozfhYVrU3wJ6a4iToaUcEO7Z-FOBkD9gkD2PD7p9aPDc0UnzlBcrQIrShlb4BwQh7jt4qNnP928uYkqY6HNQ7h1OluAiGmqoag20_AW3qwOj1b1OM3jja9AbbWbMpoBGh3GWkgM5cXB58qzvpEQo9otVl0KEtlltOB1naQYYSRQXGi3ITJr1A1x5m4Ks-OryWGph7gOdZmh9HAp_Y8Y5ecCaHNQB8dsGVHSppgFznjxJYeKZDeX_xnutWVrGFzuBgyiiVkfdQvi4X3Uoqyj7bcCCmOmsbYmo3sfQXaT5P6vNBKfw15XokzGv-z_tsfNr1O2-KrCZVgiWG6WUhdvsdZlZutk8N6j2b_eDfGVtQjqAD-MYvYGeUixFViEHN6wRdGuTYVgb8w5wlYz21FJ95VvwfMom0JfkxeT8MWTvAQAOPOQMgSSLyvzUhniA91Z_dDXFsWZQqHztGtqfAwBufISrEMBOg35SI_CITHpJOPwNSZddTxa1blNDPZA8Ocaylz0ZMM6GQ_KyZTXPexAePf4_CmSbLir3A2l3a4_E" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خبرمصدوم‌شدن‌کورتوا کذب‌محضه‌اسکای اسپورت همچین‌خبری روکارنکرده ولی باتوجه به فعالیت‌های دعانویس ژنرال‌ممکنه‌یک‌ساعت دیگه خبر بیا کورتوا و دیبروینه سر صبحونه کینه های قدیمی رو دوباره کشیدن وسط و سر دختر دعواشون شد و گارسیا به دلیل‌مسائل اخلاقی‌اونارو ازبازی‌کنار گذاشت. ویدیو بازکنید متوجه منظورمون از کینه قدیمی میشید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.7K · <a href="https://t.me/persiana_Soccer/23984" target="_blank">📅 15:24 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23983">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fc33af7706.mp4?token=Vgi8G-EzbqhA43rBiPpcQmMAdzvS25Dymi5vEz7qnaLYxPIzeW242lhcRkmMmbIqfv6Xl3uqb2tB5uCwrT7II01IGa4UNrZyAsqCtNYqVsxGEbU6MN6HwJ3AfyV5Nik-darAmzqOyameVUN1_0wfvDMHKWCVIvd5OzgBu0lbYiXz_4UUyn7LMrxO2R5775Fzj_oCy3pBu9Yvdsc5X32NgWZEj0dILhd9NKO4GVCv86lJUIW5sUdq-q97KVCQ0R6SObH6jOtawiuHvVJO_e_jmUkrIALm7s2ytdaLsGFaufSzfFpU-Emu6PD8GytgmTt9QdXdzwcOiWhYYy0F_xYWgQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fc33af7706.mp4?token=Vgi8G-EzbqhA43rBiPpcQmMAdzvS25Dymi5vEz7qnaLYxPIzeW242lhcRkmMmbIqfv6Xl3uqb2tB5uCwrT7II01IGa4UNrZyAsqCtNYqVsxGEbU6MN6HwJ3AfyV5Nik-darAmzqOyameVUN1_0wfvDMHKWCVIvd5OzgBu0lbYiXz_4UUyn7LMrxO2R5775Fzj_oCy3pBu9Yvdsc5X32NgWZEj0dILhd9NKO4GVCv86lJUIW5sUdq-q97KVCQ0R6SObH6jOtawiuHvVJO_e_jmUkrIALm7s2ytdaLsGFaufSzfFpU-Emu6PD8GytgmTt9QdXdzwcOiWhYYy0F_xYWgQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇩🇪
#نقل‌انتقالات|اسماعیل‌ سایبری هافبک تهاجمی جوان مراکش‌باعقدقراردادی 5 ساله به بایرن مونیخ پیوست. هزینه انتقال 55 میلیون یورو اعلام شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.5K · <a href="https://t.me/persiana_Soccer/23983" target="_blank">📅 15:07 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23982">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e0eba240be.mp4?token=RzIk7bmcBUP_ZGbJEjrLrW1p-TOEp_zoXtMIBekqikabo_uPod4aVh9qvwZsOsVlEdVkCM3teCgnjxxIjfxJlI0NYU-5baGDb7XPXYGliWh7pS3SzmNaBuTZQp-_ydxBqXBROpJMmWvlUPmPIk75uPkUDYWEoWPWJFZ_gNlwbs3D-VqnnNmq_fDU46hTVheOGyUccQ1C4k53qa8-GBjXLrLk8wXqrQ1cQ2RNGzgJs2UEhWbQfF6z83yI8RuPg-bFfZiQZ3NPhNwAWQ3fyk6kzYrLkkszr66Decnu_oeWFjX4xAYk9Ko9T6WSssH3eNKl9-X0f0LRxuALg7nPsM0kqQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e0eba240be.mp4?token=RzIk7bmcBUP_ZGbJEjrLrW1p-TOEp_zoXtMIBekqikabo_uPod4aVh9qvwZsOsVlEdVkCM3teCgnjxxIjfxJlI0NYU-5baGDb7XPXYGliWh7pS3SzmNaBuTZQp-_ydxBqXBROpJMmWvlUPmPIk75uPkUDYWEoWPWJFZ_gNlwbs3D-VqnnNmq_fDU46hTVheOGyUccQ1C4k53qa8-GBjXLrLk8wXqrQ1cQ2RNGzgJs2UEhWbQfF6z83yI8RuPg-bFfZiQZ3NPhNwAWQ3fyk6kzYrLkkszr66Decnu_oeWFjX4xAYk9Ko9T6WSssH3eNKl9-X0f0LRxuALg7nPsM0kqQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
50 ثانیه از دیوانه کردن خداداد عزیزی توسط جواد خیابانی در ویژه‌برنامه‌روزای‌اخیر جام جهانی
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.6K · <a href="https://t.me/persiana_Soccer/23982" target="_blank">📅 14:57 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23981">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sFvRA2Wcb2NNkrOhMoFHR664ongzcI7kIZ-pawYut_U1PIxgvILtxbsQbNdu2JaiDoHzdLv5ej5eqOistFC50QwyDS7cwk_uBobiLAf77lKxygIXlW4FlHG5qsByW3GI5iqdFsq_hKUaeO4AQvyP0fPcqNFBvyJBv-9nqL7tDGJP5aMGnhueIc8kGjSZZx7JOZVoBpK5lIkzJlKZAUMqPfMISPql7hHuluP_UbA0sZNXvstHy8VBTHbj07pIwgKTlX39qmZsSHmVegT1rrOxvBZ6CFEOJZZyf_0Vl0-Hal-pfHYxKPnfukcujIdIlLm4aFfxW63cZtAl0MmRAlHNdw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
#تکمیلی؛سهراب‌ بختیاری‌زاده سرمربی جدید استقلال امروز صبح باحضور در ساختمان این باشگاه قراردادش رو با آبی پوشان پایتخت به مدت دو فصل امضاکرد. بختیاری‌زاده‌درباره تقویت کادرفنی و جذب بازیکنان مدنظر نیز گفتگویی مفصل با تاجرنیا داشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.9K · <a href="https://t.me/persiana_Soccer/23981" target="_blank">📅 14:42 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23980">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/krz7LPik4lGdTLE1zYLYshhDZ_rvZmb6YZT6xhX90XI6wZzIVqS9l-HMnbclsFrP1bdYV3eL2MHsR6iM8-Cc87apG6z0xMh5jXXZBCi5VgdOUVuri9KsGNxE1y9J9_tI4zoDXlPp5dyvHZlLtSPy8jr6Liz2-5w_4hnVzu_T--eAQ6Rl4KsduV-NGuXPHJO6e6dDlJ8zcDgrsHYNf6QQnFnNJcK-IU3rNI_uJOtTAbDvN09iBePgLpi5b1JjjA5gKUaRcJcEx0dxTtVjRTP8beR3IGmWOWmOF9doGR-ESw1xzmsuftqCKfU94CFcrvOB9O-KakBvA0U-0jCKKthO1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
#تکمیلی؛ تاجرنیا امروز صبح در تماس با سهراب بختیاری زاده سرمربی جدید استقلال گفته درصورت موافقت او سریعا با گابریل پین قرارداد امضا خواهد کرد. بختیاری‌زاده علاقمند به مربیان ترکیه‌ای است و احتمال داره دستیار دومش هم اهل این کشور باشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.6K · <a href="https://t.me/persiana_Soccer/23980" target="_blank">📅 14:13 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23979">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nESqrOxQS1v58VqVpcF9gZIDGu5jGzHSjisDBvXHFGnQV8IjSpGzEEMuTIa6xbG3ghR_M5Ol1peNq4YzJX6W9qwdnqP9rGUT9ayxc9JhCtFQDbtXwo5eylvo3WCmJsW7_M54f_CD0J2bWzZBC8XPLWbcPQrn_Dsjc0B3ry56UOL2vSdZyvWr9zqBLejvtW4NLQoIo6ecR08oEKG_vVs1o3SS8ho8njttlAGsxbnfLVLkASYRXEimOTNTzm9y-Vnwk46p3I9qOX8uxBgd0RKgWd04KQuaplxLEN7FaDSMdLoPogWNOOGVG7AO3GNEcyNYiiWOrJCKJyfr94122A-4vA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
#تکمیلی؛ باتوجه‌به‌تعدادسوالات زیادی که درباره آخرین وضعیت نیمکت‌پرسپولیس پرسیدین لازمه در این باره به یه جمع بندی برسیم؛ امروز پرسپولیس با اسکوچیچ مذاکرات نهایی روانجام‌میده اگه به توافق کامل‌برسند بر سرجزئیات قرارداد امضا میشه اگه به توافق نرسند اوسمار…</div>
<div class="tg-footer">👁️ 40.7K · <a href="https://t.me/persiana_Soccer/23979" target="_blank">📅 14:08 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23978">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b9df1a6812.mp4?token=hubq86CscdPLOig7FcAjDTsiStumoBdY2TCxrUiD5HSnXnenoxGfsyuNGsksnJuqkyExeGISSSoPwXrEVGhdFqyjALY0r_jIJ_OpfMgBraWQTtIrMnhP6g2FSGGwzGd-LyWxdYL1GiuaYqT_zLVTjfyMxenRHMPHqM-1eFoxv10Tl_uOUIy8S_YRxM2uzLvI3pCZCQaH3tGDDXBIKzW7x4g71AnjJxbwcQ2G8SbCK78iy7eQQb11ibm7gKCg3gpYWWXJkdpMt5XsNNZofONv_SkLcjXNNTwK0OlC3gKBjfMVu0tv6M5wHzGNIvFqxNRAnkpNleDXTXM8cMrBvtmb8w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b9df1a6812.mp4?token=hubq86CscdPLOig7FcAjDTsiStumoBdY2TCxrUiD5HSnXnenoxGfsyuNGsksnJuqkyExeGISSSoPwXrEVGhdFqyjALY0r_jIJ_OpfMgBraWQTtIrMnhP6g2FSGGwzGd-LyWxdYL1GiuaYqT_zLVTjfyMxenRHMPHqM-1eFoxv10Tl_uOUIy8S_YRxM2uzLvI3pCZCQaH3tGDDXBIKzW7x4g71AnjJxbwcQ2G8SbCK78iy7eQQb11ibm7gKCg3gpYWWXJkdpMt5XsNNZofONv_SkLcjXNNTwK0OlC3gKBjfMVu0tv6M5wHzGNIvFqxNRAnkpNleDXTXM8cMrBvtmb8w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇯🇵
هاجیمه موریاسو سرمربی تیم ملی ژاپن با دیدن هری کین کاپیتان تیم ملی انگلیس فورا تبدیل به یکی از هواداراش میشه و باهاش سلفی میگیره:)
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.2K · <a href="https://t.me/persiana_Soccer/23978" target="_blank">📅 13:49 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23977">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Nv7peAJ0HMOrWAZjVfKn9m_7EasSoZf3YbttEWgZhLSSNQRyf1R6gQ-e1QnsTQ5JRanvp0O2w4RFgC_CUdlF7ixe2OZuZWOROreBPfGkjlncCHAHNh-hae4st1Gfsa8wY-m7z_8UYL4dFQPqfqRASu71jPle1JChiLoUqDjXIPvVWYhUv8KH2ZiGDzuvHqr6QqJMQdNDfETdPBFwHmzXgkP8-9JGjASU26WWPTae9vogo-zMvBgNty4n1OiSlQDcirHbXn0GYGEzOzkbb_m1AvKxIfSVWfi0Fv2k-CJOWAYeuwS2MX4CjFZis2qqQVCDvZch3loexSIHNXyk3qEWEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
بیانیه‌رسمی‌تیم‌ملی‌بلژیک: آقای قلعه نویی عزیز دعانویست‌رو از تیم بکش‌بیرون‌. ما اصلا با شما بازی نمیکنیم سه امتیاز بازی‌برای‌شما. تک تک بازیکنانمون رو به دلیل مصدومیت داریم از دست میدیم.
⚪️
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 42.2K · <a href="https://t.me/persiana_Soccer/23977" target="_blank">📅 13:32 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23976">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CGr2AO-3puRbQ-APZ6wZ4wT29u6WZQ_E88a-c4oVkTswasnV920zWKZsrM_9us6XJLv0YZ_z6uK5vZowQRjjbgnKnEAnc2TqxT-nHf3FY1SkQk58dSm4WcTi9MIi0dnmV87BVusNV6peoWGJiVXzYBsOFxzFg42h9qfUt55kU5hplIOmLCILETmvjPlwn8ODB5s_PhVK_KZ3NeEZeRx3LNaxWO9mrEZLUCPLULf-fG9lrO3wKzMu3D0R9IeMwHo1NMMM5RYqq-KbvxWTkcRThdKgFesYN65aRXS3uzkcCTg5rHiPUtt3DKRFgER7woYZiDCME4kTXVWbt-8jzZ9RKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#فوری؛ مگه‌میشه؟! رسانه‌معتبر اسپورت بلژیک گفته لئاندرو ترسارد ازناحیه‌کتف‌احساس دردمیکنه و ممکنه دربازی‌امشب‌مقابل ایران فیکس به میدان نره. پزشکان بلژیک در تلاشن او رو به این بازی برسونند. تروسارد جانشین جرمی دوکو مصدوم شده بود.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/persiana_Soccer/23976" target="_blank">📅 13:26 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23975">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tizu5hK7fOUkzjLexAFvcH7vrkcDXhFm3Y-H7uC7wX1DtIZ98wgcNmbwd9khxEPWGqMBaIm4McqCbOpy0ThuG-mvy_q8MgpZ1I8YQ_RSlXiHy_2uYSv6usSoVrLh5QxPVnKJOXb9QLYaK9p-KMIhrBHqAfc_Mp37HXmgeaRa5E-5XowI8gAkFrUdT5YUqelIVr7CCoV72H_ju2Ec-cw9D7AkBxVkSn88Akk6loKi1OikTbK-ywpG0auEzAe7MfQ57JZByoll8MVvuHNXEXKrEfmJC5pieiEONe2TNG0y5x4kE5ZgGUgBQiz-tnqUAg-yePR1w8CcJzcDkNWg-meHNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
طبق‌شنیده‌های‌پرشیاناازباشگاه پرسپولیس؛ امروز ساعت 14:00 جلسه نهایی مدیر عامل باشگاه پرسپولیس بادراگان‌اسکوچیچ و نماینده‌اش در ترکیه برگزار خواهد شد. باتوجه به مذاکرات مثبت روزهای اخیر انتظار میرود امروز قرارداد رسمی بین طرفین امضا شود و اسکوچیچ بزودی راهی…</div>
<div class="tg-footer">👁️ 41.9K · <a href="https://t.me/persiana_Soccer/23975" target="_blank">📅 13:18 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23974">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n-e7xbGm9FzzUDoleq47-JP0L_bbdiH-iy17_0VYH8Sjhq7nbSUA3LPXq07IhRWaE3tQdzp-NhVP7--vLR7_QvnVdBNBhblHEN_Poo9YqLuiyx4egpnjTVzf0sPQwyvygiwgmQ7w3IRzkb3JxDWmv71-tUjm9D2_R9S5j59NQEFw8RCgwP8eU5KcjvZi6MyIKLPqaQoZfPX3o6n93uJ45NqkD13L5mWrHUuuoCnsOZhX2hbUiQ5FcABIvk9INtvQq6WFJHoIfcJPpRlSlv74UQw7h760xaGzT_sJs8TiL2S3jD5rPs7-ZncH-USDdYVQnRwXXOROZrZLqIRrnYBXWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تاییدخبراختصاصی‌پرشیانا؛ با اعلام فدراسیون فوتبال رقابت‌های‌فصل‌اینده‌لیگ‌برتر 18 تیمی خواهد بود. هیچ تیمی سقوط نخواهد کرد و دو تیم از لیگ ازادگان نیز به رقابت های لیگ برتر خواهند آمد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.4K · <a href="https://t.me/persiana_Soccer/23974" target="_blank">📅 13:07 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23973">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/415bb37d05.mp4?token=SmVVNjp0g1M-EUS30eKaAttygDK7i5qfnqtwVxLH7dG23tX6vcebLHPbBxUJmDPHdtY7qGPOmkIYLWSsMLuTzgTykuFQiQYiX_-duLi6tJpbWiNMaRavkW9dcPGkGhFUR2r_fyHx1acpJoNDq8D5Zf0a5leQ-17mjfex6PiBp2Is3rioZAJ8kMr3XF6wo4Yz9WkA7lxBHDr7_e0LLHTQ_ZV3te--Mb2oSGQYy1aUuMz42O26ezk8hoTDI-kwTxRkhKpJKq6b9YBfjeXiin5SSMDawKF-M8BlmNKjduj1ik19G8hXlClpC9CTmm-yNV6RXuJSuxaVccVSstBiqzQHWnqk2paAsK2bpI9qeKHmtVCgRU42ER_JH9hssXHTF9E3a7sJlL8Id0w7lFsII3hwRdWx3UJzFSG61VNM-swrwhzM-7_2sEFwqydgdCG25mwqItxjJrRInMuBZnPf_MiMSYtXL2-2_grmDKlGEy-F0TmmmfAKEx7m5WRxWY-DjYZk02YpaHwWaZIMCRmFxW14BdKkOLZk9LYzip2xurJ98gekeJfjEUxgAqTjEO0E16GiGbhh79ckp72q8tLiawayN2l0SMHkRZeWUrmPevMm6WFlIQJfSTkNq1zfc44iyfSBxtBkyUZl3WjfM062gm1QbIWEGzdiCUvhz_rzWRWNBdg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/415bb37d05.mp4?token=SmVVNjp0g1M-EUS30eKaAttygDK7i5qfnqtwVxLH7dG23tX6vcebLHPbBxUJmDPHdtY7qGPOmkIYLWSsMLuTzgTykuFQiQYiX_-duLi6tJpbWiNMaRavkW9dcPGkGhFUR2r_fyHx1acpJoNDq8D5Zf0a5leQ-17mjfex6PiBp2Is3rioZAJ8kMr3XF6wo4Yz9WkA7lxBHDr7_e0LLHTQ_ZV3te--Mb2oSGQYy1aUuMz42O26ezk8hoTDI-kwTxRkhKpJKq6b9YBfjeXiin5SSMDawKF-M8BlmNKjduj1ik19G8hXlClpC9CTmm-yNV6RXuJSuxaVccVSstBiqzQHWnqk2paAsK2bpI9qeKHmtVCgRU42ER_JH9hssXHTF9E3a7sJlL8Id0w7lFsII3hwRdWx3UJzFSG61VNM-swrwhzM-7_2sEFwqydgdCG25mwqItxjJrRInMuBZnPf_MiMSYtXL2-2_grmDKlGEy-F0TmmmfAKEx7m5WRxWY-DjYZk02YpaHwWaZIMCRmFxW14BdKkOLZk9LYzip2xurJ98gekeJfjEUxgAqTjEO0E16GiGbhh79ckp72q8tLiawayN2l0SMHkRZeWUrmPevMm6WFlIQJfSTkNq1zfc44iyfSBxtBkyUZl3WjfM062gm1QbIWEGzdiCUvhz_rzWRWNBdg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
ماجرای جالب آشنا شدن اوسمار ویرا سرمربی فعلی سرخ‌ها باسنگربان برزیل‌ و لیورپول؛
پسربچه هفت‌ساله‌وتپلی‌که حالا یکی از بهترین‌های دنیا شده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41K · <a href="https://t.me/persiana_Soccer/23973" target="_blank">📅 12:49 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23972">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mLm1iF8HSEcLdl2i_TJDuNTDcJL2KnZpc97ry2bgXVcekwpyeETQwNSrGLL_SV7nSG_TjDw-yaomZRdjtgc4kTmaQr3e1tEwL5S4teLGEvc8JLrSbpR2E_JuOZ-c_4CeKqoKphtdvk7Baizn0CpiWxEUCxFK80AvqzougnifrNi0nYAPrGu3yRmvoW8m4TFOwoB4lnwLOBN3dSK3YB1fpUdpvJO8EnQfwTHpKvYRcF4KFvjusqtZhm-yeqc_DGlNDzJNkwR5iBJmGtuTp3yM7t8-fcGwpTa0EAFdcTlEevrpIk2ziZjld5TmB_2JZfE6nMIkoUH3yRm8VEN8-CJNtw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
رکوردداران‌کمترین‌درصد مالکیت توپ در یک بازی جام جهانی؛
پاراگوئه با مالکیت ۲۱ درصدی در بازی با ترکیه، در رده هفتم کمترین میزان مالکیت توپ در یک بازی جام جهانی قرار گرفت.
‼️
ایران با ۳ بازی، تنها تیمیه که بیش از یک بار در جدول کمترین میزان مالکیت توپ قرار گرفته است.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.3K · <a href="https://t.me/persiana_Soccer/23972" target="_blank">📅 12:38 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23971">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rJTnP7zdP33z_VmBBDSGjDVrgbhx32bVftzrIVjySxoLcid67jXNOxkbyOq03Z6qPZSNNhauF8V29pJG81ZZs0oDrxvyzmAax5pLy_tbWt8GhWDbXVwvFJeFiUdsVqH5aBd00qtCts35QdNmc-5IYgtorKrtLcDEFFpZVMGhdoMIKJ4UtIz5FQ56rvQZt1R9HBP2NzqOA0b39k_f2eV23mMHZXbi84aB8l19ClA4y7x-XTnQAfxY5Av4QDtCWcL0JqoZgrOZy3vEqWNy8uBHbiHqjsrgH5fz3DeZ9d_L_iyIMFhci_lKxSpwoP3PTTfV5MgMd-bTilgueLz3znkSYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📱
فوق‌ستاره‌های‌فوتبال‌جهان بابیشترین تعداد فالور در اینستاگرام؛ کریس رونالدو با اختلاف در صدر.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.9K · <a href="https://t.me/persiana_Soccer/23971" target="_blank">📅 12:19 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23970">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a3e56w_BRo_ed1CgvfpqM-NC2nKHIYwrqAoKq2IfraL7Q2U565A3uTsYjV65OFkr9jOYyzPYVpwiLQo2EgHqcT1Pr9hk9eW2Z3pP0CP8-q0QwGZiGnlbxo_DBJu6jBVBk8u4wXezUu9b774Mj33ernqSqKR2zV8_w80nSOcW2Kq5aUICnprIfmLg8WHgjyl5Xgt9RaOr2WHvW4UxhSxQ8NbBCt660nDphCQXnqQokSY_dhcuUkBqzIRuOzkJfbK9pGTzBH5BdO0gHdBp-eXT3snYzfYFboLNcjTDDbrSx0rDd2aqq817UMVyhs-HsdWKAmyU0zEiwrqtrOiCZ4xlzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی؛ به احتمال زیاد دراگان اسکوچیچ کروات روز دوشنبه یا سه‌شنبه همین هفته وارد تهران خواهدشد تاکارهای‌معارفه‌اش بعنوان سرمربی جدید باشگاه پرسپولیس در هتل اسپیناس انجام شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.6K · <a href="https://t.me/persiana_Soccer/23970" target="_blank">📅 12:04 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23969">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9d78439566.mp4?token=eFzU5_BEqMIOdGa9g8AifJzTs2OYeAE5vSbQkA5vRl6S2xrI0YyVWPzTW70pJF9GL8p7-pcGYl6JD4p97Jk9KUxF-u3jYMGaj2ow99J74OIa7pkQX2PPTVIgD9N8joN8fODJaET_1j_dxn0YhRvHShduF7EssGCQbfpNX3zAYdCZ59SdjEqsMyKKNsFCjGF5NjqC_62hd-LCQziyaD5GG7vr_t3swqih8FmaJ_srzSfZ-S6QI14E7LIxKxGzrz0cRrKgdmYvE4wMAfdqNIERfh60fLzxmUmKoxdCzvYVMhbxkuxVeuCrCqglqQZ_yeRgahZrj9H5WASyeQBwxtIkcQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9d78439566.mp4?token=eFzU5_BEqMIOdGa9g8AifJzTs2OYeAE5vSbQkA5vRl6S2xrI0YyVWPzTW70pJF9GL8p7-pcGYl6JD4p97Jk9KUxF-u3jYMGaj2ow99J74OIa7pkQX2PPTVIgD9N8joN8fODJaET_1j_dxn0YhRvHShduF7EssGCQbfpNX3zAYdCZ59SdjEqsMyKKNsFCjGF5NjqC_62hd-LCQziyaD5GG7vr_t3swqih8FmaJ_srzSfZ-S6QI14E7LIxKxGzrz0cRrKgdmYvE4wMAfdqNIERfh60fLzxmUmKoxdCzvYVMhbxkuxVeuCrCqglqQZ_yeRgahZrj9H5WASyeQBwxtIkcQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇧🇪
بااعلام‌‌رسانه‌های‌بلژیکی‌؛روملو لوکاکو دیگر ستاره خط حمله تیم ملی بلژیک به دلیل مصدومیت جزئی در بازی‌ امشب‌مقابل تیم ایران فیکس نخواهد بود و احتمالا این مسابقه رو از دست خواهد داد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.5K · <a href="https://t.me/persiana_Soccer/23969" target="_blank">📅 11:54 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23968">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">‼️
رکوردجهان توسط یک مرد اهل جزیره کوچک کم جمعیت‌در دریای‌کارائیب‌شکسته شد
؛ الوی روم دروازه بان 37 ساله کوراسائو در بازی دیشب مقابل اکوادور موفق‌به‌ثبت 15 سیو شد و رکورد بیشترین سیو در 90 دقیقه‌یک بازی جام جهانی رو شکست!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.9K · <a href="https://t.me/persiana_Soccer/23968" target="_blank">📅 11:51 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23967">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/21c204841a.mp4?token=YKcWRpPjfCHrO-2F6JhoZb3Zad465M3PSEcvYFuJk75WPsUrkO-OBaSY2-73L-ZewLp6U9jnWDhPA9FZVPY-HtKIANAN6dYso3-Cd3h6k8Wd1_9KtY5Xk7HEjxxJmIq8DFg-J3Zu9nG2GxeEog5C6WqF7QsBf4gBbxkrHD6e9O3OAxF6dfW3tasj8r_HHN41bkoildwDmR7D5gr8puCclPXiIIjlPr_5uCCHiCWI0AXCdey18v6-4R7DemI_qsJGu3bpcWIddb6oO6h91k-HKWw7Gkce-OlfLzTrh59xBaton2J86DWaU389xazJ_xVOwcDuZK2bQhYpAJ55ve9hAA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/21c204841a.mp4?token=YKcWRpPjfCHrO-2F6JhoZb3Zad465M3PSEcvYFuJk75WPsUrkO-OBaSY2-73L-ZewLp6U9jnWDhPA9FZVPY-HtKIANAN6dYso3-Cd3h6k8Wd1_9KtY5Xk7HEjxxJmIq8DFg-J3Zu9nG2GxeEog5C6WqF7QsBf4gBbxkrHD6e9O3OAxF6dfW3tasj8r_HHN41bkoildwDmR7D5gr8puCclPXiIIjlPr_5uCCHiCWI0AXCdey18v6-4R7DemI_qsJGu3bpcWIddb6oO6h91k-HKWw7Gkce-OlfLzTrh59xBaton2J86DWaU389xazJ_xVOwcDuZK2bQhYpAJ55ve9hAA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
فیروزکریمی‌کارشناس‌ویژه برنامه جام جهانی:
خانم‌های ایرانی می‌توانند داور بشوند. حامی بانوان هستم‌. داوری بانوان از رانندگیشون خیلی بهتره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.7K · <a href="https://t.me/persiana_Soccer/23967" target="_blank">📅 11:51 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23966">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U9BUGbYT0Pq1WUI_orfFngIhXiKpuVGC_zbOgivD2Rxyjn_DTZXuWKObTDzSAQsHZVdw0iQiWWV7wykZIeawAnVnnwwe5GS5vCijG2oQY4QNyIYSJ1ckItaOm_jNE-qbCzXxo_JthINhOc11HKyq5e6hMmdetXa9FRGn9YqK5CiclQk7vFzBT9lDaQgU1dQ-p42YqNADCSI-iy6EHiwxmmcilLuUTJousPRbRd4hbIpkY-TyaEs6B2KIkQIuu7ZBEX5rITVXKORQ65AIX63nz8U3vHXMU--zwsYZnI-9Xtotiqxq0reTUSXxFTk2t1P876d23dJr46izC_R5qU-YVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
پیشنهادویژه‌فقط برای بازی ایران
🇮🇷
- بلژیک
🎁
🤩
🤩
فری اسپین رایگان کازینو در انتظار شماست!
فقط کافیست حداقل
🤩
🤩
🤩
هزار تومان روی مسابقه ایران و بلژیک شرط‌بندی کنید و
🤩
🤩
🔠
🔠
🔠
🔠
🔠
🔠
🔠
رایگان‌دریافت کنید.
⚽️
بازی ایران
🇮🇷
vs بلژیک
🇧🇪
💰
حداقل‌مبلغ.شرط:
0️⃣
0️⃣
0️⃣
0️⃣
0️⃣
5️⃣
تومان
🎰
جایزه:
0️⃣
5️⃣
فری اسپین کازینو
⏳
فرصت محدود!
همین حالا وارد شوید و شانس خود را امتحان کنید.
هوشمندانه بازی کن، برنده شو
🔤
Winro.io
معتبرترین سایت ایران
🔤
Winro.io
کلیک کن و درآمد کسب کن
📱
کانال اخبار و هدایــا er31
🌟
📱
@winro_io</div>
<div class="tg-footer">👁️ 41.2K · <a href="https://t.me/persiana_Soccer/23966" target="_blank">📅 11:51 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23965">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t6YyB3C8ZqFOGHuXZHeGzIhox2dgRhmaHXrTBE4OpakHxxmwzNpijjqmEUIJjI0AIBRakdHdgPHPAOJlyzGjGG5QGopfFelXybviG_A51o20SMAHvwtik32nOTwKsNRkGkpbQCXIwjIfguyPm6Nbv23vSLfa-AgUnba06y_QoIXd8Bs5dNW1lRcXTv7BN7rARHvfN5fWP7vbevBY6_vS2c4nChi3hqhzkb-1BkLWW-vs82Ng5mIMMneGvtoKQWlMbMHp-Oun1UEEQixuixCxkF9EjoHugk8m2BY_pF8spJZ8FS2cBNMKt0XdvqpAg-iqi9NwGD432K-qQ0Fc3KyRwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇧🇪
طبق ادعای رسانه‌های بلژیکی؛ گویا روملو لوکاکو ستاره تیم ملی بلژیک نیز دیدار امشب مقابل ایران رو به دلیل مصدومیت جزئی از دست داده است.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 44K · <a href="https://t.me/persiana_Soccer/23965" target="_blank">📅 11:28 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23964">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TIgZsA_mTWr0cQFyT1o5vSVkSIz7I4KK4w05mWwav8yx5I8MYncoD9EGaTht9TXBCuqkFlP4-W6hgGl5N2PsS2U0wP3zGsxV70ExfnlQcYV_KO1TlvUMJVB4XDrXxgxGj9OfnL1hj5g-Io_gpxSAseBTpTtji9MfBuabAIAYfXUy2CT5a8ilGjkAU8RqBn8N7GKOnB6_Dgdz3rUfkJhL77w7sr470J5rnvNxE_7CEzVvzYfhHxR7wxdLJPoAP1rvEYdpk_xHZ8f_EsgtnrUmRsbAffrnaDxc-Q5fCowkivF6_2wC7ZH8zoCducTX0abUWRJ3KC4PuydGPP4oMervMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی؛ طبق شنیده‌‌های پرشیانا؛ باشگاه تراکتور بامدیربرنامه‌های محمد دانشگر وارد مذاکره شده تا در صورت توافق مالی با این بازیکن قرار داد امضا کند. دانشگر در کنار مذاکرات باسایر باشگاه‌ها درتلاشه که با قراردادی خفن به استقلال برگرده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.3K · <a href="https://t.me/persiana_Soccer/23964" target="_blank">📅 11:09 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23963">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QmAz8XWI6zu5xgXdJP-Jel1z6FjiFw8aAraS_ump66hb6x6NjUON_1ajTmwYetXl6l8GPS6Bg2QwBT_eTmOZMieBssXgxDLb33tJoJjpMNm_DhSOY1u3sSBpYkAKww_6rHcurrAfGwbAyR34sW5JqyJcOBOHxNlpUOLlQge8yy_A8MBJFW0vBORiQoZ_JNouutPTAhbCPeLv3OV4kYVgL1jn2Nkh5FM9z8UFjAjiuUc7TqEkfVYig64h0LeuBaYCR00bYXn9dk85xZm-z30Va9ga_cv9GBerBgN7E4sY_ollnxq2PnGnTQCay8cvDuLVCgo_eNpp00yqqdX-fZ29yg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
طبق‌شنیده‌های‌رسانه‌پرشیانا؛باشگاه استقلال امروز با وکیل‌ایتالیایی‌خود تماس گرفته که این وکیل به باشگاه اعلام‌کرده‌است که نهایتا تا پایان هفته اینده فیفا پنجره نقل و انتقالاتی آبی‌ها رو باز خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/persiana_Soccer/23963" target="_blank">📅 10:44 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23962">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L0bsN2EGRdzt_Dv3QE0D78Q4eYRWOnRU36S2gp7pWgGvr51nOLIOFoh5DzWHoyCkn3OMhJaEoUMQD0VyK2CHfHYcjAvRGWQYuJsca8dPsRymKCiNWu6p5aS24aRFaAHC0Q42wt5JGce9XHayk1bFPb15Gd4pJy_BZAtmQ4_syuPhn_xyJT1YxK0J7fp7B9JAvVikHw2wfY-ufUTRXqn-drOZWvc9XwmGallVuehqMfYzrBxPA5ZxZ4JlxCs7KzL_HjaYeajl_zgD-RrYn3JS_0lVsvbr0w4jKkfBO3f0cKmsL51prUoyRwAnjC7TazQzv5kv0weALK1tcRGivjBvnQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
پرچم‌باشگاه استقلال تهران درحاشیه بازی امشب دو تیم آلمان
🆚
ساحل عاج در جام جهانی 2026
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.1K · <a href="https://t.me/persiana_Soccer/23962" target="_blank">📅 10:37 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23961">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Rax1S2ThfEDX0VcH3flGfa_1tsnoMd2ooFj13OQNjFhEtWH7E9ASojyJI4cS1whky9x99KgAOM7hgltyzcXf7m2zFgRKICSj2xgr3BS8mg34uGricsN9pLaXURABIlKBZ-v7UHqnqmKQ9rQinr_8PAZJ3ogTyavxu9w1UKMggeAJTUyy1CDdPOcuGrJkzAWI7m8XS5I7NqhJl3uxhIhAbkxx_W8jbIdWXIk4Eai-uCNpHNV-5cws98YEQWP4tgx1gQT_JFFWCg1XHIVOJ8xIYNy9jXdNkLylA1VXoIyyWHlx34Eig8Xm9C7oJR-JQah7X4cN2eDJPKZ_cvqO18fmaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
آمار پیروزی تیم‌های‌ملی‌آسیایی درادوار مختلف رقابت های جام جهانی؛ کره جنوبی فعلا در صدر.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.2K · <a href="https://t.me/persiana_Soccer/23961" target="_blank">📅 10:19 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23959">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/550fbf8a8f.mp4?token=QCefCO_7oq9LkN7NA3kzXbaStI6mq7n2T5bJnAJlA81w5pnVHNqzXkQv38oKBPIB7in3Lka7BMiU2HOM-naBXZqC_IeaKV_tv_5GUn4CgJi65JuvWJ023_tPEQpm-wZdDQK1JM7a292rUt5p1FRz3SjAWE7VS46E_Kh7uef82f_NJNC651hiShrfbwnlh5fyrNLLmb-jO1-bPH7ycjaCxBwp9Tkb6Ff75Rqb6e3icJW6msKnQr5e_VMEtXqrY90GfRg0gafE7thBM5U1YAWMCWcX-QjrFKijUYDaap2boBoH7HlA8V47o32QFklbsqlyk3M9Zdsdf16jv-OethwUqw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/550fbf8a8f.mp4?token=QCefCO_7oq9LkN7NA3kzXbaStI6mq7n2T5bJnAJlA81w5pnVHNqzXkQv38oKBPIB7in3Lka7BMiU2HOM-naBXZqC_IeaKV_tv_5GUn4CgJi65JuvWJ023_tPEQpm-wZdDQK1JM7a292rUt5p1FRz3SjAWE7VS46E_Kh7uef82f_NJNC651hiShrfbwnlh5fyrNLLmb-jO1-bPH7ycjaCxBwp9Tkb6Ff75Rqb6e3icJW6msKnQr5e_VMEtXqrY90GfRg0gafE7thBM5U1YAWMCWcX-QjrFKijUYDaap2boBoH7HlA8V47o32QFklbsqlyk3M9Zdsdf16jv-OethwUqw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
سرهنگ علیفر:
از اونجااصلا نمیشه گل‌زد؛ واکنش صادقانه آیاسه یوئدا بازیکن ژاپن به علیفر
😂
😂
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.2K · <a href="https://t.me/persiana_Soccer/23959" target="_blank">📅 10:02 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23957">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NZox_iem1rOdn3mRHlUztAXjABhMAWxE70Wk-dHArBl-OmosfOxUoH_1NO2yq51S-E3_aFmkeOkuBt9BBz5DsAxWKf0iWWFRBARJXnfNS7wvBn9G_7Tgmb53SwBvep4HwE9SWTA1S5wRijNq-elA3oBkCiWLl9leHuLlAC1Jvt9H79BOLjlzaTYeuCj6igxTFT0mdemvnsLzftXWd4s7SRJeSHiPigIFrQMvRPO8xRrHaxYBXZKuNoUwVsXx8DOLZbaC6ny9QYobe2wEdOobgZpV3uemKAGa4SLZUEIbQWunRj5EqCStGRGJAwaHN4YchF58oTd744sxaUpjJdI98g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TwZ50vwVKRTJTmKzlnOEt5oGsj2zjAl6i-LtlGI7rEC5ZTJZ7_GAD-oD_md6XxrJHGGw_PdudE4yD2E4mU0HLXW3xw7f0XoF8p5xIGzIwsCVDubugse_tILUCyUTU9RfifsWcWWadrm4RmGdwTp96IPPtb3Z37XaYGL9CO333_QZdFmRAb-lVD72G1AfthIG9EhQ23SjNYRrCI0QBVH9xBo4XTnAv2SRxs0ky2x2pt9jfmq7sIsft-DQmrctJjpllKDFD5iekjfTY5Tjhw5JEWuXG2oysADLuKt2OwlOxtkMFh6Q60xJpFn627ElE1oiFga8YarQhgFIBdNTxt5u5g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">✅
برنامه‌دیدارهای‌امروز؛ از جدال ماتادورها مقابل عربستان تا مصاف بلژیک با شاگردان امیر قلعه‌نویی
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.4K · <a href="https://t.me/persiana_Soccer/23957" target="_blank">📅 09:52 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23956">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Psj4lHQ9EmSK_DbXW-OegFPkvuWXIs4QHvhPTv6Qd5pchy9SCUkGEv45A3TSGf0Rw-c1bacmugN75HLD1_tIvnXtWXg8xUlViO98Pld9JB1ZuNNOdGgKALchm6V6cLwlO_STkZfNpiczOAthPpLoNdjGPfq2_fqddyfHsQ6-5ODtLDSbmoehV4ULXWXURfpUEg5T_fm5DMnHCfAk90bEJwh7iM-UoLWP_BbYmaPy07liyvsDBekmuId0Ji6utR3bjw-kPykXJyu7PGuiDiwfU2u7T6myzsXVZFUcW9zzj-4PEUls9q-OqmkXk8XZ_D1bKwrUPqHzqrfHbww01YT-EA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇧🇪
رودی گارسیا سرمربی‌تیم‌بلژیک:
مهدی طارمی، سامان قدوس و رامین رضاییان بهترین بازیکنان تیم ایرانند. رضاییان اگه 25 سالش میبود الان در یکی از بهترین‌های تیم‌های اروپایی میتونست بازی کنه‌‌. چند تااز بازی‌های او رو دیدم فوق العاده بازی میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.7K · <a href="https://t.me/persiana_Soccer/23956" target="_blank">📅 09:01 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23955">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dvQ8kjivefkVqZ5hlrlGtGjwsfmClCwoeZSojlpbJ-avYIwqqBCnmjYNBUWTS1f0oKiWpNgru0jMSyZOKVIz-mudTlB7J55hUdOFhVtwjmduH1_sRlchvFdKaHuD66mKF7MvFC8k-dqYrh2cd6Pap6MHwzJ346y3vZaG_2nR8aSu2mgcAH26J95dgsAGISqWT2kXuf7moun7zxzHO5WC5eCU0h4W-qLbYwAe2N13czSN7UWpPnrWxpG-PFy-uo-awKppMbbLgtTCe4k081gYZJlb_y9NZyhqCdzkWwgkgL_JWUohozFOO8i-nfT2YqomtqaCzUKJNFmeIwH64MbCUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته دوم جام جهانی 2026؛ یه پسر کُرد سه امتیاز ارزشمند روتقدیم ژرمن‌هاکرد؛ کامبک  دیدنی شاگردان‌ناگلزمن‌درشب‌درخشش‌دنیز اونداف ستاره کُرد زبان آلمانی‌ها در فاصله تنها 20 دقیقه.
🇮🇪
ساحل عاج
1️⃣
-
2️⃣
آلمان
🇩🇪
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.4K · <a href="https://t.me/persiana_Soccer/23955" target="_blank">📅 02:56 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23954">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HL4FcC-nWkWb306KvSlGiO0ceiwnT23p7C_KA9GM6uKhbbsLLaWAhnbpuG-eBj9CGzXaVebkrcqEjCsGR8Bf-dCuNv8bPO4EJU68A2lzWlvgIUwa6QjSLrZKx9YNuEIZIqclwgJ9xyOkHUqAwnSVL_IHKqgbYOtcMjUTR3TT0gB7vV12rif_G0kavkyRoInmUkvjfWjSc_yEIgcqzYxRNvwBFvsm_jdWnbIKkLMOzhv8PrkpBAm_McZkBvWwDuOJ4EAHJZOI_g_RSKlSoSX7UxXvr6qoAw8KYXbHxaFLXV_QSdUg3KXRqp1egc1usKhsZUqid-SaijKD0EZyAKbMpw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇩🇪
دنیز اونداف ستاره اشتوتگارت همیشه در شادی های بعدگل خود کُردی رقصیده تا اصالت زیبای خود راهمیشه به همگان نشان بدهد. امشبم کلا 30 دیقه بازی کرد دو گل زد و نمره خارق العاده 8.7 گرفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.9K · <a href="https://t.me/persiana_Soccer/23954" target="_blank">📅 02:35 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23953">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D-wTJAy4NSvngcQsdlcqKa_XHEKhjDL-rRGo3iK2euPuAI3FrQs7lLh6B8nabvAk0n9Z-KixGZFCh7xtsfQeUCFjIDlS2lQsiCzhqx8L5MQyRbpSajflPokhdCdvu_hrdR9xRMScGMhB2ExcBj_7VB5pyFpWiwqD7iH4qw3w0qtnQdcnJlARSjLG5sptskglJDGzsFPm0Z3z1NMh-cDIbtX5NNkBj0hUb4PgLGN3IwjJ436WuYIuvWrb3xQdr5bZUPWDwo_j793048MzyD82VnNCy9tbUPTpv5gZcQAx7_1zen4taCObAdTaPhgveGjXNWqZCQu8z7TCqngyjBJV6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌دیدارهای‌امروز؛
از جدال ماتادورها مقابل عربستان تا مصاف بلژیک با شاگردان امیر قلعه‌نویی
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.4K · <a href="https://t.me/persiana_Soccer/23953" target="_blank">📅 02:05 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23952">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Co9WAlgrURpo57RC82szb3w_HedE2WQLZ3m4QKDI-xUrEavGTvODZbFmp5bXRVt0a_LlUiUbqQu1wCLE5QJz977EuvtwmbrVxe-ai4MNBuXjrbliucVKQAKcQn4gjRl79tXy_qg5F_UtI6ytK06wAw2i3MnkCIsLR754z6-Dcs_Xg_twQbQB9Q-KOUtDoVtGVpDvLHrjxA9SYM8mLvSs5CdoD-6ItNO_OqCKptDj-ghFjdC4crg2qZGCVSnEgLMScKNXmMsQpVdZRut3X8WKdRhoaIIEPdtYEfiaI0krkGZ0Vl90Q9APBKQ0sUJtDzKfjEajVRcyAyyExMAioLesFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌‌‌دیدارهای‌‌‌‌دیروز؛
ازبرتری‌برزیل و هلند مقابل رقبا تا راهیابی مانشافت به دور حذفی جام جهانی
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.8K · <a href="https://t.me/persiana_Soccer/23952" target="_blank">📅 02:05 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23951">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2bf800e040.mp4?token=j5v6bOIYZ_7-cCwd7mb9AF8G9Xq0zS-HjthtdYQ6q8iL6SEtG6UgdmXXN8fF1d1dDYz8nVwLdM__zj4wpHz1zCfBl4SUujLNY_qOzQg7nilubIjt9oztizV-u-lr7PCBGvlF5jsr4vfKa-IYZNdMR97PFEIFWw4yJkJKmavzZF6MXkOhGJlrOvmKpndKx6Q0CB9Qj1ygqcbqUcvsh2t5uSo5NQocL5DDAjuvjCL0oStT8Nvx95S-Y-pXK8coERXuMO7VYfRabckgBiAhJQhXqPAQpXeb0uPCoke9NyexwES-zdcYmHr2zBLuweXUE3m8K3QKVAbFLk4GO1xghcoFdQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2bf800e040.mp4?token=j5v6bOIYZ_7-cCwd7mb9AF8G9Xq0zS-HjthtdYQ6q8iL6SEtG6UgdmXXN8fF1d1dDYz8nVwLdM__zj4wpHz1zCfBl4SUujLNY_qOzQg7nilubIjt9oztizV-u-lr7PCBGvlF5jsr4vfKa-IYZNdMR97PFEIFWw4yJkJKmavzZF6MXkOhGJlrOvmKpndKx6Q0CB9Qj1ygqcbqUcvsh2t5uSo5NQocL5DDAjuvjCL0oStT8Nvx95S-Y-pXK8coERXuMO7VYfRabckgBiAhJQhXqPAQpXeb0uPCoke9NyexwES-zdcYmHr2zBLuweXUE3m8K3QKVAbFLk4GO1xghcoFdQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇩🇪
دنیز اونداف ستاره اشتوتگارت همیشه در شادی های بعدگل خود کُردی رقصیده تا اصالت زیبای خود راهمیشه به همگان نشان بدهد. امشبم کلا 30 دیقه بازی کرد دو گل زد و نمره خارق العاده 8.7 گرفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.1K · <a href="https://t.me/persiana_Soccer/23951" target="_blank">📅 01:55 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23950">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g9vW6KwP5vQyuPwpUOit8LOgJ8_XBlN6N72ZiisH-IIVnwPy0zMDMmTe1Z2xCZi8gQhVesx9lTdFze7egnMR004Q9z9kVBFsgO_ZO7QZoUBl0wGcK2zWYN5Sg_1qxr8WenzBuqSh_TQu-8UVGxs9h9q0BqLvqRiwkIrpaQqlk33yE4pIXdTVs2MvMn50G8Pc2rCJK8VpnawRerT930xvbbsxWnjLyE2jt8bb7ByzUeajaJV96jtC3Qeru-bpyPYswSei57pNyRTZ6LM3XhEm1dvf2O2ff51L5Pc3Nk0eSdgz75rui5MDiPJ09EJ544p30XXfZA-v5MEyRLQ57uVYYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
باشگاه‌ گل‌گهر به مدیران استقلال اعلام کرده با دریافت20میلیاردتومان‌رضایت‌نامه پوریا شهر آبادی مهاجم جوان این تیم رو آبی‌ها صادر خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/persiana_Soccer/23950" target="_blank">📅 01:55 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23948">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/40b51e8a93.mp4?token=hzMuZFRpTc4wUTfgBJgzCd7dr1pcI_60XljzfLbNbP_JQJUi1wtE3fkl229gZUssWeUrXpekgS5-xUADwYc42B8VH1823IT-h43zmo6-FdVqV-8RRhNAp9rgWsZmQbbj9pNAqmFzNa1566EBOX6jg_sQuSa7HaNtbrQRUujTHaGyZxN8XgbbuLsNSYU07nm01wbjmipmca_-uWxUVvKGHc18LWvcqbtsrCKDwc9icIXaeE6te-haxvZ0WeQEv5OK7KDMPhdqQf6UXwCzFu6jvJAUq0DR58ywolKATzxoqF5Yj-bYcBbgKA8LI7f1UV9cUjksLk-zr7yP0vb0OsKNrk6-26Db0Bt3Y0xtbeoh8lu8l-41e_rkBi07XYBU2A0Mox3MabbHOf-b70zVg-JxUbgg_cDocm21Zuk5PSMH_jZckSU3xo9zmTFx2OnLNROjHru-fewrYLZ9PHEq3vkebbWQ4pTZwRCR2fHU4kSvFQXhinF9nsQsxdgaKLwEyEGTQkF4UOfnp6sBkHSCbP4brmBCpd0RmP0HboUc4E98qZbuWyuStY3UTcYIetyM2k1v-fk3NRSyJJDLfqDyYju8dG6Hrg14g_Wgf-pzukC2c1HxLWuAlW5XLc8KHahKtkr1xlu0K1OCeHYUw8sdGMOQULXmlwMGIiD-Z61vpNJ1jOU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/40b51e8a93.mp4?token=hzMuZFRpTc4wUTfgBJgzCd7dr1pcI_60XljzfLbNbP_JQJUi1wtE3fkl229gZUssWeUrXpekgS5-xUADwYc42B8VH1823IT-h43zmo6-FdVqV-8RRhNAp9rgWsZmQbbj9pNAqmFzNa1566EBOX6jg_sQuSa7HaNtbrQRUujTHaGyZxN8XgbbuLsNSYU07nm01wbjmipmca_-uWxUVvKGHc18LWvcqbtsrCKDwc9icIXaeE6te-haxvZ0WeQEv5OK7KDMPhdqQf6UXwCzFu6jvJAUq0DR58ywolKATzxoqF5Yj-bYcBbgKA8LI7f1UV9cUjksLk-zr7yP0vb0OsKNrk6-26Db0Bt3Y0xtbeoh8lu8l-41e_rkBi07XYBU2A0Mox3MabbHOf-b70zVg-JxUbgg_cDocm21Zuk5PSMH_jZckSU3xo9zmTFx2OnLNROjHru-fewrYLZ9PHEq3vkebbWQ4pTZwRCR2fHU4kSvFQXhinF9nsQsxdgaKLwEyEGTQkF4UOfnp6sBkHSCbP4brmBCpd0RmP0HboUc4E98qZbuWyuStY3UTcYIetyM2k1v-fk3NRSyJJDLfqDyYju8dG6Hrg14g_Wgf-pzukC2c1HxLWuAlW5XLc8KHahKtkr1xlu0K1OCeHYUw8sdGMOQULXmlwMGIiD-Z61vpNJ1jOU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
هفته دوم جام جهانی 2026؛ یه پسر کُرد سه امتیاز ارزشمند روتقدیم ژرمن‌هاکرد؛ کامبک  دیدنی شاگردان‌ناگلزمن‌درشب‌درخشش‌دنیز اونداف ستاره کُرد زبان آلمانی‌ها در فاصله تنها 20 دقیقه.
🇮🇪
ساحل عاج
1️⃣
-
2️⃣
آلمان
🇩🇪
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44K · <a href="https://t.me/persiana_Soccer/23948" target="_blank">📅 01:36 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23947">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MSlqQlFe36zxAhOoZg4lomuilBGUSeRdyqlC34CCbmP5fB1ixvZxJDIvnZEqSPzoKM8M10GOYgpcnr6zhxwolTTTfMEhTxD-uEpK1ZkYojMpy1F-8gAa9hh6x22nPt78ucrOIvgtNGTR9LUnftTM-sE_5Zyy7ODpp2liMfgMj227GLd9wA4c7oe8NWTw9RCdY48hiFhw3pMwr3WED8AoZQC8XQOq_XVie6iSqjjNqkYdHiMksjz93uxvPlWggCEftaNoYiSv6dA17tutiLNNgHUEczPUyftMJ_t_gwSXZTSalu3lu5BPOG_rd9llSCai7DW58PpjlyL585f5Vf3VkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇩🇪
گل امشب تیم آلمان به ساحل عاج: ندیم امیری بازیکن اصالتا افغان پاس‌گل داد. دنیز اونداف بازیکن اصالتا کُردگل‌زد. اونداف در دقیقه 60 به زمین اومد و8دیقه بعدش گل مساوی رو به ساحل‌عاجی‌ ها زد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.2K · <a href="https://t.me/persiana_Soccer/23947" target="_blank">📅 01:31 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23946">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s4ptpsIZj10hfCbyK1I5I01BheI69BDZ3W7c3ukUYMi79NJ7DMsZersKQLgoP4emvQT6o8rtSpZqsBsZPSYkt9hQoXejFvgvE2Xfis91-U3eWEgY-K9AfR4aPM4W_zdvLU18Rug19kVKUVYPk1jC0i8_bMMy6k0rJ-y4TRu9z3kkeB7-JhCacNvIbZVc6ij3ttgss2KPid_qHq6ntXxiRPPgkBnXIhp-ZarwHVBlhtIh29XvmPigTLu2cOv9a_yH4vGS8pTiAPT9M4qte72iJqmp3RTHs7hEN5DDgmSe7xOdpaSoVtu4HPurukWJqjo0bMw3_KHEoviQdxK6-DCaGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته دوم جام جهانی 2026؛ شماتیک ترکیب دو تیم آلمان
🆚
ساحل عاج؛ ساعت 23:30 از شبکه پرشیانا اسپورت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44K · <a href="https://t.me/persiana_Soccer/23946" target="_blank">📅 01:21 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23945">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YgQJClEHcQHtXp3VsdmrNjsMeDG-HMoxbERahm_Ku6ZJcN0-DZ2Z4g1g89LZjYwZLeu75nwUlKkyEKWrzqBi3v8Kh4YTwWz0NG7JD8S6FFoVFM7sWRECztcD9FBJyOp-auFD-kgG29_tdd0CMicFTd6oomL6n5bRTxuDxycqsd8eAQIaWXTBNn5tIKtDvRAKg8AZk2tLNMM77sQBbdBHIRpW7cFf8nN0IcpixqCdXBFpwFkqCNbs9Vc_k-PywIcnd_PGGWT0aqj7U_EFQS6ccQ5zQkFNRzhnsBXwtEP1_ECKCEl-ZQTZYwppGwm5a9jarQ8OFE53W4oXa0wqqx5I8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
👤
امیرقلعه‌نویی سرمربی‌تیم ایران به این شکل نشون داده که ساعت رولکسش رو پیدا کرده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.5K · <a href="https://t.me/persiana_Soccer/23945" target="_blank">📅 01:12 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23944">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eb124e2149.mp4?token=BcB0gHqSkXWCa2Li_233UKL67neUznx2d6xHHn9kGRKL9VrHtwS3Nwn82zhQiPTYv7q8t203sjaDHBKtH2dNsxZYzntQxKDhKtlpsLqc_eWEvPw33tIK1CKY76rqGJ9I_OqEO0ul9yLqXsQz2VxEOm7UPhLFjnbQzYoM0UBwxwPxHuQNl0IFs2GU_jWs3Tg3Ua2HfeOOc5v43L6SSEqW2F51PnPWkKhgUZxuU1eOZDzKbeFegQIGwoGbgsc4GazsBRq4Jjabqtxm0SECmKRAlvKaJgW-4-geYe-EUxU3xAd8uxmPlxsM-dkWzqMZ7b8kUJ8BfhuyZ03kj4bsHtlG4Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eb124e2149.mp4?token=BcB0gHqSkXWCa2Li_233UKL67neUznx2d6xHHn9kGRKL9VrHtwS3Nwn82zhQiPTYv7q8t203sjaDHBKtH2dNsxZYzntQxKDhKtlpsLqc_eWEvPw33tIK1CKY76rqGJ9I_OqEO0ul9yLqXsQz2VxEOm7UPhLFjnbQzYoM0UBwxwPxHuQNl0IFs2GU_jWs3Tg3Ua2HfeOOc5v43L6SSEqW2F51PnPWkKhgUZxuU1eOZDzKbeFegQIGwoGbgsc4GazsBRq4Jjabqtxm0SECmKRAlvKaJgW-4-geYe-EUxU3xAd8uxmPlxsM-dkWzqMZ7b8kUJ8BfhuyZ03kj4bsHtlG4Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
روزهای اخیر شایعه شده بود ساعت ژنرال فوتبال ایران دزیده شده که عکسای رسیدن تیم به لس‌آنجلس نشون میده‌که‌خداروشکر این خبر کذبه.ساعت‌امیرخان
🟰
خط قرمز مردم ایران
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 45.3K · <a href="https://t.me/persiana_Soccer/23944" target="_blank">📅 01:07 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23943">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Oaz7MfA4EG0QF8F0FatTLg_1-1Hk-UL4BPApcIEz4mbgZb9bA8KXG1jpzxDcGo_X8N_0VwccttpdkIidtIdSJS01i86vdOWZaZTbjtHR5ftJPI06quyPfxxH7UFGalkqD7KHu4bQjZqJ2ojQuC1FtcUny7Huyat0FegJLMpLOJC-I5qRKPkd79Kip8Stnmrhg_Aoehv9QRP_u8eKFcoqCedCczTutt2BbOO-gycH7HVMST6cMMNJQ-k63YV-8CCI87HMxf77e8k2qlMOsa15vE0o3GQmxrcWC04LmjKY3p5FqY5M2Uv43MWLbrUv3sKJWPL3Xpl2bx8FjZ8uVDLFvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته دوم جام جهانی 2026؛ شماتیک ترکیب دو تیم آلمان
🆚
ساحل عاج؛ ساعت 23:30 از شبکه پرشیانا اسپورت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.5K · <a href="https://t.me/persiana_Soccer/23943" target="_blank">📅 00:39 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23942">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dDBUwKk6mxXROLVLWnu00dwGxQ_lsrVOdXMRA2_6wVHpeaTvWUZkfzdz2hbFaYNjox8GPVMO9SdlPSa7GpSjAltOh4BhjB4iHiDUl4OhftJgVh1_IG-ZJiOPTPw_EFIEtqVX2MWnk1LloWCgRypxq-m8lC5EYmaK7V5U3k0Ct2OwuGH1wsON4fHLd7rj3Rldf5Um94BQqGbfkbiF5ERKzWmg5RwjC7AixtDM0DbePqgWWMkUGJwri_cVSSQx7NThKDlgPHfWSLXvrgkVmhwgEp5-BEKu7Y46owVZu3KlycYn17zaa2MgJpkdmqRxf0r9WPkZaKuPDrEnrJhBtg35eQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
#تکمیلی؛ مهدی‌ گودرزی ستاره‌ جوان تیم خیبر امروز از طریق نماینده اش آمادگی خود را برای پیوستن به تیم پرسپولیس در نیم فصل اعلام کرده و درصورت‌توافق دوباشگاه‌این‌انتقال انجام خواهد شد. احتمال اینکه فخریان راهی خیبر شود نیز زیاد است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46K · <a href="https://t.me/persiana_Soccer/23942" target="_blank">📅 00:25 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23941">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1a6c4ff321.mp4?token=Y8Ul5UqsAGtGc-qgX8hcVW4QIdi-V3RIE1bNz_dS60uPxlDew3fC_kQ8TFWFBSta0K_zdQIdjELVaZpbEpJS_p19puEQwE0CjljPbNWDwiNuj-bleYWCLWaNTDrRQsfIZxx7N28q31GoVPU1cotncDOSOk9iIJ-roE2e54daDwwERIq9x2VfGxmA8CAnUO2DqF_pXOEULSuE8s0JVl-EMMUD5zwHvUhxSnAwtTTOi9OiG5myHP-jw6bfpzLHj3vkbPo_iFtgcx1kWHyFf0N17fPVoy78f3bQsjQGeSIcCj17nYLEGQblSbMvZNIG2NGnsdb2eZ_H19blyO7kK8MCXw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1a6c4ff321.mp4?token=Y8Ul5UqsAGtGc-qgX8hcVW4QIdi-V3RIE1bNz_dS60uPxlDew3fC_kQ8TFWFBSta0K_zdQIdjELVaZpbEpJS_p19puEQwE0CjljPbNWDwiNuj-bleYWCLWaNTDrRQsfIZxx7N28q31GoVPU1cotncDOSOk9iIJ-roE2e54daDwwERIq9x2VfGxmA8CAnUO2DqF_pXOEULSuE8s0JVl-EMMUD5zwHvUhxSnAwtTTOi9OiG5myHP-jw6bfpzLHj3vkbPo_iFtgcx1kWHyFf0N17fPVoy78f3bQsjQGeSIcCj17nYLEGQblSbMvZNIG2NGnsdb2eZ_H19blyO7kK8MCXw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
خداداد عزیزی از دست‌کارای‌ جواد خیابانی فشار افتاده میگه حضرت عباسی این کارها چیه میکنی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.8K · <a href="https://t.me/persiana_Soccer/23941" target="_blank">📅 23:53 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23940">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cJ3jiiCBl8A_7KHgVkecBokUGbgubboVPHWjjKhqyZ7EpxvPiPUgod0RWoCFDBy9MsbFAUdO-Y8ubOnTpJENbBq3PuQOs_3Tzd_Je0Do3ABaGKMPa6Ywub6_NfycHym_8nJFjfxmNVmreC-rcKh_D4u8prD4CiHLrlR57qDLkyz1YQ97KQqdk_BMfRCJab6LMka7rNda52rQ-CUu_FgrYsxFOAGs5Pj-G6qBS-xXZGCKD7MBgs5YNhCWuSGmE63MU6AKycHEZaxhseWeB6bNlVreJRnm0ccLiUhutFH3nFdNbgXgJNEFCe9COVojNkpSEyqfHNJWpBAkErDW5NuxJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
بازیکنانی‌که در جام جهانی ۲۰۲۶ امتیاز کامل ۱۰.۰ را کسب کرده‌اند: لیونل مسی مقابل الجزایر؛ جاناتان دیوید مقابل قطر؛ کودی جاکپو مقابل سوئد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46K · <a href="https://t.me/persiana_Soccer/23940" target="_blank">📅 23:43 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23939">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HpQsRU2SWrDp4A9JyZfv_kddKtEfW5z7IZH5LN3YHzaUskxwSqmFMrrBwnOjVJtUk9O11McpoPdw01Cay6j9V7qcGS5jpTTrRuMjXhgQxRpj57IRvcfufG0DLreDqLY_T9MepKeWhHJUjQCLll4meo1_19ZqEu_Xrew7G9kp4CmpxPcOtVIL59Kb3yx4G6FsLFzHeFzP15L40Z4MI7WmJDQenMdfG3X9AOtaittl-0I3YgTnsCqG_Y0kpZ8LvboSPYq9djGy4yYVMOOHUBMtNb2poG65K2rmpQgXlf4cK3Ro69KGEMwPOnPgJjzRFH1ug1Gaj6Pb2YI2Y8wgILRZtQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته‌دوم جام‌جهانی 2026؛ پیروزی ارزشمند و پرگل لاله‌های‌نارنجی مقابل یاران گیوکرش در سوئد.
🇳🇱
هلند
5️⃣
-
1️⃣
سوئد
🇸🇪
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.8K · <a href="https://t.me/persiana_Soccer/23939" target="_blank">📅 23:28 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23938">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Wh4CxUEW5nhvKw7ZhqDllCFsm3GEZLK8xL40SpUFSMihaMsazon6-7jNMQFiOx5_wZnOyCB40JeAntOhPslAZ5eavELCT9dTd4gF73Q-akzgl7f_G_QgGFAQNkTBHK6a3faI6wZJdOsob7-PeXmBfXDjIu1a7o-8Cg8gC8ARuV_Iy3t0b-q1hYcJWnx3q0VAD5cYrqDsg5hD62nxBrRAayzktxGeYuzIKcWSkyH3ErFo9m2YNlov4vgPCA7N_0sPnsIvy630SsHZji4yFyXYjVhrTVWqL5N1USEv_9iQwvaRP9pB1Zr-m9aFlPSbtt8LnSv4GZfaftWYjAB_9wFXLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
رسانه‌های بلژیکی مدعی شدند که جرمی دوکو ستاره تیم ملی این کشور دیدار فرداشب مقابل تیم ایران در هفته دوم جام جهانی رو از دست داد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.7K · <a href="https://t.me/persiana_Soccer/23938" target="_blank">📅 23:04 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23937">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OEZ-27rJKmXbLi9nzp8ODkz858hAv7PcUgL-Y3om3HBv0D_E3Rd1N5sAf646o3OvZXSexp7PQHL1PMSX5jDN-dno5fFLUuICKsunaAxAU_ZEXsigB3eE-C80ATgMZKSFXUfg6DRsRUBA6UUXKjCi8iCFZL1KLcJ73trRvK4bUBKIT0Ez9Btnz3Y-i2fH7gZ1eUtsWuEu0CYvDfEn4lmJP7VPvJZjlG9HwYmkbePP97nF5Liy_P_rBUQQc3I_RZBYVjIOjoCKJxGfFjWOSa1flGx4COryNcMe2xx7aYw5_3SGYoAYXg19dXG1OEJ836XdKd8Ry9C-G3Rc773OPK6Krg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی؛ پیمان حدادی مدیرعامل باشگاه پرسپولیس برای انجام مذاکرات نهایی و عقد قرارداد با دراگان اسکوچیچ  راهی ترکیه شده. به احتمال 99 درصد اسکوچیچ سرمربی فصل پیش‌رو سرخ‌هاست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.7K · <a href="https://t.me/persiana_Soccer/23937" target="_blank">📅 23:00 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23936">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e541eb115f.mp4?token=E0m15dEQ4LJ4Y728fNRvrSCb32nTN4j47AvC4l2p5izFDkaj2LKZwiGidYasNBquS_IiJN1B_jY1VLH6dJsDsWBguaqipe9ilwWbOJ2WWkgXtLDQy1NpyTeZPWjxJ9470Bqt2Lh74ceZj-nePY3emiEvJA5j-9SEJ386EqT-OV5KLJKj9tWy0CZup4sAfoo94pPBDnl9bbO6mN49JSxk2_PV7cV-MpIlI6gNnqK_kUEHFzWLpISakWef8lvLNxqCE8M7dLRx4wu41Bt1WLLYpg20PCx4XjoKRO6ituxxOtA9ZgddP9xs8JhaoGpE7BjKWXZbxPynrnVwHDK8wxpMW1dcazGFdOUE7CmEQh2W4ptnlxsIjdQr5Uy_y2lAtKrhswxhFQ75UA7Wi8KLU-g7EmTCuLd-0j2e5J94JsysMprr2BjY69bd4by7JIK6NiP1RqLqitX4xq3CtkSbEab-vVIXUIY7Q-p2Bqkfk42nMhevZJVyO1go2SDcFeCJPDNGGNKVHXX07Khx99lR9DABC9Isa9ko4Rm2sOQkUvYB7DXr-BO8jdSZiD1Fyrq8LNLTrc1-rzk5lO9bk5-0LCSCwWhji6fxmTON64eD7qhCfE1JVOFzzPHTVCUi3sUyzrl-Irv5fQMpdCTZRY4OVViDXGc590qBLlpKUImHWmGEWOY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e541eb115f.mp4?token=E0m15dEQ4LJ4Y728fNRvrSCb32nTN4j47AvC4l2p5izFDkaj2LKZwiGidYasNBquS_IiJN1B_jY1VLH6dJsDsWBguaqipe9ilwWbOJ2WWkgXtLDQy1NpyTeZPWjxJ9470Bqt2Lh74ceZj-nePY3emiEvJA5j-9SEJ386EqT-OV5KLJKj9tWy0CZup4sAfoo94pPBDnl9bbO6mN49JSxk2_PV7cV-MpIlI6gNnqK_kUEHFzWLpISakWef8lvLNxqCE8M7dLRx4wu41Bt1WLLYpg20PCx4XjoKRO6ituxxOtA9ZgddP9xs8JhaoGpE7BjKWXZbxPynrnVwHDK8wxpMW1dcazGFdOUE7CmEQh2W4ptnlxsIjdQr5Uy_y2lAtKrhswxhFQ75UA7Wi8KLU-g7EmTCuLd-0j2e5J94JsysMprr2BjY69bd4by7JIK6NiP1RqLqitX4xq3CtkSbEab-vVIXUIY7Q-p2Bqkfk42nMhevZJVyO1go2SDcFeCJPDNGGNKVHXX07Khx99lR9DABC9Isa9ko4Rm2sOQkUvYB7DXr-BO8jdSZiD1Fyrq8LNLTrc1-rzk5lO9bk5-0LCSCwWhji6fxmTON64eD7qhCfE1JVOFzzPHTVCUi3sUyzrl-Irv5fQMpdCTZRY4OVViDXGc590qBLlpKUImHWmGEWOY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
صحبت های فیروز کریمی سرمربی سابق پاس و آبی‌ها درباره‌ اون‌ویدیو معروفی‌که ازش بیرون اومد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.3K · <a href="https://t.me/persiana_Soccer/23936" target="_blank">📅 23:00 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23934">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">✅
هفته‌دوم جام‌جهانی 2026؛ پیروزی ارزشمند و پرگل لاله‌های‌نارنجی مقابل یاران گیوکرش در سوئد.
🇳🇱
هلند
5️⃣
-
1️⃣
سوئد
🇸🇪
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.6K · <a href="https://t.me/persiana_Soccer/23934" target="_blank">📅 22:34 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23933">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/apsSCAJjIJ5edSwSVFyBhGozGb92OEO7JAeWKe9mOH8J_rh_haSAL79oBmB_dPjWxzqKCgd9gtz5UCW95I9xbVAslIlLXrC0vXeOMvFgTojo0VCUC9Wk2lf9knkW34fz1TDm9d_ljdrb5KGVP8cjCRNXsZ7hyX9wChKZEK4pf2r4A9k-enrjhxR45P3N13pvHA8ucFKsYT--n93qCcCwE_0ugel00VQglGx1Xf_hZRFLZdrySia16s1_MvJu7RkY2d2Fgks0B11Ab-sJAjMt7x-XmZm2hAuJy94CjrF-dVkODvNrGc6O41hf38gc4UYL6e_HVvlF4C5A5BnNbiJteQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
هفته‌دوم‌جام‌جهانی 2026؛ شماتیک ترکیب دو تیم سوئد
🆚
هلند؛ ساعت 20:30 از پرشیانا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/persiana_Soccer/23933" target="_blank">📅 22:29 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23931">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QBeE3UhsfiMz7zMgqiCyzyTlBbv4qAu1aU49gvP4eLGJIry41xZMYfHADCEF31dmCkKsUd_NyOWyAhge_IxdXofhbfEup_iJFch-yMvBkJLQcVoXL7fgbeFkOrl-9LyxJRbG3PSeznIF-8JI6qACAs-6RdPBLrgBsxp1_UuTA1rSDMHKsy_tmdQSc9QVLeBPPFWhlz3CgxYMw83hlcwLsKDda56RywET0JV_dC8nmv7Tis-crKPBgbjz5aQqxXHdd4_8gLLnFfIvF2q1laLjUKDa8TTCePmvQNjgK2otJMCibbx-jZH5Brcz-S5R7RfSKcD3jObVgPyX58PWis5bJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LL2BD4Cx8VFNvOZWqOggGSTS9dLFnT8EQCiiREDJZ9P7wrMdhEZq7V4yluHzd5ZQlFsVI6Rgo-wYC2yB9GAOwRdWdyaj-pitVaCre1U84zEOO7MxWcPMKmCFouYI780R2DQkMN9PwHq6ubVk3xw1fkN5DFXwExbdRah0NaYh7EjEVVJYphu4PKu3Ro-oYgMJ3WwY0SL2qVkp5bVV54bfT3t7rjtKFMONXK-hVhVf13qMku_2tDcDeq3uHlzmie2xHQYSW_7L9XZxPhrwmk3ukrGiTDWTcHEWRpRokIo3tM1tleWCb0GUEvXHG4Xpgc2GeXgAXeZ7XD2P9BRncyCkVw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">✅
هفته دوم جام جهانی 2026
؛ شماتیک ترکیب دو تیم آلمان
🆚
ساحل عاج؛ ساعت 23:30 از شبکه پرشیانا اسپورت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.2K · <a href="https://t.me/persiana_Soccer/23931" target="_blank">📅 22:19 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23930">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bow8972DZFIp9yQiNeEHPBDKN_xSf4nYRKupDs2c5j6-tVM4sROAaIxfj4lDU7t0Y8vs9FYh5siIcDP8Q5VoB9mwGbQfZX4OQyVSVDZCEHvs_9H2mdL9R6PkGOAwsPGRzEJhSc4tGhTVnUrPhMdLBSPg8mKWWatgFuncJ6fzGb57sFLD_nhIoz3jwP5Mb_ksZOowbIr5XNO_Pc2RaXKEmu_rgSQsWfqSeen0s36AxwMMbJsJglRq1z_051SvYDBHvUGarFP0iI3pZ_83X3xpavsfDMT5L3FmJaHu38vyvKVuviDISYERhsS2DJzAR3E3CW4WiCDJe5EOJeFh9wRMCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
جرمی دوکو ستاره بلژیک بخاطر زایمان همسرش و متولد شدن فرزندش اردوی تیم ملی بلژیک رو ترک کرده و ممکنه به بازی فرداشب با تیم ایران نرسه.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 44.5K · <a href="https://t.me/persiana_Soccer/23930" target="_blank">📅 22:11 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23929">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3537466720.mp4?token=LZpnCBNpe3sVc4PUsOIY9bgDR_ETS139pPaX5ezVy3fUcw5e_66v24T6nRbHi9WG9FUIL5NsVULK3dripu8DXe-88CGMp14BXGCyv9O4xy5ZQdX8xg_GuvNeXRtG8x3-qqbr3y7H9SkBCpiALz7sQo0Q4JXA69-bcV_csVT4uWwhHU3XxbRlDDXnOcHowNY6cHTO18SinFYf06GW3dXBq6ykEemdE1hYRMQTuq_eY1mZFpTrZtz-02GpcjFMa56dQvMeRt-G8RmGwfqHHBknunbvm59cafLM35Mi-j8XGxeaOu27-NX-jjYPdtLk3IhHkhYzUzYm6NGeW2-9l5PVrA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3537466720.mp4?token=LZpnCBNpe3sVc4PUsOIY9bgDR_ETS139pPaX5ezVy3fUcw5e_66v24T6nRbHi9WG9FUIL5NsVULK3dripu8DXe-88CGMp14BXGCyv9O4xy5ZQdX8xg_GuvNeXRtG8x3-qqbr3y7H9SkBCpiALz7sQo0Q4JXA69-bcV_csVT4uWwhHU3XxbRlDDXnOcHowNY6cHTO18SinFYf06GW3dXBq6ykEemdE1hYRMQTuq_eY1mZFpTrZtz-02GpcjFMa56dQvMeRt-G8RmGwfqHHBknunbvm59cafLM35Mi-j8XGxeaOu27-NX-jjYPdtLk3IhHkhYzUzYm6NGeW2-9l5PVrA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👤
سعید دقیقی امشب‌ مهمون‌برنامه عادل بود بنده خدا داشت‌راجب‌برادراش‌میگفت‌عادل برگشته میگه خودتم سفید مفیدی؛ عالی بود ببینید
😂
😂
😂
😂
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.4K · <a href="https://t.me/persiana_Soccer/23929" target="_blank">📅 22:08 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23928">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/463a3196cd.mp4?token=L-m6AypcHocCXTBc9xNaOc3w_mfQrPH5ZljBM6SUACLXeC44aFH0cSdC2RofIh8MnjCeQQht3rt5JfIXBVQjGhfrkHReMuwTqUoVNz4kXctBnWCXyZsY30mdpYRsZe_h3Ac-1oU2s5GUTQKJwWLsrK0J_qDCJqpdgsk1JLZL81n-iQ7RdWjPPAvbWIqESvkyWuupqkZm9RgLAQTxjp9ctS6wUTiE2XP0LO9tYTEBZ5qSIVxVp7O1kODKsprbjXyR7h9jE3pPaPtgCiTU6pbkfFPTnmioGEU7fytbB6tW10Jef5gSqu1T-6Cko_enSS0NgtdAqRg0qNueaaXughtS4g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/463a3196cd.mp4?token=L-m6AypcHocCXTBc9xNaOc3w_mfQrPH5ZljBM6SUACLXeC44aFH0cSdC2RofIh8MnjCeQQht3rt5JfIXBVQjGhfrkHReMuwTqUoVNz4kXctBnWCXyZsY30mdpYRsZe_h3Ac-1oU2s5GUTQKJwWLsrK0J_qDCJqpdgsk1JLZL81n-iQ7RdWjPPAvbWIqESvkyWuupqkZm9RgLAQTxjp9ctS6wUTiE2XP0LO9tYTEBZ5qSIVxVp7O1kODKsprbjXyR7h9jE3pPaPtgCiTU6pbkfFPTnmioGEU7fytbB6tW10Jef5gSqu1T-6Cko_enSS0NgtdAqRg0qNueaaXughtS4g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
این بخش از گفتگو دیشب عادل و اوسمار ویرا تامل برانگیزه؛ زندگی‌سخت و تلخ اوسمار در بچگی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.4K · <a href="https://t.me/persiana_Soccer/23928" target="_blank">📅 21:57 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23927">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">🇳🇴
هوادارای‌نروژ وتشویق‌وایکینگی‌شون‌کف آمریکا؛ چه عشق و حالی‌میکنن، چه تابستونی رو میگذرونن.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.4K · <a href="https://t.me/persiana_Soccer/23927" target="_blank">📅 21:48 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23926">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fExyKHzahWKdH-4AQNH_kesqe3CevRf4UxzpJKTZfm4PAnM67HvOfHegnGJ_6p6J3tcDPCpZ8U61Jm1OkjPXpSiS2uHfOJiHz4xGuvTUp7ZAKGvz6AGeEyLZqnGg1KImpUMH1jdI3WH4ybtTL_kVZ557lvM0JcXL45V2wgota9FW_fFKM4K_SKNfWT7bTmW571svRL9Li9OC0QuDSrQ943xECDA5M3ybqeluJ2OrgxYkfNvCZDzeTG90F1nGTe0Zzo_83pcd-GKENJPl1AiDvNJMnWFhNwXoDSsCgm9uVU4K6tBK4F0IIkyIrujH_el25ngz9yiGjBiBRi7hS2PdEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
طبق‌اخباردریافتی‌پرشیانا؛دقایقی‌قبل با یکی ازمسئولان‌باشگاه‌پرسپولیس ارتباط گرفتیم که ایشان اعلام‌ کرد بزودی قرارداد اوسمار ویرا با باشگاه فسخ خواهد شد و او فصل بعد درپرسپولیس نخواهد بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/persiana_Soccer/23926" target="_blank">📅 21:36 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23925">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JTcmvQeEQ7biKqatP6eFDIIAp2XxUzCm5rZzO_vzn3Zpq7H6E02H9ra0RmD4YOOR8ldpzIzbHzQU6ma_dmlwJylSPJOTAVAVgfDCg7Kbyn-RhvgscPlTH9pz12SIVNo8VrffIwbx6oc_23iJsw-S1qCf5EDRXgWUaNvQqVeeXa-idnsuvxNBbgNmQlD8w78_1oaXTgphQUgKbbd3LsuHnywQ-GyOlRAbkUjnsz6Z7i_UV0YcuADFAmeG_I3zbxqLq4r6PQ2vfPR0t1KvTpS-hThrJZubpaVtytidYPqDJK93X_WS0Ym2zwDmXKOTOw2K0m0TLpLm-6rp5uMxHoK4ZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
🇹🇷
تیم‌ملی فوتبال ترکیه با ترکیب 300 میلیون یورویی و لژیونرای مطرح بادوباخت بدون گل مقابل استرالیا و پاراگوئه از جام جهانی 2026 حذف شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.4K · <a href="https://t.me/persiana_Soccer/23925" target="_blank">📅 21:05 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23924">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">✅
محمدجواد حسین‌نژاد ستاره سابق سپاهان: من خیلی میتونستم به‌تیم‌ملی کمک کنم و خیلی ناراحتم که در جام جهانی حضور ندارم.از لیگ ایران پیشنهاد دارم و احتمالا برای فصل پیش رو برگردم ایران.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46K · <a href="https://t.me/persiana_Soccer/23924" target="_blank">📅 20:28 · 30 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
