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
<img src="https://cdn4.telesco.pe/file/hFKH2Nz-yflLidgTchok_cRdkvEConDCDdA348uGclv2P_bDvnS8eFCYGuTsSk2_IstKp3pUbmROw0I2-pBMCc0Rn3bca8zZvorWuBJdoSfKhDlswVy-RHEUiBfMAGPaZqjieuo_AjvEM9leLphhZQTkcwtvsaxF_Q1qlQECoakTm2je77zzhG4eukLFIsA9xMnfBMZ9lirbbzYgdBRVnL2Mt73AzR-gL5ox_JcjD6I5y13h0xL-uvysOWaK2t4PqrQu-YUYN-OOhlRcJq2MEVq3kRzf4Op-Gx_eElwTkmQscNkHVh8qNPfOsFVBxwl75z-SBqfdJpp0WgtvMKFSjQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Persiana Soccer</h1>
<p>@persiana_Soccer • 👥 407K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@ads_Persianaaپیج اینستاگرام:Instagram.com/Persiana_Soccer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-15 01:23:25</div>
<hr>

<div class="tg-post" id="msg-25041">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ae7cbb0612.mp4?token=ReWfvu945k0EcrKuNAb_RxpLxjSOhZ8-dMNGfQFaQsKohZmZjbPIvUOsK5-8cY1HqVrkHa9jlBnYPZWGskUSWGO9X7FF1lio49IM0hlp7q62gybbpQhwstlWIC-bSB1-GJxeoi0ZMc5Q7CkEDbrFM3QiYdFiJyzok_RTKzQlSUgwcESSqwcPmrBn5VDhLaEGwBYpcLz9-vJfC5Zy4WeJ44YigryGPzKNYj6gAy_FfJm6_I222mE9BuzqPSbbgivrltJWrR2GMWUdEBOwb7wf1nDpyEIM7ADnRMZbqAYf0I7__PRKnQjhwN4g-r8vtle47FeKmCk3jub0s5tACbaezg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ae7cbb0612.mp4?token=ReWfvu945k0EcrKuNAb_RxpLxjSOhZ8-dMNGfQFaQsKohZmZjbPIvUOsK5-8cY1HqVrkHa9jlBnYPZWGskUSWGO9X7FF1lio49IM0hlp7q62gybbpQhwstlWIC-bSB1-GJxeoi0ZMc5Q7CkEDbrFM3QiYdFiJyzok_RTKzQlSUgwcESSqwcPmrBn5VDhLaEGwBYpcLz9-vJfC5Zy4WeJ44YigryGPzKNYj6gAy_FfJm6_I222mE9BuzqPSbbgivrltJWrR2GMWUdEBOwb7wf1nDpyEIM7ADnRMZbqAYf0I7__PRKnQjhwN4g-r8vtle47FeKmCk3jub0s5tACbaezg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
تشکر دونالد ترامپ رئیس جمهور آمریکا از فیفا برای بخشش‌کارت‌قرمز بالوگان‌مهاجم‌تیم ملی آمریکا. بالوگان حالا می‌تواند مقابل بلژیک به میدان برود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 4.24K · <a href="https://t.me/persiana_Soccer/25041" target="_blank">📅 01:11 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25040">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8897e8ba1a.mp4?token=tAVKVAEDXOtOZ891S1ZkQSLfR6OHy_fFVjy3d_Fq57U-6aUXeO2DZ4lWLWubEk6TMJ8MWWKqgICUtQs3spWjoFoWSfAWImNfS2-mPtlRPU0QfEScRKGb0KzRRVfPpIxehi9QW-ktW9WwxwknmDbSi5Q4GGv658lVYuNDYvdKBTDkw128b_ic5fL_H8Z5GIjb8PvRElobfwP30ExrRRJjfUnTz9Zo_76l7-Fiv72oR5s9BIRC2rzC74mUI2gnSNC40ex9aIN3M3U8n9m1imiYQ19B2kSB5rvMJtzE1meTiBEnLbdP-enhmfNvt2-Q45_1tYYBkSn0DuQox-Kzogx59g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8897e8ba1a.mp4?token=tAVKVAEDXOtOZ891S1ZkQSLfR6OHy_fFVjy3d_Fq57U-6aUXeO2DZ4lWLWubEk6TMJ8MWWKqgICUtQs3spWjoFoWSfAWImNfS2-mPtlRPU0QfEScRKGb0KzRRVfPpIxehi9QW-ktW9WwxwknmDbSi5Q4GGv658lVYuNDYvdKBTDkw128b_ic5fL_H8Z5GIjb8PvRElobfwP30ExrRRJjfUnTz9Zo_76l7-Fiv72oR5s9BIRC2rzC74mUI2gnSNC40ex9aIN3M3U8n9m1imiYQ19B2kSB5rvMJtzE1meTiBEnLbdP-enhmfNvt2-Q45_1tYYBkSn0DuQox-Kzogx59g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇵🇹
کریستیانو رونالدو:
خدا کنه آخرین جام جهانیم نباشه، تا شماها بتونید بیشتر منو اذیت کنید!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/persiana_Soccer/25040" target="_blank">📅 00:42 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25039">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bN2QZDCldUxwwAKczOVMGN3hHuzqSlVb-47SmgHKws3yktCcWRmEXUrIOhZkarsiPk0C90IFdaulaMMwsieB9HmBc-iwuGI-g4bz0TF6JBJxGR5RcPljpC7nPsv8dl7vApXmN1OP7l1-fvmkHn9sKS8rycsUULFqYN8htKJhb3pWp3krxr8JBE2klbHzcDPgLNSUyjk5Emk2lZWyCtj3tX6OqyX7qD1ZAlaAYgUjT9q6vXNixm4GanXax9Rb491Dj2YxZiH8h_AXJEkAQtwJLeW20UjoRZ0VqFKa82jdmRSkpXd1B-lCOR7SEfh3flld6zMHMoJIEHgEg80U0hDYEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇳🇴
پدر ارلینگ‌هالند ستاره‌نروژی منچسترسیتی:
شاید روزی در آینده نچندان دور هالند رو در تیم رئال ببینیم. ممکن است اتفاقات هیجان انگیزی رخ بدهد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/persiana_Soccer/25039" target="_blank">📅 00:09 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25038">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a_HbwJa9FJJd43b-bucxF6WymmUDlDSfNco6k-TlCYknOk5YuCtLkWYCqjkXYtTr1E2SDURlFaa1tdf6rFEIh5jPb4kL087VJJsTEWFPDOga0KsuvBEWlfqr4bMUricS0lhK09L3WO5D1AmZZpHQG_eoMC01jehnoJcuFyINhysNCReJ36z9SFYlkvJIS9D9lJS-b9BnjWLhsLsEtPtxzIhSDcXbRotpp9Nsp-RTMtOcScxDuZAQlsDKS1EbLsDk2HANdky0LqjKjyYxPqSAi5-2016NcsDIFzjv7EM56nUlpfbi4OX--iZKHjQgWG0l92aGUKzAHiQT0ruCYmovfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛ کارلوس کی‌ روش در بخش دیگه‌ ای که از مصاحبه‌ اش به تعریف و تمجید از مردم ایران پرداخته و گفته من حدود 12 سال اونجا بودم. اگه روزی ازباشگاه‌های‌ایران‌پیشنهاد رسمی‌ دریافت‌ کنم ممکن است به‌آن‌پاسخ‌مثبت بدهم. من برنامه‌ای برای بازنشستگی ندارم و علاقه…</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/persiana_Soccer/25038" target="_blank">📅 23:52 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25037">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IhGuJltbDnlKiRqVBguHR60V4g5lbYYnEyTH3KvoiqLW3rrPQ0zkv90C-1TVpeg1Em5EokdHWo-IiMe97gzlidrA8It4u0ftfoxpX70c5tmIOQi7C6AH9rHOmxHiPDpRQpdbA3FsKNNHl33rFu7TX49OeinW6yIzUchfFyATzaNXNT-Euxev9eANYovRFsZALLWNLbt5oIaytKElrOPo-wXNAj-qlzHLLnxk1Rh7sFU4UEoKu53umOw4P2B7nYuQqchMHGcdeDYUj_wxVSseZXu8_NnkO89_QCNAlogP4lRS1paHAK7qVsJjyYMs2F6oKlrImPTk3Ns6KoGibhGb1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
باحذف تیم‌ملی‌غنا از جام‌جهانی؛ به احتمال زیاد کارلوس کی‌روش به زودی قراردادش رو با فدراسیون فوتبال این کشور فسخ خواهد کرد و جدا میشود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/persiana_Soccer/25037" target="_blank">📅 23:41 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25036">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/81c1096e89.mp4?token=csQvaxO3mwPUWmNP6yaDUhGgiAX4oZMZ_-flNZPfCKBFkJUVC_gB0QpZEp2JcXEqXPKUBOMh6VuQDJeQFafOuCWEwzTaXyjolPwEpaV3FXeaJ7JfzwKNzncqLhaT9gGGoT3n-e15bahmyo4g1_TqLSf-RItGDIdGx1cF0zdtFG1mDgnjAEQDUnjPs7CDyal00yRVpHar_UujW4dEpX_ugi9D3nPuoub4qeFiTND_UiMh_Omjcs4Y4AMufRml1IGVmkVToBrJF1LT-uKWuV4qVHXhcciFbJ3YqsKoIbii4STbZW3-D2rD_q6OvcoWkHab4ZlmRySIyz17FmPc2wjuk21u1gskEiJw5POCoMDjcmPGgS6OR5QVNP0zyHQ6V51MJ0KzJzOINUTSiMAQoIRDJ3r9GE2u91juvge0E4zawHQjFC9FKPg4qWvlPYs2vcTu9-p-5m15mjh_9V7J4gd5g2-nGPZwuGva8jS4UKtwufIhcQQ88xX5xIl1CJZ2PHPDDYIueOm4m_DCmIleG2ROAn5QfvkYyQbu7SHwFCjOcHgZLaqt6sHnL1zeXB7YiebLMmFz0yU9-C0Fdo079krTp5mkWHBsuOlHhmFp1-YAfXrg9sciSUl-loj1pFhnnagpdRqD6-A9AI2bzHMj-UTGkFMDDAmc0gE8h0rBXmicJY0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/81c1096e89.mp4?token=csQvaxO3mwPUWmNP6yaDUhGgiAX4oZMZ_-flNZPfCKBFkJUVC_gB0QpZEp2JcXEqXPKUBOMh6VuQDJeQFafOuCWEwzTaXyjolPwEpaV3FXeaJ7JfzwKNzncqLhaT9gGGoT3n-e15bahmyo4g1_TqLSf-RItGDIdGx1cF0zdtFG1mDgnjAEQDUnjPs7CDyal00yRVpHar_UujW4dEpX_ugi9D3nPuoub4qeFiTND_UiMh_Omjcs4Y4AMufRml1IGVmkVToBrJF1LT-uKWuV4qVHXhcciFbJ3YqsKoIbii4STbZW3-D2rD_q6OvcoWkHab4ZlmRySIyz17FmPc2wjuk21u1gskEiJw5POCoMDjcmPGgS6OR5QVNP0zyHQ6V51MJ0KzJzOINUTSiMAQoIRDJ3r9GE2u91juvge0E4zawHQjFC9FKPg4qWvlPYs2vcTu9-p-5m15mjh_9V7J4gd5g2-nGPZwuGva8jS4UKtwufIhcQQ88xX5xIl1CJZ2PHPDDYIueOm4m_DCmIleG2ROAn5QfvkYyQbu7SHwFCjOcHgZLaqt6sHnL1zeXB7YiebLMmFz0yU9-C0Fdo079krTp5mkWHBsuOlHhmFp1-YAfXrg9sciSUl-loj1pFhnnagpdRqD6-A9AI2bzHMj-UTGkFMDDAmc0gE8h0rBXmicJY0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇵🇹
🇵🇹
درگیری‌رونالدو بامارسلوبچلرخبرنگار برزیلی در کنفرانس مطبوعاتی پیشاز بازی پرتغال-اسپانیا
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/persiana_Soccer/25036" target="_blank">📅 23:23 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25034">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sWPrqp4fHRXz5Kj2YJ6UeZkkO6WIKR-kqToVY53GmPD0Nk0mzL-9Nbrx6jarp1Y40UiwVRC7Up3qkL1I5avA36spCZeJvj7SojlV_iwHIFqn1GsgyPLgfRDMil2jhdp5yyesBcHfWXEMpaH-GjyLaajRfLlL9qPjF2KIMoLSAzlRIRxXebPJvhSLa-Cq02rR3W2i4jjnnrOpLDOWp9o4yHsaymI85lpNAst65a1Ufc7tboNM6edWhfaMndKm7tlXu0iUdoW9a2CjhJQzOzIHl3BfvG6E7-eoSvAWe1kPXNIqpYC_Wj0wOXwaVpESUbRDBq4wsskerhs3uEUY10-J1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
طبق آخرین اخبار دریافتی رسانه پرشیانا؛ علی نعمتی مدافع‌ ملی‌پوش سابق باشگاه فولاد برای عقد قراردادی دوساله‌باپرسپولیس خواستار دریافت مبلغ سالانه 75 میلیاردتومان‌‌شده‌است. درصورتی‌که بانک شهر با این رقم موافقت کند به زودی پوستر رونمایی از مدافع جدید سرخ‌ها…</div>
<div class="tg-footer">👁️ 33.1K · <a href="https://t.me/persiana_Soccer/25034" target="_blank">📅 22:59 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25033">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nHHcjTpDYzkXUslbWD4YCSalGrGAxziDGRga0lxLvGUzCbdbX4wdo5SCYI_d6eFcWk9qmZv5a0x3Kptr-lNNU8IHjJ0iEZySaVkE7s4ocOgrxkmHuzJt4xFPpShAumrlRVlAVyUmVEFE2ziGh6VZVXKvmPO135qkCcghvP95FkDgA8QM0MpmU7xBasPKJCxcuJ3MQDmPkUM0dDi8JAVm4Lytls-vV8Lft0BYt-Cx75n7cyJ31XqdsY-xHrFRACf6XWYpIRaSQCSUcjD0iO4BF6sp4wT0ZBOxAfGUncKa2WfgV1gb6n6tYg8UC1hDrVvS9HdLF-GzWotkpUztEL48hQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
یک‌هشتم‌نهایی جام جهانی 2026؛ شماتیک ترکیب دوتیم‌ملی‌‌برزیل
🆚
نروژ؛ ساعت 23:30
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 32.5K · <a href="https://t.me/persiana_Soccer/25033" target="_blank">📅 22:59 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25032">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UB4OS9oYQ_TBSardgNxr6uQwd4Kbis2-n9LU8LsClg70zaFsy2CAZUClBsjOrG8Fhg3MDXkMjDCGUgqXBrVJkAMzqJbxksJg9ZhEm0oek7l0clo2yVyTFY1fFwPM6B9mw3Iq3JDMGCXV8Ju7PKC95ZysSld049uMYo24TyO05IE8eWMMfbQCroERiAmZhaP7RHsuMahXQJOAblpfhCqwSNgoDRCoSRYxRVBvMCYJW2iaKAV9l5I2xgLgKMErkGlNcJ8-Z0TLYIxot1AE2GJUdBwiJmjNGa8DEg5klXBPTUG3P_wnV0WCbVpkkwml3BuELKAuHixwCd69xpQB00pOcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📣
🔥
بلاخره انتظار ها به سر رسید
🚨
👤
نود جورجینا همسر کریس لو رفت
🔥
👇
🚨
👈
گزاشتم تو لینک زیر بگا نریم
👇
https://t.me/+wYDPG2ky70AwODU0</div>
<div class="tg-footer">👁️ 31.9K · <a href="https://t.me/persiana_Soccer/25032" target="_blank">📅 22:58 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25031">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nsfiaf36fr0_5dLOzP2E3Pub_wZTotim-ro4kfPk0yDRbmbNL72JyMI2PJBSIrYgim3kUZoOzJYaIl-Wfp6w_KOeKGq7DCj4Gi_MNLajKqs3_XpaJlb6uCiZCqk8MJj4TMLJmDubuu9rQXCL3GeiLNPpvW3os2uGFd6BW9Jzcuxd2X6vud2fPmn3Lg4z2IBNj1BM1bPSk5cqJA7dlc7NtZWGGb4SBRqgYAofnmZIRmz58rDaPiNhb51_6PodyM8fxEtMB6nEiUUNplSmhp3m-k4y8b3MPyvl4lLw7U5uzZlxERp60CoxMAxQTeT3B7uFW37Z-wIVzUAVxs7CfruH1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
باشگاه پرسپولیس برای تقویت خط هافبک خود؛ احمد نوراللهی و محمد قربانی 23 ساله و ملی پوش رو رها کرد و قراردادی 2 ساله با پوریا پورعلی هافبک دفاعی30ساله‌ سابق گل گهر و تراکتور بست. پورعلی درتراکتورِ اسکوچیچ کامل‌نیمکت‌نشین بود.. پوریا پورعلی جانشین میلاد سرلک…</div>
<div class="tg-footer">👁️ 35.1K · <a href="https://t.me/persiana_Soccer/25031" target="_blank">📅 22:43 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25030">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cDr2qSqbZ3yhciZGS9DicjioVS_5gSwy2nNqQNhL6J5QubOvJtdBnivAv4qA81fVjd1BIINgovDtOBlw8n7Asg6GkJFLEcngUh96odGSg7C0ZCHhDMvpviA-KeopLdrWDiDPQAARwrI2UabDmLooEHZ2LvD70qfDi2i-LlGudGf4r1Nb7CmDKb5gN4A27WCNrmCZNZ7lfxS0W2Vwuuh6FQoEUH6Baq5-z5SB9_X8O8n0r_gisqiOFyaptkmflYLlx6TCYbi6YU-EIZNsd51H2HojbNIrUtEf2GsuPUPZcjEbCUbd14Xh2LyviNO14zmV9qHfqaKnkxgWcL58qCNnFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#اختصاصی_پرشیانا #فوری؛دراگان اسکوچیچ سرمربی‌سابق‌تیم‌تراکتور و نماینده رسمی‌اش از شب گذشته بایک‌باشگاه‌لیگ‌برتری در حال انجام مذاکرات نهایی است و به‌احتمال بسیار زیاد فصل جدید او رو درلیگ‌برترایران خواهیم‌دید. مقصد جدید اسکوچیچ فوتبال ایران رو سورپرایز…</div>
<div class="tg-footer">👁️ 37.1K · <a href="https://t.me/persiana_Soccer/25030" target="_blank">📅 22:24 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25028">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uQiXVQp-dAdY-cseqgXdrJirXhOsw2rL0o2XKN3qaUvcb0QxWz1kpvJ7kNWWZyzvoJ1JRKD03ai-Um-ow_A9bvMEjvsgSfFu3meBppUdWlNnj_u60zkLW2nhnB-bAikPk-1PHrftX7rfqJh69Co8SB3aULcsxjfbXWtLKNgrEw51ZqwUQ09TvEIfY7wqZEMh0n2iZ9MnuvZfqhxE3bckTK4KR96AFfDN1UGEuYRJcJx8s9SrSlEnPmEQD5oedRstk_b3RiSau4idN_AdknsaYSkelhcyFdm43zvP4JcpWhYmim7Cq_NdnOeuLPg8POKHssDUVJpic_yfzfkeI4suCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ALTWGg1Sg-37orXPTRTw-MK5HlDvxWxFqhoq5DVnkLOH-D1RA59hxheE7q1xb0TGhxhz-_xYTPjer1_HKtdvdt1Jnhj-XH5GV0dGiI39OSrRpiOdhKA483_F2lxvreZpvZjHQ51PUs2hYnA5tSgRGqzRkRNTKEXdxRb9TU5JNkHHjEKgdhy_NPPHThnghJMPSGqUbId0QYxXNROWg_pSf_vDp5l2Ztd3Z11XNqxW4CNhRERWomt9k_ee2GM7i5ZCweF-97mVoS-uZ2D1hQojxPaY5n-0bLi9mPFYTvrWSid1np6pRYpYkKhEw4u8Oxl94qnpVk6GrWdjICRBNogdEQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🏆
یک‌هشتم‌نهایی جام جهانی
2026
؛ شماتیک ترکیب دوتیم‌ملی‌‌برزیل
🆚
نروژ؛ ساعت 23:30
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.1K · <a href="https://t.me/persiana_Soccer/25028" target="_blank">📅 22:10 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25027">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WWbGRXdQNz_gWibiAp3oK4cAzfo_MU3vTyqxbD8S4Zkekg9YDWUdcTOigkN3-oYCXVamOgk8pou0O93EanwZmU0RiOcQ5nupcHWp3sOMGA3G3h6mc2cBwluTkf1omxi__UDt6sjNG6MWOj1D6seNIwiRe-oHilO57VH0qfWKr68O-y_LNLlkbfH4_0lWOHd2XiU_WECPUyW4AogpbLOGCvWSPpWsuwUpbeUwQ2AsmQXTFJl7bPVwiQOgiTHcHTc_spLyxcUJ-HG0OEOIqa9nzYcXrqckHMqP33yLyHBRtOZQuqoZ8nU-XxtWXj_EhVAiZTBNXBvYpcJbZaLNzzkgpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
تشکر دونالد ترامپ رئیس جمهور آمریکا از فیفا برای بخشش‌کارت‌قرمز بالوگان‌مهاجم‌تیم ملی آمریکا. بالوگان حالا می‌تواند مقابل بلژیک به میدان برود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.5K · <a href="https://t.me/persiana_Soccer/25027" target="_blank">📅 21:57 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25026">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ni4EqpumGxf_4WO6DHWETIWTXl-ixxMIHWbfh9K5yIzopLRq8m7Iel2B4R2XJ_YQkzDtzZVW7jmBrY8gcvqvkNe4rkIfv-wdY0keuX541CIzU0jaYoKPCeC5GIjchbWEmnaAqbQ2UfAh9X7JK3iF2yriOw-Ir3JMAvt0XY8YnljrKv3O4xfDNmtgtKjdvSIR3UafQCOtOOuIaMAa4wMwRQzl18tJQwjle2CjQVjDpaNnwQXb8vjW6gXGpidiTsYoycxApuivp9Y92jH_fZEOp14qQ4oMgoesWOZOBaJ5nIW4sLywCKqlpb67QPbPcGxp2we0HZ-AX4BvW1b8ldYV4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
اقدام انسان دوستانه همسر رونالدو؛
جورجینا برای کمک‌به‌زلزله‌زده‌های‌ ونزوئلا پنج تخت اورژانس به یک بیمارستان اهدا کرد و ۵۰ هزار یورو  پرداخت کرد تا برای خونواده‌های آسیب‌دیده غذا تامین بشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.1K · <a href="https://t.me/persiana_Soccer/25026" target="_blank">📅 21:44 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25025">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TmxILp82VtwEiRvr_2I-93QhOy2cBdb-1bN0wdQVHeNyTcOtUWlihLf_KiJi3XoEOMdrYPLCbsliXh_JeJO5DwL8mqu_vX5l1MHFpv_zTcFD6-7hoPwQrIZ46FYSzyKlg0Y1sNvWks6qZVoqFoj6KLJrnQX742FdKdN46KarJc6i8SnkjXKEX5-9q-z9gZzxW0SQnaRCyUW5QiXqZ8OmTBcDvxxh2z2pkDEu6kuv0YIvxainnFrcGtrXNyjAAIORI8SPgCOtgo3hmng1iBLb1BRCoro8kd4CTTRsjsH0W48rqQ8cUBpQVKhljIq-jyYgk6vYkcyV7EpDMqKa3021jA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نوراللهی نامزد جایزه‌بهترین‌بازیکن ماه لیگ امارات شد؛ احمدنوراللهی‌بازیکن‌ایرانی تیم اتحادکلبا امارات بهمراه مهندعلی، تادیچ، کوجو و کریم البرکاوی نامزد دریافت جایزه بهترین بازیکن ماه ادنوک لیگ شدند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.7K · <a href="https://t.me/persiana_Soccer/25025" target="_blank">📅 21:20 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25024">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Hn8GotJOuoA06MNofoTdGrcKO8z9M6-3-GOViPUmCdKWSAC_vAqHm2FdDU0J9zC5pHGCa3frZy08z5G7NqbKP6YWxDbGTypSeFwfSmSM-uN5YJ8XP7Vq8InF7pXUPEXKwJ6DL3up-MZ8kYf2ANqejX_lMajF8mQ924VDAEZw2_iygs0AghLIBriH_CcNrVXaO-hSEyraaLZvR9C6YjOu5YLYn68wnH-N7Yysj8hYHOxqRZU4sS62whMopp_Q6elboc4d5vrAULY4_AIAYmgA-TGOP4mlACE6H2gjRK9xWppeUa5LJ5w5fvuidr6AXTBeGR6OejDY1pFqPT2vlubzOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
مهدی رحمتی سرمربی موفق فصل قبل خیبر خرم آباد با عقد قراردادی 3 ساله به گل گهر پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.5K · <a href="https://t.me/persiana_Soccer/25024" target="_blank">📅 20:53 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25023">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Lcc0t9k96vliflTKXIpVxoCqQCu1BB89jGCjs0pEvKpmlVbRwhbLy5PCPUfJFU4ZBJqh8U5vl9CstWz4oIXsGMr-3Zvq9dMEUEK--oFIe53ZyZMA9dpXW6Yu0BHOQmzu35s6sEvLelr7Z5uYpXMAYqmJ2jL7_R1BCsAWpIHSJ1fjNsxnnbKpx_qj9JZqtkxE5VslfVrXC2DWHQT_M7am_JDha5GMK1xvjf1-X3dbs07tw_B4PXDG0HUdVQGtkncc2hcFHTCdh8IOOoowsByQ4Zf7Uw8Vyo5mUuneAMEd7cri3f41KQs59EMgyI_p63IUIrHFugf8t4nxi_x9uh6PuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
مهدی رحمتی سرمربی موفق فصل قبل خیبر خرم آباد با عقد قراردادی 3 ساله به گل گهر پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/persiana_Soccer/25023" target="_blank">📅 20:40 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25022">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9652d5ab0d.mp4?token=irfEk36vfg0kebpPfkuVUnibF25VbsGLjkBuFItMasl5QBmlhA8FH_GBN0HJ_0g9-TNa8ho7LAdwNkT_g5XNUdPktu4Cpn9TFTD7iwJGr8_uvO0xRjrFYkgkqLDpLrQFEeb3NhXK5LPWFa-YPY4bEvdc6lVtEbdHvUcN5uVypr-YvfMPD8s5IrXsdN9WkqYgYvY5iQDS3Gi9tF8xw28_JBWjieGa1C639O0DDEqARRfqrKNivtD7mEU7zXBb7wZFcc1bR55E8zgrXEgXgzAyk1l8hEAOFAE7YwqVouwqpoKxnBd1NtvreJP-H_y_rWT5tr5vjQMcMLkW-Gasamb5JQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9652d5ab0d.mp4?token=irfEk36vfg0kebpPfkuVUnibF25VbsGLjkBuFItMasl5QBmlhA8FH_GBN0HJ_0g9-TNa8ho7LAdwNkT_g5XNUdPktu4Cpn9TFTD7iwJGr8_uvO0xRjrFYkgkqLDpLrQFEeb3NhXK5LPWFa-YPY4bEvdc6lVtEbdHvUcN5uVypr-YvfMPD8s5IrXsdN9WkqYgYvY5iQDS3Gi9tF8xw28_JBWjieGa1C639O0DDEqARRfqrKNivtD7mEU7zXBb7wZFcc1bR55E8zgrXEgXgzAyk1l8hEAOFAE7YwqVouwqpoKxnBd1NtvreJP-H_y_rWT5tr5vjQMcMLkW-Gasamb5JQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
تایید خبر اختصاصی روز گذشته پرشیانا
🔴
مهدی تارتار سرمربی سابق تیم گلگهر با عقد قرار دادی 2 دو ساله رسما سرمربی تیم پرسپولیس شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.2K · <a href="https://t.me/persiana_Soccer/25022" target="_blank">📅 19:53 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25021">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/89b613cca1.mp4?token=HQMfzxYTQ2XPwvBbbzS804laVzynC2GKxHYbYZkDDduLfFo92cejAhy4nw3o0d6upGkvYkElxuRaYbl47NQndd9K0-gULSyVpy_2lacvNvBifAZ7SyBjZ_0zo1GHUe6SF2s3TnRUMR1pli7-c0qCmdEI2-rqY5zS2s5YVLcsvpMhXIOdiq6fuam-2LUEQMsppFDhF6jZ8wdM1mQEaRiZhp8ND1oKF3hUvtJHQ5f5yMN3meFm4fdRjD_3wlhEWzIiBAe0XjLwuOyuj3msjXGF1JaLHhMkRVrVQ8L7NKHQB8bGYx3hspF73EDuI6DN48F3Qe4UfFB_012olkbjsz_P2w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/89b613cca1.mp4?token=HQMfzxYTQ2XPwvBbbzS804laVzynC2GKxHYbYZkDDduLfFo92cejAhy4nw3o0d6upGkvYkElxuRaYbl47NQndd9K0-gULSyVpy_2lacvNvBifAZ7SyBjZ_0zo1GHUe6SF2s3TnRUMR1pli7-c0qCmdEI2-rqY5zS2s5YVLcsvpMhXIOdiq6fuam-2LUEQMsppFDhF6jZ8wdM1mQEaRiZhp8ND1oKF3hUvtJHQ5f5yMN3meFm4fdRjD_3wlhEWzIiBAe0XjLwuOyuj3msjXGF1JaLHhMkRVrVQ8L7NKHQB8bGYx3hspF73EDuI6DN48F3Qe4UfFB_012olkbjsz_P2w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
همراهی‌رایان‌شرکی باکیلیان‌امباپه در پایان بازی با پاراگوئه: لازم باشه توی کثافت، شیرجه میزنیم!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.5K · <a href="https://t.me/persiana_Soccer/25021" target="_blank">📅 19:41 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25020">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G3BCl6ykH5YGCgxMEh_4K0TRd171MUdj0E5Nl3CivPrkb2CcZMCdV7dG-Jn1ekSj4ciFQn1xA1ZIVyNlv0aiDwXWIW71ByK7H0L6z5RTluj7uQ3ygmcBqg2vrvFs3T7y6jMXLY4pJv50N_fas2PSRrj1mqa9TM7xVimNNoSFB2piEuhfFaTEWGog5SRxZhWxEezfFrIc-l0CvWtIktU9QBC7p_tR43OitQMoRYXWOhLF_Og7UIul-6hbKLz9lf7saq4bIDnfx_BzItMh0L3s3Rs0xttLV2_759qZKHEW9n2IJOtRsPevTiJOppKnZks4tNRSKRtnRP36bHUjDLuqkw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
تیری هانری اسطوره آرسنال:
کیلیان امباپه در سن30سالگی‌به‌رکورد 1000 گل زده خواهد رسید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.3K · <a href="https://t.me/persiana_Soccer/25020" target="_blank">📅 19:28 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25019">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VWZn5cqNnz4PNhBh86r-u_sDa5cLG_dfbXVpnifSq--3M9SdgUh8nUGdXeursNUFt3JNVq-D1HkupZSIV4-Z0zAYuu2A1i2uxRpWJDUDW0Qi34Jc7iMN007uF-PK1v5WU6GBnG_x4s0CQTinWdfdxUe23NfxE-8fqmUNy5ofI0MQOmq3KTZ4uHZykDweKFCO9tIJXfLeqgSWiOGYaxzK55I4igj764hta7HJ43Qt6XerCwYf3iIC8V2yjK0YbKxFMGzNhx_6EAD2FeuLkVqAjnE3oNyFZNaBOM4QT3YY2EG1vQobZWz5IDGinkx2UiEHXDeMGwgtul1evWfqytJp_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
دیدار فوق‌العاده‌حساس‌وجذاب فرداشب دو تیم پرتغال
🆚
اسپانیا رو عادل در آپارات گزارش میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44K · <a href="https://t.me/persiana_Soccer/25019" target="_blank">📅 19:27 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25017">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBetegram</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/L4aktiPfGYEJqqqF2zt0OWgDZiblXQ74KbFESfuNmw9oCMbEV8fYssf9cq7ABpQ5ykvFSqfHThuNeUru4xpa1WQUxYGsqm95gmuvRJR5p0FroDmrhWtatHTjVJePehiBcEhydvo2Uif3Lq3mp7RhGEDc9MMokeQIaKadNIo6MvPYHIlBks3ZH1R_KHlHiK5lKd8Ul0uimPuDga3YTZI-4e6gQcmkNFIs32_vdLPBXrQ0SctEWbYilGlV2DpYv53dnEP39Yc20ufD-6VGhyXkgFKG--bzQFCbJXPQ9fgplr3NuW4MRK3OUGjORH6Ye2LzjKBLoTYUTpKxn3wSibFkzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/N0V-iDXcbPe5_sifhEYA2zmQIg14ir4cdxjhdsadIilaWaq0JhomwLeGeVuRG4vH1KU6stPkXfg7lZNhg376obs6SHl8kWmYmW8W_PoXmkhDD5HXzFB8hVLTSCYBkK8cv9mBrovc3RJodLG7fsfreh5iUH-NaW5SyyXP4Sxx-x7Ml1GWNuEfwWakN6tq30sQs6pHlbggfSv0tB15xgzFNQb0PPnO8yLzTHhqd53H-eSN5a2CMYG1SEv9Wc9Y-TUxtjfJCOhyb6b3Zww4gRAXRzkLrKIqd9XS8G8V9KZv72hN3zlq_nAooFqO-KEOb9trPHvnImgZKbxYz-hRvAaesQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇧🇷
🆚
🇳🇴
🗓️
۱۴ تیر
⏰
۲۳:۳۰
برزیل
🆚
نروژ
📌
صعود برزیل یا شگفتی نروژ؟
⚽
🔥
پرافتخارترین تیم تاریخ جام جهانی برای ادامه مسیر قهرمانی به میدان می‌آید، اما نروژِ آماده رویای حذف یکی از بزرگ‌ترین مدعیان را در سر دارد.
👀
⚡️
برزیل صعود می‌کند یا نروژ تاریخ‌سازی خواهد کرد؟
🚀
بتگرام در تمام مسابقات جام جهانی ۲۰۲۶ همراه شماست؛
با پوشش کامل بازی‌ها، آپشن‌های متنوع و هیجان لحظه‌به‌لحظه رقابت‌ها.
👉
🌐
🚀
betegram.com/affiliates?btag=3_l7
🔥
⚽</div>
<div class="tg-footer">👁️ 43.2K · <a href="https://t.me/persiana_Soccer/25017" target="_blank">📅 19:27 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25015">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P7yzuM_Vq_11Gi2HwTup0obqume3FrTnnRo2oZNFk3o4oaI88-xF6xGAiNafQFsr43wsbQlaZubkyz1buQ22q1E3ycbJMzP58WVvE-kNmB1osKiZbKqN7Rmh06DKQSLYSozvBqGbg4MLNdR7eDztQa1WIpjq1nmhzWftDRzLnI1iCvzayMZMxykQhgzx7mcqbtwcdsRoVvsyEqBBzevgo1twpN5YNyZf6iY8TyoOocsVGIOWsJhQN7EQUOAoccX9YzIFGRNJCdLePsHX8xc6Jkc439YJon_uO_O7lwJ08w6e3gOs6_79r6kco5FJVFdEEkEAdd4nr03Dq1AgHky-3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
دراگان اسکوچیچ: مدیریت‌ تیم پرسپولیس به شان‌وشخصیت بنده توهین‌کرد. تو عمرم ندیده بودم مدیران یک باشگاهی این‌چنینی با گزینه سرمربیگری خود برخورد‌کنند. اگر شرایط مهیا شود روزی دوباره بعنوان سرمربی یک باشگاه بزرگ به ایران برمیگردم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/persiana_Soccer/25015" target="_blank">📅 19:09 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25014">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nRizUKVIekKdzQ5XNQdGnahA2_5udmQ4AT8JPuzHWKtUQl4FcDQw_4DnKfutsXiwwyCBWCrftOYcpVlTSw0q9m0DhZEN4ZCwjbKBBky2WAzjUF_NT6kSuERWwIseyJTZReTTKntgiesZLjBR812uKm3V49_wenCzlWszyGewPixGVsQtkoOhySCwkv1OV8tZ32R4aDW15SWNJ-FMG9qjvZByQq1saLw8HaW2mRn9mGYvPNzLh8BnUD1qhPUeg2f9ZmCJ9sXsz0pWHojjpufI0BKIKOdoR2oQlgKAdL50wrr-MDwljfmf88-GKZuOPrnCJNY97ZELFyS6ImvGP3Qstg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Aparat Sport [3.6.2].apk</div>
<div class="tg-footer">👁️ 44.7K · <a href="https://t.me/persiana_Soccer/25014" target="_blank">📅 19:00 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25013">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rUzfQZVh9DeHt4Zqq41m21n9XKP4o27yXG2jqw6H5li6UNkkWODjxUg-qEGM4gFxKKoHHhEER5N_XrtnpiKtlaZkM_1HNyZcEIJ8HyQd5VlnUwq7XGGjO44XoTB2F_-6BxPoDgKrFc4tuAtHD0D955D7BeMV5lWL38P3a_ZRGJj-buD99eYLYEXbcsZqZOUt7Yw6QpZ2AgTMHJ391bQdPBefaC78te0cX_13SCP7sXW1C0y1-Q-93pPeCceFUiEgx2aMJks6ivSHTvzu8Qtxs4rIVJc8RVdMO78-kSRAYzKpoBKikjl0_or4s00PxEVC0g_UHQjGICR09wKN1P0D-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تایید شد.. مهدی تیکدری، مدافع راست 29 ساله فصل گذشته گل‌گهر سیرجان، با امضای قراردادی دو ساله رسما به باشگاه پرسپولیس تهران پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.7K · <a href="https://t.me/persiana_Soccer/25013" target="_blank">📅 18:44 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25012">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O8IfSBMuZj9k79lZ9LRpxdvoDzUx3jwkmgCrs1vqe6WiW0gSfqpiNhTdUnPt3SrmFg214jbw7fgboxf3y5MrftyiCsoQrQGjwVDpxf3C2JieXQ8xROMNqrlZWdOyO__TowSaTc1aac8iKumUdD698MLF4fUgwLuJ3wT_lkunHsrc2wmqwKkaRQOVPSEiV718QqG2fcoOm66vismrJ4GxH1mWMG6BFP29q39wlt7NGoiX0SO_ocz8aIx2RdPL_Xdl3X9AU6a7V88-zS9o3NQpimMceqysu6uPqJY08neyKg6HZyvvNlpis69kLv1nyzFmzKiSFsRnImMWWhQzlyvKJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی؛ مهدی تیکدری ستاره فصل قبل گل گهر سیرجان که دوبار تا آستانه عقد قرارداد با دو تیم سپاهان و استقلال پیش رفت درنهایت‌ ساعتی قبل با عقد قراردادی دو ساله رسما به پرسپولیس پیوست‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.4K · <a href="https://t.me/persiana_Soccer/25012" target="_blank">📅 18:21 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25011">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rREAptpw2M30r0SlkluYO0Pw7rb6BDlxYR2Fi71aVDb8H7-uH8gKoqp1vNcy0AQ95JEj-f47VLsX7-HTAAYXDixJzwxkBKqlOeSLcnG0cUhvk70AFxxkyLbzsL-ce1StC-Sq9d68Xo9robmixt-kp9B8spSDWadG_qmMA3yivtC-mRkaEAPtV5vbkscgFApSCu7dqAw1ICzm9Cy3Uw5IPeZUwwQyvC2zMS2nXasMT_WoKxjrD-65PfFsQfHouvafqIuGbOR2FqQAhKyAyDSeCF8mn0AdLiMJYnGh-bZ015jXBwtncQswLydAZ3uwUyGcOb-hFqRBj_-r5P2pPAMQFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛باشگاه‌آلومینیوم رقم آخرفروش محمد خلیفه رو به باشگاه استقلال اعلام کرد: 60 میلیارد تومان. ایرالکو تخفیفی 10 میلیاردی به آبی‌ها داد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.2K · <a href="https://t.me/persiana_Soccer/25011" target="_blank">📅 18:17 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25010">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sb0G4KwNhU8a6Chrh6ngWRdpbSVjEfVoBTooB-HyuPAXfFFVeUgk_tFJWho2mXeL8tYibPx42rVRG7zCwfN4pTm8yMDN6bfKetov8nXvqQKFLVLNmpMDMGQzJBkYvdEJ_7TmVXE_t2-3SKZXUAf2XhROwRHhi6vJajSvWS-DGgaRej6Bh1OBS6Q4R0kVwwo302ihBHLZ_Vm0JCkxpzZSdDWLErUgHonWIV432261YPF-4V9W6sKzffCmS4rtIAVq71KPNOgzGP4RjdDbCPk6QC7jlyqTDJKebJjdOTYBVC2GTSQUQiMSnW6iu4Nrp83zPrsAhu0IufkQJP44ocRo2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
14 روز و 14بازی دیگه‌از جام‌جهانی باقی مونده بعداز اون‌باید 1440 روز برای دوره بعدی صبر کنیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.6K · <a href="https://t.me/persiana_Soccer/25010" target="_blank">📅 17:40 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25009">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0b051966bf.mp4?token=M9x62NowOmGqGr6vbTFJQ3IxTqAxNXyJ1J14cFEQGv50DPokN8kOpsLeZg3Oxp1xVTK0N0g-7_GyJljvwV3ym7SM1ieIlP0O1rHoETROanr0TVoMEVk5x0AhdWac-PYFXljImUXIAZ2-n5PYFJOkZx9ehFoIzCzgJPl556qJ0_6b9X8CEOOzxW5yOyEQu_I-bQgkCI4_SSjWnzokjbzkUBcdMqoDhRJBGCknUFtjSL7VXakWf-B9KEPHA3sDYdPHEAY51qeWAzjs6jGRdtlKyJhWp6DLMHllTWwgWPGjMOcbgy-imNuCM89_gCsRlRgsfW0IUFw4jalZsDhvFqRTjQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0b051966bf.mp4?token=M9x62NowOmGqGr6vbTFJQ3IxTqAxNXyJ1J14cFEQGv50DPokN8kOpsLeZg3Oxp1xVTK0N0g-7_GyJljvwV3ym7SM1ieIlP0O1rHoETROanr0TVoMEVk5x0AhdWac-PYFXljImUXIAZ2-n5PYFJOkZx9ehFoIzCzgJPl556qJ0_6b9X8CEOOzxW5yOyEQu_I-bQgkCI4_SSjWnzokjbzkUBcdMqoDhRJBGCknUFtjSL7VXakWf-B9KEPHA3sDYdPHEAY51qeWAzjs6jGRdtlKyJhWp6DLMHllTWwgWPGjMOcbgy-imNuCM89_gCsRlRgsfW0IUFw4jalZsDhvFqRTjQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
ریمیکس امیرقلعه‌نویی هم بالاخره منتشر شد؛
دهنتون سرویس این چه سماییه درست میکنید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.6K · <a href="https://t.me/persiana_Soccer/25009" target="_blank">📅 17:29 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25008">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZHhzGPggE0r6IgNlVSzkmP29VddAOoDW86h1OkYZpAANeq1kMWL4Jddc7DYrjyo2IJ0sWK_44XETedcIXR5n9vYjLt06rHsl26tX49k3QPE_kMwReXOo-f_JCdapt8I6usz102xcyBZuaK8hSLANOlINp1L_YaPX-Mzt1z93-jig6xKjx4cBW6rm7jH1qYoPkl7HnJSR7Sh_AogixfBEak1DZdYrHumw53bGEu1KOyaq9CjLZnBASQ1d4ShlqIRLv7KhFknjU-hgzKq1R9AI-O8Yc4oiyr-BkD3tPWe2Bsw2ZX3ye_zYC-PgdzNaJmHYKF0eUN4WWANCnS2QJCJBYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔹
سرمربی تیم‌های مدعی ایران در فصل جدید:
‼️
استقلال: سهراب بختیاری‌زاده، پرسپولیس: مهدی تارتار، تراکتور: محمد ربیعی، سپاهان: محرم نویدکیا
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.1K · <a href="https://t.me/persiana_Soccer/25008" target="_blank">📅 17:25 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25007">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eeaaa6b3cd.mp4?token=VWDzjInIbLKlUv1p_Gmb3qprY-uhydfsETRXlhMZyayKQwTymow48U-S7TTeE0DttWKZ1RDfiCYkm-0_7uoknCQEGNkJmcCyumtxlkpn5x0AJzAGJ5a8r3yMZ2tqapFkMTbwZs6Crzpz4NExgM45KHZC3AOeNs-UpueKHtAELuYztf6a04NDTD6omUXii8uyMnpNg4Rq8wWXKPp6qKfAxcY0vIWbV2ZuEERV7MQ4WOq6BBWu8LNE5-dV7sf9SZj_eZUcAkdfBTBfQPUkBB9vvsPEt6EbHvpZMWESGOsiz1XfCBXKBhl6sV0Lw1QEwGhIojW78miiSR3yYN-d48B8vQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eeaaa6b3cd.mp4?token=VWDzjInIbLKlUv1p_Gmb3qprY-uhydfsETRXlhMZyayKQwTymow48U-S7TTeE0DttWKZ1RDfiCYkm-0_7uoknCQEGNkJmcCyumtxlkpn5x0AJzAGJ5a8r3yMZ2tqapFkMTbwZs6Crzpz4NExgM45KHZC3AOeNs-UpueKHtAELuYztf6a04NDTD6omUXii8uyMnpNg4Rq8wWXKPp6qKfAxcY0vIWbV2ZuEERV7MQ4WOq6BBWu8LNE5-dV7sf9SZj_eZUcAkdfBTBfQPUkBB9vvsPEt6EbHvpZMWESGOsiz1XfCBXKBhl6sV0Lw1QEwGhIojW78miiSR3yYN-d48B8vQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ویدیویی زیبا از تحلیل جذاب گل دیدنی لیونل مسی به کیپ ورد دریک‌شانردهم‌نهایی جام جهانی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.4K · <a href="https://t.me/persiana_Soccer/25007" target="_blank">📅 16:45 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25006">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Zd6Wpx-nyNklQ9JfxeXGfDBAk-iZtGI6QirlRhYKg8g9uUxUsgIyYqF1OGKWoBuKa4OmWEZukELHXBVXVz5ninBvdt1EIz9MW9njBvHjIXfo8RCl92BY1smd2nIZ-JCuPvXh9nI6pHI8mEZGalJe-h3N8RoPCM9p80OphaNx6lR4tbbCPvUEkanny3TATg2jp94j-vizgN1_eLFYWuva_HDxWelnUw8j0RxLgLSy_raLfI90XZ8QELA1R3AFIRd69D12Lp8i1-e50-nluXhQcj9gAqYYAGzQeTBei3FXEtwcFXuEl1E2U5uzk4rItTbDUssiwK4QIRPJSDFxZAnCQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
🔵
باشگاه استقلال و تراکتورتبریز امروز صبح با ارسال نامه‌ای به فدراسیون فوتبال خواستار افزایش سهمیه خارجی تیم‌ها از عدد چهار به شش شده اند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47K · <a href="https://t.me/persiana_Soccer/25006" target="_blank">📅 16:34 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25005">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F46uVxAl6N0y0RQ1TPJ892GzOfUiaScOjGBC5j2yG0xygcoRD30PXpBW5RKp65EzLhwz8PjKVcrEwkMJCfRCyJR0vO9PlsPQkAUvEI4ET_PM5YBhYrQcEASDm9C8VfdtXqnAPpsJS6mhq_wxj9jCGVL0fht0de4W5PTvuES2tgN0zMXQ9bSE0zxo3k4OSzZ-WIZ6-ng7PwG71aohjjgeMgjyg4BO0-Ljzb47TY_ZfRtXkE-6JGHI6qplMamLbPAZYmGKzJU86fwDP02SXMqRBr70rYvvSFPs8l5Cr20YceUzav4wQViitxaemLvRJB4PNvtbfEtFzXQRhRPX74woKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇧🇷
#نقل‌وانتقالات|پیغام پرز برای وینیسیوس جونیور: یا تاقبل‌از اتمام نیم‌فصل قراردادت رو طبق شرایط باشگاه تمدید کن یا قطعا تو رو میفروشم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.5K · <a href="https://t.me/persiana_Soccer/25005" target="_blank">📅 16:27 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25004">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8aa6c0365f.mp4?token=lTfFnXMuzfR34rOoMpJ7tYBA6dgaCTPKV6xh93G_PuDiudXs-EE7Jt5XAuhUgelU3Jrb-wTyFvSgIuCCGzFTUPBBsbsTNsUhzoAgSwTB1WqlvW1YVNvEFWsXR4JLsOidvRVLscyZ89d6WuXvVmmYos6DZ-JBAfNTsiQANWZE7xCvr7ZjeEtULe8FhrJkLRIbiRBuZ1fKiXMDe3ADgzCqRDkQbA2A_A7Dl2CvoWb56GjwpFWDCtFtOz6AUCSi7dhvn8wmCvjSSgnIJgrc-X1fkQhAb4D9Y0mOe1FVOWnWpNMiOSAR4SH7u3d99JN7bzZDdHiAm6eNknv3RLhKNX2Tlw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8aa6c0365f.mp4?token=lTfFnXMuzfR34rOoMpJ7tYBA6dgaCTPKV6xh93G_PuDiudXs-EE7Jt5XAuhUgelU3Jrb-wTyFvSgIuCCGzFTUPBBsbsTNsUhzoAgSwTB1WqlvW1YVNvEFWsXR4JLsOidvRVLscyZ89d6WuXvVmmYos6DZ-JBAfNTsiQANWZE7xCvr7ZjeEtULe8FhrJkLRIbiRBuZ1fKiXMDe3ADgzCqRDkQbA2A_A7Dl2CvoWb56GjwpFWDCtFtOz6AUCSi7dhvn8wmCvjSSgnIJgrc-X1fkQhAb4D9Y0mOe1FVOWnWpNMiOSAR4SH7u3d99JN7bzZDdHiAm6eNknv3RLhKNX2Tlw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ویدیویی‌ازهواداران تیم‌ملی‌مکزیک رسیدن جلو هتل بازیکنای‌انگلیس‌که‌نتونن خوب استراحت بکنن: بامداد فردا ساعت 3:30 بازی مکزیک و انگلیسیه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.2K · <a href="https://t.me/persiana_Soccer/25004" target="_blank">📅 16:22 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25003">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">‼️
یه‌ویدیو سه‌دقیقه‌ای‌جالب و تامل برانگیز درباره زندگی شخصی و فوتبالی مدافع تیم ملی کیپ ورد
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.3K · <a href="https://t.me/persiana_Soccer/25003" target="_blank">📅 16:08 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25002">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hX8bYjPvooNIZqhhe3Svb_CSqH0xpqdH8SSmQ134LMxVcF9NSBbj_wvb5ZNJzkCkD8t5XpGghUwPW4R-1UynRE-j_u8WZ17uV91x9iwK0ECDDZl0eGKvCyIqdMGkVoezfswJIR8cvB8Zl8_aJ0jetukGZmqAOIA4xry9bajS58mP9qhDgkjWxIGs1zpDXTFMh3xZ8g5IDO8903_WY-JCZqvqqrOKj5EUown6qRXRv_4bLnVHFUeDlowWJdUfQ7LDtpCzUzQX1BAsFuey3K8IoGzsz3iSKHWyGJer0HbiHFnBh7Of_rRVXwO0EJua3hurQVFtdEoklP0Dk89L74-TEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تایید خبر اختصاصی روز گذشته پرشیانا
🔴
مهدی تارتار سرمربی سابق تیم گلگهر با عقد قرار دادی 2 دو ساله رسما سرمربی تیم پرسپولیس شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.6K · <a href="https://t.me/persiana_Soccer/25002" target="_blank">📅 15:51 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25001">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NNkIErq-BzQvYUailM3Ibw1InEO55_mT5ileTNh0kXVDPe8IQ2EN_1JJrA3W2jV7zW0NkmvHYQMW7BXEKdYkcbzJCrgblShxFJWh0uGNnFY2ipjJ-U1_FkdXtDhE4Tkp9MMwhFFSaudxLi9msuGZt3rvpWZxKlj-jvBwKCzUD-z5iy96m1c9rn6NQ8O9qQndX9rcavPXz1w_hnWwI7D1c8JFV555hNkgSxMAVK2TLKQn-eUSkQgbcI5W5CH19_I8oPCiKI_BBfRLWgZMhnFo1O369A-RghzLtA-l70ycgxiwU03vcWvV4U-oqFKUxeqZaCF50k2ASjpDf52Pq0w0gQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی؛‌طبق‌پیگیری‌های‌پرشیانا از مسئولان باشگاه گل گهر؛ روز شنبه هفته گذشته 9 خرداد ماه؛ پیمان حدادی جلسه ای 3 ساعته با مهدی تاتار برگزار کرده و به اوقول‌داده‌که درصورتیکه باشگاه با اوسمار ویرا ادامه ندهد اصلی‌ترین گزینه هدایت سرخپوشان شخص او خواهد بود.…</div>
<div class="tg-footer">👁️ 47.4K · <a href="https://t.me/persiana_Soccer/25001" target="_blank">📅 15:39 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25000">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/avWyeT7OlPF6-QffDPliBrgDOjc7_UVWjYOubK67NCqctDsMI1Af6lA0LZlluThsauxxXjKmYGDe2qOmYPBNWHBC29yClhh7HnTNEFM0R6SrugorLCB4pnweRsKk0chUJJCPu2CNGecsr3doIh0_c_cEsU5CV8XgXn3kchIHh9nliqjjU5p-jyg5cQsaZW4ukZ5BDGEoSnPVf-AcsUBcElJs68dadnYYbtZLK_kWsPcO7hzlzBOnHNxlh-399ILrQxZBnpfRPPp-nuVJ6mSjtcjTA5tPeHciO3bTZ0nkTdr4knwCG4XRCfTs_OsNY5Xl2O7DxuKYzaBkWvHUQ2NnvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#اختصاصی_پرشیانا #فوری؛ باشگاه گلگهر سیرجان که اخیرا قرارداد مهدی تارتار رو تمدید کرد بندی در قراردادش گنجانده شده درصورتیکه باشگاه پرسپولیس این سرمربی رو بخواهد با پرداخت 20 میلیارد تومان رضایت نامه تارتار صادر خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.7K · <a href="https://t.me/persiana_Soccer/25000" target="_blank">📅 15:36 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24998">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Ti07BJsVS_nZ99rFz3xH4iImNLuKOsWcXiDfzNWh7vvXZ-xerSxqRe7j2S8pq_F3CiuYxxkRpH-TZm_Le-Ybt9D2bS7Jvu0jjU_KCx6PzKDP679fe24tek5VDDH8QZyhvdAcSPSx4mEQSjbOX6p0j0UgonyAntI5yz0XpbpZrQ3KJommpP-JNi--nmf5Ddpn2vjXMXPmnsPCkQ-pZjNMm7_N32aICnhoH3eZ34fuESgnBGtvOnprDGuTIYFxooGHTBCGUSaNSYQvhvL7KRY-jbcaTXkKeUYcLud4r_hPcvQucBpa9cmyh6KnYkhISNRMt1BYt7oQZv7oYspT-QPSRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uuZm2yWbykqKtGoJ8Bq06cJs6DeZqsrew44_XuZpLzlbMjF-yRzBtczAm4oUbMxxRJ8Hh9iIk2THAVq4Lx9ELdQk8kSlQxeub9spjyGrRs91cXK1evjJAC3sRo8QUom7c9GaKr509Bgyb4jnCbxCYppSn7Rgd8Re8GKxzSInDKLKBMsDe-M6PSNQPh31jMU3Ipfewu4Jibz8BJjfkMqVlCpj84DlXVUW_ShWcv6zPU_xPaO6Iz_KlKpHruMXiRPLAx1zK-HNPkmL00edbeYiSCQ06yS0L5uYk6DWxIVimmIP70zhdJIYE7A0TBjuU3m6C8rTqbu_3s8FbFKwwLOsoQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🗓
#تقویم
؛ سال2006 در چنین‌ روزی؛
جواد نکونام پس از جام‌جهانی 2006 به‌تیم اوساسونا پیوست و به نخستین بازیکن ایرانی لالیگا تبدیل شد. او طی هفت فصل حضور درتیم اوساسونا 197 بازی انجام داد و ۳۱ گل هم به ثمر رساند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.4K · <a href="https://t.me/persiana_Soccer/24998" target="_blank">📅 15:31 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24997">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OEjSl4kdZtmJmmOICj3Ppzhrf_-w7rkemXGTIEGlNNLMI4k1xJDsf4W_MXJjjQmpwhcRJtDBOcQOAa0dCZfgsRIoD-ZYkoBHqQfrrs_mIpurBJFD_fkJIecqmD_sA3xT-cbwARGE7jK4nwfXRKVJrFCSl2wTLATPJ2a7qtu_eXoVVnrWj0pqGgdUJIMl2TKrF5z7D_sxY93Y0suVTIg08Jo2tQDjWoVD7p6dIiE1k5UgEuU_bibmrXmy1Wi-l5VTX-4CXPW_RNuUWTVqYM9D1hEhfhyMhdleht5ABSrQfWNap9jL75gUIBRe3LNGuKJNwS9sBEzIuD2MBPLlDEarLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
✅
🔴
تایید خبر شب گذشته پرشیانا؛ با اعلام باشگاه‌گلگهر مهدی تارتار از این‌تیم جدا شد و بعنوان سرمربی‌جدید باشگاه پرسپولیس تهران انتخاب شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/persiana_Soccer/24997" target="_blank">📅 15:17 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24996">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pMNsohj7uuSJgoGK0dkwjo9wWfnUSfobd6sgK7a7ZrDJqOn8uWaKMObeAyB_aIbPE5BKVwLwGgERCHedJh6aoso_s0L421bsNCI3m_FKNm1MNIgX9fu_8x-c-RflCmqfApKwY6wMgqcTBckXB-TojkanNi_bhhLsEFMQoTk8mB6lbpRGaMT20hqygmu2aEyzltzTWTJNMECWI-vo77n-HHpg7sK1UvFPddoad8_QWiA-ky-KJij_SvSLOmNMY59DK9jmouUIkVrlWdrmp9oGkJd74rdFkbN83WPIoBop4pbFafP2WbpmbSZ3EFu2mpBmXeDlXFFOecKOIa7WJ95unA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی #اختصاصی_پرشیانا؛ مهدی تارتار به‌حدی برای نشستن روی نیمکت باشگاه پرسپولیس ذوق داره که به پیمان حدادی گفته خودش مبلغ 20 میلیارد تومان به گل گهر سیرجان پرداخت میکنه و قرارداد دو ساله خود را با پرسپولیس امضا میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.6K · <a href="https://t.me/persiana_Soccer/24996" target="_blank">📅 14:57 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24995">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WbQL76zz002DGfNiw-H3PE4Uw6dHyj3RD7pRLWuKItk0c5HD_t4rVUVQnC_cNLTwXNs8hDC97IxZqNFddgc6N-20v-U1X7_RpSN-c8yIuPKft624GGaNK2frxkE-LX6uZKnKHoHJ5-8msl3z3SGFq0pK41jh87P0iWPlnXw1sUuT62N8VjwKYuaOx3P2X5ztx2a3ksxAsw4-S_zQm-ukX3FXZ-a6TeEvIW3hfZlYp1bdZxrsftpvJEBAmBXoxT55_gArJS8dT1Ca4defsRuXC7UxK57ikhz8oDaZ2D0iEKKd4wpvzPXQH6yROPK9Szz4t6kekIDUE7ClDSrcLVAq_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه دیدارها‌ی‌‌ امروز؛ از مصاف فرانسوی‌ها با پاراگوئه تا نبرد تماشایی سلسائو برابر یاران هالند
🔥
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.1K · <a href="https://t.me/persiana_Soccer/24995" target="_blank">📅 14:43 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24994">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jMUZM2V8jesUVdNfzIyDBYv0rPvPBW6L2ngyeU8Cph91PAsV8GXzgVimP21A66IqCCamfRxYQTgjdKMbuOqigWm2X1dlnnL5ZOYoGu-9peYTJTa3rvng5Hrwb908xE8BS3qcJE7KDhxwTIUiS5p0UijQZBwynUYniCALhTi8PDqrG13UB11G0yTjXAj0xj6nPhlkIn3YxQK_RQ77hatLU0wdgyNR7hCHN3XlNQnIZk2LPeQ8_ZKST0sOnyc6tQ95lXh-y_40qrj3cU3jXQzJbO7PFHaqznbY812n9ImzVIfOAEhiPqijoG3YKY7--u8aTfKxirH7XAIfB8RCFFH5hg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
وزینیا ۴۰ ساله در جام‌جهانی ۲۰۲۶: ‏۴ بازی، ‏۲۳ شوت مهارشده،۱۸سیو، ‏۷۸.۳٪ درصد سیو؛ مردی که ۲۵ سالگی وارد فوتبال شد و از رانندگی اتوبوس و برقکاری رسید بدرخشش مقابل‌آرژانتین و اسپانیا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.6K · <a href="https://t.me/persiana_Soccer/24994" target="_blank">📅 14:31 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24993">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kvpF9MRsir-x6xfzMbOad9rjLmlVUYVaQcEoRX9M74tw6OK5pJb7JhMLv4blj2T_8A7erpejHBP41MOSclxX0JHyzjOgr8Lep-8ZMIUmfHNGaBevYCf6rI0hFRtBoSfioFgytgVtiBjU5KEsDZcR17MOO6tBmL5DHem2iohMrt-BzMYd_ghSYucNGpHVMfmgm5q_0CV9aHb68Nsm009hIgR2jvLqedFJ0y4C-oL0fD_2E7QndfQNsMue7eIYZlBzsFlQlp3lCOeCXdnw0NzaJgmw2QivT7bTtAMtCrPO8QncmSanxJIl_0CLycvJTpnXZ6AOG7HRjPlfzpbLyau64w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
مهدی تارتار عصر امروز مبلغ 20 میلیارد تومان به حساب باشگاه گل گهر سیرجان واریز خواهد کرد و با عقدقراردادی1+1 ساله‌راهی پرسپولیس خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.2K · <a href="https://t.me/persiana_Soccer/24993" target="_blank">📅 13:52 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24991">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z58ebWYbUP7eIICL-3gvA580emRZi2lq4JUmyjkmRz6aN0-RA96m8W4dpehVli9XoTcQnuXzGQFpI3ihuBVznnpmu6nZwmXgDttX4KQRikj-82FqRRa-9UR0mbx8T1v7y75c2zEP829HQurtIAQxwcasnBaGJ5FOZMk_M7BbHudjw9uhyYFlV1IDE3YMWdUSieB3RB8JBA7OLh4Be9tvzA1hxggWLcei1kOaTWk69Y9Rk68Ihho-n7W-pmyxwIh88hB9yx4iuxEjGvi_7HedVRQBJVgnDf-mv7pA5CTfeLZL0y7wRJaZcnP3lmjRb3G0KujE1MJol4D3n4FJwd9_bw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
رومانو: ابراهیم کوناته و دنزل دامفریس با عقد قرار دادی 4 ساله رسما به رئال مادرید پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.9K · <a href="https://t.me/persiana_Soccer/24991" target="_blank">📅 13:42 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24990">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gLLImF3QgPDzVgq3QXV5KvIq8oHgEKG4bmi56vgbEs3WY4SUQ8RBUGNXL-CV0XikYan6cm6w-4P4_nWz2azsEo4vOr-Ny4AaL1GCO-WxJ1OI8FE_WkUZVDnUiToABfkpwdmP7E12r42xIBLchOq_2vkhnQQWaRymFX-zjDIN0JRhiV_UFa7N04e33fJY6DVhT9QapREzwzzD-9A22y4dqUhsH6obXWx45w92AmHIfvhC_H-r9WAzmfMntOXTrco-UVhWuHjCzZcuEvUQATX4q2AoS_MWaYqI0N2yHYvhYshs_ayOgURI8HiN25mBFcFTeoHQ635Z7y9Xzz04M1UamA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی #اختصاصی_پرشیانا؛ گزینه دوم باشگاه پرسپولیس برای سکان هدایت سرخ پوشان مهدی مهدوی کیا اسطوره سرخ پوشانه که مدیریت باشگاه پیشنهادی سه ساله با دو دستیار خارجی به ایشان داده است. مهدی مهدوی‌کیا از مدیریت بانک شهر حدود یک هفته زمان خواسته تا پاسخ بدهد.…</div>
<div class="tg-footer">👁️ 53.8K · <a href="https://t.me/persiana_Soccer/24990" target="_blank">📅 13:27 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24989">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fiKsNLW0QbyV3QUtlZCvjpkYs0i-hMtWBeP4fBEhNcJw6NwZOMOu-kvkPJ317ISYl6K-fFcWnmetkbqlbXQR7ycKGqrRCEiJLX1ErbxpYkTI9XHKwD_8qdIec_n6ZU-mCGILAeY0FcSCsbb8nYHaWvwBhXs2utfFEEHC6dfA4fECONWf4mby0A95jAqBoezAmMPX8yRst0CYHsluqOLyh1JncCXh2iYsBchHtsTY0xT52LPW8gX1thBVoEOfZLMp12bE-af4Ldfodn20_nNtm_o5XI1r7YjXjW30OmX63hJNcixGyvGJz5JpuO2EDqnW49e-H66WI4pMSpHO9Cpuaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
بااعلام‌رومانو؛فدراسیون‌فوتبال‌آلمان با ناگلزمن سرمربی خود قطع همکاری کرد. یورگن کلوپ اصلی ترین گزینه سکان هدایت ژرمن‌ها در یورو بعدی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/persiana_Soccer/24989" target="_blank">📅 13:17 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24988">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RpyLQCXXH11FpYLJVUHgtDoqY5jbAA2bP7h-Owi7m1FVVa0wd4QKlDK391VbYXY7JZjQfZqQc1sgSu914K5BAY93JEkFFdA03uALTAqWpF6G2k4-P-2J-6rrLwR8mPqkROVM-AT4dWXVf0zUr-t1of-e-4QL5NAuna3dq-3_tcyy0SiZ89Njfu4YxH_9kFakZBiCVJgwMkQ2BOf0C5yjLJpo3TS8_dv8hrBsLd-LksDzVaSFl5FER1gEZ4iVC4NE1Ft0eeQVqJvt32hjF0-QsVP7S6AL1ZyKlN6HFU8bCFnZtGJ2FpCCqD7_ZTu1DxID6b2WWfabGToxK3spNKvYyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
مهدی تارتار امروزاگه‌بتونه‌رضایت نامه‌اش رو از گل گهر بگیره سرمربی پرسپولیس میشه. در غیر این صورت مدیریت‌سرخهاسراغ مجبی حسینی میروند.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 51.7K · <a href="https://t.me/persiana_Soccer/24988" target="_blank">📅 13:14 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24987">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kgJSSH-x5CLd4OAUjeJXk0lBOJ3Bc2TlAcWlJst3CljQ02HB_ygQCr0BlHYFUl5wbl9TuLeKBS_Mxj4kCU-vCTRoiwueIHI1xL8FWfSUoGpnmS400MTaK4pnWaEeWvUk0Ta_OsyPAAf1dv2zRcaCtT_kbY6sURr8OOfTfODOiGos9xk2H5-ODyhXA7wBEQAbZBQRMF5Yq-N66R_hlcOGZwDMqdGak7VqcqXXzl_74G9mbN_x12ZE6cjSH7k_Jo4WG66OZ6-5Yz7KXuF4E6UWimT53tdGfCsQsVZ1e_tvOnNLY-02EnH1n3kbz8I2uEwWbWNrh0p0xx9A1zupoYumKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی؛‌طبق‌پیگیری‌های‌پرشیانا از مسئولان باشگاه گل گهر؛ روز شنبه هفته گذشته 9 خرداد ماه؛ پیمان حدادی جلسه ای 3 ساعته با مهدی تاتار برگزار کرده و به اوقول‌داده‌که درصورتیکه باشگاه با اوسمار ویرا ادامه ندهد اصلی‌ترین گزینه هدایت سرخپوشان شخص او خواهد بود.…</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/persiana_Soccer/24987" target="_blank">📅 12:50 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24986">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YfX7clEZO7FMzgjW2tGhiugKI3DvZw6EYb1q7EiGZw3KPjJ7OKiGnCmvALCbsKgU61mmfHO39Cxb-fYaUYOzbnGHJeZjFazpsrggVXkkf1-AaLtNSo57-w_o1LCoOPVtHQXAfCF5BIqF51LJBEP05kr4gf2Fl4zh4O9-d1lIpV5H6eyacLeBqrsNCAeWNJVEakNyaeipI4FPyd6cuX664pa9Uo34rvKolnQ4_Ymo8IGBsx3S4_N0hNduiGwq3Z1EmavqwH_pXUO5bIS_HPyp_0PAC7NGhbP32exRXIRWAc_Nac-iBwpypxF9R4WnSD30xMIBTPaXNJm5JvUxVZu49g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
#نوستالژی؛ یادی کنیم‌از مصاحبه قدیمی کارول سلیکو، همسر سابق کاکا و علت جدایی‌اش از او:
‼️
کاکا هرگز بهم خیانت نکرد او همیشه با من خوب رفتار میکرد و خانواده‌فوق‌العاده‌ای به من داد اما من خوشحال نبودم چون یک چیزی کم بود. مشکل این بود که او برای من خیلی کامل…</div>
<div class="tg-footer">👁️ 55.3K · <a href="https://t.me/persiana_Soccer/24986" target="_blank">📅 12:34 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24985">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jlqgfqv3fHrbF2A7aOswnRkTXI7RZtKsET0L3xQFYMLdPkz1sRRYlqm_XgMJARBIb3JghuMtBwM0DlBQqsXwEfNZlkxHVU20RpY8Ywn7cgZdOfA1Oy8i9O0MTDgOxfVINT7G3SZM1SBO-JGmOIlltULTrxHfTZjsKzSMU1E4JF7Aq8ujjY9K1cg-UuxPkzgrB3n8PGn0MhPWKTj7GF6hbLfu9aj_JEdzOkQkrj3RiIrG6_QS5lHT85sDHIh8OoCWxIa37bJRMrcwchYW0yfuf95z6iUGZHKnZNjlx9a_l7MS2jatvSSXiBw1G8MDQyghQajqJdHY3nlesFj_P34mGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#اختصاصی_پرشیانا #فوری؛ طبق‌آخرین اخبار دریافتی پرشیانا؛ عصر امروز جلسه نهایی بین مهدی تارتار و مدیران‌گلگهربرای‌فسخ قرارداد برگزار میشود. همانطور که شب گذشته نیز خبر داد مهدی تارتار به مدیریت تیم پرسپولیس اعلام کرده خودش رضایت نامه‌اش رو از باشگاه سیرجانی…</div>
<div class="tg-footer">👁️ 61.1K · <a href="https://t.me/persiana_Soccer/24985" target="_blank">📅 12:22 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24984">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K0JwJyhKE2JMuYNT5zdHg_mwSHYG2nTI94Y4xz7FEs8tpuxzoL0DXwQNxY94tIrqXXD5BQldL9H4Zzm9e2rPonYfV3J6O1ymiKSzoVnBVgsdM5Vyf2Wyj3DO_AxPdGFkCGEXscyKVgsp-bFknpyCr9L7RZbwuDhPZwobdEb_CDeyv5LGNZuK5o1M9bGg1Kf9d-DLvem09wk4catXofQbW9yJ8Ou0kkduzmJ1gMiol3na7Jb31-qQboUq_kjOAS7_vZI9Jx4-xrpmxMkhvOuN9KDokU78OFqiFwtbDjJgb_8rtEQHF641xQXKtJ71dNlWsBQOlCFx7X9THAZt_QwSQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی #اختصاصی_پرشیانا؛ مهدی تارتار به‌حدی برای نشستن روی نیمکت باشگاه پرسپولیس ذوق داره که به پیمان حدادی گفته خودش مبلغ 20 میلیارد تومان به گل گهر سیرجان پرداخت میکنه و قرارداد دو ساله خود را با پرسپولیس امضا میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 67.7K · <a href="https://t.me/persiana_Soccer/24984" target="_blank">📅 11:37 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24983">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TKZSwsRroy5u0svbuL_PADa3fj5STxgKuyP3cvpP6SXEeQXDjQNVCqdEQjCow-wyr2UiqiQv0X5CWJ4I5LAYgLW17eXN3y7SAap1X6HlRVAiJYgf_CbCdr8KqIPVNx4H-WGKP24l3EJ0i-y55q8r_88XHI5IlhO-Nv0Otos44gSmgiPx9UWjIf5yFaNKXFZwa424GOv3dzXgmuUDARu1VxdIprhZadtAL9g4cJb5C0BxJT1eDsnGmsiaC23R5OQsLHvkHKUZysx46fUER1s5rY9n1Z2cyt9I5W_y7QUueqppu_deLBdw2h800NYcXH0nONxXUTlMiq8r3VHddEfuQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
وضعیت‌مرحله‌حذفی جام‌جهانی2026؛ فرانسه و مراکش در یک چهارم مقابل هم قرار میگیرند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 66.4K · <a href="https://t.me/persiana_Soccer/24983" target="_blank">📅 10:20 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24982">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NugUPCNjoFy118x2dFXZJmRXKFHCT6xJ0homBAArrfT6m3PwTP1u_orlGHvsgu40UZIboHgJXy2BU3EJIWF7WBf-s7fwG6h9K2VnwYsecjXz8CRZzPgJ6bPT0K63we7ba24dgM_VgC9ABcKvu6xxuJVJIoYBU8lykh14oUNgVCL3BduDPYWYZ8-Q_SWQZIWQsIx-DlQiH83d_2unb0O4O5L8sXonRIXLaKfRpM8jrZ6Ui0_udssIg7FTxNFhSMLra1FCh8nrfy_I5VyE7KWW5nS5Q1y5vwXqy8cszMbTn06ZQ33_DJU3A2W4ELpVG2hjGkLnVdK-s3A3OUaxrIESYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
‏این‌داستان: امباپه‌‌کم‌عقل؛ رابطه‌ی کیلیان امپابه ستاره فرانسوی رئال مادرید با دوست دخترش، استر اکسپوزیتو باروشدن‌خیانت امباپه‌ کم عقل تموم شد.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.7K · <a href="https://t.me/persiana_Soccer/24982" target="_blank">📅 09:57 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24981">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ivHkcULFR4aG8T3x6VdJQwUGRPNSfwEJFFNoWSoD5m9FGagPl9rFwQQoopPOX4S1NvwljM-5r0dDhUNX8Zl8EajWqwQ3AQz_k1Kowqvu30KK3JfFQZxthN-OtsNhVc0uTBb9_2JQw7aWF2LFi49J5hndx3dn7c_p892Sjzev4Aidudm4gXCLnI9SgdhgV5LmtRuLaY5tyEXTFHXrbhqPcZrWD5vKSCX3gZl_XdQy-jr39g9ytDL-hGiPzy3j8qmTjjx-VkhPr4Vux2IN-qFw7TLLAXWKdllwBAefqZ99oRmgs2fIyGw_SxeNWKX5MgzXRrxLUq727FehHBdC88WpoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛باشگاه‌دهوک‌عراق به درخواست یحیی گل محمدی؛ با سینا اسدبیگی، حامد لک و محمدرضا سلیمانی سه بازیکن فصل گذشته فولاد وارد مذاکره شده‌اند تا درصورت توافقات نهایی این سه بازیکن با تجربه فصل آینده در لیگ برتر عراق به میدان بروند.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/persiana_Soccer/24981" target="_blank">📅 09:36 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24980">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7875374a88.mp4?token=giEoLwoNOdxzFiasT_UhEPMu9YfI7SXxEw0feZLn4sfqJsyht8EFUqe54jnLEN-kkC4vUAIzUUyQ1zFuJz1uYzkPwSTwcDkOTnMtUy7tlBr2HSmT6YYs8kRTUh2MG2KEU_L2nUH8hwDlUF6YAExwv3NgGh3nfbrZ0kUyIQ9kihaybn4hMeiaRNWMfQte3HMpii8RbAnf4TC4TqlSdhMiTfkqualKSbkHOkcVfoSxrC4etAdz_horckjRnGRb8HuyOfHp1OwgFSOPn0_GK-vLhy8OSPeztXU_w_bhEgkyL_3LHoX9k9DLgzJn8LN_qFEuumOxNbNk5EP4ucvRQU2O1w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7875374a88.mp4?token=giEoLwoNOdxzFiasT_UhEPMu9YfI7SXxEw0feZLn4sfqJsyht8EFUqe54jnLEN-kkC4vUAIzUUyQ1zFuJz1uYzkPwSTwcDkOTnMtUy7tlBr2HSmT6YYs8kRTUh2MG2KEU_L2nUH8hwDlUF6YAExwv3NgGh3nfbrZ0kUyIQ9kihaybn4hMeiaRNWMfQte3HMpii8RbAnf4TC4TqlSdhMiTfkqualKSbkHOkcVfoSxrC4etAdz_horckjRnGRb8HuyOfHp1OwgFSOPn0_GK-vLhy8OSPeztXU_w_bhEgkyL_3LHoX9k9DLgzJn8LN_qFEuumOxNbNk5EP4ucvRQU2O1w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🔴
#تکمیلی #اختصاصی_پرشیانا؛ مهدی تارتار به‌حدی برای نشستن روی نیمکت باشگاه پرسپولیس ذوق داره که به پیمان حدادی گفته خودش مبلغ 20 میلیارد تومان به گل گهر سیرجان پرداخت میکنه و قرارداد دو ساله خود را با پرسپولیس امضا میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.6K · <a href="https://t.me/persiana_Soccer/24980" target="_blank">📅 09:13 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24979">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cmcB-C4VPOeBlCsxRqlfD57rC14Ei5HXS3xsPBft7d6s-YUy2v1JoP0cw_9pPzY711caiW10M4cVWHwThwFY1YbpjwyRlSdYlD3GYUDlw23dGTeFTCNIOkHiGWnel61TKvsax7NjQZvbH3PhlXSjKBFXH0HSBPZPirgAh-a_1nbIG0YyabrF1zbqZ77Leo_aT88tLgysX2LF1dK6r-OeTo0OMhClY1tWpzdleHFHo0XtN2C0uE84IcQLzEXOQAPtiYF-C3fKuCuqkBjvpCgcXanpEqn6A-4GQaazPv-ZQfyMsaZJHLV5IePJq12NcWkw_XFP_UMMQie2c5wsziV-DA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
گائل کاکوتا هافبک‌تهاجمی‌سابق‌چلسی و استقلال در سن 35 سالگی از دنیای فوتبال خداحافطی کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.2K · <a href="https://t.me/persiana_Soccer/24979" target="_blank">📅 08:35 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24978">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0cd8c901fa.mp4?token=tRyCL1FwPiqMRyJTE2DixcKkiIt2c2WcHKMYzvIMRHhTDakTqOqaQnNs7lK6YMKWAyQM5vIca4LKgOv2U9ZKcuY4QuaIpuh3NxHZj7ETxx0Z83DrwWTPQkZY-T_FVOjKN2comcburXEjFOHBb1Z4C9Xy3TrpUFdHiYE_5yYg6cz0UHcjZNRAenqDgaPD2v8Li6f3fSmlJyolk3U1aPSE3AT8cW43FnU5IjPvqwyIcqCdCN3iHQCi1D3wQ0da62LAjQRruKtlVsORKqYfOv2Q_WnxOIskERnsEJHl_TO9NOx2nStGIAB9JcXODwiV0FjP5n5R2uwHcga0nEQ1c5DQCg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0cd8c901fa.mp4?token=tRyCL1FwPiqMRyJTE2DixcKkiIt2c2WcHKMYzvIMRHhTDakTqOqaQnNs7lK6YMKWAyQM5vIca4LKgOv2U9ZKcuY4QuaIpuh3NxHZj7ETxx0Z83DrwWTPQkZY-T_FVOjKN2comcburXEjFOHBb1Z4C9Xy3TrpUFdHiYE_5yYg6cz0UHcjZNRAenqDgaPD2v8Li6f3fSmlJyolk3U1aPSE3AT8cW43FnU5IjPvqwyIcqCdCN3iHQCi1D3wQ0da62LAjQRruKtlVsORKqYfOv2Q_WnxOIskERnsEJHl_TO9NOx2nStGIAB9JcXODwiV0FjP5n5R2uwHcga0nEQ1c5DQCg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇫🇷
کیلیان امباپه خطاب به تیم پاراگوئه:
اگه لازم باشه دستمون روکثیف‌کنیم و وارد جنگ‌های تن‌به‌تن بشیم، این کار رو هم میکنیم، ببخشید که این‌طوری میگم. ما اصلاً مشکلی با این قضیه نداریم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/persiana_Soccer/24978" target="_blank">📅 07:15 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24977">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JP4V9LAN3bpTz-1J__QM1LO1U_a5mVra0Yy_YPZwD3GUjs3M2Gi_w7LXQWmy0vtJ4nZHRfuRI9qy_xcb2IVp-nL43R8fHl-7XJl7aJelw2m8J3tX77KucOdymKe5EAochKurU0AxLDn31jTMx2OyGqSWI5IHOwBSzhSUXc2wHAozFwjFOcpfCpbPEwv_PuBsRyIsLqAeWUfGgWNsNGpdWu_k26zqKJZ0UX8tCzIdFR7i1eJDLCFoHuy6nO5gspdAjFHt_fmXIlKy0f3zO3P-NxVci1yZnksJgsTHsFKJnVO0w1fN2_t4evZ48aC3ukQSiRANHo-MZBClq2AtJFyz4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
وضعیت‌مرحله‌حذفی جام‌جهانی2026؛
فرانسه و مراکش در یک چهارم مقابل هم قرار میگیرند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.5K · <a href="https://t.me/persiana_Soccer/24977" target="_blank">📅 07:07 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24976">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e5736be2a0.mp4?token=CRxVeoFSxHRmjoU3drE7_VE16llTrc1XplruPlM5W2zp2rC6mT8-PHdRmM9ReF7jmaASAlsO4IxBjNLgMUAZTGtWKMH6zQLIotLLby7nIJp_OhCd3_Lgs1dRHX5G6PABPqr_8yEaa4K9OR1zlVmgrhvPUj16UhaGu0jIs8yUTYYNf0VKFVMun2ZJKHVp9citp50l-3CbLCw_d3UzjX1p_7RoJHFyw52UiH3yYW9lukqdZWW5ynxTBLQrt-vwdyYbbMMcMRM_jHplthPpJU07pRbuakJgP43y-tmab-aKMFca9c7ynerbfdzTwCkC8AebBH6191EU1z-iAyZwsXSIQQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e5736be2a0.mp4?token=CRxVeoFSxHRmjoU3drE7_VE16llTrc1XplruPlM5W2zp2rC6mT8-PHdRmM9ReF7jmaASAlsO4IxBjNLgMUAZTGtWKMH6zQLIotLLby7nIJp_OhCd3_Lgs1dRHX5G6PABPqr_8yEaa4K9OR1zlVmgrhvPUj16UhaGu0jIs8yUTYYNf0VKFVMun2ZJKHVp9citp50l-3CbLCw_d3UzjX1p_7RoJHFyw52UiH3yYW9lukqdZWW5ynxTBLQrt-vwdyYbbMMcMRM_jHplthPpJU07pRbuakJgP43y-tmab-aKMFca9c7ynerbfdzTwCkC8AebBH6191EU1z-iAyZwsXSIQQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
👤
👤
این‌روزها ترکیب جواد خیابانی و خداداد عزیزی خیلی‌سمه‌خیلی؛ از دست‌ندید. این بار خداداد به جواد گیر داد ولی دهن سرویس کم نیاورد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.1K · <a href="https://t.me/persiana_Soccer/24976" target="_blank">📅 00:56 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24974">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e_4Ifa68wARtkXwt6MBnG7Gpp4fUT8zDYnEBOJTaDR6sv0saveu7BDtw7T2RLxWi30Y-QMCeyrtLdUHT06PyX2ZZG6hUwdN4pBi4lePjR0WfitUvLke4qHBHpRugoqCwQe3NZs-y7rtP2sKAwsKyMdmJDujceJjLtrALxV14LkYrHoVz_T0ADs2Au_MGb3IHrpIqfM96auBwusd-LsK-mordazGwcEDCrnijnBbfA3PVX2bUlDQfCtiezVLqBJgslgTr0JxBPN7YgallyMkamjR06NdMR4W21gU5sYtirznRnXGsn7dQgQGUlXklxRicKOVMQuHJ1iewIbEv62egvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی #اختصاصی_پرشیانا؛ گزینه دوم باشگاه پرسپولیس برای سکان هدایت سرخ پوشان مهدی مهدوی کیا اسطوره سرخ پوشانه که مدیریت باشگاه پیشنهادی سه ساله با دو دستیار خارجی به ایشان داده است. مهدی مهدوی‌کیا از مدیریت بانک شهر حدود یک هفته زمان خواسته تا پاسخ بدهد.…</div>
<div class="tg-footer">👁️ 56.7K · <a href="https://t.me/persiana_Soccer/24974" target="_blank">📅 00:46 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24973">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bw1dVwcOfk-ocCBbg02jhSIS6xanticT-f2gvGhDKamy9-NDSx6WZ7vbOqvO_keNBDJW9GRgFZ467eMTwbEx8CoZaegae82CVjpTVHBtYDcPsNz4_oM3_anP26_oBALPHTllamfbNeOvM1Xk-nZGQQPzWxsJBC7mNo1zDhhNS3CRm23urXicPq_5t9fHyktQIiOWSkqnmmTff2RhINKwLUwmri-QVWpV0Zx9KhKJQUHfYFM04zqzM_em3dkV4yV9nyH2YrIzMLXcdo16cMeiIef34ZyymzlSb88Rx-selEp12VY-mOS8y1e65jMVxANPRAhNcKma7FWwNldZ7w_z4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه دیدارها‌ی‌‌ امروز؛
از مصاف فرانسوی‌ها با پاراگوئه تا نبرد تماشایی سلسائو برابر یاران هالند
🔥
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.2K · <a href="https://t.me/persiana_Soccer/24973" target="_blank">📅 00:39 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24972">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IA1Osky6ODwtFPSANu528Qj13AHRXFIxUhfFLqWk_ZWHAZSs2w4fvrDCABiAqQkmQM8rb2qmpk3jg_ZKBx5smQjXyd6QNE02o1M3razTio_ek1yAavKRETZm0CSLfaFnk_yQC3vzv1ZkikxHj8xsyoRwqIPdpg_R44y09POU3qxkF5FHIsWaOkX8bCfmL_dFuKjF4sJ4dXfXDypdbAIz6hwT68-IpFMcx98VucEYKXJsusz6bQxB-c5DLbL7mV9qWEPvkwk6ZLzsVxnZptT1EXNxNkz8VDud6D9GVYZKvvTPVTj4xl9jcD9CVH1Gq2ISITtO4ADh7fvD0lzrkFR9yw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌ دیدار های‌ دیروز؛
صعود دشوار و نفس گیر یاران لیونل مسی در دیداری تماشایی مقابل کیپ‌ ورد و برد قاطعانه مراکشی‌ها برابر کانادا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.3K · <a href="https://t.me/persiana_Soccer/24972" target="_blank">📅 00:39 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24969">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c3Kn8-XbgVMFicnwfGmxWEZCJMp6ut4fvTWjnkE5lyNHY3YT8aklLFr1UJK0uR-6syiDWXrQzZ7EACkvgafjEc-gNOPe2A2WS8IDwXqEWGC2JcfVV537eVZi7bpwgSuLTatpzkr1HvA4zDOHqyqPeKWqukAi-cTs3x4U7A7ETs40VT-dyouV4mk9TZ92XX5D2JSGYaiW85xayjBm2f89wOlK_4fohA-MO944Z9O3SF4TpdxYvcI_okI9DDeDIsYsnLZpBxwz3h-uLypkhoDVOWg5AVskw79g7PqKGM3GiCkWYJ4m0uTfJX514oaHXMn-X0KZUlqVwn8XQechmRuvuw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
با اعلام باشگاه الاهلی عربستان؛
ریاض محرز ستاره 35 ساله تیم‌ملی الجزایر از این تیم جدا شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.6K · <a href="https://t.me/persiana_Soccer/24969" target="_blank">📅 00:25 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24968">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FhMblFjQJOUFH_ajENu_R_l4Q0e-VtQ0dvZUON8MxDWWpuVLhWRtQRGm6DH1Q0QmOoeJVVVqkSQDUIgnTr7SxJ88O7t-NMATUM4guzafnPOWG2ad-v3ZN6nm4BR0AyGz_VjCyCzaolSPQOYcMAwqMkHIEn7EkzVNhGKQ8J39Aoe5aoq1oU8vxPvxBGR14lisxNXjN1CknMPnZ0Txj1UQJiSvFjGCFg-uoINi8EwlDo-3wuC--n2Xwg0zRlvVQUfBUPbloNiiE5KUqkTlwssPklRYCmVgTQeLXqIgCYqYPx2pwtYd-kJYHl29npy4ogomoa6umbo2t2dChmi6YBssSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
باشگاه‌پرسپولیس‌دوگزینه‌داخلی برای سکان هدایت سرخ‌ ها در فصل جدید مدنظر داره که سعی میکنیم اطلاعات دقیق و کامل درباره این دو گزینه بدست بیاریم و امشب یا فردا شب بهش بپردازیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59K · <a href="https://t.me/persiana_Soccer/24968" target="_blank">📅 00:13 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24966">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i6Z7uhIQaroI5vITjYeTnWtbaR3NqEqC_YtiH0N9nWoEuZ7MrfeUuDvYRSGHstjbBsufgjqlBj5AGNOoTHqvH-WwlRRTY_ubgIdMNu3KNrZZOBXpM5vg87NfK80UFcKTW0PkdL4VABMyUnzDg7yK6vuxwbT6w3IzcPPsOpKK9BivJ8kJwbDE9exnnq0JwkxMYwwr3HTsL7FztpT3XH9Au3GEjghlc940e2uQ8GIDONbJ-XFvT4DstURvaadX79HZATiOyzF3PBnlp1rnoUQ56pl-kAyo_E0uSkHkFGS4QZJ88pxT1EC0onNW_0TE91ijKw8VxpH1EGwIMwNyXWQzBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#اختصاصی_پرشیانا #فوری؛ باشگاه گلگهر سیرجان که اخیرا قرارداد مهدی تارتار رو تمدید کرد بندی در قراردادش گنجانده شده درصورتیکه باشگاه پرسپولیس این سرمربی رو بخواهد با پرداخت 20 میلیارد تومان رضایت نامه تارتار صادر خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56K · <a href="https://t.me/persiana_Soccer/24966" target="_blank">📅 00:06 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24965">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nNMd5WZkCje-A28D4gwre_-hRY1-tDKqsjTdADZQLNSQ2mNGcML_edF60PReeT6ObV0TnRKrys9ZaUebNQIs6ZI35zT8YsRehdkDATqCI510Gd5OCo0FYhNu8N6yAzaBOGyjvB4y7AqbD0_S-xDWPnFAgqqdNun_WfSB8GcN9a5v_4g6DbKFk-aJQvdrpDiXSBuMafpCLMsIVaYc9eEDCdDvUnTD0ClGf3FcehQNGutq2MFtioeHi5HtMy-n4rz3w--rhxovEhql9O4OWrqjv3-DjmdsPvG_YnSgoI6EbKL3ie21QNyzz1gtHTbg3O8LnD-mwLEh_pA4IVcRopZM1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
#اختصاصی_پرشیانا #فوری؛باشگاه‌استقلال برای جذب دانیال ایری پیشنهاد فروش عارف غلامی، محمدرضاآزادی + 30 میلیارد تومان به نساجی داده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.6K · <a href="https://t.me/persiana_Soccer/24965" target="_blank">📅 23:50 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24964">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RScxqzZqB6R3Zg8mk95nbS9n3QTrh6sLKgN2G7Tn7vcshTGHNXYS57d-lN_gtm-4VSebvNkoyPBsIXqryeHBWYqbZ2-9P5sl12-JpOf3iRRkeQ8D9iZTC7blgvnjtlNINE39VT6dMA47bW3HSE8wpuOAWT9nXQzIpfYF5IbKhzhC4InOpouPJwcLBqg5swt3gNHtk_O4SPY7oZZu7ReDkeu6ZCvuPzfCRiYCOI2zw-19XNtOMaXfB8K5TQstUZKKy6isqlPXh-CkC3ATJKeggzLogfgxKw8ZoQDuDO0jzM_o6wf0n2_Np-0LvEkhxLwP-EMtKQNbtffgfRNJ0NFx1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
💰
#اختصاصی_پرشیانا #فوری؛ باشگاه پرسپولیس با ارسال نامه‌ای به باشگاه نساجی رسما خواستار جذب دانیال‌ایری مدافع‌ملی پوش 21 ساله این‌باشگاه‌شده‌است. سرخپوشان به مدیریت نساجی اعلام کرده که 90 میلیارد زیاده و تا 55 میلیارد ما حاضریم برای رضایت نامه ایری هزینه…</div>
<div class="tg-footer">👁️ 55.9K · <a href="https://t.me/persiana_Soccer/24964" target="_blank">📅 23:27 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24963">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NejeqjEgcZ7u9wQUOEPIlQ2TJgvhdP7mHL4BZ0p-nlbaExgyZwS4U_5xnpjHXI-wYl8WSG_3bNVKrPfpOEicnrIMiWBD9X4UMfmQySePL9NmwugSDirD1bZ59H5k0elMFzaD5lSaqG91z6lsG0TznLiYee3a2VG5R1jOGxo-Bb6a5TiISMmBP2ARElIDtfBbd_7roX16e3MaUSQDnV2haRA8pmnHrVM8Kzl7BRUN2V-Y1eypQBUbyCHd7LkFO4cA73589cRmD8GZk6e9PYN1RZONbstQXF4usISpk0lc6vLPYl2UYcJ3aYiv8qoij44tk8JBqo1bYd3gvdcgpcwWiw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
در بازی شب گذشته؛ این هوادار آرژانتین کیتش رو میندازه برا لیساندرو مارتینز که براش امضا کنه، مارتینز هم کیت رو برمیداره و با خودش میبره‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.9K · <a href="https://t.me/persiana_Soccer/24963" target="_blank">📅 22:52 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24962">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kJdmk-mOEWuMojumFfEkrdfbyQsblqBi0N5qdmIRi200yIv4c0duhWl5gCLl3f1KvyvS4ccwk4q58XzgXIrkt8jWZjURe5RBB3Eagw6qvG-8QlfJTKWR-vBnx4xEb85OihpagDxFMS7alpa7tqbMB9F4z13Ir3EJCu0EmV6GyCUmbB3lp4R66NePXFbLwy9tU5h0k7MK9v9aw_YXk6uSl8sKNPRNRC_mopPlEQtVt8bnY0uS59Sx2S62ZYRiQNi3xVICZxoUIETpqg7uwlAbHv1aRVkifwBi8RJ9WFjxYXW1wGtMker_qt231RuNrtFf7tCyZGZxMXeSy78mQihw8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
یک هشتم نهایی جام‌جهانی؛
پیروزی ارزشمند و شیرین یاران اشرف حکیمی مقابل کانادای میزبان و صعود تاریخی به یک چهارم نهایی رقابت‌ها.
🇲🇦
مراکش
3️⃣
-
0️⃣
کانادا
🇨🇦
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.9K · <a href="https://t.me/persiana_Soccer/24962" target="_blank">📅 22:35 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24961">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JNbfkuMrza2AWfzKfq1tfQwSzzeGh-lwHZhdr_TGfS6uBYaI-1C7phav8k8z4iM_gk-7Anq6Gr6ZTu-SW3UOHCVqxmn7tW34muJH3nXzOSaPRACaoth7DoOygwHy91DSFm9C6GVPf2qK9_BrqqFhT9eSEyVzi4bZb9czq_by4Vp_5iGS_MeXGSSkeqWRWVYrqkq1yC0TGryMbub3yo7E7g4ki3R4Z9xn67uoBI4UIoTm_rIz3iz-wIdAMqQNOnH_QQWmFL1YXQpN9gt9yOvezx8SK1GISixXkntPREkclEz-ZEf5moor_2G-GWjoGyVbznpg5sXpW0bhhr-3sjX90g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
#تکمیلی؛ طبق صحبت‌های امروز وکیل ایتالیایی استقلال؛ تا روز 25 تیرماه پنجره‌باز خواهد شد. کانال پرشیانا موظفه اخباری‌که از باشگاه ها دریافت میکنه روپوشش‌بده. بسته یا باز شدن پنجره دست ما نیست بخدا قسم که از ما گلگی میکنید‌ خبر موثقی که به ما میرسه در کانال…</div>
<div class="tg-footer">👁️ 54.5K · <a href="https://t.me/persiana_Soccer/24961" target="_blank">📅 22:05 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24960">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P4WAESLMvR4puQ0sIiD-lii5e1ZEKo-LE4zkQC7UYgNl3T3ICN26P9HOBSHqnDqaj3DhgFxd64vXRb7BJ_m6fnKmecb7e0oVJy2-wL4aL3E9kc6sj41hz6MXUNSQ60AvZ-cMHYhkcxJm6HEh171cu8aTE8lZGdeAfIXvc_gkzFWbZMmGFNjo_P9X8H13wWGocyCIjeOjNP_KZ4_G_RLFssxIciaMPCZm98IQc6I1hvvRqTvovUXFnbyNSDDvX6EjOrmpqsRJWUhq3hhDDTeeIXyUdimVszjDzbYkcUOYnK_RD-gRMNMwy9ryB-Dmb8DI7SKOhwcb3iqR3mkeIVFikA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
هروه رنار سرمربی مراکشی تونس بعد از دوباره از عقد قراردادش از این تیم جداشد و در حال حاضر سرمربی آزاد بشمار می‌آید. کاش بشه ایران آوردش.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.5K · <a href="https://t.me/persiana_Soccer/24960" target="_blank">📅 21:56 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24959">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sbV6diytiukzR2Xfzh0NVcbi0DGoXUHKT70Z5geJAb13E6IOInxEvJlZb0MKdkHX3ZckXVBi5t6QQSCJHm1lbK9Eb3kw_nHccTmySz_bOqtCyTOt29fkGfmMdX9mg7diNP12UFsYqGaKbqr6igJDoWF6pdmQvGLQzu8boCiiNMq0kIjKbB4M2Vdw51tjeiaPod9Uf6Le49vwGpHKVqIj8coC_anKThDscknK7uULzzy_LonaYhtF6W4pFoL7fLsxg8-YrPlDfMWkvVPIWLEPfGEbu4aPKitL8lTPfTjGVOZqtbNRlesO4wOi9v9DxLDkRUqRHCixwMWjIwpxv_mZ6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇧🇷
🇮🇹
🇧🇷
بااعلام رسانه‌های برزیلی؛
کارلو آنجلوتی تصمیم گرفته بجای پاکتا مصدوم نیمار جونیور رو در بازی‌فرداشب‌مقابل نروژ فیکس کنه. نیمار در تمرینات روزهای اخیر با انگیزه بسیار بالایی حضور داشته.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.7K · <a href="https://t.me/persiana_Soccer/24959" target="_blank">📅 21:31 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24958">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GK9vlnLhAAYvyj1XPB8jPvid-p5RKRNUezSz10O-8Ro2s8w4oYYVjVSyX4fF470JTdCK-WlZsaKc8xLjGqlp-8W8Zp78_ba1tkSRSG-0YnVBM7Vg6IrJc-CpPSnlC53MEmmWQ7PeF7hdQmrga9tZK4TJAyXRzdd_eSvyeLK0nRG81niWpsRLDWhVxbAfP-X8QCV4FH7XpbLDD4cCCTf4UPZMvj5XmMizoY05nVXqd7OUXahH-sDoNGSnOZEeYx_xQXOkjlhovfBW-4RgV3gleSpwe9YrKOjcFd3cvZfuZR9bcnQHy3kRdPbFQzkuCX5mRkpyzkiSZ414TeVLSqN1sQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
منیر الحدادی ستاره مراکشی استقلال امشب در تماس علی‌ تاجرنیا رئیس‌هیات مدیره استقلال اعلام کرده تا روز شنبه با خانواده‌اش به تهران باز خواهد گشت و به تمرینات آبی ها اضافه خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.2K · <a href="https://t.me/persiana_Soccer/24958" target="_blank">📅 20:34 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24957">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p2DGfM5caw9uFiF7sP6DySmA20FTlt9GjcswCB5FWAuITXIcdiZi4m1C0AQskW-OOZMTdZ2A2NGrKA_KbbiMe-CP8Z7vm6Z31vXTWy5wjs6l0DnuHYKoBhJZmHTZDXsgjSGRhWvO8_4qtbLJaFXQZjqdZIM7fIfDAAyHfC7lmQ4KMKbCmw1lQpo_x5gvTT6EDO-Qgx09SdvULPB_lly3YnofHE3kh91Ebjop5p1hkJ0Ej0QxYTAutiVSOeg3_MuO9qakOddsTLI-DzsFH1lR0P5FXtYCD7UgcR2k4_BzX8dktMLjnZojIOXQxwNJYD_EmwuPK6JKc4zILHQvveejVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇦🇷
جادوگر غنایی حین بازی آرژانتین
🆚
کیپ ورد لایو گذاشته‌ومیگه‌کار یاران لیونل مسی امشب تمومه و حذف میشن. بازی تا پایان 90 دقیقه یک بر یک در جریان است و بازی رفت وقت‌های اضافی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/persiana_Soccer/24957" target="_blank">📅 19:36 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24956">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DAgsEotmpBpLH8iz5s_QfBpXyzucWwo6v1_yWkgGc3v135MD0hJJ_F9N7j6300uS9AM-YJYaujguwFQqUCrPMTjXNu3Ie_wm591-QoP9f-6lIKHyW1uVWgh8QHlCpLn7trqwZZNoAykaD_TVf5lV7DJ2G1fw0xpZRLHiyjz7mR-AYvEQvneMDFU9ngm1P9qAVp-uL6qLykJzWkuYB9lfCTvcdBPh5Z2-g9sX031FVPl53CQT_qyK_VrzeMlZa4Yxyq3HsjTrz-NFwmb_LqpQpmc2kWK2NamKxVjbgq2ctWTzJEJtgHdrkZtMjJQGYPa7_thldk6jyxAQy2Jdro3SfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
جدول‌گلزنان برتر جام‌جهانی در پایان مرحله یک شانزدهم این‌مسابقات؛ لئو مسی با اختلاف در صدر.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.4K · <a href="https://t.me/persiana_Soccer/24956" target="_blank">📅 19:29 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24955">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">‼️
خودزنی‌خداداد‌عزیزی روی برنامه زنده جام جهانی از دست جواد خیابانی ؛ میگه اگه زنوزی اینجا نمیبود همین‌الان برنامه رو ترک میکردم و به ارواح خاک پدرم دیگر به‌برنامه برنمیگشتم‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.9K · <a href="https://t.me/persiana_Soccer/24955" target="_blank">📅 19:29 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24954">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBetegram</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CAZdR_BNYgYVAkiosLQQohyljk2rcEKyDik0_k9BCTQ5F4NdTwmAK_HiSMqeNURBTTdVhOqqVjdYCo1iq87CINp9tNhYbnGJdEVQ3tbe-KJ2fm1zwe5_AdVsjusBHMdMkvzQo6O7VH24mIedOoxEBtm7rVMpIoGsaVWoZpm-mOkvRRdcZ7j_l1Bfy-M7p-KYho1dRgtAj4RktaiNdMMX2Jt0md-gjJTd1NBJ4KPzOX5SQ7rODNGUFHihLePjcu5SH3nwmxvxrqz_xjgQLTspzQs5u5w7VxfKeEeKwaDfjAjbS3fF_VSQBQureEX3r2ZFiNey9qdUIqM74Pl2O4ZUtg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇲🇦
مراکش
🆚
کانادا
🇨🇦
فکر می‌کنید کدام تیم برنده این دیدار خواهد شد؟ رأی خود را ثبت کنید و اگر پیش‌بینی شما با نتیجه نهایی مسابقه مطابقت داشته باشد، در تقسیم جایزه
۱۰۰۰ دلاری
بین برندگان واجد شرایط شرکت خواهید کرد.
💰
جایزه به صورت مساوی و مطابق قوانین و شرایط سایت، بین تمامی شرکت‌کنندگانی که پیش‌بینی صحیح ثبت کرده باشند، توزیع خواهد شد.
⏰
مهلت ثبت پیش‌بینی: تا قبل از شروع مسابقه
👇
انتخاب شما چیست؟
🇲🇦
مراکش
🇨🇦
کانادا
شركت در قرعه كشي:
Https://t.me/betegramd
📺
پخش زنده بدون سانسور در کانال تلگرام
🚀
برای تماشای مسابقه و ثبت پیش‌بینی، به کانال تلگرام ما بپیوندید
عضويت در كانال
Https://t.me/betegram_official</div>
<div class="tg-footer">👁️ 51.4K · <a href="https://t.me/persiana_Soccer/24954" target="_blank">📅 19:29 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24953">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eMEC72QWf-SsV4Dxo_SaOCCB3skhdfmxCfWP9YSc7uUSdhwKXdGDrFT_7WwxvtXJLGy-aniG-kNbOBWbfMP_MMfBfKA7uEFuGbPl2UWx9vcTMekmuQtY38yd8bCtootJ4S9qx52EkLMAjk6aBRIJAf5d3Umb_wdMjyigXbkNe1xVysf5ic1noa5if1D6Kzy01BhfKCoM6VlKbfZjOMv1tukNq1ftHVQZ_K3p_C6OFKdC6dgpm8dl5kobWo2Cxkv-t5SGE2DVpEcr7lDe6YE1Q0lm9RqRPcdqegWHv1QDtPBqrA0Dwmi7np0120DUGOFltKYBfwU6Uk01477qAZGadQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
طبق شنیده‌های پرشیانا؛ باشگاه الشمال با ارسال ایمیلی به باشگاه پرسپولیس خواستار جذب اوستون اورونوف ستاره 25 ساله ملی پوش سرخپوشان شد. این تیم قطری اعلام کرده حاضر است تا 3.5 میلیون دلار برای‌جذب اورونوف به‌پرسپولیس پرداخت کند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.4K · <a href="https://t.me/persiana_Soccer/24953" target="_blank">📅 18:50 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24952">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Sq7axjBShgCNNnQ9giQ4o6osW1rdLR4kBTLuyYRrjS5br3nuD9fWhQx81Q9AK_jZ_wD2lLjPDBexMiiLBoC51FF3ugx8J3EDRvxusPalx1wBh6e-cVYaIHh9HGcjL0Jl48nO7ykkWRLk1niQjFkNFOXKN5k3MLzizob9-WMWKdh-CmyY6vTwJP_iYL3n7qGUi92Cc2UjUJlA9quFhe0JgJTrpkocY2LnkapLrNv0O5ZVss7QxbTGcxIpNTjWcjuh7xQoRwsjCkO7ZTWLdd4jaqf-lWzv25KhGj0mfxG2Fr5DLpMuEbVOmvMz1UiXDXvJUdYE2AUUM-cVOnB-4Qt0CA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
وزینیا ۴۰ ساله در جام‌جهانی ۲۰۲۶: ‏۴ بازی، ‏۲۳ شوت مهارشده،۱۸سیو، ‏۷۸.۳٪ درصد سیو؛ مردی که ۲۵ سالگی وارد فوتبال شد و از رانندگی اتوبوس و برقکاری رسید بدرخشش مقابل‌آرژانتین و اسپانیا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53K · <a href="https://t.me/persiana_Soccer/24952" target="_blank">📅 18:30 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24951">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kKtHnsrpJwroF5yW_XGLWJIHfuMB4d2ptAUjtrI288KcBeCBt5dv8dRTf7CYfadVwzX3tW4jSxvz0MO4WI1AFCg9_oDcFJc7PZpZQ3i-cf3nYQpSXSXd9rytF-5oJfC8ypqbU1jXA78gvgvw43wzE9LJ4TlnhOL1jPMRyt3oAQTOH_Pu7uqT89zfyflEYxrhwfyGp8K43Ta1uKoEjBUU1dqz6tKEgbeBy70Yq_9fnYOgVwbLvBp8vQxdTyajkdxioSlIgslc5R7fFy7OU6SnXKRrtLQ5l9Y09epxNhU8_6OARXAdufgs4vkA1maqNvma56cGllS7CrPvjL_7maPp_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
طبق شنیده‌های پرشیانا
؛ باشگاه الشمال با ارسال ایمیلی به باشگاه پرسپولیس خواستار جذب اوستون اورونوف ستاره 25 ساله ملی پوش سرخپوشان شد. این تیم قطری اعلام کرده حاضر است تا 3.5 میلیون دلار برای‌جذب اورونوف به‌پرسپولیس پرداخت کند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.4K · <a href="https://t.me/persiana_Soccer/24951" target="_blank">📅 17:59 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24950">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BU7_6jhV3vjq-Di-KvWhLzchvSg7vWAHdhJeCxYi_1aBzwlR2YqwviCi9_ACekjBNT9KsVf7R5aW2YTD4wyXEQqp2bMiASERs-hFwg3wNMjtOmPvQ-dBQBPJJI64x1hyKOKxcbtRCQjl8Kxh72phgqIVZrhIg7y6SDn0I6672NHBJgC2ALiXRScXgkKqorUmPYc9KhrhL7cZ8SXaHXmf04do14wjUFU_0fb6PsRRJKv2xdPXinP4vIr7q9JIERQQuTQ7gjwvrKwWzR60y86oKumshQy3rVSqApka-9C-TyXtOprc8HIqCQW6O5bnUlaIOv8sGrxy44Of8hPDVfJJCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
باشگاه‌پرسپولیس‌دوگزینه‌داخلی برای سکان هدایت سرخ‌ ها در فصل جدید مدنظر داره که سعی میکنیم اطلاعات دقیق و کامل درباره این دو گزینه بدست بیاریم و امشب یا فردا شب بهش بپردازیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54K · <a href="https://t.me/persiana_Soccer/24950" target="_blank">📅 17:21 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24949">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FWoRDsnN5OkrDp6FLTyNCRr29EBjrboZBhBzbqDZjRjECLmAats2fbNrtRt3RQiYmg-c6kKUjWB9y-sgkeLhpPZSJErf29pdcW8Vq1JI8riepx2trfdYqRRe9t91_B-hVJIJN6SKC7nH8J3H1T7pcEI41C8Ju9x7sZlFjpRWbA0nrAP_02bLRLLRnD310Ei4DT4kleIbkkW5Ekuk6gI87DaEw1RODLTXSa-6HAgc-b_uzkyAp_FAC1UTrJzUVfk7LCzEAmJYs_OYa9ePTZmrrG0NowTp5S1M50IMW7bEtBffesFCRCN2HcazNEy4KNZAhva-GBLMAQBZUCy9LLR5zQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
وزینیا ۴۰ ساله در جام‌جهانی ۲۰۲۶: ‏۴ بازی، ‏۲۳ شوت مهارشده،۱۸سیو، ‏۷۸.۳٪ درصد سیو؛ مردی که ۲۵ سالگی وارد فوتبال شد و از رانندگی اتوبوس و برقکاری رسید بدرخشش مقابل‌آرژانتین و اسپانیا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.2K · <a href="https://t.me/persiana_Soccer/24949" target="_blank">📅 17:04 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24948">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mQPZjMePxk0RViYNsbNN-_7Dle0MBsNvjB8AAZ_sxuGSSWLIPOKFuXe-8a_rYhnatnSz2ZqoNmCsdQSJN2nU7jVBpkB6bbvThaqjgoKRF1wGfcnmTBYOPX6L7R2LBFQ35bYn6sj49nbMO7qmGe5hUP722JR8tVGVVDT2-b-6bEfUg6DE_3qbX9yIBJ266fFUCQ1qMXvAlwfDrGWY7sCdDUJ1zl4tDv2QrpUJefRQ1CBH62IHOMOa--KJScK8VO6LaRFV_YNsyD56TlEvmCvIBhHzU3MZbOsBQFhhVCTdiSoWfy9q6pIcuKIq7gJ_aOcaM2jFf2iIbL0sETB9uLIr6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
15 تا سیو مقابل ستارگان اسپانیا و آرژانتین در جام جهانی سرنوشت یک بازیکن 40 ساله که تا قبل از جام جهانی تنها 50 هزار فالور داشت رو تغییر داد و به رکورد خارق العاده 20 میلیون فالور رسوند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.6K · <a href="https://t.me/persiana_Soccer/24948" target="_blank">📅 16:43 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24946">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qKP0AXTD3chVN__fRpGiInsuELPXO7VGS_0iqDsFvxhSR8WWrYJ8YchcbWsrF9A59_Um1LPFTWWSxm-nXCD1sb5odxkCX0XJV0T_7f5aVkK_l9LlTQYUWmkSqv1CeTNajqRZ_NKqpkFBgqtvGlemjE-7vZzFOqZj4M8uFNnE4TV3UeWHU2QP2kuX8ks-iph2kxjaYDckqBPN5x6BbmVnP_52nPMr6gmzzjzN1xxm7Vk3Qkp8Y2wjjCnkdYzjWL9AOw0i9LhhFi1awpfN9o_q0Pu2og4iuwUHXwHZDapzDjLgCXtNr2zqxwvxfhMI6Z4pmSjkReHtNgx2plyVtPidWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IfQmYbTrSpJviG4mc8v6D3kIeS15qqCjjDBiesICAcA7qYJhD9ymm4p8fUfqoAjatV8XZ2o8yG3huYJqdcnUaB_4bGXkj2m2ysvYb88CBLeopIA0tWOmySjdgZQPOaAUQ7HHew-cWnRcO7xzG7rHix802X3rn0cesq6k_V2tcW5awg9Bqx_YfMre-Jv6Ftp62Uo503Sp4034TDGXFBvTRVa_1S01SA79I_W2Spy94pJRKqoEwb36mmXNZHSWD6EGK6tQxT2SaWncwrhUA6MI3W5Yuz5XYLUTuUqf21g2X1dZEmJ-dvmCXw_M1GftdKW-2Gt8gC8evmjQxfCZa366EQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🏆
هوادار تیم ملی الجزایر که علاقه زیادی به لیونل مسی و آرژانتین‌داره‌ودوس‌داره این تیم قهرمان شه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.4K · <a href="https://t.me/persiana_Soccer/24946" target="_blank">📅 16:17 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24945">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Oq8LzpXc99frnW8b5qyC_lggRWAFVWs6v2_dRmPGOY_4SbzHdHCTmVog6ew3XlhymQgNHNhNPoWMEgmrbReRkZS8PLhIhA_TybYB7uQJw-8U4L3PWBy_j6yVfiRO1sI7MRWFbFZ5E-NHlFELkOsuPR0qblibpSZCzJnQpZwylvKWw8WO0o_7gG2mtwASFTEOOPb7ZMOkhvyxDgpO7qmrE3Q3kAehNWkugcHxTdfafIiR3ETuH8w-C97R581SdpuicqT7eS7EXnC5X93yZx5GYwuOBQFdD3HmH9U0Qm_E1eQzdPfJ3V4r3Xt2rn7Cj0KZALFgxXBAHrWwO9gYmWZZfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
🤩
مقایسه تعداد گل‌های لیونل مسی با پیراهن تیم‌ملی آرژانتین در دو جام جهانی 2022 و 2026
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.2K · <a href="https://t.me/persiana_Soccer/24945" target="_blank">📅 16:00 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24944">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L2QD-WcatATFmYPZtnf6J9VA3wiuw82y7l1E09EMEPlvX3GrybF6EaRyJ1wgBsIxdrwH1OE5qETBcEIqB38Jo1NG1vU3miyvJp9zO6dwcirR9SbEZw80HHjBTs2dxqgDvFqyNCOpo4z1-Ui0QhsXZDB7DZa-pqreyxYOg4kIRv24qOaUFG6gGuUCvmWM_JHElQ9Sbw3XozILGI6VwjSRB4Wgx5wtZ8jaVA6Syr9Wc8q4gah2WRz4kmv9kqwc2klF0b-yozcZ-m5hcAVipFucQSPY0NwQXqKj2Kibh2CZ_ZjaQlY7N0iSs-ytgSqSH-sz_XDxlfZbz0dHeiDZfO1lJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
#تکمیلی؛ طبق صحبت‌های امروز وکیل ایتالیایی استقلال؛ تا روز 25 تیرماه پنجره‌باز خواهد شد. کانال پرشیانا موظفه اخباری‌که از باشگاه ها دریافت میکنه روپوشش‌بده. بسته یا باز شدن پنجره دست ما نیست بخدا قسم که از ما گلگی میکنید‌ خبر موثقی که به ما میرسه در کانال…</div>
<div class="tg-footer">👁️ 51.6K · <a href="https://t.me/persiana_Soccer/24944" target="_blank">📅 15:53 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24942">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Jsn-qFwj7wvxvIu9kdqBGhcDG7601MuZGI0V82Gk0rLBKtHOmNgsjPGrawHBhknSwsFPTzhLaXusAr8GVoYu3SmED6IOS0_mE9fbid_-nAKM5NqINxmoj7uL1W3DgTgDIoPxfjzQCwIe7hlJ17Xw3k4EN0Tyrcx7Bh8t4HBIm8D-Ljx5tLrCU0-7I7Q9iCII3VidbUSk4HrCVP2Ky1E2ggF5w7Ba7yfjnb07Yb3IuLrQcPtbQElTqsUv9H1h2r227EpCHU7J0hqViNr2TfbUABj_APurG-0H8ewAp8-NzyauprqPL_M6Zae77UemPDZbpzDGWh48tJXIi1d1UyuyWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🟡
#نقل‌وانتقالات
|امیرحسین جلالی‌وند وینگر جوان فصل گذشته باشگاه استقلال خوزستان با عقد قراردادی به‌مدت ۳ فصل به باشگاه سپاهان پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.4K · <a href="https://t.me/persiana_Soccer/24942" target="_blank">📅 15:39 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24941">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GXB81_mqZ9GUwVvtPubH8--TH8WpGNAmt94PycVIP2hw07iPjxg6bWxSMJECBZMxWC9aLZWXq1ZuimGn_uh2EWs5UXM8Tsxh0yQFmQjUdIsHzQ5aiLktnWcrYEeEAcdjJWWlYufK74UkEKiF5a0Sg8KFd7xFsheFHZ9SHvUA8axv7tw9J-B-NtBN0soFBTO10rgyM1tWTODOcfKZ-dxnSu3fVyQxYc736pWNPvU507_LlNzTfHMUZNbsGo2Rk6oXWHGCWeY2wrOh1MBl6tK5SfeJksL8DD6Bg2hl1DP2DqgecU1Em5fKMbTLyNW0-YmcakVlGARGnoUSjuALOVBLPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
مقایسه تیم های حاضر در ⅛ جام جهانی 2026 با تیم های حاضر در ⅛ نهایی جام جهانی 2022
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.9K · <a href="https://t.me/persiana_Soccer/24941" target="_blank">📅 15:17 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24940">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u6F_DTTy_d9QH447GLgEd_sIlgoR4NGPPVb01HWJ6GJ5AoGJ8rMkZsuA_tuH2sHYPeI92ZTVYprQeImBk6wupg5kIva6IBjtJQJI8voxGSVJ9f5am6oSOexbaXLzSLH5mjf4vy27XQGDPvgzHH-AyXtdwZBVctGUy57dAZ8afNC76GJhQ6EIKURfcRAEIZxmyqY-AnvPHbegq17LNt06WQPWgdryODCgUCGCNsdM6uDN999t8JyjT6Vao6PV58P4E1-tewyUT67OHi0IZbzju39kpiCYhX_O8242nirA2uIM63Ev2vE0_KTbGyf5zMYTb9qTBb9K-IFLymGYkMsQIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
همه از عملکرد نه چندان درخشان بازیکنان تیم بارسلونا تو تیم‌ملی‌درجام‌جهانی2026 حرف میزنن ولی کسی از این حرف نمیزنه که این نبوغ فلیک رو نشون میده که با این بازیکنان تو دو سال اخیر ۵ تا جام‌برده و تو سال اولشم تا نیمه نهایی چمپ رفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.7K · <a href="https://t.me/persiana_Soccer/24940" target="_blank">📅 15:01 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24939">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Wlpws7ktWRH7EbiWkuCs0IgRzuOhW6zJ3TVboLjVCuwFhIpKDt14mn9M7FBoKEkVdT0M6G0fbbaU9nS3FbBD_cqNZc8tB4Duv-BNR8gy6e245mSggHQegOZr7s_gbyDsCJyBCFqNoqJlVGU_CfXtY_hLuMQi_HIJrSfdCE4B0-2-8E1N-XQU4Cb_KoMjeaY8_NnJH0Tk6G7WAnF80e244qFX9DxcjWarhBe3BkOzi3FDkPWmp0TFVr2FyVLN34WpSB2UbyTazY-MOw0RhCgNy-RSwb3CdEL8lVuuR0t4h6OQOVAS83n2gt-RUfzh5Tq6XKoOohegyMRvVLzUhYxDcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
در بازی کیپ‌ورد
🆚
آرژانتین؛ لوپز با یک شلیک باورنکردنی دروازه‌ی‌آرژانتین رو در دقیقه‌ی 103 باز کرد و بااین‌گل‌دوباره نتیجه‌ی بازی به تساوی کشیده شد، ولی آرژانتین‌ها در دقیقه‌ 111 گل پیروزی بازی رو به ثمر رسوندن و به مرحله‌ی ⅛ صعود کردند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.1K · <a href="https://t.me/persiana_Soccer/24939" target="_blank">📅 14:39 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24937">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/i0EK-9qiKFyLVW8LKpJ7nKwSjVsYzzYLarVSzkBFV6brqdyg4UDKI_nN0CR7c_CKOhBD1CvOlOWjP793ISPNnWDVY8dZ_PP7wVSq8m8Cw4HwaPM8m6tYUAVfgE-ULO9pddFut29T-U-A3COcpbWoiLBjiUImK2EOjvIl3U8gruZ2XgqBUsD-exnmJy-DAjF7u-ThvggcYcVuoe1c-waa0VlLKeNmFd8SJJ3PaBax3OYw59UvuIB5_UH9wrG40A7y-jdRDVHnroa1MxYVZTpGn9TtlkWsNKb0ELqI-WLsjEf_sBsNcNRa6towhwfgAPAtoK8qKmIf1jZXUDD1nHJihQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/ROvcDxlCuRjRmqeMlfEt-443rUWsISg5yEcwwpT0zxYqb18qh7p44NxNQZrPwJnSXXf4h540AOwEY7-wuBAvWQDUZRfY6a3j64lvr1ZApYTvgdNxt0d_RpixpDw5Kfr7j_tX988_lbzUkrb5-IPG81LKM3TVcVcxXK0J_nbMtwxg7zFNuELF8wTYwMy9g4mrOyGZFdMiNmFkrjbzgW7imHTFaHWgneamfDg2rDXq4No99ZIQWJTanushpOvHz7xJuDEpKlQZPIvTrkbyvn0cz9YpW3QXLxKk3YEWex4rspksu-w-VR6-sO1HOXtXfUNdy3MkEE2EQz0cxXHHVlyYoA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🏆
احتمال صعود هر تیم به مرحله یک چهارم طبق میزان شرطبندی ها تو سایت پلی‌مارکت:
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.5K · <a href="https://t.me/persiana_Soccer/24937" target="_blank">📅 13:57 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24936">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2bbb73e166.mp4?token=K9coSnmRV0WVGrFIlFQLj08174syZKoh8qz0SFINrCE8BAoz48euVtecp4SDjexEF3yY1TRUrlEh7KbMg6IErXmh-bKSwWmsG3NbWE8qnAxmU8EdTrKptbApU2K0QG_JBuA-f6pdIXYKPMYK0IF-yJ6Pg0Ykzcy2BDqvjn297O1Cw2Zz5xURgtVcsNuiXDcrxiY5os-IboQwfRIUqPf3dUQrowpXiq3tfJlOHvL3fluNLzJ0MULb0oXVqHY61g_X_Nmqg_En2W8D0CcphpLFYp5h2NgkCzRI4XRLdGWeLN1b3N0lZGFcW1rb272Z8w6ACrV20M706yFJuXVGpvNpMQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2bbb73e166.mp4?token=K9coSnmRV0WVGrFIlFQLj08174syZKoh8qz0SFINrCE8BAoz48euVtecp4SDjexEF3yY1TRUrlEh7KbMg6IErXmh-bKSwWmsG3NbWE8qnAxmU8EdTrKptbApU2K0QG_JBuA-f6pdIXYKPMYK0IF-yJ6Pg0Ykzcy2BDqvjn297O1Cw2Zz5xURgtVcsNuiXDcrxiY5os-IboQwfRIUqPf3dUQrowpXiq3tfJlOHvL3fluNLzJ0MULb0oXVqHY61g_X_Nmqg_En2W8D0CcphpLFYp5h2NgkCzRI4XRLdGWeLN1b3N0lZGFcW1rb272Z8w6ACrV20M706yFJuXVGpvNpMQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇵🇹
🇵🇹
کریس‌رونالدو به‌تازگی و در اقدامی زیبا برای یه خانوم‌بنده‌خدایی‌خیلی‌یهویی یه رستوران خریده! حالا داستان چیه؟ عمو وقتی ۱۰ سالش بوده و وقتی از گشنگی ضعف میکرده این خانوم بهش رایگان غذا میداده واسه‌همین این‌حرکت‌خفنو براش اجرا کرده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.7K · <a href="https://t.me/persiana_Soccer/24936" target="_blank">📅 13:48 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24935">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RTcFAxb97dJmk7CJckryHF43WOd_3hilmduEL3F6lA5NB0J8h8f2DDzJef_T9X7RL4-UYABP5cc2jGs95u4Ewgcq8Mf3Ze2u4AnSE8mX7qpf1yl8MH5AYvN3dYHvukpfN0X11J4HvYGixRCXYomEBAKDuDcplt2GkQJd_ISV50IiG1E9W1I3Uc5pUR8No63Rml_A8opagaHJZCE2CcZn8QmK5l-aib5i7jwgzbchl8F9n1w1l7O2jkilI454jToTpGhpMDnEhJYfGFRBOvIH4b8gYPfxPir9nQGlAEJ0UgHcRlxkCXQ1vwN5EkpsIUNNtW1QgRbRPovLRKdFJvHSEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
دیگه با استوری که‌شخص دراگان اسکوچیچ گذاشت همه‌چی‌برای رفقا مشخص شد که اسکوچیچ دریکقدمی رونمایی با پیراهن پرسپولیس بود و هیچ درخواست جدیدی نداشت اما اختلافات بین مدیران بانک شه  باعث برهم خوردن این انتقال شد.
‼️
کانال مردمی پرشیانا هیچوقت خبر رو از روی…</div>
<div class="tg-footer">👁️ 52.4K · <a href="https://t.me/persiana_Soccer/24935" target="_blank">📅 13:31 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24934">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kyWCGBTKe5obp8MSOJVn4iZeHpmehhGYK0Ma3yK8SLzn3mwUCUiKurrUH3uR5m6s0UWa7ekzUx0q1O7jTorrGLzPVtvIkAkWr7b_kXLT3si9IeNTuFURbzAidf7VvYA2c2MuzabvgtTFaDXY3TNqGtlXHrL75A3L81Vq-ZD6gL-NYOa_S27EK3HWUhYP0GHoELjv9qeg0kqqQRNFLEbx6m0MU8G4YEg6PZ8bbQlVb4PCwD9f4RNyF6Xz6nmQCRbGqjL71sHT6Lwst1OM7ajSkUF23BLriqMg6cQh-pzZxcAc3m3vxKYQ4jmnQfw_aTpRmtjNyOYBK6anv8YuMKpxQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کی‌از مدیران بانک شهر از این اقدام پیمان حدادی دلخورشده</div>
<div class="tg-footer">👁️ 52.5K · <a href="https://t.me/persiana_Soccer/24934" target="_blank">📅 13:23 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24933">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s3oKyN_Ql_NZCcyuuXl8HjeKgcG9IxcWFunB9yTg_lOBK5jBWHTd1_6ngv0Lff_todsxxbw_oQg5xjD0SM_iRuCYY9GQ8CeeNkuPolIdqnSrWc3_CNX4SNwLLADrh5XSMheNm63qNbJRE16IklDOoefFFlwb_nk58eV0KuUAVa_DmcV3uytzJeBemPZTij2afn-h9r3uOCRfoUPwmNLnZMaMsiefZCIjW-F4QIlh1w4ur0CsMgGAfY43i7oyKVweVA3ONFB2XZpZ2F9bcJc88PKH71C4m9Se4yxducZwxz54E3CnctNGkq-xnmawrmfrdGzKzIjyX5KNSfhnWRz4ug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
دراگان اسکوچیچ: مدیریت‌ تیم پرسپولیس به شان‌وشخصیت بنده توهین‌کرد. تو عمرم ندیده بودم مدیران یک باشگاهی این‌چنینی با گزینه سرمربیگری خود برخورد‌کنند. اگر شرایط مهیا شود روزی دوباره بعنوان سرمربی یک باشگاه بزرگ به ایران برمیگردم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52K · <a href="https://t.me/persiana_Soccer/24933" target="_blank">📅 13:04 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24932">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CXKsstK5M1bDs4quT84Tj8Ul9voqKAEvKA2sXCRMxKXq9l8YUtHdbgQ-4YFeHbAGhAtH1sWAMp1gLh_rrMsME34Alkml58A77dwUw0XmV2o2graLqROlNcHf8yyNvzZp-O87Ktw956fdB5qubFHjfqGGbz0AacVbkeS7CEF8N7QXeEniUEz_Wpn9jaRXHOFYATv3u-iW7imdJH4Wo6KGKFZ7nJuFreErLSr5ccsYfsRvC0iSAKirTFbqoa2sEQ6UXr6G8vTZL79rQQ8QS4va4UhI24nltOMH1MEfpdT5nCAUc7QkLBf_YrAKx7sRZ87-G3tLHQinFYKakeo3-rBp_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
کادرفنی‌ مصر برای‌ضربات‌پنالتی پنالتیای کیلیان امباپه در رئال مادرید رو به بازیکناش نشون میده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.3K · <a href="https://t.me/persiana_Soccer/24932" target="_blank">📅 12:59 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24931">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F-DUFcZeI1-04dLb_WT5Dizp-yg-naJKhwUbo1yhnqLU4PaDBOrlHOwF6MwFjcixBVMMuFH3Ms4HvpkRJR89yTWMA3xYkvFbz-bl3IBMd5iV7IrNvHhfoB4F3xX1LKxKj_7Uc00PCF5zpwCpOXYGkFhzzKj5Q_EPMke5Z_xBCXRb4QprvPIKj-a9pW_b3ynaQC-i4Y3jVkySiVenUnMidm1x5AR4XJOoWRyHif41pTbnqRnYPEfuIgDF3ydHUMtZNv034ugmtS28qpvMS9V0ef3SDH1W9DN_3XjhEjgd8tW99jf53Ist7Zt6vQa5r2t5dLhD4e9W-ZkwlQmFDddrnQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
روبن‌نوس:
هنوز با ژوتا صحبت‌میکنم، چیزی که افراد کمی از آن‌باخبرند. ما یک گروه واتس‌اپ داریم که من همسرم دبورا و همسر دیگو روته کاردوسو در آن هستیم و همچنان در آنجابااو گفتگو می‌کنیم. هر زمان که اتفاق خاصی رخ میدهد من چت‌های آرشیو شده‌مان را باز می‌کنم و برایش پیام می‌فرستم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.3K · <a href="https://t.me/persiana_Soccer/24931" target="_blank">📅 12:34 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24929">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8cfc13f85d.mp4?token=O2Xr73zRM9fS5hXd0eob1UrbVjC8USPShVbpQ8uMGbmvQQb0qg2gbm9_YP0v4scM_qSI-_FOOgzkK69UMK056sn2yexvoI5MrZX7x9hPOt82XZWvD0C0tjIQ7U3usR6zvWwk-MQsfam_NrSTgeugbwq21T-YdvQgesiO4i8DEnSPmZVmcbuRQ6HXI0ay8HOh0Oq2VMtF36hi8RN7Jla4qNQtYMgkwmXkoY1zcR4eCx6D8daiGjysbsmKloBE0dA_8uV0KtUN0gOaTr4LEJ12nMMLTr8wzroCdZK1RwWf2HzmAgqetbRz4tk-m_bNBMzdQGSptfRtfzYMroFFKSl_-w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8cfc13f85d.mp4?token=O2Xr73zRM9fS5hXd0eob1UrbVjC8USPShVbpQ8uMGbmvQQb0qg2gbm9_YP0v4scM_qSI-_FOOgzkK69UMK056sn2yexvoI5MrZX7x9hPOt82XZWvD0C0tjIQ7U3usR6zvWwk-MQsfam_NrSTgeugbwq21T-YdvQgesiO4i8DEnSPmZVmcbuRQ6HXI0ay8HOh0Oq2VMtF36hi8RN7Jla4qNQtYMgkwmXkoY1zcR4eCx6D8daiGjysbsmKloBE0dA_8uV0KtUN0gOaTr4LEJ12nMMLTr8wzroCdZK1RwWf2HzmAgqetbRz4tk-m_bNBMzdQGSptfRtfzYMroFFKSl_-w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
🇪🇬
در اقدامی جالب توجه؛ مربی مصر قبل از ضربات پنالتی، خلاصه بازی‌های رئال مادرید رو برای تیمش پخش ‌کرد. مصری‌ها این دیدار رو بردند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.3K · <a href="https://t.me/persiana_Soccer/24929" target="_blank">📅 12:21 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24928">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7c33bd6932.mp4?token=l8yWhIwDSuBUL8zbqJBkO_AlgwiZVzr1ksrhPYXdT6eYb9Wo0r5VVGFDotjY7QxUiKafe5gbrcmF1dP_-dCxIqaPHMSj5wQ4M2DWKQd4NVYpdmbMkwZuEdPwvDF2KYpf6GsxCTzAa5uMiFrj4YgIB0g9ydmTCtgkm-a25lDRrJvzrZFIaB8uhEoTQKS8WZq_tvOiNGDPGr-ZKUePV0-cKCkAwqbruCheT7OupbTRlTYB_1QWi2EyBIHDtVmoJ5WcKgRetvKyO7YnmRJawCbZPZe9ThLx3WUuto9WH_ncO-1LlH1YPSR6W3ETl6JKhBWBaZ8ZT9kDCYkAuGn0djw2EA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7c33bd6932.mp4?token=l8yWhIwDSuBUL8zbqJBkO_AlgwiZVzr1ksrhPYXdT6eYb9Wo0r5VVGFDotjY7QxUiKafe5gbrcmF1dP_-dCxIqaPHMSj5wQ4M2DWKQd4NVYpdmbMkwZuEdPwvDF2KYpf6GsxCTzAa5uMiFrj4YgIB0g9ydmTCtgkm-a25lDRrJvzrZFIaB8uhEoTQKS8WZq_tvOiNGDPGr-ZKUePV0-cKCkAwqbruCheT7OupbTRlTYB_1QWi2EyBIHDtVmoJ5WcKgRetvKyO7YnmRJawCbZPZe9ThLx3WUuto9WH_ncO-1LlH1YPSR6W3ETl6JKhBWBaZ8ZT9kDCYkAuGn0djw2EA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
در بازی کیپ‌ورد
🆚
آرژانتین؛
لوپز با یک شلیک باورنکردنی دروازه‌ی‌آرژانتین رو در دقیقه‌ی 103 باز کرد و بااین‌گل‌دوباره نتیجه‌ی بازی به تساوی کشیده شد، ولی آرژانتین‌ها در دقیقه‌ 111 گل پیروزی بازی رو به ثمر رسوندن و به مرحله‌ی ⅛ صعود کردند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.9K · <a href="https://t.me/persiana_Soccer/24928" target="_blank">📅 12:06 · 13 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
