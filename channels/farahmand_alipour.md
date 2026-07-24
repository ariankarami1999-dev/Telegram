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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-02 17:17:09</div>
<hr>

<div class="tg-post" id="msg-6341">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">سپاه خطاب به مردم منطقه : فورا تا شعاع ۵۰۰ متری از محل‌ حضور آمریکایی‌ها فاصله بگیرید.</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/farahmand_alipour/6341" target="_blank">📅 14:05 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6340">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gqWa70UuXvYgm82q4WeB5gldwDWB5ClQHPmwXBrE9yLirAFDO8IRtphWIuQnI-DJlGJgio9FCHztlSkzIGlwzwDFYTgCTOZktFtBnPJhUSyN0bQXatKmqFJIZ7cHOhW7MJAQBkR86PBrhtq2H2d0HtfqehXRFmrudeDVfLoX0x0Lh_C5m5ACEMTa4Pligf8NTyC6iwKGWkRiBCOMNI1J6wDvvZ7EedzqBR4dpQpZr5ks6Gja87kAQYgyroQJ2NWD2HEcsehKynWin5It9wU7gW9jJRipjlAhzPR1nx7H0gSFvbXFB-FkxpIFXStH49YPNAKP-AbUWCovJ1ScAqaseA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صفحه دوم روزنامه کوریره دلا سرا - ایتالیا
حمله دیروز گروه تروریستی حوثی
به دو کشتی تجاری عربستانی،
حدود ۱۰۰ میلیون دلار خسارت وارد کرد.
ترامپ : هزینه این خسارات‌ها رو از پول‌های
مسدود شده ایران بر میداریم!</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/farahmand_alipour/6340" target="_blank">📅 11:25 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6339">
<div class="tg-post-header">📌 پیام #98</div>
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
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/farahmand_alipour/6339" target="_blank">📅 08:24 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6338">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d4193f544e.mp4?token=IlCvjUfAFBmLg1zWWPt2p7YF1VRmiFKFzrXtog9v7YUcyJG7l939vJSi88DNd3BL_vMZqOMtcTrjApJs5nHrzlzL_Uib85wUPh7iG47x7o7NbvTu6Ai-aMkrkhCnnbMHLrOdSk1ahWgZHQ5Vy1SoJUyJj0QYGgj6IHaGA2yFZxLod2fE6dpfXZKFt_ix0fQZ0CZuhifAk6ve0n9CZSaE5N7HplG4qsC_VQxzCJ-Ah67bxDp0qs4EIi8HROI3ZXUBJ4dag3p6hjLuszd1-TgZURRg5W5__z-TXJjy1_uWeMZsWtA0-2QZzKSUin07GZyTo7Zb9zZp51sCUcAVQwgIWg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d4193f544e.mp4?token=IlCvjUfAFBmLg1zWWPt2p7YF1VRmiFKFzrXtog9v7YUcyJG7l939vJSi88DNd3BL_vMZqOMtcTrjApJs5nHrzlzL_Uib85wUPh7iG47x7o7NbvTu6Ai-aMkrkhCnnbMHLrOdSk1ahWgZHQ5Vy1SoJUyJj0QYGgj6IHaGA2yFZxLod2fE6dpfXZKFt_ix0fQZ0CZuhifAk6ve0n9CZSaE5N7HplG4qsC_VQxzCJ-Ah67bxDp0qs4EIi8HROI3ZXUBJ4dag3p6hjLuszd1-TgZURRg5W5__z-TXJjy1_uWeMZsWtA0-2QZzKSUin07GZyTo7Zb9zZp51sCUcAVQwgIWg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دیشب - انفجارهای پی در پی در بندرعباس</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/farahmand_alipour/6338" target="_blank">📅 08:03 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6337">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZMTx5dkGl32RMhG-1Hg_CtPAzpfVN27SicsOysr20M_aNLCquCTAtN-gFSbLC-onlxVwNmJMrlK0xifEzyk2wsUcaZW0pUF5FTYD0dJeuty-EFwUlZw5PYG9eQ6oyuaCWjKTQ9tOF4xI8uVayMzIWJhXhpZVLc3Zgi0V1mtIuxuGNfkk3n2KFE5zQBIix0FYskm02ZBXZ4FHoogqjFTyyp8KW2riGk3IG3Q6J98oEE0zNPingE_KCVaCHOXuCMLV4YEta8rNetg-zCZ18LGrjZPGH-NrrFfxsBJlvjhpVY46okXIEx12oo17GXcpQYvzP67av4_q4eoNs3lJ5O83Gg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تهدید تازه ترامپ‌: از پولهای بلوکه شده ایران، خسارت کشتی‌های آسیب دیده توسط جمهوری اسلامی را پرداخت میکنیم.</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/farahmand_alipour/6337" target="_blank">📅 08:00 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6334">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0d84604bc5.mp4?token=tNU5uEPzoKYo-rrTKMF01kX7H1CATupCxPqAqeJjAWYQiko8IlcNMalrEX0yuOcyeNsf1RRMzUJu0ecZnTa4mmD_ZYwzONb-VAN-IirexBaCu1yzSQBSiPhScGYvyzGE_rjEmmnoMgewxQNiyDTecxkj_PL-3P26UNhbeqbcpAYhG2DHuc8CJS10lrbfEIpMIYnctv5DnE2VTXUSLKqxdqqyvsgSeilk8lLCW2FZ7MC_lkXJOljtGCwvvBYD8NEuo5M47uDsuTM9AQn1i6NSQjw_ep3r-UN53Lw1SKRRqA1YRFKgcaEGZ5mb7WyCfZRAqEp19v_C2IrHEhIU8WiXcYi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0d84604bc5.mp4?token=tNU5uEPzoKYo-rrTKMF01kX7H1CATupCxPqAqeJjAWYQiko8IlcNMalrEX0yuOcyeNsf1RRMzUJu0ecZnTa4mmD_ZYwzONb-VAN-IirexBaCu1yzSQBSiPhScGYvyzGE_rjEmmnoMgewxQNiyDTecxkj_PL-3P26UNhbeqbcpAYhG2DHuc8CJS10lrbfEIpMIYnctv5DnE2VTXUSLKqxdqqyvsgSeilk8lLCW2FZ7MC_lkXJOljtGCwvvBYD8NEuo5M47uDsuTM9AQn1i6NSQjw_ep3r-UN53Lw1SKRRqA1YRFKgcaEGZ5mb7WyCfZRAqEp19v_C2IrHEhIU8WiXcYi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نصب ماکت آبگرمکن در مرکز تهران</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/farahmand_alipour/6334" target="_blank">📅 22:52 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6333">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">🚨
ترامپ به کانال ۱۲ اسرائیل: در حال بررسی یک حمله گسترده به جمهوری اسلامی هستم؛ حمله‌ای بزرگ‌تر از هر اقدامی که تاکنون انجام شده است. به تصمیم‌گیری درباره آن نزدیک هستم.
او در خصوص احتمال مشارکت اسرائیل هم گفت اگر از آنها بخواهیم ظرف ۲ دقیقه آماده می‌شوند، اما برای آغاز عملیات جدید به هیچ کس نیازی نداریم!</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/farahmand_alipour/6333" target="_blank">📅 21:56 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6332">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">‏هشدار سپاه: هر پایگاهی در بریتانیا که برای انجام حملات علیه ایران مورد استفاده قرار گیرد، یک هدف مشروع خواهد بود.
‏واکنش سخنگوی دولت بریتانیا به هشدار : نیروهای مسلح ما آماده‌اند تا از بریتانیا در برابر هرگونه حمله محافظت کنند.
بریتانیا به‌صورت شبانه‌روزی و در هماهنگی نزدیک با متحدان خود در ناتو، آماده دفاع از خود است.</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/farahmand_alipour/6332" target="_blank">📅 21:24 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6331">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OGDYdVfLT2yjxfrmqpU3DMHcE56lmQ4Mld9YSZbGVAIVUtXMrU8ZVIFHU9d4hVRalJIzgI9QwyDmxKzNbc3uksUYLSZUC3ZFuQB7CNKWcpA-__ZT4CidkjrGi88IY2s-qodYOScUyejpnkGisClSI7MwwXW1tHeAi6hDyoHQM2azpN0uHPKMMlZRbYwePfI35esvvmvEFIpC_jKSy2rb8ezcHOaXSwgRHqzUlF7ZRX44do5uAQ-XGaOU81xnSQscg7rHtmw3qv_VicMLhhiS3Ye5N6lxDd72wv7RgxAUfvFtaJRbmKy1J4FAZxX8p3WAmJMZoCb-SiaBio44sTsFTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ضرغامی : فعلا حرفی از مذاکره نزنید!</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/farahmand_alipour/6331" target="_blank">📅 21:22 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6330">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r5E1UvQisOUYNvRIBdOWx-bY3uG05FRSG-1gr3f2qY3oNGAiiIv2GUsfaCeCUVPwrhKFukgNo_CqWHm42-opva1tFSKkfTeRpdqHECndLHEEMJt-oHbJJpBy4HryLEee007nSj-xlxGShSLG0qTGx2VmvD2AHuB1RmL-015pVBw66W_pGkLz-eEBBhqWrEMoGU9SOGrKhWRzl_AFtOvQjI5DuRRQOMMgKAzSSSPO4PWulAJR6DuKHFfwtvJZz-sioJ17H7-CeiTyznVfOEOn-eDON1cY1BbsZ2XtNzV5iu9yFSunEu6Itqj_4Z5UUIOnBzCruoQFdUnNuFCxtN-s1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دو حقیقت محض
۱- تروریست‌های حوثی به تحریک جمهوری اسلامی وارد این جنگ شدند و به کشتی‌های عربستانی حمله کردند،
پس مسئولش جمهوری اسلامی است.
۲- حوثی‌ها ارزشی برای جنگیدن ندارن!
اینه که ترامپ مستقیم میگه فاکتور هزینه
حملات حوثی‌ها رو شما باید بدید!
و این یعنی بازهم ایران باید هزینه سیاست‌های جمهوری اسلامی و نیروهای تحت حمایتش رو پرداخت کنه.</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/farahmand_alipour/6330" target="_blank">📅 18:37 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6329">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/InUHe-PMLaDx2K9scrvuaCEE5PMmtEv8j37YKAZSFPQeYLWt5YaapkpmI37vouvGii24xDzgum4OdblYGtxXTrlyaLSj43f92Gty6MJln0MGdUxbl5IuZHZ-55D4-C4ZWxwsOu5gjXAoi9bgOp2ekfoGhslblobMxPPOplyoD3PDUfcwUbiELl6XSFaXyWUylQF32ZfInLOY8kc8cBPOQetViZ1avsB6gkpL4WwI_WFBGYsINNYt8gkxhMLZdHSyixDvYj-fmHwes7mJ-0aKPfCDkcc5OxKC5-6PxfGhzj1CVxuSCV4r_dGWSBANrPwcUrmvwCMoEdLRm2fNoSBBgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قاآنی، فرمانده سپاه قدس، با ارسال پیام تبریکی به «خلیل الحلیه» نوشت: «آنان با انتخاب شخصیتی که نماد مقاومت و شهادت است، بار دیگر اثبات کردند که همچنان بر استمرار مسیر مقاومت اسلامی تأکید دارند. مقاومت اسلامی امروز قوی‌تر از همیشه، مسیر عزت‌مندانه خود را ادامه…</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/farahmand_alipour/6329" target="_blank">📅 18:07 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6328">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IpDfhuwUVA7D_vukw--punel5VYWFSWuPlGiBExSYEj--tTFv4eUzPBUX0LQiX_fcPh8G6V9z2nEac9WJzaC-FmE6hFPbLv43Yiz958Qjro4DN7VGFAjTLJh_m8JyODFYYmxAs7Ndio3phyQMKwfIaVFo0lPOpakaRQHWbniwzOfmhex0vrgFyLGvu78C3MAiXupDtA3e6yVXnIQBemQInE5mcqzH3YzNUVZD_CDhL8rHsNCw5YvKr_1CHbf5ul3PDzMktrqT8yKnXB1auS38vTfuLTb8DhGMTPAl9U3pCZCAGfh6NTHF8O5OxL_cAKFcZvZo6m3fU6jmjZQZDl0qw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/farahmand_alipour/6328" target="_blank">📅 14:57 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6327">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jfKoV0gTyaCZcUulO6eoMt__181eK1aDzHb7BK9cGQS99Dg907jlT9LXBT2HG0ku32WOusIa_Pj6dOzPabVq0SfCCFquY8ER9KrYh324K6YBX5lYyOKj1HW1lWw_7FEn0AMO4JDzgK7cl5GEUfqMbOGfeVT950G2Psl81WBmNQKy46XVCzBREiCoZfDQ6MmCBPATf_YeGfNcCo6ZvsTK47L9NQG_udQkI37tJ58L1Dk1963XZFgpe1B43bixT7i3WLbQ3efeJBeJlNkR4GhgNJoudo35qIxr7QOSJTo3tdK_D9i6QF-1ZxU09Fig_NlegPDytC2Gz2ULTFlUicMwrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/farahmand_alipour/6327" target="_blank">📅 13:46 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6326">
<div class="tg-post-header">📌 پیام #87</div>
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
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/farahmand_alipour/6326" target="_blank">📅 13:36 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6325">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z5e6gqbtaiqMLDiAyunn8kGz9PU50p1SfNlg_8YwUXnAziW7g5Lp7WuEV5a9co26Z1tjMHKfOd-jvlLsX8k-g9ROoEIsGtRNc8Lf83BK5pGAMM5BjkAYVVc56kJcvr6IuD5E8uZuuhLcs32NzfDixg3y5JIWR4Wa_dsb817afol8ynVHpT446yvtiN5t3dmmIpcgmITUX8IlNT7DC3coSXOIowRxQ6s5-Z6deNba7QHPuacfbzo5xMwFImI4EegyokZOGZs4S7x5pZK9_0PgJ33_0M3hNeKd44zIQrwHj0SqAvil4VCQxf2oNAvbm3b-c2hApfwDttlBIIRhs4SVxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارتش: مراکز و یگان‌های آمریکا در پایگاه‌های الدوحه، علی السالم و عریفجان کویت را هدف قرار دادیم.</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/farahmand_alipour/6325" target="_blank">📅 08:58 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6324">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bTHIgkHMBtosxPvZiC3SVLcM4JjB-s1SDYb-XL-Ut7EOn7x75dLWeHsHWUiGWxgqIoJZMiuAbduDLB1Q2J985B2rW8Mdk-vNnCPkRGMBU8jZDKPeLPvKCqYs9qHetJNk9rJXT42fqdTTsZrhVyu_wadx2ZjeLwGxzXVxP5EVVOU2UbWvCnRwJTjNKaDhuGdRRrH7hjLv37_aZBIT7ipigvoYTU9BOoOJA1-K1Bd_fuFDItzT8RkC3kazTAZrQpsMtZrSA7YjU7huf9dSGPJvhn0373xlQtfz3NDETvkfeHGVkTTGxPC9bD_t1zg3m4vSNZkUZyNUxh1aG9gL88yrmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در یک تحول تازه در حملات‌ ۱۲ روز اخیر
و نشانه اینکه حملات وارد فاز تازه‌ای شده.
«بی‌ ۱» برای حملات بسیار سنگین و عمیق
استفاده میشه.</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/farahmand_alipour/6324" target="_blank">📅 08:48 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6323">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">ارتش: مراکز و یگان‌های آمریکا در پایگاه‌های الدوحه، علی السالم و عریفجان کویت را هدف قرار دادیم.</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/farahmand_alipour/6323" target="_blank">📅 08:41 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6322">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">جنایتی نبوده که جمهوری اسلامی
در حق مردم ایران انجام نداده باشه</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/farahmand_alipour/6322" target="_blank">📅 07:56 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6321">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/08ac20eb0b.mp4?token=gGGVbbEvzN4yZ6-GZFt9kQDNQXDIB7Bq1WirrN5rUwjox8-PDLuRVgE9-siQSuVwMkGpLt54lIV3P-P7DImjC0br4MVhSrToD6WtFjyXyykp0QE2i4RlLqD6nojt7moaek-mDZfUkdNcbdFv6CrUI4dLkbHK-7jELDRKGj32OjZTxNZYpKrdDqDfH12DiIEhpkilTcPaaic69BT94JOmACO3qtCCEbyXtImrDalzrpVGzJ9NKvbo7glQAYNgwS5uMQJf-F2chy_gYD28yW2kbkMW9pycso01gg-nFZY82-b1vHcYZZDhMr-DB4x9spVg0EpjhCELWxnlxMVIt65ZSk0Y-B4u_LhARpXNl1Jv28qTRO_E1PKWr1ZNYeVxpUAwScdTnXrJbOWWYsOXvWijl383sbfiYdGpNsbX6zw0U796jkY9uPDbuNKSG7Qf3olKBQRws0eXePUfmAbxs85nA-zM8SriVisScngKNGmXIoDzci7JWE3_tEyPe90Dj8OuLI5Oouf-fx8srJQQ08_bgJzogmiplfZ8jiheXs6Ep5AMzCsUNW3h8RZh5aX7KoK4SA6oKCf11EjI8cc9msUp7qH51XkOY9LIabi7lpifjjWUZf9-CTpglR-MrWeW5a9ZA0_eiNcrZICvSSTrDb2F1hhUqU9rUDt3Ps_-nMBeYUQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/08ac20eb0b.mp4?token=gGGVbbEvzN4yZ6-GZFt9kQDNQXDIB7Bq1WirrN5rUwjox8-PDLuRVgE9-siQSuVwMkGpLt54lIV3P-P7DImjC0br4MVhSrToD6WtFjyXyykp0QE2i4RlLqD6nojt7moaek-mDZfUkdNcbdFv6CrUI4dLkbHK-7jELDRKGj32OjZTxNZYpKrdDqDfH12DiIEhpkilTcPaaic69BT94JOmACO3qtCCEbyXtImrDalzrpVGzJ9NKvbo7glQAYNgwS5uMQJf-F2chy_gYD28yW2kbkMW9pycso01gg-nFZY82-b1vHcYZZDhMr-DB4x9spVg0EpjhCELWxnlxMVIt65ZSk0Y-B4u_LhARpXNl1Jv28qTRO_E1PKWr1ZNYeVxpUAwScdTnXrJbOWWYsOXvWijl383sbfiYdGpNsbX6zw0U796jkY9uPDbuNKSG7Qf3olKBQRws0eXePUfmAbxs85nA-zM8SriVisScngKNGmXIoDzci7JWE3_tEyPe90Dj8OuLI5Oouf-fx8srJQQ08_bgJzogmiplfZ8jiheXs6Ep5AMzCsUNW3h8RZh5aX7KoK4SA6oKCf11EjI8cc9msUp7qH51XkOY9LIabi7lpifjjWUZf9-CTpglR-MrWeW5a9ZA0_eiNcrZICvSSTrDb2F1hhUqU9rUDt3Ps_-nMBeYUQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">- رئیس جمهور سلام میرسونه و تشکر میکنه
- باشه</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/farahmand_alipour/6321" target="_blank">📅 07:00 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6320">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">🚨
در جریان حمله آمریکا به مرز شلمچه ۲ نفر کشته و ۱۱ تن زخمی شدند.</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/farahmand_alipour/6320" target="_blank">📅 06:57 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6319">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">مارکو روبیو وزیر خارجه آمریکا : جمهوری  اسلامی تفاهم نامه را نقض کرده و لذا دیگر  معتبر نیست.</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/farahmand_alipour/6319" target="_blank">📅 06:56 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6318">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/65da400742.mp4?token=kVIyCjlttJ5zwzUTLw_y0_gpcqeb2JKSrT0vUAn3Qq_b8laDyyBekUcuTx5XUWwBpmZtrvQs4dOXDEktyDQRIoI_zm0xxEjUMNhE93PDxWv7em1KBfzjnJ3K4hH9RqQImaIgSvHB727b5HWPu0M1eXEAiyWHOCPxqvNK5nJcbBzu1gW8b9mIySgsasejPm75XCn48dB0rjrnc7QxpVEBPAuvXPqMTMxrX0IkQGDGUOGuLJ2kzc4Bbp7Of9F9ybroonU_cz9D7nalFB1KuIBSEgjaHDLAihb2ut8px8C9lMABSMR41b416dOXUQzWCjE7dw2wgIUtRKOWNY63IG0H7w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/65da400742.mp4?token=kVIyCjlttJ5zwzUTLw_y0_gpcqeb2JKSrT0vUAn3Qq_b8laDyyBekUcuTx5XUWwBpmZtrvQs4dOXDEktyDQRIoI_zm0xxEjUMNhE93PDxWv7em1KBfzjnJ3K4hH9RqQImaIgSvHB727b5HWPu0M1eXEAiyWHOCPxqvNK5nJcbBzu1gW8b9mIySgsasejPm75XCn48dB0rjrnc7QxpVEBPAuvXPqMTMxrX0IkQGDGUOGuLJ2kzc4Bbp7Of9F9ybroonU_cz9D7nalFB1KuIBSEgjaHDLAihb2ut8px8C9lMABSMR41b416dOXUQzWCjE7dw2wgIUtRKOWNY63IG0H7w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اون بابایی که با نخوت …</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/farahmand_alipour/6318" target="_blank">📅 22:41 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6317">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d716a2e5bd.mp4?token=t-iLWePhESkLrxXqQiPfcAYeNYsh5QE8zXxwBYWtfApjSzcCSRHwjbHFZhRQVtwykJ7Ml0RMB4yvUkSH8WxNIORokDv4kdC29P0b-cGh_gwigY6geCIZsAHYZ06zy-vdHPlIppept9yUW2FnPvipDTmeY5mGn8oVTolfilTlxEhsE5cZB-zFST-8zDuj7U5aCztK3Vl0RuQ3TofNYjUPXKIPLw6E3kKA7GMtuZ55a8jyXS8yamkoNvk2n5EsqA0Ihs0cETXyla0T6SLuR2BzLpFrHsOS65mX84nvgzpkDz3a00OltxyqGkB5380U3ps4PZftv_2q_PXwtAvr_D7JIqbtaCNSfp_EtS04oiDL11ZF688IAa4ok-9aFMgNfd4D5A5KIelbD9D8qJNW_rKC1arez9Ur9F3oleuOykBZhQ7yVBLZFZeRt8ruICGTBV3uIGIJ5v9Nkrm6_kmmVK4z_sNrosl6vhGQpuV-G6yf9XFLj7MFSr01OiRYeHf-9Z5WlwrPu1OQ3S05mUzf06mzrx-Ek-vihO4Cg28D6n0Qg29K5uLnrMM8oEc3TwOMbTmHr7uxli94Kx7wiCC0SoGtCMCGYcLEgNwvRPkjUnIWCIOdT2XS8IUxbnYxNgeieb8MN8uN-YmMuOHqUVDMDX_6xR9ZEA1bqBX1R_-PsBZVNZI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d716a2e5bd.mp4?token=t-iLWePhESkLrxXqQiPfcAYeNYsh5QE8zXxwBYWtfApjSzcCSRHwjbHFZhRQVtwykJ7Ml0RMB4yvUkSH8WxNIORokDv4kdC29P0b-cGh_gwigY6geCIZsAHYZ06zy-vdHPlIppept9yUW2FnPvipDTmeY5mGn8oVTolfilTlxEhsE5cZB-zFST-8zDuj7U5aCztK3Vl0RuQ3TofNYjUPXKIPLw6E3kKA7GMtuZ55a8jyXS8yamkoNvk2n5EsqA0Ihs0cETXyla0T6SLuR2BzLpFrHsOS65mX84nvgzpkDz3a00OltxyqGkB5380U3ps4PZftv_2q_PXwtAvr_D7JIqbtaCNSfp_EtS04oiDL11ZF688IAa4ok-9aFMgNfd4D5A5KIelbD9D8qJNW_rKC1arez9Ur9F3oleuOykBZhQ7yVBLZFZeRt8ruICGTBV3uIGIJ5v9Nkrm6_kmmVK4z_sNrosl6vhGQpuV-G6yf9XFLj7MFSr01OiRYeHf-9Z5WlwrPu1OQ3S05mUzf06mzrx-Ek-vihO4Cg28D6n0Qg29K5uLnrMM8oEc3TwOMbTmHr7uxli94Kx7wiCC0SoGtCMCGYcLEgNwvRPkjUnIWCIOdT2XS8IUxbnYxNgeieb8MN8uN-YmMuOHqUVDMDX_6xR9ZEA1bqBX1R_-PsBZVNZI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حسن روحانی ۱۳۹۷
تا آخر هم افتخار میکنیم به نفوذ
در عراق و سوریه و لبنان و…..</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/farahmand_alipour/6317" target="_blank">📅 22:30 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6316">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N4a337Nna_jZDuOKi4egjSXXJIVq_CrfBO5RCg2pF9QGkckV_2kjT8jQljAOclepGU0SeYHnXRJql68tQoZvtGO4EQrOUWL6pk0MsndkS8YjLdzbxpItb6wVXds8yEkQJEaks51AYmDo7urvNNb8gBTf0gIvJjCMZV057WFbUTDvjzlop4z3uYviQP1gj5Bbx4PEhwFzPmcG0iIBKI66P4157cbpGAcl06KPcOk3nElT5hCIEivnJcxFwfRr5cu6cIi2AullN772deWxDe1Vr6D2791GMfbADmfiMWb1M4MN0P6xlMLORUKhIkdarqhjSY81Y2BN2PoRXHm7_oy1MA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏سخنگوی سپاه خطاب به شرکت‌های کشتیرانی‌:
مسیر مین‌گذاری‌شدۀ جنوب تنگۀ هرمز  [ آب‌های عمان] مسیر نابودی سرمایه ی شماست!
قرارگاه خاتم هم دقایقی پیش هشدار داده بود که فقط از آب‌های تعیین شده (بخش ایران) باید تردد کنند.
جمهوری اسلامی رسما آب‌های سرزمینی عمان رو هم ناامن کرده.</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/farahmand_alipour/6316" target="_blank">📅 22:22 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6315">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">🚨
قرارگاه خاتم :
تنگه هرمز همچنان بسته است و اگر قرار هم باشد شناوری از آن تنگه عبور کند صرفا باید از مسیر تعیین شده [از سمت آب های سرزمینی ایران و نه عمان] و برابر ترتیبات اعلام شده قبلی تردد نماید.
‏
🔺
در صورت عملی شدن تهدیدهای آمریکا، نیروهای مسلح جمهوری اسلامی ایران اجازه صادرات یک قطره نفت را هم نخواهند داد و زیر ساخت های نفت، گاز، برق و اقتصادی منطقه مورد هدف قرار خواهند گرفت.</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/farahmand_alipour/6315" target="_blank">📅 22:16 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6314">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uDRwHjN_gMj29kL9TYBJA31bA1WkPFuXYOLsdG5u3w3DQNbcDHisHeHVIwbL7dw5EnV9hSZB4pCdtvqgDr72-H99BlTY05yaf-t5rkIT0x-cZ-sFQ1qeWUGsNaYPjpRaKu53obq1e4AUkszycbrcz8FDSb9pr_iX6i6paOnZTXNW0XjtSyHMxjuVkBDoO6fcGm-Ostsnem24syuluqRlFGzL8nfJ3DZuMUvEGwkDFCvih0vzJtphuoqCPzYIqyjGj_FrblkAE1iQ12RSVhxTA-K-ba3LFCyqb60fXaO819IySeyH511EnSNQi3Sq_u8pIX8Dr1ztUgsO_B1SFJATZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
تهدید ترامپ: کشتی بزنید نیروگاه میزنم.</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/farahmand_alipour/6314" target="_blank">📅 18:06 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6313">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bANrRZW_N_qnYAWDmcx9Rb74o09Or992Q1v6kncA56CJzHz3d1ehAaRfcY-l9zXh1Ouy1ezkkEDwCkHjBGUkoMcZZpzqij_KY3DybglahjLjLC28Trz0p_s-OHoc-gsPOaSiBMazowawLtOdLKHv99-eZuwQ7Elsm8DPyMue7yEDt_oZ0bUv56-Ing4SALEosp_pIb6EV7DTXDDZDpIeMi5lCVaragOu_FAsmvUXyqxdvXSN8DHVjj1vM6rI5SFHfUsnvPpb5BYtDlQDPEn56PKY1m2FPzUQ52I4XyRkti0QnTipQUy4W5kNMjj1Tu2TzJHu9g0TGExB7RK1IG6M3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
تهدید ترامپ: کشتی بزنید نیروگاه میزنم.</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/farahmand_alipour/6313" target="_blank">📅 17:20 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6312">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">🚨
شب گذشته صدای انفجار و پدافند هوایی در ۱۹ نقطه کشور
تهران،  بهبهان، امیدیه،  ماهشهر، سیریک، بندرعباس، بوشهر، چابهار، کنارک، تبریز ، بانه، کبودرآهنگ،  همدان، خرمدره، ابهر، زنجان، دینارکوه،  چوار، آبدانان و انارک.</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/farahmand_alipour/6312" target="_blank">📅 08:32 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6311">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9577aecbb9.mp4?token=UEgJCLceEhgypfFUX8ky1jaThx-c6cLtnNgAzLUua_DDsaNsZ6OF1DgxgQp2kglkBEiwWwiuG16g_iO-j1tt6r9pSYbVT8Yoscy31pZ1HsbmzljlcsChznEg39Mg8E_kuX3656cZMGuXq1epQ7y-fM00E_fzTHB9e4fbqfuLTIKt5m8xFtaekOOCPyWckth3LjZfEpu_xrl0NxVGQm-A2538ncQrN_DuXXqJNzlc2bDUfn_vBuobzJJ50_j4pJF5ghBuGNW0bN0flcTxqJlc199ZaocZVQDwJ_m-s-I2XniIK6z754-J5ShJyXoKclVopZYrBF36C6GxFjvXU_KO0g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9577aecbb9.mp4?token=UEgJCLceEhgypfFUX8ky1jaThx-c6cLtnNgAzLUua_DDsaNsZ6OF1DgxgQp2kglkBEiwWwiuG16g_iO-j1tt6r9pSYbVT8Yoscy31pZ1HsbmzljlcsChznEg39Mg8E_kuX3656cZMGuXq1epQ7y-fM00E_fzTHB9e4fbqfuLTIKt5m8xFtaekOOCPyWckth3LjZfEpu_xrl0NxVGQm-A2538ncQrN_DuXXqJNzlc2bDUfn_vBuobzJJ50_j4pJF5ghBuGNW0bN0flcTxqJlc199ZaocZVQDwJ_m-s-I2XniIK6z754-J5ShJyXoKclVopZYrBF36C6GxFjvXU_KO0g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هگزت وزیر جنگ آمریکا از ضرورت
برخورد با جمهوری اسلامی میگه
ونس، وزیر خارجه با ناراحتی به او نگاه میکنه.
(ونس طرفدار گفتگو است)</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/farahmand_alipour/6311" target="_blank">📅 08:28 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6310">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Psw7WgB4c1ZHGNeZq92VZrYh5Q24c9xM4X2fQ36AHVlzDAEMjThcXB9i2U6MYdPufAg9eHB4YWWwaC8AhIZnPGu12u-OcIgxcUXTJRpqLWyts8-34Hkmah8lexaTZIbxR0ZozUpTM4lt57z1yqnHr-b3-uqE2BInfAhDJGYbpIeYqpo1RIb6qaTqTPXn2J8KqgrrNT3ySMEn-aXNCRzZroI-ODKkkG7pprbCdKgi8_uPatm9182Xvx7R54lHrjMbcrwoR8hGTGml_JaYaRkQuT7PwkeNs5O6n5YGgIbUnEEgUOvzmZUer2CKLzyCLsMKhbId_nDRSNUZTGeRQnZ3WQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
اندی برنهام نخست وزیر تازه بریتانیا که از دیروز در این کشور قدرت گرفت، با در اختیار گذاشتن پایگاه‌های بریتانیا به آمریکا برای حمله به جمهوری اسلامی موافقت کرد.
پایگاه‌های «دیه‌گو گارسیا » و «قبرس» از مهم‌ترین پایگاه‌های بریتانیا و مشرف به ایران است.</div>
<div class="tg-footer">👁️ 30.1K · <a href="https://t.me/farahmand_alipour/6310" target="_blank">📅 00:52 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6308">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bBITnzUSSPDQYRN9PUuSyQTIIs2NjT3t5OulqIc89tTduzHwezRc5Erjn0IRkleH67_zz0V1vgIsqSktzGrJZvtrpY_cuUBFV7PDDebGrDoPpqnnwXLXPQGN9vKJXLcSR9BAXQexkQc4cSFBuRKmKS8nHJPcMbWa1zgVv-zn6rPi240-DIglWA65T_b5zgyMoqb8O5rk2w8KSq9dF2hncY-Z50yKSbntOsG1PDmRbyQzuszyuPfPrNEuNW1ZsBIoK5Qt-eN9dUOjGy7CPRCUidzvcj-ZH8Lwxk0Zs8SXsFnbhNlMUf6w31vHJQjssGU9MlEEP2pZS8YxMLuSnQ6qVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DlgOa8NhZzBmnkNX5rUwD-gk6DCDBqQvqWCUUWikz4bUYEfF5ovexX_0T9FXtCLcokEQTVHUhJPK5IGS2effa7EcOdzN5Tk6V7otbJLMeVQaWudUwdBMjSgaEP5uWm7LrYk9it1sCpNaRvBbS_duAkIFBCFvVqBXB_bICod6GIKq3s4Za-d2jLdTHeFdJcYGTDFeprD_Q32P30cX2kjZOlmVch7ccvTR2fqiasA1OFWxN3zCiA9yYEtdBllwNgRJ2rnS9DXwG05u1SpLUy5d3CZfXQD6xEWmsZENOwd9Hx1jIVsulzcP1w_rC4LJ1zkGpSyq14R4T6ZyC9LQ_WQD2g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">حسن روحانی رفته خونه لاریجانی تسلیت
چهره زنان رو!
بعد همین ها میگن اگه ما نبودیم داعش می‌اومد توی ایران
داعش ۴۷ ساله که در ایران حکومت میکنه.</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/farahmand_alipour/6308" target="_blank">📅 23:28 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6307">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">🚨
🚨
گزارش کانال ۱۴ اسرائیل :
جمهوری اسلامی به سفارت اسرائیل در بحرین حمله کرد.</div>
<div class="tg-footer">👁️ 30.1K · <a href="https://t.me/farahmand_alipour/6307" target="_blank">📅 22:01 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6306">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QpjLijjgFA9YKU-3hGE7-F2gLv1LtNbJsWi2hcxpoCka3wJ2ip2e1PR3ae1oVOScgLgExUMVR2Kf0bzLKt4wBVOmGJnQPE0BDw_cz9Jx9xoXKTK56WugXsIoNvMrz4Yk-tADHtCG_lx34i_tc8sE2wfk3dBzbjSsv3dnsEHhS-Zu6b1SXkndHQbkCoFwIsRkXtUZWCpi7m8Cbg_D2FcidNbOTVsSOMFT_zOjusmA5EHpEX1vYON7PKZqLjc_yU3j12mmUIySzzDmZhEwFsHJ_cL1I4yG5oRGQthUwh-RUb7FjqiQvg4PMIYOb4SGmqpnPuudbyWIxnPIbPA-mksF3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">موقعیت کوه کلنگ، در نزدیک تاسیسات هسته‌ای نظنز، گفته می‌شود تونل‌های بسیار گسترده و وسیعی از چند سال پیش زیر لایه‌ای ۱۴۰ متری
از سنگهای سخت ساخته شده است
و پس از جنگ ۱۲ روزه،
هزاران سانتریفیوژ به این تونل‌ها منتقل شده.
گفته می‌شود اورانیوم غنی شده ۶۰ درصدی ج‌ا
در زیر این کوه پنهان شده است.
بازرسان آژانس بین‌المللی انرژی اتمی هرگز موفق به بازدید از این مکان نشده‌اند.</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/farahmand_alipour/6306" target="_blank">📅 19:28 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6305">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3814b8c91f.mp4?token=kTPWyVmb7K8nTPKonIR1rABYO7wkQbwi1wr-hZy62ryxQCBmVh-zMbQHj8bhIwKeaes2jDkAUeMnx5yTJwsjjqY2Y9d-TdPokX2_WRcYlaDc8XdbYYk1ufsr_E0F882MTrZJh1dMAKGUAir_B7d3K0Z7bPbZPPXd1Bnf6ROV6KLcCKu7-qBFqqiBFaLvG30DMnHB8mkGyDGxqoxhaH2cMPwY3xnnbxSO2nUrx41RSQbHRN9_RAScDDTtzDms7w0SoQjqW17wCrBvoQwCRZJIzSDdIogZ9CRoCvxJAprzJAeszLVrqnhsZW48lQ-BAeJfvoKtkU5dVusEwXc6CkkH9TzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3814b8c91f.mp4?token=kTPWyVmb7K8nTPKonIR1rABYO7wkQbwi1wr-hZy62ryxQCBmVh-zMbQHj8bhIwKeaes2jDkAUeMnx5yTJwsjjqY2Y9d-TdPokX2_WRcYlaDc8XdbYYk1ufsr_E0F882MTrZJh1dMAKGUAir_B7d3K0Z7bPbZPPXd1Bnf6ROV6KLcCKu7-qBFqqiBFaLvG30DMnHB8mkGyDGxqoxhaH2cMPwY3xnnbxSO2nUrx41RSQbHRN9_RAScDDTtzDms7w0SoQjqW17wCrBvoQwCRZJIzSDdIogZ9CRoCvxJAprzJAeszLVrqnhsZW48lQ-BAeJfvoKtkU5dVusEwXc6CkkH9TzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏
🚨
🚨
ترامپ: قطعا به زودی و با شدت زیاد به کوه کلنگ  در ایران حمله خواهیم کرد و هیچ کاری از دستشان برنمی‌آید.
‏ترامپ در دیدار با رئیس جمهور لبنان گفت: «ما قطعاً به سایت جدیدی که آنها در مورد آن صحبت می‌کنند (کوه کلنگ ) حمله خواهیم کرد.
آنها به دلیل سلاح‌های هسته‌ای در این وضعیت هستند و سعی در بازسازی یک سایت هسته‌ای دارند.
‏ما به آن سایت ضربه خواهیم زد. هر سایتی را که آنها حتی به سلاح‌های هسته‌ای فکر کنند، با قدرت بسیار بسیار زیادی خواهیم زد.
تا الان زیادی باهاشون راه اومدیم!»</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/farahmand_alipour/6305" target="_blank">📅 19:17 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6304">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/acc280d27d.mp4?token=dH1UE_wj7Fs1dYrz961x9plLFJnx5p6PuQuSOiO7o5JADZpGXJ46qpf__9wyDMPeA7vWz91tTYETKCnPRktcF6fM3XWmLNQdY3tBVCLrj7Qb1fiqOPP-VyhGPblhEtte8EJJwcczszlNZwLJ80PwsKriGe07cRzDs48uco-E3hAwUp711hPgm6LwVIxVSA6Un9k3ATmCwBry1_LXJWsnjNr4Ui0Yv4_xppvPglndHpWNMsyOt2hoWQN8Ru8J4yicyKsd8hnmuJtF2A8c7DyyQIGIktrMW1MDqPVLosiUFu2GgZgM-jWzIKV4xSrvMa4f6liIJqJ-tQk73ma_d92ySw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/acc280d27d.mp4?token=dH1UE_wj7Fs1dYrz961x9plLFJnx5p6PuQuSOiO7o5JADZpGXJ46qpf__9wyDMPeA7vWz91tTYETKCnPRktcF6fM3XWmLNQdY3tBVCLrj7Qb1fiqOPP-VyhGPblhEtte8EJJwcczszlNZwLJ80PwsKriGe07cRzDs48uco-E3hAwUp711hPgm6LwVIxVSA6Un9k3ATmCwBry1_LXJWsnjNr4Ui0Yv4_xppvPglndHpWNMsyOt2hoWQN8Ru8J4yicyKsd8hnmuJtF2A8c7DyyQIGIktrMW1MDqPVLosiUFu2GgZgM-jWzIKV4xSrvMa4f6liIJqJ-tQk73ma_d92ySw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
نخست وزیر اسپانیا : «در تهران، یک خامنه‌ای با یک خامنه‌ای دیگر که بدتر است جایگزین شده؛ چون مجتبی از پدرش خون‌ریزتر و دیکتاتورتر است و او واقعاً سلاح هسته‌ای می‌خواهد.»</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/farahmand_alipour/6304" target="_blank">📅 18:49 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6303">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/403aadedf7.mp4?token=u8PSNcEOfg5MKS7YTKTr3HbB6RQa1vJIh8_StZPr1cQkl8yUkpRuAWrT6dmUfoD9Jmk6xoiPiOGUKIPMEewtVfDNFoMI27o14SItWf2jRVKEJss7mrpijOdvSI1Of4bgkJNPFgOHQ8yjIxTKhb7coAghm8It8JD9KKAZuFT_Df1vyLqPxWuM3t_klx3jqopNY63UzfoQmotKLHDMLLBYDdERSUO5_fXzLWTGhbjyigyjfpTcbtalg-Vqu_pnRHn_4rXwqw6vREWayylI7_SxEqY_TuwXl_S7-w0dK0KFJX-alm1TNfPpu8AFH4B6QXTXNxFuv_5GtZCMNw2VAl5JFQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/403aadedf7.mp4?token=u8PSNcEOfg5MKS7YTKTr3HbB6RQa1vJIh8_StZPr1cQkl8yUkpRuAWrT6dmUfoD9Jmk6xoiPiOGUKIPMEewtVfDNFoMI27o14SItWf2jRVKEJss7mrpijOdvSI1Of4bgkJNPFgOHQ8yjIxTKhb7coAghm8It8JD9KKAZuFT_Df1vyLqPxWuM3t_klx3jqopNY63UzfoQmotKLHDMLLBYDdERSUO5_fXzLWTGhbjyigyjfpTcbtalg-Vqu_pnRHn_4rXwqw6vREWayylI7_SxEqY_TuwXl_S7-w0dK0KFJX-alm1TNfPpu8AFH4B6QXTXNxFuv_5GtZCMNw2VAl5JFQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اسپانیا که این روزها دارند
پرچمش رو میچرخونن!
می‌خواستیم ۲.۵ میلیون دلار بهشون بدیم
برای اینکه با ما فوتبال بازی کنن، قبول نکردن!</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/farahmand_alipour/6303" target="_blank">📅 18:43 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6302">
<div class="tg-post-header">📌 پیام #64</div>
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
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WE2TfZG_ddsDCPepmC8wEY5uCWnHit-rMd9Rz2FV78Yu0nLnvZ9Mnn5Pk9ngSzMsAybCQkQy-LnbULD129pjReQFlXsJJ4_SpjT4Wl9YUY0NSvFxOfaGIxgEfmliX_TJwI9UaOZsDk_MDCyN92rjDfEkgh7Nbj7Jf2_1SYV3DuCqivPB2JpKyWql3Vz5MVm_OCnr1lmPFpSfdXbpVTQwSy66qUrKYhmwpFCP8X-H6GK9TJhZdBXRP-qRrrheekdtM5mEF3X4EFw3QjSbK4JzxY4X5-zXAS5V8R8anBDkTnfsm2M_JlrhMkA5HWgzPjcD8IKSXLQpO7ZpZ3D1gsXwJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ با بازنشر تصویر گل‌محمد محمدی ۲۳ ساله، که امروز به دست جمهوری اسلامی اعدام شد:
«جدیدترین قربانی از اون ۵۲ هزار نفر  معترض کشته شده.
وحشی‌ها!
کی قراره دمکراسی‌ها بیدار بشن؟ (نسبت به جنایات ج‌ا) »</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/farahmand_alipour/6301" target="_blank">📅 16:52 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6300">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/46c8806804.mp4?token=Gh_2aDeClnZ3sPAndgj9_iJ4vQYMiSYnRzUNarTf6n10d8oWAr7QJ0h0yVo_dRPx7rFnQ9md919Oc8qoUgycTyS8HH0sQpLT9OS0768qWCY58MC2je3pbiMuZDLYzgfBUGszGSSX1FhTHNcPIyJ_O-lBcTjTnjzF-OgrOC6XOAigQ5tXpKmXT5_uQMg3Am6fJfQbUbgGy_uR6jCHNAiikKFkFRQzGBIHZgg4Dqvv61uhxN5ooL-Ngh6DaLr03SelT6pec0vufiON6Nj2OZi10EhnN4W7bblWKCThUnJMlLik71hrHJASJG5NKPV3AjW_9m7fMEYB1ld9BHWhB9peFw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/46c8806804.mp4?token=Gh_2aDeClnZ3sPAndgj9_iJ4vQYMiSYnRzUNarTf6n10d8oWAr7QJ0h0yVo_dRPx7rFnQ9md919Oc8qoUgycTyS8HH0sQpLT9OS0768qWCY58MC2je3pbiMuZDLYzgfBUGszGSSX1FhTHNcPIyJ_O-lBcTjTnjzF-OgrOC6XOAigQ5tXpKmXT5_uQMg3Am6fJfQbUbgGy_uR6jCHNAiikKFkFRQzGBIHZgg4Dqvv61uhxN5ooL-Ngh6DaLr03SelT6pec0vufiON6Nj2OZi10EhnN4W7bblWKCThUnJMlLik71hrHJASJG5NKPV3AjW_9m7fMEYB1ld9BHWhB9peFw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خامنه‌ای: ما دنبال اقامهٔ حکم الهی هستیم! ما هستیم برای تحکیم دین خدا! برای رونق اقتصادی و… که دیگران هم می‌توانند انجام بدهند و در دنیا هم انجام می‌دهند!  بله! بقیهٔ دنیا دنبال ساخت کشورشان هستند، این‌ها برای تحکیم دین خدا!! پول و ثروت ایران برای این خرج…</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/farahmand_alipour/6300" target="_blank">📅 16:28 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6299">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">‏رویترز: حوثی‌های یمن در ایمیلی به شرکت‌های کشتیرانی نسبت به بارگیری یا تخلیه بار در بنادر عربستان سعودی هشدار دادند.</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/farahmand_alipour/6299" target="_blank">📅 14:26 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6298">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">🚨
جمهوری اسلامی امروز دست به حملات گسترده‌ای به قطر و بحرین زده.
علاوه بر این جمهوری اسلامی به دو کشتی یونانی در تنگه هرمز حمله کرده.
حمله به اردن هم ادامه داره.</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/farahmand_alipour/6298" target="_blank">📅 13:16 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6297">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3cb0045793.mp4?token=IXcv4LVmyoWHYjsoxGx2dY-djUfwzTWGQxdmIvFUwoGUq_uexlaE8IhYIGHJnCGUkyrruwT-aujurL7p3wuV8UvU7zrndPe8LyaJ7-h2L0RjsDnIlMrVK27LsxjMgOgTssSYDYElnJsNakeIJB-Uj0wk8bVm7cqGaPeySh-8iDFSmsoKslHnI855lIkfbdTkNEwWBrq8bnXtAeD1-5NSQnlzA0tC8RNQeImBhn1D13MxkaHO8dVNFovUQPMS8mxLi55GPzO59p4BAMjH7EBq0SUpShgTLVCzJRDulxAdtYEYt2whBH0AQSrS5rdTAyntx-cfONQhud88EVeyWU5dNQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3cb0045793.mp4?token=IXcv4LVmyoWHYjsoxGx2dY-djUfwzTWGQxdmIvFUwoGUq_uexlaE8IhYIGHJnCGUkyrruwT-aujurL7p3wuV8UvU7zrndPe8LyaJ7-h2L0RjsDnIlMrVK27LsxjMgOgTssSYDYElnJsNakeIJB-Uj0wk8bVm7cqGaPeySh-8iDFSmsoKslHnI855lIkfbdTkNEwWBrq8bnXtAeD1-5NSQnlzA0tC8RNQeImBhn1D13MxkaHO8dVNFovUQPMS8mxLi55GPzO59p4BAMjH7EBq0SUpShgTLVCzJRDulxAdtYEYt2whBH0AQSrS5rdTAyntx-cfONQhud88EVeyWU5dNQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">«آتش‌بس نظر مجتبی است؟ »
عراقچی طوری پاسخ میده
که گویی نمی‌دونه این نظر مجتبی بود
یا نبود! «ارتباط سخته»!
خودش هم میگه مجتبی رو هیچ وقت ندیده!
اصلا معلوم نیست زنده است یا کشته شده
برای همینه که نمی‌دونن نظرش چیه</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/farahmand_alipour/6297" target="_blank">📅 11:54 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6296">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/011fb08ef0.mp4?token=OwE2PjPAG7f15A8MCGLvUe0fTBHbA3FB1gaFMYoh5VLno-TDuXm4WR1f-43mgiiEwEhFLZogaXdFerH1aVWUs_9GH4DbGohnR2onvYCjxEg9qqeM7qTxGjuieGFjSegf8ggVbo19AI8RimZrshkgbbFeeJ1V-PbwpGYrChPQAEsvQuOzIZSOI9jm6fYUWZdHAuy7SBAM-6SU7Lg08dtehHg-1wHKpX1tDTJ-aSkDEXTIZ5igKR_eEiBHzm7LwDXq4TyAiVkYJ9CBmcfqWX9YOyDauVv7FqvM-_Dyyf9Vv1pSu4ccor9KPcoJ2xfN9F2p1W6SEKZ7nwqCE5KeIuCAeQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/011fb08ef0.mp4?token=OwE2PjPAG7f15A8MCGLvUe0fTBHbA3FB1gaFMYoh5VLno-TDuXm4WR1f-43mgiiEwEhFLZogaXdFerH1aVWUs_9GH4DbGohnR2onvYCjxEg9qqeM7qTxGjuieGFjSegf8ggVbo19AI8RimZrshkgbbFeeJ1V-PbwpGYrChPQAEsvQuOzIZSOI9jm6fYUWZdHAuy7SBAM-6SU7Lg08dtehHg-1wHKpX1tDTJ-aSkDEXTIZ5igKR_eEiBHzm7LwDXq4TyAiVkYJ9CBmcfqWX9YOyDauVv7FqvM-_Dyyf9Vv1pSu4ccor9KPcoJ2xfN9F2p1W6SEKZ7nwqCE5KeIuCAeQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">محمد اکرمی نیا سخنگوی ارتش
‏به روشنی میگه اكر آمريكایی‌ها
بيان در جنوب ايران ما خاك خودمونو هدف قرار میدیم.</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/farahmand_alipour/6296" target="_blank">📅 11:35 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6295">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromحافظه تاریخی</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/78bd1813e8.mp4?token=gci9m1Drw82PHsKg_AeNm1eOpKB4eKOry4glj_BMDo7jmn7YwAbXN2p-xdJ1G5XCq3n1zrUFpP-uqqUTOu6o8fw_-XqYxsuwPXlSrdY7YJvR1O0GRd5nFVk91tuoKu8LtADA7pVVrNxHE4dsixZIQQ6I5gnqssv6YvT3FHUBlX7OarahNTIO8FVCglNOphvdXcO9gzXliLVkVBmHggm0qM4qgkk0GpnuT6lcRI8T_0Cu7UocqhAnK1oP7yt3f1rGfLwiRdzzPO5mvWfiXYWomoKAS7PA6g_cLPPPtdu90gUgvNjcmhAui_Ji1mSokZB8Er4uQLGrum5VKmH5eRNV2jSNc6UWnVCMvGvj2m_a17JyqrA7iAAIZlsEuBwMzX4-yZNKfI8MF7Vk922h5dMK4KfUJ5roiRGSQbMbsPHcCxPwVWB66twgn-tRi6fDDceCK1Y8CCyNcseY_ZLlOeh6SDzaUoXS89lXEqWW7y2SSVNRguBU9zwXcSDWShc4JgfFlctAgTSieOmNAIUMJK9Ap6EszpAp114Zjvwwj1kHEr_eb5J7E6QrEZpsOw_rm_63qQa3VXGqid0m1V3nZE8p-FJYpwiJZV8kRlPC2xdvgxnZ4lVvCfAVr8S1cTYlnspFyp2QSwHdOlIHe4TjtRGyUoHzO96aNQi_Sw75SauXV_Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/78bd1813e8.mp4?token=gci9m1Drw82PHsKg_AeNm1eOpKB4eKOry4glj_BMDo7jmn7YwAbXN2p-xdJ1G5XCq3n1zrUFpP-uqqUTOu6o8fw_-XqYxsuwPXlSrdY7YJvR1O0GRd5nFVk91tuoKu8LtADA7pVVrNxHE4dsixZIQQ6I5gnqssv6YvT3FHUBlX7OarahNTIO8FVCglNOphvdXcO9gzXliLVkVBmHggm0qM4qgkk0GpnuT6lcRI8T_0Cu7UocqhAnK1oP7yt3f1rGfLwiRdzzPO5mvWfiXYWomoKAS7PA6g_cLPPPtdu90gUgvNjcmhAui_Ji1mSokZB8Er4uQLGrum5VKmH5eRNV2jSNc6UWnVCMvGvj2m_a17JyqrA7iAAIZlsEuBwMzX4-yZNKfI8MF7Vk922h5dMK4KfUJ5roiRGSQbMbsPHcCxPwVWB66twgn-tRi6fDDceCK1Y8CCyNcseY_ZLlOeh6SDzaUoXS89lXEqWW7y2SSVNRguBU9zwXcSDWShc4JgfFlctAgTSieOmNAIUMJK9Ap6EszpAp114Zjvwwj1kHEr_eb5J7E6QrEZpsOw_rm_63qQa3VXGqid0m1V3nZE8p-FJYpwiJZV8kRlPC2xdvgxnZ4lVvCfAVr8S1cTYlnspFyp2QSwHdOlIHe4TjtRGyUoHzO96aNQi_Sw75SauXV_Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حملات نیروهای مقاومت فرانسه به رهبری ژنرال دوگل به زیرساخت‌های فرانسه و منفجر کردن پل‌ها، قطارها و خطوط راه‌ آهن در جریان بمباران‌های متفقین برای آزادسازی فرانسه اشغالی از حکومت نازی‌ها، ۱۹۴۴
@hafezeye_tarikhi</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/farahmand_alipour/6295" target="_blank">📅 09:37 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6294">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">واکنش نیروهای مقاومت فرانسه به رهبری ژنرال دوگل به کشته شدن ۶۶ کودک فرانسوی بر اثر خطای بمباران متفقین در جریان عملیات آزادسازی فرانسه از حکومت تحت حمایت نازی‌ها @hafezeye_tarikhi</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/farahmand_alipour/6294" target="_blank">📅 09:31 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6293">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromحافظه تاریخی</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/59eba4787d.mp4?token=QNlixRDdZUWZ1r7jXpNgtQqa2hyi94IHzLqWhbbCDb4Be5PYltb0gZfTrYBsafajAIR7oTgShzYPT79B7-uss2Wfyjph1ncVbJxaVDmW7jAjC8IZ9IKzvOpquEDzz0NyyLnmuMQqE5y2ib5onh1ORNqUTvQyyIVO5hVXK3VQfe9lf7us6YfcBgvJI3a7MGqdwqehC6cY3IY4ruu16zhu6nVKqaMWvsiig9BbRG2nN85i-ZUDiifErT6bsPIdXs6OM_IPS2lzfc5YPxxhfGFlFpNtSpToKrpFXBe1vxgzatJjrF-f50aSS748VvCSMwTzGa6WlvE_4Oc71nTEYuS1nw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/59eba4787d.mp4?token=QNlixRDdZUWZ1r7jXpNgtQqa2hyi94IHzLqWhbbCDb4Be5PYltb0gZfTrYBsafajAIR7oTgShzYPT79B7-uss2Wfyjph1ncVbJxaVDmW7jAjC8IZ9IKzvOpquEDzz0NyyLnmuMQqE5y2ib5onh1ORNqUTvQyyIVO5hVXK3VQfe9lf7us6YfcBgvJI3a7MGqdwqehC6cY3IY4ruu16zhu6nVKqaMWvsiig9BbRG2nN85i-ZUDiifErT6bsPIdXs6OM_IPS2lzfc5YPxxhfGFlFpNtSpToKrpFXBe1vxgzatJjrF-f50aSS748VvCSMwTzGa6WlvE_4Oc71nTEYuS1nw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">واکنش نیروهای مقاومت فرانسه به رهبری ژنرال دوگل به کشته شدن ۶۶ کودک فرانسوی بر اثر خطای بمباران متفقین در جریان عملیات آزادسازی فرانسه از حکومت تحت حمایت نازی‌ها
@hafezeye_tarikhi</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/farahmand_alipour/6293" target="_blank">📅 09:30 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6292">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3ba53f516a.mp4?token=rHyKahmbdFEf1kQB43jp1-rDIqgL0QDMnVfhWxrF-9-l7N_0mNFEoTCTpd8Qnb9liY2cRlEiDuOyOiDEs-uuDl32IugS0xohPQJwII7f2pbXOpQ929I_hYWEEBwwtMKftAMnZKdEj-pSKnOCKADz9XPl4bviybQM4i70iAR5M2KluywmxARfDMprRIcAOtdvNb9Oeis_9MuxLDud0NNyhSVexVqo5H3aG-aMAw-ahyW_l16AjmJp0bg8XkuBE1h2gsrgH2rOnBJ7TxNURbrJv5LPBDAjX_i8IJVH5TFUwqZDpA65bTezcq_ZYz19HZMCQUEVDRTLUymB1-_E7NPTHg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3ba53f516a.mp4?token=rHyKahmbdFEf1kQB43jp1-rDIqgL0QDMnVfhWxrF-9-l7N_0mNFEoTCTpd8Qnb9liY2cRlEiDuOyOiDEs-uuDl32IugS0xohPQJwII7f2pbXOpQ929I_hYWEEBwwtMKftAMnZKdEj-pSKnOCKADz9XPl4bviybQM4i70iAR5M2KluywmxARfDMprRIcAOtdvNb9Oeis_9MuxLDud0NNyhSVexVqo5H3aG-aMAw-ahyW_l16AjmJp0bg8XkuBE1h2gsrgH2rOnBJ7TxNURbrJv5LPBDAjX_i8IJVH5TFUwqZDpA65bTezcq_ZYz19HZMCQUEVDRTLUymB1-_E7NPTHg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">۲۱ ماه پس از کشته شدن «یحیی سنوار» رهبر گروه تروریستی حماس، این گروه «خلیل الحلیه» را به عنوان رهبر جدید خود معرفی کرد.  او در رقابت با «خالد مشعل» موفق شد این پست و مقام را بگیرد زیرا که بیش از خالد مشعل، مدافع اقدامات یحیی سنوار بود و جنایت ۷ اکتبر! که چیزی…</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/farahmand_alipour/6292" target="_blank">📅 09:15 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6290">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iMGEZwqvhyeAZxd1Zg3GBeX4MScM6t9OWF17y2BE6bgK09zzFQnk_nLbSffxyqX0aZ8evIEli5pZECuYVLK0w8kN4j6ctwvcXp99lJyMvG4c7UN6fxRdz0hfYA8_OsbpCW3sQxI5VudKy2cius2v9lHHUvOYGJV9n-lV9lbCz6pClW0jaYXGq_rN9G9C9GQXyt6c6HowEmp1otMRby_SL48NmzWNzBY1h8WyAUL6QK6EZFxaKbLaI9R9DDjqv2OmbvpPhyHxcjEDceaZtwuUiVK1dqjyDAWZvxarjFC2VMI_52B7jdA0rvJRH6mlZI7vvBGC2CDY9SJnk4OBWkuOXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۲۱ ماه پس از کشته شدن «یحیی سنوار» رهبر گروه تروریستی حماس، این گروه «خلیل الحلیه» را به عنوان رهبر جدید خود معرفی کرد.
او در رقابت با «خالد مشعل» موفق شد این پست و مقام را بگیرد زیرا که بیش از خالد مشعل، مدافع اقدامات یحیی سنوار بود و جنایت ۷ اکتبر! که چیزی جز فاجعه برای غزه نداشت!
تصویری از خلیل الحلیه، رهبر جدید حماس با خامنه‌ای. هم خامنه‌ای و هم یحیی سنوار توسط اسرائیل حذف شدند.</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/farahmand_alipour/6290" target="_blank">📅 09:12 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6289">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C_RRyZsPYQqFcns7pPgJbH5iTi6hpdsvqNsNQ1yb4K_vsXgFqaliToRrKvVjsJHvuiOiv5d__DrxAJHFoL-2nHbt5qhMxKObvlwVZOD4HAsxCBDr3trILxXgmZLvTRKWRluvrIOvQwO7QoCErypEyWiWDeObdeVSUDCz_kh-ksCnPvYgNgXMePqsJL5OyDWgSEwz6sjTksgdwdaMABsHHJXI6_y_nF_V0ds6bPZB0Z18Ws5M946AqCXPLlws-yNpVW3K2vSYbU2CSfVEcHaGFwcOzoF39OZH-C5svpqkn2RnNqqma_TEWTyzj3a5otzFs_-MzRw-gBwGsFMZE2i_fw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارزیابی اطلاعاتی اسرائیل نشان می‌دهد جمهوری اسلامی پائیز گذشته هزاران سانتریفیوژ غنی‌سازی اورانیوم را به تونل‌های عمیق در کوه کلنگ منتقل کرده است.</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/farahmand_alipour/6289" target="_blank">📅 06:50 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6288">
<div class="tg-post-header">📌 پیام #51</div>
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
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/75cc0ec8fd.mp4?token=OPY1l9lXXwysENdhzMKhId_Jbzghj5sQ4mcTRmAq0KxC-s6hJznkDwt5nswq2Lu9W8C2FQL-XeOMjQzzt98lX-N-BNhwhDNWNylHkhc8XdUVsGhsLIacRTT5Ak8tke1dQpWp04ESSTZ9b-C0bRQhaF1ECuJNmdC6HRM1wi7ZaqISt_CXpPHpkULOUtEYKMhkKm_3Vp4dCVt9R76b6Kpx6B8_xZsfEmb8GLMVEdujAowjHnA-hBkBr1Gl_xS2uiJEi9adYv_QEX2NcqyHBWqKL2m1elberuAJVxDTQbanSOpsUjpXJzHS6l9hvzMjq8OdSbQHFhaii98IqPFCFu6OeTEnTNuPmLkQ4cKG1_cO0hxXTfId9w-djTCHh-MYNif7JY2oWdwbOMSZAa-Qy5qBp8mnDR5fmNfW_6g-lwfd3X4QbsMQrcokqdKt9SEgjdCaT9lCiXaDOx2KQmbsadOJUDWhpf6PVYBoTUuPsOIdH3C31Cht_KnoaaNZaE-HrnE8hfHFGtNDjwf47-_74zr2yzQy_HRdpRNRNnIE6Hm-y9ghBpFa-abhAOL_SKQ4LNMLvcJd7ClGXBXsXJ-PHv6ZjkVnd7NRYfZhnm-Vnfq_WwzmaZ5aFiflB8dqNfa04EiJ4OXy2DIeRLDhyIo5qw8Xo0QU5WAgtaUq0dwzhyFx5g0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/75cc0ec8fd.mp4?token=OPY1l9lXXwysENdhzMKhId_Jbzghj5sQ4mcTRmAq0KxC-s6hJznkDwt5nswq2Lu9W8C2FQL-XeOMjQzzt98lX-N-BNhwhDNWNylHkhc8XdUVsGhsLIacRTT5Ak8tke1dQpWp04ESSTZ9b-C0bRQhaF1ECuJNmdC6HRM1wi7ZaqISt_CXpPHpkULOUtEYKMhkKm_3Vp4dCVt9R76b6Kpx6B8_xZsfEmb8GLMVEdujAowjHnA-hBkBr1Gl_xS2uiJEi9adYv_QEX2NcqyHBWqKL2m1elberuAJVxDTQbanSOpsUjpXJzHS6l9hvzMjq8OdSbQHFhaii98IqPFCFu6OeTEnTNuPmLkQ4cKG1_cO0hxXTfId9w-djTCHh-MYNif7JY2oWdwbOMSZAa-Qy5qBp8mnDR5fmNfW_6g-lwfd3X4QbsMQrcokqdKt9SEgjdCaT9lCiXaDOx2KQmbsadOJUDWhpf6PVYBoTUuPsOIdH3C31Cht_KnoaaNZaE-HrnE8hfHFGtNDjwf47-_74zr2yzQy_HRdpRNRNnIE6Hm-y9ghBpFa-abhAOL_SKQ4LNMLvcJd7ClGXBXsXJ-PHv6ZjkVnd7NRYfZhnm-Vnfq_WwzmaZ5aFiflB8dqNfa04EiJ4OXy2DIeRLDhyIo5qw8Xo0QU5WAgtaUq0dwzhyFx5g0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نماینده رودبار :
اول جمهوری اسلامی ‌آتش‌بس
را نقض کرد و سپس آمریکا پاسخ داد.</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/farahmand_alipour/6287" target="_blank">📅 01:10 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6286">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">🚨
گزارش انفجار مهیب در شیراز
🚨
گزارش انفجار در اصفهان</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/farahmand_alipour/6286" target="_blank">📅 01:02 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6285">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">🚨
🚨
به گزارش خبرگزاری ایرنا، در ساعات اخیر صدای حداقل ۱۴ انفجار بزرگ و کوچک در چابهار و کنارک شنیده شده است.
فرماندار چابهار : از محل اصابت‌ها هنوز اطلاعی نداریم!</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/farahmand_alipour/6285" target="_blank">📅 00:32 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6284">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">🚨
🚨
گزارش چندین حمله به چابهار،
🔺
چندین انفجار در بندرعباس،
🔺
انفجار در سیریک، قشم، بوشهر، دزفول.
🔺
پرواز جنگنده‌ها بر فراز چابهار در ارتفاع پائین.</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/farahmand_alipour/6284" target="_blank">📅 00:06 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6283">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">🚨
آمریکا از شهروندانش خواست تا هرچه سریعتر خاورمیانه را ترک کنند.</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/farahmand_alipour/6283" target="_blank">📅 00:03 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6282">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dBCqk2oiB-DVrll56APrHibPY9PGaUFhozpyMPc7lxdWDZ7Yi-80fInLEWmCEIGZPYNTkQWOKI5e0OnJQx4AfyFKFwTrMOwlp293987vCTK-s7Hv3iIlcN9e7vHj3RRlWTm3KOkI7VeFsqhfa43cJIHK4rNYThfQ2dE7yC18TKN4xAY77LmAp2I_M4gtokw8U8rieo2nZvYq1V4kyogwvrap59SEeleL4_-wupcqTwwv_tFsii9JCIin5wxgfQbFvAKbEVPsCRZTnRWBcovMqULFYrg1wsRJwPHj518_3GTauyfvis55bptk6Ehzy7ay8fvjMbL38OS8jEDAFbJSIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ :
اگه قراره کسی دستگیر شود، سران جمهوری اسلامی هستند.</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/farahmand_alipour/6282" target="_blank">📅 21:09 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6281">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YlfqYGU4z2XRksuZPWYNdLONt9k8vasqjRwDfkXXpKgJc--PfA002FPCNP90N0VDB_J9lLQJ5nOEPBstzHXBRGCXRF0-n_mxO_aXtOHuH90EAeczY4hFWhrE82gcdaV56_NMJAmtP72Ded2DJC0SZIXZuqUhxK2qYPs6vkCetcY-M2jRXZuk3yffLUaCalzgqehmuqK_We7N8bR3qsy8hbnGNAJK3RY02ABUXymJ2aoIxI29v6VaB19uG3RvM3zxg0C8za_wRhSUTboPJPfHJl9YVQ_IXOtzIzJJChK1dg72NknSS53HlJF6S7PQ8eiiL-h_g4TrtmyFntyAoANUkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حمله جمهوری اسلامی به یک کشتی
در تنگه هرمز</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/farahmand_alipour/6281" target="_blank">📅 18:12 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6280">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/svn8wjfAzB0fZZFp1eoquc40uySfShCT9FuxJLgC5CxxLHlezIAseE13W-8WrqfUhkT7fj3YQ1OspV5PFbRC3wN4fVCRe3oOEj-10T0WHAuQgfa6h770IpwyqtCJe_ry6mkdWdCHhA8Co1TAmHlVESGXSrVJvo1-6C9jRDCamb78-OOfYst_7k3mIu_oOT9pJvx0gcWLvXYqw26eZBqzbf5t0Dfoeow5JFUUb8eKa7qS3WxbJy-UeefQ44rxRZljU7hEMp6YlOWwYp9osHASkXHuBf2rqVC0cFCv2lamvDdn_kNcfwKGttor8mYvqolEzMs_1A2EsyMgNIH6hW8Sxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
گزارش‌هایی از حمله به شیراز
هدف: احتمالا صنایع الکترونیک شیراز</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/farahmand_alipour/6280" target="_blank">📅 17:53 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6279">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">این سخنرانی ترامپ در عربستان رو به یاد دارید؟  پارسال، درست در  تاریخ ۲۳ اردیبهشت ۱۴۰۴  که به درستی گفت :« رهبران ایران روی دزدیدن ثروت مردم خود و خونریزی در خارج تمرکز کرده‌اند.»</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/farahmand_alipour/6279" target="_blank">📅 17:27 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6278">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">این سخنرانی ترامپ در عربستان رو به یاد دارید؟
پارسال، درست در  تاریخ ۲۳ اردیبهشت ۱۴۰۴
که به درستی گفت :« رهبران ایران روی دزدیدن ثروت مردم خود و خونریزی در خارج تمرکز کرده‌اند.»</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/farahmand_alipour/6278" target="_blank">📅 17:27 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6277">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b8Y7UMyB-WqHv5Awy99B2oJkdrJfp8mpBSRTV82z5XOStH0mtgxzhVc21qVxM-B7k_RhNdmxZShVlWOR-9zayUA6tTGZjimsipjvwd1JdM0GJ0a2b82fmsckNUjiC1abLH59P02ojH2vtNd0GvI8KnYHVdDipNjqkRyngIzHwFGUOgsxkdfvtNGJYWweywmRzj8zcSR8EHiRwbf75LReh51gh85Ba1UcNSbwt5dv7SbANi6Z-NVfKWQcmAwRwEfDK-jW2hsSg2qhyDED8Jv-TPYCopLOCxgLipxfz7T2bDnC5cF9ATRkUSjaOr7UnRLIGmlmpnHgJSn4Pgib1BinDQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/farahmand_alipour/6277" target="_blank">📅 16:00 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6276">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3d8904c5eb.mp4?token=pmIHrKUGkZcNErC32E498Tc6ulMVuJU0DB_Or8y0Dq7rubz5mOBgRMjH5Jq6KYH6M3AwYJqe_i_Yd3jw-S9dFMCve4iQmS9MIw_zh3YE7QAW5ggQjkG5jZec5S-xed9HjpaTuVnLhh4B6E4YWBRFHHFGtHzSJUKImYZUxLsY7s2pGVfLK0M5-kYL7FAGCjVRGYn5BE51Y_MtGIIYsc9Bm1zSEMtv4451q6lhXmx4rHtGZBNuH0cmS4FaY2EDsZpfNSnERHEHD1ZirwJnCIbvQ1_YcUh0iEJpkyJxUvSuvDBziuMX8Op_3vH9r5Ei4rJWOAwDXJZqPRuNkMVX6DeiD4wdMqr5mUDwh1On-nhG_BEKvIZGYrZOujucApmLx1ze5-34142u-2quBa3U8YuVAfW-KWPJ8Gx436SV3g8wxJUfA0fkuUGYe7Ct8gDCUaKWhH0vG3cBn64dmxg2AbyyZTwRDvo0_jACv8wL0x-QyTItS3xOSO68Brm6v6ABAroHhUwJtS9Hc0nY5apunjtKuyeXaz_cHCQeX2u5fm1NUgPvFE0DHgHepFayRUgdhq0Tfs9_ETZ4Xv1UTFzICQccWF3JyX6i6GCtSYIGz32G0Jgli_MbpFGAgAefTzeUGscB9sYqFbftQnNA6EYkiqkgcHvy1pciCW7NrbXPaDPEqqQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3d8904c5eb.mp4?token=pmIHrKUGkZcNErC32E498Tc6ulMVuJU0DB_Or8y0Dq7rubz5mOBgRMjH5Jq6KYH6M3AwYJqe_i_Yd3jw-S9dFMCve4iQmS9MIw_zh3YE7QAW5ggQjkG5jZec5S-xed9HjpaTuVnLhh4B6E4YWBRFHHFGtHzSJUKImYZUxLsY7s2pGVfLK0M5-kYL7FAGCjVRGYn5BE51Y_MtGIIYsc9Bm1zSEMtv4451q6lhXmx4rHtGZBNuH0cmS4FaY2EDsZpfNSnERHEHD1ZirwJnCIbvQ1_YcUh0iEJpkyJxUvSuvDBziuMX8Op_3vH9r5Ei4rJWOAwDXJZqPRuNkMVX6DeiD4wdMqr5mUDwh1On-nhG_BEKvIZGYrZOujucApmLx1ze5-34142u-2quBa3U8YuVAfW-KWPJ8Gx436SV3g8wxJUfA0fkuUGYe7Ct8gDCUaKWhH0vG3cBn64dmxg2AbyyZTwRDvo0_jACv8wL0x-QyTItS3xOSO68Brm6v6ABAroHhUwJtS9Hc0nY5apunjtKuyeXaz_cHCQeX2u5fm1NUgPvFE0DHgHepFayRUgdhq0Tfs9_ETZ4Xv1UTFzICQccWF3JyX6i6GCtSYIGz32G0Jgli_MbpFGAgAefTzeUGscB9sYqFbftQnNA6EYkiqkgcHvy1pciCW7NrbXPaDPEqqQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مارکو روبیو :« ایران کشور ثروتمندی است.
یکی از دلایلی که امروز ایران در چنین وضعیت نابسامانی قرار دارد این است که هر پولی که این حکومت به دست می‌آور، چه از طریق کاهش تحریم‌ها باشد
و چه از محل فروش نفت، آن را صرف تروریست‌ها در منطقه می‌کند، حزب‌الله و حماس می‌کند…
.
در حالی که باید میلیاردها دلار برای ساختن و توسعه کشور خود و مردم ایران هزینه کنند، اما در عوض آن را صرف حمایت از تروریسم می‌کنند.»</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/farahmand_alipour/6276" target="_blank">📅 13:18 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6275">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">‏
🚨
دقایقی پیش، شنیده شدن صدای انفجارهای مهیب در ⁧ ساوه</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/farahmand_alipour/6275" target="_blank">📅 11:41 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6274">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">🚨
🚨
نورنیوز رسانه شورای عالی امنیت ملی:
شب گذشته تبریز، دشت‌آزادگان، ماهشهر، سربندر، سیریک، بندرعباس، چابهار، جاسک، کنارک، خورموج و خرم‌آبا‌د مورد حمله قرار گرفته‌اند.</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/farahmand_alipour/6274" target="_blank">📅 10:27 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6273">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">وضعیت اسکله بندر رجایی - بندرعباس
بندری که ۷۰٪ صادرات و واردات کشور را بر عهده دارد.</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/farahmand_alipour/6273" target="_blank">📅 10:20 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6272">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">🚨
🚨
فرماندار بوشهر: دقایقی پیش چند نقطه شهر بوشهر مورد اصابت قرار گرفت.</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/farahmand_alipour/6272" target="_blank">📅 10:04 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6271">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">علیرضا پناهیان : اگر بی‌برقی و بی‌آبی را تحمل کنید، اول منطقه را و بعد جهان را آزاد خواهیم کرد.  به زودی نام نویسی برای آزادی جهان آغاز خواهد شد و آب و برق جهان را از ستم صهیونیسم آزاد خواهیم کرد.</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/farahmand_alipour/6271" target="_blank">📅 09:45 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6270">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">علیرضا پناهیان : اگر بی‌برقی و بی‌آبی را تحمل کنید، اول منطقه را و بعد جهان را آزاد خواهیم کرد.
به زودی نام نویسی برای آزادی جهان آغاز خواهد شد و آب و برق جهان را از ستم صهیونیسم آزاد خواهیم کرد.</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/farahmand_alipour/6270" target="_blank">📅 09:26 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6269">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8e62469a72.mp4?token=qLkN4cWrdicAOEbuflcRPaIYqZTxdOX8mO1WI_U9eGjMRq4K_-6b4M6Y1tV3TrE99HkRea7MpVotIz8DosO75osYXMhpRPvaq-g7cJwRSOkzQK4Nf-f-PLXj01HuXVF0uElsVvf5fwBVGgTH80IIIp2lWvRavA5fLgr5VePpcq31_pEhrTkntDP9wgA2B0PJtoVbUzufq7TiZGW2orLwqEe2bdtrZDqDKAQop5_V2jHVWknB_DCvyGjlrAoi4ahLrJVDhOiWEsRSZ0u8IdcvVGM3YtVsbHoixjHA-jaKjJyNqVxpzWl4Bae8WRnLAh5dIQvTiiQS0wlq063oz3PdDA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8e62469a72.mp4?token=qLkN4cWrdicAOEbuflcRPaIYqZTxdOX8mO1WI_U9eGjMRq4K_-6b4M6Y1tV3TrE99HkRea7MpVotIz8DosO75osYXMhpRPvaq-g7cJwRSOkzQK4Nf-f-PLXj01HuXVF0uElsVvf5fwBVGgTH80IIIp2lWvRavA5fLgr5VePpcq31_pEhrTkntDP9wgA2B0PJtoVbUzufq7TiZGW2orLwqEe2bdtrZDqDKAQop5_V2jHVWknB_DCvyGjlrAoi4ahLrJVDhOiWEsRSZ0u8IdcvVGM3YtVsbHoixjHA-jaKjJyNqVxpzWl4Bae8WRnLAh5dIQvTiiQS0wlq063oz3PdDA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
ویدئوی منتسب به حمله و  انفجار مهیب دیشب به تبریز
مدیر کل مدیریت بحران آذربایجان شرقی شب گذشته در مصاحبه با ایرنا از حمله به یک منطقه نظامی در جنوب غرب تبریز خبر داد.
برخی گزارش‌ها اما حکایت از ۳ حمله به اطراف تبریز دارد.
حمله حوالی ساعت ۲:۳۰ بامداد رخ داد.</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/farahmand_alipour/6269" target="_blank">📅 08:46 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6268">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">🚨
کویت : در حال مقابله با حملات پهپادی هستیم.
کویت در چند روز گذشته در صدر اهداف حملات جمهوری اسلامی بوده.
مساحت این کشور کوچک عربی به اندازه «یک دهم» مساحت استان کرمان است.</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/farahmand_alipour/6268" target="_blank">📅 08:37 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6267">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZA1-yysOW3KIBnU8Sh6pD1afeaylx3EfQcimKzfh3-J8wdHY4ZU6fJDtqyKcKvEzBqWaiveLfXQV77JWhzPrDoJL1lso7R8-1YHNFQS5-dqC4lSFp1IeM2e0HjUpgYbQQNWYUs67jDogBIDEDS8EHd53M_b0-sclQtF48QhGpzjEHJwNBnH9l6zrtM8spWVk4ocsefW6lbxf5qCt4jh4EKiGCkLo_a7AS3y-_dJ59eohVqtYeaLx1weqQ7Tl19h_8KUa59Nh3WIqPetMeD_Y-3nqlESkx8pMyBMt1KmPhZfvXRrPoPH4iqyG28M6NMFIJeGxmCsDNgLbahQf4b8WjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
استانداری بوشهر:  بامداد امروز در دو مرحله، دو مکان نظامی در خورموج مورد حمله قرار گرفت.  این حملات باعث قطع برق در مناطقی از این شهرستان شد</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/farahmand_alipour/6267" target="_blank">📅 08:31 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6266">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">🚨
دو زمین‌لرزه ۵.۷ و ۵.۲ ریشتری حوالی کوزران کرمانشاه را لرزاند.</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/farahmand_alipour/6266" target="_blank">📅 08:22 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6265">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">« یه راه خوب اینه که چاه‌های نفت
امارات، عربستان، قطر، بحرین و کویت رو کلا بزنیم» !</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/farahmand_alipour/6265" target="_blank">📅 01:42 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6264">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eqtXoAvHMcnzTBL4tI-tkyiRbdM84d15nioDW49nJAJXrO9UazvAxnwkQryBzjGfOaH_1Q2ZZlTYhK5Mtz6qKYDYDKmGOOuDAIEKFq1Ss48xsQ21ia7_3qdJ7zOncOXpNy0v5S5W2ag8v8FwOMIroCYKrOLe7IFFt7NyA_u20ulyAynx2YT0_eBRi2o6iLoy4AJp58QmP2tVkYDRjZNTUIB0ixrKIv0i-mQzlemerXx6hYbJ8l9d1oSTa_u3J3j6ibQyyaBWI7mczQ0vVDg31KMOrVe4ZzLN3xm7PDCVN_YECyXAt7Vwd-nvChOCaaNnfVeudf9OiHES-lmsp728HQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بیسیمچی مدیا:
الله اکبر - اسپانیا برد :)</div>
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/farahmand_alipour/6264" target="_blank">📅 01:35 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6262">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/imOvz2VsBh3ze-Zn25IKRw1OwAWL-1RiwpYNgKCjcyYljsKbdSFV08al8wLxPwc-KyHFUC24meyAMI9tDmzBwNfNL9a23MEflVV5RYGgW8VBaWgOaUiNAiqwuGDsDBTFmrnYEiYARCNEnEyPAb8vvYKHnBEyzi0ri1Pi4dE3SKsCgRtZnYXLgYqH5veTfhAPdeJ6VX3Hao7e_nNlTmunzE3ynzxYnJrZSBZxvGKj3kAU8UMrUztoaUtHKwZ5IAE3hgB7pUmp2xEKVWLms4Q1RSyYc9ldEjpCTJkkDKe2ffK_slWdD7oTjAZ8osZ66dh9cGNaPoxgGsVc7NrTcJxljA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jDIXEE9vf-WrbzneOjhBEMtMm-sIDdwsoYdjqj1bJnJVjB--9dGGj7CFpw8q7K5yIh5PTGsNS1mG16tJwrfcx-S5r21LM2X-KhlE8K5ePWv5vIRZ5DsCvKXZOfzOEqTiiqO_-d-WVc5XxeZlctXn0G8zwsY007F7p6MtGhJMafW-QcZuBsutD0AmGJg8vyTkxcscr1yg1PBpQXppjbM3-X2tI8Ca_BjJTNI1WKACUSfQSYVx7pebofa3Qki5OrU5cHzfEPAzo4aGA6MCZHJaZd6QDk9X1QpQmrOujrGaPzGLpaJ0kXAo5nd4r3mTmw7371H2bydD-Qrt2ilE50x1-g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">حمل  موتور پهپاد آمریکایی با الاغ</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/farahmand_alipour/6262" target="_blank">📅 00:04 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6261">
<div class="tg-post-header">📌 پیام #25</div>
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
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/farahmand_alipour/6261" target="_blank">📅 23:00 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6260">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bOl5J7Oh9NalIeIXSx4Wg1ujKiqQsMMB7S6ko9B9gzlaOSgJ-EXp4QckNOHawhMsFLijbNNwtu_3xH3iIM0bqAFvTFiid1Y5NfUMBvF82DyAErA2csNSdNiWQqwl_TOoXdQlpEnRIekWA0SYWZdV4-h26Yl28obI1boL0JHOQOH_usLFYCU2DPDEBj60Ho9lQUY5br13IJnXR1drcG_PC5u0vvjYpPIJh2l9BhYyCQ90o0PKpuS3TS2Gi4PCJD9RsTLt6JmTV-PqgocItXX7bM5ZbYl-0K6H6Nekfy5YAS0f_nPhe7765hEDVx3g8dIIh_nffMNv-H2dSjAiT9BFEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">https://x.com/farahmandalipur/status/2078890340753568161?s=46</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/farahmand_alipour/6260" target="_blank">📅 20:41 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6259">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sC3LBeyhtGzv53UuePA9xQach-gxVmOOrjbs4wYxvoWq4XsWwJhhcjq6N2rm68I4gf2whoBtxxU4FdmcN-M6xOjns28kG9XLbeLDf_Li9qyvKxaDG6v67nDmKHW8i98_3EYQ8eZM0AXxQQrhP6ta2b97MKuXbRvC9E6akercdxC1aYZF4ip9oNCr_ydHkOIuvLSK6KKibl-9imIrE8_mUVBOZuEil7LlKThew16w7WPzu_bZXvOGt61uGZkuWvL9rNbASzb4ObKP9lb4JTDUpmtJLyAIf5RYiVOuektvLliI4Oka8ITcI9HDOmCEKOzG9UXpdPS_C0Ajsu-sZsLcjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رهبر گروه تروریستی حزب‌الله
به وبسایت خامنه‌ای :
خامنه‌ای گفته بود سوریه
ستون خیمه مقاومت است!
امروز نه از خامنه‌ای خبری است،
نه از نصرالله نه از بشار اسد و خیمه‌اش!
ظاهرا ستونش رو برای
بازماندگانشون نگه داشتن :)
یک «هفت اکتبر » راه انداختن و همگی با هم رفتن!</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/farahmand_alipour/6259" target="_blank">📅 20:25 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6258">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dNwg4px-zWBus66R8Ic4aBNHAzBXX-oh71vx15GUb8yOjXIQIGbrwBAJgidHKMruyrdkCFgqreFEsBSkxlP_GxhF_j-yDzdrAyV3roWVQcje_sI_AJF-DLUhWjQhr_EHRl9yvHv_WzCY3Hu4ZgLhFAPdKhQ8yDDSYeJXuSfPP2Vq1asbiO209c0TXjP1kCT1Ha-0bGMUWb1vau-fZ4kJ54yfDHYbCviSTOfOGwlULzJFCh3SGTZECH7cmRPWUbaNpb8TTzKMwgLiBUVSxVyoZs4BDrSxsWIiDgJ6zTp4x3YSH1paJrVWFdhlOkXXznyWYJKTXlsArLSlP8zTLeHkTQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9a1ebaca90.mp4?token=NOx9uLBXg0Sd2ga9CJYedTrayfWm-xVl7hsnLpefMFOwpS6SENtSZngVOcYSFnQsSxsksszSM_4Y_-mBjD3fd-YV6j6PNfCx7zmg1PwBiUI5nFV_RGhEEVNzTEDLTRro3buPLWDcN_CbMuEoBnKyh2blAACboWhg0ulqCBgG8jz_2tztKSsaKX3y7uRlFv8sgSanEuTH1knm8BODy1PpOTRFF2m5GMHpgJM9X_ikyvSikCQwD6VIXva1oLXFJDQVi1xj58aaEjPAbJJf9uQLOKckwEoA4Hb57LtXHLoFyY0gtM_FjEMChb5ruaZLmQwH51_qwaZ11zKFN6WwPvU7IA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9a1ebaca90.mp4?token=NOx9uLBXg0Sd2ga9CJYedTrayfWm-xVl7hsnLpefMFOwpS6SENtSZngVOcYSFnQsSxsksszSM_4Y_-mBjD3fd-YV6j6PNfCx7zmg1PwBiUI5nFV_RGhEEVNzTEDLTRro3buPLWDcN_CbMuEoBnKyh2blAACboWhg0ulqCBgG8jz_2tztKSsaKX3y7uRlFv8sgSanEuTH1knm8BODy1PpOTRFF2m5GMHpgJM9X_ikyvSikCQwD6VIXva1oLXFJDQVi1xj58aaEjPAbJJf9uQLOKckwEoA4Hb57LtXHLoFyY0gtM_FjEMChb5ruaZLmQwH51_qwaZ11zKFN6WwPvU7IA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
آتش‌سوزی در نیروگاه برق صبیه کویت
مقامات کویتی: در پی حملات مجدد
جمهوری اسلامی، یک نیروگاه برق و آب‌شیرین‌‌کن کویت برای دومین‌بار در ۲ روز گذشته  هدف حمله قرار گرفته است.</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/farahmand_alipour/6257" target="_blank">📅 19:23 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6256">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jAjKx5qtSuhe5uQ9uUTPTRH40-YHrbkOeqtKPXpP37n1_d0w_mA2n8kvlQA_2HTsXDoibMkaBe6c7tUyDk0mHuoPj1paczHPgTVucsSc1CSpV5LocaVSLE02SgJMDSRZ-Qm4ZnGEAh8X4Ms2-IhLk5P4qxCgkHi2jsWAWJ3cbBisZAuZWFkkMlP1jIxhYpqjpcK413lP4DjsK40LGhaHvNi5RsBCAjqQrj4g2S3LbIs3EZ9QLsiv_0EoO2dgyabJ-ZsEmdG1MoR_sJtPnQX671qKLFat2YwAtfIIPxkjzVmqS0Lj6jUOrYZiXMCAx2j877k7HkXaFTCvuRNeq79STg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
حمله موشکی آمریکا به نقطه‌ای در آبادان</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/farahmand_alipour/6256" target="_blank">📅 19:19 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6255">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ad154543bd.mp4?token=uqtddGtLS5njPQHPWQfaZaxTwvmm0toS2M40E5UNUEVz0vyrGfVD7raXw_l48UxlT2KlXqrhaiqPIv-eLNkmQ7WbUEtxCKoWSvnk50MZyyoBLsN3MeThB6jxHHE_6773Af6F82vel69j5qCRt3xAR-YHU2x-71VMx-TiPoe-14zGbjC25fSTKBU3UO-vuz8nL5GWtFlY-eLzbXTUvm4amDsZUwQppGsK3hp5MaSSgrDjoT0m-ZyWbF-E7M-c81_7tvqsRjx0Pk8De_rs6SiX8r7G5XzLIJ1fiP95-GFHhmLpF9txOJpbL6sY1LkfpbuyL7t6884CP1CAnBCQRkQGRA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ad154543bd.mp4?token=uqtddGtLS5njPQHPWQfaZaxTwvmm0toS2M40E5UNUEVz0vyrGfVD7raXw_l48UxlT2KlXqrhaiqPIv-eLNkmQ7WbUEtxCKoWSvnk50MZyyoBLsN3MeThB6jxHHE_6773Af6F82vel69j5qCRt3xAR-YHU2x-71VMx-TiPoe-14zGbjC25fSTKBU3UO-vuz8nL5GWtFlY-eLzbXTUvm4amDsZUwQppGsK3hp5MaSSgrDjoT0m-ZyWbF-E7M-c81_7tvqsRjx0Pk8De_rs6SiX8r7G5XzLIJ1fiP95-GFHhmLpF9txOJpbL6sY1LkfpbuyL7t6884CP1CAnBCQRkQGRA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حمایت مجدد نتانیاهو از آرژانتین.
دولت چپگرای اسپانیا در ماه‌های اخیر تندترین مواضع را نسبت به آمریکا و اسرائیل داشت، در عوض رئیس جمهور آرژانتین
«جمهوری اسلامی را دشمن آرژانتین» خواند
که دو بار در این کشور دست به بمب گذاری زده است (از جمله انفجار آمیا)</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/farahmand_alipour/6255" target="_blank">📅 19:13 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6254">
<div class="tg-post-header">📌 پیام #18</div>
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
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L1lV6tDtzaygket25cQ8FU-75Xuk3dgOSZWtN-m2RChzcmNpqrZmRPchcp-D2nurL_5q2yTY64PkeZJ3z3iy3HtId7lLmWj78_HNcUH3dsHSPDq2tlqnsQCnCFyN9sXgcYs3JTRLmJXC72k8pIbep5v91X0ATWHoDIYRRyHPaZ660_7aj4JNgkGtQC4GXTtzho5SQgfL5HKkSqfPidqQc_tOoWJRkxTgwo5bYF7rqlJ2rGk1uw_sYG3XDngrcS8-n4sHX_gVQrl6EOL5gW5PehQ-nKcYcw400pJHJJgMT_eoV8odluoIMVaHRLdbUYZB6oV_Fz59sjWngQDtHzsaNA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d28653e7d3.mp4?token=neHkeRSJKVLcSbyh3D4cyKJdeHHTdrYaomTAtr0nMd2ObIxNbLOOk3GdnL2XkdcDQqMsBxDCpLYdpDa-G_IDXpuSSUdLoYQ7tEgv2keHfPWlOEXF_lPKckyCoEnrkKENTZm8q2cWGrmJnsgsFqJYwo2_yjp8_0xbU8Vlav8kC86_cwJlrTdNThGqzxIlYic-tFLARZN6x7pKRVV_eqhGv-4oUC-6341twWvUCQk4yakLbf5T-2_nEXzEZ8CBs8QU4eVTkVJecRhX4pmO9N2fh9M95KasxDsljDu7W1hZTHjOKgjuzplu90k8O27VR8ZsR9LfliaLCLJdH8Fb7PZZZr-rqi694qUfpvAYUYOgmAKeLE0yDxBUlpVbSN_bxN6DvPTtyN-nwFcA_ZmARXZB1V-SlSmIstKWxmf233dtMkNvXYcNNoDdSfdtPppyl1OQhb7p16ZXxIbqbvO9vHbq61EnNzTOYjsM1MlaFUEYCI24m7Gk7-AdOlW7HxDqTDwyfnGGhl63YGJVVpYpJZn6gYvSnQlKItkmX8CLQhgfQb4FdmfDg8gg4ldMBskcVbsiDhf1hMvz2nPBs6imlYiARivyMslF63vtPxWMMdNpF_autfxG1TlnsXxRqWxIvOGQRoNfIk6JDh-GbWZiK3Un5XHYaOdA4fNd-8kWjOID364" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d28653e7d3.mp4?token=neHkeRSJKVLcSbyh3D4cyKJdeHHTdrYaomTAtr0nMd2ObIxNbLOOk3GdnL2XkdcDQqMsBxDCpLYdpDa-G_IDXpuSSUdLoYQ7tEgv2keHfPWlOEXF_lPKckyCoEnrkKENTZm8q2cWGrmJnsgsFqJYwo2_yjp8_0xbU8Vlav8kC86_cwJlrTdNThGqzxIlYic-tFLARZN6x7pKRVV_eqhGv-4oUC-6341twWvUCQk4yakLbf5T-2_nEXzEZ8CBs8QU4eVTkVJecRhX4pmO9N2fh9M95KasxDsljDu7W1hZTHjOKgjuzplu90k8O27VR8ZsR9LfliaLCLJdH8Fb7PZZZr-rqi694qUfpvAYUYOgmAKeLE0yDxBUlpVbSN_bxN6DvPTtyN-nwFcA_ZmARXZB1V-SlSmIstKWxmf233dtMkNvXYcNNoDdSfdtPppyl1OQhb7p16ZXxIbqbvO9vHbq61EnNzTOYjsM1MlaFUEYCI24m7Gk7-AdOlW7HxDqTDwyfnGGhl63YGJVVpYpJZn6gYvSnQlKItkmX8CLQhgfQb4FdmfDg8gg4ldMBskcVbsiDhf1hMvz2nPBs6imlYiARivyMslF63vtPxWMMdNpF_autfxG1TlnsXxRqWxIvOGQRoNfIk6JDh-GbWZiK3Un5XHYaOdA4fNd-8kWjOID364" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">موشکه دیگه! میاد میزنه
(سیستم پدافند و دفاعی ج‌ا]
عراقچی از روزهای جنگ ۴۰ روزه میگه که از ترس میرفتن تونل‌ها، جلساتی که در تونل‌ها برگزار می‌شدند.
از اینکه ساعت‌ها در ماشین در حال حرکت بود که جاش رو پیدا نکنن.
از خونه‌های به ظاهرا شخصی که پنهان می‌شوند و…
مجری برنامه هم اسم دو تا از تونل‌ها که فرماندهان اونجا پناه میبردن رو میگه.</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/farahmand_alipour/6251" target="_blank">📅 18:09 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6250">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">ترامپ درباره مشهد درست گفته بود
مشهد برای چند ساعت سقوط کرده بود</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/farahmand_alipour/6250" target="_blank">📅 18:01 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6249">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromحافظه تاریخی</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b5d96f954f.mp4?token=Wwl9S63gRQPY7MzeVOR0DtS6pngMI1cJtZe4VTq90VjLlkqbU3JMHz85YKMfa9sv6dM4xYvCbJlvRaZLur35S-k0Oa_-IILMw0wowRNiyFm-v0BM_zR2tWfFWY0ohwfqVqDZg-EgAv_9oQ0hmyQYA7a-kc1dM0x12StjpqCP_051n21STecOzb6CWmD7y_B37mwIHp6btT9FQJLMSR9BtPPpzz7U0-4kBZm_7HHFOpnB0P3-bOZr21FS6cTmhrG5K284QlT4e0WB_eoJ-D55hEnxHl-_Fx4OT7ZUgo_tvlrb41im3je7TM3oMXm9OW9OhSZPvCK2mefZGYZjZTmJZw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b5d96f954f.mp4?token=Wwl9S63gRQPY7MzeVOR0DtS6pngMI1cJtZe4VTq90VjLlkqbU3JMHz85YKMfa9sv6dM4xYvCbJlvRaZLur35S-k0Oa_-IILMw0wowRNiyFm-v0BM_zR2tWfFWY0ohwfqVqDZg-EgAv_9oQ0hmyQYA7a-kc1dM0x12StjpqCP_051n21STecOzb6CWmD7y_B37mwIHp6btT9FQJLMSR9BtPPpzz7U0-4kBZm_7HHFOpnB0P3-bOZr21FS6cTmhrG5K284QlT4e0WB_eoJ-D55hEnxHl-_Fx4OT7ZUgo_tvlrb41im3je7TM3oMXm9OW9OhSZPvCK2mefZGYZjZTmJZw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">علی خامنه‌ای، خرداد ۱۳۸۴:
خیال می‌کردند حکومت اسلامی یعنی خلافت موروثی، مثل بنی‌امیه. یک نفر مستبد با نام خلیفه اما با باطن فرعون. بعد هم که از دنیا می‌رود، یک نفر را جای خود معین می‌کند. در ذهن دنیا حکومت اسلامی این شکل تصویر می‌شد که بزرگترین اهانت به اسلام و حکومت اسلامی بود
@hafezeye_tarikhi</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/farahmand_alipour/6249" target="_blank">📅 17:51 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6248">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3fcb2949cf.mp4?token=d2mZo952KSiSdcGBy20rXe96sMnbvPlbOT8fYxKTRAboNuRC-z7rpbcSuSLFEFGwDt4DMgidr3u0v2JS9mqcpbNmeofpRRWJ_hMBUTSQ55dYrkH7yprVygKveTCog-EI7TJqUZarYXa27vwwe4_-tv4JQx2kOjFTnxG0Z1AIjP0nBVOEkMSQPnVa37MmMU4gNUNZv-CovPbEUCOVjLBdg9umaWJJAW8plWoJiLjAYGtsfHAaef4bGBnAbkaLqORs77lCLylTLUHR4WkCex-UgrMu1iqk3t_vIUOJcmLQZXQODAtP-fJKcsuTaVj6XfYcYJyhSs2XABNP1MmgkhX4BUe_HaWMoBlQwVBtephtbysILZZ0I4TVDcbjJZEDOw5elQFTdcKA8PLt4dC33a-5rgYjUSjwNwctwYZ_LYXBvrGKMMuaHkecWQ464nnLFtxaYdvGZj8t35qmoVdUIg3g99yNqNMo4oK22U04RypENW1ZeOPd75SV4ECjcmCoXi7dXNN13-OAnaE_DlO_SzpXo0-9Sh5DsaxJW00HBsZNQkocv5j7OlxjWIZHZiJltKuhnI3fG85ii3RbGZ3R_htGbxkrcXk9ct4vRMU0iQwW45K_KbVb_3pJWoM962r85IQPqZbcX_fX_MEwC8RnxTE6jOgRG8F-0NpCoGyykO0-_Dc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3fcb2949cf.mp4?token=d2mZo952KSiSdcGBy20rXe96sMnbvPlbOT8fYxKTRAboNuRC-z7rpbcSuSLFEFGwDt4DMgidr3u0v2JS9mqcpbNmeofpRRWJ_hMBUTSQ55dYrkH7yprVygKveTCog-EI7TJqUZarYXa27vwwe4_-tv4JQx2kOjFTnxG0Z1AIjP0nBVOEkMSQPnVa37MmMU4gNUNZv-CovPbEUCOVjLBdg9umaWJJAW8plWoJiLjAYGtsfHAaef4bGBnAbkaLqORs77lCLylTLUHR4WkCex-UgrMu1iqk3t_vIUOJcmLQZXQODAtP-fJKcsuTaVj6XfYcYJyhSs2XABNP1MmgkhX4BUe_HaWMoBlQwVBtephtbysILZZ0I4TVDcbjJZEDOw5elQFTdcKA8PLt4dC33a-5rgYjUSjwNwctwYZ_LYXBvrGKMMuaHkecWQ464nnLFtxaYdvGZj8t35qmoVdUIg3g99yNqNMo4oK22U04RypENW1ZeOPd75SV4ECjcmCoXi7dXNN13-OAnaE_DlO_SzpXo0-9Sh5DsaxJW00HBsZNQkocv5j7OlxjWIZHZiJltKuhnI3fG85ii3RbGZ3R_htGbxkrcXk9ct4vRMU0iQwW45K_KbVb_3pJWoM962r85IQPqZbcX_fX_MEwC8RnxTE6jOgRG8F-0NpCoGyykO0-_Dc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">🚨
گزارش انفجار در آبادان</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/farahmand_alipour/6247" target="_blank">📅 16:44 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6246">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fcKCVtvDuAWqqNUe4JdUoK77Yq2D9LX-QZxyh9_2IJbF38mFlTEMG3DoQfjWdCu5crm7-xISyrxHcuM2pcKjSdCBMpYUrePz278_6wXZCKvzP-Ai5nautYpqLqHxkSGffv0EdXQzkepCC1lYsXxdYox1VBjntHKXCwNYiAh3tZmBUu_ln5bk8E23MJDs0SysFRwME3IHOEfIe68wFkQ0c_ZqP54Kb6nr51esLLZ8tQUB45Qd3HGJiED5VEhi7WlGr3lfRxqbhyL8Cq9r1jsuB5fmO39dR2kMKW0ept7uOwP9iNzAuDLviUPZ_oCs4krvNIxPC_0DdjuOypvdTMUMLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
اردن : جمهوری اسلامی با ۴ موشک
بالستیک به بندر عقبه حمله کرد.
۳ موشک رهگیری و منهدم شدند،
یک موشک در یک منطقه‌‌ خالی از سکنه افتاد.
🔺
عقبه تنها «چند متر» با شهر اسرائیلی ایلات فاصله دارد.</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/farahmand_alipour/6246" target="_blank">📅 16:34 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6245">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v_x8kRtOCeUGxEsHRiix4x3F1INWeORt-K1QFlYukT2IvGTq1Zn-PkE31nQTPSk4_KlgfKJ6xNFq2i6A0eRTtGi-TuQRJOFME5dQJwrxjtG51lQ8gsLmm3FIdD6se-FHYoZ9sZexAdMlfq08ldLAikT_HlkmeCxDseUD_azsveHCeuQ6PfkIoZthahES5GHrPVM5VxA0IyxkbvaV9bkFm08KAMTinHWeisqvvdftZtWWMDsdD-kHhRUYBXEqH3zklbaFTOlx0qicUkOLPSbdfHtIqixPedAzREWxASniZs3RuIWEaXJAwJ3DstPeJJVV7pyIFdGgocUr0ue-jhOiXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هر روز ماندن جمهوری اسلامی
هزینه برای ایرانه و فرصت برای ارتکاب جنایت</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/farahmand_alipour/6245" target="_blank">📅 16:16 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6244">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">حرف حق :)</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/farahmand_alipour/6244" target="_blank">📅 10:41 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6243">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W1HzStMv-nV9m4UZKCyqW9OIiXWPxWqerC8p1Pzf39shOve6VYxQOYW7hOn8UYQ_l6qEaAsy4k8hit7mqB3S12Hd6YmfxiPnaRf2lfLxMQGXYq1tVQly9yKqmjPhbFJ_IQetAfNlEsynUFflOaE_P5YE4fSRHRC8SF5dJFoRIngUoR8VGbdxECFuLVKrK0BiLl34fT2fgDxLiIVyETWq13ug70NP2fNl22MHLiieH-IxnoWV1XC1bdf_u0gN7G9cgmxKYkDH2vbt71fXc4yH90l2QuPHEgR7W56XuUZEBU-kcIoYT-l24MaIx2ETleqAjsqaBz7c5MaBIMUSO_Kvgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏خاطرات هاشمی رفسنجانی ۲۰ آبان‌ ۶۰ :
‏«شام را با احمد آقا و آقاى خامنه اى صرف كردم!
تصميم گرفتیم کمتر به كشورهاى خارجى فحاشی و حمله شود
. صداوسيما هم كنترل شود.»
https://x.com/farahmandalipur/status/2078615489446543468?s=46</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/farahmand_alipour/6243" target="_blank">📅 02:31 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6242">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">🚨
چند انفجار در بندر لنگه</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/farahmand_alipour/6242" target="_blank">📅 02:12 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6241">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">🚨
خبرگزاری مهر : شنیده شدن انفجار در کیش</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/farahmand_alipour/6241" target="_blank">📅 02:12 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6240">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">🚨
گزارش انفجار در اهواز</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/farahmand_alipour/6240" target="_blank">📅 02:09 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6239">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">🚨
گزارش حمله به بندرعباس</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/farahmand_alipour/6239" target="_blank">📅 02:01 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6238">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">🚨
گزارش حمله به اطراف سیریک</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/farahmand_alipour/6238" target="_blank">📅 02:00 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6237">
<div class="tg-post-header">📌 پیام #1</div>
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

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
