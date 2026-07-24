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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-02 18:50:40</div>
<hr>

<div class="tg-post" id="msg-6341">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">سپاه خطاب به مردم منطقه : فورا تا شعاع ۵۰۰ متری از محل‌ حضور آمریکایی‌ها فاصله بگیرید.</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/farahmand_alipour/6341" target="_blank">📅 14:05 · 02 Mordad 1405</a></div>
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
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/farahmand_alipour/6340" target="_blank">📅 11:25 · 02 Mordad 1405</a></div>
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
<div class="tg-footer">👁️ 22K · <a href="https://t.me/farahmand_alipour/6339" target="_blank">📅 08:24 · 02 Mordad 1405</a></div>
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
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/farahmand_alipour/6338" target="_blank">📅 08:03 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6337">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZMTx5dkGl32RMhG-1Hg_CtPAzpfVN27SicsOysr20M_aNLCquCTAtN-gFSbLC-onlxVwNmJMrlK0xifEzyk2wsUcaZW0pUF5FTYD0dJeuty-EFwUlZw5PYG9eQ6oyuaCWjKTQ9tOF4xI8uVayMzIWJhXhpZVLc3Zgi0V1mtIuxuGNfkk3n2KFE5zQBIix0FYskm02ZBXZ4FHoogqjFTyyp8KW2riGk3IG3Q6J98oEE0zNPingE_KCVaCHOXuCMLV4YEta8rNetg-zCZ18LGrjZPGH-NrrFfxsBJlvjhpVY46okXIEx12oo17GXcpQYvzP67av4_q4eoNs3lJ5O83Gg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تهدید تازه ترامپ‌: از پولهای بلوکه شده ایران، خسارت کشتی‌های آسیب دیده توسط جمهوری اسلامی را پرداخت میکنیم.</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/farahmand_alipour/6337" target="_blank">📅 08:00 · 02 Mordad 1405</a></div>
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
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/farahmand_alipour/6334" target="_blank">📅 22:52 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6333">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">🚨
ترامپ به کانال ۱۲ اسرائیل: در حال بررسی یک حمله گسترده به جمهوری اسلامی هستم؛ حمله‌ای بزرگ‌تر از هر اقدامی که تاکنون انجام شده است. به تصمیم‌گیری درباره آن نزدیک هستم.
او در خصوص احتمال مشارکت اسرائیل هم گفت اگر از آنها بخواهیم ظرف ۲ دقیقه آماده می‌شوند، اما برای آغاز عملیات جدید به هیچ کس نیازی نداریم!</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/farahmand_alipour/6333" target="_blank">📅 21:56 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6332">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">‏هشدار سپاه: هر پایگاهی در بریتانیا که برای انجام حملات علیه ایران مورد استفاده قرار گیرد، یک هدف مشروع خواهد بود.
‏واکنش سخنگوی دولت بریتانیا به هشدار : نیروهای مسلح ما آماده‌اند تا از بریتانیا در برابر هرگونه حمله محافظت کنند.
بریتانیا به‌صورت شبانه‌روزی و در هماهنگی نزدیک با متحدان خود در ناتو، آماده دفاع از خود است.</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/farahmand_alipour/6332" target="_blank">📅 21:24 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6331">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OGDYdVfLT2yjxfrmqpU3DMHcE56lmQ4Mld9YSZbGVAIVUtXMrU8ZVIFHU9d4hVRalJIzgI9QwyDmxKzNbc3uksUYLSZUC3ZFuQB7CNKWcpA-__ZT4CidkjrGi88IY2s-qodYOScUyejpnkGisClSI7MwwXW1tHeAi6hDyoHQM2azpN0uHPKMMlZRbYwePfI35esvvmvEFIpC_jKSy2rb8ezcHOaXSwgRHqzUlF7ZRX44do5uAQ-XGaOU81xnSQscg7rHtmw3qv_VicMLhhiS3Ye5N6lxDd72wv7RgxAUfvFtaJRbmKy1J4FAZxX8p3WAmJMZoCb-SiaBio44sTsFTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ضرغامی : فعلا حرفی از مذاکره نزنید!</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/farahmand_alipour/6331" target="_blank">📅 21:22 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6330">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kn9dKMR5fvO-ZWasFVV_OK6igM-n0w6wX1OpSzI48_9QIoIen65pjxBjJiihTePxpwbPVveeVwqyzIclJCOUX19f0pfVQrGJHKFk06NJmFAushBiClWeu671ijcb71tHvXBQ6jaQLNjMj0fDr1e0BL8pLnZAkpJqCQzSMkAyTcnoDFD2tlvRx61mpk2g3oGl6m9q9M9d5GP6Tppno5BujExI3MJjjqpXhasILhUE_fwtg08Z28UNSM6i7p2Etp8fmI2MFt_ExcRu_hl2GHUt4No43rRpWPZKVzxJFTKBsbIF_RdTzSNdI_DYZb1WDSUFItlLmUfi177tELCd-l7ElA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دو حقیقت محض
۱- تروریست‌های حوثی به تحریک جمهوری اسلامی وارد این جنگ شدند و به کشتی‌های عربستانی حمله کردند،
پس مسئولش جمهوری اسلامی است.
۲- حوثی‌ها ارزشی برای جنگیدن ندارن!
اینه که ترامپ مستقیم میگه فاکتور هزینه
حملات حوثی‌ها رو شما باید بدید!
و این یعنی بازهم ایران باید هزینه سیاست‌های جمهوری اسلامی و نیروهای تحت حمایتش رو پرداخت کنه.</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/farahmand_alipour/6330" target="_blank">📅 18:37 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6329">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B_hUx6gbujC3qprdCt_6yC_b_CSMG6P-1sFP4dQpKW1CBMD5UtFXrQvNYkIg3MaHL9_pfH6lyMvxH0bVbgf3ajT6Nnz4tEwxeMaimbWGiw6NEoaqMJTG2ongqb1lFDn2PwUu8X3G7NKJDBHCSxUnCdiFCgIZuvGQKtPvWQJsTvhOdDL08GL4lRtnPP9x50JaheMvmkr4vJhsO5KBqWtbZf0MVoRB429qaoOKVHm_zKn0D6Avy_wa6-rCzMs9bUK5Z7XbA_b5CWvZ_ybXEYc1avItcosduJkz1eTk6f7Xaq0dw7szeOmaqSIlVqCrwW0J2Qt5BbElHSHnmR6nVXjSXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قاآنی، فرمانده سپاه قدس، با ارسال پیام تبریکی به «خلیل الحلیه» نوشت: «آنان با انتخاب شخصیتی که نماد مقاومت و شهادت است، بار دیگر اثبات کردند که همچنان بر استمرار مسیر مقاومت اسلامی تأکید دارند. مقاومت اسلامی امروز قوی‌تر از همیشه، مسیر عزت‌مندانه خود را ادامه…</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/farahmand_alipour/6329" target="_blank">📅 18:07 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6328">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IpDfhuwUVA7D_vukw--punel5VYWFSWuPlGiBExSYEj--tTFv4eUzPBUX0LQiX_fcPh8G6V9z2nEac9WJzaC-FmE6hFPbLv43Yiz958Qjro4DN7VGFAjTLJh_m8JyODFYYmxAs7Ndio3phyQMKwfIaVFo0lPOpakaRQHWbniwzOfmhex0vrgFyLGvu78C3MAiXupDtA3e6yVXnIQBemQInE5mcqzH3YzNUVZD_CDhL8rHsNCw5YvKr_1CHbf5ul3PDzMktrqT8yKnXB1auS38vTfuLTb8DhGMTPAl9U3pCZCAGfh6NTHF8O5OxL_cAKFcZvZo6m3fU6jmjZQZDl0qw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/farahmand_alipour/6328" target="_blank">📅 14:57 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6327">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jfKoV0gTyaCZcUulO6eoMt__181eK1aDzHb7BK9cGQS99Dg907jlT9LXBT2HG0ku32WOusIa_Pj6dOzPabVq0SfCCFquY8ER9KrYh324K6YBX5lYyOKj1HW1lWw_7FEn0AMO4JDzgK7cl5GEUfqMbOGfeVT950G2Psl81WBmNQKy46XVCzBREiCoZfDQ6MmCBPATf_YeGfNcCo6ZvsTK47L9NQG_udQkI37tJ58L1Dk1963XZFgpe1B43bixT7i3WLbQ3efeJBeJlNkR4GhgNJoudo35qIxr7QOSJTo3tdK_D9i6QF-1ZxU09Fig_NlegPDytC2Gz2ULTFlUicMwrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/farahmand_alipour/6327" target="_blank">📅 13:46 · 01 Mordad 1405</a></div>
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
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/farahmand_alipour/6326" target="_blank">📅 13:36 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6325">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z5e6gqbtaiqMLDiAyunn8kGz9PU50p1SfNlg_8YwUXnAziW7g5Lp7WuEV5a9co26Z1tjMHKfOd-jvlLsX8k-g9ROoEIsGtRNc8Lf83BK5pGAMM5BjkAYVVc56kJcvr6IuD5E8uZuuhLcs32NzfDixg3y5JIWR4Wa_dsb817afol8ynVHpT446yvtiN5t3dmmIpcgmITUX8IlNT7DC3coSXOIowRxQ6s5-Z6deNba7QHPuacfbzo5xMwFImI4EegyokZOGZs4S7x5pZK9_0PgJ33_0M3hNeKd44zIQrwHj0SqAvil4VCQxf2oNAvbm3b-c2hApfwDttlBIIRhs4SVxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارتش: مراکز و یگان‌های آمریکا در پایگاه‌های الدوحه، علی السالم و عریفجان کویت را هدف قرار دادیم.</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/farahmand_alipour/6325" target="_blank">📅 08:58 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6324">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bTHIgkHMBtosxPvZiC3SVLcM4JjB-s1SDYb-XL-Ut7EOn7x75dLWeHsHWUiGWxgqIoJZMiuAbduDLB1Q2J985B2rW8Mdk-vNnCPkRGMBU8jZDKPeLPvKCqYs9qHetJNk9rJXT42fqdTTsZrhVyu_wadx2ZjeLwGxzXVxP5EVVOU2UbWvCnRwJTjNKaDhuGdRRrH7hjLv37_aZBIT7ipigvoYTU9BOoOJA1-K1Bd_fuFDItzT8RkC3kazTAZrQpsMtZrSA7YjU7huf9dSGPJvhn0373xlQtfz3NDETvkfeHGVkTTGxPC9bD_t1zg3m4vSNZkUZyNUxh1aG9gL88yrmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در یک تحول تازه در حملات‌ ۱۲ روز اخیر
و نشانه اینکه حملات وارد فاز تازه‌ای شده.
«بی‌ ۱» برای حملات بسیار سنگین و عمیق
استفاده میشه.</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/farahmand_alipour/6324" target="_blank">📅 08:48 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6323">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">ارتش: مراکز و یگان‌های آمریکا در پایگاه‌های الدوحه، علی السالم و عریفجان کویت را هدف قرار دادیم.</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/farahmand_alipour/6323" target="_blank">📅 08:41 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6322">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">جنایتی نبوده که جمهوری اسلامی
در حق مردم ایران انجام نداده باشه</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/farahmand_alipour/6322" target="_blank">📅 07:56 · 01 Mordad 1405</a></div>
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
<div class="tg-footer">👁️ 27K · <a href="https://t.me/farahmand_alipour/6321" target="_blank">📅 07:00 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6320">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">🚨
در جریان حمله آمریکا به مرز شلمچه ۲ نفر کشته و ۱۱ تن زخمی شدند.</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/farahmand_alipour/6320" target="_blank">📅 06:57 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6319">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">مارکو روبیو وزیر خارجه آمریکا : جمهوری  اسلامی تفاهم نامه را نقض کرده و لذا دیگر  معتبر نیست.</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/farahmand_alipour/6319" target="_blank">📅 06:56 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6318">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/65da400742.mp4?token=kdfB3218iGTvmwxdAfP6cGUS78O2qKKww2zX1UQPR5y5_BKnMpHptnjsuXJ14oSsHRX3-W-FvxsEWgdzhjVkxx80ZIanGMIq86Sm2qz7GEQDXyohJ6tpYXCUlhgacpL5mWBKeMzhJ-3uziTC2HzSSFCfu4jDG8GFPqYj3m5qP27-nuHBdSz5OPonhk8V9xUB5x_r6CV6xSe4xnpqbx-Oobv-Xhfwcbjgt86Zn6O-EvzjuJ5usHwKoeclSOFaD8_lLIXkFbgAtg8YYJFpA6toC9d0WuM3-2f1PXcnXGMHSpmvShmzG2Epph_M0GZLqZHMOnB5_6zmrnenPkuGoY_IyQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/65da400742.mp4?token=kdfB3218iGTvmwxdAfP6cGUS78O2qKKww2zX1UQPR5y5_BKnMpHptnjsuXJ14oSsHRX3-W-FvxsEWgdzhjVkxx80ZIanGMIq86Sm2qz7GEQDXyohJ6tpYXCUlhgacpL5mWBKeMzhJ-3uziTC2HzSSFCfu4jDG8GFPqYj3m5qP27-nuHBdSz5OPonhk8V9xUB5x_r6CV6xSe4xnpqbx-Oobv-Xhfwcbjgt86Zn6O-EvzjuJ5usHwKoeclSOFaD8_lLIXkFbgAtg8YYJFpA6toC9d0WuM3-2f1PXcnXGMHSpmvShmzG2Epph_M0GZLqZHMOnB5_6zmrnenPkuGoY_IyQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اون بابایی که با نخوت …</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/farahmand_alipour/6318" target="_blank">📅 22:41 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6317">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d716a2e5bd.mp4?token=RY8iORhWeianzhFDk1EeJxrAeIpPD09KiR3AT5-U9YZRzrGqmIMVMK17J84sqYwYp3Jts5i0Xq3p9-LO5aAI-IR-m9wKqJOVUNJSJX8kY2Y7DaU7RQfyywauAtDHMd_wY5X-tCdiJcIH9xB0vZlzvfDFSA9ivS-9r7QfTtjMJ7RY1BUajvCbhxsiU8QLkNKUuN-aZVnE__B7ohY3ymyQ661m15nUBUjWUMlDST4AAXAldiXRIuvFkHBDLiUNASD7jBqr5b_WcKD7wjLYtJ1oGOJBQclTbP5Y3UJ4VuWiBj88JmBKVTqaXZ_n7qHBDkMl-f4oZb-i6wRkRTy1fS2KCg2RZM4JwyljBxvTbfWEWzF3oUIZwfZ56iH8MUFLB78LydM6_BK6JZYTt3M9MiVNs_kmlD9pibHOxlujZjQ1zZrlZH6WpU0LCTN4kbkqJk1RQyrfw9DvHO1n3ZlIvlevIvOhzhK9r44QOchXrLCVRjJ9rdNDg4We6WmxpujBvQXOJnQIKi7nG2Q1y3psNBoJ0VeJyvwDhzUwIJMymC0PsmltW28BHoki3QEKpSyCln6MNWVi5RJz8YY40iAHLvpHNfBXmOGnLOQu1FDvx9U-fYo5eoVrx5djtQcMFLefYSiqu-wpGTyNeAherU0zrFPk_m7bizawIxZPWYyZ4y0JG3E" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d716a2e5bd.mp4?token=RY8iORhWeianzhFDk1EeJxrAeIpPD09KiR3AT5-U9YZRzrGqmIMVMK17J84sqYwYp3Jts5i0Xq3p9-LO5aAI-IR-m9wKqJOVUNJSJX8kY2Y7DaU7RQfyywauAtDHMd_wY5X-tCdiJcIH9xB0vZlzvfDFSA9ivS-9r7QfTtjMJ7RY1BUajvCbhxsiU8QLkNKUuN-aZVnE__B7ohY3ymyQ661m15nUBUjWUMlDST4AAXAldiXRIuvFkHBDLiUNASD7jBqr5b_WcKD7wjLYtJ1oGOJBQclTbP5Y3UJ4VuWiBj88JmBKVTqaXZ_n7qHBDkMl-f4oZb-i6wRkRTy1fS2KCg2RZM4JwyljBxvTbfWEWzF3oUIZwfZ56iH8MUFLB78LydM6_BK6JZYTt3M9MiVNs_kmlD9pibHOxlujZjQ1zZrlZH6WpU0LCTN4kbkqJk1RQyrfw9DvHO1n3ZlIvlevIvOhzhK9r44QOchXrLCVRjJ9rdNDg4We6WmxpujBvQXOJnQIKi7nG2Q1y3psNBoJ0VeJyvwDhzUwIJMymC0PsmltW28BHoki3QEKpSyCln6MNWVi5RJz8YY40iAHLvpHNfBXmOGnLOQu1FDvx9U-fYo5eoVrx5djtQcMFLefYSiqu-wpGTyNeAherU0zrFPk_m7bizawIxZPWYyZ4y0JG3E" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حسن روحانی ۱۳۹۷
تا آخر هم افتخار میکنیم به نفوذ
در عراق و سوریه و لبنان و…..</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/farahmand_alipour/6317" target="_blank">📅 22:30 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6316">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I9_Z0yOKEdWWU94Khs-blpbPw_i9vqgGdgZAFRrjijo9XNEo8MHiqEGwMtZa_vXeSevW0okSGfzIJcwVskzY5PeScAypmXO90OmdnoRHFvidMpxT3KQd192vENjVv3vE2fQENS7mZtFtZX-yxw3hDNQI_N3MI_bdkKaIcgjsAJIezHVklQ551nkt5OJUtzuENrUZlzUvwd7m3h83z2RPeMmp97wtlwAgr4WTARV-OIlxY-gY5VdfyEKJySyVAVeSnYXS-pEy_r4yE2dMqLyNcOXKPpoLVCJhYcaBIldWdbEmQJciaFJAvxPhIA_irYPekldc_-OugS3692Nsv1vmbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏سخنگوی سپاه خطاب به شرکت‌های کشتیرانی‌:
مسیر مین‌گذاری‌شدۀ جنوب تنگۀ هرمز  [ آب‌های عمان] مسیر نابودی سرمایه ی شماست!
قرارگاه خاتم هم دقایقی پیش هشدار داده بود که فقط از آب‌های تعیین شده (بخش ایران) باید تردد کنند.
جمهوری اسلامی رسما آب‌های سرزمینی عمان رو هم ناامن کرده.</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/farahmand_alipour/6316" target="_blank">📅 22:22 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6315">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">🚨
قرارگاه خاتم :
تنگه هرمز همچنان بسته است و اگر قرار هم باشد شناوری از آن تنگه عبور کند صرفا باید از مسیر تعیین شده [از سمت آب های سرزمینی ایران و نه عمان] و برابر ترتیبات اعلام شده قبلی تردد نماید.
‏
🔺
در صورت عملی شدن تهدیدهای آمریکا، نیروهای مسلح جمهوری اسلامی ایران اجازه صادرات یک قطره نفت را هم نخواهند داد و زیر ساخت های نفت، گاز، برق و اقتصادی منطقه مورد هدف قرار خواهند گرفت.</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/farahmand_alipour/6315" target="_blank">📅 22:16 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6314">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XLvIN464lhCuPuH4qpppP7_n1NHRLZqzDR0UkOhfD5HGhxPdh80PHmQPUaaKhkVHIeIldlm7x5t7510M5hygADRtpivKczvGsSmcapIsNWmah4LI10bcIReUW0dzenYIGVzm68sNSOs8m_wrRc-H--nVtvUg1uIaeMwRlF6aPA3F6VZw-bRIFe0OESo5kp2_dCVKYyhFLdNOvRjby7KqjJtGuO4KLPGSMFyraqb50AJk9q8eDXqI4UsDAy9AfitbX917L5y30_K4a-1f2QmIyIdymJvNhb5pTWV9XZ8vfQ1oIJ6QDC_nxFOQ7KJpdNyTg5PLM_2zOZpNeFvcFqv14Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
تهدید ترامپ: کشتی بزنید نیروگاه میزنم.</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/farahmand_alipour/6314" target="_blank">📅 18:06 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6313">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dAN_ja17mlDMAHuB4RA61Qiwr3fdY8B68YVsx7ipZbxYyZGwleQRiemditUaORUVOdtgfG0kYLTqIHPZG3VJSf3qkkUZ0KKXYqIkRCnAgqg_qpmyruylqEHBdUWOxLOP1_IAbV37x2yEwASsZ4yb8q54a6OFpoOIOgI-bgHIxuFXmg_OFd83eX6oWQ9Wnfk1qJipg8FsIRRpH59EgQlR8VufuSUiHYMP8BYlPgQ2NkV9kW3acgqERDXi4ld1lKVVMHo2oO_zz8_XlUJVq48jWw-nANwtqy1_qZ5QTPPBz0LgWWCExhkKbmbEwhTYfaxZeJUCRMJ4XAoijASjdekL9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
تهدید ترامپ: کشتی بزنید نیروگاه میزنم.</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/farahmand_alipour/6313" target="_blank">📅 17:20 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6312">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">🚨
شب گذشته صدای انفجار و پدافند هوایی در ۱۹ نقطه کشور
تهران،  بهبهان، امیدیه،  ماهشهر، سیریک، بندرعباس، بوشهر، چابهار، کنارک، تبریز ، بانه، کبودرآهنگ،  همدان، خرمدره، ابهر، زنجان، دینارکوه،  چوار، آبدانان و انارک.</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/farahmand_alipour/6312" target="_blank">📅 08:32 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6311">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9577aecbb9.mp4?token=NCKBUfQVPfcckqaUcTR6TS4R00UXSblbGVLwwX08Ftn15P5IIjtpmBWI8VIp03W0wN1EwVokO_yB4JQClhCyxb_1QMWIA9tJvIq6ckCETtTPT60OIT4wCe2gFecLg9IpJ8XH2cNuRDpSIWJm2Jx0gR9SldAAKRqz2KMCG-KBUJkXVG4t78AB_5dOK6ecD6DfIrvRJZhPCgqi1VYYExf_W5Vl_gie2VeHn_7bG7e8NjwGwuWaI72uZk3LCFnADNPBpAKxzRQX7V80e3drJ6GZA3BQcIYHPccTfI5z8mRJDg5qImX7ERpceuXI6ayMZjMXMKT1QKzMjQ8MLq8JCnCK7g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9577aecbb9.mp4?token=NCKBUfQVPfcckqaUcTR6TS4R00UXSblbGVLwwX08Ftn15P5IIjtpmBWI8VIp03W0wN1EwVokO_yB4JQClhCyxb_1QMWIA9tJvIq6ckCETtTPT60OIT4wCe2gFecLg9IpJ8XH2cNuRDpSIWJm2Jx0gR9SldAAKRqz2KMCG-KBUJkXVG4t78AB_5dOK6ecD6DfIrvRJZhPCgqi1VYYExf_W5Vl_gie2VeHn_7bG7e8NjwGwuWaI72uZk3LCFnADNPBpAKxzRQX7V80e3drJ6GZA3BQcIYHPccTfI5z8mRJDg5qImX7ERpceuXI6ayMZjMXMKT1QKzMjQ8MLq8JCnCK7g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هگزت وزیر جنگ آمریکا از ضرورت
برخورد با جمهوری اسلامی میگه
ونس، وزیر خارجه با ناراحتی به او نگاه میکنه.
(ونس طرفدار گفتگو است)</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/farahmand_alipour/6311" target="_blank">📅 08:28 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6310">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JXfjz2KZ6ZRuc37tobG3U1fbaC3peQRmQK8oA2anC0U8OHwVwpD1PLWVRP98HMNYXDcof-9m4vcBurXN5BtAWaQBeEe8aF4K1VGDL25rVPGUhe_anjshTngD5a9q7OS1aL5QU-RmzG8d2tesd27EmCk8h7rbv_JMPeq3z7orTw1YIkXCG4JMAqGoWF0Hgt5g0J_st4DX1f4CK8f01lcNxoGllEiXCZmqLziOdSe6emsQKLzSl0Sj2gm7zzhGqINaBPSG8-xD-EDPawq9GNRCh-d8eTyDcHScQEY02NkQsdteSVXZC7ShaOKE59Gq2zsbvgFBtgXPlsvR-HNyj0u56w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
اندی برنهام نخست وزیر تازه بریتانیا که از دیروز در این کشور قدرت گرفت، با در اختیار گذاشتن پایگاه‌های بریتانیا به آمریکا برای حمله به جمهوری اسلامی موافقت کرد.
پایگاه‌های «دیه‌گو گارسیا » و «قبرس» از مهم‌ترین پایگاه‌های بریتانیا و مشرف به ایران است.</div>
<div class="tg-footer">👁️ 30.1K · <a href="https://t.me/farahmand_alipour/6310" target="_blank">📅 00:52 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6308">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dHWooTLvcbfLla4SxzQvsEPCLp6w5fLa6acSugfytJnN2H62w8jNpPYgHa0AVmyFHUJhmgGxK1XXdY9olhnJt4UdqBUt5a3XaQtMLEolDjWmVPJZlHhPP8Ck9JoXDycWRhLoB4YUZaxDLNW2jz9anjDXPzUng6VqQxadWk-7hMCzKRB38uwDhnA6PW7uT3UJHOrs5E4lxWQn2Cq-Z-CRLX0Db5giUSiZKhpkQFJkKbgy2kfrjrOAtehhytArJI4iLKTcVG_ZmJbC7q_MISz2yRl7vVtV6LkJnl0w09bs5DPNWTDEwWI70ThYtPXkyVWFGAV_wvWQL_usH47HBDc0yg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Yawu6-xywoRk8iRDloR8DSjOFAtfVB2xGWqbUSgQCf1ccMa4ezfmKkAvypkW89rXdtKKNCWGpXmohlhAgADPDY6yjyGn6HixigYT6n0qo8CeULg-tneSMtukhrJ8EwPmEtQuQMxzkCq3tnoZj7LW4PUvKhzgwx9ExbsmhJQvYad3MpgExD7DVUAlMM9fKpyW_fFRIDB0ha1rMnQy3QTlfhrqcdz_ITHCTQMGjQoOy2SF7qMdpx-pHt24Pwn_Br0jaioIqX1KPcRZKzEOz1MpNdGnG92Hdn8lr83AeeRB6kVOM-zwHmkYfAgBaNE1WNYwQv6dWu43FByUhuC6QEgUng.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">حسن روحانی رفته خونه لاریجانی تسلیت
چهره زنان رو!
بعد همین ها میگن اگه ما نبودیم داعش می‌اومد توی ایران
داعش ۴۷ ساله که در ایران حکومت میکنه.</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/farahmand_alipour/6308" target="_blank">📅 23:28 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6307">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">🚨
🚨
گزارش کانال ۱۴ اسرائیل :
جمهوری اسلامی به سفارت اسرائیل در بحرین حمله کرد.</div>
<div class="tg-footer">👁️ 30.2K · <a href="https://t.me/farahmand_alipour/6307" target="_blank">📅 22:01 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6306">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RAm544k59YHx8NlzO7dn79cdmT_9R5mDb8J9351Fb5lR-vqKUvYsP_CtdVJBO4Pd0DvaMsg2gRg2NBlvt4Y-c5flRqJt_ql4t3Buuudpnm1XuO1gnOpgm0GxyZH6osYGevxvCVTylFuorKLtEmCkTmdQQEKuz2ZxUDvEgwMQ0-Lvaxm3fiDwPQh5HoomTcGi2qeL7vX2td-tYhFPGg1njExhcNZ0sRKKooiqeuZ4bDL9_5Jk589Tj9qE_nLi3XnxpGEKDPseWI4q8s43U1nJWBBGoZr8oRzTYSd8Fz7f1UxYSZ3RJSvVQ3U7ywoN0PLGBIpNEjx3n21IdDPbID4pJA.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/3814b8c91f.mp4?token=NT0-9aCv7XJ2qGIdF2NVOHc1DUB4bjbbD75Ps8q2phQ_pEE4WBSUTGjv25T9qMBWGpM2tpCEeV_3l_i31CFje7Oq1HseSn0q1eXF_YwPL1GgeBfBUSEPq9Qc9PizgiwvtYwpJKKaD8yrsPsf_7P9h3FTYi2Ify0hTUFPx8D51LmjTQnzzdW0jzht_hJbx5KtuaOUP-UIx1inpyU78Q5Fwvhdp-WEdByA5xwb6IRljXsYyvhPIsso4d6lBl4KJC4HfnGJ8zN0E5XAydlj_vWDt1pqhWMxhuJi-0mD9DddK8581B1JhHAqNq7GjwP---JG7peOs_uy93YerlCVAXmBxoWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3814b8c91f.mp4?token=NT0-9aCv7XJ2qGIdF2NVOHc1DUB4bjbbD75Ps8q2phQ_pEE4WBSUTGjv25T9qMBWGpM2tpCEeV_3l_i31CFje7Oq1HseSn0q1eXF_YwPL1GgeBfBUSEPq9Qc9PizgiwvtYwpJKKaD8yrsPsf_7P9h3FTYi2Ify0hTUFPx8D51LmjTQnzzdW0jzht_hJbx5KtuaOUP-UIx1inpyU78Q5Fwvhdp-WEdByA5xwb6IRljXsYyvhPIsso4d6lBl4KJC4HfnGJ8zN0E5XAydlj_vWDt1pqhWMxhuJi-0mD9DddK8581B1JhHAqNq7GjwP---JG7peOs_uy93YerlCVAXmBxoWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/acc280d27d.mp4?token=WHs6OCwUeF4RBGMhp4NDKPXAEQp84Gtj5gUOydP1oAbV_aEB0LHYH_LxyMYAsLKzf_BaXHwvYuRz5BHcBxmvXrQ4gCuibWWtklguSsDa1rS69z-2AavPStUaFJSUcRVX4MMLUVP17F8g5I7Z_jw4PPe0O4NHHxZ4cApGxvppcOHU_qAIZ4xU1U9cqS06oAFyzYMz4RrJPrVFT8HLqZkGSz2ZbhQcqparXotjJsp6acuEPoi4bqB5JaRjB6r2Ur4QsTF9A2DTF4aIGwmzINDltCwLg2xzarWO1kPGEqMKUHQfr_kZxHoIP7NodwL-L0gMaEYnQZoLs9RGPrrnLpeZXA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/acc280d27d.mp4?token=WHs6OCwUeF4RBGMhp4NDKPXAEQp84Gtj5gUOydP1oAbV_aEB0LHYH_LxyMYAsLKzf_BaXHwvYuRz5BHcBxmvXrQ4gCuibWWtklguSsDa1rS69z-2AavPStUaFJSUcRVX4MMLUVP17F8g5I7Z_jw4PPe0O4NHHxZ4cApGxvppcOHU_qAIZ4xU1U9cqS06oAFyzYMz4RrJPrVFT8HLqZkGSz2ZbhQcqparXotjJsp6acuEPoi4bqB5JaRjB6r2Ur4QsTF9A2DTF4aIGwmzINDltCwLg2xzarWO1kPGEqMKUHQfr_kZxHoIP7NodwL-L0gMaEYnQZoLs9RGPrrnLpeZXA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/403aadedf7.mp4?token=DKRZ_TI1gBVFFG6vYEfZ0HJNUOLOkCuZoF7x8yMaJARIXKtrAqNoQWx5tkWCW5LwbAu4Zsl0HGWMkkZOz8rak-djVUZtUhq4rgEd625iRe0yHb8PICfgCm35WlyPtcOb5zSUnWXpRw4__l9_7RtMLtSLkPV4PnyT7ERRtTe8zCikq0WeIZEmrr5RdQ3dwVmz7NrEYEFQwmRRmlVXCdbKoaKPp1MSOA4DyzVtkH67zw4QMH91LbGjM3fZP8dxisEz32qMbgtu8NWNu05fD8xBHWGqdNjHP1Y4Fttaexqcmpppd0bOXEz3pNkJ33E8nr8eRVPdQjoIPT4dHn8lZUIVOQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/403aadedf7.mp4?token=DKRZ_TI1gBVFFG6vYEfZ0HJNUOLOkCuZoF7x8yMaJARIXKtrAqNoQWx5tkWCW5LwbAu4Zsl0HGWMkkZOz8rak-djVUZtUhq4rgEd625iRe0yHb8PICfgCm35WlyPtcOb5zSUnWXpRw4__l9_7RtMLtSLkPV4PnyT7ERRtTe8zCikq0WeIZEmrr5RdQ3dwVmz7NrEYEFQwmRRmlVXCdbKoaKPp1MSOA4DyzVtkH67zw4QMH91LbGjM3fZP8dxisEz32qMbgtu8NWNu05fD8xBHWGqdNjHP1Y4Fttaexqcmpppd0bOXEz3pNkJ33E8nr8eRVPdQjoIPT4dHn8lZUIVOQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ux4WkhwDtowb6DDFc3LXKCcC70J2PvoBWgmhhNSpTzOAfvOkpxdFSdR8Idi-JmsiRUAsTU5OFZgPbmNPDdTvzU7O8kNLfwggb9vPYrfUhf0NIOdY6hsYPsPFiJB9d59NgsusWYcmu61hTzQOMa4vaebDo4aH044zz8YBlZyRm9nSwmgf2dvNAefFCF2wtaRoDDa6mRdJwyS7yAzI4PWCNJNb4L3ulnnDXDA3EbDO3nN5u6EHqlLNeG-4G0mOfUxFEWHMbbNaQgqwUGaQ0mcej4QUawNBcNPxaKBB8s2IfR4v6g4HYPEvSLN-hsm632t7iy7e1mcvgOG_CTYQmPw2QA.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/46c8806804.mp4?token=C0QoX20LdZxzLVJg4wtocfbxHUy8rx0LkbhpsHkKHKQK8Gr5cDiTIDNZm29Kg20SuAskNxw1HvdmZ0IBoAFykvEkyTVJ6hNUuJIibnmXcZkX1hdr2MGgjAA979qL-fkECAT3gVsHtYxyrf81FtwpcuKvVOiDKfF0TjzBZo3EMqgnF11gXD4gtpHA4dEcUwX_Q_px736yG71QE2NC35sq56PsxnPe4p0NOTcH_g-sIGDxxZzA9J8NP17NGAq-HlP_D3OT40YQc6a_KQIC8ucUYamT0lMMsTBKuTqw-uSxBII9MQ3ELwTDfuJbAhDgx8GQtS_T_6iTYIpz7Fuj-QAQ-w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/46c8806804.mp4?token=C0QoX20LdZxzLVJg4wtocfbxHUy8rx0LkbhpsHkKHKQK8Gr5cDiTIDNZm29Kg20SuAskNxw1HvdmZ0IBoAFykvEkyTVJ6hNUuJIibnmXcZkX1hdr2MGgjAA979qL-fkECAT3gVsHtYxyrf81FtwpcuKvVOiDKfF0TjzBZo3EMqgnF11gXD4gtpHA4dEcUwX_Q_px736yG71QE2NC35sq56PsxnPe4p0NOTcH_g-sIGDxxZzA9J8NP17NGAq-HlP_D3OT40YQc6a_KQIC8ucUYamT0lMMsTBKuTqw-uSxBII9MQ3ELwTDfuJbAhDgx8GQtS_T_6iTYIpz7Fuj-QAQ-w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/3cb0045793.mp4?token=pVrgw3UdSkArEdRd6FZU-7Vg2rsVf4EAjiUVIAV9EMMO3rH-4u8okN_8lOZuWkfhapXaR92RTL-kopvTpeZ_f4_FaB721Kj9w5zI-BrZM3LcZDdxAr4Boblony5CxZIF8mBf6g_fnPMNgEMJEdUsqNvb3wUr3gXLd9qfqHWLzCg6C76f3meYh4CG5Mr0ZCWdy0dK2cRbXP3VTSKFRH0KUqrPYcH-URwTS_zMzjCExRbkkSvy4QT3uCedt2Py4LuQxg2JHoZJrE_pLN1Jt-VP_v552wJ299W2B7xhD2bhApnv8oYFz5br1esneFkg--f6HdcBmBvMVVz1D0urQPKIPg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3cb0045793.mp4?token=pVrgw3UdSkArEdRd6FZU-7Vg2rsVf4EAjiUVIAV9EMMO3rH-4u8okN_8lOZuWkfhapXaR92RTL-kopvTpeZ_f4_FaB721Kj9w5zI-BrZM3LcZDdxAr4Boblony5CxZIF8mBf6g_fnPMNgEMJEdUsqNvb3wUr3gXLd9qfqHWLzCg6C76f3meYh4CG5Mr0ZCWdy0dK2cRbXP3VTSKFRH0KUqrPYcH-URwTS_zMzjCExRbkkSvy4QT3uCedt2Py4LuQxg2JHoZJrE_pLN1Jt-VP_v552wJ299W2B7xhD2bhApnv8oYFz5br1esneFkg--f6HdcBmBvMVVz1D0urQPKIPg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/011fb08ef0.mp4?token=fylWK0Dtvs178p3e3fUA9_7NDBLCQiwzS_avw287KcUBKCTOK6rqPaWYcz7kEHi8I7iLn-j8TdvoJZIySDYuFt83Ojyz1zmjs7voXu1EofTbW5utCeX-OnHUbbwUy8wwST951PQYaQe6pQ1cV-JyJh-v1CMobOgo3S8LKdMj2FPqMvxTu4e1IsqRXal0qZx-A6A8tazD5pMAt3k2jNohzv38DZ69ZsN_KQIHX_p8qpy6AR5HL-YPM5EDp6PbcxvLGP8gr1PmhwHrshvRgwhk_WDoKyr9BYLRDVfXhBubN59bS2_idfy0yk03lmDvMTnrVqqjHpaoMU7ai64EU-TvvA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/011fb08ef0.mp4?token=fylWK0Dtvs178p3e3fUA9_7NDBLCQiwzS_avw287KcUBKCTOK6rqPaWYcz7kEHi8I7iLn-j8TdvoJZIySDYuFt83Ojyz1zmjs7voXu1EofTbW5utCeX-OnHUbbwUy8wwST951PQYaQe6pQ1cV-JyJh-v1CMobOgo3S8LKdMj2FPqMvxTu4e1IsqRXal0qZx-A6A8tazD5pMAt3k2jNohzv38DZ69ZsN_KQIHX_p8qpy6AR5HL-YPM5EDp6PbcxvLGP8gr1PmhwHrshvRgwhk_WDoKyr9BYLRDVfXhBubN59bS2_idfy0yk03lmDvMTnrVqqjHpaoMU7ai64EU-TvvA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">محمد اکرمی نیا سخنگوی ارتش
‏به روشنی میگه اكر آمريكایی‌ها
بيان در جنوب ايران ما خاك خودمونو هدف قرار میدیم.</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/farahmand_alipour/6296" target="_blank">📅 11:35 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6295">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromحافظه تاریخی</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/78bd1813e8.mp4?token=gWSYwdl3zqdPdu4gRl0wKz4YrUL1UwneN3m86rjlA2HO92GzK4H8dqbqDv40fDa7dhI9DOI45djz5sX44L2GY1hUW-S0bmbsqh6BVQ-Suhf7vDSibd3vDY5YKx9m8XpzI1mMUzaE_sMF4skjxAl53jGyNoVZlGyLkIv-2vOhUqq-eA7Jhu8KwIbYm0bpwPC8rXy1zuf2djXeTgBce7KFjehfSEXhplwjrH3IF845zxpt5Pgh-yHTT7iRdl6dbQ2xlAGzK08z2SA5GxdSK10cGo3buDuI23qA5ATiRx2YJxc9qucOd2h1HpyFnt-YrHmYh2uHF5Y0v0fvwOAz0w1VzlNyMYPWya1QT3UYQMh4fHsxk8Iz77PPTm2tcS_Fl4-T_QMJUqvG2-kIb279aNp5lACmOpQw408Jg8e8fzWoabd6a6diM4h6UDKGsTM-ozUYAZRMONbndUsx2EIchshI0SivnN7tW-UCajysJ2flZEJ6MkBtMBon6wuxXEFXICrsvDnp0PeQA6eEbTCLGb9ax_kZZWKswb_99PZCEW4nJu3ftaUlmFuYeXG7Tyq9V6Ksj2TUj7Dbs32q3ycFeOYpNSNb_Ymd_EjUw-AA8omXEl1n--cSKkbKHUq0lGK-UJPS8yki99PZAVMNCZ2AzhkovUCOoql8MuO6b7S2aNY7moI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/78bd1813e8.mp4?token=gWSYwdl3zqdPdu4gRl0wKz4YrUL1UwneN3m86rjlA2HO92GzK4H8dqbqDv40fDa7dhI9DOI45djz5sX44L2GY1hUW-S0bmbsqh6BVQ-Suhf7vDSibd3vDY5YKx9m8XpzI1mMUzaE_sMF4skjxAl53jGyNoVZlGyLkIv-2vOhUqq-eA7Jhu8KwIbYm0bpwPC8rXy1zuf2djXeTgBce7KFjehfSEXhplwjrH3IF845zxpt5Pgh-yHTT7iRdl6dbQ2xlAGzK08z2SA5GxdSK10cGo3buDuI23qA5ATiRx2YJxc9qucOd2h1HpyFnt-YrHmYh2uHF5Y0v0fvwOAz0w1VzlNyMYPWya1QT3UYQMh4fHsxk8Iz77PPTm2tcS_Fl4-T_QMJUqvG2-kIb279aNp5lACmOpQw408Jg8e8fzWoabd6a6diM4h6UDKGsTM-ozUYAZRMONbndUsx2EIchshI0SivnN7tW-UCajysJ2flZEJ6MkBtMBon6wuxXEFXICrsvDnp0PeQA6eEbTCLGb9ax_kZZWKswb_99PZCEW4nJu3ftaUlmFuYeXG7Tyq9V6Ksj2TUj7Dbs32q3ycFeOYpNSNb_Ymd_EjUw-AA8omXEl1n--cSKkbKHUq0lGK-UJPS8yki99PZAVMNCZ2AzhkovUCOoql8MuO6b7S2aNY7moI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/59eba4787d.mp4?token=BwpyQI52HdS-208OhpZ7OUBgdcxaqTSkZ7HVDWfrAJ-oMVNS_SI0tjnJ-DElsgW_KugPKJ9Sg348HMe0fiMPimT_TPJxX7gsF07npTGu7dfSKlog3m6B8sPPksiKypksW9az3m-dfSYtZeoMNM_MjPxrf3v1FiBR2P45qUWpLIlKyTeElRwHdiU0YhRTqT72CsXUuYuwnSfmvx1qmrty7_sjf1gdONIPDzUip1PBECTXUTkpKe5kle4s7W7uucYglHgo7r9l_Y05xp0uYnTLM_qyqgnwpGtFcOabubpdNFznVC_88yxc0aVbgtfzr2bZXdxQG_Pedxz_hri8cLeu5Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/59eba4787d.mp4?token=BwpyQI52HdS-208OhpZ7OUBgdcxaqTSkZ7HVDWfrAJ-oMVNS_SI0tjnJ-DElsgW_KugPKJ9Sg348HMe0fiMPimT_TPJxX7gsF07npTGu7dfSKlog3m6B8sPPksiKypksW9az3m-dfSYtZeoMNM_MjPxrf3v1FiBR2P45qUWpLIlKyTeElRwHdiU0YhRTqT72CsXUuYuwnSfmvx1qmrty7_sjf1gdONIPDzUip1PBECTXUTkpKe5kle4s7W7uucYglHgo7r9l_Y05xp0uYnTLM_qyqgnwpGtFcOabubpdNFznVC_88yxc0aVbgtfzr2bZXdxQG_Pedxz_hri8cLeu5Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">واکنش نیروهای مقاومت فرانسه به رهبری ژنرال دوگل به کشته شدن ۶۶ کودک فرانسوی بر اثر خطای بمباران متفقین در جریان عملیات آزادسازی فرانسه از حکومت تحت حمایت نازی‌ها
@hafezeye_tarikhi</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/farahmand_alipour/6293" target="_blank">📅 09:30 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6292">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3ba53f516a.mp4?token=JB_UaDv5779iPAkm4MAqmF01PrgulWPkq-ysKZS6AyuUn4TMWZPwRmMOWLozXZPmx2NDrroomJrQxCtcoThCTnCOQVH3iOcgeBITFTrk5wB2De1oEcH3teaXxBeNZIExq7XQC6LkAd0DHWXorDfUWATDH26ZTSmtaSnV-NTzz1HKXoLlvpk8zqphMCuaZOKxL6KSsDryHCnpiyRjauhR3N_TwtmcH4dLdRXZ6xyQaW5nPchnZrilSJwZFFu-dq5NE0QO_J9nLAMwS_6auRpvT5Jlr3UQxY6ino_T7nLOwDdpgzSx6Gs3Fk9cxcJWdh_R2iCgAtXOo-uDeiSeHI3lkg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3ba53f516a.mp4?token=JB_UaDv5779iPAkm4MAqmF01PrgulWPkq-ysKZS6AyuUn4TMWZPwRmMOWLozXZPmx2NDrroomJrQxCtcoThCTnCOQVH3iOcgeBITFTrk5wB2De1oEcH3teaXxBeNZIExq7XQC6LkAd0DHWXorDfUWATDH26ZTSmtaSnV-NTzz1HKXoLlvpk8zqphMCuaZOKxL6KSsDryHCnpiyRjauhR3N_TwtmcH4dLdRXZ6xyQaW5nPchnZrilSJwZFFu-dq5NE0QO_J9nLAMwS_6auRpvT5Jlr3UQxY6ino_T7nLOwDdpgzSx6Gs3Fk9cxcJWdh_R2iCgAtXOo-uDeiSeHI3lkg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">۲۱ ماه پس از کشته شدن «یحیی سنوار» رهبر گروه تروریستی حماس، این گروه «خلیل الحلیه» را به عنوان رهبر جدید خود معرفی کرد.  او در رقابت با «خالد مشعل» موفق شد این پست و مقام را بگیرد زیرا که بیش از خالد مشعل، مدافع اقدامات یحیی سنوار بود و جنایت ۷ اکتبر! که چیزی…</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/farahmand_alipour/6292" target="_blank">📅 09:15 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6290">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N2Hlv1A24yr7vqqHOLrHhui1GbUFJitCPKC298Zbo0VQWS2T_1GT8g7uaiKQQuLtoq2icg9Vlx55FSwUv2DCiiupuY1X3AhAJ8noCyB29QRDLu_5aJWzNix3DhgLmYSXVpTZ67hGbYRKkWpZjNWkM0GiZroOmy6nxtDUx9afCAVgc6Ol7r8a1_hnRHW0dUEp7a_PGRxfP5Fk2DEI9GrLuSMicCEDdtRxid2xD49zk6wX_SHEQpUdfbCIskqA4VOZMk5jCbXoD3PmAeGTLdme_m3vPI0DrCxj0NVC0wmTzW3wINmJ9urzQPlp_fp9mPbdoNaPTFdEyB2wuQ7yiVNmmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۲۱ ماه پس از کشته شدن «یحیی سنوار» رهبر گروه تروریستی حماس، این گروه «خلیل الحلیه» را به عنوان رهبر جدید خود معرفی کرد.
او در رقابت با «خالد مشعل» موفق شد این پست و مقام را بگیرد زیرا که بیش از خالد مشعل، مدافع اقدامات یحیی سنوار بود و جنایت ۷ اکتبر! که چیزی جز فاجعه برای غزه نداشت!
تصویری از خلیل الحلیه، رهبر جدید حماس با خامنه‌ای. هم خامنه‌ای و هم یحیی سنوار توسط اسرائیل حذف شدند.</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/farahmand_alipour/6290" target="_blank">📅 09:12 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6289">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/biK76d_J8GOi68nkePVHq9y_oyfDlYBAQHaX5iNVRqWCKLN9GrWOmA8LIqssSvI-GrTV4D3FKU3-Cxp_-Zb3dG1E6JNJfsWiQZ8xRCwMYUtVnvqZcNmeANHr_MCZ_CY_3JD655ru5RjbXHOP1elGL1bcKAjPro4vC67A1oqaBwBDF9cVsjf0ureJ8cTjc0qjWQDzh_dnTuvhamuiXfWm3K3ZXpl2utXtHDJpnFBlk4QqquTSBFV7NRLcardIgqKhYe3lsznac1bgdyNWuVIQimZVkRk3dxYkA-NVzI26pv2LW_1Q65AjCTqkc8mUsxNQb48OXbn2Duei8DZa8xPE4A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/farahmand_alipour/6288" target="_blank">📅 06:40 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6287">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/75cc0ec8fd.mp4?token=NByxKmMstAGJOD0C-qzqA1iLRv2qOnO0-NH-2e-gWtnjzPcNrh74yWXF0GbJ5fhVKoV33NhO3GcEUYEB4c8lEhH4w6v5D7YsbIMb2cqrnwoEVI9Vg5MNOz0EuXsg95rc5Tcss4lCAeqaCzst21WpdX0idOJ1sXk4AxbL5nQiO7hKKU9jQzeBNKgkW8aK48DunpK4uHIO4KoiUT7llvQbSqQOi5au87iLpE9cqiPr54zh3FXwZXys30UcU4T3oF9CwwpiEzlCVezN7aq_EKHfff3282daDbZWXQ3hQkr0qJZ1hz1pA7v3v3GGPtpUn7Y_XhHhaplsYhwW-9it6j6bNUNBDnBXC5An3rFAlKPXID3Tary6Z36zxyJxGnumFv8KDxYz7S3GVib65pt_pSpzoeNDkJg_EtKi3uWL7_mADzUGXqqjZ2k9_SXK5IdpECv4ag3jSJwFcW4OTDLMK0mwLWh09nPSmC3TDAhCpig_PwatCvmVQUJv1Y7PRx85LGriG8IAvNgxDpOLzUZY55T3GzBw72p3Lcn1Hqb_n74G6bfsKxpKqSLNNXrLnThn6pHm-c0CtXuBiKXR3gySxbFKSfT8LTzlZeNzoPxpplX9kgAZJWP19zfjpj9mcrCFMWgyOmjPxXztQL23iqa2t2kbDM8m1MwXq-ddzsDu98T9TsY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/75cc0ec8fd.mp4?token=NByxKmMstAGJOD0C-qzqA1iLRv2qOnO0-NH-2e-gWtnjzPcNrh74yWXF0GbJ5fhVKoV33NhO3GcEUYEB4c8lEhH4w6v5D7YsbIMb2cqrnwoEVI9Vg5MNOz0EuXsg95rc5Tcss4lCAeqaCzst21WpdX0idOJ1sXk4AxbL5nQiO7hKKU9jQzeBNKgkW8aK48DunpK4uHIO4KoiUT7llvQbSqQOi5au87iLpE9cqiPr54zh3FXwZXys30UcU4T3oF9CwwpiEzlCVezN7aq_EKHfff3282daDbZWXQ3hQkr0qJZ1hz1pA7v3v3GGPtpUn7Y_XhHhaplsYhwW-9it6j6bNUNBDnBXC5An3rFAlKPXID3Tary6Z36zxyJxGnumFv8KDxYz7S3GVib65pt_pSpzoeNDkJg_EtKi3uWL7_mADzUGXqqjZ2k9_SXK5IdpECv4ag3jSJwFcW4OTDLMK0mwLWh09nPSmC3TDAhCpig_PwatCvmVQUJv1Y7PRx85LGriG8IAvNgxDpOLzUZY55T3GzBw72p3Lcn1Hqb_n74G6bfsKxpKqSLNNXrLnThn6pHm-c0CtXuBiKXR3gySxbFKSfT8LTzlZeNzoPxpplX9kgAZJWP19zfjpj9mcrCFMWgyOmjPxXztQL23iqa2t2kbDM8m1MwXq-ddzsDu98T9TsY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gbWHPQnZAN1To9uLbzP2kp2Xz5MxR59Aq6OQc69MeOqWhRF52Sm_Ueg3k08bry5rOZRClEf4KG35oTIVPNLnFa8iJhd5VIGywLBRMUNPg_EZrRlQ3c4BZQhOhOwg_SMcV-UFprZxxnkqhX4uN1frTVereh6x5lQnRwwzXLTUkgDmluvfOxtqNreT7Dwg5NZoTs583NdqKRFkHnqFlh28M6n64L88mn8xzZaO-1G_N087GFZkQIefSw4dkuDX2j_24CIXKWSqZsMPEf4RKEJSu41B_2vSehgx_DO9gKcfGBeavw0uC8ZdYd6myCVFlU5meArkxVtXlqnuDZCcEH73UA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ :
اگه قراره کسی دستگیر شود، سران جمهوری اسلامی هستند.</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/farahmand_alipour/6282" target="_blank">📅 21:09 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6281">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pnh9YpbTUyiXo6bQUoHgQWzwsdQPXWvm4KCY-6lOcImRBJ9AXaot3lUdFeaL8fJ4jNbmOSNk_1lqh6tt9KvH5LbTRpc-ysXMD2ziGrNpkZkQ-gJXc177tfqXSQFJ1cyDRuykJvx1yae7-V5tN9wjlt7cVjs4tquD2vnbjaMue6wKpGTQmLO5w8K4dBTb2HIABSyz9FKbt13Hm9nsGSoBdL_lJecqew0RsuAA4fhm9NqveE8l0zABBMdrT-8jUUb_lv2d8neWT7rSjJdjnx0DGi7yefxvub3PYTfziW6x8jRGBzJdeaBz-5aFxoVvrdZq1nnffaWUNvF2aSji_8SF3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حمله جمهوری اسلامی به یک کشتی
در تنگه هرمز</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/farahmand_alipour/6281" target="_blank">📅 18:12 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6280">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ksIpIrxDbGQc2LjkWKwIotylLeo0BMg8jI8b2Z_UZ8VPiuk1rchBB17zVnuh-ejqP2lAoXz0WGh8w4FwqLJyTUayOo1QjpXyqMIj3NKfpTjUe56hUObJsTGXYt7x8b3haQnI84guLxRFWig8bQITh3CIb0pBQ8n0c4LOEeWZp3LMluHXWKGXJOXbvPvbs8Rzdrn25lzfZ-FAjuntC6WG50FCovUGyRzKiTd5I6EavmW8hdmube7dHlQCIkjtrmxnYVYGPxOmFXbrH8BJ_rUbYXz_2wIoVB6j4roOg2hhvVyEYefjIDUEahK5oR43em8VALqv5Pzl47M6NWRMiflMZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
گزارش‌هایی از حمله به شیراز
هدف: احتمالا صنایع الکترونیک شیراز</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/farahmand_alipour/6280" target="_blank">📅 17:53 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6279">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">این سخنرانی ترامپ در عربستان رو به یاد دارید؟  پارسال، درست در  تاریخ ۲۳ اردیبهشت ۱۴۰۴  که به درستی گفت :« رهبران ایران روی دزدیدن ثروت مردم خود و خونریزی در خارج تمرکز کرده‌اند.»</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/farahmand_alipour/6279" target="_blank">📅 17:27 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6278">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">این سخنرانی ترامپ در عربستان رو به یاد دارید؟
پارسال، درست در  تاریخ ۲۳ اردیبهشت ۱۴۰۴
که به درستی گفت :« رهبران ایران روی دزدیدن ثروت مردم خود و خونریزی در خارج تمرکز کرده‌اند.»</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/farahmand_alipour/6278" target="_blank">📅 17:27 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6277">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QRBzoSRXYpVULdAQ1sC4X7G7HGkB8MkqqIcQERbsoBHMDNe5gODKhdXMYI4t4DPXHqMIWFHtq5emdLH2xJn8cJBKR_SU2-AjsZx5LAog6YgScr_OQL94kXU2mwyZpJ3AFDSPLZ58yvb5mKTvOBv-hh-ooUxMlIodG4jZwaIa3t5KRbiqBTuFZX2CC5FYTi2fA5gq4ghb6OGTjBp3p48oVEVP0yA-OxF8gFr_MmIAcJSNGrs0hfDxVh1eYHFPEJrofviVLDUm8mzJc7KsnxDCLl45faBvGOvdXGQp_iD8p30rAiKS5ttLrZprCqFq2RNzDi-ijmzK6vM5Lj_otPXWDw.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/3d8904c5eb.mp4?token=kSbrIFlVAuSZRFOxs-HkGWWQIshKHn2YlTNXurt9108lqkyUahcoUGkVTRv8G7nZUOKwq_7z8JM67sLNaHvcwz4-wd2wfuNcAORXk_tIbKeDkhnJo5ZfOI2xYnSXGbjo_LshpYCxYYQ3e2MercS3l3nriRegacQkPFITwgVjgG0HZYJvv5RygNppoHhxJOun1W9yZR6iANJkC6SD0tPZ9tixp48xZ4P_4vu5UGOYpYJRWb9wgJGD9FDgSP7-01-qYoSKI1CH58XqYydfcn5H4muRqwaahcxqJRDco9CGrBcAXt4p4wr7c-Pbb0NI5tvg53qo-DtuChT26JRiUX6FzhPDL2UNJpzICLLegwbWyKoB7z7maxmRNr19hzJFMWe4wrRdOfxMjMINgP9Z36HcuA4i2AkubXxqFE72-FOCjHbAhJk2m9HlXhqi_2yjfBuCZsm1EXL4BJDrXpN8sqWAIB5Q5LllUWHDIIO3MzSS9bPQWbkamITUbswf0fDIEXb1RQCiH6vdF2_JonmMLbrSdy3vo-Bu7Q1NvNnbH4jDhhPTb6g0OWVzvHQ7LhQJ2JMFH35AAPGy9IjnfxKZ4ljpRtLmBDsWppRD8HPEzBxMANAQj6nazrciOWPFAiki4Xx4ZHD_xRHNelGlNo-Yzu12TIcyclgAW8Cj2MiohABK7cc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3d8904c5eb.mp4?token=kSbrIFlVAuSZRFOxs-HkGWWQIshKHn2YlTNXurt9108lqkyUahcoUGkVTRv8G7nZUOKwq_7z8JM67sLNaHvcwz4-wd2wfuNcAORXk_tIbKeDkhnJo5ZfOI2xYnSXGbjo_LshpYCxYYQ3e2MercS3l3nriRegacQkPFITwgVjgG0HZYJvv5RygNppoHhxJOun1W9yZR6iANJkC6SD0tPZ9tixp48xZ4P_4vu5UGOYpYJRWb9wgJGD9FDgSP7-01-qYoSKI1CH58XqYydfcn5H4muRqwaahcxqJRDco9CGrBcAXt4p4wr7c-Pbb0NI5tvg53qo-DtuChT26JRiUX6FzhPDL2UNJpzICLLegwbWyKoB7z7maxmRNr19hzJFMWe4wrRdOfxMjMINgP9Z36HcuA4i2AkubXxqFE72-FOCjHbAhJk2m9HlXhqi_2yjfBuCZsm1EXL4BJDrXpN8sqWAIB5Q5LllUWHDIIO3MzSS9bPQWbkamITUbswf0fDIEXb1RQCiH6vdF2_JonmMLbrSdy3vo-Bu7Q1NvNnbH4jDhhPTb6g0OWVzvHQ7LhQJ2JMFH35AAPGy9IjnfxKZ4ljpRtLmBDsWppRD8HPEzBxMANAQj6nazrciOWPFAiki4Xx4ZHD_xRHNelGlNo-Yzu12TIcyclgAW8Cj2MiohABK7cc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/farahmand_alipour/6273" target="_blank">📅 10:20 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6272">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">🚨
🚨
فرماندار بوشهر: دقایقی پیش چند نقطه شهر بوشهر مورد اصابت قرار گرفت.</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/farahmand_alipour/6272" target="_blank">📅 10:04 · 29 Tir 1405</a></div>
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
  <source src="https://cdn4.telesco.pe/file/8e62469a72.mp4?token=iTbNWdpGiZgJEKj8MliR6ZYLdS09Pin6glu2XIHfbzr0pLRb08f4yC2s4b6cxykn1hkqYwNlXoaRzvs4lPNJlT63oyFZY4iP5b8gM4PAPOg21xiunUvSJufwAmV2_cUmrpHbBi4YfPQxIvM-z3QxST7_qwNwx8ETnhxA5QSleARfw0Iege9kb9-eD6iZR6YO4vkckk_aOwJpgQGxeL809U9Ek_KiBYweVpWH-sBRE12ANQ2yHpgw2fHMaVlyHGtWRaEapdBQ3BOTIh-UmzELLhhKIozvOUeGSsutwX60_w4mHdXhzYKrG3KxtHYVnbs0LRg9fLAv2Rmg7yYr02Jamw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8e62469a72.mp4?token=iTbNWdpGiZgJEKj8MliR6ZYLdS09Pin6glu2XIHfbzr0pLRb08f4yC2s4b6cxykn1hkqYwNlXoaRzvs4lPNJlT63oyFZY4iP5b8gM4PAPOg21xiunUvSJufwAmV2_cUmrpHbBi4YfPQxIvM-z3QxST7_qwNwx8ETnhxA5QSleARfw0Iege9kb9-eD6iZR6YO4vkckk_aOwJpgQGxeL809U9Ek_KiBYweVpWH-sBRE12ANQ2yHpgw2fHMaVlyHGtWRaEapdBQ3BOTIh-UmzELLhhKIozvOUeGSsutwX60_w4mHdXhzYKrG3KxtHYVnbs0LRg9fLAv2Rmg7yYr02Jamw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uWLSu9mZ3H1pZtUqU1sgNuvqS3stNPLsQtqXJx4PgPHL2p0YuIlF-LvdDV40cD5PCbPkUXBvPrWm-F0lx5tXpmgNABdALRU2lJMnkRY_WbaoPCGYDCqRAfgGVKobX7Y4chRi80KZmWuZqLZI3IdaB-9wPnCOSB5SOMY7x_dMHSlFZ4PbtKgYN41QPtL2eFDK3Fx7KgG-g0zT-9hGjevd1RmNN342VDLdTACPuYZXJep9HzNOJi2nL5oEs5g0KOcOb9rpmvlsg7pQD8-bsSwejWDLcwEg69SQR8nwJhzja1iv8p_EZLX7fOqi__JnUBUdwes9l3G508aXhYgCsZ7AyA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tWY7ADbO_95AGclnNhp7zrUzr9YuECwzLR5LuWAleNevbqvxSgzLaWLFWqjMOq8KjrNVYhOIeezH9onVq8EAOWSX62iF6HYkye6k2z_0PUVvLcYxvOJDqm178aITd1RWW7iKvpmuEVUUNyXia9wr3VIkO2uUMkQh9-4CgHYqmebcZ2yiH-IRwDWsHcmGP2fdhpcDNnryVUfyRQbTYEv_T_XedBDrnY4pt3Wy-Q-7r1d8ypkHermdgWhn7DME5wvOnbcP4E8eSyNhHCDriilvcm28goxotvBj7QPajxOgUOudsGBoQmwJktlzkOjzur6Hn7YkMwN-qlWqmza72pSeIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بیسیمچی مدیا:
الله اکبر - اسپانیا برد :)</div>
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/farahmand_alipour/6264" target="_blank">📅 01:35 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6262">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DuoGICKAqUzqtEpUQYBQz6Msv_t4KRw-iTsJdjLzHSpVNyeXKun86I6fi-y41IOnMJnb5kOvCLBeAOv6bRW-LmqBw3YOojW2HA4yiAzNSf6BWyIwPdGYCoSbVP9QzalrowVBLIvO_yVcXYGw50Pi8FypUQtpaJZtToyen0iZEg0fmsiSWwP9432djx9mxwaz8leRwyWoTQ4S4ftLXA1_Cii3M8PbG8FapSsTet3WCKHWxMVKAncl2iswck06sH-QfPwQG5BDpDqeBdWVfGp8J3VkrbjYlRjglBqvcnYwWoE8mSr2M7cg_ebou6ItiNsZLwEwdT5be94Laj_8FzhiEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/W9BII7iEucLtXYQVbDO_dJTCPD49rJnfWreq8toTLtUJqa4zJtFoLl9CTRZQ0e4lChckPPoA8qwqdw7e7Qpx5eykm0FGb58F_1nEFSOB0DsgWXIoGY4RCE9FhnypGcO2Ht6lCgmXNIOscly001ssst6y3noo0jEfQ8anKrqQ-b5-oe8Uct_gnVngvlMI341uF58bdNMlKlw48uBStL38To8zhnkoE6_zOo1J4MAjyEiStMlozpy9aybHxbeWv9J21g3HEQY5GJL5WQUZVLHtBGyZ1WoDUYq9JUq_0kdfWaYOI6f1NOtIlJiIDyD2rxn_2AfpJAU8WCxlB3dw9lkDqw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/baOF47ObiaTE8ULIPtQBY32N6k4-Oc51i-YcjM8pPe2Tl4UxeHZ2t4ZpU0tWRkVoPc1Ibf9AXox0EzCXxiqVi7N8kb_cvyKFkgfKQJyyh_axfl0Rd5qETw0Qq4y9_V7npgo-hHDw7vD-r-I80EIns-owj2ADCu3SgedmusgvgOQkDSB7lZShhOXQdPieqzZ1jSuwXmfcwoO9trvhOu3P5Cb3pBEcF_nYLxHsrPDyQyO6-0PD51gLyiiMNwco2pVBQyzHvh98JkGLJVVGmpm4ez_5MU6iP4lnyHNPJkjTMDCkCioVx8vQOE3grp2alKtRcRftzwO2hUxTmEHxTEEGeA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">https://x.com/farahmandalipur/status/2078890340753568161?s=46</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/farahmand_alipour/6260" target="_blank">📅 20:41 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6259">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IVplpUtnpyrG-kt26puyVKRXgT3SkPiObgnDqJLjepDRil23-HtaTL7NNgAQLuyd4cZ4zAOGo77PJrIQnmT8DsG8lsv8zbhvBTY4K2kwTYVFn1ncYyXdc84vr63SK6OIIAoiQtWAiaIg59T-CMUkMzAncK0GBDPleDcquNp-iB9AOcWzA8pX5rVDz6xKTHtA68cGyWhkkGHMHmRSLACRqLRyuIxOmCzmHwh8lQd74SkrE4gmX7dBjufunu91q9InPxBvG7-OnizEOnMUeMCOr4P9jS4j1x8XwKGmkl0ATGqKyHMDZWSQKUm7QQ4Up6eyXFaOqewVZ999QO0Cyfaxmw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I9Y8um6QvFOGSDuOLYPyIH69TmPBH1KycvRUzZ0iTW-zgzJk39qDQyCI_eN8fAQS4N-TEcSCEfbA2tqrNpDA6aX8H2zxMZGAATetHOuKKnV_TV0xA9LXxCyM2Ouyt4uCJWnyjUAswvZvTp4b-XG1WParqr2utXuFL28tLrEgMZ1E6BHnJ94npdkTgURg_W4jqADaAk46-Bmn0OYT6vfD6hgzj4t1jovkEPnWKhtCeXpQEyedNHl5QIast4ngsDHaljyO2g6eSegYj5ipOXXBD3QvwPssahGAyAPLYxxWlJS-TxqsDFLXSxKRnJJ8VW-Etu8hlJuDD3gOXUZkezpGYA.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/9a1ebaca90.mp4?token=Zt2ZiKKfKHM9-8rYHsmxr14QzxC6e6M5PeBzPt4-OQb-Wa3ojtppbLvJOrFbbNb4T1x-ohBUg_8h6skBmS22KS-g6tpmuYWu8UmM9_pa0nsaMYLcg6aSzgD5zbRc1GBdcZnuUHYG6MaXETwpQh7IY6mguE7Cs6cp4ynTdoluL7Hg7lAZUQt-Clha8ovWlYpH9bQjslBVIxPmPY9O6edW_8Ct3PTCJoGrXtKNJttla0zcaUkgm1YH74drCJTOfWKfTfGmWj9QWYDbxY0jLoIzwbXcVahuD-dggK1HMon4vDechy-Kj33I37Nmd4pitnsBfZLJJndZkpqiQMsrp05QBQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9a1ebaca90.mp4?token=Zt2ZiKKfKHM9-8rYHsmxr14QzxC6e6M5PeBzPt4-OQb-Wa3ojtppbLvJOrFbbNb4T1x-ohBUg_8h6skBmS22KS-g6tpmuYWu8UmM9_pa0nsaMYLcg6aSzgD5zbRc1GBdcZnuUHYG6MaXETwpQh7IY6mguE7Cs6cp4ynTdoluL7Hg7lAZUQt-Clha8ovWlYpH9bQjslBVIxPmPY9O6edW_8Ct3PTCJoGrXtKNJttla0zcaUkgm1YH74drCJTOfWKfTfGmWj9QWYDbxY0jLoIzwbXcVahuD-dggK1HMon4vDechy-Kj33I37Nmd4pitnsBfZLJJndZkpqiQMsrp05QBQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
آتش‌سوزی در نیروگاه برق صبیه کویت
مقامات کویتی: در پی حملات مجدد
جمهوری اسلامی، یک نیروگاه برق و آب‌شیرین‌‌کن کویت برای دومین‌بار در ۲ روز گذشته  هدف حمله قرار گرفته است.</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/farahmand_alipour/6257" target="_blank">📅 19:23 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6256">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZnPI9Z06e_cRwwJ3agq7WQbs3ynLp_SMG5oLtusnvL-rV-yGbb4xlbc5knyDiwzcCZIAunn9MxXC25FGmnku7-KWNKFTDfKSwx3VUObIiCxd6Q50LrD4Cx-M03ngIu_Mo8aK818UvbniRTX_XEEEh-j4ws0Feayf_emHSzdUheXgCHJNchoViAmoxUfWA7bbQ3Sk7aWY0yEjzGE3iWsNFu7eDZd-oLfZV3zThtCuFdEKTRPXnGm6lbZh7KhnhTvyIl37gZXaKymQhDvrOiCP-9htPzxxMafnSnU_OURiwLHyebtEgRmbFdWW5bQQxDV0M3QkgJVrK4YSmcOUMq78uw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
حمله موشکی آمریکا به نقطه‌ای در آبادان</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/farahmand_alipour/6256" target="_blank">📅 19:19 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6255">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ad154543bd.mp4?token=eox18mpk6Lk636AySR7cx3kXMKn1nKCiBVw4V9bBypS74Bgaw5RL5WS1gUmNVGkCc4pgpVpWsjmpscgt4qkQrGSPRCP3_5SoSLHs2QGI6q6Dg0yAQuI4reXuGoG6Zl4wzXsOZYeosqlk5Th0CG5BjJsrAEY47w0IHxBIM_diwmoudR87raK17Z4DwfMCOg_0cBSWcs_pgHr4LqixsPIAehH0e3A5bUCGmetvrZBro6uHwnexiAfkLRoJap82-14AAU2mFjWAAsUSmrb0fF3dp5vBS5CmO_3Mmk_UiUVaP5o5yFe0D2jEjj7sGAR3I1rcfcBm4EMAl66rz2i2_Fe6nw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ad154543bd.mp4?token=eox18mpk6Lk636AySR7cx3kXMKn1nKCiBVw4V9bBypS74Bgaw5RL5WS1gUmNVGkCc4pgpVpWsjmpscgt4qkQrGSPRCP3_5SoSLHs2QGI6q6Dg0yAQuI4reXuGoG6Zl4wzXsOZYeosqlk5Th0CG5BjJsrAEY47w0IHxBIM_diwmoudR87raK17Z4DwfMCOg_0cBSWcs_pgHr4LqixsPIAehH0e3A5bUCGmetvrZBro6uHwnexiAfkLRoJap82-14AAU2mFjWAAsUSmrb0fF3dp5vBS5CmO_3Mmk_UiUVaP5o5yFe0D2jEjj7sGAR3I1rcfcBm4EMAl66rz2i2_Fe6nw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حمایت مجدد نتانیاهو از آرژانتین.
دولت چپگرای اسپانیا در ماه‌های اخیر تندترین مواضع را نسبت به آمریکا و اسرائیل داشت، در عوض رئیس جمهور آرژانتین
«جمهوری اسلامی را دشمن آرژانتین» خواند
که دو بار در این کشور دست به بمب گذاری زده است (از جمله انفجار آمیا)</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/farahmand_alipour/6255" target="_blank">📅 19:13 · 28 Tir 1405</a></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iM9kOoO7TJ7ACuRZay-CPkRA5Rb48wARkF-6fDT-pjICA0KrchUqGnmF7fUwTKJJjMpkdU_ZFF27WZfb5LmnVvd8vAbCvWc3tBHqNeJSc0xJ4d2zWF7CYQw0KukCdbP_yEAiZI0CvJIhh2L06v1OKYtXnhnCb0JF2AZha5f4feCQxTl1aC0wmQmC3PH4BPFML65DHrvO2ThxBVn6av8jhEekjXWq4a_NRBdM0Hg3Of3xYMdFUkz24M-JynruxA_EwmmttHjjfVLnYVDIJhEsYXXlapbOkUbGzpEVLXyinxjOAyjUiGrTnPvURt7dRsqIaszSu0nVcIa0R2tbnEN26Q.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/d28653e7d3.mp4?token=Wo1MhfbDy39Rl1VrrHzCb7lkHfSRgq711gpd09eALPNbKG0bc2TrznHhKrHIp4MmrDAfv5v1u7pD40eaZu5BMWXUxXETVAUAVZPoiqFrKLpyBEiXy8mYCgLXf-f9q0bHhskvdQJAIAa_qU6-mJyC0n8T69cACn0MqBJ_1YCFFIj2z3VpY95HoWMzwLaqRFo8OqJU5PRN3btB-IVLEw8EttHbZKJtrzV1PlIruH6daO917HPkhOu_NY5zcofoUKUQoYGzgNUy99CqwwR3y3AAcPzm3HymeQy-oFTK0jkI8KTAlCPYriCJSHr76HgNSuYTRIBiyHsLa4-hwjK3-bHtGJ6-olrBQv73OjHcY83IzfCoZAM8VyxIICEfEHgt8gXnHDFajm8_D830_5Lflow_FnfO2G9FPbKYRSza6RI1BU-dOEGH9pzGBjNVLwWjssJO6GJIsc5KnYLtHLWdEZ_8IOIZqtzHcbYMiV8xNY3wWIpH4dQYBuJLxcEtfpG2ZvhXDa2C1WgPwrZGZwN4mgDPlrE-iigtWqZldUsVHhLiiBJttdD4MunA8dFUbmEDB1EIkbNMfX1V5eaAwS-H3IeLXDmIzqjOMkkOuDibipP5k7vz7xkgKkWKePIXkM6f4vJu18MCqp5Yz85StuS4hjFazqihnytN4kZNdtTCcp4RuA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d28653e7d3.mp4?token=Wo1MhfbDy39Rl1VrrHzCb7lkHfSRgq711gpd09eALPNbKG0bc2TrznHhKrHIp4MmrDAfv5v1u7pD40eaZu5BMWXUxXETVAUAVZPoiqFrKLpyBEiXy8mYCgLXf-f9q0bHhskvdQJAIAa_qU6-mJyC0n8T69cACn0MqBJ_1YCFFIj2z3VpY95HoWMzwLaqRFo8OqJU5PRN3btB-IVLEw8EttHbZKJtrzV1PlIruH6daO917HPkhOu_NY5zcofoUKUQoYGzgNUy99CqwwR3y3AAcPzm3HymeQy-oFTK0jkI8KTAlCPYriCJSHr76HgNSuYTRIBiyHsLa4-hwjK3-bHtGJ6-olrBQv73OjHcY83IzfCoZAM8VyxIICEfEHgt8gXnHDFajm8_D830_5Lflow_FnfO2G9FPbKYRSza6RI1BU-dOEGH9pzGBjNVLwWjssJO6GJIsc5KnYLtHLWdEZ_8IOIZqtzHcbYMiV8xNY3wWIpH4dQYBuJLxcEtfpG2ZvhXDa2C1WgPwrZGZwN4mgDPlrE-iigtWqZldUsVHhLiiBJttdD4MunA8dFUbmEDB1EIkbNMfX1V5eaAwS-H3IeLXDmIzqjOMkkOuDibipP5k7vz7xkgKkWKePIXkM6f4vJu18MCqp5Yz85StuS4hjFazqihnytN4kZNdtTCcp4RuA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/b5d96f954f.mp4?token=QME-ZGr2iuSPZisfu4Fl0GeLSiHxUcyQW88Xq3HvajJyk21GSVrUKM79jcaOQHsh-m1_ZXmyem8gFxmqe-QEYh-oAZHcn_4MDlVOf8ztqQAVuQB_18wIlitOQ1rdJL0kuQ89YCbWR3_rIXMePA5Yv5Gh6f-9UZRv_gAYGOiq_r4X-gbqGSk5qO3Qr-eLGGw9hvkcjXbtScQo4wWHSFNGpfP6rMzPHvoWpOD7X7wYbsXtByfZCoPQcSgTVmu8DHgCyn4Whx26_EhRlmpcSkiDHbtwRMWildpNAMPrOr3isS5-aTaSXgtOlhcKCOU9BcMpciR25GUsIl7waJiu1Gsbtg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b5d96f954f.mp4?token=QME-ZGr2iuSPZisfu4Fl0GeLSiHxUcyQW88Xq3HvajJyk21GSVrUKM79jcaOQHsh-m1_ZXmyem8gFxmqe-QEYh-oAZHcn_4MDlVOf8ztqQAVuQB_18wIlitOQ1rdJL0kuQ89YCbWR3_rIXMePA5Yv5Gh6f-9UZRv_gAYGOiq_r4X-gbqGSk5qO3Qr-eLGGw9hvkcjXbtScQo4wWHSFNGpfP6rMzPHvoWpOD7X7wYbsXtByfZCoPQcSgTVmu8DHgCyn4Whx26_EhRlmpcSkiDHbtwRMWildpNAMPrOr3isS5-aTaSXgtOlhcKCOU9BcMpciR25GUsIl7waJiu1Gsbtg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/3fcb2949cf.mp4?token=d2mZo952KSiSdcGBy20rXe96sMnbvPlbOT8fYxKTRAboNuRC-z7rpbcSuSLFEFGwDt4DMgidr3u0v2JS9mqcpbNmeofpRRWJ_hMBUTSQ55dYrkH7yprVygKveTCog-EI7TJqUZarYXa27vwwe4_-tv4JQx2kOjFTnxG0Z1AIjP0nBVOEkMSQPnVa37MmMU4gNUNZv-CovPbEUCOVjLBdg9umaWJJAW8plWoJiLjAYGtsfHAaef4bGBnAbkaLqORs77lCLylTLUHR4WkCex-UgrMu1iqk3t_vIUOJcmLQZXQODAtP-fJKcsuTaVj6XfYcYJyhSs2XABNP1MmgkhX4BX1U4Ca2Ok1yFvdJ0RN9wkXvZ8S0ZtKDbLLDfcVTt0cN3t6ohbH-lMEyKKAEPQpxASxlNFdutaR4AKCtsDbV1NpVzFA83SwGgF8bPENrfKPv7GdjU65OU-vvYtVMdd7gKJYp8VnX4AUDmckRWisBjs3ciAlsvFcljh-QZSdQKlMgwN120Ed2wkaoprW6IThc_bViiNOHHQxMMhgGS2C2y4Opr-ZNvi-2Vbum7J_ob5GhaXxesjvZiC8fQx_zUgmeXjivdhFuO9lVZv6P6Zh1ScsxLc1atrnkTVl-mQPN83HxAVRmOD2RNZJvBCVeAVNHbLMMnz50ML0QNLk4YITzcaI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3fcb2949cf.mp4?token=d2mZo952KSiSdcGBy20rXe96sMnbvPlbOT8fYxKTRAboNuRC-z7rpbcSuSLFEFGwDt4DMgidr3u0v2JS9mqcpbNmeofpRRWJ_hMBUTSQ55dYrkH7yprVygKveTCog-EI7TJqUZarYXa27vwwe4_-tv4JQx2kOjFTnxG0Z1AIjP0nBVOEkMSQPnVa37MmMU4gNUNZv-CovPbEUCOVjLBdg9umaWJJAW8plWoJiLjAYGtsfHAaef4bGBnAbkaLqORs77lCLylTLUHR4WkCex-UgrMu1iqk3t_vIUOJcmLQZXQODAtP-fJKcsuTaVj6XfYcYJyhSs2XABNP1MmgkhX4BX1U4Ca2Ok1yFvdJ0RN9wkXvZ8S0ZtKDbLLDfcVTt0cN3t6ohbH-lMEyKKAEPQpxASxlNFdutaR4AKCtsDbV1NpVzFA83SwGgF8bPENrfKPv7GdjU65OU-vvYtVMdd7gKJYp8VnX4AUDmckRWisBjs3ciAlsvFcljh-QZSdQKlMgwN120Ed2wkaoprW6IThc_bViiNOHHQxMMhgGS2C2y4Opr-ZNvi-2Vbum7J_ob5GhaXxesjvZiC8fQx_zUgmeXjivdhFuO9lVZv6P6Zh1ScsxLc1atrnkTVl-mQPN83HxAVRmOD2RNZJvBCVeAVNHbLMMnz50ML0QNLk4YITzcaI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nn-ZmLj0cVaHoDJuN2qnOHDxhJ4_9fesUQlyCiZSaygPZCpFKlTe728_B11sWpwbr24MmxROu_vbz2ftENIZvkiCbKZwRv39p-L_2QIc7PVu9bYHYJY7C4gq7MDOY-QKBsvOBzzbzD2kp6rRJiazcoOe64pz-eHWs8nUDNmVgHAz7SjQ_CGx411McVDTv0PniCfG0bYk4JZgPtd7GvuCzwUbKL16iIt6700c4I8nTXJ8jWjnalp9PNk8YVfLt5fYed7vk7-ykNk9QiL-69jYwszrPs3mCAdKfeUdrHaSMK15fLcAv9I2s6my6dqWDVr83GQ0BIxEEPKCliVFjxPiug.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/il21NAcCrWuBvCCLtlw88LcEf7Qe9kUdd_7anqo8wlbyjjdRgi7fYVXZLQRmLxciLKoWbfmnvTW1kbepeyMRt-M-OwCh2z2eO51JOcyO_mMwbfZkgYKwNDfetKueJdIkpc715P-pwnPqsD6BUQlt6aSLSGVN3_kk0mxeM0lPIRW4bYJ3yJGB5M8ibFSZCkkH_4qKaXjZfhRCP8pSOr1NPcNOGmgPX3pvoKkjnlP5bUJkdw4yPy2_LEm63ndh1IyE2T4Pfy4IQQ5xqS1Y80Bga2gmK79MbF3mejPwvqhxTiPUfSJPk0uCbz6mRDOYed8vS3jnr6n1X6WXXRNVF3rlHQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vfCCIOwiCbttZLhS0DvsQFGUkky2XSuACZ7Xz6Abyeyb7_grDOOulM7U6Hr_tpSVDjaoRzdOg8jQzr7D7JDCnibg-Edv6bocLkr8UP6uO0X2WOhC2FoT0Vu91zzpaolL2Mjr-_dfZ5DWd2bXKVX6hCGosqnGYbsTGvr4pF5m_fKbH7QOWAptn2fnAkXeisTxP42zZiio7FmirDczRIWF2-1PdzX_Kw0RaCMAhDwVyxxG5CNoSW2W1X1AK9PdN44J47nrG4uiNZ7_olc8X7S14U-XVpPJDhd4tkA5QtBAFXw8I4oLFiNAgI-tWktiaZE7CXPPvlKAo6F8D5SDo9bSuA.jpg" alt="photo" loading="lazy"/></div>
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
