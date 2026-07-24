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
<img src="https://cdn4.telesco.pe/file/oG5WN3DumIyYO2OzQsTg9uzPIveG2NN82nUPehypSDe7gISpQSNe3TuJ76BFTHNb7fKwnhcGlw1QJw48of9NQwERO1rGMMp98FuSPE_81nYlcC2FNfdVeS9CsILDNgyQ-vSw0wfvyWKbqcLWdM3CwxUlrwoRwlj11rj2vGVmSY3CC2As58x5rNo8w-M5MdtvKu4yfXPA69bllcSne9ds6eZ4qh0dj0lK2_F_DgKDiROuYvwmw1Igg3FAQDXKUj6a6-W_tH2DiKsHaLL0sitllotWzymx4U2Ga4hnON2gw12qYUoJPMkyLiwqvfI56RJqDccqVQlgOOiqLyELySSt-w.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 فرهمند عليپور Farahmand Alipour</h1>
<p>@farahmand_alipour • 👥 65.1K عضو</p>
<a href="https://t.me/farahmand_alipour" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-02 13:38:17</div>
<hr>

<div class="tg-post" id="msg-6340">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gqWa70UuXvYgm82q4WeB5gldwDWB5ClQHPmwXBrE9yLirAFDO8IRtphWIuQnI-DJlGJgio9FCHztlSkzIGlwzwDFYTgCTOZktFtBnPJhUSyN0bQXatKmqFJIZ7cHOhW7MJAQBkR86PBrhtq2H2d0HtfqehXRFmrudeDVfLoX0x0Lh_C5m5ACEMTa4Pligf8NTyC6iwKGWkRiBCOMNI1J6wDvvZ7EedzqBR4dpQpZr5ks6Gja87kAQYgyroQJ2NWD2HEcsehKynWin5It9wU7gW9jJRipjlAhzPR1nx7H0gSFvbXFB-FkxpIFXStH49YPNAKP-AbUWCovJ1ScAqaseA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صفحه دوم روزنامه کوریره دلا سرا - ایتالیا
حمله دیروز گروه تروریستی حوثی
به دو کشتی تجاری عربستانی،
حدود ۱۰۰ میلیون دلار خسارت وارد کرد.
ترامپ : هزینه این خسارات‌ها رو از پول‌های
مسدود شده ایران بر میداریم!</div>
<div class="tg-footer">👁️ 9.02K · <a href="https://t.me/farahmand_alipour/6340" target="_blank">📅 11:25 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6339">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c07c232479.mp4?token=KHqS3Swaw2IuvSvry2Fye_286TNAYmmZvcJFna1Eyow3spKgptg7ZIzjibbDCFap78aMo3b4rAtW9Oan-mtpCfHWYGnH44UODTWa7NAPS_qjbdmDtbkc6ixEhiczSU1hNZNj4fjlQbeC-GChL8J5W-hXv9Uyxbva-GABe2p6IoyGssNp-jJPStzR-UlY4LWesawHk7nNF3BW6u74urJ9GLQ2ng3sZXWg5GGaoDogce5ZtTU7q4ttDLRgxVFkcZFmxybYkOEIVLEvrvOkfecGQDcOGXdQu9lriiqDZBwepweHddC7SnDa5ZtG6qrXEUwY2zRGHWh9ECh9dbQlZ5Cd2WX96UuJNq7bizjZ2nbs5rJLS9VGs0NMOsxVJuLZteza5Mwn9iuz6tWPipy3bPoNUof5DFUOyVRXfJybKLwFzTLNwiAkaODAKJMxplalnJtpC5uYf5VCnkY_9i-oGk7hpClTQSOsbE3-W2ZqvTprpOToPJbAYmCdr__6MpSs19nIsoCurKvBlAkCnarGkWY8eyiItXKiz5sP-VxL0vjvJFUnZ7u2Z0zWrxS6J5FGysehPuPVGNDHvHtna15O6qUVSUh1LRCi0cnhQ0vr8EsfPA0PSu4gjqwTZoq3AVuto3xXXJdJhJY14EWMMqkDII0dY6i3YYZxrfZR7AN4zmcSvHs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c07c232479.mp4?token=KHqS3Swaw2IuvSvry2Fye_286TNAYmmZvcJFna1Eyow3spKgptg7ZIzjibbDCFap78aMo3b4rAtW9Oan-mtpCfHWYGnH44UODTWa7NAPS_qjbdmDtbkc6ixEhiczSU1hNZNj4fjlQbeC-GChL8J5W-hXv9Uyxbva-GABe2p6IoyGssNp-jJPStzR-UlY4LWesawHk7nNF3BW6u74urJ9GLQ2ng3sZXWg5GGaoDogce5ZtTU7q4ttDLRgxVFkcZFmxybYkOEIVLEvrvOkfecGQDcOGXdQu9lriiqDZBwepweHddC7SnDa5ZtG6qrXEUwY2zRGHWh9ECh9dbQlZ5Cd2WX96UuJNq7bizjZ2nbs5rJLS9VGs0NMOsxVJuLZteza5Mwn9iuz6tWPipy3bPoNUof5DFUOyVRXfJybKLwFzTLNwiAkaODAKJMxplalnJtpC5uYf5VCnkY_9i-oGk7hpClTQSOsbE3-W2ZqvTprpOToPJbAYmCdr__6MpSs19nIsoCurKvBlAkCnarGkWY8eyiItXKiz5sP-VxL0vjvJFUnZ7u2Z0zWrxS6J5FGysehPuPVGNDHvHtna15O6qUVSUh1LRCi0cnhQ0vr8EsfPA0PSu4gjqwTZoq3AVuto3xXXJdJhJY14EWMMqkDII0dY6i3YYZxrfZR7AN4zmcSvHs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">روایت وزیر نفت دولت رئیسی از تماس موساد با او و انجام حملاتی در ایران
🔺
جواد اوجی وزیر نفت دولت رئیسی : ما ۱۰ خط لوله بزرگ و سراسری گاز تو کشور داریم، تو یکی از شبای بهمن سال ۱۴۰۲ ساعت ۱ شب موساد با من تماس گرفت گفتن امشب می‌خوایم آتیش بازی کنیم‌ باهم،از من پرسید ۳+۵ چند میشه؟ گفتم ۸، بلافاصله گفت همین الان خط هشتم سراسری گاز رو زدیم، ۵ دقیقه بعد دوستان مسولین بهم زنگ زدن گفتن خط ۸ گاز کشورو زدن،تا داشتم لباس میپوشیدم، موساد دوباره بهم زنگ زد و از من پرسید ۴+۵ چند میشه؟ گفتم ۹، گفت خط نهم سراسری گاز رو هم منفجر کردیم،چند دقیقه بعد مسولین مربوطه بهم زنگ زدن این خبرو هم تایید کردن،من تا رسیدم سه تا خط اصلی گاز مارو زدن.</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/farahmand_alipour/6339" target="_blank">📅 08:24 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6338">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d4193f544e.mp4?token=IlCvjUfAFBmLg1zWWPt2p7YF1VRmiFKFzrXtog9v7YUcyJG7l939vJSi88DNd3BL_vMZqOMtcTrjApJs5nHrzlzL_Uib85wUPh7iG47x7o7NbvTu6Ai-aMkrkhCnnbMHLrOdSk1ahWgZHQ5Vy1SoJUyJj0QYGgj6IHaGA2yFZxLod2fE6dpfXZKFt_ix0fQZ0CZuhifAk6ve0n9CZSaE5N7HplG4qsC_VQxzCJ-Ah67bxDp0qs4EIi8HROI3ZXUBJ4dag3p6hjLuszd1-TgZURRg5W5__z-TXJjy1_uWeMZsWtA0-2QZzKSUin07GZyTo7Zb9zZp51sCUcAVQwgIWg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d4193f544e.mp4?token=IlCvjUfAFBmLg1zWWPt2p7YF1VRmiFKFzrXtog9v7YUcyJG7l939vJSi88DNd3BL_vMZqOMtcTrjApJs5nHrzlzL_Uib85wUPh7iG47x7o7NbvTu6Ai-aMkrkhCnnbMHLrOdSk1ahWgZHQ5Vy1SoJUyJj0QYGgj6IHaGA2yFZxLod2fE6dpfXZKFt_ix0fQZ0CZuhifAk6ve0n9CZSaE5N7HplG4qsC_VQxzCJ-Ah67bxDp0qs4EIi8HROI3ZXUBJ4dag3p6hjLuszd1-TgZURRg5W5__z-TXJjy1_uWeMZsWtA0-2QZzKSUin07GZyTo7Zb9zZp51sCUcAVQwgIWg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دیشب - انفجارهای پی در پی در بندرعباس</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/farahmand_alipour/6338" target="_blank">📅 08:03 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6337">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZMTx5dkGl32RMhG-1Hg_CtPAzpfVN27SicsOysr20M_aNLCquCTAtN-gFSbLC-onlxVwNmJMrlK0xifEzyk2wsUcaZW0pUF5FTYD0dJeuty-EFwUlZw5PYG9eQ6oyuaCWjKTQ9tOF4xI8uVayMzIWJhXhpZVLc3Zgi0V1mtIuxuGNfkk3n2KFE5zQBIix0FYskm02ZBXZ4FHoogqjFTyyp8KW2riGk3IG3Q6J98oEE0zNPingE_KCVaCHOXuCMLV4YEta8rNetg-zCZ18LGrjZPGH-NrrFfxsBJlvjhpVY46okXIEx12oo17GXcpQYvzP67av4_q4eoNs3lJ5O83Gg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تهدید تازه ترامپ‌: از پولهای بلوکه شده ایران، خسارت کشتی‌های آسیب دیده توسط جمهوری اسلامی را پرداخت میکنیم.</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/farahmand_alipour/6337" target="_blank">📅 08:00 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6334">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0d84604bc5.mp4?token=tNU5uEPzoKYo-rrTKMF01kX7H1CATupCxPqAqeJjAWYQiko8IlcNMalrEX0yuOcyeNsf1RRMzUJu0ecZnTa4mmD_ZYwzONb-VAN-IirexBaCu1yzSQBSiPhScGYvyzGE_rjEmmnoMgewxQNiyDTecxkj_PL-3P26UNhbeqbcpAYhG2DHuc8CJS10lrbfEIpMIYnctv5DnE2VTXUSLKqxdqqyvsgSeilk8lLCW2FZ7MC_lkXJOljtGCwvvBYD8NEuo5M47uDsuTM9AQn1i6NSQjw_ep3r-UN53Lw1SKRRqA1YRFKgcaEGZ5mb7WyCfZRAqEp19v_C2IrHEhIU8WiXcYi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0d84604bc5.mp4?token=tNU5uEPzoKYo-rrTKMF01kX7H1CATupCxPqAqeJjAWYQiko8IlcNMalrEX0yuOcyeNsf1RRMzUJu0ecZnTa4mmD_ZYwzONb-VAN-IirexBaCu1yzSQBSiPhScGYvyzGE_rjEmmnoMgewxQNiyDTecxkj_PL-3P26UNhbeqbcpAYhG2DHuc8CJS10lrbfEIpMIYnctv5DnE2VTXUSLKqxdqqyvsgSeilk8lLCW2FZ7MC_lkXJOljtGCwvvBYD8NEuo5M47uDsuTM9AQn1i6NSQjw_ep3r-UN53Lw1SKRRqA1YRFKgcaEGZ5mb7WyCfZRAqEp19v_C2IrHEhIU8WiXcYi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نصب ماکت آبگرمکن در مرکز تهران</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/farahmand_alipour/6334" target="_blank">📅 22:52 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6333">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">🚨
ترامپ به کانال ۱۲ اسرائیل: در حال بررسی یک حمله گسترده به جمهوری اسلامی هستم؛ حمله‌ای بزرگ‌تر از هر اقدامی که تاکنون انجام شده است. به تصمیم‌گیری درباره آن نزدیک هستم.
او در خصوص احتمال مشارکت اسرائیل هم گفت اگر از آنها بخواهیم ظرف ۲ دقیقه آماده می‌شوند، اما برای آغاز عملیات جدید به هیچ کس نیازی نداریم!</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/farahmand_alipour/6333" target="_blank">📅 21:56 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6332">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">‏هشدار سپاه: هر پایگاهی در بریتانیا که برای انجام حملات علیه ایران مورد استفاده قرار گیرد، یک هدف مشروع خواهد بود.
‏واکنش سخنگوی دولت بریتانیا به هشدار : نیروهای مسلح ما آماده‌اند تا از بریتانیا در برابر هرگونه حمله محافظت کنند.
بریتانیا به‌صورت شبانه‌روزی و در هماهنگی نزدیک با متحدان خود در ناتو، آماده دفاع از خود است.</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/farahmand_alipour/6332" target="_blank">📅 21:24 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6331">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OGDYdVfLT2yjxfrmqpU3DMHcE56lmQ4Mld9YSZbGVAIVUtXMrU8ZVIFHU9d4hVRalJIzgI9QwyDmxKzNbc3uksUYLSZUC3ZFuQB7CNKWcpA-__ZT4CidkjrGi88IY2s-qodYOScUyejpnkGisClSI7MwwXW1tHeAi6hDyoHQM2azpN0uHPKMMlZRbYwePfI35esvvmvEFIpC_jKSy2rb8ezcHOaXSwgRHqzUlF7ZRX44do5uAQ-XGaOU81xnSQscg7rHtmw3qv_VicMLhhiS3Ye5N6lxDd72wv7RgxAUfvFtaJRbmKy1J4FAZxX8p3WAmJMZoCb-SiaBio44sTsFTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ضرغامی : فعلا حرفی از مذاکره نزنید!</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/farahmand_alipour/6331" target="_blank">📅 21:22 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6330">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r5E1UvQisOUYNvRIBdOWx-bY3uG05FRSG-1gr3f2qY3oNGAiiIv2GUsfaCeCUVPwrhKFukgNo_CqWHm42-opva1tFSKkfTeRpdqHECndLHEEMJt-oHbJJpBy4HryLEee007nSj-xlxGShSLG0qTGx2VmvD2AHuB1RmL-015pVBw66W_pGkLz-eEBBhqWrEMoGU9SOGrKhWRzl_AFtOvQjI5DuRRQOMMgKAzSSSPO4PWulAJR6DuKHFfwtvJZz-sioJ17H7-CeiTyznVfOEOn-eDON1cY1BbsZ2XtNzV5iu9yFSunEu6Itqj_4Z5UUIOnBzCruoQFdUnNuFCxtN-s1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دو حقیقت محض
۱- تروریست‌های حوثی به تحریک جمهوری اسلامی وارد این جنگ شدند و به کشتی‌های عربستانی حمله کردند،
پس مسئولش جمهوری اسلامی است.
۲- حوثی‌ها ارزشی برای جنگیدن ندارن!
اینه که ترامپ مستقیم میگه فاکتور هزینه
حملات حوثی‌ها رو شما باید بدید!
و این یعنی بازهم ایران باید هزینه سیاست‌های جمهوری اسلامی و نیروهای تحت حمایتش رو پرداخت کنه.</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/farahmand_alipour/6330" target="_blank">📅 18:37 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6329">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/InUHe-PMLaDx2K9scrvuaCEE5PMmtEv8j37YKAZSFPQeYLWt5YaapkpmI37vouvGii24xDzgum4OdblYGtxXTrlyaLSj43f92Gty6MJln0MGdUxbl5IuZHZ-55D4-C4ZWxwsOu5gjXAoi9bgOp2ekfoGhslblobMxPPOplyoD3PDUfcwUbiELl6XSFaXyWUylQF32ZfInLOY8kc8cBPOQetViZ1avsB6gkpL4WwI_WFBGYsINNYt8gkxhMLZdHSyixDvYj-fmHwes7mJ-0aKPfCDkcc5OxKC5-6PxfGhzj1CVxuSCV4r_dGWSBANrPwcUrmvwCMoEdLRm2fNoSBBgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قاآنی، فرمانده سپاه قدس، با ارسال پیام تبریکی به «خلیل الحلیه» نوشت: «آنان با انتخاب شخصیتی که نماد مقاومت و شهادت است، بار دیگر اثبات کردند که همچنان بر استمرار مسیر مقاومت اسلامی تأکید دارند. مقاومت اسلامی امروز قوی‌تر از همیشه، مسیر عزت‌مندانه خود را ادامه…</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/farahmand_alipour/6329" target="_blank">📅 18:07 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6328">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aymC11W0__uqFaytzSgWkPXJ3NGVjEm6fImTas3C8T3WZLKCW7MO5OodyXdx9ouBqIAakXzZsUnsNl4K1A7f9x0z3zecSTCA5HY8BUJfO6UAJhv1OOQZ7rcihNiV8oDynYxyMTA9ZBEfZvYYpXt8B_JfnI7lCwp3PnIJB_XS7Jcw8KZLCfwjKP5O4unj_gNfDIoDqFu4vuITDQBsWab3RsFhKZhABCupEIFRiErLfCmkjKD9c2vqN8tFrjXeGirj7k4YYtY7dxI9FeHgsvhd6pSNx9LbGJnSnpdT9hhQCHPxo_YERl0Yap4qBlwuiq0pzPGzxpwxYATiPz2r7ixXrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/farahmand_alipour/6328" target="_blank">📅 14:57 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6327">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jfKoV0gTyaCZcUulO6eoMt__181eK1aDzHb7BK9cGQS99Dg907jlT9LXBT2HG0ku32WOusIa_Pj6dOzPabVq0SfCCFquY8ER9KrYh324K6YBX5lYyOKj1HW1lWw_7FEn0AMO4JDzgK7cl5GEUfqMbOGfeVT950G2Psl81WBmNQKy46XVCzBREiCoZfDQ6MmCBPATf_YeGfNcCo6ZvsTK47L9NQG_udQkI37tJ58L1Dk1963XZFgpe1B43bixT7i3WLbQ3efeJBeJlNkR4GhgNJoudo35qIxr7QOSJTo3tdK_D9i6QF-1ZxU09Fig_NlegPDytC2Gz2ULTFlUicMwrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/farahmand_alipour/6327" target="_blank">📅 13:46 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6326">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/12a0e4dfce.mp4?token=IHrIS2j9oi-GDX6x7kQMPO2zOsrv_dA8E1Nta0ZMkxTIVFFQB-sO-CjlMFIfoiyXS67LUuRmbeNzkkJh2lmxs3X-zhzchkngVYq501P5lGN4WDYFbqCqQDCCbFfoYJuVWvv5iQmc5eE8NOFqADL6sIGUgfF57pfRWxXDZzhaO7lzKGbyCz2Uw_nFaCFeSDQ90nmJLG-AjfkcB2eOXhbvO9XFCT8724TxT4qPlBPNfeGMUSTZAf-86xi_4aZmeEjsnmMmrMKgwO_d0dSmd61hFSJgWitr3Wn8NZw1kWpLl05E4JikLgZKb6fYeFH0gOiNxguEu2nWp6n_VDD80F4LqA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/12a0e4dfce.mp4?token=IHrIS2j9oi-GDX6x7kQMPO2zOsrv_dA8E1Nta0ZMkxTIVFFQB-sO-CjlMFIfoiyXS67LUuRmbeNzkkJh2lmxs3X-zhzchkngVYq501P5lGN4WDYFbqCqQDCCbFfoYJuVWvv5iQmc5eE8NOFqADL6sIGUgfF57pfRWxXDZzhaO7lzKGbyCz2Uw_nFaCFeSDQ90nmJLG-AjfkcB2eOXhbvO9XFCT8724TxT4qPlBPNfeGMUSTZAf-86xi_4aZmeEjsnmMmrMKgwO_d0dSmd61hFSJgWitr3Wn8NZw1kWpLl05E4JikLgZKb6fYeFH0gOiNxguEu2nWp6n_VDD80F4LqA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جدال لفظی دو نماینده مجلس
بر سر تنگه هرمز
(پشت پرده دعوا : شهریاری اینجا داره میگه
که تنگه مال ما نبوده  که بگیم میخوایم بدیم بره،
و میگه تحت یکسری قوانین
بین‌المللی است و زمان جنگ می‌تونیم ببندیم برای فشار آوردن و….. ولی مال ما نبوده)</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/farahmand_alipour/6326" target="_blank">📅 13:36 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6325">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z5e6gqbtaiqMLDiAyunn8kGz9PU50p1SfNlg_8YwUXnAziW7g5Lp7WuEV5a9co26Z1tjMHKfOd-jvlLsX8k-g9ROoEIsGtRNc8Lf83BK5pGAMM5BjkAYVVc56kJcvr6IuD5E8uZuuhLcs32NzfDixg3y5JIWR4Wa_dsb817afol8ynVHpT446yvtiN5t3dmmIpcgmITUX8IlNT7DC3coSXOIowRxQ6s5-Z6deNba7QHPuacfbzo5xMwFImI4EegyokZOGZs4S7x5pZK9_0PgJ33_0M3hNeKd44zIQrwHj0SqAvil4VCQxf2oNAvbm3b-c2hApfwDttlBIIRhs4SVxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارتش: مراکز و یگان‌های آمریکا در پایگاه‌های الدوحه، علی السالم و عریفجان کویت را هدف قرار دادیم.</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/farahmand_alipour/6325" target="_blank">📅 08:58 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6324">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bTHIgkHMBtosxPvZiC3SVLcM4JjB-s1SDYb-XL-Ut7EOn7x75dLWeHsHWUiGWxgqIoJZMiuAbduDLB1Q2J985B2rW8Mdk-vNnCPkRGMBU8jZDKPeLPvKCqYs9qHetJNk9rJXT42fqdTTsZrhVyu_wadx2ZjeLwGxzXVxP5EVVOU2UbWvCnRwJTjNKaDhuGdRRrH7hjLv37_aZBIT7ipigvoYTU9BOoOJA1-K1Bd_fuFDItzT8RkC3kazTAZrQpsMtZrSA7YjU7huf9dSGPJvhn0373xlQtfz3NDETvkfeHGVkTTGxPC9bD_t1zg3m4vSNZkUZyNUxh1aG9gL88yrmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در یک تحول تازه در حملات‌ ۱۲ روز اخیر
و نشانه اینکه حملات وارد فاز تازه‌ای شده.
«بی‌ ۱» برای حملات بسیار سنگین و عمیق
استفاده میشه.</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/farahmand_alipour/6324" target="_blank">📅 08:48 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6323">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">ارتش: مراکز و یگان‌های آمریکا در پایگاه‌های الدوحه، علی السالم و عریفجان کویت را هدف قرار دادیم.</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/farahmand_alipour/6323" target="_blank">📅 08:41 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6322">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">جنایتی نبوده که جمهوری اسلامی
در حق مردم ایران انجام نداده باشه</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/farahmand_alipour/6322" target="_blank">📅 07:56 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6321">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/08ac20eb0b.mp4?token=gGGVbbEvzN4yZ6-GZFt9kQDNQXDIB7Bq1WirrN5rUwjox8-PDLuRVgE9-siQSuVwMkGpLt54lIV3P-P7DImjC0br4MVhSrToD6WtFjyXyykp0QE2i4RlLqD6nojt7moaek-mDZfUkdNcbdFv6CrUI4dLkbHK-7jELDRKGj32OjZTxNZYpKrdDqDfH12DiIEhpkilTcPaaic69BT94JOmACO3qtCCEbyXtImrDalzrpVGzJ9NKvbo7glQAYNgwS5uMQJf-F2chy_gYD28yW2kbkMW9pycso01gg-nFZY82-b1vHcYZZDhMr-DB4x9spVg0EpjhCELWxnlxMVIt65ZSk0Y-B4u_LhARpXNl1Jv28qTRO_E1PKWr1ZNYeVxpUAwScdTnXrJbOWWYsOXvWijl383sbfiYdGpNsbX6zw0U796jkY9uPDbuNKSG7Qf3olKBQRws0eXePUfmAbxs85nA-zM8SriVisScngKNGmXIoDzci7JWE3_tEyPe90Dj8OuLI5Oouf-fx8srJQQ08_bgJzogmiplfZ8jiheXs6Ep5AMzCsUNW3h8RZh5aX7KoK4SA6oKCf11EjI8cc9msUp7qH51XkOY9LIabi7lpifjjWUZf9-CTpglR-MrWeW5a9ZA0_eiNcrZICvSSTrDb2F1hhUqU9rUDt3Ps_-nMBeYUQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/08ac20eb0b.mp4?token=gGGVbbEvzN4yZ6-GZFt9kQDNQXDIB7Bq1WirrN5rUwjox8-PDLuRVgE9-siQSuVwMkGpLt54lIV3P-P7DImjC0br4MVhSrToD6WtFjyXyykp0QE2i4RlLqD6nojt7moaek-mDZfUkdNcbdFv6CrUI4dLkbHK-7jELDRKGj32OjZTxNZYpKrdDqDfH12DiIEhpkilTcPaaic69BT94JOmACO3qtCCEbyXtImrDalzrpVGzJ9NKvbo7glQAYNgwS5uMQJf-F2chy_gYD28yW2kbkMW9pycso01gg-nFZY82-b1vHcYZZDhMr-DB4x9spVg0EpjhCELWxnlxMVIt65ZSk0Y-B4u_LhARpXNl1Jv28qTRO_E1PKWr1ZNYeVxpUAwScdTnXrJbOWWYsOXvWijl383sbfiYdGpNsbX6zw0U796jkY9uPDbuNKSG7Qf3olKBQRws0eXePUfmAbxs85nA-zM8SriVisScngKNGmXIoDzci7JWE3_tEyPe90Dj8OuLI5Oouf-fx8srJQQ08_bgJzogmiplfZ8jiheXs6Ep5AMzCsUNW3h8RZh5aX7KoK4SA6oKCf11EjI8cc9msUp7qH51XkOY9LIabi7lpifjjWUZf9-CTpglR-MrWeW5a9ZA0_eiNcrZICvSSTrDb2F1hhUqU9rUDt3Ps_-nMBeYUQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">- رئیس جمهور سلام میرسونه و تشکر میکنه
- باشه</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/farahmand_alipour/6321" target="_blank">📅 07:00 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6320">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">🚨
در جریان حمله آمریکا به مرز شلمچه ۲ نفر کشته و ۱۱ تن زخمی شدند.</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/farahmand_alipour/6320" target="_blank">📅 06:57 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6319">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">مارکو روبیو وزیر خارجه آمریکا : جمهوری  اسلامی تفاهم نامه را نقض کرده و لذا دیگر  معتبر نیست.</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/farahmand_alipour/6319" target="_blank">📅 06:56 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6318">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/65da400742.mp4?token=rT4uzI0IVXhYv8yweDVKBbaXqJ37BXlFsWhOh0ZwZKSMCZDPsC1mJKnghkiZOnOXKkdUUr1yK1583rFmCNxuY1z7cBWa7DKCoqbh5LD9RXz3_Z3bX34LqRcq3eHReEmtrWc3X5bTqv5FWGMQ4D6PQsVs75GPdYUIELLzAibWL5gHugAYBr25L7Bn4rIev67FX0-eIhmYnpY8FXCKEHXaz5tgCbjlk6KaukZuqSnrX6CEoqa9KN7frcUPeKp5tmu8q4PCXIMufxrG9HApTEe2qqpP_Ui2M_MgouZqE3uuwEAQqdOdW89KtqHacLTvR77daAvLd4poWx4WwGzf5Bwadg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/65da400742.mp4?token=rT4uzI0IVXhYv8yweDVKBbaXqJ37BXlFsWhOh0ZwZKSMCZDPsC1mJKnghkiZOnOXKkdUUr1yK1583rFmCNxuY1z7cBWa7DKCoqbh5LD9RXz3_Z3bX34LqRcq3eHReEmtrWc3X5bTqv5FWGMQ4D6PQsVs75GPdYUIELLzAibWL5gHugAYBr25L7Bn4rIev67FX0-eIhmYnpY8FXCKEHXaz5tgCbjlk6KaukZuqSnrX6CEoqa9KN7frcUPeKp5tmu8q4PCXIMufxrG9HApTEe2qqpP_Ui2M_MgouZqE3uuwEAQqdOdW89KtqHacLTvR77daAvLd4poWx4WwGzf5Bwadg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اون بابایی که با نخوت …</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/farahmand_alipour/6318" target="_blank">📅 22:41 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6317">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d716a2e5bd.mp4?token=RY8iORhWeianzhFDk1EeJxrAeIpPD09KiR3AT5-U9YZRzrGqmIMVMK17J84sqYwYp3Jts5i0Xq3p9-LO5aAI-IR-m9wKqJOVUNJSJX8kY2Y7DaU7RQfyywauAtDHMd_wY5X-tCdiJcIH9xB0vZlzvfDFSA9ivS-9r7QfTtjMJ7RY1BUajvCbhxsiU8QLkNKUuN-aZVnE__B7ohY3ymyQ661m15nUBUjWUMlDST4AAXAldiXRIuvFkHBDLiUNASD7jBqr5b_WcKD7wjLYtJ1oGOJBQclTbP5Y3UJ4VuWiBj88JmBKVTqaXZ_n7qHBDkMl-f4oZb-i6wRkRTy1fS2KCg33Ouxn5e-fPg6pURt-nX1Ngp5EEXWVJV4NmhDUbXh8HhS0CRkM3BIyYsWZrSG1uR-ArWP48qswKQbgV9bBYcgjijHJo8twZ3AS-oG3iTcs3Tl1J2Ynb9A28gW2giysHEvsyYOqxNOIP8dLnOQwYE46aWI9r_EIeaWebwpCXQS-ZEiCkdlueMRddenSn9gB1CcFEGehoHqD1qOQSP3qminhK4AkhUuSaglH0LO4QpUtNHPYvpsckkbydeBaMNBwCz9hVm2yKTQfsQ0e2w1p8nD7vY5U63XOcaz04dm6-GZr0ZaHuzyPoDDTnxXcfPG6ObZLQkqHqEa_niHpu-59X9I" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d716a2e5bd.mp4?token=RY8iORhWeianzhFDk1EeJxrAeIpPD09KiR3AT5-U9YZRzrGqmIMVMK17J84sqYwYp3Jts5i0Xq3p9-LO5aAI-IR-m9wKqJOVUNJSJX8kY2Y7DaU7RQfyywauAtDHMd_wY5X-tCdiJcIH9xB0vZlzvfDFSA9ivS-9r7QfTtjMJ7RY1BUajvCbhxsiU8QLkNKUuN-aZVnE__B7ohY3ymyQ661m15nUBUjWUMlDST4AAXAldiXRIuvFkHBDLiUNASD7jBqr5b_WcKD7wjLYtJ1oGOJBQclTbP5Y3UJ4VuWiBj88JmBKVTqaXZ_n7qHBDkMl-f4oZb-i6wRkRTy1fS2KCg33Ouxn5e-fPg6pURt-nX1Ngp5EEXWVJV4NmhDUbXh8HhS0CRkM3BIyYsWZrSG1uR-ArWP48qswKQbgV9bBYcgjijHJo8twZ3AS-oG3iTcs3Tl1J2Ynb9A28gW2giysHEvsyYOqxNOIP8dLnOQwYE46aWI9r_EIeaWebwpCXQS-ZEiCkdlueMRddenSn9gB1CcFEGehoHqD1qOQSP3qminhK4AkhUuSaglH0LO4QpUtNHPYvpsckkbydeBaMNBwCz9hVm2yKTQfsQ0e2w1p8nD7vY5U63XOcaz04dm6-GZr0ZaHuzyPoDDTnxXcfPG6ObZLQkqHqEa_niHpu-59X9I" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حسن روحانی ۱۳۹۷
تا آخر هم افتخار میکنیم به نفوذ
در عراق و سوریه و لبنان و…..</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/farahmand_alipour/6317" target="_blank">📅 22:30 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6316">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nVbLnpORzpKj_SKlWzTRz8w821_UypUKFAe0hhewa2KyrERNFdATzIW_mIphqrWbUa6hMrIbH9YH60DsYdNGObwa6vEZC6ksYEfHQdeDYA0E9ABc4OC4a-QOgAaonhVyTAFVnX6w5X9Jz0OLGxWFTxGDLBrT1-N6WfdXw99BYCUebKpfsULryvi_fe7M4g48liHL_2givLLDHFWDSQfqwjyA4PdaEZ1bw6M5D2sKPVAvsXPbt4KpozbZ1nrTF26kgf-5d5FgE0S1thRyPnET4yl7SOiHVcKl1SBsfORwE1B2W5yUUPyNK_0FT-FWMHk78qiPWnGI4MwzM0Tl-nQ8lA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏سخنگوی سپاه خطاب به شرکت‌های کشتیرانی‌:
مسیر مین‌گذاری‌شدۀ جنوب تنگۀ هرمز  [ آب‌های عمان] مسیر نابودی سرمایه ی شماست!
قرارگاه خاتم هم دقایقی پیش هشدار داده بود که فقط از آب‌های تعیین شده (بخش ایران) باید تردد کنند.
جمهوری اسلامی رسما آب‌های سرزمینی عمان رو هم ناامن کرده.</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/farahmand_alipour/6316" target="_blank">📅 22:22 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6315">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">🚨
قرارگاه خاتم :
تنگه هرمز همچنان بسته است و اگر قرار هم باشد شناوری از آن تنگه عبور کند صرفا باید از مسیر تعیین شده [از سمت آب های سرزمینی ایران و نه عمان] و برابر ترتیبات اعلام شده قبلی تردد نماید.
‏
🔺
در صورت عملی شدن تهدیدهای آمریکا، نیروهای مسلح جمهوری اسلامی ایران اجازه صادرات یک قطره نفت را هم نخواهند داد و زیر ساخت های نفت، گاز، برق و اقتصادی منطقه مورد هدف قرار خواهند گرفت.</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/farahmand_alipour/6315" target="_blank">📅 22:16 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6314">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gOC2REGQTTeetMhogI7TqJtcD4HjBAOXTZh6NkoEXDzhg1v8UvH8ZxTuxfeMOW8-jgSt3VVorDE_h5GoKARoeFumaHjAAmv2NnxdORddALdIQBYM7BBZ0zjs9ALl70MioU_t1REZFo-6-qO6kmIhY9L1XJm1Th4xnpa6c2s0nj17XTRMG6tFRgG9T3Nc7m28i-1AwXdmdCDvsdndiGmGacJifE9XZcGnFG7CYNtF8Ls9qAzNKPl2OoUyvKZe4MnBQfKySWzsgsNnIcQHpbFO-LzHgjKYGr6q0h356xmj5gvLOkFl4PMuYY4RF1dhDm0G-IGkhGYezIiZNLOA02D-1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
تهدید ترامپ: کشتی بزنید نیروگاه میزنم.</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/farahmand_alipour/6314" target="_blank">📅 18:06 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6313">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/doEVZN5_LqGHG9ZzDGLLbrK_ff43AiVfngYNLPtttfuJxKTTe0Q9po5JryXFzHeIPkgblBPXYRLgyehnZaiNM6l5hwjhNzrSL_ayC5eqEAl7kVI8_7Ll-QcUBTySf8WHmF9R3rz-XU3rksU2SDAA0PJKq3rPvgz9DA1uR4N4glDF1F2rDl8MfzlgZ2NY8H7EBtlJTo74bP1tWlhk8-vX037iQOXDqYg2_nIY4YWtTStkazW1YGg8DeyxJU6gs-wOy5x4-PBytn66wu3Jrn6rwO2GSW_siUZnPLfbXf5oI9yLThPAZaaa-ZUrTiOpP9DAxqpSK6b4ld-cyNDrOwgWJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
تهدید ترامپ: کشتی بزنید نیروگاه میزنم.</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/farahmand_alipour/6313" target="_blank">📅 17:20 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6312">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">🚨
شب گذشته صدای انفجار و پدافند هوایی در ۱۹ نقطه کشور
تهران،  بهبهان، امیدیه،  ماهشهر، سیریک، بندرعباس، بوشهر، چابهار، کنارک، تبریز ، بانه، کبودرآهنگ،  همدان، خرمدره، ابهر، زنجان، دینارکوه،  چوار، آبدانان و انارک.</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/farahmand_alipour/6312" target="_blank">📅 08:32 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6311">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9577aecbb9.mp4?token=PzgjEqXD8Y_e_JasiOdzZy_RUyRzNPMq6S_LoFmPNcGjWx8gvqJF_WJRnd08q4jXVlOvIXvKu9jkDLsArQIL-THGKX202-9WyGWxjp9GjrBciCwj0G3KW4hURSBYyChlQJhZ67S6w7H4jaClmEQDpLGaMxhmPSWDI3HH9XEmUSDoT2Vvr0BGDKHO-Vi3Q785SIBNuPNbGdUhyI_FtOJFie5OHSZCetlIPaG5eCxBwzuSXrbta-7CKet6QI3VQFOySFzu3ICjSItpgIUjeVzfvk2cCeV3CEe4I1JqvbfP0qzypwPMtbVRkWvvnYKb8O-iqx2zOl3wqfo46Jp3pcbvzA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9577aecbb9.mp4?token=PzgjEqXD8Y_e_JasiOdzZy_RUyRzNPMq6S_LoFmPNcGjWx8gvqJF_WJRnd08q4jXVlOvIXvKu9jkDLsArQIL-THGKX202-9WyGWxjp9GjrBciCwj0G3KW4hURSBYyChlQJhZ67S6w7H4jaClmEQDpLGaMxhmPSWDI3HH9XEmUSDoT2Vvr0BGDKHO-Vi3Q785SIBNuPNbGdUhyI_FtOJFie5OHSZCetlIPaG5eCxBwzuSXrbta-7CKet6QI3VQFOySFzu3ICjSItpgIUjeVzfvk2cCeV3CEe4I1JqvbfP0qzypwPMtbVRkWvvnYKb8O-iqx2zOl3wqfo46Jp3pcbvzA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هگزت وزیر جنگ آمریکا از ضرورت
برخورد با جمهوری اسلامی میگه
ونس، وزیر خارجه با ناراحتی به او نگاه میکنه.
(ونس طرفدار گفتگو است)</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/farahmand_alipour/6311" target="_blank">📅 08:28 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6310">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oimr43V0fDN_DLFQaVfVQ4p_p3IuMkTOm0HFgCoyVNV7yp3nN8y9du8Fl3Jn813ofDJ1-MRSZcAwULeDUujAipv2l0-hRcC398PKNSd9s3dVcdgP_jECndOGT1fKFoNwF26Qh52twnrfBGliCXEDcM-Icv5OaHtgdojvsbRdsfxKddJ_mNHM5E250qhhFlU_QW67KPSOIDNpyGx2EiCK1fvTXnVAXDh0FWfcB9JQgdg_Vz8vQNdDNnL28scVM5h4ZVnvptOtSOv1YYGsFpe2dRx32xrOsx7EL7fbS0jPaQcfqR8RfxU5mK8nMiqtSX5mU0fSO-qTowZ3o85vElHdYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
اندی برنهام نخست وزیر تازه بریتانیا که از دیروز در این کشور قدرت گرفت، با در اختیار گذاشتن پایگاه‌های بریتانیا به آمریکا برای حمله به جمهوری اسلامی موافقت کرد.
پایگاه‌های «دیه‌گو گارسیا » و «قبرس» از مهم‌ترین پایگاه‌های بریتانیا و مشرف به ایران است.</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/farahmand_alipour/6310" target="_blank">📅 00:52 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6308">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dfMEadtp6MFBhJo_VQuPEdw4Juicmb15Qd9yh4kUlq7oeRZvbW5ezLs3sHLosDMXUniVyadx4gmqVuqxvvjtMaMrkSXK80H0XdGOt4C82-0KBBqRWI34gpIL8-ir711u4sXFkvHGixRPiy01gqtejC5wDatEq42MXcuQ6uWkTLPisOxsp7k0czadCZQHhsm7CQypGuHn3prM8Pu17qjcgirQRHeSZX8N_NoxSsru2u9Dw2pVoUGH-KFj105AxTVWghX_10MU8n2XGkphP8Vjl5csLl15-JFac6DMVRkXyGQOxGWn5qVtkut93liziK57aSQBE9KbbolsvD_yFDp49A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ds-qnPLWEaRfgvKnMqRTsXEEPMrtvCuWCe0gb9aNJhO9fbshmFih2z3n5OAGX9HZIEqGrC0v5FfFzzBU-Xu9VHyW_HNtcbR7ByAAGt_bTLtT0P4F5VlmlmUcdDalGTKs3K8XLLbDVtlem2_5Lc0NAPNFpdVNEejSYUnSI4WEljauxefQHv4q4N18smjUI7gnFmsx5mHbTecCE7ikJSoqvThVi2pIFG5xo9-9F7iCnDksI5ab4pwKX44qXI947Qq1bCfpi408ZEvMZJut_ZgbYUa2GYb4yofbQ7WeLevodFbYWeKS1SB4yQxcI2vE9viznXlPHyzYyreqEcdyIZMTHA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">حسن روحانی رفته خونه لاریجانی تسلیت
چهره زنان رو!
بعد همین ها میگن اگه ما نبودیم داعش می‌اومد توی ایران
داعش ۴۷ ساله که در ایران حکومت میکنه.</div>
<div class="tg-footer">👁️ 30.2K · <a href="https://t.me/farahmand_alipour/6308" target="_blank">📅 23:28 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6307">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">🚨
🚨
گزارش کانال ۱۴ اسرائیل :
جمهوری اسلامی به سفارت اسرائیل در بحرین حمله کرد.</div>
<div class="tg-footer">👁️ 30.1K · <a href="https://t.me/farahmand_alipour/6307" target="_blank">📅 22:01 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6306">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pJqjEztCVRn7G6ho43a7xCSCrMPWJ-VaDR7sys42xU8ub5QLO0_qBw3l4sGMIFXjLVQBeqIbStFjVfjF1lUCFfYJtbTOfiw7c5IUCeXoiBs1JjJODHTKscjZ8hIXHUwjmcm0aiEjyZeXxQl59YOCme3dCmWh6azuiPqkQQKxUaqiHEQq7O68WqYcJlqPx7clUYGWHj70MpjlkuZfoiS7XMoHBDV0n9s-veCinWUoGz9_sFCO1YhL0kpsBoUKL3W2df7O4ZAyp_8yJBAv8nAYhMpAzjHCGYejXh0h4VbfvrEpkhhoUT8rmGRTQF77WI7cVAzAm13Fs9kZ6NaPF8CzFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">موقعیت کوه کلنگ، در نزدیک تاسیسات هسته‌ای نظنز، گفته می‌شود تونل‌های بسیار گسترده و وسیعی از چند سال پیش زیر لایه‌ای ۱۴۰ متری
از سنگهای سخت ساخته شده است
و پس از جنگ ۱۲ روزه،
هزاران سانتریفیوژ به این تونل‌ها منتقل شده.
گفته می‌شود اورانیوم غنی شده ۶۰ درصدی ج‌ا
در زیر این کوه پنهان شده است.
بازرسان آژانس بین‌المللی انرژی اتمی هرگز موفق به بازدید از این مکان نشده‌اند.</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/farahmand_alipour/6306" target="_blank">📅 19:28 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6305">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3814b8c91f.mp4?token=L5kxFjVJlHBr6WbbVO92XUnfvoSL8D6_rysVliH6aBaXARxflhCkAyZVYj0macMKNjENgtByH9rqxltntqcOZld3cAwtkE-zWMv60Woz54sYusD-r_YTXqEPMw_igjCyjaZCe1Je1rVQX1JWbhcrNax0exJtP_0OegoYtHoeIR5WZaVzouaf5S5tFiYZvVVm8K9i4iLkPtcNfKPbHDp3bfoFGTWf49cYDCocezMoBGgTzeltMVc5UnVTAkl1awZFniwv-rHvDsp9Xcq39Mi3LBuVctT6mLfvxIWR4ihLHG3hmWIjcb0ditlag8woGo09Jfsk9z2wihZd6dxlJtFStzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3814b8c91f.mp4?token=L5kxFjVJlHBr6WbbVO92XUnfvoSL8D6_rysVliH6aBaXARxflhCkAyZVYj0macMKNjENgtByH9rqxltntqcOZld3cAwtkE-zWMv60Woz54sYusD-r_YTXqEPMw_igjCyjaZCe1Je1rVQX1JWbhcrNax0exJtP_0OegoYtHoeIR5WZaVzouaf5S5tFiYZvVVm8K9i4iLkPtcNfKPbHDp3bfoFGTWf49cYDCocezMoBGgTzeltMVc5UnVTAkl1awZFniwv-rHvDsp9Xcq39Mi3LBuVctT6mLfvxIWR4ihLHG3hmWIjcb0ditlag8woGo09Jfsk9z2wihZd6dxlJtFStzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏
🚨
🚨
ترامپ: قطعا به زودی و با شدت زیاد به کوه کلنگ  در ایران حمله خواهیم کرد و هیچ کاری از دستشان برنمی‌آید.
‏ترامپ در دیدار با رئیس جمهور لبنان گفت: «ما قطعاً به سایت جدیدی که آنها در مورد آن صحبت می‌کنند (کوه کلنگ ) حمله خواهیم کرد.
آنها به دلیل سلاح‌های هسته‌ای در این وضعیت هستند و سعی در بازسازی یک سایت هسته‌ای دارند.
‏ما به آن سایت ضربه خواهیم زد. هر سایتی را که آنها حتی به سلاح‌های هسته‌ای فکر کنند، با قدرت بسیار بسیار زیادی خواهیم زد.
تا الان زیادی باهاشون راه اومدیم!»</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/farahmand_alipour/6305" target="_blank">📅 19:17 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6304">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/acc280d27d.mp4?token=GPrNNPEHoZIIURLj_R3fA3IG1tg95dqp8xHp0RrowZg_22POR59uFcv-N0JGhVmVW2L1G54NiQUX7rB8RR4ymlmtvoSRZJYcIWsV2Ubeot9-P6SvMIDY6qN6EXsnxJPdvn_7BOrcvqLcbAJsvy2HOnLy3XJFO7qvg8DNIGVxQv-jeR3ni-RQTfrDXOC0Qo6uA2IZ_poSZbWFuXzcsdbJUEEPgpUJSEH5rr2_MOH2AQNP83dZiIGvNJeFbwq9shknt3IAH-FKZWHH95tgu850OdmtM4shyYIHXyIi5vV9aQAKup6BGauSUVKpe5mR3thv_MRLlFidHQ3JCZ4qbkVQug" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/acc280d27d.mp4?token=GPrNNPEHoZIIURLj_R3fA3IG1tg95dqp8xHp0RrowZg_22POR59uFcv-N0JGhVmVW2L1G54NiQUX7rB8RR4ymlmtvoSRZJYcIWsV2Ubeot9-P6SvMIDY6qN6EXsnxJPdvn_7BOrcvqLcbAJsvy2HOnLy3XJFO7qvg8DNIGVxQv-jeR3ni-RQTfrDXOC0Qo6uA2IZ_poSZbWFuXzcsdbJUEEPgpUJSEH5rr2_MOH2AQNP83dZiIGvNJeFbwq9shknt3IAH-FKZWHH95tgu850OdmtM4shyYIHXyIi5vV9aQAKup6BGauSUVKpe5mR3thv_MRLlFidHQ3JCZ4qbkVQug" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
نخست وزیر اسپانیا : «در تهران، یک خامنه‌ای با یک خامنه‌ای دیگر که بدتر است جایگزین شده؛ چون مجتبی از پدرش خون‌ریزتر و دیکتاتورتر است و او واقعاً سلاح هسته‌ای می‌خواهد.»</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/farahmand_alipour/6304" target="_blank">📅 18:49 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6303">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/403aadedf7.mp4?token=rEDfYoVDB-N6xY3hyepgVG3d57QzdtDbyxX-jPAegNrNDy5gkE9j_pm70I4e8ccxOuS4FKzevviEVeXMqJRMXUip22frwR-xmuNt89QupunAW2FFIm3PBs6Yv668uUk8z-_LQ9I5MPBkhAwQ1YBVw16Nw5S7VhJXxalwLhoAu0KvMHPSaBW4jTKH2FOFBl2X7ZIwOFNF8HrUt9I7s-rilgh39veiVn7DAMkgJCbRVjWrV1FalBL-0QKuenlQyk2j_GYYPwgRJ5XnsYsyvC782HA8U35BOoHTXOX8Xx84uc0LCR84pbjMDTx4I2vTpfdLJSmZ5Y4hU8Hyr7R8fLMfCg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/403aadedf7.mp4?token=rEDfYoVDB-N6xY3hyepgVG3d57QzdtDbyxX-jPAegNrNDy5gkE9j_pm70I4e8ccxOuS4FKzevviEVeXMqJRMXUip22frwR-xmuNt89QupunAW2FFIm3PBs6Yv668uUk8z-_LQ9I5MPBkhAwQ1YBVw16Nw5S7VhJXxalwLhoAu0KvMHPSaBW4jTKH2FOFBl2X7ZIwOFNF8HrUt9I7s-rilgh39veiVn7DAMkgJCbRVjWrV1FalBL-0QKuenlQyk2j_GYYPwgRJ5XnsYsyvC782HA8U35BOoHTXOX8Xx84uc0LCR84pbjMDTx4I2vTpfdLJSmZ5Y4hU8Hyr7R8fLMfCg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اسپانیا که این روزها دارند
پرچمش رو میچرخونن!
می‌خواستیم ۲.۵ میلیون دلار بهشون بدیم
برای اینکه با ما فوتبال بازی کنن، قبول نکردن!</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/farahmand_alipour/6303" target="_blank">📅 18:43 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6302">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">در مصاحبه عراقچی
حرف از تونل‌های زیادی میشه
که سران حکومت به اونجاها پناه میبردن،
سایت‌های موشکی‌شون هم،
که همه در پناه تونل‌ها عمیق در دل کو‌ه‌هاست!
جمهوری اسلامی فقط برای سرانش
و برای موشک‌هاش، پناهگاه ساخته!
ولی برای مردم حتی آژیر هم نمیکشد!
چه برسه به پناهگاه!
اینترنتشون رو هم‌ قطع کرد!
خامنه‌ای رو هم غافلگیر کردن و الا
مثل جنگ ۱۲ روزه که تا دو هفته بعدش
به «کمین ‌گاه» رفته بود، به مخفی‌گاهش میرفت.</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/farahmand_alipour/6302" target="_blank">📅 16:57 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6301">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TdBFJqvSj4dZMRj6RqZFVyBI07C8E3ZBxTH97Tu6YiTMqsetjmvPit-Rwja68TbynuzekICIBQBQVxUUNXA8nQaFflfVbpXgnctTq23kJAkTlZkbPOyWRdUSijKAN-WZsQg1oox0GPofc2gvXUqO_HLVXKYtql_M42G52oMMJCJX6msFAY7tgAItu0jSviXyiVFgZHstyNy5PH2Nuz7LQql8yrEIFvN9DQ2kQfJfPlZwWSGyqECjfKWVtBFi8gRlw2HKAehJaYmH_xnSiOqZ8fAzLmHZoxu3wHtKkjl_PRE_I-xNYLOgpGN8LquKP1PLjCA8wn8R-mskD1Zbe6ZqMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ با بازنشر تصویر گل‌محمد محمدی ۲۳ ساله، که امروز به دست جمهوری اسلامی اعدام شد:
«جدیدترین قربانی از اون ۵۲ هزار نفر  معترض کشته شده.
وحشی‌ها!
کی قراره دمکراسی‌ها بیدار بشن؟ (نسبت به جنایات ج‌ا) »</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/farahmand_alipour/6301" target="_blank">📅 16:52 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6300">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/46c8806804.mp4?token=TcuvJ9wJKiQXqJSiQjI4ADgXA2RJ-34awtpaphdB-rgfHFiJ7ZErPG2OMONuBDO-u2EJUeEGojPMl2KoZt2rgn_DymzfshnOq7Kob66x2XAtg_gqF6jheVzVRS3h2YXxKEcafPCr_uGTB_49vy7vv7rypn3kGmiv1vsc8ls6wOuNgPdzyMPD4fJvDStV-2Lffi8ScafME00al_Zj26O4FdUwwOUu-qaR-y6GMunlbvDuvYVkTkR0gQp4AWbB0bcOxrzyE7fSsjUdfLRGbW5QtbVTvtlRGCGFPpmTIep_YQtQvTYL2-K6OzaOBW0zTp7cDII2rGvdI8CqwhXnQRJybA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/46c8806804.mp4?token=TcuvJ9wJKiQXqJSiQjI4ADgXA2RJ-34awtpaphdB-rgfHFiJ7ZErPG2OMONuBDO-u2EJUeEGojPMl2KoZt2rgn_DymzfshnOq7Kob66x2XAtg_gqF6jheVzVRS3h2YXxKEcafPCr_uGTB_49vy7vv7rypn3kGmiv1vsc8ls6wOuNgPdzyMPD4fJvDStV-2Lffi8ScafME00al_Zj26O4FdUwwOUu-qaR-y6GMunlbvDuvYVkTkR0gQp4AWbB0bcOxrzyE7fSsjUdfLRGbW5QtbVTvtlRGCGFPpmTIep_YQtQvTYL2-K6OzaOBW0zTp7cDII2rGvdI8CqwhXnQRJybA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خامنه‌ای: ما دنبال اقامهٔ حکم الهی هستیم! ما هستیم برای تحکیم دین خدا! برای رونق اقتصادی و… که دیگران هم می‌توانند انجام بدهند و در دنیا هم انجام می‌دهند!  بله! بقیهٔ دنیا دنبال ساخت کشورشان هستند، این‌ها برای تحکیم دین خدا!! پول و ثروت ایران برای این خرج…</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/farahmand_alipour/6300" target="_blank">📅 16:28 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6299">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">‏رویترز: حوثی‌های یمن در ایمیلی به شرکت‌های کشتیرانی نسبت به بارگیری یا تخلیه بار در بنادر عربستان سعودی هشدار دادند.</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/farahmand_alipour/6299" target="_blank">📅 14:26 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6298">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">🚨
جمهوری اسلامی امروز دست به حملات گسترده‌ای به قطر و بحرین زده.
علاوه بر این جمهوری اسلامی به دو کشتی یونانی در تنگه هرمز حمله کرده.
حمله به اردن هم ادامه داره.</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/farahmand_alipour/6298" target="_blank">📅 13:16 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6297">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3cb0045793.mp4?token=COMWKUrzOctzLZs6FzZOFDKDrlidqE-Hf3cA8fVQP1op9dVm6vByRZ5czVwrUR8bvDpb5LruNJGHT96VeNO-11ff7-roR1d22bK_wGQXYQY-fg3q3wJlSG7GN5Zv5Q6tHNPMD8zmQhA96nd8Hcfi0_z9gjZga0D9d14W3m7NQtPqAa8vnMR2N5Ibu8M8h3GDTMrwELIiKx66uq-GQQlvDkgfRNNXWm7tgj6ERQvEl1JUBICRlh1hQGZURMnZxAphv79UlVQo_YFLhMNkXb9zbKQXPIxIDWlsbVYg0sCof-7Y3-Hq3oo9SjXHZY0rsYrpUNutgIT3sCPRC6BkMRaIsg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3cb0045793.mp4?token=COMWKUrzOctzLZs6FzZOFDKDrlidqE-Hf3cA8fVQP1op9dVm6vByRZ5czVwrUR8bvDpb5LruNJGHT96VeNO-11ff7-roR1d22bK_wGQXYQY-fg3q3wJlSG7GN5Zv5Q6tHNPMD8zmQhA96nd8Hcfi0_z9gjZga0D9d14W3m7NQtPqAa8vnMR2N5Ibu8M8h3GDTMrwELIiKx66uq-GQQlvDkgfRNNXWm7tgj6ERQvEl1JUBICRlh1hQGZURMnZxAphv79UlVQo_YFLhMNkXb9zbKQXPIxIDWlsbVYg0sCof-7Y3-Hq3oo9SjXHZY0rsYrpUNutgIT3sCPRC6BkMRaIsg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">«آتش‌بس نظر مجتبی است؟ »
عراقچی طوری پاسخ میده
که گویی نمی‌دونه این نظر مجتبی بود
یا نبود! «ارتباط سخته»!
خودش هم میگه مجتبی رو هیچ وقت ندیده!
اصلا معلوم نیست زنده است یا کشته شده
برای همینه که نمی‌دونن نظرش چیه</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/farahmand_alipour/6297" target="_blank">📅 11:54 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6296">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/011fb08ef0.mp4?token=mJQN1et_RRf0OjRnM3lzBF_4dcVoPUJb9cv16eAtoSI0EPrmdcE8euqaq8TffAX1MhL0jQG6nWyVHMuouJiuNEowIjDowjGUecJiRS2E9-H0yqBmYhqMrQ2IskOq40vOLLEPp8-8jkSAjGfAbJI1qTUq8FVZVTz5U6o3QiUqtQzMHqIaYDFQf4wfAG51ZEy6nIAwMLGahvC5TDGCoeF4tvja5UsLJZvKxFwHDwISrYmF2A0PstWZNWqTWsdutsyJKpb1F_HlqOf0OmjcOZFj_K7lcZ63o8DNpVOF9hU4aBibsSe69Y2G9Y2DVWAcSFeaUhHHfqFxdNRwrDJa8-LpmQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/011fb08ef0.mp4?token=mJQN1et_RRf0OjRnM3lzBF_4dcVoPUJb9cv16eAtoSI0EPrmdcE8euqaq8TffAX1MhL0jQG6nWyVHMuouJiuNEowIjDowjGUecJiRS2E9-H0yqBmYhqMrQ2IskOq40vOLLEPp8-8jkSAjGfAbJI1qTUq8FVZVTz5U6o3QiUqtQzMHqIaYDFQf4wfAG51ZEy6nIAwMLGahvC5TDGCoeF4tvja5UsLJZvKxFwHDwISrYmF2A0PstWZNWqTWsdutsyJKpb1F_HlqOf0OmjcOZFj_K7lcZ63o8DNpVOF9hU4aBibsSe69Y2G9Y2DVWAcSFeaUhHHfqFxdNRwrDJa8-LpmQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">محمد اکرمی نیا سخنگوی ارتش
‏به روشنی میگه اكر آمريكایی‌ها
بيان در جنوب ايران ما خاك خودمونو هدف قرار میدیم.</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/farahmand_alipour/6296" target="_blank">📅 11:35 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6295">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromحافظه تاریخی</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/78bd1813e8.mp4?token=QaZPv5VMbHVhSEKduGnJzYlPooZqAemux0V5OTtyNORs5__uZjrMsBb5d3Zljxgxnoow9xXP4lkmDkI5s4B1e1ngVMsor8XREK4lziqzkPeHF1Scf3ZVGRX9yl2clHnh4Qt0_pTAb2WvzqFrAs5zKWh6XFun8EKsjcXEHHZ4t-to0_ZUBjV0AB8aO-QPHGNMc0_-j8kCYyhNfJPkOZgq9vH_rS-bPldVaD8eoVUYb1axdeqHIbWE8EPbu5oVBu-AGRxnHNQzPeiKXpWr0Tva34UJ0_bcnOa8sNPrPUhzHh3XWUjIVrfjDIvYV6tiYy4cvTRxWELYVrvY7-irH8NVLJOBrsloryPlGQb8CmjWuLlhZpGOBxpJnfK0GlZMG68_5V8VsYLIU26Ns_pvnvYNwZ8DgN9OyyYcjluG2eS9Blyofm0NE8-gZ18KWlUi5P6EA_gmuYR8OAgIcbxV5rx3KuNhnx-fsn0BYTNUF_xuhf37jAgSfc3VNcqUksWb0AgIokg7lItv0umf7iNOfwpa2KIh7G4JFUu4yHPGhOPr98ZicwjiOMSLzcwVlg7HcLMjOS25uQmaeAkOw1ql3RzaE1mIVDfSlQV_OdrcZ0uebbJYjJ0boQ2ebxf5yd3aU2a2-wTA-1gblfpVygcFvpQ0BPb16efWnR13TkKeMb8EMdU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/78bd1813e8.mp4?token=QaZPv5VMbHVhSEKduGnJzYlPooZqAemux0V5OTtyNORs5__uZjrMsBb5d3Zljxgxnoow9xXP4lkmDkI5s4B1e1ngVMsor8XREK4lziqzkPeHF1Scf3ZVGRX9yl2clHnh4Qt0_pTAb2WvzqFrAs5zKWh6XFun8EKsjcXEHHZ4t-to0_ZUBjV0AB8aO-QPHGNMc0_-j8kCYyhNfJPkOZgq9vH_rS-bPldVaD8eoVUYb1axdeqHIbWE8EPbu5oVBu-AGRxnHNQzPeiKXpWr0Tva34UJ0_bcnOa8sNPrPUhzHh3XWUjIVrfjDIvYV6tiYy4cvTRxWELYVrvY7-irH8NVLJOBrsloryPlGQb8CmjWuLlhZpGOBxpJnfK0GlZMG68_5V8VsYLIU26Ns_pvnvYNwZ8DgN9OyyYcjluG2eS9Blyofm0NE8-gZ18KWlUi5P6EA_gmuYR8OAgIcbxV5rx3KuNhnx-fsn0BYTNUF_xuhf37jAgSfc3VNcqUksWb0AgIokg7lItv0umf7iNOfwpa2KIh7G4JFUu4yHPGhOPr98ZicwjiOMSLzcwVlg7HcLMjOS25uQmaeAkOw1ql3RzaE1mIVDfSlQV_OdrcZ0uebbJYjJ0boQ2ebxf5yd3aU2a2-wTA-1gblfpVygcFvpQ0BPb16efWnR13TkKeMb8EMdU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حملات نیروهای مقاومت فرانسه به رهبری ژنرال دوگل به زیرساخت‌های فرانسه و منفجر کردن پل‌ها، قطارها و خطوط راه‌ آهن در جریان بمباران‌های متفقین برای آزادسازی فرانسه اشغالی از حکومت نازی‌ها، ۱۹۴۴
@hafezeye_tarikhi</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/farahmand_alipour/6295" target="_blank">📅 09:37 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6294">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">واکنش نیروهای مقاومت فرانسه به رهبری ژنرال دوگل به کشته شدن ۶۶ کودک فرانسوی بر اثر خطای بمباران متفقین در جریان عملیات آزادسازی فرانسه از حکومت تحت حمایت نازی‌ها @hafezeye_tarikhi</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/farahmand_alipour/6294" target="_blank">📅 09:31 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6293">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromحافظه تاریخی</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/59eba4787d.mp4?token=kb7I8D4U7uuzF7KHW0aAOeuFTIlRwwMjbAcnxhuooDeI0rCSoXWcOtDtES8_H4Bbxy_D_MErwhkqsCTmXR-8NR4VmRzP_SIxuw9u7wU99ME6ACdJq36VVRbxMN8KKAvjg-Fds0uJteJY7RbHmSAVLgF1IRoWgJGP54U-VVAgz2RVgmQtNj1fNObZIxKnIGE2t81jLHScH06b8LJsfDSoCW7cjmZS6lwiphtj9c97cf47ryGP6D_NMDQy1Odh38kUORpjF6Jlmh_op84lap4ilHX1QHWk1D3ZN_sUhyGKTgjhdazWq5rg0ZP04u5Flb7QZ-tqSS_RmMJQuhSOWXESAQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/59eba4787d.mp4?token=kb7I8D4U7uuzF7KHW0aAOeuFTIlRwwMjbAcnxhuooDeI0rCSoXWcOtDtES8_H4Bbxy_D_MErwhkqsCTmXR-8NR4VmRzP_SIxuw9u7wU99ME6ACdJq36VVRbxMN8KKAvjg-Fds0uJteJY7RbHmSAVLgF1IRoWgJGP54U-VVAgz2RVgmQtNj1fNObZIxKnIGE2t81jLHScH06b8LJsfDSoCW7cjmZS6lwiphtj9c97cf47ryGP6D_NMDQy1Odh38kUORpjF6Jlmh_op84lap4ilHX1QHWk1D3ZN_sUhyGKTgjhdazWq5rg0ZP04u5Flb7QZ-tqSS_RmMJQuhSOWXESAQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">واکنش نیروهای مقاومت فرانسه به رهبری ژنرال دوگل به کشته شدن ۶۶ کودک فرانسوی بر اثر خطای بمباران متفقین در جریان عملیات آزادسازی فرانسه از حکومت تحت حمایت نازی‌ها
@hafezeye_tarikhi</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/farahmand_alipour/6293" target="_blank">📅 09:30 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6292">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3ba53f516a.mp4?token=tT5H8zIEYl5drMNWGrjT-4c7dzc6X53IHjgttQq7np5oebandvrLl5L5rGK72zdxZBGNEbY0SN4iA15tQ33jRvV3vKvP8YNVhfQtCfXi4ZZu2fWLfoNKJy-f3JGKT1eEjdgOYDRRTQsxgGvrXHKpGwRZIrdxHvLvWFc6lHKOvUCMRUu0BAM_OEzbRA0LUkJTJcYqeRGzLxiyiw5fldeL9qKDZoGZpk4Ug6RzZJq3nODxHNZQsOc8Pg6i2SRxa8EZ2mUDkJdeoZzXcZjZeYVz98_86oT94zmlLRypOiA-tf5f5ruQJuK1gKK7VGRzHWGCpqvS2DoF7kEo1WpEANXzUw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3ba53f516a.mp4?token=tT5H8zIEYl5drMNWGrjT-4c7dzc6X53IHjgttQq7np5oebandvrLl5L5rGK72zdxZBGNEbY0SN4iA15tQ33jRvV3vKvP8YNVhfQtCfXi4ZZu2fWLfoNKJy-f3JGKT1eEjdgOYDRRTQsxgGvrXHKpGwRZIrdxHvLvWFc6lHKOvUCMRUu0BAM_OEzbRA0LUkJTJcYqeRGzLxiyiw5fldeL9qKDZoGZpk4Ug6RzZJq3nODxHNZQsOc8Pg6i2SRxa8EZ2mUDkJdeoZzXcZjZeYVz98_86oT94zmlLRypOiA-tf5f5ruQJuK1gKK7VGRzHWGCpqvS2DoF7kEo1WpEANXzUw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">۲۱ ماه پس از کشته شدن «یحیی سنوار» رهبر گروه تروریستی حماس، این گروه «خلیل الحلیه» را به عنوان رهبر جدید خود معرفی کرد.  او در رقابت با «خالد مشعل» موفق شد این پست و مقام را بگیرد زیرا که بیش از خالد مشعل، مدافع اقدامات یحیی سنوار بود و جنایت ۷ اکتبر! که چیزی…</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/farahmand_alipour/6292" target="_blank">📅 09:15 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6290">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FZXgkvFcf1JhLCtxwtDyzKpqfsQw-r30EQ6tim0przoRN4YHjAY7fbxSfOegcDMvXnVWcLLxpw8WyFe-vekecx2KTSrA0KcWA5NTjlmLYvYLbgwoDHczBd0urdN5nbOJmZHtKXPl4ULymsQ9hlCTfF6TRPIKCiS5YDwrpJeki-YZiD5ieSQwmhzHsVqsKpeYVAdFaQGSNTULl7m-JXzetSqp4yc7wjT0Eu8kddrsEFqU5EbdKJGWHRtHL5RYknq7Wbr1YNbBPDYElEoL0khjuabbkJtM7JkL7ZZpbf-oEkf8_faoJTKSNx7H2nywgKMysJDyvnHTi9W0I6rssu79cw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۲۱ ماه پس از کشته شدن «یحیی سنوار» رهبر گروه تروریستی حماس، این گروه «خلیل الحلیه» را به عنوان رهبر جدید خود معرفی کرد.
او در رقابت با «خالد مشعل» موفق شد این پست و مقام را بگیرد زیرا که بیش از خالد مشعل، مدافع اقدامات یحیی سنوار بود و جنایت ۷ اکتبر! که چیزی جز فاجعه برای غزه نداشت!
تصویری از خلیل الحلیه، رهبر جدید حماس با خامنه‌ای. هم خامنه‌ای و هم یحیی سنوار توسط اسرائیل حذف شدند.</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/farahmand_alipour/6290" target="_blank">📅 09:12 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6289">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MzvRawHvNcVs2UwPa5JYct0DIDu57AC4VDJ9-JTDeHZnhYGDPmoflLmXWJlsF7AG5g4hXGDJlGNIVCuBBArxvj9VimNGaavDxIjqwsKp9YYDwnB-M5yTS8F11FA2iw9UDhA_ba8VqRF8rxWwkB9yo1lAYix24VE0POrhc1zKKPdoGJ7Ta3wO_eXYduzTTM82HBv2rI2GaKWW8Oya-HJBvXBGAV7qB3PEA0ei0H5sTivhnhUyHas7ug2h9yQv6CFaoX0Mcv3uLMRBj4xxAvM40C_ahfs0C-eN7NxZjMtwr6fYmu2sr8gKmFmFBZLsZtdBGrxQV3DssB1wL5ZJ6wF8tA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارزیابی اطلاعاتی اسرائیل نشان می‌دهد جمهوری اسلامی پائیز گذشته هزاران سانتریفیوژ غنی‌سازی اورانیوم را به تونل‌های عمیق در کوه کلنگ منتقل کرده است.</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/farahmand_alipour/6289" target="_blank">📅 06:50 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6288">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">یک ارزیابی جدید از نهادهای اطلاعاتی آمریکا به نتیجه‌ای رسیده که ظاهراً مطابق میل ترامپ نیست:
حملات اخیر بعید است رفتار ایران را تغییر دهد و جنگ در وضعیتی از
«بن‌بست نامحدود میان جنگ و صلح»
گرفتار شده است.
به نوشته
واشنگتن پست
، تحلیلگران اطلاعاتی به این نتیجه رسیده‌اند که دولت ایران احتمالاً نه فشار قابل‌توجهی از موج جدید حملات احساس خواهد کرد و نه موضع خود در مذاکرات را نرم‌تر می‌کند. این گزارش که توسط سازمان اطلاعات مرکزی آمریکا (CIA) تهیه شده، پیش‌تر در اختیار دولت آمریکا قرار گرفته است.
نهادهای اطلاعاتی معتقدند واشنگتن و تهران در وضعیتی
«نامشخص و طولانی‌مدت میان صلح و جنگ»
قرار گرفته‌اند. همچنین در یک ارزیابی CIA در ماه مه آمده بود که ایران حتی در صورت اعمال محاصره دریایی، می‌تواند
سه تا چهار ماه
دوام بیاورد و تنها پس از آن با مشکلات شدید مواجه شود.
Jonathan Panikoff
افسر پیشین اطلاعاتی آمریکا، درباره این فرض دولت که «حملات شدیدتر نتیجه خواهد داد» گفت:
«این ارزیابی تقریباً به‌طور قطع نادرست است؛ زیرا اولویت اصلی حکومت ایران بقاست و حتی اگر این حملات به مردم و اقتصاد کشور آسیب جدی وارد کند، باز هم حکومت حاضر است این هزینه‌ها را تحمل کند.»
مارکو روبیو
نیز آشکارا به اختلافات داخلی در ایران اشاره کرد و گفت: مقام‌های ایرانی به آمریکا می‌گویند که خواهان توافق هستند،
«اما میان آنها و جناح تندرو تنش وجود دارد»
و او نمی‌داند اگر تندروها دست بالا را پیدا کنند، چه اتفاقی خواهد افتاد.
هم مجتبی خامنه‌ای و هم قالیباف آخر هفته بر ضرورت
«وحدت»
به‌عنوان شرط پیروزی تأکید کردند؛ نشانه‌ای از اینکه حکومت در حال بستن صفوف داخلی خود است.
این ارزیابی دقیقاً در نقطه‌ای منتشر شده که وب‌سایت
Axios
نیز از آن به‌عنوان یک دوراهی یاد کرده بود:
ده شب بمباران، سه کشته آمریکایی، و در نهایت این جمع‌بندی تحلیلگران خود دولت آمریکا که مسیر کنونی به بن‌بست منتهی می‌شود، نه به وادار شدن ایران به تسلیم یا عقب‌نشینی.
به تعبیر نویسنده، جامعه اطلاعاتی آمریکا عملاً به این نتیجه رسیده است که
«گزینه دوم»
ــ یعنی یک عملیات نظامی گسترده و مشترک ــ تنها مسیر نظامی است که می‌تواند وضعیت را به‌طور اساسی تغییر دهد؛ در مقابل،
آتش‌بس ۱۰ روزه
تنها راه خروج از بحران است که نیازی به چنین عملیات گسترده‌ای ندارد.</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/farahmand_alipour/6288" target="_blank">📅 06:40 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6287">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/75cc0ec8fd.mp4?token=hZlrn58j8gfeD1FSYwISu5y5H_N8r5mOSlbDuItoWmkhiFKKQQWl_XPuv4T_fYtFgGfoaxMdH4_XUQ5P4ycEPA41tSSlkA8gFDLKPmC5usnx-450B6-HgUBho5nHjxYPGdsc3FyGpHOYxBZhzP-qQ62wk2lm8mhaLrWduMK-7BhWyG-O8aEJgcDsXJ4SFvMMpR7yqDLOUEXCzvTaxO_4YJNpxJFX7kl_KDc53Ujyc-gbyir3uT_xyISJlfYyEaczn1aR71foXWYIpazad9iFj6GJcCeEI5WFoIxePDvh9GKD72OX5tf0Ut3GSntYxDj0-Unhy4WxtS0Ghol_fOc3WolKq1xF7VH22SQg_3hKnk2y11VSFSY3IN0wC4RCWg8TxR_c8qUYNVREP-LzyRdoqP661aQZHqKtUfBhkdT27fmT4vNdeusnyCGARV6S112BtsGYRu4-CJbaDVBmkxW4LegbKnhQ54lPIsulcp2SiBVLZf4JoMzC4S01ErGl04dm_8aGSHhGJK4u8RVQ7syehSbk0qclzU6fRpj_xaC5h09bJyo4Q10pkW5O_xpCHeGmuDIaNkOIwO-nIbHjqMevVQKl8AhAcqbnHjAHaHRgNY3J6s0NUe6-Emvwsfh3DIJvjaLsy402ZyaM35KiUbUfJzz5bDeTcz3i-T0AG5ghsJI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/75cc0ec8fd.mp4?token=hZlrn58j8gfeD1FSYwISu5y5H_N8r5mOSlbDuItoWmkhiFKKQQWl_XPuv4T_fYtFgGfoaxMdH4_XUQ5P4ycEPA41tSSlkA8gFDLKPmC5usnx-450B6-HgUBho5nHjxYPGdsc3FyGpHOYxBZhzP-qQ62wk2lm8mhaLrWduMK-7BhWyG-O8aEJgcDsXJ4SFvMMpR7yqDLOUEXCzvTaxO_4YJNpxJFX7kl_KDc53Ujyc-gbyir3uT_xyISJlfYyEaczn1aR71foXWYIpazad9iFj6GJcCeEI5WFoIxePDvh9GKD72OX5tf0Ut3GSntYxDj0-Unhy4WxtS0Ghol_fOc3WolKq1xF7VH22SQg_3hKnk2y11VSFSY3IN0wC4RCWg8TxR_c8qUYNVREP-LzyRdoqP661aQZHqKtUfBhkdT27fmT4vNdeusnyCGARV6S112BtsGYRu4-CJbaDVBmkxW4LegbKnhQ54lPIsulcp2SiBVLZf4JoMzC4S01ErGl04dm_8aGSHhGJK4u8RVQ7syehSbk0qclzU6fRpj_xaC5h09bJyo4Q10pkW5O_xpCHeGmuDIaNkOIwO-nIbHjqMevVQKl8AhAcqbnHjAHaHRgNY3J6s0NUe6-Emvwsfh3DIJvjaLsy402ZyaM35KiUbUfJzz5bDeTcz3i-T0AG5ghsJI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نماینده رودبار :
اول جمهوری اسلامی ‌آتش‌بس
را نقض کرد و سپس آمریکا پاسخ داد.</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/farahmand_alipour/6287" target="_blank">📅 01:10 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6286">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">🚨
گزارش انفجار مهیب در شیراز
🚨
گزارش انفجار در اصفهان</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/farahmand_alipour/6286" target="_blank">📅 01:02 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6285">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">🚨
🚨
به گزارش خبرگزاری ایرنا، در ساعات اخیر صدای حداقل ۱۴ انفجار بزرگ و کوچک در چابهار و کنارک شنیده شده است.
فرماندار چابهار : از محل اصابت‌ها هنوز اطلاعی نداریم!</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/farahmand_alipour/6285" target="_blank">📅 00:32 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6284">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">🚨
🚨
گزارش چندین حمله به چابهار،
🔺
چندین انفجار در بندرعباس،
🔺
انفجار در سیریک، قشم، بوشهر، دزفول.
🔺
پرواز جنگنده‌ها بر فراز چابهار در ارتفاع پائین.</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/farahmand_alipour/6284" target="_blank">📅 00:06 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6283">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">🚨
آمریکا از شهروندانش خواست تا هرچه سریعتر خاورمیانه را ترک کنند.</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/farahmand_alipour/6283" target="_blank">📅 00:03 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6282">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oAqBQOWzqxsg5SuxlkeArPwaTVpm22MsHZBmiKPoK0mNXrm9JEGv6SOuxFSgvOd4ZkKkPwxlIK53vXHtDmfRWWGMmH3XiaH48Wk5qWMtUh9DTNAbzHvZHovYfjCqCw0DQs6ic2P-yG1bjs6_GTUCFYbvJLDO731oY25Dr82pQMr9zKXYB7yWyFIIqY4cOSSG6-rQ_aAX2QrrzOCNEOblF0IKztZkl1Tb3pOF1Ar0MvMaL-lfJBw7sI_KzjL517hmx0xeomWzQnMmhaV3qMsRop_UUiLVacmdNJLJVFWAGFKfgrwLfq6SI1-LPHcqLTKtimx9S3bZS7ceThif4BXRFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ :
اگه قراره کسی دستگیر شود، سران جمهوری اسلامی هستند.</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/farahmand_alipour/6282" target="_blank">📅 21:09 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6281">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AbQvNkqehP34QuwfBBtCW4QwIDORQj-mZ2ekNKI-slXuN04CUezQ9OP3FL0DEkX4nhOzHtyvtwmK_XEw2-Ome67LoPgyDexvQLTDdDiW-tlbcXSHLATMakGKQ3Vt87j2sTpUqYGws--tQCbD_tl1vOMgDCAj-KYWDS1RpqDiwg3NPSx4V5Ej-zAxDVkHIUP9gtSbzlbv03GYNH_j3AWElGXmlzMHjyRMB_IYbs_h3Ah6oYY6-OsD3tjWlLD0VEbuUMib_ODaKrPiqJ3-JDX4XI5HI-jl_-xCOYMkW0ZkJsWeWlt3SXWW6uP1B5Jmalu7oBR5ARPCxrWFDVHgJfUmjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حمله جمهوری اسلامی به یک کشتی
در تنگه هرمز</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/farahmand_alipour/6281" target="_blank">📅 18:12 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6280">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PHuwTn5Y_C8OA0n_0kHf2nAJ8aWN7m-INxpJFtgbeAT0dTiqFM5eQ-Q-DftVUUH1ocPr412uyuS6YyR_f94HG961TYMGERRcvfxomCsjecBw5dlsObgm22ZAnf6nuc4_CX1QAR0xKaWNbIndqv55rW4QZ148ANbqQFdZ2bpBhHuPnzQ5hnGA3Sl3xg_KiSW6KNe9dLvkIbf7v8h2GsNEemR9lyInRxuxjHR4dX0_sG20E2jn0gPQZlIysET58fHzNVB6KH2dgNwU0ikkTq_hkaV30krvB8haTY67cwuyHNF2yL1kPDRdO2BYxSPpBcOqDMQKH_7qmY0LZa0Jz_0kCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
گزارش‌هایی از حمله به شیراز
هدف: احتمالا صنایع الکترونیک شیراز</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/farahmand_alipour/6280" target="_blank">📅 17:53 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6279">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">این سخنرانی ترامپ در عربستان رو به یاد دارید؟  پارسال، درست در  تاریخ ۲۳ اردیبهشت ۱۴۰۴  که به درستی گفت :« رهبران ایران روی دزدیدن ثروت مردم خود و خونریزی در خارج تمرکز کرده‌اند.»</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/farahmand_alipour/6279" target="_blank">📅 17:27 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6278">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">این سخنرانی ترامپ در عربستان رو به یاد دارید؟
پارسال، درست در  تاریخ ۲۳ اردیبهشت ۱۴۰۴
که به درستی گفت :« رهبران ایران روی دزدیدن ثروت مردم خود و خونریزی در خارج تمرکز کرده‌اند.»</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/farahmand_alipour/6278" target="_blank">📅 17:27 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6277">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jW6P20lMr8nJpURkuUK1xhDe-_tdCJpqmNx_Q_Y-QUbGUpq-pxkYmQpYGXWCu2YzD78qBY6GeC8DtstbN58yCrfU6hngpCKxvfZ-nIkQhXt1txZMvt_XXmPCZZyF9z0K78uUMGYEN8qsMTeLnehLBkQuC2hXJdhQDWRJPsxMVN_NN04HBWvqzFV_iirxU9zItT3OyZErW1ehawRuice1Um8huAXVi8SL4Ps_mMtpENhSaoRvEDb5uAfQ6gCLla8Ps91-1mWqK76bJr5niaiVKNnYhHr8KSCIkQQN91XycdVKur1tN7VVyAkJXzDOfDnKgd4wxWiGks3w4v3kDCnFYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
تروریست‌های حوثی‌ تحت حمایت جمهوری اسلامی یک
«
ممنوعیت
دریانوردی
»
را علیه عربستان سعودی اعلام کرده‌اند.
آن‌ها همچنین فراخوان‌هایی برای بسیج عمومی صادر کردند:
«از همه می‌خواهیم که به بسیج عمومی، فراخوان همگانی برای مسلح شدن و آمادگی کامل برای تمامی سناریوها و تحولات ادامه دهند و جبهه‌ها را با جنگجویان پشتیبانی کنند
هرگونه حماقتی که دشمن بی‌پروا، یعنی سعودی، از طریق تشدید تنشِ همه‌جانبه مرتکب شود، ما با تشدید تنشِ همه‌جانبه و شدید با آن مقابله خواهیم کرد.»</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/farahmand_alipour/6277" target="_blank">📅 16:00 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6276">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3d8904c5eb.mp4?token=deVFL2THDtWqH-JfQPK4PtF9W6bJuKEkb-5WWF9RUIkbAxOP_n5WWNQlKzmaKICm15HdYVWTsilRigbUZoQ73rYh1cFDHE4LsAI0mdxdYE3XUTAXzmy-JTrja87rLkRZ1jvuzNr6Y8d7iuDgcZWPnVedpAnJ-KlHEeO6TFODJCFMbIXCbwdzObQoiBrGMjYe5MPR19eepS_s6SJjiuzkaaHbHSvrny5aF2Dnfg0umoqsIhuxP4m3dGbi7pFy0MiMHrdQQT8hw3Yx_G16s-OtXm-b9nt7I_oF_RGBfpTBdVs_lFPFhaQPxDi4MxBJcBeMpiwy3Bo16cYojX99y_KPbTswv00z2tYH2PfDc5wiNiI6Ry7o1GXfz8h0fnXpKEQQYdEjT56QQ4YdYjWr_NET7NRwqEpGUghj_ru1V6GDsO1zPgkpTqNsFJqhMv4Va-VJW8rl7vEXiZhqTO5cQQtO3OCGd5-cKGBMf62uOZ_ZNH_Va-1SKrKjo-wjW5oHRqL3MYpyibsWuO7dpD0SU-0qItr72Kyz3_nlJMeQWdf0JN7OUht3_dXcrswwpL5HC6Wtx-nUrHN-2Cseogcwl6ky62rFxD6yqNm3XnCb5MANZCeiuynOvH3LpwcH5D3yRsvGqWl7ivHJX7tk87W0SELRThZu9zrl6afoW-KatpJxYJc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3d8904c5eb.mp4?token=deVFL2THDtWqH-JfQPK4PtF9W6bJuKEkb-5WWF9RUIkbAxOP_n5WWNQlKzmaKICm15HdYVWTsilRigbUZoQ73rYh1cFDHE4LsAI0mdxdYE3XUTAXzmy-JTrja87rLkRZ1jvuzNr6Y8d7iuDgcZWPnVedpAnJ-KlHEeO6TFODJCFMbIXCbwdzObQoiBrGMjYe5MPR19eepS_s6SJjiuzkaaHbHSvrny5aF2Dnfg0umoqsIhuxP4m3dGbi7pFy0MiMHrdQQT8hw3Yx_G16s-OtXm-b9nt7I_oF_RGBfpTBdVs_lFPFhaQPxDi4MxBJcBeMpiwy3Bo16cYojX99y_KPbTswv00z2tYH2PfDc5wiNiI6Ry7o1GXfz8h0fnXpKEQQYdEjT56QQ4YdYjWr_NET7NRwqEpGUghj_ru1V6GDsO1zPgkpTqNsFJqhMv4Va-VJW8rl7vEXiZhqTO5cQQtO3OCGd5-cKGBMf62uOZ_ZNH_Va-1SKrKjo-wjW5oHRqL3MYpyibsWuO7dpD0SU-0qItr72Kyz3_nlJMeQWdf0JN7OUht3_dXcrswwpL5HC6Wtx-nUrHN-2Cseogcwl6ky62rFxD6yqNm3XnCb5MANZCeiuynOvH3LpwcH5D3yRsvGqWl7ivHJX7tk87W0SELRThZu9zrl6afoW-KatpJxYJc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مارکو روبیو :« ایران کشور ثروتمندی است.
یکی از دلایلی که امروز ایران در چنین وضعیت نابسامانی قرار دارد این است که هر پولی که این حکومت به دست می‌آور، چه از طریق کاهش تحریم‌ها باشد
و چه از محل فروش نفت، آن را صرف تروریست‌ها در منطقه می‌کند، حزب‌الله و حماس می‌کند…
.
در حالی که باید میلیاردها دلار برای ساختن و توسعه کشور خود و مردم ایران هزینه کنند، اما در عوض آن را صرف حمایت از تروریسم می‌کنند.»</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/farahmand_alipour/6276" target="_blank">📅 13:18 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6275">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">‏
🚨
دقایقی پیش، شنیده شدن صدای انفجارهای مهیب در ⁧ ساوه</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/farahmand_alipour/6275" target="_blank">📅 11:41 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6274">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">🚨
🚨
نورنیوز رسانه شورای عالی امنیت ملی:
شب گذشته تبریز، دشت‌آزادگان، ماهشهر، سربندر، سیریک، بندرعباس، چابهار، جاسک، کنارک، خورموج و خرم‌آبا‌د مورد حمله قرار گرفته‌اند.</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/farahmand_alipour/6274" target="_blank">📅 10:27 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6273">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">وضعیت اسکله بندر رجایی - بندرعباس
بندری که ۷۰٪ صادرات و واردات کشور را بر عهده دارد.</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/farahmand_alipour/6273" target="_blank">📅 10:20 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6272">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">🚨
🚨
فرماندار بوشهر: دقایقی پیش چند نقطه شهر بوشهر مورد اصابت قرار گرفت.</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/farahmand_alipour/6272" target="_blank">📅 10:04 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6271">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">علیرضا پناهیان : اگر بی‌برقی و بی‌آبی را تحمل کنید، اول منطقه را و بعد جهان را آزاد خواهیم کرد.  به زودی نام نویسی برای آزادی جهان آغاز خواهد شد و آب و برق جهان را از ستم صهیونیسم آزاد خواهیم کرد.</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/farahmand_alipour/6271" target="_blank">📅 09:45 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6270">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">علیرضا پناهیان : اگر بی‌برقی و بی‌آبی را تحمل کنید، اول منطقه را و بعد جهان را آزاد خواهیم کرد.
به زودی نام نویسی برای آزادی جهان آغاز خواهد شد و آب و برق جهان را از ستم صهیونیسم آزاد خواهیم کرد.</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/farahmand_alipour/6270" target="_blank">📅 09:26 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6269">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8e62469a72.mp4?token=ZfrUX18ECACEWdXTurFLPoE2JTm3vKsfwSJBHCfT5kONTwh61JSQnzuRVUsT16k7BWg-wXMM1UMmbQDKf5x6JQ6Cye9jrJe0kCabt53j7jmEmwf9Y9RmB3TefIPl5YKhajvJNsBVneEYxHPIK4Ugf6b7vy5IBJS-DDc1UEzn3XveffwIkJGb-LfyOldeG7QjRYWvDu-9-j8nkIRBBFefiED--VsHRLHtvblg5uTPCO7T53DRlt7EEty23blo6LK5G6hGsI-S0JWRimGSrsJ7tvHyeQ2XhpyLXt35Y6XMiKW7jQh0-NiHBMR2v5_NjBYR8sQMVpE681M1WOdfdQYqpw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8e62469a72.mp4?token=ZfrUX18ECACEWdXTurFLPoE2JTm3vKsfwSJBHCfT5kONTwh61JSQnzuRVUsT16k7BWg-wXMM1UMmbQDKf5x6JQ6Cye9jrJe0kCabt53j7jmEmwf9Y9RmB3TefIPl5YKhajvJNsBVneEYxHPIK4Ugf6b7vy5IBJS-DDc1UEzn3XveffwIkJGb-LfyOldeG7QjRYWvDu-9-j8nkIRBBFefiED--VsHRLHtvblg5uTPCO7T53DRlt7EEty23blo6LK5G6hGsI-S0JWRimGSrsJ7tvHyeQ2XhpyLXt35Y6XMiKW7jQh0-NiHBMR2v5_NjBYR8sQMVpE681M1WOdfdQYqpw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
ویدئوی منتسب به حمله و  انفجار مهیب دیشب به تبریز
مدیر کل مدیریت بحران آذربایجان شرقی شب گذشته در مصاحبه با ایرنا از حمله به یک منطقه نظامی در جنوب غرب تبریز خبر داد.
برخی گزارش‌ها اما حکایت از ۳ حمله به اطراف تبریز دارد.
حمله حوالی ساعت ۲:۳۰ بامداد رخ داد.</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/farahmand_alipour/6269" target="_blank">📅 08:46 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6268">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">🚨
کویت : در حال مقابله با حملات پهپادی هستیم.
کویت در چند روز گذشته در صدر اهداف حملات جمهوری اسلامی بوده.
مساحت این کشور کوچک عربی به اندازه «یک دهم» مساحت استان کرمان است.</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/farahmand_alipour/6268" target="_blank">📅 08:37 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6267">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C_G8fO7tnPauIypspXlwB2beVRzuEia0wY3K0g5IXd_AvfEar8teBjYhHGF0yYw4A-mkzFm-XX6Vs-1dHBGg-bMKa5pRi-HSsMBOHeIBMMF1Eou5XrtBPUruqNJTHNQs5PUfhoMqYl-wITlMdrZ9dWAU22QKXsiY-U5rG8udZX6u6uWNTgQvOBrZcflU0UwohHKPJlhbcumNTxmi9seBybu0z9ZORjxsegIq4A4LH10rx6wKtyar4YVjIEKjDdFSESBhIq6hPf7ji86EQzqFrIYvT6Q68Rar6aVgW6RKCa5gY6ZFKa_3qWhkC3h5cednReEHpSRpbKb23c9gD0ElUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
استانداری بوشهر:  بامداد امروز در دو مرحله، دو مکان نظامی در خورموج مورد حمله قرار گرفت.  این حملات باعث قطع برق در مناطقی از این شهرستان شد</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/farahmand_alipour/6267" target="_blank">📅 08:31 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6266">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">🚨
دو زمین‌لرزه ۵.۷ و ۵.۲ ریشتری حوالی کوزران کرمانشاه را لرزاند.</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/farahmand_alipour/6266" target="_blank">📅 08:22 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6265">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">« یه راه خوب اینه که چاه‌های نفت
امارات، عربستان، قطر، بحرین و کویت رو کلا بزنیم» !</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/farahmand_alipour/6265" target="_blank">📅 01:42 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6264">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GiH_o6J9HE6SIgXbcRDNw9sVXKuhENmIl4hNTep1Zoc9CkWHSiOwuzxDnXKxMsIwZ6_wtYQ0f6JvwDnOvvPcGosW0T8cPIz3jjFo69y51CG1njy18jTCkr5qSrGKSQcSGOYqJS-j_jck7zb6ZZHB6doD2rnpucrPscOQdWhH_cfRgARefCrsso4aQPOYMcF64uh2PIpYqPJe5NKaDcWA9sQpW7fWN4--XUPmA4SFnRlwzbhUYy6vY_bU8qicYR7lks2u1PqaDWOk97Ob4HtXZNEP-c2IarZRiljVdEVuZbWKdfBn1fNH0s-fHh2q55pjbOXo-GyBYo8mrfAicvJbVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بیسیمچی مدیا:
الله اکبر - اسپانیا برد :)</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/farahmand_alipour/6264" target="_blank">📅 01:35 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6262">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gu23bwTaEHGZyFy-uftBaY6g04GNRWeh0vEVDqgv67NF-tW6Mip_wm1xIsHFriqNXkoBPI2bYMCyP_fsPskt9NlGmWaioi4_8xRdJHD3h0dsHRvNeOaCnzd1-IEoddculStsujMxzWtffWwqi4Amuo6G0tT0rUuVVp0Wkznt0w_W6LVptUtaVMIEHgWpdN5SWnc07QlY86-X-CCPdNMKeBlbFpJJ0NUydQ-BIQJt90qWzmycnLd9sG2jB2KkhIBwisGOKA2_TkMoyzlsgL-f1_ZDvCBk6ayccRT5j63tf1ZCHzS_YPOvx1LhD3X9BFg0XHztiw60j1FRke1fTaswNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WZAej_ahCDcSHyYaG3dT9REKvv5v6FTu6LXjFWWxlZqb0RRhymLznkXn202WyAN-iwokIH25SPiPGT2KBRiiGLvoV1aZZYO4ptGyNtUV7uMO5SZ6WhlANyf6iN4WPV8hUQ6CZu1vQfO6vqL1m5VwWBAO7PBfLsp-8ytzrOx8j-OvjaLPj4yAEvBKNzOa_83xfWMww_16oOFhE2PqUmwJHkwP72cbtdO3bxGZ2KGKz0G2OgVpbkzLdnjGqaPqQI08eWZP2hf_Kd-mZnq1Bxun5Iv7h51YblFz-7sJ0-3vX8EaJPzcunHb5LQizDllsG9mbxO6tL2IRQt8JSW2REFNaA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">حمل  موتور پهپاد آمریکایی با الاغ</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/farahmand_alipour/6262" target="_blank">📅 00:04 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6261">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">🚨
🚨
🚨
یک نظامی آمریکایی در عراق کشته شد
به‌ گزارش سنتکام :
یک نظامی آمریکایی در شمال عراق دیروز  ۱۸ ژوئیه، هنگام انجام عملیات انفجار کنترل‌شده مهمات منفجرنشده باقی‌مانده از یک پهپاد تهاجمی یک‌طرفه ایرانی که سرنگون شده بود، در جریان عملیات کشته شد.
روز گذشته نیز سنتکام اعلام کرد که در پی حمله ایران در تاریخ ۱۷ ژوئیه،
دو نظامی آمریکایی در اردن کشته شدند و یک نظامی دیگر در وضعیت مفقودی قرار دارد
.
پس از یک عملیات جست‌وجوی گسترده، نیروهای ارتش آمریکا امروز بقایای ناشناس یک فرد را در محل حادثه پیدا کردند. روند بررسی برای تأیید هویت این بقایا همچنان ادامه دارد.</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/farahmand_alipour/6261" target="_blank">📅 23:00 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6260">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kOp0gQRm-TCn97AAlg81x5GQAH1awscSG3u9RTu_bMIXvWm-o9f6fJyp_zLBY29PdbGpZ3YOkdV66BaO2pt9crWhjYwEgyw_OvmRAa9Lz5826obxTFAQDWdSovXVi_Hu1Y-cG82op8YTSarnOz8GLcfJXZSC6ipj5-7cUaIxmY8BjHHqUyTBMQBKUs5EqCeXpipVGDyEIK3tlAcMq2IDVIBM_yGbXzgJCSvWAHqvU-2erTtt0hHKpv7-hxWhpRgf-j9sXbi3QXje5R5aPdlUa3712vRLg6WRh3VhDp6sRvFRHUtd4fKPtQMX8xZxJkvV2BNOo_V5cvZubjmeXZsP4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">https://x.com/farahmandalipur/status/2078890340753568161?s=46</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/farahmand_alipour/6260" target="_blank">📅 20:41 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6259">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TmjfyZBM9o_UGwZ1bm-jgnDuaHNwW1DajcsfhbUz8xagkayUcOUe9h0PI83dnLzj53QToQuA0sho4WzfPO1G0M56uDN0C83DQ3WryjWZrhSnK_s5zpzagGFsz2c01ktxr_ZFQATr4hXtM5vfrIBp76rg7qMKQnHdqx-voqUiXugBixv6wIXxNYYMavH1qUpIh3_3N0571VuVHEeXUCH51DfbY6xqgBst_nvrVQ24MBZAscju5RSloYzElLMAq4f2NCARK5ULx-rLeNlPR5TD03XwJWn5FmPPfvWdanrtMlOVo8rzyVneGv2JwF0lW2xZcHl2rwGvHWG6mAHAZcdOig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رهبر گروه تروریستی حزب‌الله
به وبسایت خامنه‌ای :
خامنه‌ای گفته بود سوریه
ستون خیمه مقاومت است!
امروز نه از خامنه‌ای خبری است،
نه از نصرالله نه از بشار اسد و خیمه‌اش!
ظاهرا ستونش رو برای
بازماندگانشون نگه داشتن :)
یک «هفت اکتبر » راه انداختن و همگی با هم رفتن!</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/farahmand_alipour/6259" target="_blank">📅 20:25 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6258">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z7LEyc_iQ8ZNuq5Jcnf3AiWlOPCqFdZ5mrDTZElUdG5sAWfVfbM9tuUrK1Tdzdo4HcZrSMv5e-kgh1PXJJCHwtNEfqNjA5TGOoKM_XbbPXxN8255qGBlPDORWUrraEcmFFSFLM43fk1VIXo__8X1XesEJ5MLxANXW4b67ZfQ7Ajb4k0jApgyQ3wmwJfTZvMd786-CuApLcLwx5eUa4bygfvmNXX_P4Jokoj_M4UXAAiFPq7U13XF2qcBmtJvKf_jKk2FJ3c0qdffYTjNrIct3CZH1nwpBdDqY7odtwmWH0LqZR_V5vGSigun0GtnG8tnX5zgoCYW7dDHWS4njWM3Xw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خامنه‌ای ۶ اسفند ۱۳۹۷ در دیدار با بشار اسد : «جنابعالی با ایستادگی که از خود نشان دادید به
قهرمان جهان عرب
تبدیل شدید و
مقاومت در منطقه به‌ وسیله شما قدرت و آبروی بیشتری یافت
.» !
قهرمان جهان عرب!
که مقاومت به وسیله او در منطقه قدرت و آبرو یافت! امروز در مسکو به سر میبره و حتی در تشییع جنازه خامنه‌ای هم شرکت نکرد!</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/farahmand_alipour/6258" target="_blank">📅 20:18 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6257">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9a1ebaca90.mp4?token=PLARcptkdPxckALQTjPnTU7Uy6uOZvQGZDVyF4NtY7Hp4e8eXVu-c-SSsdWYjTYvYjmfvIEhm3O57bR_laSrna4dLDdes4VJodQmLVaeOv-sELf6sihDcznTv3wn0ry6mG4348KIStCO4pV-1ktg0dKxNySdjM8ysJgG6QW-9ElmzPvC7d2FLuezeDDLvUrPIRFGM9RQlcLE_dA6WLr-F_G6hydTm287K5ODSd8wHNxQmx5D7TUPz6_Ct87z27lQglUWsOIuJjwgqedzwEiaRWI5pmkYUUNrVYs1hsly1xOrBa5m5JEl-wN3YZzWEjY7tsn2MmSkRHtOemrTHl9wmw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9a1ebaca90.mp4?token=PLARcptkdPxckALQTjPnTU7Uy6uOZvQGZDVyF4NtY7Hp4e8eXVu-c-SSsdWYjTYvYjmfvIEhm3O57bR_laSrna4dLDdes4VJodQmLVaeOv-sELf6sihDcznTv3wn0ry6mG4348KIStCO4pV-1ktg0dKxNySdjM8ysJgG6QW-9ElmzPvC7d2FLuezeDDLvUrPIRFGM9RQlcLE_dA6WLr-F_G6hydTm287K5ODSd8wHNxQmx5D7TUPz6_Ct87z27lQglUWsOIuJjwgqedzwEiaRWI5pmkYUUNrVYs1hsly1xOrBa5m5JEl-wN3YZzWEjY7tsn2MmSkRHtOemrTHl9wmw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
آتش‌سوزی در نیروگاه برق صبیه کویت
مقامات کویتی: در پی حملات مجدد
جمهوری اسلامی، یک نیروگاه برق و آب‌شیرین‌‌کن کویت برای دومین‌بار در ۲ روز گذشته  هدف حمله قرار گرفته است.</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/farahmand_alipour/6257" target="_blank">📅 19:23 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6256">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vgKLi7v2GXu7NXcBLl58b7Sa7LA_AjOqDSRU3DchR4aqcJ9Ab1ois2JpxgWTTp5IOBvnL372Ar0VGDkrt-H-hLTiyp0sJwhjgzGMpCmC2aaRtdbmXmjvzvQRAm84GiQTrFMv0L7F1N0ovs92d5QrN_3J0akBYYf6lXvBFUFAZu1kBijV3wSUOu5t5Mln4LHDfea88JEfUJJE-bTiMjjWCFltRzUAgXlQVXpvO2bcqXsR5WsGqPWYIFW4edhlL9NqRJYIVV2QtUBLHD14HdccdX6bcGauvXK-7UpEc_XpI1AstDXJYbUMKMr1SWDzXhdoTpsi_8ZHQ5dE9qrSYl9qjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
حمله موشکی آمریکا به نقطه‌ای در آبادان</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/farahmand_alipour/6256" target="_blank">📅 19:19 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6255">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ad154543bd.mp4?token=TPs5vhKJgdOwXLUQRs9jznGbfExa3varA14eEHMhsHkvrmJKHvM1uc0XpKbzxiG807a_VkgbhWnyjbjKVxoyNORvr4BHV1mDvviUJ9AI6d0JhZtsebNUryDlObY3Mw7IsaATZW9zTVH4peZca4uwemMcNZJtmDC4tWUfBHnNYZ2q3yitGLXjGmXHDp2peVopJLZ6QBWyjjqw0Kww1MkMYjrMLtf4zYMrBwy5-y0w3_PPQBdskh2tkUBeT5HW-j-HJMGtHQonN1T1uSAuZ1Gxk_gonkcgZhTU135eoMld1aJRcrZFJL2oS9KoQm5xdxlSt2WAidopNO6Loz70OvOI8w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ad154543bd.mp4?token=TPs5vhKJgdOwXLUQRs9jznGbfExa3varA14eEHMhsHkvrmJKHvM1uc0XpKbzxiG807a_VkgbhWnyjbjKVxoyNORvr4BHV1mDvviUJ9AI6d0JhZtsebNUryDlObY3Mw7IsaATZW9zTVH4peZca4uwemMcNZJtmDC4tWUfBHnNYZ2q3yitGLXjGmXHDp2peVopJLZ6QBWyjjqw0Kww1MkMYjrMLtf4zYMrBwy5-y0w3_PPQBdskh2tkUBeT5HW-j-HJMGtHQonN1T1uSAuZ1Gxk_gonkcgZhTU135eoMld1aJRcrZFJL2oS9KoQm5xdxlSt2WAidopNO6Loz70OvOI8w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حمایت مجدد نتانیاهو از آرژانتین.
دولت چپگرای اسپانیا در ماه‌های اخیر تندترین مواضع را نسبت به آمریکا و اسرائیل داشت، در عوض رئیس جمهور آرژانتین
«جمهوری اسلامی را دشمن آرژانتین» خواند
که دو بار در این کشور دست به بمب گذاری زده است (از جمله انفجار آمیا)</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/farahmand_alipour/6255" target="_blank">📅 19:13 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6254">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-poll">
<h4>📊 دوست داری کدوم تیم برنده بشه؟</h4>
<ul>
<li>✓ اسپانیا</li>
<li>✓ آرژانتین</li>
</ul>
</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/farahmand_alipour/6254" target="_blank">📅 19:07 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6253">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/innNTwLURv6rDu-fTCd0KCmaDVC2e79vV2SJK8iE3d8ei5aLwobCInf_eCUCZc5Vz20eO-GysFc4MXRIvKhghBu_4iZ1CZvmj7syMm4forfAs75fVky1wxupnLIaROJk-LF771pIe_nLIChhecdSOEYxAdcWy7NjcFBVyD483W4nOncYYBmy2UaJF6jVdLHMRT73sKuzbI1_VQLBXhDxeNFR1jbB8uZhWtE6ln3uT9FTA_rdaCVMeO_p5YdBYDvaMYUBxEU-1mbdTSeBd4yYjV83pknpNqibHOKStGIviwURrWdMOb7qAlN_wuNUWa0etLm1qOQKsqg0QfXyFK9DrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔺
نتایج دیدارهای آرژانتین و اسپانیا تاکنون،
۶ بار اسپانیا برنده شده و ۶ بار  آرژانتین
و ۲ بار هم مساوی شدند.
🔺
از اونجایی که تیم ایتالیا سااالهاست!
که دیگه توی جام جهانی نیست،
و از اونجایی که نیمی از مردم آرژانتین
ایتالیایی هستند، اغلب ایتالیایی‌ها
علاقمند به پیروزی تیم آرژانتین هستند.
🔺
آرژانتین ۳۰۰ سال، بخشی از اسپانیا بوده،
و زبانش هم‌ اسپانیایی است.
🔺
نام پایتختش (بوینس آیرس) اما از منطقه‌ای در ایتالیاست (جزیره ساردنیا)
🔺
گاه برای شوخی به آرژانتینی‌ها میگن : «ایتالیایی‌هایی هستند که اسپانیایی حرف میزنند»، فرهنگ غذایی، صحبت کردن به دست، تلفظ کلمات و آهنگ زبان و….. متاثر از ایتالیا است
🔺
پیش‌بینی برد اسپانیا ۵۸٪ و آرژانتین ۴۲٪  است.</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/farahmand_alipour/6253" target="_blank">📅 19:02 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6252">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d28653e7d3.mp4?token=r7LkZBavyEC59LXEbFAY3F0pyRfkYsbinxtDLBK93-PSEnPsLkh6fOOZ7-YG2oVRhsc3FRCC9iqyTk4sLLz6Ll_gjw1nT_GzmXOrsBjRBLlvNdRdQlCEYw9_PLXTi76yf2jtIMa-UFGtVlyIUGy62GM27n4ElaTcD35CUbPU1XRemrgrVsw-eIpcc_5DOwS7oaBWPHdc-jzF_15-mfWjSVyS2vIG4FNQvlv7A99BKbSG5S8zIGsQnRSpb0d6MXIckN8PPZKX29otTZCunMYEoIK0gqPXOhaMR4ETqdgq5e_WPHYCSXvbezrXsmEUtYQFApE8PFcC4JM42Zlrnati7pcAkGjWCgJ0IJ_0C_v65WpF5165cdO60-TSWWOhUEOjB9dEXbzunnfnNrDIYAo2Zp-szVWZhLgh9Eu8H0YOf4_2rT-F2vqJUnqYanUjDOJBoZCQD51Km8-QYaxLkB4v9SY98nP3te8pse5EwrgOYlwbz9aDEG6_XtvGFZVkNxQRu_WOsCCFZUn4ZztuMXRXopUhxMurN8VSyEeWw5gZbc4jz1dWl8FIGyIvHDy9bOPvaCcwqt6WHKZGGpRD913nm26IE356pnBNWlYuNMJFfWZUE_EIlwfAtQQcjyEjl0wpCK3dAJQRKd8Gjw2Aj_G0cWN1VynoFuJQbukp6bqwq20" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d28653e7d3.mp4?token=r7LkZBavyEC59LXEbFAY3F0pyRfkYsbinxtDLBK93-PSEnPsLkh6fOOZ7-YG2oVRhsc3FRCC9iqyTk4sLLz6Ll_gjw1nT_GzmXOrsBjRBLlvNdRdQlCEYw9_PLXTi76yf2jtIMa-UFGtVlyIUGy62GM27n4ElaTcD35CUbPU1XRemrgrVsw-eIpcc_5DOwS7oaBWPHdc-jzF_15-mfWjSVyS2vIG4FNQvlv7A99BKbSG5S8zIGsQnRSpb0d6MXIckN8PPZKX29otTZCunMYEoIK0gqPXOhaMR4ETqdgq5e_WPHYCSXvbezrXsmEUtYQFApE8PFcC4JM42Zlrnati7pcAkGjWCgJ0IJ_0C_v65WpF5165cdO60-TSWWOhUEOjB9dEXbzunnfnNrDIYAo2Zp-szVWZhLgh9Eu8H0YOf4_2rT-F2vqJUnqYanUjDOJBoZCQD51Km8-QYaxLkB4v9SY98nP3te8pse5EwrgOYlwbz9aDEG6_XtvGFZVkNxQRu_WOsCCFZUn4ZztuMXRXopUhxMurN8VSyEeWw5gZbc4jz1dWl8FIGyIvHDy9bOPvaCcwqt6WHKZGGpRD913nm26IE356pnBNWlYuNMJFfWZUE_EIlwfAtQQcjyEjl0wpCK3dAJQRKd8Gjw2Aj_G0cWN1VynoFuJQbukp6bqwq20" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عراقچی وزیر خارجه جمهوری اسلامی :
[ در این ۱۳۵ روز ] تاکنون مجتبی خامنه‌ای را ندیده‌ام
!
خیلی مهم بود این پیام را به دنیا بدهیم که سیاست‌های ما تغییر نکرده و تغییر نخواهد کرد.
درست میگه، جمهوری اسلامی هیچ وقت اصلاح نمیشه! نه با انتخابات، نه با اعتراضات و کشته‌های زیاد، نه جنگ.
تا باشه همینه!</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/farahmand_alipour/6252" target="_blank">📅 18:17 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6251">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">موشکه دیگه! میاد میزنه
(سیستم پدافند و دفاعی ج‌ا]
عراقچی از روزهای جنگ ۴۰ روزه میگه که از ترس میرفتن تونل‌ها، جلساتی که در تونل‌ها برگزار می‌شدند.
از اینکه ساعت‌ها در ماشین در حال حرکت بود که جاش رو پیدا نکنن.
از خونه‌های به ظاهرا شخصی که پنهان می‌شوند و…
مجری برنامه هم اسم دو تا از تونل‌ها که فرماندهان اونجا پناه میبردن رو میگه.</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/farahmand_alipour/6251" target="_blank">📅 18:09 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6250">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">ترامپ درباره مشهد درست گفته بود
مشهد برای چند ساعت سقوط کرده بود</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/farahmand_alipour/6250" target="_blank">📅 18:01 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6249">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromحافظه تاریخی</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b5d96f954f.mp4?token=PqMjW8cUdt2VSPvE4uP4NDl0QWLkTerLLOZP8nGj6HrSijQT28i1dgC48lGLLBSiRx9WU2mkDVmKg2BfvgK7-v2Ag9aajoBMYl8OVx2LLe2YIQjkOVRofHAMbfPI8Us8qMLGpC9i04Q9enn8xSF75l8whL_nxQz8tNLNirEZvUqJUi1gEpfCVi4D5iCaktZg7s2uCO9yVeBtY6bbfeGqnCBfXhJxjKPEF6EBiUa-74egNKZhw1SW3S6dgt4eM80wnyhnZ7d01lNwnmzpRkDP6CdvU0s10qaE4Hk4MApN5ArLLLCdHKdTSdcO-6DbYYDF57D4jZKJDp9b116WaK--3g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b5d96f954f.mp4?token=PqMjW8cUdt2VSPvE4uP4NDl0QWLkTerLLOZP8nGj6HrSijQT28i1dgC48lGLLBSiRx9WU2mkDVmKg2BfvgK7-v2Ag9aajoBMYl8OVx2LLe2YIQjkOVRofHAMbfPI8Us8qMLGpC9i04Q9enn8xSF75l8whL_nxQz8tNLNirEZvUqJUi1gEpfCVi4D5iCaktZg7s2uCO9yVeBtY6bbfeGqnCBfXhJxjKPEF6EBiUa-74egNKZhw1SW3S6dgt4eM80wnyhnZ7d01lNwnmzpRkDP6CdvU0s10qaE4Hk4MApN5ArLLLCdHKdTSdcO-6DbYYDF57D4jZKJDp9b116WaK--3g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">علی خامنه‌ای، خرداد ۱۳۸۴:
خیال می‌کردند حکومت اسلامی یعنی خلافت موروثی، مثل بنی‌امیه. یک نفر مستبد با نام خلیفه اما با باطن فرعون. بعد هم که از دنیا می‌رود، یک نفر را جای خود معین می‌کند. در ذهن دنیا حکومت اسلامی این شکل تصویر می‌شد که بزرگترین اهانت به اسلام و حکومت اسلامی بود
@hafezeye_tarikhi</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/farahmand_alipour/6249" target="_blank">📅 17:51 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6248">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3fcb2949cf.mp4?token=d2mZo952KSiSdcGBy20rXe96sMnbvPlbOT8fYxKTRAboNuRC-z7rpbcSuSLFEFGwDt4DMgidr3u0v2JS9mqcpbNmeofpRRWJ_hMBUTSQ55dYrkH7yprVygKveTCog-EI7TJqUZarYXa27vwwe4_-tv4JQx2kOjFTnxG0Z1AIjP0nBVOEkMSQPnVa37MmMU4gNUNZv-CovPbEUCOVjLBdg9umaWJJAW8plWoJiLjAYGtsfHAaef4bGBnAbkaLqORs77lCLylTLUHR4WkCex-UgrMu1iqk3t_vIUOJcmLQZXQODAtP-fJKcsuTaVj6XfYcYJyhSs2XABNP1MmgkhX4BTneh0MBqUX-bYVwt70PRyMOpEGHEM4NVTX7sr8mVTJYYHkmJZp0pzT6OAF0QVhl-NseiqYmMK3EVE5nSxCAC_4hoT6HParaTGRkYXdkYDAQsP4hmmikvA6bnyPkjLPr2Z2oiPiEOUESWU30R-XuSpfQ01_OE2kGxaG9FeSYNrDZF2vlds17aTdSOZ0izlEpAbHB_VKHQGWcNAyZVBm-yhwNhPFwfrN-HKW0div3iHn75IkrTfHJSOKpctYwIpq-pkwEx9pVuhkGLw77whYtFn7pAwsMddslXTT0ZWLNyZqO0LOdrrdHT2i5BZwPR7m7a-ORCaJxT4QGBoGKkcApmU4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3fcb2949cf.mp4?token=d2mZo952KSiSdcGBy20rXe96sMnbvPlbOT8fYxKTRAboNuRC-z7rpbcSuSLFEFGwDt4DMgidr3u0v2JS9mqcpbNmeofpRRWJ_hMBUTSQ55dYrkH7yprVygKveTCog-EI7TJqUZarYXa27vwwe4_-tv4JQx2kOjFTnxG0Z1AIjP0nBVOEkMSQPnVa37MmMU4gNUNZv-CovPbEUCOVjLBdg9umaWJJAW8plWoJiLjAYGtsfHAaef4bGBnAbkaLqORs77lCLylTLUHR4WkCex-UgrMu1iqk3t_vIUOJcmLQZXQODAtP-fJKcsuTaVj6XfYcYJyhSs2XABNP1MmgkhX4BTneh0MBqUX-bYVwt70PRyMOpEGHEM4NVTX7sr8mVTJYYHkmJZp0pzT6OAF0QVhl-NseiqYmMK3EVE5nSxCAC_4hoT6HParaTGRkYXdkYDAQsP4hmmikvA6bnyPkjLPr2Z2oiPiEOUESWU30R-XuSpfQ01_OE2kGxaG9FeSYNrDZF2vlds17aTdSOZ0izlEpAbHB_VKHQGWcNAyZVBm-yhwNhPFwfrN-HKW0div3iHn75IkrTfHJSOKpctYwIpq-pkwEx9pVuhkGLw77whYtFn7pAwsMddslXTT0ZWLNyZqO0LOdrrdHT2i5BZwPR7m7a-ORCaJxT4QGBoGKkcApmU4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سردار غلامعلی رشید ، فرمانده قرارگاه مرکزی خاتم (مسئول اصلی جنگ) که در جنگ ۱۲ روزه به دست اسرائیل کشته شد:
«زمان شاه فضا چنان  پر از خوف و رعب و وحشتی بود که حمل یک سلاح! یک سلاح ، دشوار بود! »
برای «دینامیت» افتادن زندان
و بعدهم آزاد شدن!
توی حکومت اسلامی ولی برای آتش زدن
سطل آشغال و یا داشتن سنگ در دست
حکم اعدام دادن.</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/farahmand_alipour/6248" target="_blank">📅 17:46 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6247">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">🚨
گزارش انفجار در آبادان</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/farahmand_alipour/6247" target="_blank">📅 16:44 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6246">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l3WDMQNmx1CaAniBOEOfOpvrTibD_n6pJDhVn6KwHEwMr85-KIlER6DKWtsM3AoJfxPN3q7cFLVFzR33z7B3nBzHa40Vw5M1Gr1eGns5hN0eSOXSxxvd95PQuhI7RMcKs2Y3-Bsl81WAoJ1P22RWPXG6hH58QM5YTGq2PizDZ9LIkP8w0W1L4O_A218CosHPP7ibG8dmisjk-0j5qc93GZH-af2GgNlJfJl-Ui4WFnC7ZwQafV7AnBaBcms-A_GP2mcm9mOBQv5sbYefCXYCvQ3pg7GSouclFvGKpnKi9SmVHL4qrjh87mp5joYbyGdn96-7X2-sMTkYKf8pq-gyeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
اردن : جمهوری اسلامی با ۴ موشک
بالستیک به بندر عقبه حمله کرد.
۳ موشک رهگیری و منهدم شدند،
یک موشک در یک منطقه‌‌ خالی از سکنه افتاد.
🔺
عقبه تنها «چند متر» با شهر اسرائیلی ایلات فاصله دارد.</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/farahmand_alipour/6246" target="_blank">📅 16:34 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6245">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TXbPIq9eR1_aii09DMXHvmiq3jNo1t2XoipEKglujj60JSDCqacNIggUI6P2sJmyjZuTW6CAFAFtH5Ym_Vz-tpBeEVWYAA0CcYVds8vQFlEj9VsZVqJMrsrfyIXMuWVbDO7vPGvWevxYvlH8TcTstcuIVdfJ1UDM0mbVjaGvJySP4W3cgU56r9Ti2LSiPTvm7z8N0Mm-w4WKhA4CsmvOWQOlIL0cA4QVbSSh_L-72SpKbrG_1vNvFx8T9-z5sFuKpSgfTI31lEMPz3NDNvi3ZhVzn8ldQ9cLcSuFvdSNBJ1pH4J1Muz362-dQ94cyi6hOxS-JoLRlQp024mWQBS4gA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هر روز ماندن جمهوری اسلامی
هزینه برای ایرانه و فرصت برای ارتکاب جنایت</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/farahmand_alipour/6245" target="_blank">📅 16:16 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6244">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">حرف حق :)</div>
<div class="tg-footer">👁️ 30.5K · <a href="https://t.me/farahmand_alipour/6244" target="_blank">📅 10:41 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6243">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WnUk7ble1I6-JR3aRWAp_hkR7i8hX33PZFr7FdtTD9rpuJQW35TRNAlGDs4WKqsek5zsQ2vxGenPTAKyGHF7QXVJdwCIaxeXnRjvYAgle5dMd8_qSUdauRZGlThNKUekaZrHRsD-Kz99b1YE94PqBfjemJgocM4ZB_Lu8EibRi9hcemXJDzMk0dWqXttdEEKKEIWbgVh3p58-WI890I2kpWMkgGZQFXDu8nvVZSz2MAFwCAypnJ4VzysaVsB_HJAZ4rk15W1ZQB9R63IoOXRHtBXvufOB0t3lTeXZ3GZtksl0jhAlg1gRoqu3ELdC3g5aWmUuGk2o2z1hLDUQbyXuw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏خاطرات هاشمی رفسنجانی ۲۰ آبان‌ ۶۰ :
‏«شام را با احمد آقا و آقاى خامنه اى صرف كردم!
تصميم گرفتیم کمتر به كشورهاى خارجى فحاشی و حمله شود
. صداوسيما هم كنترل شود.»
https://x.com/farahmandalipur/status/2078615489446543468?s=46</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/farahmand_alipour/6243" target="_blank">📅 02:31 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6242">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">🚨
چند انفجار در بندر لنگه</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/farahmand_alipour/6242" target="_blank">📅 02:12 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6241">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">🚨
خبرگزاری مهر : شنیده شدن انفجار در کیش</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/farahmand_alipour/6241" target="_blank">📅 02:12 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6240">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">🚨
گزارش انفجار در اهواز</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/farahmand_alipour/6240" target="_blank">📅 02:09 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6239">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">🚨
گزارش حمله به بندرعباس</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/farahmand_alipour/6239" target="_blank">📅 02:01 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6238">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">🚨
گزارش حمله به اطراف سیریک</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/farahmand_alipour/6238" target="_blank">📅 02:00 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6237">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">🚨
🚨
‏
آغاز دور تازه حملات آمریکا در نهمین شب حملات
اطلاعیه سنتکام : «امروز ساعت 6 بعد از ظهر به وقت شرق آمریکا ، ( ۱:۳۰ بامداد به وقت ایران) ، نیروهای آمریکایی حملات هوایی جدیدی را علیه ایران به دستور فرمانده کل قوا آغاز کردند.
این حملات برای کاهش بیشتر توانایی ایران در تهدید کشتیرانی تجاری در تنگه هرمز و
مجازات سریع نیروهای سپاه پاسداران انقلاب اسلامی
که دیشب به نیروهای آمریکایی در اردن حمله کردند، طراحی شده است.»</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/farahmand_alipour/6237" target="_blank">📅 01:57 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6236">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">فرداشب اسپانیا و آرژانتین
در مرحله نهایی جام جهانی
به مصاف هم میرن.
در یکسال اخیر، دولت اسپانیا به یکی
از مهم‌ترین منتقدین اسرائیل
و دولت آرژانتین به یکی از مهم‌ترین مدافعین اسرائیل تبدیل شده‌اند.
نتانیاهو در دیدار با سفیر آرژانتین
گفت که فردا از آرژانتین حمایت خواهیم کرد.</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/farahmand_alipour/6236" target="_blank">📅 01:17 · 28 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
