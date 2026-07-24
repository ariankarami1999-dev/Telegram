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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-02 15:28:59</div>
<hr>

<div class="tg-post" id="msg-6341">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">سپاه خطاب به مردم منطقه : فورا تا شعاع ۵۰۰ متری از محل‌ حضور آمریکایی‌ها فاصله بگیرید.</div>
<div class="tg-footer">👁️ 9.45K · <a href="https://t.me/farahmand_alipour/6341" target="_blank">📅 14:05 · 02 Mordad 1405</a></div>
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
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/farahmand_alipour/6340" target="_blank">📅 11:25 · 02 Mordad 1405</a></div>
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
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/farahmand_alipour/6339" target="_blank">📅 08:24 · 02 Mordad 1405</a></div>
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
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/farahmand_alipour/6338" target="_blank">📅 08:03 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6337">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZMTx5dkGl32RMhG-1Hg_CtPAzpfVN27SicsOysr20M_aNLCquCTAtN-gFSbLC-onlxVwNmJMrlK0xifEzyk2wsUcaZW0pUF5FTYD0dJeuty-EFwUlZw5PYG9eQ6oyuaCWjKTQ9tOF4xI8uVayMzIWJhXhpZVLc3Zgi0V1mtIuxuGNfkk3n2KFE5zQBIix0FYskm02ZBXZ4FHoogqjFTyyp8KW2riGk3IG3Q6J98oEE0zNPingE_KCVaCHOXuCMLV4YEta8rNetg-zCZ18LGrjZPGH-NrrFfxsBJlvjhpVY46okXIEx12oo17GXcpQYvzP67av4_q4eoNs3lJ5O83Gg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تهدید تازه ترامپ‌: از پولهای بلوکه شده ایران، خسارت کشتی‌های آسیب دیده توسط جمهوری اسلامی را پرداخت میکنیم.</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/farahmand_alipour/6337" target="_blank">📅 08:00 · 02 Mordad 1405</a></div>
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
<div class="tg-footer">👁️ 23K · <a href="https://t.me/farahmand_alipour/6334" target="_blank">📅 22:52 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6333">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">🚨
ترامپ به کانال ۱۲ اسرائیل: در حال بررسی یک حمله گسترده به جمهوری اسلامی هستم؛ حمله‌ای بزرگ‌تر از هر اقدامی که تاکنون انجام شده است. به تصمیم‌گیری درباره آن نزدیک هستم.
او در خصوص احتمال مشارکت اسرائیل هم گفت اگر از آنها بخواهیم ظرف ۲ دقیقه آماده می‌شوند، اما برای آغاز عملیات جدید به هیچ کس نیازی نداریم!</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/farahmand_alipour/6333" target="_blank">📅 21:56 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6332">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">‏هشدار سپاه: هر پایگاهی در بریتانیا که برای انجام حملات علیه ایران مورد استفاده قرار گیرد، یک هدف مشروع خواهد بود.
‏واکنش سخنگوی دولت بریتانیا به هشدار : نیروهای مسلح ما آماده‌اند تا از بریتانیا در برابر هرگونه حمله محافظت کنند.
بریتانیا به‌صورت شبانه‌روزی و در هماهنگی نزدیک با متحدان خود در ناتو، آماده دفاع از خود است.</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/farahmand_alipour/6332" target="_blank">📅 21:24 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6331">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OGDYdVfLT2yjxfrmqpU3DMHcE56lmQ4Mld9YSZbGVAIVUtXMrU8ZVIFHU9d4hVRalJIzgI9QwyDmxKzNbc3uksUYLSZUC3ZFuQB7CNKWcpA-__ZT4CidkjrGi88IY2s-qodYOScUyejpnkGisClSI7MwwXW1tHeAi6hDyoHQM2azpN0uHPKMMlZRbYwePfI35esvvmvEFIpC_jKSy2rb8ezcHOaXSwgRHqzUlF7ZRX44do5uAQ-XGaOU81xnSQscg7rHtmw3qv_VicMLhhiS3Ye5N6lxDd72wv7RgxAUfvFtaJRbmKy1J4FAZxX8p3WAmJMZoCb-SiaBio44sTsFTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ضرغامی : فعلا حرفی از مذاکره نزنید!</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/farahmand_alipour/6331" target="_blank">📅 21:22 · 01 Mordad 1405</a></div>
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
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/farahmand_alipour/6330" target="_blank">📅 18:37 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6329">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/InUHe-PMLaDx2K9scrvuaCEE5PMmtEv8j37YKAZSFPQeYLWt5YaapkpmI37vouvGii24xDzgum4OdblYGtxXTrlyaLSj43f92Gty6MJln0MGdUxbl5IuZHZ-55D4-C4ZWxwsOu5gjXAoi9bgOp2ekfoGhslblobMxPPOplyoD3PDUfcwUbiELl6XSFaXyWUylQF32ZfInLOY8kc8cBPOQetViZ1avsB6gkpL4WwI_WFBGYsINNYt8gkxhMLZdHSyixDvYj-fmHwes7mJ-0aKPfCDkcc5OxKC5-6PxfGhzj1CVxuSCV4r_dGWSBANrPwcUrmvwCMoEdLRm2fNoSBBgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قاآنی، فرمانده سپاه قدس، با ارسال پیام تبریکی به «خلیل الحلیه» نوشت: «آنان با انتخاب شخصیتی که نماد مقاومت و شهادت است، بار دیگر اثبات کردند که همچنان بر استمرار مسیر مقاومت اسلامی تأکید دارند. مقاومت اسلامی امروز قوی‌تر از همیشه، مسیر عزت‌مندانه خود را ادامه…</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/farahmand_alipour/6329" target="_blank">📅 18:07 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6328">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IpDfhuwUVA7D_vukw--punel5VYWFSWuPlGiBExSYEj--tTFv4eUzPBUX0LQiX_fcPh8G6V9z2nEac9WJzaC-FmE6hFPbLv43Yiz958Qjro4DN7VGFAjTLJh_m8JyODFYYmxAs7Ndio3phyQMKwfIaVFo0lPOpakaRQHWbniwzOfmhex0vrgFyLGvu78C3MAiXupDtA3e6yVXnIQBemQInE5mcqzH3YzNUVZD_CDhL8rHsNCw5YvKr_1CHbf5ul3PDzMktrqT8yKnXB1auS38vTfuLTb8DhGMTPAl9U3pCZCAGfh6NTHF8O5OxL_cAKFcZvZo6m3fU6jmjZQZDl0qw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/farahmand_alipour/6328" target="_blank">📅 14:57 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6327">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jfKoV0gTyaCZcUulO6eoMt__181eK1aDzHb7BK9cGQS99Dg907jlT9LXBT2HG0ku32WOusIa_Pj6dOzPabVq0SfCCFquY8ER9KrYh324K6YBX5lYyOKj1HW1lWw_7FEn0AMO4JDzgK7cl5GEUfqMbOGfeVT950G2Psl81WBmNQKy46XVCzBREiCoZfDQ6MmCBPATf_YeGfNcCo6ZvsTK47L9NQG_udQkI37tJ58L1Dk1963XZFgpe1B43bixT7i3WLbQ3efeJBeJlNkR4GhgNJoudo35qIxr7QOSJTo3tdK_D9i6QF-1ZxU09Fig_NlegPDytC2Gz2ULTFlUicMwrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/farahmand_alipour/6327" target="_blank">📅 13:46 · 01 Mordad 1405</a></div>
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
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/farahmand_alipour/6326" target="_blank">📅 13:36 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6325">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z5e6gqbtaiqMLDiAyunn8kGz9PU50p1SfNlg_8YwUXnAziW7g5Lp7WuEV5a9co26Z1tjMHKfOd-jvlLsX8k-g9ROoEIsGtRNc8Lf83BK5pGAMM5BjkAYVVc56kJcvr6IuD5E8uZuuhLcs32NzfDixg3y5JIWR4Wa_dsb817afol8ynVHpT446yvtiN5t3dmmIpcgmITUX8IlNT7DC3coSXOIowRxQ6s5-Z6deNba7QHPuacfbzo5xMwFImI4EegyokZOGZs4S7x5pZK9_0PgJ33_0M3hNeKd44zIQrwHj0SqAvil4VCQxf2oNAvbm3b-c2hApfwDttlBIIRhs4SVxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارتش: مراکز و یگان‌های آمریکا در پایگاه‌های الدوحه، علی السالم و عریفجان کویت را هدف قرار دادیم.</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/farahmand_alipour/6325" target="_blank">📅 08:58 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6324">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bTHIgkHMBtosxPvZiC3SVLcM4JjB-s1SDYb-XL-Ut7EOn7x75dLWeHsHWUiGWxgqIoJZMiuAbduDLB1Q2J985B2rW8Mdk-vNnCPkRGMBU8jZDKPeLPvKCqYs9qHetJNk9rJXT42fqdTTsZrhVyu_wadx2ZjeLwGxzXVxP5EVVOU2UbWvCnRwJTjNKaDhuGdRRrH7hjLv37_aZBIT7ipigvoYTU9BOoOJA1-K1Bd_fuFDItzT8RkC3kazTAZrQpsMtZrSA7YjU7huf9dSGPJvhn0373xlQtfz3NDETvkfeHGVkTTGxPC9bD_t1zg3m4vSNZkUZyNUxh1aG9gL88yrmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در یک تحول تازه در حملات‌ ۱۲ روز اخیر
و نشانه اینکه حملات وارد فاز تازه‌ای شده.
«بی‌ ۱» برای حملات بسیار سنگین و عمیق
استفاده میشه.</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/farahmand_alipour/6324" target="_blank">📅 08:48 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6323">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">ارتش: مراکز و یگان‌های آمریکا در پایگاه‌های الدوحه، علی السالم و عریفجان کویت را هدف قرار دادیم.</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/farahmand_alipour/6323" target="_blank">📅 08:41 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6322">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">جنایتی نبوده که جمهوری اسلامی
در حق مردم ایران انجام نداده باشه</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/farahmand_alipour/6322" target="_blank">📅 07:56 · 01 Mordad 1405</a></div>
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
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/farahmand_alipour/6321" target="_blank">📅 07:00 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6320">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">🚨
در جریان حمله آمریکا به مرز شلمچه ۲ نفر کشته و ۱۱ تن زخمی شدند.</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/farahmand_alipour/6320" target="_blank">📅 06:57 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6319">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">مارکو روبیو وزیر خارجه آمریکا : جمهوری  اسلامی تفاهم نامه را نقض کرده و لذا دیگر  معتبر نیست.</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/farahmand_alipour/6319" target="_blank">📅 06:56 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6318">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/65da400742.mp4?token=rT4uzI0IVXhYv8yweDVKBbaXqJ37BXlFsWhOh0ZwZKSMCZDPsC1mJKnghkiZOnOXKkdUUr1yK1583rFmCNxuY1z7cBWa7DKCoqbh5LD9RXz3_Z3bX34LqRcq3eHReEmtrWc3X5bTqv5FWGMQ4D6PQsVs75GPdYUIELLzAibWL5gHugAYBr25L7Bn4rIev67FX0-eIhmYnpY8FXCKEHXaz5tgCbjlk6KaukZuqSnrX6CEoqa9KN7frcUPeKp5tmu8q4PCXIMufxrG9HApTEe2qqpP_Ui2M_MgouZqE3uuwEAQqdOdW89KtqHacLTvR77daAvLd4poWx4WwGzf5Bwadg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/65da400742.mp4?token=rT4uzI0IVXhYv8yweDVKBbaXqJ37BXlFsWhOh0ZwZKSMCZDPsC1mJKnghkiZOnOXKkdUUr1yK1583rFmCNxuY1z7cBWa7DKCoqbh5LD9RXz3_Z3bX34LqRcq3eHReEmtrWc3X5bTqv5FWGMQ4D6PQsVs75GPdYUIELLzAibWL5gHugAYBr25L7Bn4rIev67FX0-eIhmYnpY8FXCKEHXaz5tgCbjlk6KaukZuqSnrX6CEoqa9KN7frcUPeKp5tmu8q4PCXIMufxrG9HApTEe2qqpP_Ui2M_MgouZqE3uuwEAQqdOdW89KtqHacLTvR77daAvLd4poWx4WwGzf5Bwadg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اون بابایی که با نخوت …</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/farahmand_alipour/6318" target="_blank">📅 22:41 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6317">
<div class="tg-post-header">📌 پیام #78</div>
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
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/farahmand_alipour/6317" target="_blank">📅 22:30 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6316">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nVbLnpORzpKj_SKlWzTRz8w821_UypUKFAe0hhewa2KyrERNFdATzIW_mIphqrWbUa6hMrIbH9YH60DsYdNGObwa6vEZC6ksYEfHQdeDYA0E9ABc4OC4a-QOgAaonhVyTAFVnX6w5X9Jz0OLGxWFTxGDLBrT1-N6WfdXw99BYCUebKpfsULryvi_fe7M4g48liHL_2givLLDHFWDSQfqwjyA4PdaEZ1bw6M5D2sKPVAvsXPbt4KpozbZ1nrTF26kgf-5d5FgE0S1thRyPnET4yl7SOiHVcKl1SBsfORwE1B2W5yUUPyNK_0FT-FWMHk78qiPWnGI4MwzM0Tl-nQ8lA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏سخنگوی سپاه خطاب به شرکت‌های کشتیرانی‌:
مسیر مین‌گذاری‌شدۀ جنوب تنگۀ هرمز  [ آب‌های عمان] مسیر نابودی سرمایه ی شماست!
قرارگاه خاتم هم دقایقی پیش هشدار داده بود که فقط از آب‌های تعیین شده (بخش ایران) باید تردد کنند.
جمهوری اسلامی رسما آب‌های سرزمینی عمان رو هم ناامن کرده.</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/farahmand_alipour/6316" target="_blank">📅 22:22 · 31 Tir 1405</a></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/on6SFY6lWOwMj5wYTtp11YTD9CJd6OfOZvllwMLOf_xPKsBuhi9ngwJznEM2IuDT0r3xNP8ddEv08MLc0fwH1jR1NlQ2r13y_vqliVxpCpQYWWeVYmNyK6tlII60OdGIX1eRjNMi6L9ougZeGSNvYydvWBBfs_N_GNhZ2hfVBUZRZDv3LxR-SgBFTbPTXS8cGLf83rJTZ-vGpTdksaLbp4Kugxe7NE3XeoOpR9uJN6bNJh_V75vx3_P4ZChePlaYcWaLW2ffHyYAD1miz6Tynh85sw0mKF9t_sJ2bje9iSfnJK-jIXB28pI3V4km83t2ZVhisJAgOLERKVmLyimVUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
تهدید ترامپ: کشتی بزنید نیروگاه میزنم.</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/farahmand_alipour/6314" target="_blank">📅 18:06 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6313">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iI_jMfi0ryd7cRLq_MVLVGTaDFoXhXfeYdd8z1G0byPGlQdL8Zadgt4Z0q4Cljz-H4nbn2Tm1-K4dIW293ymv5lo7K-pXpN-c5XKIf6Ewq19DDbxd1D3NcGpV0kx9DsYNQ1nXFc5FFaTnqGY-zuotKk92svkS1ZG0cJblxEl_sWbfLU0kVjOJkawE9NHsSMSkb1LsxRJJy23_4tGzr0Zj3XgOoPixPf_Bv6Ga0uJwRFHd_Ju2H6nmcMNBfGjfQghMwf4WMnzef8-_Zupas6ixhS3AP5-TR-ijj3A7kkefhwdqpjxpDqzhYPuNPhKojkhWVNsY61J9-ASfbrZV7aEog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
تهدید ترامپ: کشتی بزنید نیروگاه میزنم.</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/farahmand_alipour/6313" target="_blank">📅 17:20 · 31 Tir 1405</a></div>
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
  <source src="https://cdn4.telesco.pe/file/9577aecbb9.mp4?token=hvCEktMEsdRqUIi1GlXt7g8chTzwwAxAphD58Ony7PkDKW4ugNdzN9I2QDi7MX7PFLSnjg_kdfknMSUNO1gn0NRyiuFar1XiACbaEjSTtsIhog3myvq6Be8Y8aHmTnagyn5KmbN-w6ZVF2-cOhRoq2I7Fclj96fvYhbvk82hyebH-bfjeHIPkC_uYBbyXuLRdcPKE-0851MKvzWA585a_WJDcvgnKYUKSaeyW02lXCUNYh_3QNorY_ux-CEtad4XTdz73Mu7xYgv8TepQc-iXGHMt5m_aLatHwsysPWUBINY6pXFTWoa52DxQi7AVG4bqUkwEl-If7MmrgDK39TZqw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9577aecbb9.mp4?token=hvCEktMEsdRqUIi1GlXt7g8chTzwwAxAphD58Ony7PkDKW4ugNdzN9I2QDi7MX7PFLSnjg_kdfknMSUNO1gn0NRyiuFar1XiACbaEjSTtsIhog3myvq6Be8Y8aHmTnagyn5KmbN-w6ZVF2-cOhRoq2I7Fclj96fvYhbvk82hyebH-bfjeHIPkC_uYBbyXuLRdcPKE-0851MKvzWA585a_WJDcvgnKYUKSaeyW02lXCUNYh_3QNorY_ux-CEtad4XTdz73Mu7xYgv8TepQc-iXGHMt5m_aLatHwsysPWUBINY6pXFTWoa52DxQi7AVG4bqUkwEl-If7MmrgDK39TZqw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هگزت وزیر جنگ آمریکا از ضرورت
برخورد با جمهوری اسلامی میگه
ونس، وزیر خارجه با ناراحتی به او نگاه میکنه.
(ونس طرفدار گفتگو است)</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/farahmand_alipour/6311" target="_blank">📅 08:28 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6310">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oimr43V0fDN_DLFQaVfVQ4p_p3IuMkTOm0HFgCoyVNV7yp3nN8y9du8Fl3Jn813ofDJ1-MRSZcAwULeDUujAipv2l0-hRcC398PKNSd9s3dVcdgP_jECndOGT1fKFoNwF26Qh52twnrfBGliCXEDcM-Icv5OaHtgdojvsbRdsfxKddJ_mNHM5E250qhhFlU_QW67KPSOIDNpyGx2EiCK1fvTXnVAXDh0FWfcB9JQgdg_Vz8vQNdDNnL28scVM5h4ZVnvptOtSOv1YYGsFpe2dRx32xrOsx7EL7fbS0jPaQcfqR8RfxU5mK8nMiqtSX5mU0fSO-qTowZ3o85vElHdYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
اندی برنهام نخست وزیر تازه بریتانیا که از دیروز در این کشور قدرت گرفت، با در اختیار گذاشتن پایگاه‌های بریتانیا به آمریکا برای حمله به جمهوری اسلامی موافقت کرد.
پایگاه‌های «دیه‌گو گارسیا » و «قبرس» از مهم‌ترین پایگاه‌های بریتانیا و مشرف به ایران است.</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/farahmand_alipour/6310" target="_blank">📅 00:52 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6308">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/J8WbLN56Y3nfV99QPYFF5Gksp3tisuPi-XLpcCn_lotrLge3gtJRt-dsFgT4c8eLEWXVm443qrd5tEkoiOOEX0Rvpvw0ZPBYhZt0zHBnCfpi_udy5TKvp6dPGYmBU4T5k-NOnUVRiIhTE1t4rE4ThrPeC1IgxYGRQl9xbQB7e6TAQb4_HxYZrKLsHT1F-7i_TRta21P6LCpcx7OINlvox8osSbvEaUhtZbRBmE9E2_VhMID433lm9gZ0Mnx2RiiKgtAeJN3fsS1C4WTrI_-z1MMyGGXoEDkb15tGaf-422ilUpW7ZLeq_7c7GRwAfRQHyirE-1Qw8fcDuFskpop1GA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ds-qnPLWEaRfgvKnMqRTsXEEPMrtvCuWCe0gb9aNJhO9fbshmFih2z3n5OAGX9HZIEqGrC0v5FfFzzBU-Xu9VHyW_HNtcbR7ByAAGt_bTLtT0P4F5VlmlmUcdDalGTKs3K8XLLbDVtlem2_5Lc0NAPNFpdVNEejSYUnSI4WEljauxefQHv4q4N18smjUI7gnFmsx5mHbTecCE7ikJSoqvThVi2pIFG5xo9-9F7iCnDksI5ab4pwKX44qXI947Qq1bCfpi408ZEvMZJut_ZgbYUa2GYb4yofbQ7WeLevodFbYWeKS1SB4yQxcI2vE9viznXlPHyzYyreqEcdyIZMTHA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">حسن روحانی رفته خونه لاریجانی تسلیت
چهره زنان رو!
بعد همین ها میگن اگه ما نبودیم داعش می‌اومد توی ایران
داعش ۴۷ ساله که در ایران حکومت میکنه.</div>
<div class="tg-footer">👁️ 30.5K · <a href="https://t.me/farahmand_alipour/6308" target="_blank">📅 23:28 · 30 Tir 1405</a></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dy4IbaW20HVpfesQcVPUt9QX1abcoaQmZQZGyJcmFk9nDc8Xg14KrUkaJ_SZzoUJb9e3Arrs-IskIntHbsiJOPgF9AcBZRMCJLIkLH7wLSEABEVZ6yCn1TfcPgM2cWSmeo0w7_ZhpuvP3pGMQtVMJvj_tZp7GleoPFiaJjG58C-kCP4kpVOFSYuVA7UxAfEXV4zqoR1avCVdZG85muuSx6X8iNB42_aFVSBc1Y5TrZ7l4K35Qe5g1mEDWntDcl8W4s1oefjZkKpd3hZlKjE5UUPVnDakIJ8iR-7C6IrxQJwz11fWm7rh1crV--kWdMXLKbs57aL3mzmt-XkAnIw19A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #66</div>
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
<div class="tg-footer">👁️ 27K · <a href="https://t.me/farahmand_alipour/6304" target="_blank">📅 18:49 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6303">
<div class="tg-post-header">📌 پیام #65</div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TdBFJqvSj4dZMRj6RqZFVyBI07C8E3ZBxTH97Tu6YiTMqsetjmvPit-Rwja68TbynuzekICIBQBQVxUUNXA8nQaFflfVbpXgnctTq23kJAkTlZkbPOyWRdUSijKAN-WZsQg1oox0GPofc2gvXUqO_HLVXKYtql_M42G52oMMJCJX6msFAY7tgAItu0jSviXyiVFgZHstyNy5PH2Nuz7LQql8yrEIFvN9DQ2kQfJfPlZwWSGyqECjfKWVtBFi8gRlw2HKAehJaYmH_xnSiOqZ8fAzLmHZoxu3wHtKkjl_PRE_I-xNYLOgpGN8LquKP1PLjCA8wn8R-mskD1Zbe6ZqMw.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/46c8806804.mp4?token=PdH1WNqAbWbDDhV0b6GYkfm8jba8q204FIM69AU-EFeTCvBsrlp48K2yzYp1c9BWiQlQAZbuY9HAgcldaXebmi5_sHGs6r6FGrw9I8mUHYLK6Ka9vlAnXEYFKgcULiqadv9WtCOauAou8dpc1cwjWY-mspG21u5qecegHRbKhX0wGy3wSsslHp-TmaTXZ5ZcBap4uthbow1nrqFAtoci_aCp7LuUL94EnMuf6u5stHHTWTaMXm2smFiVNNTzJR5v-o4GmUYu_hYOKIyKn_bkPsYEionbkJlpehPVcC6HOkwfPYs4KMOW8oFnmhpdoXYtK1Xu9IGreqRGrl_F2q60Jw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/46c8806804.mp4?token=PdH1WNqAbWbDDhV0b6GYkfm8jba8q204FIM69AU-EFeTCvBsrlp48K2yzYp1c9BWiQlQAZbuY9HAgcldaXebmi5_sHGs6r6FGrw9I8mUHYLK6Ka9vlAnXEYFKgcULiqadv9WtCOauAou8dpc1cwjWY-mspG21u5qecegHRbKhX0wGy3wSsslHp-TmaTXZ5ZcBap4uthbow1nrqFAtoci_aCp7LuUL94EnMuf6u5stHHTWTaMXm2smFiVNNTzJR5v-o4GmUYu_hYOKIyKn_bkPsYEionbkJlpehPVcC6HOkwfPYs4KMOW8oFnmhpdoXYtK1Xu9IGreqRGrl_F2q60Jw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/farahmand_alipour/6298" target="_blank">📅 13:16 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6297">
<div class="tg-post-header">📌 پیام #59</div>
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
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/farahmand_alipour/6297" target="_blank">📅 11:54 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6296">
<div class="tg-post-header">📌 پیام #58</div>
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
<div class="tg-post-header">📌 پیام #57</div>
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
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">واکنش نیروهای مقاومت فرانسه به رهبری ژنرال دوگل به کشته شدن ۶۶ کودک فرانسوی بر اثر خطای بمباران متفقین در جریان عملیات آزادسازی فرانسه از حکومت تحت حمایت نازی‌ها @hafezeye_tarikhi</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/farahmand_alipour/6294" target="_blank">📅 09:31 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6293">
<div class="tg-post-header">📌 پیام #55</div>
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
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/farahmand_alipour/6293" target="_blank">📅 09:30 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6292">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3ba53f516a.mp4?token=tT5H8zIEYl5drMNWGrjT-4c7dzc6X53IHjgttQq7np5oebandvrLl5L5rGK72zdxZBGNEbY0SN4iA15tQ33jRvV3vKvP8YNVhfQtCfXi4ZZu2fWLfoNKJy-f3JGKT1eEjdgOYDRRTQsxgGvrXHKpGwRZIrdxHvLvWFc6lHKOvUCMRUu0BAM_OEzbRA0LUkJTJcYqeRGzLxiyiw5fldeL9qKDZoGZpk4Ug6RzZJq3nODxHNZQsOc8Pg6i2SRxa8EZ2mUDkJdeoZzXcZjZeYVz98_86oT94zmlLRypOiA-tf5f5ruQJuK1gKK7VGRzHWGCpqvS2DoF7kEo1WpEANXzUw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3ba53f516a.mp4?token=tT5H8zIEYl5drMNWGrjT-4c7dzc6X53IHjgttQq7np5oebandvrLl5L5rGK72zdxZBGNEbY0SN4iA15tQ33jRvV3vKvP8YNVhfQtCfXi4ZZu2fWLfoNKJy-f3JGKT1eEjdgOYDRRTQsxgGvrXHKpGwRZIrdxHvLvWFc6lHKOvUCMRUu0BAM_OEzbRA0LUkJTJcYqeRGzLxiyiw5fldeL9qKDZoGZpk4Ug6RzZJq3nODxHNZQsOc8Pg6i2SRxa8EZ2mUDkJdeoZzXcZjZeYVz98_86oT94zmlLRypOiA-tf5f5ruQJuK1gKK7VGRzHWGCpqvS2DoF7kEo1WpEANXzUw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">۲۱ ماه پس از کشته شدن «یحیی سنوار» رهبر گروه تروریستی حماس، این گروه «خلیل الحلیه» را به عنوان رهبر جدید خود معرفی کرد.  او در رقابت با «خالد مشعل» موفق شد این پست و مقام را بگیرد زیرا که بیش از خالد مشعل، مدافع اقدامات یحیی سنوار بود و جنایت ۷ اکتبر! که چیزی…</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/farahmand_alipour/6292" target="_blank">📅 09:15 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6290">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FZXgkvFcf1JhLCtxwtDyzKpqfsQw-r30EQ6tim0przoRN4YHjAY7fbxSfOegcDMvXnVWcLLxpw8WyFe-vekecx2KTSrA0KcWA5NTjlmLYvYLbgwoDHczBd0urdN5nbOJmZHtKXPl4ULymsQ9hlCTfF6TRPIKCiS5YDwrpJeki-YZiD5ieSQwmhzHsVqsKpeYVAdFaQGSNTULl7m-JXzetSqp4yc7wjT0Eu8kddrsEFqU5EbdKJGWHRtHL5RYknq7Wbr1YNbBPDYElEoL0khjuabbkJtM7JkL7ZZpbf-oEkf8_faoJTKSNx7H2nywgKMysJDyvnHTi9W0I6rssu79cw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۲۱ ماه پس از کشته شدن «یحیی سنوار» رهبر گروه تروریستی حماس، این گروه «خلیل الحلیه» را به عنوان رهبر جدید خود معرفی کرد.
او در رقابت با «خالد مشعل» موفق شد این پست و مقام را بگیرد زیرا که بیش از خالد مشعل، مدافع اقدامات یحیی سنوار بود و جنایت ۷ اکتبر! که چیزی جز فاجعه برای غزه نداشت!
تصویری از خلیل الحلیه، رهبر جدید حماس با خامنه‌ای. هم خامنه‌ای و هم یحیی سنوار توسط اسرائیل حذف شدند.</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/farahmand_alipour/6290" target="_blank">📅 09:12 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6289">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MzvRawHvNcVs2UwPa5JYct0DIDu57AC4VDJ9-JTDeHZnhYGDPmoflLmXWJlsF7AG5g4hXGDJlGNIVCuBBArxvj9VimNGaavDxIjqwsKp9YYDwnB-M5yTS8F11FA2iw9UDhA_ba8VqRF8rxWwkB9yo1lAYix24VE0POrhc1zKKPdoGJ7Ta3wO_eXYduzTTM82HBv2rI2GaKWW8Oya-HJBvXBGAV7qB3PEA0ei0H5sTivhnhUyHas7ug2h9yQv6CFaoX0Mcv3uLMRBj4xxAvM40C_ahfs0C-eN7NxZjMtwr6fYmu2sr8gKmFmFBZLsZtdBGrxQV3DssB1wL5ZJ6wF8tA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/farahmand_alipour/6283" target="_blank">📅 00:03 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6282">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oAqBQOWzqxsg5SuxlkeArPwaTVpm22MsHZBmiKPoK0mNXrm9JEGv6SOuxFSgvOd4ZkKkPwxlIK53vXHtDmfRWWGMmH3XiaH48Wk5qWMtUh9DTNAbzHvZHovYfjCqCw0DQs6ic2P-yG1bjs6_GTUCFYbvJLDO731oY25Dr82pQMr9zKXYB7yWyFIIqY4cOSSG6-rQ_aAX2QrrzOCNEOblF0IKztZkl1Tb3pOF1Ar0MvMaL-lfJBw7sI_KzjL517hmx0xeomWzQnMmhaV3qMsRop_UUiLVacmdNJLJVFWAGFKfgrwLfq6SI1-LPHcqLTKtimx9S3bZS7ceThif4BXRFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ :
اگه قراره کسی دستگیر شود، سران جمهوری اسلامی هستند.</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/farahmand_alipour/6282" target="_blank">📅 21:09 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6281">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AbQvNkqehP34QuwfBBtCW4QwIDORQj-mZ2ekNKI-slXuN04CUezQ9OP3FL0DEkX4nhOzHtyvtwmK_XEw2-Ome67LoPgyDexvQLTDdDiW-tlbcXSHLATMakGKQ3Vt87j2sTpUqYGws--tQCbD_tl1vOMgDCAj-KYWDS1RpqDiwg3NPSx4V5Ej-zAxDVkHIUP9gtSbzlbv03GYNH_j3AWElGXmlzMHjyRMB_IYbs_h3Ah6oYY6-OsD3tjWlLD0VEbuUMib_ODaKrPiqJ3-JDX4XI5HI-jl_-xCOYMkW0ZkJsWeWlt3SXWW6uP1B5Jmalu7oBR5ARPCxrWFDVHgJfUmjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حمله جمهوری اسلامی به یک کشتی
در تنگه هرمز</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/farahmand_alipour/6281" target="_blank">📅 18:12 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6280">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PHuwTn5Y_C8OA0n_0kHf2nAJ8aWN7m-INxpJFtgbeAT0dTiqFM5eQ-Q-DftVUUH1ocPr412uyuS6YyR_f94HG961TYMGERRcvfxomCsjecBw5dlsObgm22ZAnf6nuc4_CX1QAR0xKaWNbIndqv55rW4QZ148ANbqQFdZ2bpBhHuPnzQ5hnGA3Sl3xg_KiSW6KNe9dLvkIbf7v8h2GsNEemR9lyInRxuxjHR4dX0_sG20E2jn0gPQZlIysET58fHzNVB6KH2dgNwU0ikkTq_hkaV30krvB8haTY67cwuyHNF2yL1kPDRdO2BYxSPpBcOqDMQKH_7qmY0LZa0Jz_0kCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
گزارش‌هایی از حمله به شیراز
هدف: احتمالا صنایع الکترونیک شیراز</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/farahmand_alipour/6280" target="_blank">📅 17:53 · 29 Tir 1405</a></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QdpPV7_8BsQhBOR7i8OpJlaTnBluWCzz_61FcQ-OA4TSURoNt4FlJyLzg8G3z_BrjOGDIWTpz_zXFmFY0Je9tA6-SISXnp45ldKhxZrbzKHQ6LMpWSN-ptlpGGqOSkQ_O_NtulBlts4hk6E53bNzLBFTucb40_3-aJBB7xgwLjwJUtk5-fUWfzN0S2ZwVDTkjnOgqYuYH_fd3r0bBWvOgtRV2xrlYdxBNfrMIXo3lHH9tuBk1H3l_hdnTpnelrID3uzvXcqCnSwNzJuFlr061qUgLAfq2SWpwJYVPE0NCzIjeiI_7NT-wYVv21zzeU7H4HBQXATj1tP_Fn-roTEaEA.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/3d8904c5eb.mp4?token=j7dwbOT0uK5DQukB26O8BGHFmDR8p_jt0QBCtMlwT_6Lb-Xw8YF1kyo195ZJg6680Q0DWpcQy26ODoJoPG6Isf2xA_XxGQSavr0eq2LhxM-b2Vea36I75x53KZcfXmswLe223-6KRndq76meZ3inKu8upEofOsiIoDhBBU_V6gcNux_M5Fsbo1mS4Wnjc55-g54JKkBq6-OvUmUMvLJciht3FCY2995enzfIpJ-D059qikiigC7cLX4o-p9_epzLaEUUauHYMqajYSKxJRWvTNl3XPZSn0JVjzvA8N10M16_SdQO2IRg-fxAayNx8rN4mPFQntGlZCVspVbhnkyvRRkLa90CbxuGYCwHyku-Igc4Yik1B15BY9OD-hyhb0a1cYQbCfAz6Y3edZC72VtasWc7RsWVpej3APVx_28GGjCm2eZJv6Y1g4Waxc-D_p6rP4smXbqij2rbuf4GzE69pCE9ue0rqRiugMpH3Oe7TrWLzQ_zMawd6aTTrD1Z3Lohi_mI4JK4MrERWkWnVU-H2iyHmhxHLYreE16sMzRNauCnJ4SHChiDTqO245qZMb4RBYiQq_CdxyYg6yaesRgM-izULI06chMnyS7vGoOOIMq1ZcfrjXJwHWKMY9frMqTA_VcxvVliiayVUZs6-dTkulFiRleqpvnD3qfX4h5Wtbo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3d8904c5eb.mp4?token=j7dwbOT0uK5DQukB26O8BGHFmDR8p_jt0QBCtMlwT_6Lb-Xw8YF1kyo195ZJg6680Q0DWpcQy26ODoJoPG6Isf2xA_XxGQSavr0eq2LhxM-b2Vea36I75x53KZcfXmswLe223-6KRndq76meZ3inKu8upEofOsiIoDhBBU_V6gcNux_M5Fsbo1mS4Wnjc55-g54JKkBq6-OvUmUMvLJciht3FCY2995enzfIpJ-D059qikiigC7cLX4o-p9_epzLaEUUauHYMqajYSKxJRWvTNl3XPZSn0JVjzvA8N10M16_SdQO2IRg-fxAayNx8rN4mPFQntGlZCVspVbhnkyvRRkLa90CbxuGYCwHyku-Igc4Yik1B15BY9OD-hyhb0a1cYQbCfAz6Y3edZC72VtasWc7RsWVpej3APVx_28GGjCm2eZJv6Y1g4Waxc-D_p6rP4smXbqij2rbuf4GzE69pCE9ue0rqRiugMpH3Oe7TrWLzQ_zMawd6aTTrD1Z3Lohi_mI4JK4MrERWkWnVU-H2iyHmhxHLYreE16sMzRNauCnJ4SHChiDTqO245qZMb4RBYiQq_CdxyYg6yaesRgM-izULI06chMnyS7vGoOOIMq1ZcfrjXJwHWKMY9frMqTA_VcxvVliiayVUZs6-dTkulFiRleqpvnD3qfX4h5Wtbo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مارکو روبیو :« ایران کشور ثروتمندی است.
یکی از دلایلی که امروز ایران در چنین وضعیت نابسامانی قرار دارد این است که هر پولی که این حکومت به دست می‌آور، چه از طریق کاهش تحریم‌ها باشد
و چه از محل فروش نفت، آن را صرف تروریست‌ها در منطقه می‌کند، حزب‌الله و حماس می‌کند…
.
در حالی که باید میلیاردها دلار برای ساختن و توسعه کشور خود و مردم ایران هزینه کنند، اما در عوض آن را صرف حمایت از تروریسم می‌کنند.»</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/farahmand_alipour/6276" target="_blank">📅 13:18 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6275">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">‏
🚨
دقایقی پیش، شنیده شدن صدای انفجارهای مهیب در ⁧ ساوه</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/farahmand_alipour/6275" target="_blank">📅 11:41 · 29 Tir 1405</a></div>
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
  <source src="https://cdn4.telesco.pe/file/8e62469a72.mp4?token=MKkpCywY3gz6GIRL2I1aZevwMLi9_BZ_Ct5Ophz9CobPZmwtHTjCdcDlg7qVQ318uCqQdvZF3lMmU7lcFvhq2pLU8BcrYtxWzw83pPQ-w64uw1phvgwa1UrbzUkyMkG6tlaJqMBUNjuFPPL3o5xbF5wVdEZlHuysAst-SDivvi2iTuuhn76_tpxq0I_LkqPG3IvtUSZXtFYiSBf4JmCWUcjQEJJfICs3X6ygrpXcT9XwMGDyEIvQoFsQQBE2_vh41T5wZyj5AqVsTkoeO8_TwoLhD19nphDs1u57WWeBC9gn7pbvMKDEBsgzxeuHBbiqawrkOl-Jh8Devapkxa02vA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8e62469a72.mp4?token=MKkpCywY3gz6GIRL2I1aZevwMLi9_BZ_Ct5Ophz9CobPZmwtHTjCdcDlg7qVQ318uCqQdvZF3lMmU7lcFvhq2pLU8BcrYtxWzw83pPQ-w64uw1phvgwa1UrbzUkyMkG6tlaJqMBUNjuFPPL3o5xbF5wVdEZlHuysAst-SDivvi2iTuuhn76_tpxq0I_LkqPG3IvtUSZXtFYiSBf4JmCWUcjQEJJfICs3X6ygrpXcT9XwMGDyEIvQoFsQQBE2_vh41T5wZyj5AqVsTkoeO8_TwoLhD19nphDs1u57WWeBC9gn7pbvMKDEBsgzxeuHBbiqawrkOl-Jh8Devapkxa02vA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Rv58UJjFuCesYElCIkUTSW0WaK3_xvYxNPDTi81YTr251I-p3gJcBM2BJ-qqaveXvVg_pmquR_9_QAIn_kwKJaek4P_AgIln2hvZEMgyWI1P_UgcQC1jGT1L4SvhBylEKAye7SODuvn19JDUhjYfLnjL6Cq8hG3eF40uC9F2JZrL3hPVqAW6tZye5INLxLwET43QTtFXDFPpificb8h0Qd7CU4-1AJep70S8BRiqkBjYJ33VCN_HuizA3D1W6vhsREjR0x8HTkRM19Ta76hP7lKIVwwkBgEE1VspT3CyIJX6jAMzB5GWDP1T961kXbO3_0QfduRYfeKBzn65Deu_vg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZoJf2TX1bbqwF-Z7rKfi5LVnIXytVATl1SBzC0YIC84JODl-pt5jiugbQezahldSgsdn_B8f5GlXYfAemr8AFnpgVpndrN4qkCr0N0IaJhqxjA73rSE9-Fwpy7l69xIJyHDCV_bGLW9rTe5bES6myxr16ORkwocVbh4WwR1beohosEKxn9ZuG2I_RguMBmKJI04nNKiPirQYLWGq017eO44tx-Nr6xhAB1uIYrbkZK7fPMVlaDSs9i3adjnu_e0F_ye088TuhAmJ0fm4pUy3gcsc13Wb38HkPu1-bbhDmo6Co8GaL-y1MTwNWlIFte9xtQbhWs3zl2q692WC6F5w5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بیسیمچی مدیا:
الله اکبر - اسپانیا برد :)</div>
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/farahmand_alipour/6264" target="_blank">📅 01:35 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6262">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/j5DGRLCFxFGYI_u8kjMGz34L3lAhBU6j2zS1pC_VKXUEIA8Y7AKjS12H9EKAlnlpaFlzr31HoGWVp0oJzpw0VfooBWweM0h3IS1c0Bz4hlNmcIKwFIodagNYnfG21W2qOSTpLZnIIOGrn-5kMLpfMIbDDVxC-yQylCOQhCoomwIWasDLniOOnjKjWSwABWIKJh1zwS9J0hov9FApiRJqOuPA-9WbJxoCOMD9vZE3A2rsuKVSyrS8METJIncGHaMAyf4fPvyLI3JAg8Hit7d92FUVY3fL4dCqFo0_RZea4o9pni1JDCdZSatKmvoZN_C3MWsmFK4pLmAyl955uf85dA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/o5RBU8h0sVFcX9rK5yhSZl6er1c8fWlPyKCFoDJfMu4xU-Bdln0N2NKjUbtkP5llLSAUJCGuIOhP-I5XAdxcy-7faK6EIA21XAP_bY8zIuqP1esAGUUjALyk8u_rlcxX1Ku3FNvQUSUNBBgW41FP4ZxhvnjInLhrvOM1EQTjQ2POIE_hwn4Ja21ypxdCxDw10gJe6WabJO_oaQW7GjfAxMriZy-raC5GHQi-lPRhXS9VMLaq6NtP-Z5cpsPtH0ApFQfokyZTgxk5xFmY1MjQGZH_XshOUg5PUv7iwI4oCCyAFwchVxVGe_gknFbG0A_c3FhWTFOZQ7u9tcSddyQ3Fg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TH4gFYg8yAYaAnvcoAn4p8KfgQA2JjHCfSq3OnlKe6isSUVJoYlHDpAPcNm4IObMqgNqVq8TmAD2ZVAjFdMomyTjjAHuSc3zsgoMNu5M7wCnVk9ZgjIEyAje03GbcbmFAXoFNfVbGRYbYXHQIjD44h3SOkszz6rxl8qsR-FMA77P5jcSK0SEwA7fYSOSzb8Q0vb-vzN7P22DkFtuIGzo_oG-58vpbFjuQC0IEUrq0PRzg9H39bbSxL2TYPP7gfzycwD3ZTn15IfQWoXINH36YID6NbHhrLonyFAzeOpXH1RYvu0asuXr1G1TNVW5r-ldkOTKTIhAxHqCd20-J-04fw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">https://x.com/farahmandalipur/status/2078890340753568161?s=46</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/farahmand_alipour/6260" target="_blank">📅 20:41 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6259">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dscannMeTsVcdi2nOt8KOgh5_rc0_9eikgsBnnnHkAZPOiRh86_PTsD7Mjul__cav5-rVVm5wHRhx-U4gZ0QcodrTrO52a_ZISRYs0yuzKihrEYF04tRM84FbL5JrMos8KWmhaP4ARPutAQ-rF_Jg-D0tdKef9IdVTcYEVQjdJUKNMcHHsZzo3sO0k971sTnDM7QMRHjPIycUQldRv-SPg_W_SklwCJfocNKTveN_bKkVP8W-sTZdck-IeRnzy6FadaxJjuKc0R-ouPvTURtBqajmK5RXjiA6a66s1ztrUKdeJ_iZTowioTai6-hVV9sYMAVKmh43v-Aj_lXMRXZ8Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EWhDq79yOE2xSOoAsC-foIsl7MDwUrNPvChbM5G2fuMTE2L74qrWbID5RkGkNfIt956Hi_Ad-MsMrtdnd38edlANNv0AeaaESe5utxP-UXW7HAdUOUjv_hM9mT4qrLnaDUTTUR7iOY_S-tmkcXTtXT92SRktNsEU3GGSNtYifYFHKbHabsWvKTHgB-X43T-DR2DRzD6q05awgIcNbCPdDPOBz6oVEVFre5Xq4ackEoFhxXaKx2WIGRG40PnpJ0B8yt8ggQi07-BcocC-h0HlJO9xs4DJYg5mEMeNyBaaq2aIw5aQA9-Xky6uBVeWD4qSk6jSrFgKdjQiNa-0nx_mhA.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/9a1ebaca90.mp4?token=UuaC6941XLFRsZ-VxpTcUniGGL_24KRALXj60FD-95-hrK-yT-WMwJWztUMCqVo_WllY3Ox_R5uI5wOVYlcJJ0aD6Szo0TGmN1cdFTAL5YC94-b3nbA0Cmhlz5xSI_CfrEyWl4CBdPA92o1DZNzVXWuUODesR62XpKvUSuo75KwiA7y7ba3BuFOmubKe3bAWmK_5CmGkMMf4lZV9amaJE12vkHoAntLjF3HfdQ_i_4QdA5fmNlcZgjuo1Ro0g6SO-1L-1V3QaG5n1-rB3dYfG4aJ6HHWEjMCnNFQ2fV8eYzO6m01an9rhEd7mfDYGZ-HU5ha6otN-P9cp7HkSL5Ybw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9a1ebaca90.mp4?token=UuaC6941XLFRsZ-VxpTcUniGGL_24KRALXj60FD-95-hrK-yT-WMwJWztUMCqVo_WllY3Ox_R5uI5wOVYlcJJ0aD6Szo0TGmN1cdFTAL5YC94-b3nbA0Cmhlz5xSI_CfrEyWl4CBdPA92o1DZNzVXWuUODesR62XpKvUSuo75KwiA7y7ba3BuFOmubKe3bAWmK_5CmGkMMf4lZV9amaJE12vkHoAntLjF3HfdQ_i_4QdA5fmNlcZgjuo1Ro0g6SO-1L-1V3QaG5n1-rB3dYfG4aJ6HHWEjMCnNFQ2fV8eYzO6m01an9rhEd7mfDYGZ-HU5ha6otN-P9cp7HkSL5Ybw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
آتش‌سوزی در نیروگاه برق صبیه کویت
مقامات کویتی: در پی حملات مجدد
جمهوری اسلامی، یک نیروگاه برق و آب‌شیرین‌‌کن کویت برای دومین‌بار در ۲ روز گذشته  هدف حمله قرار گرفته است.</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/farahmand_alipour/6257" target="_blank">📅 19:23 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6256">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Mz7jh9kYqBz6N3gWICsG91mYJYrUJIUZFKoN2DPkC7GMmmlzLm4O-6QabjEo6zTArLkBMGJc_HJ20aGZkjQbe1zlvgQViFxc5pcRJzv3LdG3XsbGn_X_NUPY_98O3yPwUO6V1ffWXEYcGU-g371yI6cFltpTvOwrJnprfTn9mUyM6MJSXadUEOg5IX6PxvVAChWDE--2upxzdit92u30PL3Q9lYkGqAqkw9LJvBctovKIwFOFnpxX4aaZiMPTmzbf37WusFRHxSgcOIGB_o55K6dubP-O6rapQ9VMuKOj3ZCAOBTmKjjOhkakrMEHi1A4VDT2MZtsvbP-A65zrmhiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
حمله موشکی آمریکا به نقطه‌ای در آبادان</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/farahmand_alipour/6256" target="_blank">📅 19:19 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6255">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ad154543bd.mp4?token=R0lDuqEHmJ9jUSuyeZA_H0EpYjIkZcdB49NyLVL-BF-kaco1V38OosKb4lHMB31mPoxlb0DoLF0EbXis9Yk9ttv26da9I5Y6Hcl4tooI9TufZ1fQNs_lrYDL4dyuawiRv_6JCHTPRC4kqYSl3JnJOkCiteBct2Qj9mHkWhZWbxyLx2jigbnVjnhhrNKInK__oHaO3G5mfFKEffcxQW-jgwiAK_iqzdPeiBoz2Lx-kNEbO3FK8lv3fAwB8jSAD4DJtz_G0vLuBB3MzRwDII8lFpMrKtQOGR6KtoD7BJ43UlmVIxT5pfzam6rbhAAczvWtb0qzBgXeOQoU6XDFGF0ZYQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ad154543bd.mp4?token=R0lDuqEHmJ9jUSuyeZA_H0EpYjIkZcdB49NyLVL-BF-kaco1V38OosKb4lHMB31mPoxlb0DoLF0EbXis9Yk9ttv26da9I5Y6Hcl4tooI9TufZ1fQNs_lrYDL4dyuawiRv_6JCHTPRC4kqYSl3JnJOkCiteBct2Qj9mHkWhZWbxyLx2jigbnVjnhhrNKInK__oHaO3G5mfFKEffcxQW-jgwiAK_iqzdPeiBoz2Lx-kNEbO3FK8lv3fAwB8jSAD4DJtz_G0vLuBB3MzRwDII8lFpMrKtQOGR6KtoD7BJ43UlmVIxT5pfzam6rbhAAczvWtb0qzBgXeOQoU6XDFGF0ZYQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cxuImGeEe4ErWIbhSra_DKhGSJTpmcZoIYKE5CirDcAchVoI1_EBEvDJyQ1LJ9e7-8LYHPxBDcGmGW_yqRot3p3eVYU1P1jeJwPMtgxMejCAWwt6PNdYCLW_Nav5kGK9gKeNTYz3y7G_2rVO9-w_sz1vcN8Au_b59Ox2-iY2dMeV56BL5pjGFx2lVVK8dDd1NqdLNVbvuVGXUEH5p3eFBWeWYGfHDGBdSWtjewkbf9bRRaVPw8SawznfmHdSz4uRVZix18XU0x5xjrTWTNjx9bSgOKQ9u8RjpDt8NSXlFSjP15Z67Ha2xOu-HIK427GC-cVSj-T22qjC30yzUHs94w.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/d28653e7d3.mp4?token=Wo1MhfbDy39Rl1VrrHzCb7lkHfSRgq711gpd09eALPNbKG0bc2TrznHhKrHIp4MmrDAfv5v1u7pD40eaZu5BMWXUxXETVAUAVZPoiqFrKLpyBEiXy8mYCgLXf-f9q0bHhskvdQJAIAa_qU6-mJyC0n8T69cACn0MqBJ_1YCFFIj2z3VpY95HoWMzwLaqRFo8OqJU5PRN3btB-IVLEw8EttHbZKJtrzV1PlIruH6daO917HPkhOu_NY5zcofoUKUQoYGzgNUy99CqwwR3y3AAcPzm3HymeQy-oFTK0jkI8KTAlCPYriCJSHr76HgNSuYTRIBiyHsLa4-hwjK3-bHtGBMQuHiWddlDIwwbcR9HTDLi99MTKc9e1MH44bYSnY9GI1FrurPeUpBt9kTzOga1AAN1_kHdgH50jqW2Fe7TwWf0jFzQZMrpKzCtifdB28PbcpnbjmenKlXIj4ER6ViYk1Hk52IknwWuWKDlxTBozvVB8d5eerBBj2xS_qbzt3ayG1gPi_9SLiGc0Yv2XioXiqQwCgAnUL13o2kT3FzOBB5hG-nTIjJ2AJ4HsDGna2rRZxfxvozTowRIX6Tdwf6NbSCWyBN_ibUDzI_U_aUw0VU1Ce5tG5mCNzxmhXSjfcUXx19S2p09Lz2agvWIVHz75c9_BWkbteUTrT0X0STyNcY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d28653e7d3.mp4?token=Wo1MhfbDy39Rl1VrrHzCb7lkHfSRgq711gpd09eALPNbKG0bc2TrznHhKrHIp4MmrDAfv5v1u7pD40eaZu5BMWXUxXETVAUAVZPoiqFrKLpyBEiXy8mYCgLXf-f9q0bHhskvdQJAIAa_qU6-mJyC0n8T69cACn0MqBJ_1YCFFIj2z3VpY95HoWMzwLaqRFo8OqJU5PRN3btB-IVLEw8EttHbZKJtrzV1PlIruH6daO917HPkhOu_NY5zcofoUKUQoYGzgNUy99CqwwR3y3AAcPzm3HymeQy-oFTK0jkI8KTAlCPYriCJSHr76HgNSuYTRIBiyHsLa4-hwjK3-bHtGBMQuHiWddlDIwwbcR9HTDLi99MTKc9e1MH44bYSnY9GI1FrurPeUpBt9kTzOga1AAN1_kHdgH50jqW2Fe7TwWf0jFzQZMrpKzCtifdB28PbcpnbjmenKlXIj4ER6ViYk1Hk52IknwWuWKDlxTBozvVB8d5eerBBj2xS_qbzt3ayG1gPi_9SLiGc0Yv2XioXiqQwCgAnUL13o2kT3FzOBB5hG-nTIjJ2AJ4HsDGna2rRZxfxvozTowRIX6Tdwf6NbSCWyBN_ibUDzI_U_aUw0VU1Ce5tG5mCNzxmhXSjfcUXx19S2p09Lz2agvWIVHz75c9_BWkbteUTrT0X0STyNcY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/b5d96f954f.mp4?token=gJuZ22mHrDIJt_i8adqWyA7vh6q3i6PSnRaZD2PWL0ZK8kY8IZSF9SuGiVUj3p4TUZ-PQUI_-QNgqUEQtvoYm08L510SqFDLWjna3S9XL6NvTHRKdxubzd6ucX3KbMXTuiQnOWzi4d0x1kZU4szAa1-9JPFElB8BCVTVRFpYlPwVwp9iSRoU433YZiNdJUDJYd_igxXMYaDdKgw15fJKG4MQkaOOuaLPm0Vua-UV49MNrxYF-h4SzXzEzUeJ1mUKY2URvq96uROHrftRqUNLIbcVUH-bse9RlBk3CaBXzPZl0fHiaFPKdFB8OW_QpdYgesZ0snyXfgO6JXCD-YCP1g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b5d96f954f.mp4?token=gJuZ22mHrDIJt_i8adqWyA7vh6q3i6PSnRaZD2PWL0ZK8kY8IZSF9SuGiVUj3p4TUZ-PQUI_-QNgqUEQtvoYm08L510SqFDLWjna3S9XL6NvTHRKdxubzd6ucX3KbMXTuiQnOWzi4d0x1kZU4szAa1-9JPFElB8BCVTVRFpYlPwVwp9iSRoU433YZiNdJUDJYd_igxXMYaDdKgw15fJKG4MQkaOOuaLPm0Vua-UV49MNrxYF-h4SzXzEzUeJ1mUKY2URvq96uROHrftRqUNLIbcVUH-bse9RlBk3CaBXzPZl0fHiaFPKdFB8OW_QpdYgesZ0snyXfgO6JXCD-YCP1g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/3fcb2949cf.mp4?token=d2mZo952KSiSdcGBy20rXe96sMnbvPlbOT8fYxKTRAboNuRC-z7rpbcSuSLFEFGwDt4DMgidr3u0v2JS9mqcpbNmeofpRRWJ_hMBUTSQ55dYrkH7yprVygKveTCog-EI7TJqUZarYXa27vwwe4_-tv4JQx2kOjFTnxG0Z1AIjP0nBVOEkMSQPnVa37MmMU4gNUNZv-CovPbEUCOVjLBdg9umaWJJAW8plWoJiLjAYGtsfHAaef4bGBnAbkaLqORs77lCLylTLUHR4WkCex-UgrMu1iqk3t_vIUOJcmLQZXQODAtP-fJKcsuTaVj6XfYcYJyhSs2XABNP1MmgkhX4BUuflo1AzUVN3YjnAXEafGKlcPeBOUBjfRCQavEbFk01IVggD1n743GkJTPzR4Cjl0Zws_0NC8MC5kATHcVJ3ryq_6uGBJJEQehZzXddDABhldodGcxCF48Vs-0BVf9LLdCZ52M7k5CpNEEBUIbkEsiocZAkpc2TgbdXdTAGE993lj5C5Owbga855gz_cZEzKbk--U4WlYhCjx_KHzaMxTG4RVlnRoffqBMhJDo1LQWQm0ZXz7tjdowhj6Aq1pLt86iYM0WjMdsMF2i0byx31JCuGPIaipa_fr82wX7R9PVvBW6rVdvDS-vyVXXjbR5LNA2BHo5NouwVSwpqap77cD8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3fcb2949cf.mp4?token=d2mZo952KSiSdcGBy20rXe96sMnbvPlbOT8fYxKTRAboNuRC-z7rpbcSuSLFEFGwDt4DMgidr3u0v2JS9mqcpbNmeofpRRWJ_hMBUTSQ55dYrkH7yprVygKveTCog-EI7TJqUZarYXa27vwwe4_-tv4JQx2kOjFTnxG0Z1AIjP0nBVOEkMSQPnVa37MmMU4gNUNZv-CovPbEUCOVjLBdg9umaWJJAW8plWoJiLjAYGtsfHAaef4bGBnAbkaLqORs77lCLylTLUHR4WkCex-UgrMu1iqk3t_vIUOJcmLQZXQODAtP-fJKcsuTaVj6XfYcYJyhSs2XABNP1MmgkhX4BUuflo1AzUVN3YjnAXEafGKlcPeBOUBjfRCQavEbFk01IVggD1n743GkJTPzR4Cjl0Zws_0NC8MC5kATHcVJ3ryq_6uGBJJEQehZzXddDABhldodGcxCF48Vs-0BVf9LLdCZ52M7k5CpNEEBUIbkEsiocZAkpc2TgbdXdTAGE993lj5C5Owbga855gz_cZEzKbk--U4WlYhCjx_KHzaMxTG4RVlnRoffqBMhJDo1LQWQm0ZXz7tjdowhj6Aq1pLt86iYM0WjMdsMF2i0byx31JCuGPIaipa_fr82wX7R9PVvBW6rVdvDS-vyVXXjbR5LNA2BHo5NouwVSwpqap77cD8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y5Xj74N1kkeagrFA7mNF-0gllFmNg9LpG2ypu2-y7r_Hfi3nTLqSd6wMUJ-2lfgCTKyxIrFL8uapcC__sI8dN3llGtcfaqvR2OiNYXG6RzNLHCYLro0okk3MH80uAzvLOoSSUbgYz2xxgYHKHyq7irMvdQ66kfZz4t4aqjDaovfK9gLg6o7nqkWs_DFyEXHGjZ54jXZTNP3oV2fOtyrgD8E4u0eaJCuk-WV_M51yLG4vhbJL8fGkqvjDjU3WOAns_h--DfAzLFubO2wb1dE2leB3giO3eszM2QpolT5SbJV4H5b6AJD11JgJE_AuPaHVZw2Wj4LfdbhzyCCAaOPnig.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QHCunXDKpN5fr0rbPM67j_7SSUih82DnBQYJ4GnjY892ADLIqGixcpU9R-447_EB43FRmhRR6ZEFifqsxsIduNwGr14pPbtjY4HOPW3YssSPnKokyrYdMabCU58d0N1ITDSOQciq7JLalV4mJXweFdaQyHfApaCzhv29q-PZcuJbAQ2WLsUQUck-pRYQovlC9Rp2BVB1MNzZCjTL4Okcc7hMKN3tFlMegYZ8qQBNLUWRWw2tAYkMPFxa8m_hrr9id7fRUpATsK-D5t3CRKC6BDOt6J5742ToILbGECidtDKtbuPs3L1mKCfrdfcfT0aDSjHRrOUrAqJdSZd9SHSNZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هر روز ماندن جمهوری اسلامی
هزینه برای ایرانه و فرصت برای ارتکاب جنایت</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/farahmand_alipour/6245" target="_blank">📅 16:16 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6244">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">حرف حق :)</div>
<div class="tg-footer">👁️ 30.5K · <a href="https://t.me/farahmand_alipour/6244" target="_blank">📅 10:41 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6243">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N5VC5DtRlLKyFNKkHzpI4lgTwa0f1qp98nlaWWNw26OWoqDqRD-J4Wl3gFT8WniQOFJhYRzrrhHLl8PoaNy9WUaIqmOJRLTSiHxY4Twl54AR_y3MfXSBV4mYKvXTOav5G86ssxmMYWIFRA2IoeabaUbqweWGaDZr6I82v-wordHEgx-55JaV39gPy1k4UW5dD2j6ALRB1fm4wKFIuMuxogRj6dmkH4BrJh3ilxtKfVzls3DK9kabBJ8mZVFCOojHG_BlXbkmsxNjFpwScwygEfVYNEqCJy_VKKV2W7mCcM9NhzI968AhGIh5v0LmCbxSWn3DbERBfUjgCPLDNiFdRQ.jpg" alt="photo" loading="lazy"/></div>
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
