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
<img src="https://cdn4.telesco.pe/file/oj0gncYJeNXVxeJjKB4zVltjXoH9UqkjFxeJ3jexXfXew2ov2zq2A_-QzTlaMbldI1LbFtze9n10edhZBUKGZ9khy757g095LVyXvDahHo6-XIbqyIdAa4OH0RG36oixq4bC-MnnxFd-iACZXFEzUkJHm3yRkBhJe-CqKCAea2j-CSlH3Miwn6c-Mwy1RR5m1ThbvkaaWtlKM90B4NYJClUWpCmiP4XxrtT1UWD6FRk19Lt9ldLRVXx_WHkGBF8kZDceV1Zw3684EpBOronLF_hlUMVBKymIXdJ6MmPtEdlvXgK9nBQhu4Chj4FTvEdgYPOF3a7y3WGhSNDvM9999Q.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 ArchiveTel</h1>
<p>@archivetell • 👥 9.61K عضو</p>
<a href="https://t.me/archivetell" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 🚀آرشیوتلمرجع تخصصی معرفی، آرشیو و آموزش ابزارهای متن‌باز و پروکسی‌های مدرن.🛠بررسی روش‌های پایدار برای دور زدن فیلترینگ و اینترنت ملیآموزش‌های فنی به زبان ساده!🌐https://www.youtube.com/@ArchiveTelll</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-11 00:15:32</div>
<hr>

<div class="tg-post" id="msg-6676">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LN58w0VDbQGTZKAgptbdY-PxEx1ezCkpCyRF6zikCoSFlpP1oUNiPAjhH0DgCFY1cP92CTRxTLOfwdgnbGm0NppZogPKiMSMJqWBNxG5ygtBPV7nS3Q4zcFyI0k_EqYR7t6q9a1nEnVIn3KI46fqfXoAfQ7_AbR9zC-1VcHlskJOqacDsAngIi8kr4QRo68vgsGutdaeOk1ywRttsTdddunxtJHdwakYi4vF-6moGdBqNxrxcqEwd0DCTrM45PonScgoBJMfNZbASb9MgZeNGbeUhd96K1sttcGd6jYM0s7-zb9mdtYDgv3aPC7M1wBPTJ1i79-igIZKFZ3F_lN2RA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بازگشت Fable 5
🔥
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 544 · <a href="https://t.me/ArchiveTell/6676" target="_blank">📅 23:20 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6674">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4eb8383feb.mp4?token=jnTzFrmMc-rGKVWq4U2DdkpnC6SQ6-_7uPrySOIdDA78Sm-w60SEvRNqfGa11ItjyRRnYzyB3xVsoWYBLFeVs09uReWf6RVa3DEiRc5aCleH4oTnuO8wi9QF9TCOHVvN_gzzm6bCTcg6sKRE4hv9GWkwj0ewX32JRCKJ1wxhjR2FhnaJXPe_KfEfjOqZRPpjA_OTqShoYSamKKubnHnxbZphJXUXK6c7R5T9MiaCxZK4az_757-MzI69vt0_oh0ZSyweZpRIPbuqa7Tj9nkv9RPIVzI1GbQiAomALYdYwy2qp53IslHEfEzvtuaKbZmfG8DnhLObuTiRStBSHwHTCRGYPdNzPRzxFVw64iT2iNt2UUUTH9NpXgCKP9dlPhDHs-GoZS4lEPgzpOYzqn5Fo7VZqI0nrWYZzbOmP0qnHFfefjK-OBPHsh8ldvwHRO1PnZ7c0P4g43MGOymbQl7dE4SPZX21g348jKjQkx3YLC3wD7cfRLwmcInZ-OLpyeUOzVjUc-sRy7gXhXwDw01ZQDJL1f2Wl0sA5L2prIld2-XIoTcM-Ft3KxxWDiG8aurQeDNeRMmJMNSdPQXnyflIaKuv6g4K27rbCkBqnjRFFuSOoklTBFTUDSD0ZenxpqpHXt6v-C31nMUGgP698ey8lfl2_geN2rQjRZcB9Q4p2XI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4eb8383feb.mp4?token=jnTzFrmMc-rGKVWq4U2DdkpnC6SQ6-_7uPrySOIdDA78Sm-w60SEvRNqfGa11ItjyRRnYzyB3xVsoWYBLFeVs09uReWf6RVa3DEiRc5aCleH4oTnuO8wi9QF9TCOHVvN_gzzm6bCTcg6sKRE4hv9GWkwj0ewX32JRCKJ1wxhjR2FhnaJXPe_KfEfjOqZRPpjA_OTqShoYSamKKubnHnxbZphJXUXK6c7R5T9MiaCxZK4az_757-MzI69vt0_oh0ZSyweZpRIPbuqa7Tj9nkv9RPIVzI1GbQiAomALYdYwy2qp53IslHEfEzvtuaKbZmfG8DnhLObuTiRStBSHwHTCRGYPdNzPRzxFVw64iT2iNt2UUUTH9NpXgCKP9dlPhDHs-GoZS4lEPgzpOYzqn5Fo7VZqI0nrWYZzbOmP0qnHFfefjK-OBPHsh8ldvwHRO1PnZ7c0P4g43MGOymbQl7dE4SPZX21g348jKjQkx3YLC3wD7cfRLwmcInZ-OLpyeUOzVjUc-sRy7gXhXwDw01ZQDJL1f2Wl0sA5L2prIld2-XIoTcM-Ft3KxxWDiG8aurQeDNeRMmJMNSdPQXnyflIaKuv6g4K27rbCkBqnjRFFuSOoklTBFTUDSD0ZenxpqpHXt6v-C31nMUGgP698ey8lfl2_geN2rQjRZcB9Q4p2XI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎮
واقع‌گرایی GTA 6 شگفت‌انگیز است: یک علاقه‌مند صحنه‌هایی از تریلر رسمی بازی را در دنیای واقعی بازسازی کرد.
بعضی از صحنه‌ها عملاً از نسخه‌های اصلی بازی قابل تشخیص نیستند
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.28K · <a href="https://t.me/ArchiveTell/6674" target="_blank">📅 20:18 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6673">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hxlYVurrk-TZ_3G3e7kk-gdPLwsLQL9DPJLEB9aKNAp4ZsPwO74byGax8579pvESndrxu1EnadnXImHc6S9utZ2l4Ayfi59_l9snxjhDwBBrvK9zv3eUKQRlvuonMh89pN-d27Xh2yQMnHDYKo4_5kG-E8NwN3NMtAZ3A_ToZ6nsRxFPnqxH3toUeRMw0RGEvO6ZwppzzQ5s4xILQofimGYwA9H6XYUiTIRcaNbxZJbfryxMYTe-5WAPyOvGImhwo4kK5ImTmfVpI2sG9j1AxC40vqOZdeW54V07TsVFFXiEvMXnHj67dFqGt-VOrM7fO47pJRz_7hxE26zcMl8RoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اکنون هوش مصنوعی مهارت خودآموزی (self-learning) را به دست می‌آورد — عامل یک راه‌حل پیدا شده را به خاطر می‌سپارد تا در هر جلسه جدید دوباره آن را جستجو نکند.
🧠
وقتی هوش مصنوعی با یک مسئله مواجه می‌شود، این روش را ثبت می‌کند و علامت می‌زند که دقیقاً چه چیزی کار کرده است. دفعه بعد سیستم مسیر اثبات شده را دنبال می‌کند، به جای اینکه دوباره گزینه‌های ناکارآمد را بررسی کند.
https://github.com/Kulaxyz/self-learning-skills
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.32K · <a href="https://t.me/ArchiveTell/6673" target="_blank">📅 18:54 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6672">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BOqzAqOEnFVk9nFJbLoIRspLqYfC3I4_rwWeRxWTYywPgPjisosYoGwbE-v5Kw3FHi8w4_qlTEWrgRrxYana4kryr4eXu6zAjCq0rGtXaZUrs_kCxBR4n3nAmx584UxzP38BJ8J4Xjrq64Yt9Vu2wvaeQ5eCXs9x7tdcEnz-oVVxHcpAoCM6mpk9m1oYISFmvB8ILqggzehdcLkwWkEYt3D1y9tuou2da05wI5WXsP352tGO_i_cowjZIJ2Jkk0Q7usL7O7LOFmU047kV5AwlNlI_bdFJTRA4S_10jFwZalMTT_oi43z__e-DEM0Oh4jTHgpSxH8zb2xBCB8g5zCFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">RevPDF
ویرایشگر PDF سریع، بومی و متمرکز بر حفظ حریم خصوصی به صورت آفلاین است.
این برنامه امکان ویرایش متن و تصاویر را مستقیماً در سند PDF فراهم می‌کند و همچنین عملیات‌هایی مانند ادغام، تقسیم، فشرده‌سازی و تبدیل فایل‌ها را انجام می‌دهد.
تمامی عملکردها به صورت محلی روی دستگاه اجرا می‌شوند و حریم خصوصی کامل داده‌ها را بدون نیاز به اتصال به اینترنت تضمین می‌کنند.
https://github.com/Pawandeep-prog/revpdf-release
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.17K · <a href="https://t.me/ArchiveTell/6672" target="_blank">📅 18:44 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6671">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fc1d8b6548.mp4?token=IeQPGOysnxBPmLyhM2QYd7cFWayOuyyj_678ZwXm7oRXPZT2wwQsPFwShUpCsy1Duga7hHNgThM1uJMl491DqNAe52RtOSRnZ3EN584TqfpmDNXTc_wp0TLMSECNCG3XZmoyHRcp2lXwUDEzMkfqlTPyKKypwBPaZF2vM9aWBaK4C6_FxdXcu5GOec4ddfGKzurXeU8jUQYuMk9xEoNMUx4W1js87LfeNiWBWn9XmISbd3EBrfFiWRtu6ZkKyEzwVtfSw04YoIibBl9MhOiWpk8ZO4EyD3mF1ydkg7m8dnPTVsb0OPPrWhT0S6R_9np7xpLpMmJKMqf7dt_QlKMFOau9i1xQJziW4KWz_YCknM6EN5zM1CgZfXbuPS9BQ3yokRVoH_sURhD-CC5CZ992t8zS7vNm32iC7rNDmiWBo2mPNG96Aowrs7oZVPHkVyUascQV1j9DPlmRMfFXX-yP9SxAumUkToQmv3tDZpDgryOLY1SxdAR1lYM6XcnUyk3Wg4pDL25tju-f3ckFDede58VsmwEPSMgZGaZsa9Ye1CT-GaVJjmnE52wrthCipKUM_reeQuLSw8cISCmnPlKz1NTBQX1bS2Wz7Aj8VD5rp8ZuTt62TlxM__MMz2j1uFjxL3t3Uq_ivmgxa5EpDxm7I57YWY4x-1fjUzXygY-XzHg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fc1d8b6548.mp4?token=IeQPGOysnxBPmLyhM2QYd7cFWayOuyyj_678ZwXm7oRXPZT2wwQsPFwShUpCsy1Duga7hHNgThM1uJMl491DqNAe52RtOSRnZ3EN584TqfpmDNXTc_wp0TLMSECNCG3XZmoyHRcp2lXwUDEzMkfqlTPyKKypwBPaZF2vM9aWBaK4C6_FxdXcu5GOec4ddfGKzurXeU8jUQYuMk9xEoNMUx4W1js87LfeNiWBWn9XmISbd3EBrfFiWRtu6ZkKyEzwVtfSw04YoIibBl9MhOiWpk8ZO4EyD3mF1ydkg7m8dnPTVsb0OPPrWhT0S6R_9np7xpLpMmJKMqf7dt_QlKMFOau9i1xQJziW4KWz_YCknM6EN5zM1CgZfXbuPS9BQ3yokRVoH_sURhD-CC5CZ992t8zS7vNm32iC7rNDmiWBo2mPNG96Aowrs7oZVPHkVyUascQV1j9DPlmRMfFXX-yP9SxAumUkToQmv3tDZpDgryOLY1SxdAR1lYM6XcnUyk3Wg4pDL25tju-f3ckFDede58VsmwEPSMgZGaZsa9Ye1CT-GaVJjmnE52wrthCipKUM_reeQuLSw8cISCmnPlKz1NTBQX1bS2Wz7Aj8VD5rp8ZuTt62TlxM__MMz2j1uFjxL3t3Uq_ivmgxa5EpDxm7I57YWY4x-1fjUzXygY-XzHg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚡️
«اودیسه» نولان - تریلر نهایی. این فیلم یکی از بزرگترین آثار چند سال اخیر خواهد بود.
با بازی ستارگان: مت دیمون، تام هالند، ان هتاوی، رابرت پتینسون، لوپیتا نیونگو، زندایا و شارلیز ترون.
اکران: 17 جولای.
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.13K · <a href="https://t.me/ArchiveTell/6671" target="_blank">📅 18:16 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6670">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nuKII0iZSkSlNf1S-4cVDbr5z9rsR2bxvfziaxG3SIMn_uaWxfvIXSW6ONu4wQGafwLcnBKBXgNemaQ0K2ZNsXxJSVeS_E66R23c2LelvikGDZ6FlwQjID2Y4Wbricw-5TsPH67-2c8d2xoJlzgLEHJqhM6hOUBaDMMrlqaSgBEIcG7_Ealb5zqSbGOtUP0MEDdJFZn7ByyZHnmrEUCa0GMciIA1J3RyPly_aSD9j0PTD4d1jQdZuQeQzAfzfc_XoVSFByWT0DScHf9kUpfP6EEGzJvb6wR6ffSSrOAvS3Fi27fY5LKhxE9plwRUE7_hAr3HvcU5i7xtqpjj7FQGZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در عرض چند ثانیه هر نوع کپچا را در سایت‌ها و منابع دیگر رد می‌کنیم
• به سرعت بیش از ۳۰ نوع کپچا را حل می‌کند، رفتار انسان را تقلید می‌کند تا هر محدودیتی را دور بزند.
• با چند کلیک روی کامپیوتر نصب می‌شود، نیازی به ثبت‌نام و نصب نرم‌افزار اضافی نیست.
• فوری و به صورت محلی کار می‌کند.
https://github.com/clawdbrunner/captcha-solver
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.08K · <a href="https://t.me/ArchiveTell/6670" target="_blank">📅 18:08 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6669">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/268d269709.mp4?token=hmK6HJq6XSoXHB8AdZKO8cJ3jOEydJBOxsOcC2clV67fVZ3HIQlcnXKl3Y8DfcI_L155ViBvvKnI5Av4TQ_tKSi8ZioJcJ9Hv5T4OaCBSsa6Bze3SboJNBMkCZLZ1Z4vKf23EIavpGKTZxbdbjhP-lwpBrrH9d1VFOhFI-PaVOJv30WWmnOXWteO2cBXqNVoFAYEf7qN8zY83y692Dtb_gt5Jb63tNiLrE7nrs8B1ufTg9GwXdh-BVvSBP__sGMI8jXDHscvcji1GufSxChke8gh9FxmIdw-IyCsQL35-9MsZy-2C7Ycln_mTqUsFjGXn5A48SVzFzWj7oD66BSeMg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/268d269709.mp4?token=hmK6HJq6XSoXHB8AdZKO8cJ3jOEydJBOxsOcC2clV67fVZ3HIQlcnXKl3Y8DfcI_L155ViBvvKnI5Av4TQ_tKSi8ZioJcJ9Hv5T4OaCBSsa6Bze3SboJNBMkCZLZ1Z4vKf23EIavpGKTZxbdbjhP-lwpBrrH9d1VFOhFI-PaVOJv30WWmnOXWteO2cBXqNVoFAYEf7qN8zY83y692Dtb_gt5Jb63tNiLrE7nrs8B1ufTg9GwXdh-BVvSBP__sGMI8jXDHscvcji1GufSxChke8gh9FxmIdw-IyCsQL35-9MsZy-2C7Ycln_mTqUsFjGXn5A48SVzFzWj7oD66BSeMg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
شبکه عصبی Gamma به ChatGPT اضافه شد — حالا می‌توانید پرزنتیشن‌های زیبا را مستقیماً در چت بسازید.
ابزار هوش مصنوعی محبوبی که صدها هزار نفر در سراسر جهان از آن استفاده می‌کنند، در ChatGPT ادغام شده است. حالا کافی است ایده خود را توصیف کنید یا متن را وارد کنید، شبکه عصبی آن را به یک پرزنتیشن آماده با اسلایدهای طراحی شده تبدیل می‌کند.
می‌توانید تا ۱۰ اسلاید را به صورت رایگان تولید کنید.
🔗
لینک
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.04K · <a href="https://t.me/ArchiveTell/6669" target="_blank">📅 17:58 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6667">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pvUVfC_A6PYsV21JHqBKNUA2Q1OdMK-ELsQFFCsBc8cYs5imXWOuCfvfLLFe82UHByB-ZX_AyAQLx40HWRKAT3MUpQJy3PDWWitCwExxyRzArxqVyddCyEN029zaUeMei-PCzymhYP9sohDDVXrprTRt0ir7EPdtC7ewilbyPwGRZkfv-c8xB2nkrUt7_DGToVCyCSbJFeL_SwJBNLxpOn8Q5Rl3iUGGR_0TcHVtAKxk_jrV08IwvrPcNQa8DIP-ZWHocUZWf7T2j7DOlMVe4ylwUKmabQSCC1N5VVj6afGmuns3cwHUhRkS9b7WHei6GNHHHrmKbylAg9c4u33l8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚡️
دیسک‌های بازی پلی‌استیشن سال ۲۰۲۸ ناپدید خواهند شد
بازی‌های جدید فقط به صورت دیجیتال منتشر خواهند شد. همچنین سونی فروشگاه PS Store برای PS3 و PS Vita را خواهد بست.
یک عصر به پایان رسید.
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.12K · <a href="https://t.me/ArchiveTell/6667" target="_blank">📅 17:46 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6665">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">🚀
معرفی Superfile؛ فایل منیجر مدرن و فوق‌سریع برای محیط ترمینال!
📁
✨
اگر از طرفداران محیط خط فرمان (ترمینال) هستید و به یک مدیر فایل قدرتمند، زیبا و سریع نیاز دارید، ابزار
Superfile
دقیقاً برای شما ساخته شده است. این ابزار با رابط کاربری بصری (Intuitive) و کنترل آسان از طریق کلیدهای میانبر، تجربه مدیریت فایل‌ها در ترمینال را به سطح کاملاً جدیدی می‌برد.
🔥
ویژگی‌ها و امکانات برجسته این ابزار:
1️⃣
پشتیبانی کراس‌پلتفرم (Cross-platform):
اجرای بی‌نقص روی تمامی سیستم‌عامل‌های دسکتاپ از جمله لینوکس، ویندوز و macOS.
2️⃣
شخصی‌سازی بی‌نهایت:
دارای سیستم پیشرفته برای نصب پلاگین‌ها و تم‌های متنوع جهت تغییر ظاهر و افزودن قابلیت‌های جدید به محیط برنامه.
3️⃣
نصب سریع و بی‌دردسر:
قابلیت نصب تنها با یک دستور ساده از طریق پکیج‌منیجرهای معروف مانند curl، winget، scoop یا Homebrew.
4️⃣
محبوبیت و پایداری بالا:
توسعه‌یافته با زبان قدرتمند
Go
که توانسته بیش از ۱۷.۷ هزار ستاره (Star) در گیت‌هاب به دست آورد و نشان‌دهنده استقبال بی‌نظیر توسعه‌دهندگان از آن است.
https://github.com/yorukot/superfile</div>
<div class="tg-footer">👁️ 1.19K · <a href="https://t.me/ArchiveTell/6665" target="_blank">📅 16:31 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6664">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tiPbgHjJgjmPXI6LT0taNH9FBdMrcCS9ODYnOEKVr2IB7yJXWzuvONO8WF3MnjkvKFlbeXAUUO8JZHJfZD-ABRl3qwdEI7_KATKAYjT0_T4JEzNQyoCVqKfX7ZZJYEwB7hoxt3pgwG1phaRel66ud3PlRdKktM10xTrPwp-zd1y2hggZ8ZWmSBlS4qIOlDDMm75Rxr3Q3FbgbMIMt3iTclvXBJVQYwVnwn9oPZAaFiObu1KFipZLTQVRGRmUYyunR4c53qJLSjLIhuwv7qMB8PhhqPe9rzhomRIxDIUFOMqYjYFZUE3i1OvvMsAPognY5EEUoi7kEJnEFq_YEyDHAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پسر اروین یالوم خودکشی کرده ظاهرا
😐
اروین یالوم نویسنده و تئوریسین روان درمانی اگزیستانسیال</div>
<div class="tg-footer">👁️ 1.4K · <a href="https://t.me/ArchiveTell/6664" target="_blank">📅 15:03 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6663">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h5c-4hZg5AbTU0Rw4pUccKPcuIddOjkrNNkXFfMvhjeist15gcxoGDdyNh9fqttdjoM0EpXRbPdFsXTZtasNcm19jS8bZMn-tsmPLnwZ2dhwAq4oTSIhNcjs3AQDvBnRea59Y506heI0UNUQ1Ei152Ox6dGyyExRm0V-JuFzZj0WDtFC-sSW1ZE5AG-8PWKug9LaLA8f1H87ooFRX_GREXRX9I0_G4xGI31rScI87dwmOD40tUKsr5EMnoQGC6NeuTnknxNxwO51JFfS6x-uuFlrLkXZy5Ek4fidwd6Mb9MHs_BlT8pBFS8SU4NVLhh4Y4Sz1q_-Nimt5dvB2krHLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کلودفلر سرویسی راه‌اندازی کرده است که پروژه را از نظر سئو، جستجوی هوش مصنوعی، احراز هویت ربات وب، MCP و پارامترهای دیگر بررسی می‌کند.
سپس به سایت امتیازی از ۰ تا ۱۰۰ داده می‌شود و یک پرامپت با اصلاحات ارائه می‌شود که می‌توان آن را به شبکه عصبی داد و سایت را بهبود داد تا امتیاز خود را افزایش دهد.
https://isitagentready.com/
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.53K · <a href="https://t.me/ArchiveTell/6663" target="_blank">📅 13:27 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6662">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OK_sjPbLDmA4V-0bnlKBZxu855gxQHqAu8qBISbgU_hD1XlMfgnwpiTk9O4Y9g3_EYhd4uDGcAxf5HnhfqueA2t-2eKjWPrd8sDEgdxo3NZmiI_DtyAgMU6OLGCjvuckN4AJz8L6ishC50UjMpB6yYzLhXAp12ZsodLK1etiJL8bHlHAspiPrpPcEPSu-gl-T4PvcTCuPi75u5HXJ9BpC-q4FSkGr74Xob4vtdthTwNeGHbvTVprwAMuhokscl94u4Eq5MSo7MlnJ20B-zUKr7Z_l1BRUl7F_zTGs8-6zS07g3w_Fr3_69ognOBcDRJoFMUfp5wZ-QSAaGQfs_6tew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">منبع مفید برای توسعه‌دهندگان: در گیت‌هاب یک فهرست عظیم از APIهای رایگان برای همه موارد زندگی جمع‌آوری شده است.
🌐
بیش از ۵۰ دسته‌بندی موجود است: از آب و هوا، ارزهای دیجیتال و مالی گرفته تا یادگیری ماشین، نقشه‌ها، موسیقی، اخبار، انیمه و میم‌های بامزه با حیوانات.
🐱
💻
https://github.com/public-apis/public-apis
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.43K · <a href="https://t.me/ArchiveTell/6662" target="_blank">📅 13:25 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6658">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QYTO4BDIEoxM3kll3W3r8pSqF0YZE--zZ9hrw-uvvbh-57N0b2MAP40JcDGpywRAfZ40p1Dna6yHw6NzJhJdtedbSi_0iG9KEohtM4bQln0dkmM0peQIm7UVfwqnLllAhBVDguV0msi1Mq6RHY0lLfE0ncgbwa_rduOlHxL61Tedk5MD_-kE2CsosrpkL6d-XOBrk0njDjkfDiQ2ogIBH5lGGntMOVJ5jWVx-_0m63p2QgZqrLZBlPG3mwnPBp5-BUVdSH9LpNav-aPMtzsvBEL6E5BOz1NciJNbb6qLj3h5LNMhIuu1kBQBL73QB547MYRWvCFsZrdY--bzDEwEtw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/W6RZlm2qBFzNSgTHhsUmZTYiB2wvber-TaAhx4AyJ8IcVJ4No6L63_nv7toUT1yNqYf1qSgEhFMyXzojvNiITr4CkeGrp4Tfe4WGIopSuLRisE86fBrt_LPg7HtJCwCSeY0SxHG5Tgrci8Lq_4Imy2r03kt-UUP4OLBOFZH2n35eDFWiSK_19SByys4ufG9PmzSHLKJeZeIJdOs_uzeyTiSbjxnq9QeaieUIJHZ2WvYPYd2y8Sq5zu0x7z2CH5F-ICJSBJd6W07Gsvf6eJcs9KfDyQdaCpUDcGgi4U5uTL0dv68ynu1KMFBvB1Me3eLvK4Nr21OlEzSLdo59EMcjDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/caz3IggL-8AsuVYMuVw_b8pCCAmrXNBetS-KsckbojWV1_I8ncgpVORRcXVQwOV4byEEMeZcMRe2YpJtQrUjLHrA3ILbEdW_Uee1pJgish5kEwiF4btL_2pduYKVSiuN12QdiHKO9qNtr-DTBzHm52WqVNwZfmB3XvuDARSZpqUgqnFw1gXKqdbHqCWe5ym3Kjq_mMGDl658Kb7w4dDwRt8zxLusgM6UK8ZH35N2qZSC3O4ZY2B0PEIXca545-AJ9nDxjRGmjKK5W8wTluUezpyxbH1jTNbm3ALw_YVb_VLKOVdRdOocaVIs2mod30MRx6OlEiDWeOXlzmy5tzJ10A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Ba28W7k0Kd55kaieyu5p2ORP6U1pqpC5emORRFs3SoCAB6lIBG96B5TUEtIPTAD65oYAt7NoSFyvLxBaJHECiNB2xeeNyVKnkuHmrrQa7EMG3qJa3ihUKbQL8-jQKrzvFEAE0p675nnhmIgIPS1uTtOobHfjdeZMKS2MWBANY3RYBFiK_3qYgMIlDDybdOjHmE0CsPUD5VUNoJdsxo1ojWwwiDsGjPBsXqFqaIymNHA0Tthvyo2WiJKwte8sl6i1KbMftq9k3AcHhCX4tczuO-1IQF1Hgxd0eSSHZKpRcKSjdXQS46DcWs1aGMMffKBQvgxBz-BDBCbno20jjk9nsQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">PlayTorrio
مگاتورنتی که همه چیز را دانلود می‌کند:  بازی‌ها، موسیقی، فیلم‌ها، کتاب‌ها و هر نوع فایل.
https://playtorrio.pages.dev/
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.57K · <a href="https://t.me/ArchiveTell/6658" target="_blank">📅 09:35 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6657">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HdJhQ6FtIfvB8AcRc1Tgr0rtMjW6pQtkgpI6xzuIjwnaZMi5fGEv_CeX2LESmElaXFXPHf1VS3joxX5G4yFvmzxembh8QPL_wEyRx9KK6o3yV4E0NAYZONoE-8S5rc749OpRCZPpku4rlbOSZs1jbMQaLKTRVJ79ao1pNu99_SO70zcSMWSeCX5ESYQL5g0vDsWMKCHYgIXMAbFuZcHZES8w4Y3GbHwUkKVVVPGAoZT2-FGG6tn6KpUYrZWGZBjF59xCb1-eepcQMSug2OKq4LnxvA1uNUTgMc-97a4p55e2qNZ2him5hiHAYnSsmkSXijtj-7h7K0f8wwYtvRsYbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚡️
کلود Mythos و Fable 5 برگشته‌اند! دولت ایالات متحده این دو مدل‌ رو از حالت مسدود خارج کرده است.
امروز Fable 5 برای همه کاربران در دسترس قرار می‌گیرد و تا ۷ جولای می‌توانید تا ۵۰٪ از محدودیت‌های هفتگی خود را روی این مدل استفاده کنید.
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.51K · <a href="https://t.me/ArchiveTell/6657" target="_blank">📅 09:10 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6656">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LkUk6-0nsQVFKk2sC_XiWh0j__Lv_LyY1rWwbjc3A3WDeobnXC0hJilVLWoZISmSHSJRakPk2SiHyfOEmrPvk8hSyo7imufbCt94FdiOl4lgdIOVk8abqZz1hJC3P97bPtmRHYHuD1RzC0D-Fr0gzEAvDMz745PcYTSmfPVT0F6Xhs-jhdhu76rAmLPGq_RFq-BKw6SUDMro-yBV7_BRx_LZZEEnOMBaA503Ke56uxysjKZ40bHZx4EZtAlgQTah0f4VumWmUdiTZcK_vd3-suIaa387UKbrou5sPvEXedXC5avXoCsTEnLy2MkiSpeDg2PcRLHrNV-DGwig9KKA9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کلود اوپوس بدون سانسور منتشر شد!
توسعه‌دهندگان Qwen 3.5 را با داده‌ها و استدلال‌های Opus 4.6 آموزش دادند و یک نابغه شرور واقعی ساختند.
• محدودیت سوالات فقط تخیل شماست.
• می‌توانید هر چیزی، حتی ترسناک‌ترین‌ها را درخواست کنید، اما مسئولیت آن با خودتان است!
• به صورت محلی اجرا می‌شود و بسیار سبک است.
https://huggingface.co/DavidAU/Qwen3.5-9B-Claude-4.6-HighIQ-THINKING-HERETIC-UNCENSORED
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.42K · <a href="https://t.me/ArchiveTell/6656" target="_blank">📅 08:45 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6655">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">ArchiveTel
pinned «
🔥
آموزش ساخت سیستم ایمیل موقت نامحدود و اختصاصی (روی کلودفلر - بدون نیاز به سرور)
🔥
رفقا سلام! تا حالا شده بخواید تو سایت‌های مختلف ثبت‌نام کنید ولی نخواید ایمیل اصلی‌تون پر از اسپم بشه؟ سایت‌های ایمیل موقت (مثل Temp-Mail) هم که دیگه تو اکثر سرویس‌ها بلاک…
»</div>
<div class="tg-footer"><a href="https://t.me/ArchiveTell/6655" target="_blank">📅 08:15 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6654">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">درود دوستان AssA هستم
بابت خرابی ربات
@REN_WZA_BOT
دیروز معذرت می‌خوام
حقیقتا به خاطر شرایط نتونستم سرور تهیه کنم و ربات روی کلودفلر ران شده
فکرش رو نمی‌کردم که قراره انقدر استقبال بشه که سقفش به نصف روز نکشیده پر شه
😄
خبر خوب اینه که یه ربات بک اپ گذاشتم برای وقتی که سقف اولی پر شد بتونید کار هاتون رو راحت روی ربات دوم انجام بدین
جای نگرانی هم نیست تمام اطلاعات دیپلوی ها و کاربر ها انتقال داده میشن پس عملا هیچ فرقی برای شما نداره
مورد دیگه این هستش که خیلی از دوستان بدون اینکه پنل قبلی شون از کار افتاده باشه یا مشکلی پیش اومده باشه ده تا ده تا میسازن که واقعا عجیبه
🤔
خلاصه که دیگه قرار نیست به همچین مشکلی بر بخورید
و نکته سوم هم اینکه ربات دوم کمی با عجله ساخته شد اما از تست های خودم سالم بیرون اومد
اگر باگی یا مشکلی دیدین با تگ کردن آیدی ام توی چت بهم بگین
@Assa_7788
(بابت مشغله های کاری و پی وی شلوغ به احتمال زیاد پاسخ ندم بهتون پس ممنون میشم پیامتون رو با تگ کردن آیدی ام توی گروه بنویسین)
و عذر بنده رو برای طولانی شدن پیام بپذیرید
🌚
❤️</div>
<div class="tg-footer">👁️ 1.52K · <a href="https://t.me/ArchiveTell/6654" target="_blank">📅 05:49 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6653">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">الیوم اکملت لکم دینکم
🚶‍♂️‍➡️
😂
(حس تکمیل پروژه خوبه)</div>
<div class="tg-footer">👁️ 1.57K · <a href="https://t.me/ArchiveTell/6653" target="_blank">📅 23:24 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6652">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-footer">👁️ 1.62K · <a href="https://t.me/ArchiveTell/6652" target="_blank">📅 23:23 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6651">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e5Mj08CGCrFhp8_nJ_QQwM5hRddyA7QjaBNFxJnGdJzC8CokL7uLyJlHmRclYamPhPul6C7QmzLNHrGx-0-BSMnQVtPsjYPzd6deKo-X7xfFDwEhx_q2ynkcPmRLFHy_unVpTKWybut2O0aQI0ZnDWJhsyFC0Z2btRwX8S2lbBc6_gZ2CHG15LqQ5P8ZaCotVTpsVKMha7HsIGxNuEXn6mk7kVXuHwbP4z97NVlnzyTQoeeCMqPm72-WstB04lR69UMG1WcCMp7CmgfQlBxB7VcWu7wJr9IIJ9ZgVxHga1ND_kWsF6MpQqIThLtmkC1qxx3u0ucmUNLGPe0P70F9fQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">https://www.youtube.com/watch?v=JnpHyg-Vc40</div>
<div class="tg-footer">👁️ 1.62K · <a href="https://t.me/ArchiveTell/6651" target="_blank">📅 23:23 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6650">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">CFMail@ArchiveTell.zip</div>
  <div class="tg-doc-extra">471.7 KB</div>
</div>
<a href="https://t.me/ArchiveTell/6650" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔥
آموزش ساخت سیستم ایمیل موقت نامحدود و اختصاصی (روی کلودفلر - بدون نیاز به سرور)
🔥
رفقا سلام! تا حالا شده بخواید تو سایت‌های مختلف ثبت‌نام کنید ولی نخواید ایمیل اصلی‌تون پر از اسپم بشه؟ سایت‌های ایمیل موقت (مثل Temp-Mail) هم که دیگه تو اکثر سرویس‌ها بلاک…</div>
<div class="tg-footer">👁️ 1.53K · <a href="https://t.me/ArchiveTell/6650" target="_blank">📅 23:22 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6649">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">🔥
آموزش ساخت سیستم ایمیل موقت نامحدود و اختصاصی (روی کلودفلر - بدون نیاز به سرور)
🔥
رفقا سلام! تا حالا شده بخواید تو سایت‌های مختلف ثبت‌نام کنید ولی نخواید ایمیل اصلی‌تون پر از اسپم بشه؟ سایت‌های ایمیل موقت (مثل Temp-Mail) هم که دیگه تو اکثر سرویس‌ها بلاک…</div>
<div class="tg-footer">👁️ 1.51K · <a href="https://t.me/ArchiveTell/6649" target="_blank">📅 23:20 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6648">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">🔥
آموزش ساخت سیستم ایمیل موقت نامحدود و اختصاصی (روی کلودفلر - بدون نیاز به سرور)
🔥
رفقا سلام!
تا حالا شده بخواید تو سایت‌های مختلف ثبت‌نام کنید ولی نخواید ایمیل اصلی‌تون پر از اسپم بشه؟ سایت‌های ایمیل موقت (مثل Temp-Mail) هم که دیگه تو اکثر سرویس‌ها بلاک شدن.
تو این آموزش یک ترفند فوق‌العاده رو پیاده کردیم: ساخت یک سرویس ایمیل موقت اختصاصی روی دامنه شخصی خودتون با استفاده از زیرساخت رایگان کلودفلر!
🚀
این سیستم کاملاً ضدِ بلاک هست و می‌تونید تا بی‌نهایت آدرس ایمیل فیک بسازید و همون لحظه پیام‌هاش رو دریافت کنید.
🎥
آموزش ویدیویی و قدم‌به‌قدم (از صفر تا صد) رو تو یوتیوب آپلود کردم. حتماً ببینید:
🔗
[لینک ویدیوی یوتیوب ]
👇
خلاصه مراحل و کدهای مورد نیاز برای رفقایی که ویدیو رو دیدن:
۱. مخزن اصلی گیت‌هاب (برای فورک کردن فرانت‌اند)
۲. ساخت دیتابیس (D1) و کش (KV):
یک دیتابیس به اسم
mail_db
و یک فضای KV به اسم
mail_kv
تو کلودفلر بسازید. فایل
schema.sql
(موجود در مخزن بالا) رو تو تب Console دیتابیس اجرا کنید.
۳. متغیرهای طلایی (Environment Variables):
موقع ساخت Worker برای بک‌اند، این متغیرها رو دقیقاً با همین نوع و مقادیر اضافه کنید (راحت کپی کنید):
DOMAINS
(نوع JSON)
👈
["yourdomain.com"]
DEFAULT_DOMAINS
(نوع JSON)
👈
[]
DISABLE_ANONYMOUS_USER_CREATE_EMAIL
(نوع Text)
👈
true
JWT_SECRET
(نوع Text)
👈
یک_رمز_طولانی_و_رندوم_انگلیسی
ADMIN_PASSWORDS
(نوع JSON)
👈
["رمز_ورود_شما"]
ENABLE_USER_CREATE_EMAIL
(نوع Text)
👈
true
USER_ROLES
(نوع JSON)
👈
کد زیر رو کپی کنید:
JSON
[
{
"domains": ["yourdomain.com"],
"prefix": "",
"role": "vip"
},
{
"domains": ["yourdomain.com"],
"prefix": "",
"role": "admin"
}
]
🚀
مرحله ۵: آپلود کد بک‌اند و هدایت ایمیل‌ها
۱. در منوی
Runtime
ورکر، تو بخش Compatibility flags، کلمه
nodejs_compat
رو اضافه کنید.
۲. روی
Edit code
کلیک کنید و کدهای فایل
worker.js
پروژه رو کپی و پیست کنید. Deploy رو بزنید.
۳. تو تب
Triggers
، یه ساب‌دامین اختصاصی (Custom Domain) برای بک‌اند اضافه کنید (مثلاً
apimail.yourdomain.com
).
۴. حالا به بخش
Email Routing > Routing rules
تو دامنه‌تون برگردید. اون پایین قسمت
Catch-all address
رو ویرایش کنید، Action رو روی
Send to a Worker
بذارید و ورکر پروژه‌تون رو انتخاب کنید.
6. اتصال ظاهر سایت (فرانت‌اند):
مخزن پروژه را در گیت‌هاب شخصی خود
Fork
کنید.
در کلودفلر به
Workers & Pages > Create > Pages > Connect to Git
بروید و مخزن خود را متصل کنید.
تنظیمات Build (دقیقاً این مقادیر را وارد کنید):
Framework preset:
None
Build command:
npm run build:pages
Build output directory:
dist
Root directory:
frontend
تنظیمات محیطی:
یک Environment Variable به نام
VITE_API_BASE
بسازید و آدرس ورکری که در مرحله اول ساختید را در آن قرار دهید (بدون اسلش آخر).
تنظیم SPA:
در مسیر
Settings > General
، مقدار
Not Found behavior
را روی
single-page-application
تنظیم کنید.
روی
Save and Deploy
کلیک کنید.
ارادت، Bachedev
✌️
🆔
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.38K · <a href="https://t.me/ArchiveTell/6648" target="_blank">📅 23:20 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6647">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">سورپرایز امشب
اختصاصی
🗿
❤️
از یوتیوب
تقدیم به بچه های گل کانال</div>
<div class="tg-footer">👁️ 1.32K · <a href="https://t.me/ArchiveTell/6647" target="_blank">📅 22:57 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6646">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FyFPkAGpfZPymuP25SMXGTenVPTIB6ZS8ykzO7CPm-kApkNFascBG_LNZMxVQvVfbmRbYfHgDTS422tuDSXTNw3DSzrT-19bWjdS2bD6bPzxKTrQvQu48NwP9ZT6lvw2efpAw82vBmKfY6Jqpt4oGL_P2bdQ-mKzqv3Bx-zzE1Guft4YJwVHwqjLP8jYG6w9z7WKee0wO7_7ValTKcGgIjL-ivQFVVVJ7bGMZ8VEVLQ-G4TH2NrduC-DXIvcE7BSRMXAdYTgv0kXYG9aOk-CBQ9n9_Y0nMS_QoBbpNoHKew0DS9gJLtd8XUH5YP33W1Eyz6sjPApOa00Wx4xxfwbfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Claude Sonnet 5
منتشر شد!
مدل قدرتمندی برای کارهای روزمره اکنون برای تمام کاربران، حتی کاربران رایگان، در دسترس است.
• از نظر عملکرد بسیار به مدل Opus 4.8 نزدیک شده است.
• به مناسبت انتشار، Anthropic همچنین تمام محدودیت‌های مدل‌ها را حذف کرده است.
https://www.anthropic.com/claude/sonnet
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.67K · <a href="https://t.me/ArchiveTell/6646" target="_blank">📅 22:02 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6642">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qu9L1wQHIxQCC8paG4ye9vOenY_P7qVAhmFgzZvayxJ-YZg2kUNxwgDkReDbo8ciz3VkcDt5eXml9msaiCVKpFTrNkFd3Mw7h6nKd9LXC9ix7Fvd2KZKrQUnqktkIVduS826jQ7ovMhqKYYaONcAYwS73DO3m5elbsZQRBU82HWXZGZ1B475n3YNA2pKfyBiQeQJ-BO_s1KJzLFaNpY3718oRsmu5xB95D45BsxgGgn6R1UyAAnLdtOZ9stuw7k3M0q7Q89vEHjRv6TSxIfahwAWXsh9OvnQPMuON2f2d8EzvdVne0Y5Srue6KHJn5GwvKzSEDihr8jATRrvXN5-AQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pCAMs9MlRXiybUe5LTgOy_xM2_5fJKRRpVNGBx-lMV_x1SipHYPFW8JN-Yk4EBkPltJ8CQsMTAQGV0kb0Ez16_F7cthvZKO0FaHz4rA58jA4uHNNVVEn-Ivbv2bkT5bYHoDhBJixBOgXtOfAXeiJsbXcHnNH3dBRA81V2wrrFRQnXe3kwj0icCTsLHEo3hSpUdyOiMmrdAm11I7yuvXDsCHcb_JVqCyjRi-BnFIxeCj42E9uuFnICRzEa9Ig2x_pdxSM4X3v0GCSJ1OavgK5WcfcrhyFSFLyUFYdKF6UVTEZaUtANqxgVar0yL6QYi_NeWyzascNiyX_v7f0vf9jqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZDQKl4yZHZMpjH5_NR9wv7cDkXZm_rws7fMwyW48Pl970EXalOeV_VVzhG8fN6pzI9nyZNw0h4Wcvq4ZISwddMMrkm9Bwa5jH7SeaRfmX0g2Rljz03XTVXMUSJp5Bm159bPpR2A1jNpw-QgERuDUA114rlSbqHMizXwnAOpdyg_EvSRrGAMGSWiHIh1LhhBcrBNua8Xc7QoOuNV9kjsRvtC-8C0gnmG92YG_fGtWR50ZNpJqxF9KQXgMj29mYQ7c4XYwqp4lvfokQrRTOPN3JFdB91H594vLEtp6YNdiZX3-U_PQrF3Ba1bIFVVGaK61fA7vzYrIAy3iY7FO6k324Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9de073ef68.mp4?token=O2umh1tqLbfGt2NesK_csFplx56ynchMPKxQGRK6MkS2e3Ka2JmhOPeT_-X7No_thMrC2tvp8a7mrbpEvUqA50VwWVeDmiVlOhY8-SFO9Ocx-NFH14mkqkWCu-b-JmGZbcJCUW1UjzOTSEBmOfwvN1p1crh5WKJzmr_S0gPT7s3oQg62HbbtQ743ZcIQqEmeBLqy7_dHYxSCO1E9JMN5eIRp-hhsobS2KboGYnEOHYvfRaO91CjBaGkEJ6hrxny1iJt1ztecVFVGkHZg6_MAmxzqtYobDtJ12aOxzIPN_hkTQTZty788PEgbTyU2rJdvXNYCoiT5I7hY30EV-YJdQQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9de073ef68.mp4?token=O2umh1tqLbfGt2NesK_csFplx56ynchMPKxQGRK6MkS2e3Ka2JmhOPeT_-X7No_thMrC2tvp8a7mrbpEvUqA50VwWVeDmiVlOhY8-SFO9Ocx-NFH14mkqkWCu-b-JmGZbcJCUW1UjzOTSEBmOfwvN1p1crh5WKJzmr_S0gPT7s3oQg62HbbtQ743ZcIQqEmeBLqy7_dHYxSCO1E9JMN5eIRp-hhsobS2KboGYnEOHYvfRaO91CjBaGkEJ6hrxny1iJt1ztecVFVGkHZg6_MAmxzqtYobDtJ12aOxzIPN_hkTQTZty788PEgbTyU2rJdvXNYCoiT5I7hY30EV-YJdQQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💰
تولید محتوا ارزان‌تر می‌شود — گوگل مدل‌های Nano Banana 2 Lite و Omni Flash را معرفی کرد، نسخه‌های سبک‌تر از مدل‌های محبوب خود.
نکات مهم:
؛Nano Banana 2 Lite تصاویر را تقریباً در ۴ ثانیه ایجاد می‌کند و هزینه آن حدود ۰.۰۳۴ دلار برای هر ۱۰۰۰ توکن است.
با وجود قیمت پایین‌تر، مدل کارایی خوبی در زمینه متن دارد، متن را به درستی پردازش می‌کند و نتیجه‌ای با کیفیت و بدون آثار قابل توجه ارائه می‌دهد.
؛Omni Flash مسئول ایجاد و ویرایش ویدئو است. هزینه تولید هر ثانیه حدود ۰.۱۰ دلار است.
از نظر هزینه، Omni Flash در سطح Veo 3.1 Fast قرار دارد، اما کیفیت بصری بسیار قابل قبول است.
ویژگی اصلی — می‌توان مدل‌ها را با هم استفاده کرد: ابتدا تصویر را سریع با Nano Banana 2 Lite ایجاد می‌کنیم و سپس آن را به ویدئو با Omni Flash تبدیل می‌کنیم.
https://deepmind.google/models/gemini-image/flash-lite/
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.65K · <a href="https://t.me/ArchiveTell/6642" target="_blank">📅 21:23 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6641">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e1nGFScQ3JjNRoja-f2CZiTJLZfvJT76spPwaIXriVy7TUnUwNslAWmGIlmCihMsJjuE1bbzLpA8kBsk39qf9yIAESndixFsH1oeXZVTAhUhIsZdJ9-bRMpHQb6UzFAAjn47lZigjiz_jEqCtbpsmSADt4joEH4oD2_dTbUGMsfAf_dX62_yyj8KEsM8z9aX4Na7m5TilvtWqnkI0ImvsWkewPR_yA_OA4XDMFd3qr144msEa3SIV3CuQ-mzDRwz13qQhBvneMq0DcFT8W1cXkHJxpBD8BmeQ1rK_Od81Rb0tUhdQq2fR1aqUmka40yk0p26HG9RDodDNN3heUwRlQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دسترسی رایگان به API هوش مصنوعی Opus 4.7
سازگار با همه پلتفرم‌ها:
ربات تلگرام ، وب‌سایت ، Codex و Claude Code
http://zyloo.io
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.34K · <a href="https://t.me/ArchiveTell/6641" target="_blank">📅 20:41 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6640">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4d39bc32d0.mp4?token=vqHOu-uuoBCT6xBmR43x1h0ekchV4fcgaOSVszk3LLLQzZ6iq27y5R4rkRNb3Nr35Qdsht3XKuSQvNFbHah1tdJayZfY8an8YvKuvKz_FAtIqqh7L3xyLD-zpssWfQM0EKjZgDSpzbyZmW0uoOBHB2RBHQ-DD05-HzQJAMGMmiOH9nNlVy6qEzQk0gAUa6vOtUF9MY0kMLcv3dfQTIb2c9R1F70uj0CpB6grKCCiBc7xVrjR9P4LyhAlFLewvWsT6I9XfTUeSqXAJ042WkvglUtZgGEBSz8eFMGLGCFFwjmJCdpCilidaVfyzrhuaFeA_JOGc64GuxzPw0j_8dnVSA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4d39bc32d0.mp4?token=vqHOu-uuoBCT6xBmR43x1h0ekchV4fcgaOSVszk3LLLQzZ6iq27y5R4rkRNb3Nr35Qdsht3XKuSQvNFbHah1tdJayZfY8an8YvKuvKz_FAtIqqh7L3xyLD-zpssWfQM0EKjZgDSpzbyZmW0uoOBHB2RBHQ-DD05-HzQJAMGMmiOH9nNlVy6qEzQk0gAUa6vOtUF9MY0kMLcv3dfQTIb2c9R1F70uj0CpB6grKCCiBc7xVrjR9P4LyhAlFLewvWsT6I9XfTUeSqXAJ042WkvglUtZgGEBSz8eFMGLGCFFwjmJCdpCilidaVfyzrhuaFeA_JOGc64GuxzPw0j_8dnVSA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دقیقا همین‌طور در سال ۲۰۲۷ رم (RAM) خواهیم خرید — یک پروژه با جاسوسان هوش مصنوعی پیدا کردیم که برای شما اینترنت را زیر نظر خواهند داشت
😋
ایده به این صورت است: شما سایت‌ها یا جستجوهای مورد نظر در گوگل را مشخص می‌کنید و «جاسوس‌ها» در فواصل زمانی مشخص اطلاعات را رصد کرده و گزارش را به ایمیل شما ارسال می‌کنند.
https://github.com/firecrawl/open-scouts
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.35K · <a href="https://t.me/ArchiveTell/6640" target="_blank">📅 20:35 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6639">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N2md0UifHzefGrGjMVkpBIrO5CkvWZ02-9aNkph6z2919t9AZ_FvtXbW5SDKVlDEtS-HekDht4txM_XDiswIl9DcREvqZj77bBnR3cw12QRfEpHHf_T6k4-N6JPiQCcvoEd43HaNWZv_R7Nm9CDMsYZWY78pbSLy-qazZc47sIPBfwFOesJ0rObAR1m-rLAjPmXF1XHQK7rBKwiWJhg6HcYJ_UP6oSnjFCCWVbxcKMEcFiS7LhHjielblWYvbESly9VZrMnrLxWcjLsSo33IvoEBaWGWHV3hHgTMuw08NAe4BseJ5Q5v9RRaCqYOJ6GEifzpX2sfEla_DLjhk7OzRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">DocumindAI
راهکاری برای تحلیل اسناد PDF است.
این ابزار قادر است حجم زیادی از اطلاعات در فایل‌های PDF را تحلیل کند، داده‌های کلیدی را استخراج کرده و رابط کاربری منحصر به فردی برای تعامل با خود سند ارائه دهد. این امکان را فراهم می‌کند تا به صورت تعاملی و مؤثر در سند حرکت کرده، اطلاعات موجود در PDF را درک و استفاده کنید.
https://www.documind.chat/
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.3K · <a href="https://t.me/ArchiveTell/6639" target="_blank">📅 20:32 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6638">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LZPS5wL9G3qO47_4kP3byG51H4Gu9kz5DN6przLp1Zb7Qt0e5db9EZzLjhixOpWAW0Xs6S1M8USpM87M9eWPaFtZl8iD25wv2mfhSsh-rN-gqU8OrBscXwcFC1OE9CBfJgX6ZawReejE00wuVP677x9_SRW4bddtS5zZL_AiE0yFYk4YNRwfpkWdlds1ARnW2I6-53t16gQrG-eJXlFK2DxiCVXkhbLaXYwBXOxeTO5OQSTNff67cAKvk1LmOavbB5ucoWHzmgZMrT9G0o_2upVRcIGrCYgABQ3coCZWXjOXtFM66UNxbsQ0jnszcJBPLfhlMWz50nVDgE2t6y6Z7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🧠
نورون‌ها بالاخره دیگر هیچ چیز را فراموش نمی‌کنند — OpenHuman حالت Super Context را دریافت کرده است که بین جلسات، زمینه را حفظ می‌کند و کار را از جایی که متوقف کرده‌اید ادامه می‌دهد.
🔹
در هر بار باز کردن چت، زمینه را به خاطر می‌سپارد.
🔹
مستندات را مطالعه می‌کند، لاگ‌ها را تحلیل می‌کند، ایمیل‌ها را بررسی می‌کند و می‌تواند آنچه روی صفحه نمایش اتفاق می‌افتد را ببیند.
🔹
به طور مستقل اهداف را تعیین می‌کند.
🔹
به ۱۱۸ برنامه متصل می‌شود.
🔹
با سبک کاری شما سازگار می‌شود و به صرفه‌جویی در توکن‌ها کمک می‌کند.
🔗
لینک مخزن گیت‌هاب
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.45K · <a href="https://t.me/ArchiveTell/6638" target="_blank">📅 20:19 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6637">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LBGxmq4IU1uoz5H3l6G0AIO13fx43Jgm2k_g3PR3M6Q9OPNvWIDUcjQyNfp_WzN7FcK89GBOPNe2cVqmHi_0sB7PdSjiUtK-TK3HZEaRD0b3_eS_fQNC6R5V_JR-RE9D9G5KSK2ARi6yxyw-_e9aSUHzBaWcSTELPfIWJZkf5BrslQWApEYU38NZ56xGrgT-bmw3eUNsDVoGPpRRo85FzFbZtoFLVjHMXYRjbhtC_LYIA_eS1QS-VMglpXTfB8vvUEfyBrkUviNG38sDu6pzdUCB8-ghOB8xEVmfQL9KI2XW1zkH-cfnb8jXZG3tP9ceFcy85OQa28WmSAEcheMr0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پاک کردن واترمارک، افراد، اشیاء مزاحم، متن، برچسب و غیره از تصاویر، با تکمیل خودکار پس‌زمینه توسط AI رایگان
لینک:
https://magicremover.org
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.56K · <a href="https://t.me/ArchiveTell/6637" target="_blank">📅 17:27 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6636">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QVlArk58qU4t7jdq7HVzWaY4TPRhaMRHTBuiQQ-fNEGvPH5M_cs6xlRwCZFXp2KHzEtum9b0k9Hd5c62m90ollEYer99TZZ75NS5CigrfgzlzLPepScpLiNxV6kbgiYw2kXlvZ9LH-26EBOHgnwxL_hlRHviQGxFF8G1GA9GBU_0wRD62RskeX0IPz_7_caHAS9G7Kc_aRxzCwlwSrtaXf13Kzd2bJya0dE-96gSmlWEtYrUdomYjDxCfRi8FNpSN-Kge3XrueG2BA38Q2-4tTLmy6ijNdCuCcLzWYZZbKiAaJlwjNYNwl4iiOhJXdEgHb9aNgK_SXIctp9ZwvOHRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
🤯
گوگل را دور بزنید! ‌NotebookLM⁩ رایگان و لوکال شد
🚫
☁️
‏نسخه متن‌باز و محلی ‌NotebookLM⁩ منتشر شد؛ دقیقاً همان تجربه قدرتمند گوگل، اما روی سخت‌افزار خودتان و بدون ارسال داده به سرورهای خارجی.
💻
🔒
🔹
چت هوشمند: تحلیل عمیق، خلاصه‌سازی و یافتن تناقضات در اسناد
🧠
‏
🔹
ارجاع دقیق: لینک مستقیم به پاراگراف‌های خاص، بدون جستجوی دستی
🔗
‏
🔹
تولید چندرسانه‌ای: ساخت پادکست، نقشه ذهنی و دوره‌های آموزشی از روی ‌PDF⁩ و ویدیو
🎙️
🗺️
🔗
لینک مخزن گیت‌هاب
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.69K · <a href="https://t.me/ArchiveTell/6636" target="_blank">📅 16:18 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6635">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JorJmr_5m0g632QHQ_lUa2IQGkfsShRMmksp_Pr9AedgL1Z9a4aA6xBTXcUuEuOYzGTrNOeglmuoSJV-fnfyzCBuIw_MSllOHL5Yu7xcLbN2XIw81xYsIwYmqByh52yApQAZogoSf5juCuiAwUPfmxNZMakCSJpINUpsqNeiDtbJCBdbU94tVYLMG5ZVY1yV1wBc-fz7WN6nqVLsbMlpOEo_K4d4GmXFLoxRpDoa8GOQZ9gM-IShrP51_eexYmrp4aKj-3j9aiFWM9Zuo6bzOb8_TgSXPzd6eBnsQMBOnzIXDD_Zp4hxrvmuZfL3iNHVXDa8b6dmVq5McQ65p_kXeg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دانلود فایل از اینترنت با ‌Torlink⁩، سریع‌تر از همیشه
🤯
‏این ابزار خط‌فرمانی، جستجوی فایل را برایت خودکار می‌کند تا بدون دردسر به منابع معتبر دسترسی داشته باشی.
‏
✨
قابلیت‌ها:
‏•
🔹
بررسی هوشمند منابع و یافتن فایل‌های سالم
‏•
⚡
نمایش دقیق حجم و تعداد سیدها
‏•
🛠️
دانلود مستقیم از محیط ترمینال
‏•
📦
متن‌باز و بدون نیاز به ثبت‌نام
‏
🔗
لینک مخزن گیت‌هاب
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.72K · <a href="https://t.me/ArchiveTell/6635" target="_blank">📅 14:29 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6634">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1b49cca50b.mp4?token=snjXjVNQFojwFi2CueqDq2diBI507Xpge8HP1cG3jhsEAr4i1d7XTkfQW4CT2bzzhRCx6C12SLOfx6GheKlRbTUN4F_15p2rsOOoh5_gTYkZnOxOlSA7wIVF0rgNFTuH593iWfiDl81zIUuje5Z3T3R0OPXv3Z5i6STAA1H2dp3eYoXhFFIK4mjHsw3zGlVk87QukOKgKBntQ_lpgXAs8pzzBbb58_wZ4r3ElU3-ZT0aHHhMRe3nafRgiuHVbs5JGf4FfRbGawCwTdMldicMnz7FX2EWozIPDIXXOSYtkk3YoXR2GXDXw7dqkrQva0UaYAFF6eWiN4gTtGaGp81ntw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1b49cca50b.mp4?token=snjXjVNQFojwFi2CueqDq2diBI507Xpge8HP1cG3jhsEAr4i1d7XTkfQW4CT2bzzhRCx6C12SLOfx6GheKlRbTUN4F_15p2rsOOoh5_gTYkZnOxOlSA7wIVF0rgNFTuH593iWfiDl81zIUuje5Z3T3R0OPXv3Z5i6STAA1H2dp3eYoXhFFIK4mjHsw3zGlVk87QukOKgKBntQ_lpgXAs8pzzBbb58_wZ4r3ElU3-ZT0aHHhMRe3nafRgiuHVbs5JGf4FfRbGawCwTdMldicMnz7FX2EWozIPDIXXOSYtkk3YoXR2GXDXw7dqkrQva0UaYAFF6eWiN4gTtGaGp81ntw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گوگل تصمیم گرفته که پشتیبانی از API پلتفرم Tenor، بزرگ‌ترین مخزن انیمیشن‌های GIF در جهان را متوقف کند.
دسترسی مستقیم به کتابخانه عظیم Tenor از تلگرام، دیسکورد، توییتر و سایر شبکه‌های اجتماعی غیرقابل دسترس خواهد بود.
اگر بخواهید یک گیف انتخاب کنید، باید خودتان تصویر را جستجو کنید.
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.9K · <a href="https://t.me/ArchiveTell/6634" target="_blank">📅 13:31 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6633">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KooP7ZRSP9blYe_PPixZIWN0e4h7BXtO0F2AsG81st71Dcgd1-DqAMCgnsVOVpa1QmA3NUQW-viuNQ_lcEmJ_7NzTRGAZOALOjcP05fgf3nuSTYdlHh_phn6zZMocu2nR0g-BLnAoy2KpbyuRsPCsQTcZ6K9Wz0j0SwZ8luSMw3xZeP1gE5mBc8S5MzyXjSkGL8GfpqZPYBdfyT09ELcf_uF2Iyk_afglWj-q_BNQOBApMZjNukCJLmWEWQGQuOsNEzO1VBOKQm6iuGAcuuf6u8f3pnAQAxIF-O80GlMJ5rZWLDvNDtXo6m54kTGKafE_U2BQa6rk9ScUhcN2j3t-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚫
غیرفعال کردن ردیابی در مرورگر — راه‌حل ایده‌آل برای کسانی که از جمع‌آوری گسترده داده‌ها خسته شده‌اند و به دنبال حفظ حریم خصوصی واقعی هستند.
افزونه
Fingerprint Detector
در سه حالت کلیدی کار می‌کند:
🔹
شناسایی — نشان می‌دهد که سایت دقیقاً چه اطلاعاتی را از کاربر استخراج می‌کند.
🔹
شبح — داده‌های واقعی را مخفی می‌کند و آن‌ها را با مقادیر «میانگین» جایگزین می‌کند و دسترسی به canvas، audio و WebGL را مسدود می‌کند.
🔹
جعل — رد دیجیتال شما را به طور کامل با یک رد جعلی تولید شده جایگزین می‌کند.
🔗
لینک مخزن گیت‌هاب
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.8K · <a href="https://t.me/ArchiveTell/6633" target="_blank">📅 11:26 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6632">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oF9kTFA7mNXwALwb3WpU9Zu08bDPKD1Dlp-AEUOXtCulqtaQsh7JtqjcqynWi0anmJH2BOitUjWbge1GODpkVDHV6NVFgAOBrnn8E2AsOPk71fnwbk3_04A7_o_XsES06N9_khiB2bj0zXMiYHxdTHTP4ep4d05YxkbQLMJudy4ZUSgRlxPKZAow2G1QjSI8rceKtOM9Iz4l5yBqMafnF5XFKtQE9ze2FnQg177ZWlSYzrsNm0eH0W4w8Jx8Uw7QXDqJih6KeNo0VG9auHzv7Tpp1VbbyZ9ZEC51aAq_CWC7zYL_hkeeKWhaNEjwkTw8JUTSx4zzUhum_qzlKGk3Wg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
🤯
هوش مصنوعی بساز، پول دربیار!
‏فکر می‌کنی ساختن هوش مصنوعی فقط مخصوص نوابغ سیلیکون‌ولی است؟
🤔
اشتباه بزرگی است!
‏تصور کن یک جعبه‌ابزار جادویی داری که از صفر مطلق شروع می‌کنی و تا جایی پیش می‌روی که محصولت را به شرکت‌ها می‌فروشی. این دوره دقیقاً همین مسیر را بدون پیچیدگی‌های خشک دانشگاهی به تو نشان می‌دهد.
🛠️
‏
✨
چرا این دوره خاص است؟
🐍
مبانی:
پایتون و ریاضیات را مثل آب خوردن یاد می‌گیری.
‏
🧠
دانشمند:
مدل‌ها را آموزش می‌دهی و بهینه‌سازی (کوانتیزاسیون) را مسلط می‌شوی.
‏
💼
مهندس:
سرویس‌های واقعی می‌سازی و مشتری پیدا می‌کنی.
🌐
GitHub
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.72K · <a href="https://t.me/ArchiveTell/6632" target="_blank">📅 11:09 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6631">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">این هم آموزش راه اندازی</div>
<div class="tg-footer">👁️ 1.96K · <a href="https://t.me/ArchiveTell/6631" target="_blank">📅 05:03 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6630">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">🚀
آپدیت جدید بات تلگرام ما منتشر شد!
✨
بخش جدید
Hugging Face
اضافه شد!
از این به بعد می‌تونید خیلی راحت پروژه‌های خودتون رو از طریق تلگرام دیپلوی کنید:
🔹
فقط کافیه در سایت
huggingface.co
ثبت‌نام کنید
🔹
از طریق بات، توکن خودتون رو دریافت کنید
🔹
پروژه به‌صورت خودکار دیپلوی میشه
🚀
⚡
برخلاف خیلی از گزینه‌های دیگه، این بخش فقط از
سرورهای آمریکا
استفاده می‌کنه.
درسته که سرعتش به پای سرویس‌هایی مثل Render نمی‌رسه، اما در عوض:
✅
حجم بسیار بالا
همچنین در بخش
IP تمیز
می‌تونید این IPها رو اضافه کنید:
🇮🇷
Irancel:
52.214.248.106
32.195.122.200
108.133.38.41
🌐
All net:
amazonaws.com
108.133.38.41
34.196.7.222
3.162.112.2
18.185.80.10
23.162.112.25
2.92.189.25
115.185.114.108
18.138.171.15
135.160.210.199
🔥
تجربه دیپلوی راحت‌تر با
@REN_WZA_BOT
💻
توسعه داده شده توسط
AssA
📌
سورس پروژه
⭐
برای حمایت از پروژه، می‌تونید وارد گیت‌هاب بشید و با دادن Star از ادامه توسعه حمایت کنید.
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.06K · <a href="https://t.me/ArchiveTell/6630" target="_blank">📅 05:02 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6629">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">سورپرایز تو راهه...
Ren panel</div>
<div class="tg-footer">👁️ 1.87K · <a href="https://t.me/ArchiveTell/6629" target="_blank">📅 04:03 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6628">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Mi-JWJbNeCM0ZZW3YCJd6tQOouVBaezZlHlkm8aJJZ-VgGtIUVmxzlCQEGELw8Qbn9BKUK0-fQZS20DpjUgnpi_c4_vn2l_pLcJgt5najVNYjuNXTcmbSMBd1Wh-cn65v9nqZkRjOYIpkNRYnL5gBum3LgDF_CyIj3iboJHb6v7mcWeVXHSgwrM6FLQXO-hdMhGVO0KM_HN7rnFOXPetKIVwheAq_tkxbDsza4M5v8wje99KUHcxXSJ5tLV6z31T_RvN4Rlrb2ndTT993LQzsvL79e8Rr2zLdHrT6y5dwWDFUBtQrEUMVFtNcGwp-XSyyfzm9wlg-wNxQuLrYybKlA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">واتس‌اپ پس از تقریباً ۱۷ سال از وجود خود، نام‌های کاربری را معرفی کرد — می‌توان بدون شماره تلفن با کاربر شروع به گفتگو کرد.
تلگرام به انقلاب سال واکنش نشان داده است
😁
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.14K · <a href="https://t.me/ArchiveTell/6628" target="_blank">📅 22:53 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6627">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d53c28976b.mp4?token=p5XVRDHBt5yFe4Px5tY3JnxQh22m0hncrdwfO91eEXSena2POy0SPjFogMxShI86rknWgwvwBYPl-AISDrBPP4Ap3ZeXRY3JzpwlZcqRf13FhRTJ07ikQPL9dgxIkcH2d51Zwp8XdL9GMwyuUVxyF9hAab-_9puQvkwYQ-HyHCzwz69lQZNdev8b6wmVuC-U4YZ5fT8MlWH6mgIUSUfZcmR0BilZ3PUmwTME4u79ugP-MiRr2MWYy5An_4GMyEnnYiEQS0iZSV63q5E8nW3SvkLlFQDwihogk_41BBnQXzL_ZuZ68SVy_fu-wdB1QQtXO4npVHEgoKe7eecVVwWcb4xfnq3C7u2esrXgJDcuCVipwmgi6NKdYBNmXyb8GcBgNbc4UEOepe8y5loOzvnujGJTjZO40ykSrdpkVjTqes9QyCFrymevXaFatmE3Lfbt5e6J_B8HYVQ0aLwGRD2x3rGBq2nAO3eenMbtlt6NSIKFO3jmGKaGBzHuyEkFrDcvejJuYczDoHeP-evYfUOVjPD4L_e27nMGg8dT5Tyx3s1FofwqN6K3dmhH-Ty9ns8jCk0z8Xn54QFhcXE4FONlGvRiqaUwH08oD1kKs6rONK9l-f9nZ7k8ptVJXTAzpiuVLD4k2rJ23wN2kT-RGUiHPwL3uy-0v0LswoeGpMsf1s0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d53c28976b.mp4?token=p5XVRDHBt5yFe4Px5tY3JnxQh22m0hncrdwfO91eEXSena2POy0SPjFogMxShI86rknWgwvwBYPl-AISDrBPP4Ap3ZeXRY3JzpwlZcqRf13FhRTJ07ikQPL9dgxIkcH2d51Zwp8XdL9GMwyuUVxyF9hAab-_9puQvkwYQ-HyHCzwz69lQZNdev8b6wmVuC-U4YZ5fT8MlWH6mgIUSUfZcmR0BilZ3PUmwTME4u79ugP-MiRr2MWYy5An_4GMyEnnYiEQS0iZSV63q5E8nW3SvkLlFQDwihogk_41BBnQXzL_ZuZ68SVy_fu-wdB1QQtXO4npVHEgoKe7eecVVwWcb4xfnq3C7u2esrXgJDcuCVipwmgi6NKdYBNmXyb8GcBgNbc4UEOepe8y5loOzvnujGJTjZO40ykSrdpkVjTqes9QyCFrymevXaFatmE3Lfbt5e6J_B8HYVQ0aLwGRD2x3rGBq2nAO3eenMbtlt6NSIKFO3jmGKaGBzHuyEkFrDcvejJuYczDoHeP-evYfUOVjPD4L_e27nMGg8dT5Tyx3s1FofwqN6K3dmhH-Ty9ns8jCk0z8Xn54QFhcXE4FONlGvRiqaUwH08oD1kKs6rONK9l-f9nZ7k8ptVJXTAzpiuVLD4k2rJ23wN2kT-RGUiHPwL3uy-0v0LswoeGpMsf1s0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خداحافظی با چشم‌درد دیجیتال!
👋
👀
تا حالا شده بعد از چند ساعت کار با لپ‌تاپ، چشمانت بسوزد و احساس کنی  به یک لامپ ۱۰۰۰ وات خیره شدی؟
💡
😫
بیایید روراست باشیم: صفحه نمایش‌های امروزی مثل آینه‌های صیقلی هستند که نور را مستقیم به چشم‌هایت پرتاب می‌کنند. اما تصور کن اگر بتوانی یک لایه نامرئی از «کاغذ واقعی» یا «شیشه مات» روی مانیتورت بکشی. جادوی
Paperman
دقیقاً همین است! این ابزار با تغییر بافت پیکسل‌ها، صفحه نمایش را از حالت آزاردهنده به یک سطح نرم و خوانا تبدیل می‌کند، درست مثل ورق زدن یک کتاب قدیمی و دلنشین.
📖
☕
✅
چرا باید همین الان نصبش کنی؟
•
🧊
حذف بازتاب نور:
صفحه مات می‌شود و دیگر نور چراغ سقف روی مانیتورت نمی‌افتد.
•
🎨
تنوع بافت:
از کاغذ کاهی تا E-Ink (مثل کیندل)، هر سلیقه‌ای را پوشش می‌دهد.
•
🎯
هوشمند و انتخابی:
می‌توانی افکت را فقط برای مرورگر فعال کنی و در فتوشاپ یا بازی‌ها خاموشش کنی.
•
🖥️
همه‌کاره:
هم روی ویندوز و هم مک‌او‌اس به زیبایی کار می‌کند.
به نظرت کدام بافت برای کارهای روزمره‌ات مناسب‌تر است؟ کاغذ کاهی یا شیشه مات؟
👇
💬
🔗
دانلود:
Windows
macOS
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.09K · <a href="https://t.me/ArchiveTell/6627" target="_blank">📅 20:49 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6626">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">اولین تریلر Cyberpunk  Edgerunners 2 منتشر شد!
🔥
انتظار داشته باشید که هر ۱۰ قسمت این فصل جدید،
پاییز امسال
پخش شوند.
آماده‌اید برای بازگشت به نایت‌سیتی؟
🏙️
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 2K · <a href="https://t.me/ArchiveTell/6626" target="_blank">📅 20:28 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6625">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">حدود 900 تا کانفیگ مختلف
📶
https://raw.githubusercontent.com/SoliSpirit/v2ray-configs/refs/heads/main/Countries/Germany.txt
💬
@Archivetell</div>
<div class="tg-footer">👁️ 2K · <a href="https://t.me/ArchiveTell/6625" target="_blank">📅 20:03 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6624">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">#اختصاصی
🎧
استودیوی کامل AI: از ایده تا مسترینگ
۱۱ ابزار برای ساخت حرفه‌ای موسیقی:
🎤
تولید: Suno, Udio
🗣️
کلون صدا: Kits AI, Synthesizer V
🎹
سمپل/لوپ: Stable Audio, Splice Create
✂️
جداسازی/ویرایش: LALAL, RipX
🎚️
میکس/مستر: Sonible, iZotope Ozone 11
🔊
پاکسازی: Adobe Enhance
💡
نکته: ترکیب این ابزارها فرآیند تولید را از هفته‌ها به چند ساعت کاهش می‌دهد.
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.06K · <a href="https://t.me/ArchiveTell/6624" target="_blank">📅 17:22 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6623">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UxwWikwrW0tOGcC6RIu6wf_0UWJ1uSFJDRz-SuJyiwC0cdCR9F_sG2yWdJmUlfIghCKSSEGu3LLXJItioRZsqyKk_b01vN0ds1ZnLYvuqLkI1UY5C9SLihjmAqYYp5VNDXVCz1umQriHHB27jtzUdanMGaaeEKgnt5_GwvgyYNnAlVg404cXFK8JbA28znK4zzN1k3g06z0tQp7LDzB5TwsS13oqkquwqVJBRrJ4jZeIwfnhSuH-9303AMBqX0HmbQ-dBNQ3F4hMrwxOCkGZAQElPYBMgKKc1iss0tpsnfl9G0zh2NoScCbwwZLE7iYjYGEg9-IzSB9MO5jg_JKFpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
معرفی GTweak؛ جعبه‌ابزار همه‌کاره برای شخصی‌سازی و بهینه‌سازی حرفه‌ای ویندوز!
💻
✨
اگر به دنبال یک ابزار پرتابل (بدون نیاز به نصب) هستید که کنترل کامل سیستم‌عامل ویندوز را به شما بدهد، GTweak یکی از قدرتمندترین گزینه‌هاست. این برنامه با رابط کاربری نوشته…</div>
<div class="tg-footer">👁️ 1.96K · <a href="https://t.me/ArchiveTell/6623" target="_blank">📅 15:28 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6622">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">نحوه اکتیو ویندوز با اسکریپت Microsoft activation
💻
اول تو منو استارت Powershell رو سرچ کنین و باز کنین   بعد از اجرا شدن پاورشل فقط کافیه کد زیر رو وارد کنین و اینتر بزنین .   irm https://get.activated.win | iex   اگر کد به مشکل خورد و اجرا نشد دستور زیر…</div>
<div class="tg-footer">👁️ 1.97K · <a href="https://t.me/ArchiveTell/6622" target="_blank">📅 15:20 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6621">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">نحوه اکتیو ویندوز با اسکریپت Microsoft activation
💻
اول تو منو استارت Powershell رو سرچ کنین و باز کنین
بعد از اجرا شدن پاورشل فقط کافیه کد زیر رو وارد کنین و اینتر بزنین .
irm https://get.activated.win | iex
اگر کد به مشکل خورد و اجرا نشد دستور زیر رو بزنین ( نیاز به ویندوز ۱۰ یا ۱۱ به روز داره )‌
iex (curl.exe -s --doh-url https://1.1.1.1/dns-query https://get.activated.win | Out-String)
Github
😀
📱
@Archivetell</div>
<div class="tg-footer">👁️ 1.9K · <a href="https://t.me/ArchiveTell/6621" target="_blank">📅 14:46 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6620">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">حجم : نامحدود
زمان : تا ۱۲ شب
vless://63b43d54-3bdc-4d9e-b3f3-10163c892936@64.90.7.102:8443?type=ws&path=%2Fws&host=play.google.com&security=none#%D9%86%D8%A7%D9%85%D8%AD%D8%AF%D9%88%D8%AF
وصل شدید بگید</div>
<div class="tg-footer">👁️ 1.83K · <a href="https://t.me/ArchiveTell/6620" target="_blank">📅 12:12 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6619">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Qy5qHuDqM9sKIS5LKxzosQs7v7Y_eT4Q7x8yVkTJGGyLZjKw1PUex1ugr9T0b73kpa4aP06O1cXsGZ57lck9RnfhBrziybmEh-0efLJDH00ez-Fd8TRm6t_nR_PfZeIN_gkZ6GWypYCY8OzuFDP6a57Wy7COrwJei4Ht3ZR-raXBNXD8cjwiCauC_v6PiKTXOdBrb683k3wTpv3E1JfAyEGGidhXqB_yjiQhh5WgytCbeu6U_aePUBt4TswnrhFQFms3IKj0q5c1JndfCmFWsApygz8SH5kgiKxrFhVuTTDneg0MfwZrtyOTPhCnbwTFNmeRV4tDpePMdxQzS2eu8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نقشه راه جامع علوم کامپیوتر: ۸۰۰+ منبع از دانشگاه‌های برتر جهان
🎓
اگر می‌خواهی به یک توسعه‌دهنده حرفه‌ای تبدیل شوی، این مخزن گنجینه‌ای از دوره‌های دانشگاه‌های هاروارد، استنفورد، MIT و شیکاگو است.
✨
چرا این لیست؟
•
🏛
منابع معتبر:
دسترسی به دوره‌های دانشگاه‌های تاپ جهان.
•
🤖
پوشش کامل:
از الگوریتم‌ها و زبان‌های برنامه‌نویسی تا هوش مصنوعی و رباتیک.
•
📚
دسته‌بندی هوشمند:
گم نمی‌شوی؛ دقیقاً همان چیزی را که نیاز داری پیدا می‌کنی.
•
🔄
همیشه به‌روز:
نویسندگان مخزن را مداوم آپدیت می‌کنند.
مسیر یادگیری‌ات را از اینجا شروع کن!
👇
🌐
GitHub
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.93K · <a href="https://t.me/ArchiveTell/6619" target="_blank">📅 11:05 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6618">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E-n0-pMZL_4vL-Lm9_5mk4fZDE6qMTsWGQC_HgJsA1X8fFDksNheMGhFFSEg92a9nr4N5WprUp9WMtfeRM4MAydCWd8b32FpbZ0mk7JHG25iyKDlYwzjGDA4v5SyylqgBwv3cuNfDa4vfRdBoK99iiAFvw5RuVgceGbouYKS3kbIZ5ie8CR2jDdxn2MWqUfCccScj8HPJB5vT2CWz7du8lRsSUpWJGzFrL6XQAVi9vKSbxppAumqB7BBA6bqe2i4yZen1MTSrSAMjnKUpppHfwYXtc0xRL430avqLTCFYlw5Cp_Bc5nkNEKQztU7hl57Q1T6WcaabFmhFWRe2L2nJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شرکت Anthropic بسیاری از دوره‌های هوش مصنوعی خود را رایگان کرده است.
🌐
Site
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.09K · <a href="https://t.me/ArchiveTell/6618" target="_blank">📅 09:36 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6617">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iZUBliDWjqt188blOewPPURr1aKKV_cH2LxAW9tuyK4G1m0ti6RWKDm_OqEEHEDkpPtLrnyTlkq__VjMI4ipQs7V-wcVkNVwABaseIKJ4DDP6st6RnLJD84QswdI6nGYbc8fwfNxR2vIchOxaJzrqyaJkW0316YQ-6ZEodV5DPlMsADar5WAlWVd7XbhXJN2o0FFX2d63bmIk2tpW_HLKPIQbHkUvOn_q_zmlL2VmOnjAkc82SsCtDaf9b89RkQzVaWHhlMVQOLx7gkoebqhdpOfJuPImtsG5kKjlqGYW0PjKWCPYNAFESFbuHTgDPy-16dpYVe7DDAww2fwfUpJkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">OmniRoute
۱۶۰+ هوش مصنوعی رایگان در یک API!
🤯
دیگر نگران تمام شدن توکن‌ها نباشید. OmniRoute با ارائه
توکن‌های نامحدود رایگان
، تمام مدل‌های برتر جهان را در یک نقطه جمع کرده است.
✨
چرا OmniRoute؟
•
🔄
تغییر خودکار مدل:
اگر توکن یک مدل تمام شد، بلافاصله به مدل بعدی سوئیچ می‌کند.
•
📉
فشرده‌سازی هوشمند:
تا ۹۵٪ کاهش حجم متن برای صرفه‌جویی بیشتر.
•
🌐
دسترسی جامع:
GLM، Grok، Mistral، DeepSeek، Qwen و... همه در دسترس.
•
🛠
پشتیبانی کامل:
سازگار با MCP و مهارت‌های پیشرفته.
یک API، تمام هوش‌های مصنوعی دنیا. رایگان و بی‌نهایت!
🚀
🌐
GitHub
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.98K · <a href="https://t.me/ArchiveTell/6617" target="_blank">📅 09:00 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6616">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">10 میلیون توکن رایگان هوش مصنوعی Mercury 2
🎁
وقتشه ربات تلگرامیت رو با هوش مصنوعی ارتقا بدی!
✨
✅
مناسب برای ساخت چت‌ بات
✅
دسترسی فوری و رایگان
⚡️
همین الان فعال کن:
🔗
platform.inceptionlabs.ai
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.85K · <a href="https://t.me/ArchiveTell/6616" target="_blank">📅 02:05 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6615">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f9a7cbc953.mp4?token=NaQqdm1p2DaPv2MzOXn0EE-Smztqd7_LY58KwFfwcfW2byC34Fyb2XUhgqJdXpSATkYZxssDG7h7tddyZZ-ZIVmFKWb_td0nGYfznwicvB1FWH-7Vxqfshw_ZatbU39Po7Jel6c_1uAyY1xmLh-4mV234Vw6NlyMbIqhve6XGGj6JuBGO63nEavZmHPfIgvDniL-CTRuNFLvP22AEO83QmPUlLnHJ7tlg_V0V78e1Hj97kQm820JAVazvWtfLQQ3n9n9lYXT-gFSYxwMT65UIY3KDGGm0fQp8gTKJj5y0hC6BMZCFYM22AaGjYecOdN5-pNmnYnDdVsLip2S8xgBtg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f9a7cbc953.mp4?token=NaQqdm1p2DaPv2MzOXn0EE-Smztqd7_LY58KwFfwcfW2byC34Fyb2XUhgqJdXpSATkYZxssDG7h7tddyZZ-ZIVmFKWb_td0nGYfznwicvB1FWH-7Vxqfshw_ZatbU39Po7Jel6c_1uAyY1xmLh-4mV234Vw6NlyMbIqhve6XGGj6JuBGO63nEavZmHPfIgvDniL-CTRuNFLvP22AEO83QmPUlLnHJ7tlg_V0V78e1Hj97kQm820JAVazvWtfLQQ3n9n9lYXT-gFSYxwMT65UIY3KDGGm0fQp8gTKJj5y0hC6BMZCFYM22AaGjYecOdN5-pNmnYnDdVsLip2S8xgBtg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">#اختصاصی
🚀
معرفی PokieTicker؛ کشف دلیل واقعی پشت هر نوسان قیمت در بازار بورس!
📈
✨
اگر شما هم از دیدن نمودارهای شلوغ و کندل‌استیک‌ها (Candlesticks) خسته شده‌اید و همیشه این سوال برایتان پیش می‌آید که *«چرا قیمت این سهم امروز بالا/پایین رفت؟»*، اپلیکیشن فوق‌العاده…</div>
<div class="tg-footer">👁️ 1.88K · <a href="https://t.me/ArchiveTell/6615" target="_blank">📅 00:42 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6614">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">#اختصاصی
🚀
معرفی PokieTicker؛ کشف دلیل واقعی پشت هر نوسان قیمت در بازار بورس!
📈
✨
اگر شما هم از دیدن نمودارهای شلوغ و کندل‌استیک‌ها (Candlesticks) خسته شده‌اید و همیشه این سوال برایتان پیش می‌آید که *«چرا قیمت این سهم امروز بالا/پایین رفت؟»*، اپلیکیشن فوق‌العاده و متن‌باز
PokieTicker
دقیقاً برای شما ساخته شده است!
🔥
این ابزار چگونه کار می‌کند و چه امکاناتی دارد؟
1️⃣
تلفیق اخبار و نمودار:
نقاطی روی نمودار کندل‌استیک ظاهر می‌شوند که نشان‌دهنده اخبار منتشر شده در آن روز هستند. با کلیک روی هر نقطه، متوجه می‌شوید چه خبری باعث آن نوسان شده است.
2️⃣
فیلتر هوشمند اخبار:
دسته‌بندی اخبار بر اساس تأثیرات مختلف (گزارش درآمد، تغییرات مدیریتی، محصولات جدید، سیاست‌گذاری و...).
3️⃣
تحلیل و پیش‌بینی با هوش مصنوعی:
با استفاده از مدل‌های قدرتمند
XGBoost
و
Claude
، سنتیمنت (احساسات) اخبار را تحلیل کرده و روند قیمتی سهم را برای روزهای آینده (T+1, T+3, T+5) پیش‌بینی می‌کند!
4️⃣
کشف الگوهای مشابه:
روزهای گذشته که اخبار و شرایط مشابهی داشتند را پیدا می‌کند تا ببینید در آن زمان بازار چه واکنشی نشان داده بود.
5️⃣
رایگان و آماده استفاده:
دیتابیس لوکال (SQLite) از قبل در مخزن گیت‌هاب قرار دارد و برای اجرای اولیه نیازی به خرید API کلیدهای پولی ندارید.
﻿
⚡️
مشخصات فنی:
*
بک‌اند:
Python (FastAPI) + SQLite
*
فرانت‌اند:
React + TypeScript + D3.js
*
مدل‌های AI/ML مورد استفاده:
XGBoost, Claude Haiku / Sonnet
﻿
🔗
لینک مخزن گیت‌هاب
🔵
@ArchiveTell
| Bachelor
⚡️
──────────────────────────────</div>
<div class="tg-footer">👁️ 1.91K · <a href="https://t.me/ArchiveTell/6614" target="_blank">📅 00:40 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6613">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8393e8cd0f.mp4?token=QcQbNpOVbM4CgJI6m8X_79MgBXDeaMW5TyWLiyjwr8jHee6EhMfZ5pI0juPLmZqaGy6eWOxSJOIH07R6rqJ1v2chhJdeidGrwTLL55cOFCNGGHGFHNH0B3Ei1fRYYFmk22gZItc1ZpeA5q6OUIhh_erZ6YTKbtX9TlOolKbjqZMD8eIhOw1PAev5K2pB8Mw_Ft0ewhG-Kgh92VVJaOyqe_vKkRrLA1gvmvXYOMJHHjH684BH-aplggqlRvZMIgyssDErJ5Uxy6yDdUwwO4t4NWgjMr-od1j6eoEByPnBytzQzla3fy2mviwqQ-8K2N-wMJV6cVLQ-oHrVPuK1rmBHQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8393e8cd0f.mp4?token=QcQbNpOVbM4CgJI6m8X_79MgBXDeaMW5TyWLiyjwr8jHee6EhMfZ5pI0juPLmZqaGy6eWOxSJOIH07R6rqJ1v2chhJdeidGrwTLL55cOFCNGGHGFHNH0B3Ei1fRYYFmk22gZItc1ZpeA5q6OUIhh_erZ6YTKbtX9TlOolKbjqZMD8eIhOw1PAev5K2pB8Mw_Ft0ewhG-Kgh92VVJaOyqe_vKkRrLA1gvmvXYOMJHHjH684BH-aplggqlRvZMIgyssDErJ5Uxy6yDdUwwO4t4NWgjMr-od1j6eoEByPnBytzQzla3fy2mviwqQ-8K2N-wMJV6cVLQ-oHrVPuK1rmBHQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">DewatermarkAI
حذف واترمارک با هوش مصنوعی در مرورگر
این سرویس رایگان واترمارک‌ها را از عکس‌ها حذف می‌کند و فایل آماده را می‌توان با وضوح اصلی دانلود کرد.
🌐
Site
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.77K · <a href="https://t.me/ArchiveTell/6613" target="_blank">📅 00:00 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6612">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VX04Jqmu0TAzl89FUOuCQx_yEPV5ni276OPSkoI0SwtpDR7Qplj6ST-W5UDBEQ124M3C1paTfLAbmiR9jBl5OcD2odMW55kNYmjav69xrUkbpdMrte4EFRKeHqay2d4rxv994VsfFyfxuemtaJqMYdMjn9w6hq398AssC8obU_egBUMe8hrBfJWUKU4daxHVEOVAjtDRoTW33IgpJfC4xJBZLXh3mF7dQX4xh882rIakh-ZTBdk5eB8Wwc0fyFjXHdKMNGCB8PxqpyJjRZ3RPvl78E-EZ0NTKy1SZujiDBpBa8k0PmrdebnOw-3AY4D6sxnjtCX5pcYFLuIkzjjr3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">از به‌هم‌ریختگی اسکرین‌شات‌ها خسته شده‌اید؟ Trickle دستیار جدید هوش مصنوعی است که همه اسکرین‌شات‌های شما را به‌طور منظم سازماندهی و خلاصه می‌کند
فقط یک اسکرین‌شات بگیرید و آن را به Trickle ارسال کنید. هوش مصنوعی پیشرفته Trickle یک خلاصه دقیق تولید می‌کند که اطلاعات کلیدی مانند متن، نمودارها و یادداشت‌های دست‌نویس را استخراج می‌کند و سپس می‌توانید این داده‌ها را جستجو و درخواست کنید.
🌐
Site
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.74K · <a href="https://t.me/ArchiveTell/6612" target="_blank">📅 23:35 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6611">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oAL5YoXW-koICBvLcu81JGiwDkjXQZsB5U_9O_EYXWwKZC_bBAeAkfjzPLpB2F56PsXvZslBIpEYO-eulG45XPeVBESr4L1hlIjGvBV9NBRjo4103bL5U2v0dOM8uRnGWogID_Jr_yYPbMwrVQ_Vwe7DaHIgXA9Fzaa9iqi2RfBz9TEiy_QksLDLL8MVyZ5KjA76tA6cxydEZ_u3j3OXV1_5HAopLGLfvLQVjQYy-eNCDkG-RoufvoWRHjc_xe7PpJeJ4uVRcD3y6-vGxDL1tLXPFHWhBwRoIGUuvx0ATIjnjCMr3d1Com4Q4PsyUhnsdzqN_3yBBvmwnoQSSujcjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🧠
شورای خردمندان هوش مصنوعی: تصمیم‌گیری با قدرت ۱۸ متخصص
آیا از پاسخ‌های ساده و تکراری هوش مصنوعی خسته شده‌اید؟ با این ابزار، مسئله خود را به شورای مجازی فیلسوفان، دانشمندان و مهندسان بسپارید و تحلیلی عمیق و چندجانبه دریافت کنید.
➖
مناظره کامل بین ۱۸ کارشناس مجازی (سقراط، ارسطو، سون‌تزو، آندری کارپاتی و...)
➖
بررسی مسئله از زوایای مختلف فکری و تخصصی
➖
ارائه راه‌حل‌ها همراه با نقد و رد استدلال‌های رقیب
➖
دریافت نتیجه‌گیری نهایی بر اساس جمع‌بندی بحث‌ها
➖
تحلیل واقعی به جای پاسخ‌های کلیشه‌ای
این ابزار برای تصمیم‌گیری‌های پیچیده و نیاز به دیدگاه‌های متنوع، گزینه‌ای بی‌نظیر است.
🌐
GitHub
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.74K · <a href="https://t.me/ArchiveTell/6611" target="_blank">📅 21:45 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6610">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jK486J9UAYxHTnWXUCIAT5CBhxb7jyCXVVE6D1hW2RYEAy8g4WozQzq0B0zukSP_lwzF26hkmbmDi_KBFLl4A49EBeTBaqtkLfTTbMnkqEAYasiGeFX65JzWMyC06bhzifCbS_EuLI7_Rx1dpR4uFHSu5tcDS_KlKwMya8RE883dATxvmEQ_wre2SbT61Aa9lpSZMyYEWOn2QwFKK_SPBfexPlIiHNH59c6-QjX1YDXPCXmhv6YOUItlnDjE31itTaF8Vf42id5QG5Y0JlDRzE-CM6C1bbyssTppuM35MnqsYThKqp3LbtQ02O4L9uv9-4GYbzUS0E8qhavJM2Grzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎵
OFPlayer: پخش‌کننده موسیقی محلی و حرفه‌ای
➖
پشتیبانی کامل از فرمت‌های FLAC و MP3
➖
مدیریت آسان کتابخانه و لیست‌های پخش
➖
نمایش متن ترانه (Lyrics) و کاور آلبوم
➖
تحلیل دقیق فراداده‌های صوتی
➖
اتصال به سرویس‌های WebDAV، Subsonic و Navidrome
➖
رابط کاربری ساده، رایگان و بدون نیاز به ثبت‌نام
این پخش‌کننده برای کاربران NAS و کسانی که مجموعه موسیقی شخصی دارند، بسیار مناسب است.
🌐
Site
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.73K · <a href="https://t.me/ArchiveTell/6610" target="_blank">📅 21:26 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6609">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ITPusbtvyiVV-j40KrTVSvceKfnZPVs9pV2BemXQ2BvQYAtrM6BhLblrYKkEDNR8HptZFtXNwT3D68nntrvTKzAI2-6Xez5H7Gue3PW7jCtDw_cXL6Cz_Xd_8VhGuZZ1w4lC9lMdmSedallefX9nkA8lmwF0UfNqzietWDljCTnJG0fHrCLSQjG92RZHffqY4VpV8weZwkpbi9I3e99KU55gCM7y1ljmlXTMS76_E2u0-3YfACa0FZtJYIEaLz5Xnslw0460T93iVhCWuFCW2Cl0dc7fOeZoaO4XEivb1n-RhHGoLRhFPbfogxJhL3BpIFUFyoZwcraa1pAN129OEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏋️‍♂️
مخزن کد با ۱۳۲۴ تمرین برای اپلیکیشن فیتنس!
اگه میخوای اپلیکیشن فیتنس خودت رو بسازی، این گنجینه رو از دست نده:
• ۱۳۲۴ تمرین کامل
• انیمیشن‌ها و تصاویر باکیفیت
• جزئیات عضلات درگیر و تجهیزات مورد نیاز
• دستورالعمل‌های گام‌به‌گام حرفه‌ای‌
پروژه خودت رو با این داده‌های غنی شروع کن!
🌐
GitHub
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.81K · <a href="https://t.me/ArchiveTell/6609" target="_blank">📅 19:25 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6608">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">خب Claude Fable هم استفادش برای مردم عادی کنسل شد
چینیا هم دارن مدرک جعلی میسازن تا بتونن ازش استفاده کنن
😂</div>
<div class="tg-footer">👁️ 1.77K · <a href="https://t.me/ArchiveTell/6608" target="_blank">📅 19:20 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6607">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">🚀
تبدیل جادویی اسناد پیچیده به Markdown خالص با MinerU!
📄
✨
اگر برای استخراج متن، جداول و فرمول‌ها از فایل‌های درهم‌ریخته و پیچیده مشکل دارید، ابزار متن‌باز
MinerU
دقیقاً همان چیزی است که نیاز دارید! این پروژه فوق‌العاده که با استقبال بی‌نظیری روبرو شده و بیش از ۷۰ هزار ستاره در گیت‌هاب دریافت کرده است، اسناد شما را به راحتی و با بالاترین دقت به فرمت تمیز Markdown تبدیل می‌کند.
🔥
ویژگی‌های برجسته این ابزار:
1️⃣
پشتیبانی از فرمت‌های متنوع:
توانایی پردازش و تبدیل فایل‌های PDF، DOCX، PPTX، XLSX، تصاویر و حتی صفحات وب.
2️⃣
استخراج دقیق جزئیات:
بیرون کشیدن بی‌نقص متن‌ها، جداول و فرمول‌های پیچیده (ریاضی و علمی) از دل اسناد.
3️⃣
پشتیبانی از ۱۰۹ زبان:
قابلیت تشخیص و پردازش بی‌نظیر اسناد در اکثر زبان‌های دنیا.
4️⃣
کاملاً رایگان و متن‌باز:
یک پروژه Open Source قدرتمند و بدون هیچ‌گونه محدودیت پرداخت یا نیاز به سرویس‌های ابری پولی.
🔗
لینک مخزن گیت‌هاب
🔵
@ArchiveTell
| Bachelor
⚡️
─────────────────────────────</div>
<div class="tg-footer">👁️ 1.87K · <a href="https://t.me/ArchiveTell/6607" target="_blank">📅 18:03 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6606">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v5HtgJL-ee1UXRANZa2OXDHr0UhKXBMumyC4hNMv6FNj9SWIp0UzKLngH5mLCaNMe2NUu2NSDSzuLVOVL_eM1QDG9y8SkJOG46zI_Mno2uXMK7OWqDarXlZi_CZ4NAOJx7amAts8jbyGIkfMCu-kUxYc8JIc3HtYnNcQP_fMXYjA-smSaVPyT-fDeaumU79YUhddA_AotyYbjq3sTvHyjkSh5b650nt44cjC88pjA1Ye4jA5LPcPfjCIFvPg5p62bGMdwdCb4Rh-o-JeO1prK8-g5bkBVlEvOmxmHiVS4WozxjbUxmEuAj92Ciq0Bto0UQsIQ9N7nsDU6PgUhwmJkw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چینی‌ها ElevenLabs را کشتند!
💀
توسعه‌دهندگان ByteDance نسخه SeedAudio 1.0 را عرضه کردند که هر نوع گفتار و افکت صوتی را کلون و تولید می‌کند.
1⃣
ایجاد گفتگو با چندین شخصیت: هر شخصیت متمایز است، دارای احساسات، سرعت، تمبر و حتی لهجه منحصر به فرد؛
2⃣
دریافت تا سه منبع برای کپی کامل صدا، احساسات و سبک؛
3⃣
تولید صداها بر اساس پرامپت، مرجع صوتی یا حتی تصویر.
آیا این پایان دوران انحصار ElevenLabs است؟
🤔
🌐
Site
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.82K · <a href="https://t.me/ArchiveTell/6606" target="_blank">📅 16:00 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6605">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EksBs5AnaXAqjWPHV95nTt6ZNo-0pq4sxgA6IBhUGMm_rUGuiJzM_rioue_BT8FwYlUbXkcneIBSHD3SL50MUHmePPMQ_Y_tOCwZ4GevMpGLSQNNNpcyskKKOj0yuxrYij3cy5C92BBgucM0RbPxGeGey425QaS4hrivJcMZDIwwcDTwvKBlxmOiPj0IGdI3fGVHG_jeag7W5noJk-GvN03WKg2iJaJoAwte6byB7Fzd2SRQ-5ju4kRFnm7nNVfyp4v35J4ogUxo5NFPB-6O3e3rzKUQJfzF-EoMik-QvSkgZOaurgC08Of1U-7m2d-2s3r0p0T990ysh7qaenl54Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎨
تولید رابط‌های کاربری زیبا با پرامپت‌های آماده
🌐
Site
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.82K · <a href="https://t.me/ArchiveTell/6605" target="_blank">📅 14:50 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6604">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">🚀
معرفی IstanPdf؛ ابزار قدرتمند و آفلاین برای مدیریت فایل‌های PDF و DOCX!
📄
✨
اگر از سایت‌های پولی، تبلیغات آزاردهنده و محدودیت‌های سرویس‌های آنلاین تبدیل فرمت خسته شده‌اید، اپلیکیشن
IstanPdf
دقیقاً همان چیزی است که نیاز دارید. این ابزار کاملاً آفلاین توسعه یافته تا جایگزینی بی‌نقص و رایگان برای سرویس‌های پولی (Freemium) باشد. در این اپلیکیشن حریم خصوصی شما در بالاترین سطح قرار دارد و هیچ فایلی از گوشی شما خارج نمی‌شود!
🔥
امکانات فوق‌العاده IstanPdf (نسخه v1.0):
1️⃣
ابزارهای حرفه‌ای PDF:
*
Merge:
ترکیب و چسباندن چندین فایل PDF به یکدیگر.
*
Split:
استخراج صفحات دلخواه با تعیین محدوده صفحات.
*
Remove & Reorder:
حذف صفحات اضافی و تغییر ترتیب صفحات یک فایل.
2️⃣
تبدیل فرمت (Conversions):
* تبدیل یک یا چند تصویر به یک فایل PDF یکپارچه.
* استخراج صفحات PDF و ذخیره آن‌ها به عنوان عکس.
3️⃣
ابزارهای کاربردی DOCX:
امکان حذف صفحات خاص و تغییر چیدمان و ترتیب صفحات در اسناد ورد.
4️⃣
حریم خصوصی و امنیت مطلق:
کاملاً آفلاین، بدون نیاز به ساخت حساب کاربری، بدون محدودیت حجم و آپلود، و فاقد هرگونه تبلیغات و پرداخت درون‌برنامه‌ای.
🔗
دانلود
🔵
@ArchiveTell
| Bachelor
⚡️
──────────────────────────────</div>
<div class="tg-footer">👁️ 1.98K · <a href="https://t.me/ArchiveTell/6604" target="_blank">📅 13:52 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6603">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MY4t1eFEYWWCQE2QOdwlK61n0Uk9oMNeLMf7oAbdCHlolem7xYfZU4dCt3HCLh2U8vZ_wzyCRqXZHJvn6UApCaFlM6WH0p9AVKJE75Kd8zKSpSJNSG1_rSZIfWGH0lRYFVSFtY9-pqtru2lGOUdSkCePPc9Gxuyn985QrPTjSFhaRbepaS1s1PYuG_nwSc28vLmvp3Hzuqda5NVOOOfGNwIqqMUnQjfK4ukxZbyL-28Y8BrEfyIWwRzRSyBrhYorP3-jq4-IdEbRXPtQIsM0XmQTakPqnb75UH6OmFHkM4IUQdsvyeITRuAKgYbNSnhJTcC6O7MZoYUyXTm4ad56gg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🤖
جایگزین رایگان و متن‌باز برای Claude، Cursor، Codex و سایر نمونه‌های مشابه.
✨
ویژگی‌ها:
•
💻
تولید کد برای وب‌سایت، اپلیکیشن و بازی در چند ثانیه
•
🆓
کاملاً رایگان؛ بدون اشتراک یا محدودیت پنهان
•
🌐
اجرای مستقیم در مرورگر؛ بدون نیاز به نصب
•
📝
فقط پرامپت بنویسید و کد آماده دریافت کنید
🌐
Site
#AI
#Coding
#OpenSource
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.87K · <a href="https://t.me/ArchiveTell/6603" target="_blank">📅 11:21 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6600">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/be7baa23f6.mp4?token=DLr-2wMbtaBPpB_PEJ60rqjWaUVq3DHNBl-xB6X41e-U62hKcXzciS_dw3Hq8ALV-KgAhZaIw9fbZSa_jqa-Tfvoad3LMiW-w4kjyXYKQXfIs9hH27L6rf9RanDB7RahaXiMKgF4c8GRiaUyB5r_gDPJSTj7XE0G5lqQy-qmV_pc4wi1LXQKtvcnDXy3dUP8Q1p_4lrCCsmp3eCY30E4hbTlHEMXIIS7yMKl1k6X78JFj_2WSQPLMyLdL1vAc4qraCv6YXy66IrqaTvZ8dG_3hyUv7Q88z2qB04xoazj2YdguyOyOBVOkrbnpWrjEZkaCRRACYNheUb3Ffo8BO5X-w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/be7baa23f6.mp4?token=DLr-2wMbtaBPpB_PEJ60rqjWaUVq3DHNBl-xB6X41e-U62hKcXzciS_dw3Hq8ALV-KgAhZaIw9fbZSa_jqa-Tfvoad3LMiW-w4kjyXYKQXfIs9hH27L6rf9RanDB7RahaXiMKgF4c8GRiaUyB5r_gDPJSTj7XE0G5lqQy-qmV_pc4wi1LXQKtvcnDXy3dUP8Q1p_4lrCCsmp3eCY30E4hbTlHEMXIIS7yMKl1k6X78JFj_2WSQPLMyLdL1vAc4qraCv6YXy66IrqaTvZ8dG_3hyUv7Q88z2qB04xoazj2YdguyOyOBVOkrbnpWrjEZkaCRRACYNheUb3Ffo8BO5X-w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">#اختصاصی
🔥
🔥
هر نوع رسانه‌ای را از تلگرام و حتی چت‌های خصوصی دانلود کنید
🤯
• دانلود صوت، پیام‌های صوتی، ویدئو، GIF از چت‌ها، استوری‌ها و حتی چت‌های خصوصی که دانلود در آن‌ها ممنوع است.
• پشتیبانی از دانلودهای چندگانه بدون کاهش سرعت.
• قوانین تلگرام را نقض نمی‌کند، می‌توانید با خیال راحت استفاده کنید.
🌐
GitHub
#Telegram
#Tools
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.29K · <a href="https://t.me/ArchiveTell/6600" target="_blank">📅 08:44 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6599">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">دریافت 7 میلیون توکن روزانه AI به صورت رایگان!
🎁
🤖
مدل‌های موجود:
• Mimo 2.5 Pro
• Mimo 2.5
• Mistral Large
• Mistral Medium 3.5
💻
کاربرد:
• ساخت وب‌ سایت
🌐
• ساخت ربات تلگرامی
🤖
• کدنویسی در ترمینال
⚙️
🔗
NaraRouter
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.98K · <a href="https://t.me/ArchiveTell/6599" target="_blank">📅 01:45 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6598">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">#اختصاصی
🔥
🚀
معرفی Metapi؛ هاب هوشمند و همه‌کاره برای مدیریت APIهای هوش مصنوعی!
🤖
✨
اگر برای دسترسی به مدل‌های هوش مصنوعی در سایت‌های مختلفی ثبت‌نام کرده‌اید، حتماً می‌دانید مدیریت ده‌ها API Key، چک کردن مداوم موجودی و تغییر دستی تنظیمات هنگام قطعی یک سرور چقدر کلافه‌کننده است. پروژه متن‌باز
Metapi
توسعه یافته تا به عنوان «پروکسیِ پروکسی‌ها» تمام این مشکلات را حل کند!
🔥
امکانات و ویژگی‌های شگفت‌انگیز این ابزار:
1️⃣
تجمیع تمام APIها (Aggregation):
شما ده‌ها کلید مختلف را به Metapi می‌دهید و این ابزار به شما
فقط یک API Key و یک Base URL واحد
می‌دهد. حالا می‌توانید این کلید واحد را در تمام برنامه‌های خود (مثل Open WebUI، Claude Code یا Cherry Studio) قرار دهید.
2️⃣
مسیریابی هوشمند (Smart Routing):
اگر سرور یکی از ارائه‌دهنده‌ها قطع شود یا مدل خاصی در آن گران باشد، به صورت خودکار درخواست شما را به یک سرور جایگزین، سالم‌تر و ارزان‌تر می‌فرستد (بدون اینکه شما متوجه قطعی شوید!).
3️⃣
دریافت اعتبار خودکار (Auto Check-in):
به صورت زمان‌بندی‌شده در سایت‌هایی که سهمیه رایگان روزانه می‌دهند لاگین کرده و اعتبار شما را به‌طور خودکار جمع‌آوری می‌کند.
4️⃣
حریم خصوصی ۱۰۰٪ و نصب آسان:
به راحتی با داکر (Docker) روی سرور یا سیستم شخصی شما نصب می‌شود و تمام داده‌ها فقط در دیتابیس محلی (SQLite) خودتان ذخیره می‌مانند.
5️⃣
سیستم هشدار پیشرفته:
در صورت بروز قطعی یا اتمام موجودی، از طریق تلگرام و ایمیل (SMTP) به شما نوتیفیکیشن می‌دهد.
⚡️
برخلاف پروژه‌های مشابه که برای تیم‌ها و فروش API طراحی شده‌اند، Metapi کاملاً برای
استفاده شخصی
بهینه‌سازی شده و رابط کاربری بسیار سبک و تمیزی دارد.
🔗
لینک مخزن گیت‌هاب:
🔵
@ArchiveTell
| Bachelor
⚡️
#AI
#API
#Metapi
#OpenSource
#Github
#SelfHosted
#Docker
#Tools
#OpenWebUI
#LLM
──────────────────────────────</div>
<div class="tg-footer">👁️ 2.08K · <a href="https://t.me/ArchiveTell/6598" target="_blank">📅 01:04 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6597">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">#اختصاصی
🔥
🚀
معرفی Awesome Android Root؛ گنجینه‌ای بی‌نظیر برای روت و شخصی‌سازی اندروید!
📱
✨
اگر به دنیای روت، کاستوم رام‌ها و دستکاری عمیق سیستم‌عامل اندروید علاقه‌مند هستید، مخزن
Awesome Android Root
یک دایرکتوری جامع و بی‌نظیر است که بیش از ۴۰۰ ابزار، اپلیکیشن و ماژول مخصوص دستگاه‌های روت‌شده را به همراه آموزش‌های دقیق در یک‌جا جمع‌آوری کرده است.
🔥
امکانات و ویژگی‌های کلیدی این لیست:
1️⃣
آموزش‌های قدم‌به‌قدم:
راهنماهای کامل و دقیق برای آنلاک کردن بوت‌لودر (Bootloader Unlocking) و نصب کاستوم ریکاوری‌ها (Custom Recovery).
2️⃣
پشتیبانی از جدیدترین متدهای روت:
پوشش کامل و معرفی ابزارها برای روش‌های مدرن روت سیستم از جمله
Magisk
،
KernelSU
و
APatch
.
3️⃣
کالکشن گلچین‌شده ماژول‌ها:
مجموعه‌ای از بهترین و کاربردی‌ترین ابزارها برای مسدودسازی تبلیغات (Ad-blocking) در سطح سیستم، اتوماسیون وظایف و شخصی‌سازی عمیق رابط کاربری اندروید.
⚡️
مشخصات فنی:
*
زبان:
Python (برای مدیریت و استخراج داده‌های لیست)
*
پلتفرم:
Android
🔗
لینک مخزن گیت‌هاب
🔵
@ArchiveTell
| Bachelor
⚡️
#Android
#Root
──────────────────────────────</div>
<div class="tg-footer">👁️ 2.02K · <a href="https://t.me/ArchiveTell/6597" target="_blank">📅 20:36 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6596">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">سلام
دوستان اگر به وایب کدینگ علاقه دارید یه نگاهی به این سایت بندازید:
https://risman.pro
برای ساخت محصولات فنی میتونه خیلی کمکتون کنه. (بدون نیاز به هیچ دانش نرم‌افزاری و برنامه‌نویسی)
امکان انتشار در دامنه خودتون هم بهتون میده.
با اولین لاگین حدود ۱۰۰ هزار تومان توکن هدیه میگیرید و اگر خواستید توکن بیشتری مصرف کنید میتونید از کد تخفیف welcome برای ۵۰% تخفیف تا سقف ۱ میلیون تومان استفاده کنید.</div>
<div class="tg-footer">👁️ 1.95K · <a href="https://t.me/ArchiveTell/6596" target="_blank">📅 19:12 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6593">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UDtXVJcVGLZ9AbHXrJGoNLCXa2pCy848axkS5AYNJWZUQ-Jb2DsGiXbD690XRsdIX7k65uUeYXfHyzwxq2PUD4XnuHR2aZzH9IlE48MCI2WEbuoC7mg-diNDNufUT2OgNkhQIeou3crIRwxK6VJUl3AD8sB9IO76mcP3PA9i2BTB0YGm6u9XYZnALIV-wcfEgJHx6cuXptN-ElnSWTi6Ycz_p6p3WsOWt99Jb3vOmIVR4MpkpuYX-eLFaX_R0VAAYu4GLw1D4g-pE_28Hw1Xg6Pm6H9DPkq0cbg-M-EmYh2yJGMNZDgpVv_NGYkAu53VkruL0kFvMNw1kSN0RS_FMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قابلیت ست کردن پراکسی لوکال
خیلیم ساده
مرورگر باحالیه
🔥</div>
<div class="tg-footer">👁️ 1.97K · <a href="https://t.me/ArchiveTell/6593" target="_blank">📅 15:56 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6591">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QJ3VMJTu_wXy7oSlGDYDkcWkob-4qh0DqfIojk_xwzhszcyf-4zZWj9e44WutFc0qPz-hUj0GtwkyMKDq8uORYz5cjoWaKIDfwGnDfbrhDcTh5zPkWJmnQ2IURHKURDX7onxPHzj6vz1zdbMuTRKpV4g4fotjGEoCsNdbXRRA5gmtWRgT_KmqkxIXNVIo3ILnp6I4ThiJQOg9PNoy7UbvUUiXLbuffQHE8NUTPY2K5UovsxrrlTBHei_7Q6OeNyCTqbdLIzCbCrOaoAC4SpdJyFQtudxsFZ5JT9Kd7lCMZcPP3snFA-d-_X8I4dm0utn7OS_D7TLPBQsnxnhDuMvkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
معرفی مرورگر Solipsism؛ وب‌گردی با طراحی منحصربه‌فرد و متمرکز بر حریم خصوصی!
📱
✨
اگر از ظاهر تکراری مرورگرهای موبایل خسته شده‌اید و به دنبال مرورگری خاص، قابل شخصی‌سازی و امن می‌گردید، اپلیکیشن Solipsism یک شاهکار در طراحی رابط کاربری است. این مرورگر اندرویدی…</div>
<div class="tg-footer">👁️ 1.81K · <a href="https://t.me/ArchiveTell/6591" target="_blank">📅 15:51 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6590">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">🚀
معرفی مرورگر Solipsism؛ وب‌گردی با طراحی منحصربه‌فرد و متمرکز بر حریم خصوصی!
📱
✨
اگر از ظاهر تکراری مرورگرهای موبایل خسته شده‌اید و به دنبال مرورگری خاص، قابل شخصی‌سازی و امن می‌گردید، اپلیکیشن
Solipsism
یک شاهکار در طراحی رابط کاربری است. این مرورگر اندرویدی با ایده خلاقانه "Rail-first" تمام کنترل‌ها و نوار آدرس را به جای بالا یا پایین، در یک نوار کناری (سمت چپ یا راست) قرار می‌دهد تا کار با گوشی‌های بزرگ با یک دست بسیار راحت‌تر شود.
🔥
ویژگی‌های شگفت‌انگیز این مرورگر:
1️⃣
طراحی نوآورانه (Rail-first):
قرارگیری منوها در نوار کناری با قابلیت تنظیم اندازه (از کوچک تا Super Compact) متناسب با اندازه دست و صفحه نمایش شما.
2️⃣
زبان طراحی Material 3:
رابط کاربری بسیار زیبا با گوشه‌های گرد، انیمیشن‌های روان، سایه‌ها و قابلیت هماهنگ‌سازی رنگ‌ها با تم سیستم‌عامل اندروید.
3️⃣
ابزارهای قدرتمند حریم خصوصی:
دارای مسدودکننده تبلیغات (Ad Blocker)، وب‌گردی ناشناس، کنترل کوکی‌ها و WebRTC، پاک کردن خودکار داده‌ها هنگام خروج، و یک قابلیت بی‌نظیر به نام
Decoy Mode
(تولید تاریخچه وب‌گردی جعلی برای محافظت از حریم خصوصی!).
4️⃣
امکانات کاربردی و سریع:
دارای اسکنر QR داخلی، قابلیت نصب مستقیم وب‌سایت‌ها به عنوان اپلیکیشن (PWA)، پخش تمام‌صفحه و بدون مزاحمت ویدیوها و ابزار دانلود حرفه‌ای.
5️⃣
صفحه خانگی شخصی‌سازی‌شده:
امکان تغییر والپیپر هوم‌پیج یا تنظیم آن روی حالت کاملاً تاریک و بی‌صدا.
﻿
⚡️
این مرورگر سبک که بر پایه WebView اندروید ساخته شده، تجربه‌ای کاملاً متفاوت، سریع و مدرن از وب‌گردی را به شما ارائه می‌دهد.
🔵
@ArchiveTell
| Bachelor
⚡️
#Solipsism
#Android
#Browser
#Privacy
#Material3
#AdBlocker
#WebDevelopment
#MobileApp
#TechTools
──────────────────────────────</div>
<div class="tg-footer">👁️ 1.82K · <a href="https://t.me/ArchiveTell/6590" target="_blank">📅 15:50 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6589">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">🚀
هوش مصنوعی دیگر کدهای شما را فراموش نمی‌کند؛ دستیار حافظه دائمی برای ایجنت‌های برنامه‌نویسی!
🧠
✨
اگر از پریدن کانتکست (Context) در چت با هوش مصنوعی و توضیح دادن‌های تکراری خسته شده‌اید، این ابزار جدید مشکل شما را حل می‌کند! به تازگی یک دستیار هوشمند برای مدل‌هایی مثل Claude، Codex و Cursor منتشر شده که دانش و اطلاعات پروژه شما را بین سشن‌های (Sessions) کاری مختلف حفظ می‌کند.
🔥
این دستیار چه کارهایی انجام می‌دهد؟
1️⃣
حفظ همیشگی کانتکست:
اطلاعات جلسات کاری شما را ذخیره می‌کند تا با بستن پنجره، کدهای شما فراموش نشوند.
2️⃣
یادگیری ساختار پروژه:
معماری، دایرکتوری‌ها و ویژگی‌های خاص کدبیس (Codebase) شما را کاملاً به خاطر می‌سپارد.
3️⃣
بسته‌بندی خودکار دانش:
اطلاعات جمع‌آوری‌شده را به صورت خودکار و هوشمند بایگانی و بهینه‌سازی می‌کند.
4️⃣
بازخوانی در کسری از ثانیه:
هر زمان که ایجنت به اطلاعات قدیمی نیاز داشته باشد، در کمتر از یک ثانیه آن را فراخوانی می‌کند.
5️⃣
پشتیبانی بسیار گسترده:
سازگاری کامل با
Claude Code
،
Cursor
،
Codex
،
LangGraph
،
CrewAI
و سایر ایجنت‌های هوش مصنوعی.
🔗
لینک دریافت و راه‌اندازی پروژه
🔵
@ArchiveTell
| Bachelor
⚡️
#AI
#CodingAgents
#Claude
#Cursor
#Codex
#LLM
#Memory
#ProgrammingTools
#DevTools</div>
<div class="tg-footer">👁️ 1.79K · <a href="https://t.me/ArchiveTell/6589" target="_blank">📅 12:31 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6588">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K4S5IWRkCY4MxQXIEVAN_azU3NLftTSERouwRWs3TOKG0TulrfeMK5mdlefx2hYU2nlFIMzoSvJ5rTLZSIm2DjGcKP4TB83tgwuKpthBSjnq2fLI8DhbNPrcHiA4er_lLgm3ZBNRAjosAuMmoQ0XkzHs0bj-lKGnke6eYPbioVDIV-bj9Dub2RzXdi58LDULCLGtsmPz6pcoUAcxrDoI9RX_22GSfJRYMnM9_XIkZbxJG30ISZ9qq7ZfbdAbs95WiwyPzP7R0ILD6b_Q5k903T9sihBJwlV9Tsum_GEwqQ3PXyRYyBVFC5AWm1n27qlmjN2V-IYdxuOZWJarVkFsEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دریافت 1T کانفیگ شخصی
🔑
🟢
از لینک زیر میتونین شروع به ساخت اکانت کنید :
➡️
sign up
بعد از ثبت نام وارد اکانت بشید و روی
Quick Subscription
کلیک کنید و داخل اپ هایی مثل :
Nekobox,hiddify,singbox و ...
اکسپورت کنین .
به دلیل نوع پروتکل یعنی AnyTls بودن فقط داخل اپ های ذکر شده میتونین اکسپورت کنین و داخل اپ هایی مثل V2ray کار نمیکنن
😬
خط های تست شده :
🛜
🛜
💬
@Archivetell</div>
<div class="tg-footer">👁️ 2.33K · <a href="https://t.me/ArchiveTell/6588" target="_blank">📅 12:10 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6585">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XqqihrvfL8nzsZOUC7cQlu3BHLYXqgZqFLy7exjM_BCK18N-9AmF2jLhBdRCM6H5kKoAb4gHSst2RlP6fwz9NwhugNxZjuZBbhB22kLAuqx7xLieJaLPKxr0Liqpq4Hi_xiD34Y2Nyw_0cSeMRsiBWf0QRVuxuEmognrNr9MeMxhUGk7oCsEBV-fycKxVMLV4zV2JvBMx4EQ4ZfoWlgo1oocf-i6uAmy8Z4jORXj7hV_Ecfw-qSbGUs3Yq0LWo7bzLybu8G1PQp9_Eq0dOIau-_Faug18PQp7sdylrPE9r-dxeUd-icDT1NnbPMAJet2RdQiIvLKNc7uOSxwD6Y1lg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FxtBkp562Tl72r4E8jlqsWmgYbJkD6pUqVzvMwzGcMvJlb7c_ByzsAfupEz__ePLooXyCZt7o6ByWBCSff26dEDt5l2CSe_FEctCPBvh8-72V2fEFdc4x_FKz_oGBL9AMUUP6xZYg7UUmwq9naiJLDbOKF6SzXX-PjrSP_oxHi96emD5_X5SysqeJnEbQKkkQWiFPprJgALulB3qC6rxh05kpg2-YHwk_cg29sitEPI2okTrZSojl2gKfURWSy-NrLJfyiSSuu0LBW2A-FY7Mgyjk3M-sOfzcfawIRxpkzkTSTsvhtzTPNfg33LPLEMf8rRS7SbTx7MJYvxoGAOCyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qoD48trLffs4vC4oOZfjYXQZKGwPmaBDP4wX6bMPuzriVumwVkqywl85Nklsv8S_Wfbsm5oIPkFgnqVTnBxhayYEph1jb6vEkY6m9ek2hw7Lgzjqe7YPcf4soYVt0qbli61ACUasMvl8EjSnJKyK79whAC4DNiTVqJOlJpJ_kisv11NEHXoHAM5pa4_aGvYmGudzUayuWP9wx3DCRjyp2A4HKfgtHVdi6aJMpW-shAaVczmrdRJCcp5iuk6Lf8jZv33Oat33Zkuyh3jT3QeGtN3717t10k3DPMHqX_fyk_pSS9f2nKOSw37F0wS1AT8pInhRID_xNBHeKkefIgNNNQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">تبدیل عکس‌های معمولی به شاهکارهای هنری با هوش مصنوعی
🔥
✨
قابلیت‌ها:
•
🎨
انتقال سبک هنری (مثل ون‌گوگ) به تصاویر شما
•
🪄
انتقال سبک بصری یک عکس به عکس دیگر
•
⚡
مبتنی بر شبکه‌های عصبی کانولوشنی و الگوریتم‌های پیشرفته
•
🛠️
رابط کاربری ساده و سریع برای ویرایش آنلاین
•
📦
بدون نیاز به نصب نرم‌افزار سنگین
🌐
Site
#AI
#Art
#Tech
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.96K · <a href="https://t.me/ArchiveTell/6585" target="_blank">📅 11:00 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6584">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Pw17u7OEYGAEyMprrleZ-tw48OkGprMBu8QWQQfePMKgEh21sHK8w0jL53zzboBQDS0lLEErDaRinV0QI7SoRuPg5bEgIg0vg4A_ScMDzuXk1BBN1jt8_VCIQ4HQLg9T913cFpaAD46Rq8fPRUCJ_vV20jQITjB_wLMbD-HfaHVVH9Afn3BOk0Uj5sd-K1M8fwujqPXL88CBkOfEd7lzQQOGSvPZ40SUToNi2-8zM8DX7YNNG9G9lofs75SnhbfgyGSyltePwJdksyROQSbfyv6H0jJsnxJABOaASKxyWmlwyXNasGW0yYknT6TeQGSd73E6qUzbGyQC1-INLBjzyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ویژه
🔥
🚀
معرفی Orcafile؛ ابزار جستجو و دسته‌بندی سریع فایل‌ها بر اساس پسوند!
📁
✨
اگر از گشتن در میان پوشه‌های درهم‌وبرهم برای پیدا کردن یک فایل خاص خسته شده‌اید، پروژه Orcafile دقیقاً برای شماست. این اپلیکیشن دسکتاپ و متن‌باز (Open-Source) به جای اینکه شما…</div>
<div class="tg-footer">👁️ 1.64K · <a href="https://t.me/ArchiveTell/6584" target="_blank">📅 09:43 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6583">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">ویژه
🔥
🚀
معرفی Orcafile؛ ابزار جستجو و دسته‌بندی سریع فایل‌ها بر اساس پسوند!
📁
✨
اگر از گشتن در میان پوشه‌های درهم‌وبرهم برای پیدا کردن یک فایل خاص خسته شده‌اید، پروژه
Orcafile
دقیقاً برای شماست. این اپلیکیشن دسکتاپ و متن‌باز (Open-Source) به جای اینکه شما را مجبور کند پوشه به پوشه بگردید، کل یک دایرکتوری (یا حتی یک درایو کامل) را اسکن کرده و تمام فایل‌ها را بر اساس پسوندشان (Extension) گروه‌بندی می‌کند.
🔥
ویژگی‌های کلیدی Orcafile:
1️⃣
اسکن فوق‌سریع:
قابلیت اسکن بیش از ۱۰۰ هزار فایل در پس‌زمینه بدون افت عملکرد سیستم.
2️⃣
مشاهده لحظه‌ای پیشرفت (Real-time):
نمایش لحظه به لحظه وضعیت اسکن فایل‌ها.
3️⃣
جستجو و فیلترینگ هوشمند:
جستجوی آنی نام فایل‌ها و فیلتر کردن دقیق بر اساس فرمت و پسوند.
4️⃣
دسترسی سریع:
امکان باز کردن مستقیم فایل‌های پیدا شده در فایل اکسپلورر ویندوز.
⚡️
مشخصات فنی و
پلتفرم:
توسعه‌یافته با ترکیب قدرتمند
Python
و
PyQt6
.
نسخه اجرایی (App) در حال حاضر فقط برای
ویندوز
منتشر شده است، اما از آنجا که پروژه متن‌باز است، با استفاده از سورس‌کد و دستورالعمل‌ها می‌توانید آن را در هر سیستم‌عاملی (مثل لینوکس و مک) اجرا کنید.
🔗
سایت پروژه
🔗
لینک مخزن گیت‌هاب:
🔵
@ArchiveTell
| Bachelor
⚡️
#Orcafile
#Python
#PyQt6
#OpenSource
#FileManagement
#WindowsApp
#Github
#Tools
#Productivity
──────────────────────────────</div>
<div class="tg-footer">👁️ 1.83K · <a href="https://t.me/ArchiveTell/6583" target="_blank">📅 09:41 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6582">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f93c42b223.mp4?token=j5HVJInUWeQg50RiIaqrFr5gPVL9_HqBaMcUstMvB54bJI5tk40mBzYz4IOqtwsR1X71Ytr0Ixk-R8Spu2NkgRMmo65l3H-DWefQxeve0DijAb46f4sfFXsIUJZEHKy12tjqdxKE9vP94_Vj7PXnOEvUvDiaO8Degugdx_aaQ9O3L1yQQePN8Hrf0tn3GHlRC08dCIKp2E4s3bAJwrgdGa_Z1mw6882BRaLY2clYVvSbwTgZouHL5mqkkBo6ep39dU6fDD0ut4SUtt0uJPHXfwotTdDXO2HVqmRV-4iS6-nYe7fUI1pZSa4uu9dIyJT9YrtMMIr00N_PlOsB256YLg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f93c42b223.mp4?token=j5HVJInUWeQg50RiIaqrFr5gPVL9_HqBaMcUstMvB54bJI5tk40mBzYz4IOqtwsR1X71Ytr0Ixk-R8Spu2NkgRMmo65l3H-DWefQxeve0DijAb46f4sfFXsIUJZEHKy12tjqdxKE9vP94_Vj7PXnOEvUvDiaO8Degugdx_aaQ9O3L1yQQePN8Hrf0tn3GHlRC08dCIKp2E4s3bAJwrgdGa_Z1mw6882BRaLY2clYVvSbwTgZouHL5mqkkBo6ep39dU6fDD0ut4SUtt0uJPHXfwotTdDXO2HVqmRV-4iS6-nYe7fUI1pZSa4uu9dIyJT9YrtMMIr00N_PlOsB256YLg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💻
JanAi
جایگزین محلی ChatGPT
این برنامه مستقیماً روی کامپیوتر اجرا می‌شود و نیازی به اتصال به اینترنت ندارد. می‌توان از مدل‌های زبانی مختلف برای متون، برنامه‌نویسی و سایر وظایف استفاده کرد.
🌐
Site
#AI
#OpenSource
#LocalLLM
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.08K · <a href="https://t.me/ArchiveTell/6582" target="_blank">📅 09:16 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6580">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XlKD-F5XN7WXyFx8oiG2z5qqqwUt1N_Uw944UIwCHgIK4dDNTgGH8SJkJB5jSD7cisN03mLuMbZGg42aEOP0FW6Ozl_mp_AUaZWYQ0IU6sEAnXqq2ypp-LKTqyat0sgH2yplwGXtU0DALUT4lMQGr-XlYIGkRW4EAyfKjfAq3FI6beWWOgsLJiHPmikWFnIWMSTjyEMpIHrlDSwCXm_fUvID_-z-5P8oX3HIJY6TZzBRDz3JbVncnlQ3IdGz6EZTe93NTaKJRYQyFddz0E8OeNlK732bNYEvu4NiZpJLUoyw8vnMz-Md0MPFjlCjtB9tLVzjwlYOQTAURpOSmdzDug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XaEyenfkStY4tAgltSpoT2IAji_fFsn6iO1AkA_a43TGvZaXw7h7uNahc-gRVVXpg9FnMS4nHLur_0KCj211VR1ykzJG-inAPrllHKKAwfOe-f39ysEovwjCha_-v0uXUAhym5FJiuY0ms4xxCycfh1t4gdusPw96OlUp_pjBH9CRy07pDf_FnzqKnlpkF_kJPDg_p8WBh5aHcQlMRUfwbftUwRNtQu7z7hhu1OZ_tBrYE9i0r42kQCxSAt1pNm7Dyy4cQH376mSO6kwwkHndaWb-Rz3r6QzrtnfQEn9cEsW5psQVY8mhhTGUYHWxpJhXpxMFXSjJwxFo0LRUB8-cA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">⚡️
«انجمن‌ها» به تلگرام اضافه می‌شوند — در نسخه آزمایشی برنامه چند ویژگی جدید پیدا شده که عملاً پیام‌رسان را به دیسکورد تبدیل می‌کند.
• در انجمن‌ها می‌توان چند گروه را در یک فضا ادغام کرد، چت‌های عمومی و خصوصی اضافه کرد و همچنین دعوت‌نامه‌ها را به آنجا ارسال کرد.
• همچنین می‌توان کانال‌ها را به انجمن‌ها اضافه کرد، اما این ویژگی هنوز فعال نشده است.
تاریخ انتشار به‌روزرسانی بعدی هنوز اعلام نشده است.
#Telegram
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.85K · <a href="https://t.me/ArchiveTell/6580" target="_blank">📅 08:56 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6579">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">طراحی وب و اپلیکیشن در یک ثانیه با ابزار جدید GenSpark
🚀
✨
قابلیت‌ها:
•
🔹
تحلیل مستقیم فایل‌های Figma، عکس و کد
•
⚡
تولید طرح نهایی بدون نیاز به کدنویسی دستی
•
🛠️
دسترسی به قالب‌های آماده برای وب و موبایل
•
📦
ساخت رایگان نمونه‌کار برای فریلنسرها
🌐
Site
#AI
#WebDesign
#GenSpark
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.03K · <a href="https://t.me/ArchiveTell/6579" target="_blank">📅 00:06 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6577">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SmMbbabL0B50HUrV7oWvbPyo3MEliek3ZghbiG0qZTBk5s9trycUQj_-AqtxMzWncR8k9667cwwcS5K2AcKAR4sfaxHHUVGiOh31atmVkbhz1Qk6NczI-CU9PBDpTf7q01S9yd2uqhTacsXlBpEvDbs742OiJyukvCcDOFm4UmVI8XLeRQ5dPDq74PC1NBDlz2RWMDGHlKgcOPiORdQjK1h_Xm9hGIxEuWAWCCcd45OsU-J2N3rDv6FPEeQlC6PIpWaXlR0YS6csAbXP0QGKV0aU1reX2AtEu-5dqw2cABzLJLS8P7HrorIu-gB_V5aJF0naJQdK966Kqo4IDghtpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎧
انگلیسی رو تو حرکت، باشگاه یا پیاده‌روی تقویت کن!
با این ۵ پادکست، بدون کتاب‌های خسته‌کننده به گفتار زنده عادت می‌کنی:
•
🇺🇸
American English Podcast
: انگلیسی آمریکایی، فرهنگ ایالات متحده و مکالمات واقعی.
•
🧠
English Learning for Curious Minds
: داستان‌های جذاب درباره علم، کسب‌وکار و زندگی.
•
⏰
6 Minute English (BBC)
: قسمت‌های کوتاه با واژگان جدید، اصطلاحات و موضوعات روز.
•
🗣️
The English We Speak
: عبارات مدرن، زبان عامیانه و اصطلاحات مکالمه‌ای.
•
🇬🇧
Luke's English Podcast
: تحلیل زبان و فرهنگ بریتانیایی، یکی از معروف‌ترین‌ها.
#EnglishLearning
#Podcast
#Language
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.97K · <a href="https://t.me/ArchiveTell/6577" target="_blank">📅 22:06 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6574">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/q0woHmT1v1iw-bLnu4YcRdQ4vPYs6id7UIyo7iD2JTOJqZfaTMvZegKwbeTNFtu0WaWrwBypecb8mr46kenKnsIDp8Q9QYiAm_eHeFlVP48Aa_bGmcONfx30uzVm9B-UAvvARGmcw4Nmn5JDzKGuTlfDMmlarIyMQgBM2ovFZlgt3-BBeFhUxIgB4cE1TejksLWqZ9mxvA3wJ27fHawkCnE_awZKH6XQhthuj_13lJdKdyQ113f4TSkz0-zFmI9pPKDxkHKUvvaoS2FmGk5PFL4IYNUxp4F7fown9eRyeJirTjMiaeA4yxDrzXKfZDX509eEzVTj9h3VqvY_8xF9FA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mbWcrfR3QOAA2qm6iAdECW8KGqZO4vhvLV75FoRKOgakPC2JmyjiFEOY6ABdsBMDDB0vTVkBH8cc3KTjHJLoYjuKKQOFXtzKSzSSkh_aK_XciC85YBBTb2yWjMVbGQlrx31AnkG5Npu5uR-rr6lsFgRndIVYra1Q1aFu4H7uNwjaZpoJHO1SKvwCVkN_x_vYxI3-EFiJuUEljQmlN8s2t9UaXbliQRaXA978_SfAxg2ZWYxHffKKvzO32ARmhJug-qtaUDx0E2ddWqUXEWmFN55VnYM3YcGrAh8tIrf5ibdtFYrDVtAATeswohcoNFcneBxv8WJhrl6Z0POxUKnWEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FLbukxW99DNqACaF63AV0E7iMjBErccVpMQJbPiLkiQojPtgKZ6D29ovBxlLr49iN8XQgjk_pAC71G6TRUE_QbsdsRsv1AG5l3N3TFvKnNffvs0UvJ21w54m6pJDBscvD_oBVcPw9dbA7aZRMIQ07N2S7NlENoxU_MuCr4Evm4RSY6OLRNIEZ5mkVKrR0tgiLTlPDNhsrgy-_-Va0_Rwr81CQ9S2Nm80wbMC_a8Fnt-JpKFGl3uJTxH9otw21_eUxrC4R9NjsVqN8CCWozLIrNCTEjMuvk231g3WWVlwIiCspjzY77B3oF5MOcGdDhOwkOLHojSGZR7FTf4FBMdmAA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🔥
OpenAI
مدل جدید GPT-5.6 Sol را معرفی کرد؛ مدلی که در چند بنچمارک مهم، حتی از رقبای مطرح هم جلو زده و تمرکز اصلی‌اش روی کارهای پیچیده و توسعه نرم‌افزار است.
💻
🧠
•
🔹
عملکرد بهتر در بنچمارک‌هایی مثل Terminal-Bench 2.1
•
⚡
توانایی کار مداوم روی پروژه‌ها برای ساعت‌های طولانی
•
🛠️
مناسب‌ برای توسعه نرم‌افزار با دخالت کمتر انسان
•
📦
معرفی مدل‌های سبک‌تر و ارزان‌تر Terra و Luna در کنار Sol
🌐
Site
#AI
#OpenAI
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.88K · <a href="https://t.me/ArchiveTell/6574" target="_blank">📅 21:44 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6573">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">الان برای API بهترین
aerolink
هست که بهتون
opus 4.8
میده
خیلی ساده
لینک ثبت نام
نحوه ثبت نامش دقیقا مثل
freemodel
هست طبق این
پست
نحوه اجراش روی
claude code
هم همونه فقط تنظیمات رو این بزنید
هر ورژنی از claude code هم بزنید قبوله
{
"env": {
"ANTHROPIC_API_KEY": "کلید",
"ANTHROPIC_BASE_URL": "https://capi.aerolink.lat/",
"CLAUDE_CODE_DISABLE_NONESSENTIAL_TRAFFIC": "1"
},
"permissions": {
"allow": [],
"deny": []
},
"apiKeyHelper": "echo 'کلید'"
}
لیمیتش هم دقیقا مثل
freemodel
هست
فقط مشکل اینه هر ip ایی تو claude code قبول نمیکنه باید تست کنید
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.65K · <a href="https://t.me/ArchiveTell/6573" target="_blank">📅 21:01 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6571">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromAssa</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fa1ffe541d.mp4?token=vMCN9vhcX--WCtLHRDsz--pJ-42sIzSu7b1sPSczbB-u6tkFsQfNUxkAw9zm2YB-AOuOhQjdcoFqpygH9mBCG22qaGLlnVutTXuz3-67Sd5zteaQUeWii6nlvVg2PPyOATSEWrRGnkxFHsvTvgg0iuiN5fIJB31-bKqXD6p0UWmPL8MC8k0JypyuonIrmEN8vq4mf7rOt4VHywvvOUSSY_HNiImQFKgnWErgd72p7JhQ6jFWFGNIBht97p-KnZV9s7V9k25Yi8_cRNWaCUZB85NhikwHGXBh2Ja8uAqPg2jIa7-jnzVQ3iHRxHaDRhhwcUm8RfEd0u7kyk3o7xj74oAoobD_PgS3t1sl_1cIqsGajs8bLj4tuL7P1oxg97RVNQMjHqbanUnXj-N_ARttxVZcGBPyk7AQL_9Fn8XR_HLYu6Hj5HXq6BROSKjh8Z-4pB6D1oFSJpcso4YgokRrLzltQMPruNlFFNTZt_iuZ1iGC_9gJxfqS2hLkyKTGdEJYc4BCtOxA6m6DDT5v7I9RVX4P2o8fyQwJq1CL28OCVMG793WWTIrpR9Xh4DlqCWsWchgNCWnUzyXTeCIiUE1OvZZAzJ3lBh2V7pZ72OPKxCxugo_KorPgk3VREvQGckjeWFCwG0IXlXNz-xxIZWqOrlxIl4KEHYksoeTytlsH8c" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fa1ffe541d.mp4?token=vMCN9vhcX--WCtLHRDsz--pJ-42sIzSu7b1sPSczbB-u6tkFsQfNUxkAw9zm2YB-AOuOhQjdcoFqpygH9mBCG22qaGLlnVutTXuz3-67Sd5zteaQUeWii6nlvVg2PPyOATSEWrRGnkxFHsvTvgg0iuiN5fIJB31-bKqXD6p0UWmPL8MC8k0JypyuonIrmEN8vq4mf7rOt4VHywvvOUSSY_HNiImQFKgnWErgd72p7JhQ6jFWFGNIBht97p-KnZV9s7V9k25Yi8_cRNWaCUZB85NhikwHGXBh2Ja8uAqPg2jIa7-jnzVQ3iHRxHaDRhhwcUm8RfEd0u7kyk3o7xj74oAoobD_PgS3t1sl_1cIqsGajs8bLj4tuL7P1oxg97RVNQMjHqbanUnXj-N_ARttxVZcGBPyk7AQL_9Fn8XR_HLYu6Hj5HXq6BROSKjh8Z-4pB6D1oFSJpcso4YgokRrLzltQMPruNlFFNTZt_iuZ1iGC_9gJxfqS2hLkyKTGdEJYc4BCtOxA6m6DDT5v7I9RVX4P2o8fyQwJq1CL28OCVMG793WWTIrpR9Xh4DlqCWsWchgNCWnUzyXTeCIiUE1OvZZAzJ3lBh2V7pZ72OPKxCxugo_KorPgk3VREvQGckjeWFCwG0IXlXNz-xxIZWqOrlxIl4KEHYksoeTytlsH8c" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تو بخش انتخاب پنل ۴ تا انتخاب وجود داره
طبق تجربه نوا و زئوس پنل های خوبین</div>
<div class="tg-footer">👁️ 1.68K · <a href="https://t.me/ArchiveTell/6571" target="_blank">📅 20:41 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6570">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">🚀
معرفی Cloud WZA
با Cloud WZA مدیریت سرور و ساخت کانفیگ‌های کلود ساده‌تر از همیشه شده است!
🤖
یک ربات تلگرامی قدرتمند برای ساخت کانفیگ و مدیریت سرویس‌ها، با امکان دیپلوی سریع پنل‌های محبوب:
⚡
Nova
⚡
Zeus
⚡
BPB
⚡
Nahan
فقط با یک دکمه پنل موردنظر خودت را دیپلوی کن و بدون دردسر شروع به استفاده کن
✅
✨
امکانات Cloud WZA:
🔹
ساخت و مدیریت کانفیگ کلود
🔹
دیپلوی خودکار پنل‌ها
🔹
مشاهده میزان مصرف کاربران
🔹
ساخت کاربر جدید
🔹
مدیریت کاربران
🔹
تغییر رمز عبور
🔹
مدیریت آسان و سریع از داخل تلگرام
Cloud WZA؛ راهی ساده، سریع و هوشمند برای مدیریت سرویس‌های کلود
☁️
🚀
🤖
ربات:
@nova_wzabot
ــــــــــــــــــــــ
توسعه داده شده توسط AssA
✨
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.55K · <a href="https://t.me/ArchiveTell/6570" target="_blank">📅 20:40 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6569">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/93b5316c72.mp4?token=FEbGw2dU3yr5gHdL6L7vupDr7hLQeb6mtdCC8aErA8Fk-ddO2dPAVs41av0OPBl3wmy9MZEWH9JHLI-cWBeYW_fM8VftuEQHcHQpOI1JPTEWRodmgBj2Yp59aoMtA5XImAFxn3ED6wqH3qwcQSZOP2niW-TPG-oNnfbzCzelTSMwfaY5NnSt3_iKSHpjstu5Clz0QwW9p9BOmde_InkhWiUqGYMlmX3YKzAFBdUFtYFKkPIKEQ3osHofiO8Gqj-RQU6eB4wmdIi221hm27SRvmkbhoFNRFYwUrIcftN71DJ2PVQ5CfXzsaVZLhSvCQzpKT-hkxpPnc_zZGUHvhHQfg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/93b5316c72.mp4?token=FEbGw2dU3yr5gHdL6L7vupDr7hLQeb6mtdCC8aErA8Fk-ddO2dPAVs41av0OPBl3wmy9MZEWH9JHLI-cWBeYW_fM8VftuEQHcHQpOI1JPTEWRodmgBj2Yp59aoMtA5XImAFxn3ED6wqH3qwcQSZOP2niW-TPG-oNnfbzCzelTSMwfaY5NnSt3_iKSHpjstu5Clz0QwW9p9BOmde_InkhWiUqGYMlmX3YKzAFBdUFtYFKkPIKEQ3osHofiO8Gqj-RQU6eB4wmdIi221hm27SRvmkbhoFNRFYwUrIcftN71DJ2PVQ5CfXzsaVZLhSvCQzpKT-hkxpPnc_zZGUHvhHQfg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">KREA.AI
Enhancer
تصاویر پیکسلی را تا 22K ارتقا دهید!
دیگر نگران کیفیت پایین عکس‌هایتان نباشید؛
KREA.AI
با ابزار قدرتمند Enhancer خود، تصاویر بی‌کیفیت را به وضوح خیره‌کننده تبدیل می‌کند.
🖼️
✨
✨
قابلیت‌ها:
•
🔹
ارتقاء کیفیت تصاویر تا وضوح 22K
📈
•
⚡
تبدیل پیکسل‌های بی‌کیفیت به جزئیات واضح و شارپ
🔍
•
🛠️
استفاده آسان و سریع برای نتایج حرفه‌ای
🚀
🌐
Site
#AI
#ImageEnhancement
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.61K · <a href="https://t.me/ArchiveTell/6569" target="_blank">📅 20:00 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6568">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rjfj4O0FUjKZ-HIuXTSStedc4DvjRiT-iDIx2wNk7QvLVeXQGd9jOrz-IMLe2yd8dyUYl5R9tYKAfguMEcZgNbVYVleTCvX1UWnWw5X1CIiY2vavecjVA_mcARKAK-Fkw74bcUxH1ScBx1T338c0ljPer0K_rjbjVbpDLrsz7ZdBJbly2KOSipa2YEszRtWLzqNlcX7Mt9VuWF-SQJlCNW4_TZxseAPgsEZ6vuhLwrwgSDGwSWlu-30iceKvX7WjRF4zs2loznG6A2wFeFZA7-exCN8XWVWjAgZ8Tm_b606VEmL30Jvv_K-hkeawm_eOcNhYo5XxeZ4TM-u_BO5Mpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">1000 برنامه رایگان برتر برای آیفون و کل اکوسیستم اپل: یک دانشنامه واقعی از نرم‌افزارهای مفید در گیت‌هاب ساخته شده است!
🍏
در این مجموعه همه موارد ضروری پیدا خواهید کرد: از پیام‌رسان‌های امن گرفته تا ابزارهایی برای تماشای فیلم از طریق تورنت.
🎬
🔐
🌐
GitHub
#Apple
#iPhone
#FreeApps
#GitHub
#OpenSource
#Productivity
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.65K · <a href="https://t.me/ArchiveTell/6568" target="_blank">📅 19:20 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6567">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b9395cb697.mp4?token=PWc7o1dc1_e13iCSgbKCev_V4R88E15DncVQG28iEXHMEkw8RotKZ1c6H4suFRwb9SeU8DcWqa2CKM12INgnSVI2SfiWiK0LY8YUzzOTPP-I1tOyHsTUGRb-dXtvUKB6-UHK815bJDhnyR7-wnwbYur884gE0NhF-u4TVaGW3J79Rmuf0fG-xUtVXUi9exhboxZE4tm__GtClXm-peyQNbZBMrAUKaNLFpmJLAj5LI6fyoRYsEH8DUGBHurBy2YR9Wnv8GzNza4yyMa32FEOpJB5p5ywzQmtsnF_1ppv1jmxlkOJ32Blene71aJzbqQIq6E2OY7hvAk2z7Wl4zEnHA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b9395cb697.mp4?token=PWc7o1dc1_e13iCSgbKCev_V4R88E15DncVQG28iEXHMEkw8RotKZ1c6H4suFRwb9SeU8DcWqa2CKM12INgnSVI2SfiWiK0LY8YUzzOTPP-I1tOyHsTUGRb-dXtvUKB6-UHK815bJDhnyR7-wnwbYur884gE0NhF-u4TVaGW3J79Rmuf0fG-xUtVXUi9exhboxZE4tm__GtClXm-peyQNbZBMrAUKaNLFpmJLAj5LI6fyoRYsEH8DUGBHurBy2YR9Wnv8GzNza4yyMa32FEOpJB5p5ywzQmtsnF_1ppv1jmxlkOJ32Blene71aJzbqQIq6E2OY7hvAk2z7Wl4zEnHA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یک برنامه‌نویس جوان توانست با ترکیب علاقه و مهارتش، درختی که با پایتون کدنویسی کرده بود را به قیمت 8 هزار دلار بفروشد. این پروژه از 100 دلار شروع شد و در چند روز به این قیمت رسید
🤯
#Python
#Programming
#Business
#DigitalArt
#Success
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.71K · <a href="https://t.me/ArchiveTell/6567" target="_blank">📅 18:42 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6566">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">🚀
آموزش اجرای Opus 4.8 در ترمینال با Claude Code توسط Agentrouter
1️⃣
ثبت‌نام در Agentrouter
وارد سایت
Agentrouter
شوید
با حساب Github ثبت‌نام کنید
بعد از ورود، صفحه احراز هویت نمایش داده می‌شود:
🎉
شما 125 دلار کریدیت گرفتید
2️⃣
ساخت API Key
وارد سایت شوید
از منو بروید به بخش
API Token
یک API Key جدید بسازید و ذخیره کنید
3️⃣
نصب Termux (روی موبایل)
📱
اگر موبایل دارید، از Termux استفاده کنید
4️⃣
دستورات نصب در ترمینال ( به ترتیب وارد کنید )
1⃣
آپدیت Termux
pkg update && pkg upgrade -y
2⃣
نصب ابزارها
pkg install proot-distro nano -y
3⃣
نصب Ubuntu
proot-distro install ubuntu
4⃣
ورود به Ubuntu
proot-distro login ubuntu
5⃣
آپدیت Ubuntu
apt update && apt upgrade -y
6⃣
نصب ابزارهای ضروری
apt install -y sudo ca-certificates curl wget git nano gnupg lsb-release build-essential python3 make g++
apt install -y curl nano nodejs npm
curl -fsSL https://deb.nodesource.com/setup_22.x | bash -
apt install -y nodejs
7⃣
نصب Claude Code فیلترشکن بزن
npm install -g @anthropic-ai/claude-code@2.1.167
8⃣
تنظیمات Claude Code
mkdir -p ~/.claude
دستور زیر را برای باز کردن فایل تنظیمات بزنید:
nano ~/.claude/settings.json
کد زیر را داخل فایل پیست کنید (کلید خود را جایگزین کنید) و با زدن Ctrl + X و سپس y و در نهایت Enter ذخیره کنید:
{
"env": {
"ANTHROPIC_API_KEY": "کلیدت",
"ANTHROPIC_BASE_URL": "https://agentrouter.org/",
"CLAUDE_CODE_DISABLE_NONESSENTIAL_TRAFFIC": "1"
},
"permissions": {
"allow": [],
"deny": []
},
"apiKeyHelper": "echo 'کلیدت'"
}
▶️
اجرای Claude Code ( با فیلترشکن خوب وارد شوید )
claude
✨
حالا آماده استفاده است
🚀
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.86K · <a href="https://t.me/ArchiveTell/6566" target="_blank">📅 18:00 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6565">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">🚀
دسترسی رایگان به API غول‌های هوش مصنوعی!
با لینک زیر به جدیدترین مدل‌ها دسترسی پیدا کنید:
🔹
GPT 5.4
🔹
Claude Sonnet 4.6
✅
سازگار با همه پلتفرم‌ها:
ربات تلگرام ، وب‌سایت ، Codex و Claude Code
🔗
zyloo.io
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.89K · <a href="https://t.me/ArchiveTell/6565" target="_blank">📅 17:01 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6564">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9a86123e61.mp4?token=MZlvqjno5vF6Nzt29myqqlfcFYfP9mIxqH2YZ3D741nBlpWc-qdSfDmOWNmIrAf5xSB4bqhqc7LD6t5htke5NT3Ye8iIIgyme-J64VsUnw5T7S3qQkb2OqmXmldMEab1X2uODTheNTGHOyRrpA_DEgoLsMOXPdS8MUwMIX96Ca351Zik5gf-3g_d-oOLTB4NJnWsJCofMVrCyuRKdGLOUKNgX9FNoyRYqnjnTqi0ab8jiMoYxNKzCzBAIEaSLMizvRd86cUib46m-zsxtXT3e4F-P0Xver7sami3Wurhw9av7C7_OrU7B0EYGB37R3XxRZGCpt3l-hBf_U5qdUmGXw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9a86123e61.mp4?token=MZlvqjno5vF6Nzt29myqqlfcFYfP9mIxqH2YZ3D741nBlpWc-qdSfDmOWNmIrAf5xSB4bqhqc7LD6t5htke5NT3Ye8iIIgyme-J64VsUnw5T7S3qQkb2OqmXmldMEab1X2uODTheNTGHOyRrpA_DEgoLsMOXPdS8MUwMIX96Ca351Zik5gf-3g_d-oOLTB4NJnWsJCofMVrCyuRKdGLOUKNgX9FNoyRYqnjnTqi0ab8jiMoYxNKzCzBAIEaSLMizvRd86cUib46m-zsxtXT3e4F-P0Xver7sami3Wurhw9av7C7_OrU7B0EYGB37R3XxRZGCpt3l-hBf_U5qdUmGXw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😮
Morflax Mesh — تصاویر سه‌بعدی در مرورگر
این سرویس امکان ساخت تصاویر سه‌بعدی را در چند ثانیه فراهم می‌کند. عناصر را بکشید و رها کنید، فرمت‌ها را تغییر دهید، رنگ‌ها و نورپردازی را تنظیم کنید — همه چیز مستقیماً در مرورگر کار می‌کند.
تعرفه پایه رایگان است و دانلودهای نامحدود دارد. با پرداخت ۸ دلار در ماه، به کتابخانه سه‌بعدی، خروجی با کیفیت بالا (.jpg و .png) و قالب‌های آماده دسترسی پیدا می‌کنید.
🌐
Site
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.86K · <a href="https://t.me/ArchiveTell/6564" target="_blank">📅 16:00 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6563">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HW7Hwi_wqUVw0PnCDOTLye3Pe4WYPycoStNqZemATV5s61GDbiXwxi3NvqGfzpC6inG6QKFScegUCqew1zp-OxTdwqtQ0uykd4rbse7vtG7ycpljdlTd6k93F5CFYSXIcbp0TvYSRLTVEtCyXa_CKCOaG9MXcgk8yzVfmXIApJED1Kkha3L1FDGZ4zYb0ZUVZRYFaqcP7mqVn-pe3OuK6Xpt7ssOniH3j-FK5bTbuhx6OntADiFucLGatL5EB3r4bKQjGEKqotW6or0dApv2qXpAffpXMENLphuRf_Kq8gxQdgxb-WcoRo4RtKhzPdgiaIoRaA9V8BBM0gW3FHyjyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
یه ترفند خفن برای چند برابر کردن سرعت گوشی‌های سامسونگ!
احتمالاً شما هم فکر می‌کنید هرچی مقدار RAM بیشتر باشه سرعت گوشی بالاتره، اما یه گزینه‌ای تو گوشی‌های سامسونگ هست به اسم RAM Plus که به صورت پیش‌فرض روی همه مدل‌ها فعاله و برخلاف اسمش، تو خیلی از مواقع باعث لگ و کندی اعصاب‌خردکن میشه!
🤦‍♂️
🧐
اما چرا این اتفاق میفته؟
قابلیت Ram Plus در واقع میاد بخشی از حافظه داخلی گوشی رو به عنوان «رم مجازی» اشغال می‌کنه تا برنامه‌های بیشتری تو پس‌زمینه باز بمونن. از اونجایی که سرعت حافظه داخلی به مراتب از رم فیزیکی (سخت‌افزاری) خود گوشی پایین‌تره، وقتی سیستم می‌خواد اطلاعات رو بین این دو جابجا کنه، پردازنده بی‌دلیل درگیر میشه و گوشی کُند میشه.
🛠
چطوری غیرفعالش کنیم تا گوشی پرواز کنه؟
کافیه وارد تنظیمات گوشی بشید و دقیقاً این مسیر رو برید:
⚙️
Settings > Device Care > Memory > RAM Plus
(اگر منوی گوشیتون فارسیه: تنظیمات > مراقبت از دستگاه > حافظه > رم پلاس)
گزینه بالای صفحه رو روی حالت Off (خاموش) قرار بدید.
بعد از این کار گوشی ازتون می‌خواد که یک بار ری‌استارت بشه)
✅
🆔
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.73K · <a href="https://t.me/ArchiveTell/6563" target="_blank">📅 15:42 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6562">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">🚀
معرفی MinerU؛ استخراج جادویی و سریع متن از انواع فایل‌ها!
📄
✨
اگر برای پروژه‌های هوش مصنوعی (مثل RAG)، کارهای تحقیقاتی یا روزمره نیاز به استخراج متنِ تمیز از فایل‌های مختلف دارید، ابزار رایگان و متن‌باز
MinerU
یک شاهکار به تمام معناست!
🔥
ویژگی‌های شگفت‌انگیز این ابزار:
1️⃣
پشتیبانی همه‌جانبه:
تبدیل فایل‌های PDF، Word، Excel، PowerPoint و حتی اسناد اسکن‌شده به متن خالص و بدون به هم ریختگی.
2️⃣
سرعت پردازش خیره‌کننده:
می‌تواند یک فایل PDF دویست صفحه‌ای را در کمتر از ۱.۵ دقیقه پردازش کرده و متن آن را استخراج کند!
3️⃣
اجرای کاملاً محلی (Local):
بدون نیاز به اینترنت و سرورهای ابری روی کامپیوتر خودتان اجرا می‌شود که برای حفظ حریم خصوصی فایل‌های حساس بی‌نظیر است.
4️⃣
بهترین دوست هوش مصنوعی:
پشتیبانی از پردازش گروهی فایل‌ها (Batch) و قابلیت ادغام و همگام‌سازی بی‌نقص با ایجنت‌های هوش مصنوعی مانند
Claude
،
Cursor
و سایر LLMها.
🔗
لینک مخزن گیت‌هاب
🔵
@ArchiveTell
| Bachelor
⚡️
#MinerU
#PDFExtractor
#OCR
#AI
#Claude
#Cursor
#OpenSource
#Github
#Tools
#RAG
──────────────────────────────</div>
<div class="tg-footer">👁️ 1.82K · <a href="https://t.me/ArchiveTell/6562" target="_blank">📅 15:37 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6561">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rf6AkrZpvdSQOoBvHpGJJ8PiZ5kKo9Se5KUcFht9DB8VRZvdCldN3D_qPoL60XHVjXZGqKhY08CxkOL3fO1orHbBtmEVL6feqimPVp982Iwf_wZMO42s90gFQ-ULckKOvuc_fGE_WoxJda295SwKmDNh_HnmbhOoXPvLlBNHVQGsb_gT4BFVHK4KN8n8gtVRXXXDsSnxJZfQuvUJXW9pU9sPoMUTDiYEBzzIteUrHUSPYYCiQYAAt-CXWdM_Ps8vzdArSBMzDanlb2CorfaO9nL7fQleLiUmsDjfWBt2clB3Sgy6bcLhXuSedcn-l9MLdDSGOrjxXvuHOYLrZL_PeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Popit Music: ساخت موسیقی با هوش مصنوعی و مالکیت کامل اثر
🎵
✨
قابلیت‌ها:
•
🔹
انتخاب ژانر و حالت برای تولید سریع ترک
•
⚡
ورود خودکار به پلی‌لیست و رقابت با آثار دیگر
•
🛠️
مالکیت کامل حقوق موسیقی متعلق به شماست
•
📦
دو بار تولید رایگان برای شروع
🌐
Site
#AI
#Music
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.95K · <a href="https://t.me/ArchiveTell/6561" target="_blank">📅 13:43 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6560">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">🚀
معرفی droidMirroring-mac؛ تجربه اکوسیستم اپل برای کاربران اندروید در مک!
📱
💻
✨
اگر از گوشی اندرویدی استفاده می‌کنید اما کامپیوتر شما Mac (سیستم‌عامل macOS) است، احتمالاً همیشه حسرت قابلیت یکپارچگی عمیق اکوسیستم اپل (مثل iPhone Mirroring و Handoff) را خورده‌اید. پروژه جدید و متن‌باز
droidMirroring-mac
دقیقاً برای حل همین مشکل و پر کردن این خلأ توسعه یافته است!
🔥
ویژگی‌های جذاب این ابزار:
1️⃣
انعکاس صفحه (Screen Mirroring):
مشاهده و کنترل کامل گوشی اندرویدی مستقیماً از روی صفحه نمایش مک (دقیقاً شبیه به قابلیت جذاب iPhone Mirroring در نسخه‌های جدید macOS).
2️⃣
کلیپ‌بورد مشترک (Universal Clipboard):
همگام‌سازی بی‌وقفه کلیپ‌بورد بین گوشی و مک؛ متنی را در اندروید کپی کنید و در مک Paste کنید (و بالعکس).
3️⃣
رایگان و متن‌باز:
این پروژه کاملاً Open-Source است و بدون نیاز به خرید اشتراک یا برنامه‌های تجاری گران‌قیمت، ارتباطی عمیق بین دو اکوسیستم متفاوت ایجاد می‌کند.
اگر به تازگی از آیفون به اندروید مهاجرت کرده‌اید ولی نمی‌خواهید راحتیِ کار با مک را از دست بدهید، این پروژه گیت‌هابی یک معجزه برای شماست!
🔗
لینک مخزن گیت‌هاب
🔵
@ArchiveTell
| Bachelor
⚡️
#Android
#macOS
#ScreenMirroring
#Productivity
#OpenSource
#Github
#Tools
#Handoff
──────────────────────────────</div>
<div class="tg-footer">👁️ 2.11K · <a href="https://t.me/ArchiveTell/6560" target="_blank">📅 08:35 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6559">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cX7gIvkoPJ-qAlddMm6VcJjsm2nbZF6nyKUbqysCTo7UsCKr76IM6mwBpK94hZftJrFSZqjis2U-d3hPatk6nKRdjRt1sQkrInpI4hlvc41jqywDHkjCb_J79fC5bik2H0HijqfZ6FMMnvLWvs1FF18Bfcra3SplUfku4iZQdWVw95oDb4rIyzWw3Eqdoz8dENrrpCG_5pAjEI7mKJFQDbGJ-Uf6UfZE4oE9kiKTWoydKtyom6IHSoPFIlXoCdSEoPlhDHxgTJ99q3pIwZCeuvNMz5qar9NRMFtrnvJMHdcx5-aUzxpP3PHvgbndb2ZXjTIuEwyz7gxcJvySEJRYOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">> توسعه‌دهنده‌ای با نام مستعار slqnt نسخه وب بازی افسانه‌ای Half-Life 2 را معرفی کرد.
اکنون می‌توانید این شوتر افسانه‌ای را مستقیماً در مرورگر اجرا کنید، بدون نیاز به نصب برنامه‌ها یا راه‌اندازها.
بازی پایداری شگفت‌انگیزی را نشان می‌دهد و کاربران در حال آزمایش پروژه‌هایی مانند
Ravenholm
و
City-17
در مرورگر هستند!
🌐
Site
#HalfLife2
#WebGame
#Gaming
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.3K · <a href="https://t.me/ArchiveTell/6559" target="_blank">📅 23:25 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6557">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8491578554.mp4?token=dXruPJ3hg8Lxus8KJNizsCrVnmYYZ9j-KsWnpHQl_UmD0tIcPsHkWdLpEwLt2DLDs2ZBWuNGpzb1_5jYXIBuCsHfrdCDyiUsdOkKuzWRW5GhU6IcrMPuCi2KlW5gb3McbX-9_8QR8q-EOGW38JRFqOvwR2ugClalUOilb36-AiW5m_6QbYXKPA7YuFoo7uT3yn3yZpWgpnbxC-ZyAhbtNdPIJs3RDcfLxW0O8VljqRhjDoRBg_V4TQ_9a_ntXW46rrz8qco-o787bUdXPaPpSNmT2_UQoL-P1zE3cAinQE5ZT1Zut1tBjgkTqCIIhCJPWYY2Udvr2vFgoJrmLXNNew" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8491578554.mp4?token=dXruPJ3hg8Lxus8KJNizsCrVnmYYZ9j-KsWnpHQl_UmD0tIcPsHkWdLpEwLt2DLDs2ZBWuNGpzb1_5jYXIBuCsHfrdCDyiUsdOkKuzWRW5GhU6IcrMPuCi2KlW5gb3McbX-9_8QR8q-EOGW38JRFqOvwR2ugClalUOilb36-AiW5m_6QbYXKPA7YuFoo7uT3yn3yZpWgpnbxC-ZyAhbtNdPIJs3RDcfLxW0O8VljqRhjDoRBg_V4TQ_9a_ntXW46rrz8qco-o787bUdXPaPpSNmT2_UQoL-P1zE3cAinQE5ZT1Zut1tBjgkTqCIIhCJPWYY2Udvr2vFgoJrmLXNNew" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚀
معرفی افزونه Caveman؛ ابزاری برای کاهش شدید مصرف توکن در هوش مصنوعی!
🧠
✨
اگر زیاد با چت‌بات‌های هوش مصنوعی کار می‌کنید و نگران محدودیت پیام‌ها (Limits) یا هزینه‌های مصرف توکن هستید، افزونه کروم Caveman دقیقاً برای شما ساخته شده است! این افزونه کاربردی با…</div>
<div class="tg-footer">👁️ 2.03K · <a href="https://t.me/ArchiveTell/6557" target="_blank">📅 22:28 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6556">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">🚀
معرفی افزونه Caveman؛ ابزاری برای کاهش شدید مصرف توکن در هوش مصنوعی!
🧠
✨
اگر زیاد با چت‌بات‌های هوش مصنوعی کار می‌کنید و نگران محدودیت پیام‌ها (Limits) یا هزینه‌های مصرف توکن هستید، افزونه کروم
Caveman
دقیقاً برای شما ساخته شده است! این افزونه کاربردی با بهینه‌سازی کلمات، مصرف توکن را در سرویس‌هایی مثل
ChatGPT
،
Claude
،
Gemini
و سایر مدل‌ها به حداقل می‌رساند.
🔥
این افزونه چطور کار می‌کند و چه ویژگی‌هایی دارد؟
1️⃣
صرفه‌جویی تا ۷۵ درصد:
این ابزار پرامپت‌های شما و پاسخ‌های هوش مصنوعی را به صورت خودکار بازنویسی می‌کند و با حذف کلمات اضافه، مصرف توکن‌های خروجی را تا
۷۵٪
کاهش می‌دهد.
2️⃣
حفظ معنای اصلی:
با وجود کوتاه شدن جملات (شبیه به لحن انسان‌های اولیه!)، پیام اصلی و محتوای علمی/فنی به هیچ وجه از بین نمی‌رود.
3️⃣
پاسخ‌های بدون حاشیه:
به جای خواندن پاراگراف‌های طولانی و خسته‌کننده، هوش مصنوعی را مجبور می‌کند تا جواب‌هایی کاملاً خلاصه، سرراست و پرمحتوا به شما بدهد.
4️⃣
پشتیبانی گسترده:
این افزونه برای تمامی سرویس‌های معروف LLM قابل استفاده است.
💡
نکته کاربردی:
ای
ن ابزار مخصوصاً برای کاربران نسخه‌های رایگان Claude و ChatGPT که زود به سقف محدودیت پیام می‌رسند، یک ترفند طلایی محسوب می‌شود!
🔵
@ArchiveTell
| Bachelor
⚡️
#AI
#ChatGPT
#Claude
#Gemini
#ChromeExtension
#Caveman
#PromptEngineering
#Tools
──────────────────────────────</div>
<div class="tg-footer">👁️ 2.1K · <a href="https://t.me/ArchiveTell/6556" target="_blank">📅 22:12 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6555">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e8c485a59e.mp4?token=DnLatKrA6H2_7KKJLAu0ZHETej8NBe6eitRsBSogAEOe8ljtCJcD8IBaD6PS_Uz15RX7slMUMS0-XGZcc-JMrdwdAmtIH6rZGY937gZU3GxwGwk5zlhj_5D5pgZXEGlKsF5xLyR21LryjD7AMBt9t4K8mV7ouwXmgvSTSHfVDoE5z3hhQGugCqYYxC5VhAK-5DJr9pGU_anbSfIHOl0dj4xFaL6dhpCVJSAX82sD3eoFkPNMFtds8b2a5nxqZxMrgBcfpb8K3zs2z0xIz8_v_7JsePSZdSw9YGaPxiitJGVIdqlFBffy5dcw0bQ2R1TkQrths0npqqva8l8stKSMEA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e8c485a59e.mp4?token=DnLatKrA6H2_7KKJLAu0ZHETej8NBe6eitRsBSogAEOe8ljtCJcD8IBaD6PS_Uz15RX7slMUMS0-XGZcc-JMrdwdAmtIH6rZGY937gZU3GxwGwk5zlhj_5D5pgZXEGlKsF5xLyR21LryjD7AMBt9t4K8mV7ouwXmgvSTSHfVDoE5z3hhQGugCqYYxC5VhAK-5DJr9pGU_anbSfIHOl0dj4xFaL6dhpCVJSAX82sD3eoFkPNMFtds8b2a5nxqZxMrgBcfpb8K3zs2z0xIz8_v_7JsePSZdSw9YGaPxiitJGVIdqlFBffy5dcw0bQ2R1TkQrths0npqqva8l8stKSMEA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎓
ساخت دوره‌های آموزشی شخصی‌سازی شده با Gemini
🚀
✨
قابلیت‌ها:
•
🔹
طراحی مسیر یادگیری بر اساس هدف (مصاحبه، پروژه یا تحصیل)
•
⚡
تولید خودکار ساختار شامل سخنرانی، تصویر و کد نمونه
•
🛠️
شامل آزمون‌های سنجش یادگیری
•
📦
دسترسی رایگان و فوری برای همه کاربران
🌐
Site
#AI
#Education
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.01K · <a href="https://t.me/ArchiveTell/6555" target="_blank">📅 21:41 · 04 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
