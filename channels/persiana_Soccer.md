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
<img src="https://cdn4.telesco.pe/file/h-gvLBS3_WEOir7T1VuDkCGEwFaLuWplxFamZpQnQkgUs3Y228_R8MX40yoMwgHyDhewFVjaHssF5gJKvYBuyLft2g0HGO3oqRB_s8QY1cR7d6V0XCWC7Qzj6mCSI8KnlK4L4k-bp_LdOgjThIQtyZl1nG9HtCLekHpTAt-BM3Ai3YpWw77XK3Of3jTOj-wF_gQ-0uVHzTUnfrtnyHc7NrCRw4tqaQRIXeQHOJVdskspMHehlho6OH5PgfwWltzwv3RLXqc7T6Fmb9T6-s_cxs16P_60lrYZOlZgi2md6SulGr_C3Dp1J05vzSs50l3WxSIJlKNlEodCUAT5lN6QsQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Persiana Soccer</h1>
<p>@persiana_Soccer • 👥 179K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@adspersianaپیج اینستاگرام:Instagram.com/Persiana_Soccer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-09 23:33:29</div>
<hr>

<div class="tg-post" id="msg-22506">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kMhH7AKb4YvsTp-gDxFVmjm6d2-7qW934cz032BpOu45fepeQur4bysZF7NwqK5lkvhofHyMenbgMkDdSWI2KyJ1PU7JrDiKcMYsE4B3zlXJqn1DKArQ6Xm-09GLMhhbZtbnTxbxg6E-DMiL-3-8l8Th9XgrSs4UEtogbhcBxESgsA2eMLTXIgEUbDaahj7LpHu94aZ_kjrKKcQYvbUYpBqj175tqX1Dd0bZ9xI5Vc5Brj0l2caM69gU7G6E3TkKybOur9YqwsW68887Je3TY7pVmvtAltYsbWiExbupF_gSZ7fjDnk-Scn-Fy88RPgHjTyUOq-IeN054pV-3vOtdw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">▶️
ویدیوکامل‌ضربات‌پنالتی دیدار حساس امشب دو تیم آرسنال
🆚
پاری‌سن ژرمن در فینال چمپیونزلیگ.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 3.03K · <a href="https://t.me/persiana_Soccer/22506" target="_blank">📅 23:26 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22505">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/78d5a3b7a3.mp4?token=ZHdDdsFPzFIJ6uL-Udg5ZdzMwzjcgl-cK2VAgn8ez61gjWAXi3br3eguMHUvA5nuLfTmWt8GJSL5i9Ha-NhOtLTu4LAmxlMPUpSHMPkLGBal1OVw_u563CinAecVRa3S807nnSDncNzgeu9JJAirKMGVrldwKGL2o2pcjToVujxubUXPe6x4x4KAV_GudcsJeq2TBfjRvehTpRlOriN7aeIYCDlikwDQL9PWLLKPJ9AFjQob0MXfJ7a-74aRtOEKvrJ-FjIsta00Ws0aaX4wdvpLky0mbFmUHWTYmGzhXbnhpe666In9LxGui_RbstBsLZcJAcaIJf-knjmLwE1L4g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/78d5a3b7a3.mp4?token=ZHdDdsFPzFIJ6uL-Udg5ZdzMwzjcgl-cK2VAgn8ez61gjWAXi3br3eguMHUvA5nuLfTmWt8GJSL5i9Ha-NhOtLTu4LAmxlMPUpSHMPkLGBal1OVw_u563CinAecVRa3S807nnSDncNzgeu9JJAirKMGVrldwKGL2o2pcjToVujxubUXPe6x4x4KAV_GudcsJeq2TBfjRvehTpRlOriN7aeIYCDlikwDQL9PWLLKPJ9AFjQob0MXfJ7a-74aRtOEKvrJ-FjIsta00Ws0aaX4wdvpLky0mbFmUHWTYmGzhXbnhpe666In9LxGui_RbstBsLZcJAcaIJf-knjmLwE1L4g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
اینم‌نسخه‌اصلی صحبت‌های امشب عادل فردوسی پور برای دوستانی که قصد استوری کردنش رو دارند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 5.76K · <a href="https://t.me/persiana_Soccer/22505" target="_blank">📅 23:18 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22504">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/52a1e84d8c.mp4?token=LjYv_qBsHOOxvQ5sO5sDy6mYolhMKxC_Wv1YtfznR3ZpfKts-GXpuU2EXunuIA-_IkPxgQltou4_8r8BlPWUwcYMUZHF8KkNKccEdv6RA6WLF1xtJsw7_kPgOCLp13fjdAkepjYaDXUSSMy546yZvegX1McB1EScYsqd13SVVqspzCgqQgSLhqFadHJTSMe-3qIYqDAEOg6qSTypM5uUhWsFBlUT3rudqV327wHx1u386nXrR0Fb-ZQlGONcB2ywhAKuo-D__kZ_ZFExbjbApW1H9O-_ZH3zRpJADm_vmaD_e2-DhZlJYCfCpUTQNfo5t1vB4kI6WqueYPuobOtaug" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/52a1e84d8c.mp4?token=LjYv_qBsHOOxvQ5sO5sDy6mYolhMKxC_Wv1YtfznR3ZpfKts-GXpuU2EXunuIA-_IkPxgQltou4_8r8BlPWUwcYMUZHF8KkNKccEdv6RA6WLF1xtJsw7_kPgOCLp13fjdAkepjYaDXUSSMy546yZvegX1McB1EScYsqd13SVVqspzCgqQgSLhqFadHJTSMe-3qIYqDAEOg6qSTypM5uUhWsFBlUT3rudqV327wHx1u386nXrR0Fb-ZQlGONcB2ywhAKuo-D__kZ_ZFExbjbApW1H9O-_ZH3zRpJADm_vmaD_e2-DhZlJYCfCpUTQNfo5t1vB4kI6WqueYPuobOtaug" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
👤
صحبت‌‌های فوق العاده ارزشمند و گران‌ بهای عادل خان فردوسی‌پور درشروع‌مسابقه امشب فینال چمپیونزلیگ و تسلیت به خانواده‌های داغدار دی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 7.89K · <a href="https://t.me/persiana_Soccer/22504" target="_blank">📅 23:12 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22503">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QVqUl8-pm1K0ZmfQEVRFM9HTiAwRj-K1kiUMIZWF7Prw7ketzkEJXWdXvXN-k-rnEwFnPZxdSqVSNpmoNZ9xGxm6GhTEtcaCsdR-2H670xMoX5QzLn7C9Xt50zBMGpKQ9CToCF-2ugmvNsSLN9k1XcEMKpSw-j753ue8456GBpKkJWplT2O1hE7gr14xHst8WjYR_IZnA9O56WsSRuu_OXfVP34pVer3SPnhvNPp1Q0PkL6wPk48FKZ7IyOxasXH_5OA0DMNRulT3yFsOEgdq4YmlyVZZc610BfFOhMtPoYY-illU_AkF8OiqDLKhR9QpENuRdP7Mw4f_KzPWQ0Xsg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
لحظه حک شدن نام باشگاه پاری‌ سن‌ ژرمن روی جام قهرمانی فصل 26-2025 لیگ قهرمانان اروپا؛ این دومین قهرمانی UCL در تاریخ PSG بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/persiana_Soccer/22503" target="_blank">📅 22:55 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22502">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5d915ebc4d.mp4?token=O_h3BIez4CzGzhX_XdSdBU_Bu7ET9hJ4AfwIhn6KKAPuJTcKwi2mDtGkA_evsf0AGA7Z2yF9cLCN1f8jZSVoZA3ywIy6OwIoCrBRK6h5AyZ20dgWbkKtU1PE85cqtpmyDqyUcWXhXOrke-7vQjKK9iJH54x1oZakaOSNNf6UjNjhnVW7y-lUmFqDMVJh-FiRj7pzl_VNEPqknwRgRHwMX4GDSJe6S5bROOWaaDH1PCegHmUnxZ76OfcQzH4qGceAObMXwCtE0I5up5O_QPrZmtNA4y-fDE4rUSfP8cyRDhSVrX5BlpORX4gLhQce0Ynzc-ksrA6Gf9ABR8dujBG7JWue82sMGdFxVniEmcy3wId7tiGbSDWVhikpQ3V6nET68lUpT9xFTvYBKxPmVhD3ncYdHH_a3tGtz4qtu1xxyYAmyJydXmKLgX_Nx1KbO3GEmCb4PRa-6fxnalAkQmN11GGs-aTjOQ6qcdELKArfXGNroig_4zv22pYriyPJhUyXm7-l8toIIxaKJg9DQZGeQ6bhbBuQA252rEWj_UCiNigmri1jeq2VFl5tpKLv42Jy_3Z7pjaSJ6Oxmg3NK7cE3aBbGvLPyraTSddfCDMgMXajgRaD7D45yCAl5QjnwVTFkkWz8C84peW5GFznyI2WGkEAlcfi1HZqIlbiWKY8Yvw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5d915ebc4d.mp4?token=O_h3BIez4CzGzhX_XdSdBU_Bu7ET9hJ4AfwIhn6KKAPuJTcKwi2mDtGkA_evsf0AGA7Z2yF9cLCN1f8jZSVoZA3ywIy6OwIoCrBRK6h5AyZ20dgWbkKtU1PE85cqtpmyDqyUcWXhXOrke-7vQjKK9iJH54x1oZakaOSNNf6UjNjhnVW7y-lUmFqDMVJh-FiRj7pzl_VNEPqknwRgRHwMX4GDSJe6S5bROOWaaDH1PCegHmUnxZ76OfcQzH4qGceAObMXwCtE0I5up5O_QPrZmtNA4y-fDE4rUSfP8cyRDhSVrX5BlpORX4gLhQce0Ynzc-ksrA6Gf9ABR8dujBG7JWue82sMGdFxVniEmcy3wId7tiGbSDWVhikpQ3V6nET68lUpT9xFTvYBKxPmVhD3ncYdHH_a3tGtz4qtu1xxyYAmyJydXmKLgX_Nx1KbO3GEmCb4PRa-6fxnalAkQmN11GGs-aTjOQ6qcdELKArfXGNroig_4zv22pYriyPJhUyXm7-l8toIIxaKJg9DQZGeQ6bhbBuQA252rEWj_UCiNigmri1jeq2VFl5tpKLv42Jy_3Z7pjaSJ6Oxmg3NK7cE3aBbGvLPyraTSddfCDMgMXajgRaD7D45yCAl5QjnwVTFkkWz8C84peW5GFznyI2WGkEAlcfi1HZqIlbiWKY8Yvw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
ویدیوکامل‌ضربات‌پنالتی دیدار حساس امشب دو تیم آرسنال
🆚
پاری‌سن ژرمن در فینال چمپیونزلیگ.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/persiana_Soccer/22502" target="_blank">📅 22:43 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22501">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/50097d1448.mp4?token=lGNM6E1X3NJLmwAOAcyC6TU-uuDcfX7FvX6UZjwJEd0VzqDsr3N56aBzkuruZZg7yND7L-ZEkTaYtlCFYC8riLXPXbLJfMKj-mKcnTIV6HFeOLZk_W_9RYi5645tM3ZMN6iPZj-FDXMjMAUapvvXJkHQVZD76PfH-MK305rjSCVnC9gFSIA3zqzsj528RMjw7JF1F3AKITTkxTspQByq3wpTxMAU6RkE7cyLwb8vJLHgjuOjly_4mxX5w8EyLcGWZj7Kb_tstH0NmQ1V9vJ65IJiGiw2f5O4xNFvOreiwzSyZTiaMyinzzrSZhc0AKlt7-Fnd_FOHee_aYXIWYrtgw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/50097d1448.mp4?token=lGNM6E1X3NJLmwAOAcyC6TU-uuDcfX7FvX6UZjwJEd0VzqDsr3N56aBzkuruZZg7yND7L-ZEkTaYtlCFYC8riLXPXbLJfMKj-mKcnTIV6HFeOLZk_W_9RYi5645tM3ZMN6iPZj-FDXMjMAUapvvXJkHQVZD76PfH-MK305rjSCVnC9gFSIA3zqzsj528RMjw7JF1F3AKITTkxTspQByq3wpTxMAU6RkE7cyLwb8vJLHgjuOjly_4mxX5w8EyLcGWZj7Kb_tstH0NmQ1V9vJ65IJiGiw2f5O4xNFvOreiwzSyZTiaMyinzzrSZhc0AKlt7-Fnd_FOHee_aYXIWYrtgw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
لحظه حک شدن نام باشگاه پاری‌ سن‌ ژرمن روی جام قهرمانی فصل 26-2025 لیگ قهرمانان اروپا؛ این دومین قهرمانی UCL در تاریخ PSG بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/persiana_Soccer/22501" target="_blank">📅 22:41 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22500">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WhQeOU9pq0yJXgU9_FJeqx-2ZvbjHb9xeKLSpOHdoPg7n9ymgL0pPbNvfE3CLootEWJ7bXGR6VtGzgKXKNKaGmvWEzSChQZj4Qz6c4smrufkULGHBTkZlobRUvtx81Q3DzxTXXyhzf7ImGRxGTHfCBYP6mu9-IxKk6G7m0x71VxiaCru3fUNi6vOiRe3hd-CfqtuR3TJZFmKqepY_iPtKdQs44HglIBVyaykDF5kGSrFqaETNV6x-tch3OI7WPIwv6Jn51QNnhXDyhL_zO6qJIrT6q7J4wPVdeuYE1VHyG2JBc4dmhdN-CVQjVm_CcZ4ocpgwu0llFyyYM8N6vIoWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
دیدار فینال‌لیگ‌قهرمانان‌اروپا مابین تیم‌های پاری‌ سن‌ ژرمن و آرسنال پس از تساوی یک-یک در اوقات قانونی و اضافه، به ضربات پنالتی کشیده شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/persiana_Soccer/22500" target="_blank">📅 22:36 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22498">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c46R93KJ1KuIHx0rHROguWv4Nm5TVO2od1hT5Sc-L8I-DydwTNUrUSsz2AGlvTkgdTx2Bj4KIgGu8w1M-lt8XqBliwmUoTavfOP9jJLe2NHzNKcFLoXLEuxO49pHnp9pdBDcQDI_lHyZm7uLTW_frUtfUbTGw3gJiWUv6301f5pY-yx1ED5wqdwhKY_w10hqd8OJnbdVg5C3jQuzb3a52lW6OIf-AXWN9WLF0ZoHw0tJtEHWXwxZ5_FtEw8IPzEcanQdyNu01f098lbl1uOOOY8Xbrb60aKKW2jSqdHrLS54DM8x77wJeNI_1phCpzvW_-no0AhmK2QV-6eikojppQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
بازی مهیج و دیدنی امشب دوتیم ارسنال
🆚
پاری سن ژرمن بوقت‌های اضافی کشیده شد. آمارو ببینید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/persiana_Soccer/22498" target="_blank">📅 22:17 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22497">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AQoc_B05wBBog7n0gGTnh-dqjjlLt0ui5t81ffvL9g8FigQRbun2kKF5aikS1GDeWFncpMSTaFrhtlkUkTQjgr-0VwET45dsQg5D2FJB63F4JQf2b5aLmZRMEl3NmelMmgFQ77sGgFXAmhYRuZbeDSWqfh698YxtBRgZnRjvjHJ74NUDSgVu1sQcpuBasE0SueUIEnKA6wVuc-GZfK0xmqOmLDb0O_HktHa-ez_XX2WFFnPpI66OonypydMWxefwyFvI89CYAiec9pgzW_DkKYUcfQyuz_ZWzut6xBL9liLwFKwg06jvGCfasbqryloGFvym4me3e9xE5Qd5dsUFuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#نقل‌وانتقالات|سران باشگاه منچستریونایتد به درخواست مایکل کریک سرمربی جوان خود با ارائه پیشنهادی 100 میلیون یورویی بدنبال جذب فرمین لوپز ستاره اسپانیایی باشگاه بارسلوناست.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/persiana_Soccer/22497" target="_blank">📅 22:10 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22496">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Jw2GjmN0gou1ASIvJInDjHrB5Kl4h1rXlbcK0poW35msQQA0EpJw9rBXcf8lpCMChYByPQ7aYN70cKTICeo_zc8jW-4AkqWmOP6xSRQomJqseycKDtuKubMqNx1kgSe3XF1YQGwn9GATv5aLw4xIuFL0dnJejylZIB0yCw-eJWk_vh3XgcZraXve-7g2QQYwc_zbfsIwQ9B5EJOQutc0bDdJo5bXB-HoQqDKZfkUexkyCJ5SYUptdBNsvwi6LzlChtif8XdicVg7ky_4J3K_cCxEk1gQEyR9MX4Z3HTGKeKSN6pABjqBuUi19KQvd94VRJRMVydbU2ZsQzr75bSAkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
دقیقا 19 روزپیش؛ صبح 21 اردیبهشت؛ مهدی تاج با تاجرنیا رئیس‌هیات‌مدیره‌استقلال تماس گرفت و به او گفته بود که فدراسیون به این نتیجه رسیده که امکان برگزاری لیگ وجود نداره و بزودی استقلال رو بعنوان قهرمان لیگ معرفی میکنیم اما تماس‌های اخیر حدادی مدیرعامل باشگاه…</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/persiana_Soccer/22496" target="_blank">📅 21:49 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22495">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O96aoxv3S9af4fkRxQ0boK1gm1pA-t9gCTL18oiVnB22MbMYvPaYW8ZpuLge80kvsmNfWo1NG5D6fA2xWkSGKrtDEsrfvtNo_fzCbZrCopjRKZUMF4P5PivPEbv8RSDqtEUzZifjLsCD7T7k8zUi6KgZRTuIq20wp4mU0kP46dE2fef4WPF67pbW0P8Sibo9vElgrywAJTC_fRqiqUJz2j6ew5NtqBPWpuyslmuUgxXL5P0-s5PRkJvUCS0B_ameA011_UwBKcDFnP0k5XVkROEReD8hf3hBmjPabkyG-mVq3okO4jJTd30_dA7xumsGIEPIJGt0XaiXaPmvfu-TqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
تنها 45 دقیقه تا قهرمانی تاریخی آرسنال میکل آرتتا درلیگ‌قهرمانان‌اروپا و کسب دومین جام ارزش مند و شیرین فصل؛ جای عارف خیلی خالیه.
💔
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/persiana_Soccer/22495" target="_blank">📅 21:35 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22494">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AnDIProYWn4nFNFP_jByLxOfSyNQLVwbDgsGwmMJEW9m8TDrOKuO7Pc2_Sw7pkPnRIyJ1v3T-jyFBVpoI_cTSVVSCW2VquxkqbDRvP5vDc6mW1gc53voos0fWafpEZnx5y17CIYJSUin9yHO97VpxywCJo7ib3cVISxHVMtpGBWKEXSW1AlWaur2hrMqGC3he4XJr469MbXu5XUM4o9FwkBBZvlE-mVaIu9t-dTUVX07GAehOPMBIWXuUrGGEsJUFhNH0kzl-So-ek0gvOeOGisLPNlrz9pXVUvgPhuz2tNRqlA1L7Cx-t2ye6FKxZUZ5fMUz84n2aTYY9MUIG6hMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی؛ باشگاه پرسپولیس پیشنهاد مالی بسیار بالایی رو بمدت‌سه‌فصل به آریا یوسفی داده و احتمال قبول‌کردن‌این‌آفر فوق العاده از سوی این بازیکن ملی‌پوش‌بسیارزیاد است. سالانه 80 میلیارد تومان پایه دستمزد + 20 میلیارد تومان آپشن.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/persiana_Soccer/22494" target="_blank">📅 20:51 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22493">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Nnis9gXjq62ixFYn9xPoEDr7BqcF63LWynyzSjbXjRYZEEYchJW_HNGP9EouqR3MRLGsH9wRcUXCIxE9j6mkaLyHghHu1hJx-1CWAMDgeQzWYtIgOZg1kW_K2FHhq98BKV7X-U0KSCt_2-0f0xcHfkwRSpKAhlFCebsfZRGGOFOLrVvX_aqrgiWLFXl-hpE4ryGrXWtSrBu4un_-ua9POpqA4CQoIhEwCucYl12E1ul6MgGg8XzFoRRTm0w-TckcE17G4qw-kmRb6Cmhk88X7nVkKxq9xMGU0ZOZfu_uF6frCINtFREJ8NGR4uULfcUpKbUrxidawFJcFgIsxvZkyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
علاوه بر دریک؛ این‌مدل‌انگلیسی طرفدار آرسنال اعلام کرد روی قهرمانی‌این‌تیم درلیگ قهرمانان اروپا دربازی امشب با PSG پنج میلیون دلار شرط بسته.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/persiana_Soccer/22493" target="_blank">📅 20:29 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22492">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a443979ea7.mp4?token=ayWr8ai4KHiZ50f8ETEZeiGYNYmRQfGTM78pK3bJO84lUL-HSIwqsQtRaYyfehR_KL5aaxkPkBcC5nZVkL3M8q-0DH4SFGoPrqUG2Ae5n-OMmUfafox-Q5QToGk0zQoHfcgAmtfZed_BoJltXNzXEKEPLc9Nhyp5qHQIJTvPtIhjVTW0bZDrVtN3chfpZ52_EUjlPAaWXQFjulodsY9n0_zIeA3jm0zCXLSXZF1ZgX_vu2lREqCRMxkxFCYCxAhivXjXFmYWEr5hme4fsQ_UkqO1cb1mrCf3L_jYUrEhbffbSwYCIWwZdUXAIOjr4zR6oK--sn-oso8NB8dKJPYnBQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a443979ea7.mp4?token=ayWr8ai4KHiZ50f8ETEZeiGYNYmRQfGTM78pK3bJO84lUL-HSIwqsQtRaYyfehR_KL5aaxkPkBcC5nZVkL3M8q-0DH4SFGoPrqUG2Ae5n-OMmUfafox-Q5QToGk0zQoHfcgAmtfZed_BoJltXNzXEKEPLc9Nhyp5qHQIJTvPtIhjVTW0bZDrVtN3chfpZ52_EUjlPAaWXQFjulodsY9n0_zIeA3jm0zCXLSXZF1ZgX_vu2lREqCRMxkxFCYCxAhivXjXFmYWEr5hme4fsQ_UkqO1cb1mrCf3L_jYUrEhbffbSwYCIWwZdUXAIOjr4zR6oK--sn-oso8NB8dKJPYnBQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
دریک رپر معروف کانادایی یک میلیون دلار روی قهرمانی آرسنال تو چمپیونزلیگ شرط‌بندی کرده.
🔥
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/persiana_Soccer/22492" target="_blank">📅 19:51 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22491">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SHt6_Yt6meqrOf4-vGuq-zqiL32jUMI9hhom030SnZOJPEBnjRlGnzkXE5_pzlC6Ijv1F1_fwpo9e6VTjOdMKtRr-pU-AbEqKfr6x6rES4Rms7xWXbt3azwgQgzAMypi9LaRwDFjYKfthox0fxGso7LQkoi0DRNVPnHX4aRZiQ-srVk7YVjzQ45egIJFr5Js8kmUG2shNDmV4vbltGp9D9okffBU2EiHN6gksSo6eqEsiuJHAlufh_YX-9MhLXL6kUHDEKNEuy7K0gjhhdl0PuXcqZpusXgng7Br_0QJPVbwdMjfFkaGdklv1PaY9VMwESLTT6o8M8QX3c9_vAUmLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
همانطور در روزهای گذشته نیز خبر دادیم؛ آریا یوسفی و محمدامین حزباوی دوستاره جوان تیم سپاهان مدنظر اوسمار ویرا برزیلی قرار گرفته است. آریا یوسفی علاوه بر باشگاه پرسپولیس از یک باشگاه اماراتی اماراتی نیز آفر رسمی دریافت کرده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/persiana_Soccer/22491" target="_blank">📅 19:42 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22490">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PyGrXfNkUvyEg_rMLXIvMo7Ss4F7lshzepUYiz7WevBr3lQpxAl5hnQ-_3LS0gwKQ0BXD3q2vsasXyD7GL4JCjn1j4o6pKJoUohs4zP599VfYqvFyhMYOwS4JordIa0NuePIqRDC4NqmwiHXY489UE0Hpfm2fIm_FpYMJMH2Nvr9G4rAO-tCFvfqbwmCZyAHA79A45CCWuHXovlXs9wvejOT154Es2A2lGRj0f0wm2ao1QhIVUoSpma7P5vdwghGuo0SM2N10xaaz82_QS9-8iTnaXESjGGG14tdpLx_q5GzENEp1zdyeH-03LK-6WzUD38q60tko9HezqTh6s67SA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
روزبه چشمی هافبک ملی پوش استقلال نیز در تمرین روزگذشته‌شاگردان‌قلعه‌نویی دچار مصدومیت شدید شده و ممکن‌است به دلیل پارگی رباط صلیبی رقابت های جام جهانی 2026 رو از دست بدهد.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/persiana_Soccer/22490" target="_blank">📅 19:42 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22489">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZPpvilauJpHtqvc2IQrKj6sWBzdgk_XwaMGRHArbLTGiw6MOCckdP-1LzDfL-oHXDDvxa1vJnXqbB_bw4YaojWVB1Ci6DBgl6Q74qfDFU0avqavIX19MPFOBxWJpTHl0hFJ6HMXF6XWCJ0Ahf8v6HjJee8ZqfRJqp1dVEPSe0nLKJ3dfm6ZlEB6U9BSMWihv89VyC5O87WyQVPGWsDaFYPRkZJIBBtcBsKem7UhQ9LfgYU1SrB7NMRljGb4LHytU9SSea11f2GI8NOilMpkXxd8cHxA8KtUgUieFvOiqh0Qt8XmkdhOBstszcYUtqnaJu8uKimJbHQeoBL0QAXOQZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
بدون واریز شرط ببند و بازی کن چون وینرو با ثبت نام و بدون نیاز بواریز
۵۰۰هزارتومان بهت میده.
🎉
500 هزارتومن رایگان فقط با ثبت نام بدون هیچگونه واریزی!
💳
پرداخت مستقیم و سریع بدون واسطه، بدون دردسر، واریز و برداشت در سریع‌ترین زمان ممکن
⌛
پشتیبانی 24 ساعته
🌐
Winro.io
🌐
Winro.io
کانال بونوس های رایگان
g9
📱
@winro_io</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/persiana_Soccer/22489" target="_blank">📅 19:42 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22488">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sAj_yVlkhat0AjL7u5ERNx_UPtEjxf3tOx2CP7QRIikMVu0-wQTw8k57RrrsfWocYpvYmNVlNAXvuXb8Z922fdxKrePS7uutTQYqBSdnrIqy1nJ33ilmxuSBNm2S5s4IBwSHkS7rlF-iqijGmrfGBLU4Tn6PPIgxa7nR5CPZQYDJczz-JfHQETKT_t5zQHLT1uFUp_NZNV2jsXnI_SySu4CRz0RzTUgaLxK7o8FTuLcZSybWmu9gRrwrS0e6gftmosXGc5eu2eGVYxHZXijoO8H16C4f_G-uFFiX-iM6NPrAoL9bpZleX2HZsrf9_Z18YWKAmZJ-I4z0pKNKGkHIsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
همانطور در روزهای گذشته نیز خبر دادیم؛ آریا یوسفی و محمدامین حزباوی دوستاره جوان تیم سپاهان مدنظر اوسمار ویرا برزیلی قرار گرفته است. آریا یوسفی علاوه بر باشگاه پرسپولیس از یک باشگاه اماراتی اماراتی نیز آفر رسمی دریافت کرده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/persiana_Soccer/22488" target="_blank">📅 18:50 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22486">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jh_G3P5tCxtTnnAxbgbAoLI_yNTu65ryFvhy6-64rUaKpHZFYRdYkHWM3HOxZHmF5BbhRSBrjSa-td7IsCKZJc-DzzKVIgWY_uB4Q_AVEwitfRXhBZ8wlgrGwerd8vhvx5YtxIXk8kHJ5UWMDYYjPqlWtqoek2hxaWWxnmD7Bt0m1HP2h9EYugHeJyNVqDwvgOP1r_2KaV-f-uwHbg3d9qsHv3HKWhh9h6LZuiHlfnnfvyhNZ5X9nlG-CFveNqz7abc8gqR5FXK6vONl3UwuAV5ykkn68OKFkGFetiHNBIhlZ3lFf6Wrl06JuI_jvxvh_1znQGxVuyqd2HGFla5ELA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SoxC0d5ktucUyN7nU89A5vK18vYkgZbORvhSEodWxhV5ZZlLV5nbf-wJoQTZUmpZdpUHLrUQcoBBTo81ex6cOiW-DWfq2mnp5_NEszaSGXN9Y2MIfkcq_t8jjng54CmgkJ6NLdCFgW8-wwXDB8Rubi4KigSHDvGir6awZBLAOF8VcMULkiTqb7Pt0ED_okdbgiLG-_fEDL20_yZTF3xgHhM-ZwDB3s34xztwOGcmOJ57WxvSd0Y1vAsdqKbFR8CziZN4-eKrDzD_jtBPZBJgh0oO3x3gcVUOnflrQ3G6GC2AHs5ZHGxddeDfworC-aea_T2r-OREI6Abgb1TJVUBiw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🏆
شماتیک‌‌ترکیب‌دوتیم‌پاریسن‌ژرمن و آرسنال؛ ساعت ۱۹:۳۰ با گزارش عادل‌فردوسی‌پور ببینید‌.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/persiana_Soccer/22486" target="_blank">📅 18:18 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22485">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q4_0gv3ZHLoQ4zmVDyoBsibeTnVmDrQSkXloj_PbwML00isB2UGLpWU2cTKFMqiVGtKf7I_vcKrgd8zioN7jAeEHYDbVNVRRnfqXQL-oWvJ9QU0oSQUbAO4gk43bdhq5TBH5ujD97oD6wofBtb01kJtlK2PbT9UiPDZ8WVymDYFjJXaZvDV9igJLkfpCi-FtsdIXp6Ey8FiXGXOqH3gqXRdaLFNInLrAacv6jwmbwX4k5jDhzKpJ2_AgJvmLCrhJrANKGuNa8QSYGA8oQ5rL7Qzy1R4pgiSIb73qhLNhnMcf0hxZSvRjCIODS1ujidEmp8xNSFGHCqSLDfGlnolyBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
🏴󠁧󠁢󠁥󠁮󠁧󠁿
عملکردفوق‌العاده‌داوید رایا ستاره آرسنال در این‌فصل لیگ‌قهرمانان‌اروپا؛ رایا درصورت کلین‌شیت در بازی امشب، رکورددار در تاریخ اروپا خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/persiana_Soccer/22485" target="_blank">📅 17:52 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22483">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d6GgJGt--H982H2SB2Xpjh-Z3zwBpa5oM9NHYLhZSmupwDPuix5lMPG814AN9d09BAYO82KWzABYCt3R3r1bMG3ay4cRkTYAUgchQGBHNhjbsVy6oBSvJPo3ybURtU-o86v3fmci64mANXSkZOXGSMnC0mYa9dWZYJvPSsF6fV832GMpyQ5cY-QYKYG3BfpRajoY9y8g4NEEQySfUtAM3UH3J0jmiCv70xKRPgN5tg_umvT3I29xfI46vgO2W326SDuJ9qEAkjhps1Em1M-h49SAu9to0LLfgyUyyfXRe_DnbWHJ76IdP7Z0wMPsybPvETi6nboePbj21PNieOb4Ug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
#فوری؛طبق‌جدیدترین اخبار پرشیانا؛ مهدی تاج رئیس فدراسییون فوتبال امروز صبح در تماس با علی تاجرنیا رئیس هیات‌مدیره باشگاه استقلال اعلام کرده بزودی‌ازطریق سایت فدراسیون تیم استقلال رو به‌عنوان قهرمان این فصل رقابت‌های لیگ برتر معرفی خواهد کرد. چهارده‌باشگاه‌موافقت…</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/persiana_Soccer/22483" target="_blank">📅 17:35 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22482">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ATWwUcNBah5L6F9Ui5qiLrdhFbmFiFEaQlJl0_eYiuZUvLEcqXPC-q56amIBneYIkhoydTBrAfd_2mzrge-6Rw4owUyZS_x6z3dZU1Y19IdhxD7JOxujUFP55lJK71UOGlpWhhnjSr9JhJBfhOyOjohP_4QPyNSs7SFsMUUfJPxOIWmEEsb-b5xylkLeGjEvTvc3gKNRpafho3WsPh_fODfFd5QnK2VxvnKGuX9Wuoy1KCwoML0RSFt3EDLo0onz7M5CeqFL3KhJbQ2hXsszXbK4U2PlIGvD1g0brqlwCVqDUjqpmFLxXFEJWi3N6TDFp_fpIK2PvKZLNcSaQBI5DA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
#فوری؛ طبق شنیده‌های رسانه پرشیانا از مدیران سازمان لیگ‌وفدراسیون فوتبال؛ به احتمال بسیار زیاد رقابت‌های این فصل لیگ برتر بعد از جام جهانی برگزار نخواهد شد و باشگاه استقلال بعنوان قهرمان این فصل رقابت ها معرفی خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/persiana_Soccer/22482" target="_blank">📅 17:28 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22481">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Aparat Sport [3.6.2].apk</div>
  <div class="tg-doc-extra">8.2 MB</div>
</div>
<a href="https://t.me/persiana_Soccer/22481" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">✅
#مهم
؛ رفقای گل این اپ آپارات اسپرته که تموم بازی های مهم روجلوتراز صداوسیما و با کیفیت فوق العاده و با گزارش فارسی پخش میکنههه. یه قسمتی هم داره میزنی رو صفحه میتونی هم زمان هم بازی رو ببینی هم تو تلگرام و اینستا آنلاین باشی. خودمم ساعت 8 نوبت دندون پزشکی دارم از طریق همین برنامه نگاه میکنم. عادل خان‌هم گزارشگر بازیه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/persiana_Soccer/22481" target="_blank">📅 17:17 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22480">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fSvGjygDAp4449rJEQW5fI8nqGJvMzSu6Zwa3okYa7VPaqFaNnUxOoFZCs1VwHlxAQiY2uaikTV_j4swllpbkKemU8ceFMVEZLNnxKfBCHjn1ruXzFbyLshXNISdnX2X-dOFRvMP_NjOlyFjcKj51cWGQGHuNbPeiJXzFP-HUXvKwd2jBR-sgzQu8U0D_CSoISnOPTPE9UxL0N8vN333woyxK7qcmx3UDgtlfb_peg_VkZe96KDJPeiIUNnNV1yGaGsicn4a7ZXCURx_HR7UmhGOH_GbA27Cla8nMWoktJeTMf9kcUzgFV4ZKID5Y4KQdILjNLoSNJTX2eJAsnbK-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
دو ستاره سپاهان مدنظر اوسمار ویرا سرمربی برزیلی پرسپولیس قرار گرفته و به مدیریت باشگاه اعلام کرده که به هرشکلی‌که شده این دو بازیکن رو در نقل‌وانتقالات تابستانی به خدمت بگیرند. انشالله اینترنت همه وصل بشه اخبار زیادی خواهیم داد.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/persiana_Soccer/22480" target="_blank">📅 17:03 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22479">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/caf37364cd.mp4?token=TVrK46o9JczB8i2CXvAQxCJXwQU1MRayrmCBKDv6PTtyIDzLnxP7tzo5UI6tfY96TA8UgF6NVFysiDf7j1f-TumNvuWn7ad3ISB7m80EmT6NWjU2mfn2LGeld40OgLwckrgbCN1U-EzDi2WuoRVmoLJq1eues5ZXopd6elsGM3uXLNfxBMewYWBkdnKmYTWSxl5jJc8ZzZu-abSHDlxMTj2VH9gLiUh4NuoioT9UI0gvfLXc4l78yvUtCyd3MgiWw1SDMj64LBxLL-l8slpHAioWEv4ivULZT0IoX6DZhgwVPS7B94DDqCVP3C8abLK_OMt1YoPRaGWRIpxiY_UVbphO3UQcMZRBvhanELAH6ELuMyqxBo2srRF-J4gYpPORsbH4se5RJwUsWzjHh4LDHjMKKD3NehPN4wPpCCLArrmsJRYrBJ9wXqLnvKqEEZpKWbPSGiohRUa8Y1B05KH1qe4V9FTvwUN7rvLhglbBnpfhRaOAQRdJkm2z5gPyTLGihCTejdn3PNYuMIakUVb-OUS3z3jLhOBE9yshGz23BvVi3IOECRuo2W4v7mizrp5WHB094AlVPog3vzAYiG4usO6EfXC35Xbz9iam4LRG-TB88h5p-GOpvHa_Qk89zG4EphGum5T8VPqOxVE8vkvsf35R-OTAkAVyvvd6MT3K9MM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/caf37364cd.mp4?token=TVrK46o9JczB8i2CXvAQxCJXwQU1MRayrmCBKDv6PTtyIDzLnxP7tzo5UI6tfY96TA8UgF6NVFysiDf7j1f-TumNvuWn7ad3ISB7m80EmT6NWjU2mfn2LGeld40OgLwckrgbCN1U-EzDi2WuoRVmoLJq1eues5ZXopd6elsGM3uXLNfxBMewYWBkdnKmYTWSxl5jJc8ZzZu-abSHDlxMTj2VH9gLiUh4NuoioT9UI0gvfLXc4l78yvUtCyd3MgiWw1SDMj64LBxLL-l8slpHAioWEv4ivULZT0IoX6DZhgwVPS7B94DDqCVP3C8abLK_OMt1YoPRaGWRIpxiY_UVbphO3UQcMZRBvhanELAH6ELuMyqxBo2srRF-J4gYpPORsbH4se5RJwUsWzjHh4LDHjMKKD3NehPN4wPpCCLArrmsJRYrBJ9wXqLnvKqEEZpKWbPSGiohRUa8Y1B05KH1qe4V9FTvwUN7rvLhglbBnpfhRaOAQRdJkm2z5gPyTLGihCTejdn3PNYuMIakUVb-OUS3z3jLhOBE9yshGz23BvVi3IOECRuo2W4v7mizrp5WHB094AlVPog3vzAYiG4usO6EfXC35Xbz9iam4LRG-TB88h5p-GOpvHa_Qk89zG4EphGum5T8VPqOxVE8vkvsf35R-OTAkAVyvvd6MT3K9MM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
این میم دیکتاتور داره هر روز سمی تر و سمی تر میشه؛ تاثیر کیلیان امباپه روی هم تیمی‌هاش
😂
😂
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/persiana_Soccer/22479" target="_blank">📅 16:55 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22477">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YDXDNySxefPQf5ya4bJWPWltq_6fBrG1dz9ugCEux-9Llr7ZGNHgROD3xGc5uuNNcc-ufoeJC1R66ntajX_efL7RVqsGyVVhNxePWwLgjS8KnQ6CR112ogI8mYwI1hY9MeoD6bUu8p2_hzYwN-14Z-JzKhIpux1DbWcq7P6gqYNsnWZMIH9F_obRJ78piv62LlOSqA-ZQmiTdpJZl1Qa-MMdEFKft7IAqPpie-YmgZ60pIxiPnI8T_2xeRZT_oCSQ7NapfEDo7h27pIQlgLHKNg3DbavtTcM0zKkJqM_MfxT1-pNsIAZREsDn4daEal_3GBi_B2Y1VzwvUVyB33m4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/C4wiCrvO4MB_h-u25CsXKYKTtpah5zo59BdJrYlfv6gaOgVXJx6LSwZvoUGL9AwpZAs4poS4ZoeUfzHhC2j8a4unGZnj05FnUVN64I21fcNKl6hLoL0r0a3z1UW6zvsNyT9TVxdvKUQ6IyWJ7kqC0MEH4jMrL4ex7XtaF2vKiSUelmW84SbrT0nKQ9eordXYtdLhyX2QQOFt5tgGRbxQgpQrgxL61sO6rd0XWtyZkurdlNB53lAn90R14E41WvliZg7KP48o2hSqLKVG4ak8xQiqBKwHH9I-LywLWSiVfRwpWo41nZUn9-J7uD1TxnzPlkCz7qGMhTREu0P9b5r8AA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇪🇺
مجری‌ و خبرنگار بازی حساس امشب دوتیم آرسنال
🆚
پاری‌سن ژرمن در فینال چمپیونزلیگ.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/persiana_Soccer/22477" target="_blank">📅 16:46 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22476">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lB1GL1bl6aTTvmc7BEG26eXbIzCpTaNFPtcPCQ68xoagwqLKAxBe99056NT1ADC1H5WNAMZXDhOszq7KXKnwThxR5EiGxOF4Z9klYR6QZma_9sTFiVl7I4oMb2-nrE2cxHwF0-Ntk4TNI5ZlsBdGi2UMeWF_yDN5oDaM1FtbrKtpY8gtjPJNYVAh87H-hfzn05aSSI7PaYqpoQObgkMfNAYZ4NnGAVIO3TurtoQ0hKyAnlOlc0Geg4zFvfZ7qOpn_o5Xa3uRpeQGU_w1JaJ14ab2bNIySn4YGxdy6A-kmAKVfrH1oUGIcB4_t0ydp6lk7ToaufFU836X-ctNDJm_hA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
بعد از یک فصل اسفناک؛ آرن اسلات هلندی از هدایت باشگاه لیورپول اخراج شد. اسلات سال اولش فوق العاده بود و قهرمانی لیگ جزیره رو هم از مشت پپ گواردیولا دراورد اما فصل دوم ناکام مطلق بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/persiana_Soccer/22476" target="_blank">📅 16:33 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22475">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4d18fefc27.mp4?token=XXMy7TV0IpXroGT7Q3tmxvGJ_6FK77UgSy0aPk7XN3StNyKUDmHrEqn-wx5EUXzxbPK45oQKWknDnIH7ybSSD5LGeaxI6goxEtKlnVZBBvJ4t2qsvsn1RqSCzOJ4FE6qs-r_nbPWORFMEknbDsVkMcDxgmsuqM2O7LpO5710F8loUvYNDvAIQCCyZTOI-wuA4FV33M-4bQwqwZyW-mplgPbsK-pIzt_0qWywHsMhyV2XLz_XVsQnKJUSDrsujf05FSeY1WbgHEqaX7as4V8YvOnys8WCwr8Ewc-w5R8SVgGF06qV9CRx8Ua0pYO1GTRk4-JCU0M53NNtbDt7iy4SKQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4d18fefc27.mp4?token=XXMy7TV0IpXroGT7Q3tmxvGJ_6FK77UgSy0aPk7XN3StNyKUDmHrEqn-wx5EUXzxbPK45oQKWknDnIH7ybSSD5LGeaxI6goxEtKlnVZBBvJ4t2qsvsn1RqSCzOJ4FE6qs-r_nbPWORFMEknbDsVkMcDxgmsuqM2O7LpO5710F8loUvYNDvAIQCCyZTOI-wuA4FV33M-4bQwqwZyW-mplgPbsK-pIzt_0qWywHsMhyV2XLz_XVsQnKJUSDrsujf05FSeY1WbgHEqaX7as4V8YvOnys8WCwr8Ewc-w5R8SVgGF06qV9CRx8Ua0pYO1GTRk4-JCU0M53NNtbDt7iy4SKQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
مورینیو در اولین بازیش روی نیمکت رئال مادرید وقتی دفاع کردن ترنت الکساندر آرنولد رو میبینه!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/persiana_Soccer/22475" target="_blank">📅 16:27 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22474">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oEmC_Wt56hdUezatNN1eGLRrkq2elu9R2Zyj1v0bnfHaPUW1VkRFAAgbdItroMmuwuwigsixMTiATJz5u5bCxwWyEhIR5wv-8Wkw9_SwJBq_kVeKapU4kyEFLzn8zh8_EI5sC0s18AwJs5jP_RZ0o0cO5xCXttz2SLk4ciIa5--vZuQIt8lfPJt4VSp9dnuyo3PXeAlHR68J-hJuNvarmxE69HsdYCTx1elNRNLgh5TFaZ_E1gNhztcEClgqXN_qHW41coTMJWabkPe5Cpq5FjIxf6y0yofbvG-67w8CnX3eqeWDuiLs7RX-DnWFiuYGg36HnMPW7pCGMltsGRyx6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
#نقل‌وانتقالات
|ژابی‌آلونسو سرمربی جدید تیم‌چلسی خواستارجذب آردا گولر شده است هرچند رئال‌مادرید این بازیکن راغیرقابل فروش اعلام کرده مگر اینکه رقمی بسیار نجومی پرداخت شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/persiana_Soccer/22474" target="_blank">📅 16:21 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22473">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DvzQxe5BEwUDwSZuhgjqCwKNl8DpMKj6N4Er33mgQqOCBSc3KpjCzdR87KsOlmPVn3_UjSudZ9LDtYoPr0_ljj-06NRQczYvVV_-5Svpjn2Tk5WUlknhW4jdsw13UcUTEQP8Ms8RhpEDNiExKT1nBu9RmGowZqrIr6COhsCNQG2cwTR3et_SUN1WANJ0ZyQLTpiXuXjtf2H9xwP1k8PeYJ5ECjmj--GR-KkTU1WYjGssYhiXJd_0w_gnI6ZLZyCyt4-vd_O-XvFzpiz6gSEND9KMxs8qsz2oljVKXRZ00st6QhZOXsJvXz2lAsV2RWgzvyE8htkkpqQa1vQ2E9Xa2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
🏴󠁧󠁢󠁥󠁮󠁧󠁿
عملکردفوق‌العاده‌داوید رایا ستاره آرسنال در این‌فصل لیگ‌قهرمانان‌اروپا؛ رایا درصورت کلین‌شیت در بازی امشب، رکورددار در تاریخ اروپا خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/persiana_Soccer/22473" target="_blank">📅 15:23 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22472">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mZChuljK3MeGb9OkE45w32dHxuHbnjIh2CRvAiiDjTBeYFyDCMM9Ia3a-QWLn73ylNgeQtfcM9YEeSTnSOYlR-_aldzTQ2qpp1WWljPjnAe28aExvHIMOjWabziQHdasiR4GyOhE8V3d4iFPbCTLB66JeT5sCKxF5b8SufrEp0xjzcks-dR9uQD5ftZ6veS0EIoB0yiKGlJc9-ZJzy2T5DNKhIcBan5YrZwisKkb05Q0n7Z_RerLnkurDcc3RHlBcbCE2E0OoTkig1nrx-EAJAXMeZ36gReJeZLkJa2T3GU5p-jiFvnXWjOthfFowKnFcOb6va5SRyNgE5yxMFfodQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
بیانیه بعدی اتلتیکو: هیر وی گو؛ برای پیشنهاد دوم به مشکل برخوردیم، بلیط کنسرت فردا تمام شده، بنابراین پیشنهاد قبلی را با ۶ بلیط برای کنسرت یکشنبه بهبود می‌دهیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/persiana_Soccer/22472" target="_blank">📅 15:16 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22471">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VrccDkt0QtKcEnEa5HHww7-icNDGoWpnhbXizVjnfXSFdniEpiSWjdNHa5B79KShBGCg1eRIy6nCG2JwWZLxbFIGtg3JUz6tH0FnfkSdeqaZgyr_pQLjD58r2_PUUmddIGRIx_YU6yksrpb5F_okd6Fg2EJqsfUMQiOJsy8_WPdOGGdLxCKu0EaovgQnBjCufTDRSmzW1rBBKW23nPb49vKFGto-Drcbb9-E88BCcnVlfnEyIZSDyRAPtf5gEv7TxT6L9yxhozgfK9z5Gwmo71QRSalQp-W9mhzYgae6pqMRQMT1iironhSNCxVX2p4BlaYgudCVQkVizqvVImRZ0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟢
سیدمهدی رحمتی سرمربی خیبر خرم آباد بعد از اختلاف با مالک این باشگاه از هدایت این تیم استعفا داد و به احتمال فراوان فراز کمالوند یکی از بهترین مربیان ایرانی‌هدایت‌خیبر رو برعهده خواهد گرفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/persiana_Soccer/22471" target="_blank">📅 15:09 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22470">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OLfV2-VsGSQtyU_28pMDlcHhMCK6EQCPwEGTKj-8NWGyaUy29v1MjBCsqGcmd96TYyFB_bICoTyiga76fPLzUWTTQsvqPNVC57NFyu4FoCpO09iI4Ef5FOmAbEdlSi1OBTj0FlIDtSzPMt19SR5af3ADSDbZODS2Iexdl_4aNbtBHbtY_X68yuIbo-I8B0D0IVq7Pf_Loj8GrPrVanBN5ge5u1QESSL8ZbxhoY_3B4VW07zTk2P5Uvlo2wuyQBiZrkX8X-_FXDviDdfqfAWpI_mpeE37evQRu--018rMyhnThtqG7mqnWYFNHEyjhERTCvZMo2py1w2NJYZsJ-nd3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
بعد از یک فصل اسفناک؛ آرن اسلات هلندی از هدایت باشگاه لیورپول اخراج شد. اسلات سال اولش فوق العاده بود و قهرمانی لیگ جزیره رو هم از مشت پپ گواردیولا دراورد اما فصل دوم ناکام مطلق بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/persiana_Soccer/22470" target="_blank">📅 14:45 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22469">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bMbaZTqmTtEQSv31YZ_q1CiRIoui_n8kBOVK-D-fb4lENGfavygZekRq3bbGvlBgwSyrED4OXUH1JuP1aBbLOgo8yXuAQTNgdt1aRsn7QybbAW1hHJeyAmfhJ56LpOfOI6Uo9K79lv-7ybK20Fh0YhFBiHU24aRhKinlmes3Rcb6nQc_KUx0XPxQiH5xrImeJfhFOiIpXHRo8URsTIkqyv7amQvHU9vqHHowK5Myikg3MgjInbYTHH-rGXcGdrKQS-Eh3W4I1UJ9C9N9doZT-gVZ3W3CYdZTu8EkQPwVo6Mtqut0pWvu7dQOPXD0xfLSPa19_I3J0x7kTn_OBaoLTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇫🇷
🇫🇷
#فکت
؛ کریم‌ بنزما یکی از بهترین مهاجمان یک دهه‌اخیر درکل دوران فوتبالی‌اش تنها یک دوره درجام‌ جهانی برای فرانسوی‌ها حضور داشته است!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/persiana_Soccer/22469" target="_blank">📅 14:34 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22468">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gwxZxncMLyIqqQwLtQguNNGqye-H8uc9IQ0RzsP3u2KynNq9ZbdG-xm3SljMWAwht58c9bfyPKDNigtgYUhaN2_nbCV0km3uGIJgE25QrJZ8ckNXlBPGwFTv0pWjICnwWbGZYe1eKAOqjy0umoEnEqIWVYEKIA9VKh_loF_aUNudR0EAcx57b1qYzWzjgetJyavJOByvL0rfcUFyBXVyNTs30Bu0F5PTIkC0tOELV4JjV7KYjmwnp4jW3lVKpspsA3QO11ble14glKm1RfTLCoNzNGaHYyCeIsj7KdHLADlMVZvzq5xtKmQHefbHm25QiixU-EWVhqDCnRxCj30luQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇺
🇪🇸
پیش‌بینی ژاوی سرمربی‌سابق بارسا از نتیجه فینال امشب: PSG بانتیجه 3 بر 1 آرسنال رو میزنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 30.3K · <a href="https://t.me/persiana_Soccer/22468" target="_blank">📅 14:18 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22467">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/msxhkPwNPu30IpG1eJnQfVKULSZN7xSXF9cfBSt4yDvacPxOkjpebkvHrhV5T6dTDiOtkFj18Mc2E4W6wBLIBW9Pt_lAc3ij_H_MnjjPK0KAtmFMx6dj8vrn_RJEIMaQUQirxuGIszjt3YzYTcN2J62roG9kSF7LepqPwNKlA1XhJZ6-4ezKHifOWF4YG6Bc-m7C0HZpEoLS7yfCyDv6y7ypMCX10JFucN-zBnoZzMBSLv8pGBL-Lk2q2AP05lBdNMLZIBbWE1MAlOxuodhy400K5GRlToY4pqvxr_j6R66j0ZTobZVSqDRk_Vfii2zdcgsNRUQAequEYGXc16z6Hg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
باتوجه‌به‌‌مصدومیت‌های‌پیاپی در فصل قبل؛
احتمال‌اینکه امید عالیشاه درلیست مازاد اوسمار ویرا قرار بگیره و ازجمع سرخپوشان جداشه خیلی زیاده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 30.5K · <a href="https://t.me/persiana_Soccer/22467" target="_blank">📅 14:06 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22466">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QZjGZepAQL-Ta0R4godpqmFNcHbN2-azWNrpqGtH67aPUfYJNA_pHwncErQCqHaT5FPLNAhgDmamf7gBbVhT-BZFbKugi59tmFJ1Ec8vLJlURMh01DF9bh-pUU5ZwkytOr8VsPuUn3OK51oELGb_h3uInzOPnpeXMiPT09DlKZ5VpWNy4ZhI0igmPve-cs0zMaDLiMP3h-qxMqxUTITRU85r6UFehDJJwZgk-JYOol1RXGMGanUlvXP-5w5Y4BRs6szcZKc8J2beeEZs1cuSY_6chlYeV_rwk05JryubJ_9rI4losBSkNndNsN0dRY0AMNxI_xORxmPhR0rERfmMrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇫🇷
ژول‌کونده مدافع میانی تیم بارسا با پلی استیشن یکش رفته اردوی تیم ملی فرانسه برای جام جهانی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/persiana_Soccer/22466" target="_blank">📅 14:03 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22465">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AefGZcJNXuK7YrAk99Uqtelq-vkpX0JYqx9bZYl7NMRlQmXeDiCeR7JMUIRBtpLhD8axneYA0rJtEWXOiBP8Uoc0Gtwt7HUT8K0LX1rD8fzeQvOOA9L2Z7WRL33yOE6L6KiF0FFKwTwhLhzpZu0qTyKWJuTZLWCjt7lvwJtNZNWw6JuUqLPLF_x237kFKCY8Opwsf4PDn-GXh9yUJ_YU8GO4GlzqWtdk4WDeBmiyIAOhcq6uANH--lzrmkxtm1YuxqoIIQUmV2xmzn6sqowJlAzOkjF084_qbRrsTCvr7g3juS6fugbOa9UZQ9BEYjbpJsn5ZW8Q95UUUw0gAm39SQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
👤
#تکمیلی؛ علی رغم تلاش علی تاجرنیا برای گرفتن مجوز رسمی فعالیت فرهاد مجیدی در لیگ برتر؛ اسطوره باشگاه استقلال به مدیریت این تیم‌اعلام‌کرده علاقه ای به بازگشت به ایران ندارد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/persiana_Soccer/22465" target="_blank">📅 13:36 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22464">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c52DZ49OfDrIBCmq90ZhVaujgNaoZCCj8dgdjqifZ6S8EaRxMvffA817CeSq9TW2aA03XEmZSe6R2wdAZXjpJCyR-N_YmQ2pJQd2q0spRlfpMBV_rvF_YvAanHA0tYANfpKIZqUMvBELTQhH0xovQNRbZsxGIZh6CEtLRsOaQ5BXmtKEzu6IVMluotRJO85qobP1VACnS6IBV7e1OFlCx96KHatCetchQDvHHqirGCzXIaDw_AoR46Oxklwn0v780WEN7YPmwFpvhpn8F6CTLVN2aba0zP8OVelusbxzlzEi8s8yPLtExtF_Bk-UWBah5mtWQ0FLkKi4IgwxX1yfzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛ استن کرونکه مالک آرسنال در صورت قهرمانی این تیم تو چمپیونز لیگ قول داده به هر بازیکن آرسنال یه رولز-رویس فانتوم هدیه بده.
💰
این‌جایزه بین 530 تا 580 هزار دلار ارزش داره.
💵
ناصر خلافم قول داده درصورت قهرمانی پاریس به هر بازیکن این تیم یک میلیون پوند…</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/persiana_Soccer/22464" target="_blank">📅 13:30 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22463">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TPJ42_R5FvYsJSCl97DoxshD3nBN60Q6pP82MZiBEyrw81l1aVXrMZyMt6V5KJ8NXe2HIB-QgtXsU03UC-FjqJkNQh7tSc0OM-K6MHai_fEgIJqr59x77dyTpcRnezMJMsKb-lbvZqk43aDo5bWVsUzMQUA01-Ewtl9sQvcSHuHkuu-5tmQ0AXJO4w2tUml3UtDyGB-Fcc7gSFqrmZaDoSu2wOBEa3M3mHYAxenMLR0x9wCYsmeSHrZmC_cyonD0kZhOKGGYjpIh4q31pqfepqphWATnEyysEXlnyll4ZpK2ZLmfYR-bvk5N743nvJPuFTKg7VHF8SSJLjf61jgMLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
#تکمیلی؛ علی علیپور مهاجم 30 ساله پرسپولیس بزودی با حضور در ساختمان این باشگاه قرار داد خود را به مدت دو فصل تمدید خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 33.4K · <a href="https://t.me/persiana_Soccer/22463" target="_blank">📅 13:15 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22462">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YMLTX-iFGpZK7r9vFY8dVNr3hGqhsX5lSRdohlfP-lf11TpPpNnmvnZ0br_d_HDCnP0OgreSPqmfTfuSK2Kb_XVhDbtCZu2zqfRW3RMMyOIPnamB3FhqLHK_FTv8MJo0ejy0jbsMqalIzs116op0rc2S0KtkCnyAdjrRPM0GAJOR5tlrkGnhNRvb8R866kBA7WBuZI85X9WaHere4miOuXKSs0GBmeUZKpAp-lwOAxsHLR9CUueVxZ0D-OqnYYSRvtSaayulmAfaMJXX8csMHn2JqzeFYwAprYyxQcJCVcpqBGWdnGGgLxKjtITYJ7NbUIIim3Sg0dDopK-mgNU9ZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تایید شد؛ با اعلام ایجنت یاسر آسانی؛ ستاره آلبانیایی استقلال برای فصل بعد در تیم ماندنی شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 32.9K · <a href="https://t.me/persiana_Soccer/22462" target="_blank">📅 12:59 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22461">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R2i__7yXT5AoXrSOmrnlzpOyrS_QKYeDs6WghEHWKNKS_e13pMnN6yH5SQ0L7dhBpYe60OKme3ZDszGD7Hug9evZUn8S-2upRC3sAkk4t9br1T6LMKMGCKuzyS9re5-Dl8dCVRp-P8UBv6ernYPr70jxh-Y1_2_qUGB7uxH0yNYeOLc3ljO2RsbrphOHtQSl6D_5bNNGKvsYeADG-FAbKJZtwb5sZTSf_lLemhU1Itj4MYZgUZ6pdsWYOQ1X4TkbJTwDxCD4oEgsaqRz-4XtDFz4mjdIrFMY7lzFrHo3Lx0x5T5p1kDHAYiNx4V-7z2tzYgAQpQSUhB_fX5EuOFZPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#تکمیلی؛ رسانه‌‌های‌اماراتی: علی‌رغم علاقه شدید فرهادمجیدی‌به‌استقلال و هواداران این باشگاه اما اسطوره آبی‌ها به دلیل حکومت جمهوری اسلامی قید بازگشت‌به‌تیم‌رو زد. مجیدی زمانی به این تیم باز خواهدگشت که دیگراین‌حکومت وجود نداشته باشد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 32.6K · <a href="https://t.me/persiana_Soccer/22461" target="_blank">📅 12:56 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22460">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OocCeQCDrfVxd2KUE_fyBh9QsZpTKwfKBFfHM4olN39H0VUsf6PPGrtiCcWg50PF5aCOWBNW4508luMd7l5wBOwYb5g_98do4k3fw8x9fkbdluhDDVIX_OZd66HkG7rogMYXLqw5IZ2mzSK31hCoGHRLiS6OkrCt0W3v8pmW5SwoUzaBoaq-1QbLe1dPrmp12dpTmyl3dtuIlFt6iuljxyq7RZ3rHFtSS94N9PRH3QO6KyBOlRFKebj23XJzOQGZ4sNrgEpCV9c2UaxWL7x386mWzR23mSp1Hbj6gOV2ybjKTK9moc_B0mBt9zftFtZuIePL5todQT3SyBbgrZ3j3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترکیب کهکشانی و پرستاره بارسلونا هانسی فلیک در فصل‌اینده رقابت‌ها برای‌فتح UCL؛ به این ترکیب به احتمال فراوان برناردو سیلوا و کوکوریا مدافع چپ اسپانیایی باشگاه چلسی رو نیز اضافه کنید.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 33.3K · <a href="https://t.me/persiana_Soccer/22460" target="_blank">📅 12:21 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22459">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5359012d10.mp4?token=KHicVzJSYVY5ZWCfTLQN1FbiS38evSMTf83cGMtswePKfvBDPKbLV9VJJRpo59ZVAPSoci-Y3TfuPiajHimOx9vImUDCdK9v5xbBWFxcmeNLmdFyr-guEmEw5DjSRjX1iGWoCnWyOEglPEuPvPQtyh34_ooprocrka66wFPEfiDUybhSh21Fe-jtJkAZe74H0SiLxoL0Hw6oIDdamzGyED2KmTP2MEfaU9OyZub0eBvqMyV2ublkOsjAqQKwGNnzgPHfdcNbxmANTlwx7zZOXIMxkXunm8kh1gdKr-eN4r_h75PR-6kNgKhbQkeKB3cTDkZ4uE_Sunnz1_YF1fzZxYWv6shzlsZLDRrE4jz_bBlnpyoLxaxdLvz7Hcgo84iAUfIR9QdCDf8yNkYo06LKt6mqUx5DlXkOe7rJKjngaHOjN3QbVrCodUlirwrUkesxjkFVQ4309sP7mAYsqa8hedFe-VuXIndjlqKW0ITW48FEMVoaPEo_CAIitMKvLi-gu7jiXG_KEwxT1a8c-ta7LBAtL6bY2mRidnOIbIAoSUwQ9osvwkbVhZefJjnUrvUiAtNMPxMj94-6iRb-SjC0ILFR4ZW8hTj5FNrW82scQQtTGVIpWMVsA3--tDMsvilcktEzSQxlRndWDiUnyCXCfmnPWwp-upgztXTqQHllxsA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5359012d10.mp4?token=KHicVzJSYVY5ZWCfTLQN1FbiS38evSMTf83cGMtswePKfvBDPKbLV9VJJRpo59ZVAPSoci-Y3TfuPiajHimOx9vImUDCdK9v5xbBWFxcmeNLmdFyr-guEmEw5DjSRjX1iGWoCnWyOEglPEuPvPQtyh34_ooprocrka66wFPEfiDUybhSh21Fe-jtJkAZe74H0SiLxoL0Hw6oIDdamzGyED2KmTP2MEfaU9OyZub0eBvqMyV2ublkOsjAqQKwGNnzgPHfdcNbxmANTlwx7zZOXIMxkXunm8kh1gdKr-eN4r_h75PR-6kNgKhbQkeKB3cTDkZ4uE_Sunnz1_YF1fzZxYWv6shzlsZLDRrE4jz_bBlnpyoLxaxdLvz7Hcgo84iAUfIR9QdCDf8yNkYo06LKt6mqUx5DlXkOe7rJKjngaHOjN3QbVrCodUlirwrUkesxjkFVQ4309sP7mAYsqa8hedFe-VuXIndjlqKW0ITW48FEMVoaPEo_CAIitMKvLi-gu7jiXG_KEwxT1a8c-ta7LBAtL6bY2mRidnOIbIAoSUwQ9osvwkbVhZefJjnUrvUiAtNMPxMj94-6iRb-SjC0ILFR4ZW8hTj5FNrW82scQQtTGVIpWMVsA3--tDMsvilcktEzSQxlRndWDiUnyCXCfmnPWwp-upgztXTqQHllxsA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
پنج‌ موزیک رسمی‌جام‌جهانی دوره‌‌های اخیر؛ تنها دوازده روز تا شروع داغ رقابت های جام جهانی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 33.9K · <a href="https://t.me/persiana_Soccer/22459" target="_blank">📅 11:24 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22458">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nL3VYUq4bTkyPpTNw3SgVzYcKe1_HK-KUp36HkMafIXGgBOHq-4E4fYdXbA-F7PNu-KWHciunmHTLiqFBVkPRQCer51RN734gMwIh_J3nS5j2vzRN84Twwwiwfq-VFMHTH0cMBZB_E9OlXPD-KykTvsUSTwjKt6JuTHDm6LhSA8bsjwl_0_z4ayZec2-T_V99oLVEyKXArdEl6xwzYRp6Cgl_nXcYUjNZftmXuWlJ5ZPR_XQ8QltKa32H1YSreIZLSS8CqVqLtuQzL8dJG6YEJ4SeqWvAJhnOEZmaa4FSYegZ9M4WCz51QSVn8fYtxJnDmgnH9Z35Z-iBTFiHTwAGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
مدیر برنامه‌های نیکو پاز: ما با باشگاه رئال مادرید بر سر تمام بندها به توافق کامل رسیده‌ایم و نیکو درپایان فصل‌جاری به این تیم بازخواهد گشت. منچسترسیتی، چلسی، اینترمیلان به دنبال جذب او بودند اما نیکو علاقه داشت به رئال مادرید برگرده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 33.2K · <a href="https://t.me/persiana_Soccer/22458" target="_blank">📅 10:59 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22457">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mfOu6DHsvHWnwVwG04M4ByHkKvseIpJRd7UFvwtCFCJFmK6G_m3yYQ4n5zIzLIOD1vOM6nZ3yJ9eL0WNRn4735i0OixB3XUpt2lcfcdUAZRnp6nbt8iN88dPcIzysCNvoXg4kwSRuw7qNvZ_spT1XEgvFb3aDQveelyihKlEB0SoaxgWsSe6h53BVpe5h_2vrGWW-GJm-kSDnNX2RZJye_d04kVXI7y1IxYZafyyyRYtifrX0Awr_gMiGu6F5yvovdsMd1qRUYrNnBisIg2W5jXDsmrjEd-F-yS0XLysP1OBjuc9TlNdGy6ZWpn3YR-PO7KYJLfXlcOZazTqlCEB4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
🏆
به‌مناسبت فینال امشب و حساس، مروری بر فهرست پرافتخارترین سرمربیان تاریخ لیگ‌قهرمانان
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 33.6K · <a href="https://t.me/persiana_Soccer/22457" target="_blank">📅 10:27 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22456">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Kscb9K0jBGp2iIaWpIoK0DVSGTRRo-bxwv3e9bExICKs5DDSPoUhD1pgKOM3BaKAnCD9vc6dMm3axRKa6UdOlikWxTnPhFEvQlI8lwLr-hYrFveEwnFPwQj3_sI8pJSTkiiQ6odKteVxz5tIP5m0vofx-VO91Z0f4kcyjcYzIKDQNxgvq_6RD-vHlFjqefmbjjXQVoRAj0IYJ6Xtbdv3UBrwFHLG3cQjOWJIafyq8LDqCiOVYIHJEuMXw9fEAvyloCGzJCzxz-cf-vndvmOyG5isJKcG0qb-O3hY_nwzj6gRsj0YUthVsOu-HhCDQ2nzcEhJY99IikKyXd14zwZrjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
لوئیز انریکه‌سرمربی‌تیم PSG: میکل آرتتا گفته قطعا آرسنال قهرمان چمپیونزلیگ میشه؟ اینا همش حرفای هیجانیه امشب‌میبینیم کی قهرمان میشه.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 32.4K · <a href="https://t.me/persiana_Soccer/22456" target="_blank">📅 10:27 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22455">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eAe1uls1JB_Oh-rx8PZCQnBfevPYW0uYDGEdGiy_n-cO6G8QxxCJ4usf27FEv2STFwyBaG7P36Loib12cyTNZO_TL-EcEnwOSYGvlMkxsI2uRAsTRAoRGv2XKJTw9om-D4783waVVMOmfwjCDNVX8oYdJXH18Kcw4ljZbajfIOP-lkYDbML2ZbMzj-YSjtbNHkIWEI6EOJrTuqpfHipk2qaSNG-HoDMrITDIdAnppKvSkdCQ5Vh84POGrDjp2Mc781Tuene2N923Higr46uCDuPhPB-3MwKrbmcN9eSmDpP_KDK3JbTj1u3T1TlDpzXwBOm5bUqHH1NjOY1P0DANOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👇
فینال لیگ قهرمانان رو
#رایگان
پیش بینی کن!
🎯
با ثبت نام در این لحظه
#وینرو
بهت
🅰️
🅰️
🅰️
هزار تومان جایزه بی قیدوشرط میده
⚠️
🤔
میتونی رایگان شرط ببندی
👍
تنها کاری که باید بکنی اینه : عضو سایت بشی و
🤩
🤩
🤩
هزار تومان جایزه بگیری بدون واریز
💖
تنها سایت مورد اعتماد ما:
🌐
Winro.io
🌐
Winro.io
کانال بونوس های رایگان
r9
📱
@winro_io</div>
<div class="tg-footer">👁️ 31.3K · <a href="https://t.me/persiana_Soccer/22455" target="_blank">📅 10:27 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22454">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d629612bbf.mp4?token=Lzng3BLONb02lHUjWFU1VASdiZ--vyEu1lG9W8rkeB68xDKsOus6MZhHv3xYTBBCftxG3jj5VgXmfLI0Ke0FpWRGhs9c5rhSA8Zn_4qI0P-YDRnOg58dtB0Gv_8LIRfTW2h6nEWxNgLbpF2snMpk4P0cVkKaDsGRAaLKaT1MWIsdUj-kNPzUp3vRH-QYoVSoyuwlk9S3XeLoEqs4U4zI1tiB53vTHqkHZEHVA9D_BgsV874G5fVofdIRgbrf6YStAf5D8FZTTGy2hWkEgBfrF1quB2qVYaYzL3XkJmBgraGNZ_1Ypfs9T2asGIPsEwhKQslAeq-9S4-Cp9f6l8sPXQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d629612bbf.mp4?token=Lzng3BLONb02lHUjWFU1VASdiZ--vyEu1lG9W8rkeB68xDKsOus6MZhHv3xYTBBCftxG3jj5VgXmfLI0Ke0FpWRGhs9c5rhSA8Zn_4qI0P-YDRnOg58dtB0Gv_8LIRfTW2h6nEWxNgLbpF2snMpk4P0cVkKaDsGRAaLKaT1MWIsdUj-kNPzUp3vRH-QYoVSoyuwlk9S3XeLoEqs4U4zI1tiB53vTHqkHZEHVA9D_BgsV874G5fVofdIRgbrf6YStAf5D8FZTTGy2hWkEgBfrF1quB2qVYaYzL3XkJmBgraGNZ_1Ypfs9T2asGIPsEwhKQslAeq-9S4-Cp9f6l8sPXQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
پدری به‌همراه فران تورس و دوست‌دخترش رفتن شهربازی، اونوقت پدری نشسته کنار فران؛ فقط قیافه پدری که متوجه‌شد شب‌قراره تو پارک بخوابه
😂
😂
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 33.1K · <a href="https://t.me/persiana_Soccer/22454" target="_blank">📅 09:45 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22453">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c867b80a08.mp4?token=P_LaXxBtffH6dFIrXNTCXs3KaqM03QWBRQmuQxEAoghfyrV1D8FAJfohhwZzoIXBxULwPHqz0M_-zK4yLBQqBCKWibVPzrYn7IEHcYr4OCM25XK5mLHgynUmYrUHwKGho8JZxUMJ30XHEFV8Ac4AdzKMkA3EdYHuGUzOoMPKbsIH8s_OBdCyASNesuhUeSeh1IAAc7B-l3QENoe1vcDv_SMWp0bh67glEKg1elaise2BRTrY6HsBaCoYMGzi2LueetxMFVZf4f8y9TgYy2yb8eexTcFzInT3G7AtHniUuiXT83Jaiml82gAs0uQ0F1t4yFMuYjYolmDE5iPJq3Kban285GIHW5BwLovdKa0tzFRv3EoboexYw7QtqxF3cLlGt_kV7UX5PsG9RMGsdYaarOpgmKhE7-Ki9bZmhbSutn7s3C0Wltp8lijYsavG-ZXffXWkLJuIf6INS_jrKMQfWVozmSw2-F38m8INcO2yu7MMROOBJ7aBRobLSFvEYgRzMF1Bpzq9P23TSPZ2Q615W9x6lt6wRxdDP_dh9mYr-TYh5XfNMZZzojuchoCVHk2S3xHACvTLaF8OKjqi1PwTOSAuk_SRz7_vl0KbHjeklYPy5SWgg8xz2L9SULTLN6NhkTuExGJCSlHwt7QVjLMtILfagHXvxXRfLS4qGyWifjE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c867b80a08.mp4?token=P_LaXxBtffH6dFIrXNTCXs3KaqM03QWBRQmuQxEAoghfyrV1D8FAJfohhwZzoIXBxULwPHqz0M_-zK4yLBQqBCKWibVPzrYn7IEHcYr4OCM25XK5mLHgynUmYrUHwKGho8JZxUMJ30XHEFV8Ac4AdzKMkA3EdYHuGUzOoMPKbsIH8s_OBdCyASNesuhUeSeh1IAAc7B-l3QENoe1vcDv_SMWp0bh67glEKg1elaise2BRTrY6HsBaCoYMGzi2LueetxMFVZf4f8y9TgYy2yb8eexTcFzInT3G7AtHniUuiXT83Jaiml82gAs0uQ0F1t4yFMuYjYolmDE5iPJq3Kban285GIHW5BwLovdKa0tzFRv3EoboexYw7QtqxF3cLlGt_kV7UX5PsG9RMGsdYaarOpgmKhE7-Ki9bZmhbSutn7s3C0Wltp8lijYsavG-ZXffXWkLJuIf6INS_jrKMQfWVozmSw2-F38m8INcO2yu7MMROOBJ7aBRobLSFvEYgRzMF1Bpzq9P23TSPZ2Q615W9x6lt6wRxdDP_dh9mYr-TYh5XfNMZZzojuchoCVHk2S3xHACvTLaF8OKjqi1PwTOSAuk_SRz7_vl0KbHjeklYPy5SWgg8xz2L9SULTLN6NhkTuExGJCSlHwt7QVjLMtILfagHXvxXRfLS4qGyWifjE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
موشک‌های‌گرانیت‌ژاکا بازیکن ۳۳ ساله سوئیسی سابق باشگاه‌های بایر لورکوزن و توپچی‌های لندن.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 33.8K · <a href="https://t.me/persiana_Soccer/22453" target="_blank">📅 09:30 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22452">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/928b5d2877.mp4?token=SxA313SOOw-5zZFdPwZD90w71FMa_cee57uZtgEY4gOkNY5zDSGFyZhASMpqYiKiLaZVId7-oIyxFvrv7WSbtQ1h3iZcNR8QBoKkvRSybf-4-uIqCqaq9gGhHEBb8ybAZEmVWlxCx6B0hxqB-at2akV9CqmFZPDjc4s0bb7P_ntJT9RQ0AEtoBNroyrCgYAxtBvANouUMZfh_P4KhemNtU7SAlE9BMSUvLXuluoFG5c3dUzHWKK7gKN6dMhC5-xLRAIXuc6o2d_9aNadkkDRUMhwoM1cN3wYD3b3fYOkH4JomIoYq9Do9v_3gJNFnTvHvMUPSyfzC_0cm1FT5o62gw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/928b5d2877.mp4?token=SxA313SOOw-5zZFdPwZD90w71FMa_cee57uZtgEY4gOkNY5zDSGFyZhASMpqYiKiLaZVId7-oIyxFvrv7WSbtQ1h3iZcNR8QBoKkvRSybf-4-uIqCqaq9gGhHEBb8ybAZEmVWlxCx6B0hxqB-at2akV9CqmFZPDjc4s0bb7P_ntJT9RQ0AEtoBNroyrCgYAxtBvANouUMZfh_P4KhemNtU7SAlE9BMSUvLXuluoFG5c3dUzHWKK7gKN6dMhC5-xLRAIXuc6o2d_9aNadkkDRUMhwoM1cN3wYD3b3fYOkH4JomIoYq9Do9v_3gJNFnTvHvMUPSyfzC_0cm1FT5o62gw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
لوئیز انریکه‌سرمربی‌تیم PSG
: میکل آرتتا گفته قطعا آرسنال قهرمان چمپیونزلیگ میشه؟ اینا همش حرفای هیجانیه امشب‌میبینیم کی قهرمان میشه.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 34.9K · <a href="https://t.me/persiana_Soccer/22452" target="_blank">📅 09:15 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22451">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eb17964484.mp4?token=GKHkE6u1dnSyOm1rwxaG6Rvb-inqJ0K1v-YdCOMr50JMKJlnDwwUvGQ0lyACPHzH428_lJMUvWacybrzEfBWh2zIE1wHZqeLZlhKraBViagqTeWgCTNHv0VZTuM9GLjaHaNrAAOiMpsijEzSjA6YepXZ3z7HJwIQIBLFW8BSmkpYZr6iyc19T2KtTTNxCn8dTM6XbSXfIjS5eY466-mn3KpHqeLYWI1Gvuhi3c8Rl5_O6IHbZABiLd7RtfdRZdHrnj2GqKLsI45VMvV15yMte49mXX6lqdTF1TEFpRYRUdh9qCIVqwXQ7SthO1_W2PILr3c5mdSJHmDo62RtMYCa_A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eb17964484.mp4?token=GKHkE6u1dnSyOm1rwxaG6Rvb-inqJ0K1v-YdCOMr50JMKJlnDwwUvGQ0lyACPHzH428_lJMUvWacybrzEfBWh2zIE1wHZqeLZlhKraBViagqTeWgCTNHv0VZTuM9GLjaHaNrAAOiMpsijEzSjA6YepXZ3z7HJwIQIBLFW8BSmkpYZr6iyc19T2KtTTNxCn8dTM6XbSXfIjS5eY466-mn3KpHqeLYWI1Gvuhi3c8Rl5_O6IHbZABiLd7RtfdRZdHrnj2GqKLsI45VMvV15yMte49mXX6lqdTF1TEFpRYRUdh9qCIVqwXQ7SthO1_W2PILr3c5mdSJHmDo62RtMYCa_A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
وضعیت خوان لاپورتا مدیرعامل باشگاه بارسلونا در روزهای اخیر بعد از پیدا کردن نفت زیر نیوکمپ
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 34.5K · <a href="https://t.me/persiana_Soccer/22451" target="_blank">📅 09:04 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22450">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IUHjtRmdDxaeRLsdSuUvAJkr7LdVufeqdMTRVGcX-I98VgUyOZBm_BKuQvFzwxW4yhaoVswew7aYKY-8qQtWY-b2HO66PtlZ9rTwP_12kjsJlbOWnd3I0fZCxQtatM6WRn-KnuXoGWTYmShXO6lcqe7NxZGz9f_x4C2Nqk7J1OJlo4BicB157KmyYezd4t1VvnsTxjZAIliFYCFhqK3T1HmcEfg9O7TZ2cp6tFF-wxWnNH59nYld7GDHlweAh7V2uTaIWzrpRqd8Y8qeiwOOFE3awzLumEzeCyxaewrMtwdPcKqAo7HLKewnpB9Ahtfjc1ld2JxMJVfq76CN5dgoWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
طبق‌شنیده‌های‌پرشیانا؛موسی‌جنپو وینگرمالیایی استقلال درتلاش‌است که توافقی قراردادش رو با این باشگاه فسخ کنه و از جمع آبی پوشان جدا شه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38K · <a href="https://t.me/persiana_Soccer/22450" target="_blank">📅 01:45 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22448">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VQvjSIZWIqaAHUgfJVWwrknRKi6kfeNn2unw7oKaCsLOEIVmvBg35BtzWkLUd7KAI08C5GixE__JX5J0y2TKmNVSNDkaF0CcR4fuKBpHdF-XgBqYwYEIrGspOewYuFRGCEKZ_V5GpSMK0eLP_eosYh-EukyoEN0SvhOAk-t1s93L-6FqMUOeTY-EezxAjckJBAfeeaaEl9PUe2kmzilNBC9kzAvL-DzHjRjgB7dNgTzW5EEKj1KH4w23NWqZbfSGiQWWp6f381kgrBY6oPqrF8OujdOZDrbgm10Ot7RLyHCdu5VvdcjyP19JvnQuDWGOr_-STsmp-KV5gtzDk0LAZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه تنها بازی مهم امروز؛
پایان فصل باشگاهی 2025/26 با فینال حساس لیگ قهرمانان اروپا
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38K · <a href="https://t.me/persiana_Soccer/22448" target="_blank">📅 01:27 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22447">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fT8i0LvM6oxTUK69v0hxt7y4Ve_PUyKwxEh6iEE8Ny6_dIraEsKmZTdx_cb91oahPMsi9HYFEtntY-MB7cDWm4dBwkXmrQZFusTzhwGH39Y8-JQ-VRCi2EHQQ_BUMnc7NR060c8TQ2cX9v8fvo4pn8wvWX_C9Ho3Y45rajBbfEX_7h9IuUDmD-V2ChNmWAhc6MqN7Wgdk05DF_qgJqEp1fAu6l8A8ooQD3ESBOicZg6VDQxdMBwWt1u6S2N14g6JhCzGRXpDZSXwWBbhaZA8jHc_-gB9V22ZyzSCU2ybd-AJ9FAyCwEROVndIitwtpY-5bkA3tnOSt41dzSJ7Ug_gA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج کامل دیدارهای دیروز؛
برد تیم‌های آسیایی در فاصله کمتر از دو هفته مانده به جام جهانی
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.1K · <a href="https://t.me/persiana_Soccer/22447" target="_blank">📅 01:26 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22446">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s5OP4tVdYlC8tDrTZwFWAcKNk_sIVaGLxaatVn3pYJJScLIC7GLOJHX7hffOnB-jz9WItCzDboK7avhxxIEPh0YREGu3P5IRF5GdOsXD4u9-I0g_bBJDk03b-h48SRfnakpKI27BspdQID-DR-6b1d7pLcMZDjFB82kBwTcfWZamnImnQe6IsO8Xv4pzUiSXgLEpHWnTPtDDjfwQ_DgofOCs3jMfR08fQuPVlS_OkTFEt-pUdn_ooOtMGZXtooh11UdLCvOEa2noy0Xk6mqESVZhTCb5aYitlvVP3MMhjU5syojOIgQpbd9Vvkd_MQVZMjwjeoNrKIpn-DFim6cvmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
فواید پیاده روی رو ببینید؛
گشاد بازی رو کنار بزارید؛ فقط یه‌ساعت پیاده روی عادی میتونه بیشتر ازاون چیزیکه فکرش رو میکنی بدنت رو تغییر بده.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.3K · <a href="https://t.me/persiana_Soccer/22446" target="_blank">📅 01:06 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22445">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eKnLteNg5L9iuYm67FiZpzyIOsbORAnO_-AC_8U6G-GEjC7BunmralIlXbplYs6uPfSpoMlnX-kHqTGXBOq24srDLqoqgtPSxEopMyI_-3QpFMULe50-Hzuo-TjMquBWVutOqILtIHHxuo8VZul3enaCrA2ZM7gIjtHQaDmSh3BWv25OKMPwOPjuUZNoMvI7snvYxT1uXXu0fiy3-v7pLWn2Xh0XtPsBFZmd3dXfFx8VAKIlMJWdObkdeviS7o8of6iaprI0nzs3GEtO28wrsUYJEGp6_ngeKGu5xJV_CFW9tcul37zeeqLTAGwUkZd3BPD4xniWlk_GqYtWoy1r3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
بازی‌فوق‌العاده‌حساس‌وتماشایی فرداشب آرسنال - پاری‌سن ژرمن رو در آپارات اسپرت ببینید. عادل خان هم بازی رو گزارش میکنه. از صداوسیما هم یکی دو دیقه جلو تره. کلا سعی کنید هیچی از این سازمان مزخرف نبینید. لینکشو فرداشب براتون میزارم.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.3K · <a href="https://t.me/persiana_Soccer/22445" target="_blank">📅 01:05 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22443">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mPKpfBMwM8EHCkmm15eOsOsDamnMjbZs79Rbo38zjdwH0vMsV0fZGyjEm6Tp5twGA4hwTkxYprVz-X2Bbth4qAv-WrkP3vKKKEKC2_aRzV7rriIKT_XGNRlUZKbgd54NtJpu9tXasE7foIVHIHydzZkeUso8LxZEFK8nagA9zvuC_yGt9HkT8tOLq1YxhrmPjv3UfLBXRwt6U_XEC-QWgUkOkZQ0wnyyzcqZ7687xRO_ei4yFNkKInYZi419fduBPSnZiMe4jrW4C36ufHPYMgvofB9b9PS9sjozDzJklTuKAa6JK2-U4lvSy4belpokRldyp-I7PKYvUSEUZJgNgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
رومانو: آنتونیو رودیگر مدافع میانی رئال مادرید قرار داد خود را یک‌فصل دیگر با این تیم تمدید کرد.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.8K · <a href="https://t.me/persiana_Soccer/22443" target="_blank">📅 00:49 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22441">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tv8yXZa-cnUJ5VCQCac8NyzC_ltixjsM5udHAHUaw2onKRE3GqZZP8zjKtFVeqsgJ2xvdqBuY-mKbLBT2xhOOV_IC4fct1zy62gRxqgEfKY3sVzw9aQBP0RsOIzkhFR8VtfHa0pYN8H-jbDxdf1WV3kZ_lNR6k2_DZO7fGovfPl-EK7xr1AfU9knj10Ya905VuUPUCzAoUvyGtyukpUo9xEcnDAHq72SBVUCADSjDwsHMQWjaw7req6sM_V2DH-EZ9jSHHBi9HM0IgEtE75o1dt9XWcKpz4jH_bbMRfz3amyXs15FMeRolSreXYzVrP7RsLOka2ddpch5JYmbGZRjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IeBS9Elq-n9W8ZIF2Vlox79oMKyRbOnxenOY7_HfKMPtYh8EaUnJd4_AO2hWq56tv7QyR0PShMjkX0mNH85SF25ZrDjNNQqg_oobhRxfQ18FLUrc7Bu_aQVWvI_FsHOAA_nQVDyUHB8HAWi8zCgGafoVUEank08gZhPpA__Q_8MvZQkWlr2PbnMv_Fj879P53AhpwEqXNgQdTD8cpE18Y8T74Xjulj59eMI2swSPwMbRw-Z2ngnNClOknBRqDQtb1xEeO4KWx_ADBUhrbDK74SyLeYlW1ryXUsTgeCQ778P2hr5hX-4Aq3TaclNKyVe37aD4i8JotcxrNd341-EjkQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">▶️
هایلایتی‌از عملکرداستثنایی آنتونی گوردون فوق ستاره جدید بارسلونا در فصل گذشته رقابت ها.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.8K · <a href="https://t.me/persiana_Soccer/22441" target="_blank">📅 00:38 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22440">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i_47S22ivjA2MFvy2Fvav3kHc1SscwJSu3ioenuSrTf2RlUyrLu7wyCki1jbwoVd_AI8Xg1VxBBQjIkPYaMxx0HCYC_zMNcYFJV-Yo5LHKKAcTeV6-g7W5_NCPwJg15JX8n3Z_8kCuTsvRcE-J4aKlEqKgUzEj-BtBG9Rtu_cS76Ygscon-FXvBsp08RhkraG0xLS6Q3if9uDNXhfw33A4hFaId_xBNAivaqwmd83n1N4reNoqlwdrRkYzKIohf3BKhMBE32FtR-LTWb2BaPf7nl6Kdzo33bzh9vFDDe_IFDTn2NerARWC5vz-Blw8pyf_Pdr4jOKTNfgCdlP1O-UQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
ریکاردو ساپینتو سرمربی‌سابق‌استقلال‌که در روز های اخیر با عقد قراردادی به پافوس قبرس پیوست با این باشگاه قهرمان‌جام‌حدفی شد. از معروف ترین بازیکنان این تیم میتوان به داوید لوئیز مدافع سابق چلسی و آرسنال با اون موهای خوشکلش یاد کرد.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.4K · <a href="https://t.me/persiana_Soccer/22440" target="_blank">📅 00:33 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22439">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EdD0mYDYuEiwh2Wgamb3fbC_4r1KaNoMaWvy3Eq43gg2RTUfqQs6H6ngTlSVuAw_A3ENmVp5ZEwivfpSNOPQtzmLGvlWNZOMJ7xczp0nQSX-L40w5DbaW-vK4tXZ5Xejw5qbUp7kTQZktbLH3aua2wNj1HwGSLfaXUksGZZggeo3xMFKSsWd2vMs8URqChSETSDLXYZUVAz5chpPbCam4PQtJuRbXgCOyBFZDZzwVX3YB2Tch7j3LbcOieEpMU7pXvYB_S24VaeQPxZFR3uec8B3wOwV-AUUOBUL7HfWg9bWCSqVaADOLWKd7qzwFS0jK8LfJ9zrpRSyxfTdY5Gjng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
کدبیس سه‌شبکه‌جذاب ماهواره‌ یاهست که بعد بالااومدن نیاز به‌واردکردن‌کدبیس دارند. اولش دکمه F1 میزنید بعدپشت‌بندش‌سه تا 3 بعدش یه صفحه میاد که باید کدبیس رو وارد کنی:  کدبیس شبکه جام جهانی HD:  BISS:2585AB552585CD77  کدبیس شبکه ورزش تاجیک HD: BISS:03A01BBE20C16D4E…</div>
<div class="tg-footer">👁️ 39.6K · <a href="https://t.me/persiana_Soccer/22439" target="_blank">📅 21:24 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22438">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BGfGrm7CBdgcN9pEm-NqQSIMHNqkjbSvMW4i8FTkcohKYl_kq38CinA0BLgrtwzHwLkwrX2vEE0B4F9RUp232JPVjEEpj-gy_McjAU24OBimnJSZYkk7QL7aAl8AF7HBhvNJZvfwptih08c4j85sSbjjHrMQvz6MM9vSrIsnp92rSl9-ucA0PW7uCZEnhmMcRYe2HXYiMjeNxJ6G6_d6x-1QHFfJoNPcVA6XUe7aI7c-BwAFZtXCuO_apaCfXSmtIqzTqAXO9Qt6B2rKnXlLVVGUZYtHJOb9Miw1Z8mILz2vqxMuQpla8RDOPDmP3whjtPNabhpJn_5FjMNYorGo6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
طبق‌شنیده‌های‌رسانه‌پرشیانا از نزدیکان مارکو باکیچ؛ ستاره‌مونته‌نگرویی پرسپولیس از دو باشگاه اماراتی و قطری برای فصل آتی آفر دریافت کرده و درصورتیکه سرخ‌ها تمایلی برای تمدید قرارداد این بازیکن‌نداشته‌باشند او از این تیم جدا خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.2K · <a href="https://t.me/persiana_Soccer/22438" target="_blank">📅 21:19 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22437">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">✅
تیم‌امیرقلعه‌نویی مقابل تیم دوم و ناقص گامبیا که در رتبه 116 ام جهان قرار داره سه - یک بازی رو برد.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38K · <a href="https://t.me/persiana_Soccer/22437" target="_blank">📅 20:59 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22436">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J55LoRwrcTTiBkYyxt_TzaYrDyJTkDQ2bLxCMyj1R9aBmJU9bSMma-s2HIYlul7v3n3dQEn1WVTjp0AiZ-RKT884RUeb_7WQHKRiLpzJZTi8wdDMgV3VOAPmp0CvXB28ff8_WWaHewHWGVfagqeok-chXqJEtDdBl9wzIigl9j_pnzQ4BcNrJzspWM0n7TW5FDO1bz9E1Sr4ggQ7sxxVIPU6EehMAFTV3mA91jAv7I9GxV82n3IkNsEJ8tf_l0JYzJfGsbZttLwB5BEF1SAVY4rpS9TdpGKdiW827-5naL1k7yvC06Lz5UzqRojUXjU8R82H4a08Y2gq28-kK4d3Dw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#نقل‌وانتقالات|سران باشگاه منچستریونایتد به درخواست مایکل کریک سرمربی جوان خود با ارائه پیشنهادی 100 میلیون یورویی بدنبال جذب فرمین لوپز ستاره اسپانیایی باشگاه بارسلوناست.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.6K · <a href="https://t.me/persiana_Soccer/22436" target="_blank">📅 20:55 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22435">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">🏆
کار گرافیکی تماشایی از قهرمانان جام‌ جهانی
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37K · <a href="https://t.me/persiana_Soccer/22435" target="_blank">📅 20:55 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22432">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tGK_QpX6hNuweGzP0QZYQRRhsv77RTLRHVLOxrtw6h7YWGSt-09g4XFd4ZnWyF8rVVzxZOY6lWcGHfKVAHfnJLhM6wJoV8QfhUndX0T3NC0nmbMOCIOh2KOJTarXp8CGuhu9YCVyvpD9xZrxnr1ldiK9qyC5X2va6CENizmB6Evs72OyqlHyKHmyJQbPkvU8OcT2VfN297dOHDITtTe5OgIjmEvwsyWLlMsPv0OSLHOYEClUq73qratr6VS_ZOQ8iReq6qr6nyeu-s8Ti6wBixikHp7cQzXmNn_5gFIokTJZgTtUCN_fBLu70wUNAA9sr41pdQ2-bKjtRtrfID7KgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇪🇸
🇪🇸
بیانیه عجیب اتلتیکو علیه بارسا: «هیر وی گو! ما یک فکس به همراه پیشنهاد خود به بارسلونا ارسال کرده‌ایم: ۴ بلیط برای کنسرت فردای گروه «بد بانی»، اشتراک سالانه ABC و یک کیسه تخمه آفتابگردان. مشتاقانه منتظر پاسخ هستیم تا «اعلامیه رسمی» را آماده کنیم.
⚪️
…</div>
<div class="tg-footer">👁️ 37.4K · <a href="https://t.me/persiana_Soccer/22432" target="_blank">📅 19:36 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22431">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u2IbXez1KpwwGuTCW7YQKgKPSnjoYWSnS3EIC0mmMCEgymsYocsLq8dzya2rRYWj7oF-inhiKby19Y404bazvsQ7E8A6ah0jTv1HQQhJe91SDj2FKzt9D-pU0nPkZuq4rc2tte4QCwcdF0aE3haGelQ3H7k7iLHhLBym3ubMlulHx0QXXEfABmfgdCnTzmWNy53NcRKRU5dycrW_E47pzc9PyyWicEStLBFDrhYPYwS-J-QHJvyZ-nmqNiN6_coS6zMcMp_q0JxRrkq7edBSBv4QBAbseq_aAoWrWUzjRwwNuYhQwgmEVFdufqrJ_xRXkbhexIeM66KHf0utK92j0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇪🇸
🇪🇸
بیانیه عجیب اتلتیکو علیه بارسا:
«هیر وی گو! ما یک فکس به همراه پیشنهاد خود به بارسلونا ارسال کرده‌ایم: ۴ بلیط برای کنسرت فردای گروه «بد بانی»، اشتراک سالانه ABC و یک کیسه تخمه آفتابگردان. مشتاقانه منتظر پاسخ هستیم تا «اعلامیه رسمی» را آماده کنیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.9K · <a href="https://t.me/persiana_Soccer/22431" target="_blank">📅 19:26 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22430">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e4a_zH-COacoiqe0ZFwuwix4OD_O-q3_64DaLox-Ozxo8JM2ZTKV1N8iJ-DXNpPSBa4KdS-qwTW7tTR4C_UlDyZqPqDE9I65aczUqJQVTkogL3MRYB2rDdHIiIRjL2YvE3BeKu9P5BB9es4YmJzwMAbwCIyfTtz2r5Gv0_AeUaIbykKpkQJE8dEd9rKSZ5lHh0fwTZ7xix_8AUqu4H5RbjZ4HJQDL8kXey3gWnKx2Xv6dS8D38FJe1_flHqGnADC1cl4fsVxR2oF1sAYZH2JbijXND2EY9sBwpZGdsez8fLXCtjDnnAO-BSn79Itli2V-s9CF-LMgEdtFND1WjAs1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
طبق‌اخرین‌اخبار منتشر شده؛ باشگاه بارسا طی ساعات آینده پیشنهاد برگ ریزون 135 میلیون یورو برای جذب خولیان آلوارز به اتلتیکو ارائه خواهد کرد و این بار این باشگاه با این آفر موافقت خواهد کرد و این انتقال رسما انجام خواهد شد.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.1K · <a href="https://t.me/persiana_Soccer/22430" target="_blank">📅 19:12 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22429">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G-5Ah_OyNXGh4pyc09EwzJMCrqgv2gJ6grjB9xhB5kkmiD13YemgYDlBsm-GiBGmIW2ib-2e8eVhvsKGh4guk2d8i-4gQSJfIxX7I2ZErmiDx8oBLiNTkHwnxiYfY__lIenq8DL0j3MrPIBf1oTJRAjB2tnlfRaTVNESrimQjrsRrlqSxLisOE8FeJcWMCqjQOhNts_OaM7AxCe0dU-MYEBeXMlSFUMtqHCvzdLAtoFuKNo4MxkShIOOh1R0O0CaGuEYtlf645qIc3kN8qtC3BDm78eDt5hOcLzvkwvCLYBdQjOXeFCNP3WU0DnN01Etu-8l-ETa-eeiCffkj2y-Iw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
با اعلام ایجنت رامین رضاییان؛ ستاره ملی پوش استقلال که نیم‌فصل دوم به فولاد پیوسته بود برای فصل اینده به جمع آبی‌ها باز خواهد گشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38K · <a href="https://t.me/persiana_Soccer/22429" target="_blank">📅 17:25 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22428">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3e99804290.mp4?token=qAWaFx1-8LKmkelJHbVJKnybWsXGuXTwnP1Kpa-E8f45QsvzAiNsDbyVkSB8EMraxOyZIsZKLtCyAfzcVx5PaaMo4UEpCvlnlJN5NBnfQewrUO6teT4ax6hk0D7WcFLezjGKhUh5GMuEga8QgUtWnpARurWwNfdc8XA3pKEIXJ7cUVhALkyLJrq8E108V3yxAUOMzo4qrxFHfaoIY0e9HL8HtalMkhOgDb8L-9JGaVe25jzLMB_FPJjCXTiB5-eYIzMsYXcA1PBoiAtXLXDxIQR3GvinF6mHIKDwFsZXV_qKCHuYYc18Z7oe4S1Na8Dwa2ccsSOVJihK1Coj12EjIw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3e99804290.mp4?token=qAWaFx1-8LKmkelJHbVJKnybWsXGuXTwnP1Kpa-E8f45QsvzAiNsDbyVkSB8EMraxOyZIsZKLtCyAfzcVx5PaaMo4UEpCvlnlJN5NBnfQewrUO6teT4ax6hk0D7WcFLezjGKhUh5GMuEga8QgUtWnpARurWwNfdc8XA3pKEIXJ7cUVhALkyLJrq8E108V3yxAUOMzo4qrxFHfaoIY0e9HL8HtalMkhOgDb8L-9JGaVe25jzLMB_FPJjCXTiB5-eYIzMsYXcA1PBoiAtXLXDxIQR3GvinF6mHIKDwFsZXV_qKCHuYYc18Z7oe4S1Na8Dwa2ccsSOVJihK1Coj12EjIw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
گل‌تماشایی هریسون رید بازیکن‌فولام به لیورپول به‌ عنوان بهترین گل فصل لیگ جزیره انتخاب شد.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.5K · <a href="https://t.me/persiana_Soccer/22428" target="_blank">📅 16:46 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22427">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HEZo9PHlWohEYpSK7Wnprllzl4p9ZmeYXQsQ39Zk03wGkTOan8GmrPiQPYONfcrwpB4aNYDZ3c7VsCH2UggZ0y1R96uRlg-ireRiBqrUVM6PbqfDlmA0DNf-EEVIxu2orqtP22AmCzq5ISzSLDfinvpUPC9T4Rdk9j2eKZ3PybPUJGT78-fQrnSWSJz6HT7WLmmu1HqLOlsamslcTZgIuqCy1wn4odcJ599YoFzAtXDdeOUqVFa9aZE7LRr1WPjm56S7Gu4fAfsRJXKpfZMrtxxZgyM3x9ia-R0Ysf69IiXJrieW6wSAx8-O15je90k1zylEq4ZzUkB439XokBOewQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛ خولیان آلوارز به‌مدیران اتلتیکو اعلام کرده با بارسا به توافق رسیده و دیگر انگیزه‌ای برای ماندن در این تیم نداره. اتلتیکو حدود 150 میلیون یورو برای فروش این بازیکن از بارسا میخواهد.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.6K · <a href="https://t.me/persiana_Soccer/22427" target="_blank">📅 16:19 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22426">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SxO9g1lQnI_ZhnhZvDAHTY84wm_hhd4A2M5Ky5zYGsDS96ESo4kdM5uz2006svz2g-fAjOSR-cjPbx5qeMbD61l9gmC8ToI6RyXWR1Lc7n5VCBFkpTKbPmcAOa3uJdnTZ75yJxHhUTb7_7oe5VZTGCm53n_ZpSh0zZGeQbT52lwW5WxnjvRrzcTacppNUZjkHbUo4--e4YE4HQJ9xZm6W1vwvJxhFLQDZoPldLJx02YAYXHTfreQOri7digZSznw_piCaFCoN1hhOM3tW1TCrk2TAgDvNaCTvDdBuBYJB9SonO_AXMqJRw3pyKCkdbgTP1cXqYphf0ahv_Cw1x7T0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
رسانه پرتغالی آبولا هم مدعی شده که باشگاه بارسا در حال نهایی کردن عقد قرارداد دو ساله با برنارد سیلوا با دستمزد سالانه 8 میلیون یوروعه.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.9K · <a href="https://t.me/persiana_Soccer/22426" target="_blank">📅 16:05 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22425">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2ccdf1c58d.mp4?token=BhaVitFsruZ1jHh30QDsTUQTYzXoHvF31BNHd0rcKxbQFOeE-8nVFRVAacQs9Ams-T_K6Y5IcDMjN7GTsDxgogkoYkBypU_8R1l1AUCFqXl3PP1iooU3BZ0CGTv5Ob9mWO3vCmvlbd1fWgDW20XUhMmcbw6jt8br91lRXFSyls2Rkremznf9hexFvXLOwzKblwtR44GXeU4Zqw2RZ8qIFMnr8lL9AVv5BKUuIn1siQAVtberL9XgJ1vmBTrq0YKFWU79NFO2Zv1pGn_h4dzd2QKg5m7UIDBM9BVx5Us6O4kFDyCJeENxyq0cmW0FlPcBcTwFvqsHYBxt1XunXApak4i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2ccdf1c58d.mp4?token=BhaVitFsruZ1jHh30QDsTUQTYzXoHvF31BNHd0rcKxbQFOeE-8nVFRVAacQs9Ams-T_K6Y5IcDMjN7GTsDxgogkoYkBypU_8R1l1AUCFqXl3PP1iooU3BZ0CGTv5Ob9mWO3vCmvlbd1fWgDW20XUhMmcbw6jt8br91lRXFSyls2Rkremznf9hexFvXLOwzKblwtR44GXeU4Zqw2RZ8qIFMnr8lL9AVv5BKUuIn1siQAVtberL9XgJ1vmBTrq0YKFWU79NFO2Zv1pGn_h4dzd2QKg5m7UIDBM9BVx5Us6O4kFDyCJeENxyq0cmW0FlPcBcTwFvqsHYBxt1XunXApak4i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
ویدیویی‌که‌باشگاه ماخاچ قلعه روسیه از عملکرد درخشان محمد جواد حسین نژاد ستاره ایرانی خود منتشر کرد. حسین نژاد تنها یک فصل از قراردادش با این باشگاه روسی باقی مانده. درصورت باز شدن پنجره آبی‌ها مدیران این باشگاه تهرانی برای جذب قطعی این‌فوق ستاره 23 ساله اقدام خواهندکرد.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.2K · <a href="https://t.me/persiana_Soccer/22425" target="_blank">📅 15:54 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22424">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MnkBaGBrz-_L3zW6mNc9bKmbkbvyiAYPyQ826aPOEaZHHvkJiTaqrOn48iK0sWTmYNsIVcU95JwPcTdnQXIWmTcG8_hMI9WEZx61ryA794YAReImWvFyqy-RHHvtX_CaYTPyVViC-GDGb6tAyJKA4elzgzdXOGFMOlaBGocoCnU-5to606hONefrUCTSJW1aIf1_HDqUeAB3rJbBeYTAdxQUNnbe8y6NcZK7inDfbY8ZYnLKriZatxbpV_veMGN_VGc1ymfc6fGAwM7voKwZFLF4SF1f9-v0i6Okcoe87jjaDbp87Pj_Jnj_qA8e5PCTviu6d6xxNv2leMTkPoF4lA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#نقل‌وانتقالات؛ رسانه مارکا: رودری ستاره اسپانیایی منچسترسیتی میخواد از جمع سیتیزن ها جدا شه و باقراردادی 4 ساله راهی رئال مادرید شه.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.2K · <a href="https://t.me/persiana_Soccer/22424" target="_blank">📅 14:57 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22423">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q8HgQXXMi0u_CNxuI29JMvjOfA8TLuueiGh3g9NV9iJOSZWpXFbs1MOwWnnPUKUjmVcycffKYhmPrl3eXTNWQ1SzOnof8RR0cYu3U8mICei4Cz2-RpENrq92y_ocX3ipZ1lrxrfTHrKmry8CP6Z1866j8bn-c8RB9ORqZ2MIkHb-eqP431IfJ0G2buO_TrGsgJt_1cuXM9k2RVL6eF7qIPwkKeANverVSg_tJPQbrtojqLMkkenGa7Oc-qutZftGzTIgEXKgrl_OQCPL_L0YFg7QDv6KLjQc7qHyBgzIbW7ZbFM2pAJx_uzaQZ9LRddVfGQKEMDz3kw7vgHui_oC_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
جرارد رومرو: یوشکو گواردیول مدافع سیتی نیز همچون خولیان آلوارز در خواست جدایی از منچستر سیتی کرده. فلیک عملا با تماس هاش داره راه انتقال ستاره‌های مدنظر خود به نیوکمپ رو هموار میکنه.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.6K · <a href="https://t.me/persiana_Soccer/22423" target="_blank">📅 14:07 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22422">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JLyhalilvGMkHkTXG5-TzzG9ZsR6R6mwlEtzawEWu49aAVaAyKtuVuy0SzIyDCC-r7uVqxZgJjQCurqKDAZd2q8yNhCRWGluWtHmLLu-OwrmBxF1TQKDxCkAApqWawtJeQ2YcbSDRodxX1728R9O4SUYRVaUBLQbhDxfbmZZVcETTw2gd8-THcSq6NV67fN_B1P0iTI0wt9x-R6AvAhYxA7zCACrqx3PMfUo_b_8pGBftiPd9M-ew1JMJBWDYHM_wgAHKT0d4Nf4XicTW1kAD3Z7DfAEiHWAvHQV1DDn5be97Y_15dvmqbsJNbX-HKvXJS_jayXQobiF17cu72GMEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#نقل‌انتقالات|ادعای‌رسانه‌های‌انگلیسی: یوشکو گواردیول مدافع 24 ساله منچستر سیتی هدف بعدی سران بارسا بعدِ نهایی کردن قرارداد خولیات آلوارزه.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.1K · <a href="https://t.me/persiana_Soccer/22422" target="_blank">📅 13:55 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22421">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qdFZfxMS0nUAlWZvmsdur0pUCLggISFeTiqubglkAxxBTX0HufSIAzsVRiMSIrCNaED-pxKmYNji7SjYOe1xwoWCL9zuaOXOASsPfbMBUkANoN69A7nxkPMHf_finN6qbk8XvZQ_1S5JbBhZJA94dD3kbxpCVkwq-uJnj8OZTJgUAGlNMG4oFPb2FIylXUweDXohkVZT-eXkv_cN7X3JGN-DIKEuV2IYpcFlhCOpfTywocR0SKo5q7eCvZX6XbpVhq1dlYMI1Y9eK9ub7J_laa_kunsjFMthVZQnfX8S_7kTJRR391IAvWG3_jGeBRxDShlgWg-FwMAgZqkMYdZahQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#نقل‌وانتقالات؛ رسانه مارکا: رودری ستاره اسپانیایی منچسترسیتی میخواد از جمع سیتیزن ها جدا شه و باقراردادی 4 ساله راهی رئال مادرید شه.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.9K · <a href="https://t.me/persiana_Soccer/22421" target="_blank">📅 13:06 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22420">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Rcv4fJZ9OTXxcvYRiXAaeItq-noTAjHFQCq5ENaND39_7Wu4yqU74XoXmMWbAQ5GxFJhKX7ZiJFrAColZ9JJ_TajTA8bEOsnmCcL0OoCoYVKAUAdnEZrk0LSMcBAuYruRLj6mljFPaFmCLHkkptgEj2vxZg5TE74MLRGzFBuavgii9Km7SEY3jPupJBvdPiQkKk4av2fTdFpY2WG-RLuYxl4ONR4gUZIHkoT859NROSzOnXkUApMLm1vHcRoEC7A_lHMYOLSL8KE49qYuAw_DLkNIqdwJL3h3qeV58gxOcgCoBUCejlCgxt8YtVstLTsoVzlTgqnIz-EBv2-bNW3Gg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تایید شد... یاسر آسانی ستاره آلبانیایی استقلال امروز در تماس با علی تاجرنیا اعلام کرده که فصل آینده رقابت ها نیز در تیم استقلال خواهد بود.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 37K · <a href="https://t.me/persiana_Soccer/22420" target="_blank">📅 12:37 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22419">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FHwYoQZAd3Tx7xuNAYsxncaKWCueMyNuhPp-weRmbAxu1TvqeldxAx2LEh-g0E6xPaENB_gxT3KEPw0H3cCIMOpwoj1XopTiknnqUWiSMElNwlxvo_E_IzNyWFOgbmMWtjznwGDrNUjWS7z5JBmDgVBHxjbtSQv6saECi5QgSmnAPxK5NSbC93pnFgqDzM8TOwXGudJo2uLN8kXIUuPtkeyhPQj18Co7yn5Xi5O1viZ2pyod80jRrABMTUheewjNu2hBeyB_qpDmrqUgNRXq6EHHriOdmTtpoVYis_Cd1Eu9iRUtZcBufSIySTxPYH6Sbz56ID5AEFoiEgKSVF7n4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛ خولیان آلوارز به‌مدیران اتلتیکو اعلام کرده با بارسا به توافق رسیده و دیگر انگیزه‌ای برای ماندن در این تیم نداره. اتلتیکو حدود 150 میلیون یورو برای فروش این بازیکن از بارسا میخواهد.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 37K · <a href="https://t.me/persiana_Soccer/22419" target="_blank">📅 12:26 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22418">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f2J2qPsW0b0JG6FftehB7J5WlDIbyazaod0NhD3DvnFcuQbU4cqFE8v45RUZsJRdFm9S8J_OhgC63hK2WoAFYn6jRyf6ywKwcQxyyYVp4xWam8-HI6aVOP2q7AXwx-GwpPPWNz2vuWHF2JHXcmGvJZU6mCqJe3uzi_uueV8Nuy1b-r80fW6D8dMoiRQl1bX1T1fkQohE9iRqtyieSrchJSm6rEUqnYnS0vH6Y8WlQUxYKxItRzF2ihntbXz4fiPYUSsdsMKi60CpHO8r75auT8E5tI8KsNmyrCmsvz3NIM6LngOvFlBLCoFx_jU3Ur_NmRSeHNUylwIaDXx8ulNCXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
🇪🇺
به‌مناسبت فینال لیگ‌قهرمانان اروپا نگاهی بر ۱۴ بازی گذشته PSG مقابل انگلیسی‌ها
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.2K · <a href="https://t.me/persiana_Soccer/22418" target="_blank">📅 12:13 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22417">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ChYj3OHUXPnvmGvA5Xr4svy8ivYIRgA1GVmlC35ujrbCCG50LipAjJR1IGWQMpQ74tJlkBIA1bJvO8EMub5U_pwLM9jONtWpL2tfw3A66UNJfw0f284afr1QOQ0ONo5d-S0gSdI76kI1QHrjUy3lrj4mv2oxhhpOCBywPQweQyEbJQYZxlSdqchu-habNFQ5H0P0Z49OTAHSjVaAQyeQnI-M0XU1QOqgqhoXBEqbAPvY5UjeSwB08tfbkPWQBpKQgJ6lIS37jMwB3y0IhBTcXq0xhhY-vlojJuNINT58s71U4ev4ObKCIu0T7Dl_luhxfMpBvCzU_tkBhx5tbZ5bsw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#نقل‌وانتقالات
|کوناته مدافع‌ فرانسوی لیورپول به‌سران این‌باشگاه اعلام کرده که پس از جام‌جهانی از جمع شاگردان اسلوت جدا میشه. از رئال‌ مادرید به عنوان مقصد احتمالی این بازیکن یاد می‌شود.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38K · <a href="https://t.me/persiana_Soccer/22417" target="_blank">📅 11:38 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22416">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JyvXOJk2H-bZEtvZwj62JPBM7AEKrBi4M0UssJVSx0QvCfQdiQePz0lkPlZci6JUPiIAWVjjWF_ZIpnKic7DJB5wz3S3XooGGZ5e2TkBSzDP585AI_1mtQJeubYh4I2PJiWeddx6SqXicdOpQ1xnvyHEU-Ywet_hpWZ8CvL6_6lC7ai_LwZNRCNJoqTatWe3cLVYBlI7Xlwet6I6J1nGVSmy9suVBPgpbX9yQTnzo1maVuUXUZF2LNnup5Xup7l4rrnYMAwlXJ0fZ2zE3b6Qk-jeWVVzkWb4hdP_B6LEHkYbB9amltEF8hwZLyxwvSJZQP49nB7JEEnPN0dNAxn9vg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
فابریزیو رومانو: باشگاه‌بارسابعداز جذب آنتونی گوردون و خولیان الوارز باز هم خرید خواهد داشت. هانسی فلیک امروزشخصا با آلوارز تماس گرفته و به او اعلام کرده برای فصل بعد روش حساب کرده.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.4K · <a href="https://t.me/persiana_Soccer/22416" target="_blank">📅 11:33 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22415">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bVwZkX5by5RwpRKonHhDXHG2CdlePv3GMEX_lCESQfS1QpZNgIwnEftnzlB5z_NdLiqOMThWtlsJEBai9mTyTzY8ZffuPcPoa6vVXft41rWc3EvckiVoSupAHBa0yINMFnfLzG6end6Y0n5jB4P5xIlNO79OSHzzdvTZIzssjF69cU3am0Ax-5VHjxfB3kJxfJPjkzgDhsk2yoQK9K0vvErfOboTQddFEkmn59CLGyHCNcZL6VdzQalf5FMJyNWyEt2Ue800CEF6bgRiN_sKmcZwiUdI7Gbar2ywjwBAN7B4Ny1-k7NrHBmf2yQ7-xuMEOqedUqgG-0uNabAAztRIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مایکل اولیسه، انزوفرناندز، ویتیتیا و ارلینگ هالند چهار هدف جذاب انریکه ریکلمه درصورت انتخاب بعنوان رئیس‌باشگاه رئال مادرید؛ انتخابات ریاست باشگاه رئال‌مادرید روزیکشنبه 17 خردادماه در تالار بسکتبال رئال‌ مادرید برگزار خواهد شد... فلورنتینو پرز و انریکه ریکلمه…</div>
<div class="tg-footer">👁️ 34.8K · <a href="https://t.me/persiana_Soccer/22415" target="_blank">📅 11:21 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22414">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qPqkMFMzaF-mRiFVffLmvG8pKbfkQ6kc1LW0WiGRioc_UCDnIOQgW1WyzUg6tMtmdVzbf-bhakX5O_35VgDkEBLAx1FwBfBiiq2Q5sI39EbZ4wJTJC6dji103VwuT55emo6nC8uTy1NIB6nIAyJPi6c9qgdbW4WObRY7Ofr6dPa9pe9cvigsjblXTEKcOSJ1Nimp0wgsE7hV1bWAtzM4hhL8YRzUdbM-cr0slHy94ms8muLn_TSmqerBywamHIQ_trhRksi9-u4FAg_uH0nvVqXdWOITG4AQ_NMk4t_q20O2t7ckFXP2MIDhfphgaNDyJahQ6UPOZKHw1lQGrNSfAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
مقایسه جذاب عملکرد ژاوی هرناندز و زین الدین زیدان دو اسطوره تاریخ دوتیم بارسا و رئال مادرید.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 33.8K · <a href="https://t.me/persiana_Soccer/22414" target="_blank">📅 11:21 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22412">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NLcq6FT_ErSvrGU5M3Y43JXtUyidgzlFsJ85R7loueAE44KiYiCwH8IO7nJfsiChJ-59r-C-XiFwTTsHpEJLzfw2U8s6ZhsfzDOtz-X6OPOGEzNpgqvI9bsfD4ISZS6gIxRfa35SZvxRTyIN75-ZrKH5VPwv1gYAxfnOM9u2F6Iy1DyLEc8WRinEkwE3DY0SUXvSvqYnZK9bDZriwmwTEr7t8GZYp2j8uufbisKJ4xr4l1ZoP3x7ejLsv-_lB4F0M5c45u9TyILYtgXNVdPxb5jJ-_NY9WyYymqTcGfhcSVSnZ5ST5s6GqONIkD_tvEJw4AqxLl2Dko4nrfh7QVZEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⚽️
برخی رسانه‌‌های عربستانی؛
خبر از مذاکرات مثبت الاتحادی‌ها بانماینده یورگن‌کلوپ برای پذیرفتن هدایت طلایی پوشان جده در فصل‌آینده میدهند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 34.1K · <a href="https://t.me/persiana_Soccer/22412" target="_blank">📅 11:21 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22410">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">ضد حمله‌ و بیلد‌آپ های تیم رئال‌مادرید؛ طوری که زین‌الدین زیدان با رئال بر اروپا حکمرانی کرد
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 34.4K · <a href="https://t.me/persiana_Soccer/22410" target="_blank">📅 10:52 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22409">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c001aed77e.mp4?token=Rf2hPrAbYd14Tkbi6zWZw0IxBxTe1-Dj_LJqcJko1gtqRKjMA8WhxnzA3TXhfGPwtGU8HLKcEanxA1wBBkzZYg3s3E6IH2icGjMrf3iybb12hoGJPNEhu_fKV2pgGtsJRssZzYVN4AuzMOynuBuPLuVW9bOwDhzRUs3uYYk5RF0eu92qfbAOnQ2Gxg4FgwbA7KfLSKrUfmMbV90mT52rcRUv1mAvRyC7U8V7bojRQWGwPbdiKziyaf9H1FACyAGCJ4IALXWbj2lQjfjFHW4RFf9axCiQIoCsyfasuimthlIspayXhXFWc96_6uQozZOy9txnU_sav6Q4IkS-eOrk357VZszfMwOdikUm7H7cIPVFfKLLQHLRSRwUOkYD_KgeyHVc5CLNxuJLbKIhf9Jn2g9embJp7TVpvH-ywExHDBfHizLrBNfpL6vwjORGYa_zVWM6i2K8leoKeNzoTvqSS_bXP0CDO-gx2lUdsKYC1r6gBPO-9arwxenZtDpGv52DMTMCwz80ZKS5C4o-Io2jAjBec2MLb6gBEePZ3L6AnCB9lIFm_Xf4nzuVA5epJ6-1-HFTFeP1rUla32qovz2rJQpM6ewxoZrD19PmbBmgeJW1MN2jXps9ZzuBjzJqQ5jeAHvlx9etfSLbaDiQbByDKxh-9DFTaiUzquu09OKQGr0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c001aed77e.mp4?token=Rf2hPrAbYd14Tkbi6zWZw0IxBxTe1-Dj_LJqcJko1gtqRKjMA8WhxnzA3TXhfGPwtGU8HLKcEanxA1wBBkzZYg3s3E6IH2icGjMrf3iybb12hoGJPNEhu_fKV2pgGtsJRssZzYVN4AuzMOynuBuPLuVW9bOwDhzRUs3uYYk5RF0eu92qfbAOnQ2Gxg4FgwbA7KfLSKrUfmMbV90mT52rcRUv1mAvRyC7U8V7bojRQWGwPbdiKziyaf9H1FACyAGCJ4IALXWbj2lQjfjFHW4RFf9axCiQIoCsyfasuimthlIspayXhXFWc96_6uQozZOy9txnU_sav6Q4IkS-eOrk357VZszfMwOdikUm7H7cIPVFfKLLQHLRSRwUOkYD_KgeyHVc5CLNxuJLbKIhf9Jn2g9embJp7TVpvH-ywExHDBfHizLrBNfpL6vwjORGYa_zVWM6i2K8leoKeNzoTvqSS_bXP0CDO-gx2lUdsKYC1r6gBPO-9arwxenZtDpGv52DMTMCwz80ZKS5C4o-Io2jAjBec2MLb6gBEePZ3L6AnCB9lIFm_Xf4nzuVA5epJ6-1-HFTFeP1rUla32qovz2rJQpM6ewxoZrD19PmbBmgeJW1MN2jXps9ZzuBjzJqQ5jeAHvlx9etfSLbaDiQbByDKxh-9DFTaiUzquu09OKQGr0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وویچک شزنی دروازه‌بان 36 ساله و لهستانی تیم بارسلونا، بعد از ۲ پاکت سیگار و مقداری آب...
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 34.6K · <a href="https://t.me/persiana_Soccer/22409" target="_blank">📅 10:38 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22408">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3294ce3a0b.mp4?token=i5LR-Yg1ayhB7ZgVH9uXRtjMZGXkmjHzae6F5g8I-4yLZoSGmHMd0ytNI8QcSq_xDOOnpL2FOcWihS2q823kPfmMsWoT2l0S0pHv8RdrGKAyER90w-8Q-Mqnz09pjg6wAIROFbxZ4iBCHdsCSVKmEObpOZZKahlnKyLG8I-V2qkNh3f_Ht-5dl9b6TOvCH7e5qAF1IsWCSGrbD531tl4Wl24q3fAc-WBJWQffSM4pRQ-iXpvjpMrb30G--ca-Dpkr0S1L6N8w-ftlgpcYEStn0i6fBjq0NooCl_QRswY6odCsDfK5OhZx4SwxjEz3DcRBwRzGt5Bj4u2G_PvvYRyRk-1M2aTviOENW9RxtdkUmLw-49jUBtLqRlw9sqKApw-1veiWqtuEDpVvH_S1aXDAdhP15jf2pwGvPyo4fOMXWRFgRLFdP7agGF3bzquqybYgfVClMttpF1tpibrXOVdBzoXQpjUSV5ZnrhCt8245GzxJ1bGRMZTLxdw0QKsHqBEEN6ZMZWq8y1Dal9Jij_NH2Dd8xsr7RNSiEihnQMjChe39BGf43jnhKSs5E69ALD0cNn-xu9sypb-otXrmKWzwz5SV3WJVbSETwfQVonwuA_DyKhyAagrN5BgS3lldKGLw1I9WxHs7o-K4d8qHO90qP9UhqyOXCZqfo2qzerwqWA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3294ce3a0b.mp4?token=i5LR-Yg1ayhB7ZgVH9uXRtjMZGXkmjHzae6F5g8I-4yLZoSGmHMd0ytNI8QcSq_xDOOnpL2FOcWihS2q823kPfmMsWoT2l0S0pHv8RdrGKAyER90w-8Q-Mqnz09pjg6wAIROFbxZ4iBCHdsCSVKmEObpOZZKahlnKyLG8I-V2qkNh3f_Ht-5dl9b6TOvCH7e5qAF1IsWCSGrbD531tl4Wl24q3fAc-WBJWQffSM4pRQ-iXpvjpMrb30G--ca-Dpkr0S1L6N8w-ftlgpcYEStn0i6fBjq0NooCl_QRswY6odCsDfK5OhZx4SwxjEz3DcRBwRzGt5Bj4u2G_PvvYRyRk-1M2aTviOENW9RxtdkUmLw-49jUBtLqRlw9sqKApw-1veiWqtuEDpVvH_S1aXDAdhP15jf2pwGvPyo4fOMXWRFgRLFdP7agGF3bzquqybYgfVClMttpF1tpibrXOVdBzoXQpjUSV5ZnrhCt8245GzxJ1bGRMZTLxdw0QKsHqBEEN6ZMZWq8y1Dal9Jij_NH2Dd8xsr7RNSiEihnQMjChe39BGf43jnhKSs5E69ALD0cNn-xu9sypb-otXrmKWzwz5SV3WJVbSETwfQVonwuA_DyKhyAagrN5BgS3lldKGLw1I9WxHs7o-K4d8qHO90qP9UhqyOXCZqfo2qzerwqWA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
یکی از مهم ترین دلایل‌موفقیت انریکه و PSG
: اون برای بازیکن‌هاش‌بجای یک پاداش بزرگ در پایان بازی، پاداش‌روبه‌بخش‌های کوچک تقسیم کرده: مثلا هر پرس = هر موفقیت = یک پاداش عصبی کوچک (دوپامین). نتیجه: انگیزه پایدار در طول بازی.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.1K · <a href="https://t.me/persiana_Soccer/22408" target="_blank">📅 09:50 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22407">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cc6b58323b.mp4?token=bwzmb-S6ebKNcYoeVHV8_Kotp8CufGhwrjYOdFj1umDqhIvuJnvG_9ITa3fc3LPIizQ3RBm_YeqVj0rQuO_HEmU8QhfXAbq5eev3U7QfBYSWa_w7vPyGZTl9el387jdZyut0qMg4sAF7wkWFbpxtAQ_kKX_Iks25Y59Nas7vlZidGOpt8S9TKOsXkkHWKd7d5vx8DbAPAVGrksvwRUJL52-ydfRsAaFuDAQQmzo31uA9r3X06_V5ZCZmVbBOteDWtY2UStt5FetTPn0CVojZV8PxBqiW6x10yTAho6fOv3vKnf2pbz80KNQVcBpotSyBgthK2Hs99T36vB6IERnGMA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cc6b58323b.mp4?token=bwzmb-S6ebKNcYoeVHV8_Kotp8CufGhwrjYOdFj1umDqhIvuJnvG_9ITa3fc3LPIizQ3RBm_YeqVj0rQuO_HEmU8QhfXAbq5eev3U7QfBYSWa_w7vPyGZTl9el387jdZyut0qMg4sAF7wkWFbpxtAQ_kKX_Iks25Y59Nas7vlZidGOpt8S9TKOsXkkHWKd7d5vx8DbAPAVGrksvwRUJL52-ydfRsAaFuDAQQmzo31uA9r3X06_V5ZCZmVbBOteDWtY2UStt5FetTPn0CVojZV8PxBqiW6x10yTAho6fOv3vKnf2pbz80KNQVcBpotSyBgthK2Hs99T36vB6IERnGMA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
وضعیت شنبه:
آرسنال با یک گل مقابل پاری‌ سن ژرمن پیش میفته؛ داوید رایا گلر ارسنال  دقیقه 34:
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.7K · <a href="https://t.me/persiana_Soccer/22407" target="_blank">📅 09:35 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22406">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q2ozVETuLpNPBGhSAizrIMDqId8oiUOACEbVPkI-AcDljFBBd1HdsO_-DUiEbC7Q_0EJZ9mrqZxfcdWERrMJgxg8vnON72JQVRbYNOgwax6jlEiIYDXv04PIRCA0PfEeLJG3dnfNgPG4KLXp49bALSU17tp8gvtW8cZoCpR1g0Z7kypiZpAM2EXLR7wB1Z_7SyLAd4iOfLqLup4LRBukwXO1j8uYqJBe68lCLlTF-iKL_wBYLyojqN0RWS3xLotm8ZqqKALgIfw7TTxDXJvYV9aMeABB2qpI581Eo2peLfN5omgatG_kC0GWgurnVLNfASo7qYcGvM129KKv5x22yw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛ خولیان آلوارز به‌مدیران اتلتیکو اعلام کرده با بارسا به توافق رسیده و دیگر انگیزه‌ای برای ماندن در این تیم نداره. اتلتیکو حدود 150 میلیون یورو برای فروش این بازیکن از بارسا میخواهد.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.5K · <a href="https://t.me/persiana_Soccer/22406" target="_blank">📅 09:15 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22405">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LeDxF-6vHX2IMbHUc3IIkyUIll-8oro7YhfQRdIKOv8jnoaz5i4pge-0QKkgFGYqTrZ5sxPdfJkZdJFUyvqj7DLiDjdPAkk6zTZKLraiGXbLyudXnZXuIFo2Z4mdRhIAcRWn9W7lq0jP-xKLvGkl1wzTFwmLJnsRg5HXpRmr0F_4EkTb0qik5P_GvnnSopFTkb1kXdKUzDmGmHriqunbtNiydPjz-p0MwwX8rRp57__b3L2pR319BYm51DOeqVrTe1dT6sbiucGw5MsZziRdJ-B7giEwhq4JTduBZhoCCeO7Po7f6NhDtaxf3NmmNe3wVtkvwEbggLFvQCwM_F5EUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ویدئو آموزشی‌نحوه‌واردکردن‌فرکانس جدید بصورت دستی در رسیورماهواریاهست؛ شبکه‌های یاهست که بالا معرفی کردیم همشون تاپ ترین هستن که بازیارو باگزارش‌فارسی، کیفیت فوق العاده، بدون سانسور و تبلیغات‌آزاد دهنده و جلوترازصداوسیماپخش میکنند.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.3K · <a href="https://t.me/persiana_Soccer/22405" target="_blank">📅 09:04 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22404">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TwWuefrqPd5ftLHS6a9nCX7jiSvYxLLhOjqjDPcx7j9tS6TAW25JPHXHfFm8TORgqOavd0TcRWa2-Ott3PwmJvFvXWXlJfcxmeASrqDK1lWp-_11ye_1lCRrxp4gOuzpZTm8gyFlD9j2C-VzyNfEAonoWkGnj3n7y1Lir0RCbAXXzGqdeSGfNo3IzZHoXSZx2C8oyYtOkWv1lPfYXg1DHHqczcD7jVR_atolLielnKJMtxMFZpJnuT7HKAj53u1UibJPEm13A-t9S0rnVOdTLePW_ngdx0rMNmCHNktbn4fZ_LDKC41Yj3M0F14xCo6Dp6gfEvNN3_bTsNAxCu4hdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛ الهیار صیادمنش مهاجم 24 ساله سابق استقلال و فعلی اوئسترلو بلژیک رسما از این باشگاه جدا شد و در حال حاضر بازیکن آزاد بشمار می‌آید.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.4K · <a href="https://t.me/persiana_Soccer/22404" target="_blank">📅 03:51 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22403">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HX5O9lDb9NUB8M8_SN2U20vkMenYly4Qqyi1P9NdAd1KVjjv25CIlsK5y3Ay_Ple5JQR7b4SF1hb6QwrjI1lG9Defg4B39SyxNfTLe9VV8BkUFvrMNrIE0FoCl7NQkLi-xpwHTwnEODZrddQCkCaSbWVjKKNIvbfQvkJSalb3-JWiX3a2UsyAtI94duq6gdEEHJ69yuTc6ttaAogGTrhRSsCyAJytGJuigeUOke6NioATF_5HVnaggYErEnwPX2Q-9za6xYRuSj5CDjz9m3G2rd7N9mOAhDE8w6n_xg8kz2VyKyJqHL_l4c3uKsXNL8TM-q0DnWNGEZerBjMg5yBQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
لیست بازیکنان تیم ملی آرژانتین برای رقابت های جام جهانی 2026 با حضور لیونل مسی 39 ساله.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.1K · <a href="https://t.me/persiana_Soccer/22403" target="_blank">📅 03:08 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22402">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DxTTzTAFNYqDJpOMLKS6D2IqXkyzAoB1wuJ_1rAlqrx1QCLtfkeTohOyONksNe4aUrbS1Ap-wLv0_AeupTCrM5MZK70AoTOo9VbmRwwNrrBzTs3JdEwdIvBxj4NqcdnApJDV8kgisG5El3nJ_2KFxCpz1EGuSSlZGmEEcNiMJE2t9Epv168kxfUn2bPLy4ZMW5mwTMuRbVJIJL6offqfDBDvLCeoKaLrwxY5p6aNsDzmDDhSSa5uJE1FBjMiLaQ6iOrNPV8A8FCrzEpYSPYo-YKmbjMj8M3czwX64Qv1epe37P0dclMqK67yL_CKzQTzQQvnwQx49tqxQXwkTu2a0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه بازی‌های‌ امروز؛
دیدار تدارکاتی تیم قلعه‌نویی مقابل گامبیا تیم رده 116 رنکینگ فیفا
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.7K · <a href="https://t.me/persiana_Soccer/22402" target="_blank">📅 01:30 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22401">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/coho7I6szMbLOAcVebgEohAhsBDDdeLys4ocpsXW2LkK1ZrFtrJ3XgRQloC7JFfoETNLQP44Qzfual9Gp1p0iW5b4EeQyWBEN3ImUEb9smD6Fh9yAuE-VLHXD0_RIMjlYdwwMdPpfQQ34SCdHEUcKWeCMW_tSdwjsEz9VlVCAlQVkNGWr3XFhKp-qFr0ssMnXI2Eu0TqkqfNivI84ipnDEY6vwR3Wi6RYcs_yZQPNYsHAJWb_lDqlnbrWZXIr5HI_nEmOS7hXgxXafsrEWAzexuRLDrzKjqo1H84kp-Wr6y69YmTYIEJs_TezBRbcswuHNb6KbcRf4Q1ibdDJazKXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج دیدارهای دیروز؛
برتری مصری‌ها مقابل روسیه و شکست یاران لوپتگی در جدال با ایرلند
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.1K · <a href="https://t.me/persiana_Soccer/22401" target="_blank">📅 01:28 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22400">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MUYXvFf-oldJ19On1rc2Ip7pUwk7TAwgRWZH3PjTyaYFcYjEKn7LnXSQ9evOBh4v4kEYdCH2DsII9cB0xBDoVqqYzmU1YswKISigj5Dij7Lxez17S-XgPtUbmzhIf4wOdvwmCpKYIJ_5H9J1sgSsTzL1z5YZt4XyYstst6O7xNvbQS-tl4HqwA_fYE2Lr55yAGYrt5nFMo_dYIPXhseGlmaHfw0j2kN8bXuEnT3GHnFjpVFrDxHUDrhgesl9MzYprrEHTJRiMAiifkETXhpQP8wsLwV9noaY_huawqFN1i0GuwZ1mAy_a4QNBeDdAckUz2cf65Ri6fboZnVwAWSAfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
فابریزیو رومانو: باشگاه‌بارسابعداز جذب آنتونی گوردون و خولیان الوارز باز هم خرید خواهد داشت. هانسی فلیک امروزشخصا با آلوارز تماس گرفته و به او اعلام کرده برای فصل بعد روش حساب کرده.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.1K · <a href="https://t.me/persiana_Soccer/22400" target="_blank">📅 00:02 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22399">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KDAUlc4VpZgkIlnNEIzyAXd2gE18bZm7IvxK6G-GMFFdYX21bspdycbGIVpTOfRRGikk9uOBG34gWB5gRCBuKzJDfdAh6XVFy-DgeWnSEOJeE3jJgMz7c7p_qTfpiMBXXOTeEj8J_3ChSBg2larjioTHF-NSYIBbNihiKIsAA-1sS4Ys6Ud-h8hMYwr-7DarFBvcr5qXaEMAgCkkhL-uKMEqAWRsbPq11JfR9KeOALCEELm4pmQHj3WMvKsz1G8fz_MnfmuFH_aBN4aHg9aX_WjBTFy8c7W5e7xBd1udkAPeLpBlvkmkRiY2rDgG1ZQPnoZ_NO73OamDWGXPebJdfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برای دومین فصل متوالی، کیلین امباپه فرانسوی بعنوان بهترین بازیکن فصل رئال مادرید معرفی شد.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.6K · <a href="https://t.me/persiana_Soccer/22399" target="_blank">📅 23:34 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22398">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v7AzbV0naiGLOZ-Zm2f-tjXIefUxyeNqywuEHeLJv6LB4nuonPjOHZJIeBATtI72Mn_k2K4G2bHpSshBrGTzZPlKrKf5xB6W9scom7583sjECCberRXRmJTxeC5WjIHGeLNCzsmz-LGgGtcv2dPhRN4R82Kxu6bItKluBEJ0WDKhcl4q-XSJE7Ox95Cg4nr2ImW_yBCAcfi5Ca2MuKDLGDNpsVDdEAiH_F7YIYVLOG1lczhab4lGK9xe9SImzlep3D07ij9AuSh5Ud6yaLSiW0nzPEPW1tvrKNwU-pCzr4omujwL9wN7Bx0iWcO8EmOU16Dv_YAvnaIZsVkAHBRYTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#تکمیلی #فوری #اختصاصی_پرشیانا   دو باشگاه تراکتور تبریز و استقلال تهران از طریق ایجنت مونیر الحدادی به دنبال جذب حکیم زیاش هافبک تهاجمی و بازیساز سابق تیم چلسی هستند. دستمزد فعلی زیاش 750 هزار دلار در سال است.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.8K · <a href="https://t.me/persiana_Soccer/22398" target="_blank">📅 22:36 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22397">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4da3d833bf.mp4?token=ViDhcFww1GUDjGgx-nHJNUEe1pbCUPoHCoyE8irDvYvdMiXWND8xLI7fHaS7cJz4HfYp2XW0lgZSVtvkupvFMwXTW20o9TCizmyeUOW3eimWodxIDv34tL7CfFh5flqFujgzITIrb_PZV3NOp-fo9SwjsEWdXNUOJ8sg1RCih3L1uoQKjTKS8h1LFkFq2VzxMmbvg94U511gIRziWwl4Z0F-kfd2P90OswcPSSaFfmwoVjCrpM1kDkrmr3AxUZssdLRrWyv3784C5SjrE2psu9Pr38jBcsbj5EfBQBXQ_8kaK0xyRxG0kVon0qdWFjn2ls0bvJ3nqpr6PAjfm5oi2g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4da3d833bf.mp4?token=ViDhcFww1GUDjGgx-nHJNUEe1pbCUPoHCoyE8irDvYvdMiXWND8xLI7fHaS7cJz4HfYp2XW0lgZSVtvkupvFMwXTW20o9TCizmyeUOW3eimWodxIDv34tL7CfFh5flqFujgzITIrb_PZV3NOp-fo9SwjsEWdXNUOJ8sg1RCih3L1uoQKjTKS8h1LFkFq2VzxMmbvg94U511gIRziWwl4Z0F-kfd2P90OswcPSSaFfmwoVjCrpM1kDkrmr3AxUZssdLRrWyv3784C5SjrE2psu9Pr38jBcsbj5EfBQBXQ_8kaK0xyRxG0kVon0qdWFjn2ls0bvJ3nqpr6PAjfm5oi2g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نت بلاکس: این‌دیگه چه کشوریه یا ابلفضل. اینترنت ایران برگشته ولی با اختلال و فیلترینگ شدید! هنوز تموم مردم ایران به اینترنت دسترسی پیدا نکرده‌اند.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.3K · <a href="https://t.me/persiana_Soccer/22397" target="_blank">📅 21:33 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22396">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dD5Q94Ca1WdfmwvCDD6wKsADl7Z1nPiOfLuHuZ0ix6SJBGzGOVpimZ0p8-dTXvOk6-jC1axr92sgyyPNOMqLVdVYXnM40b--8-oF3sV0pIGo9oBS4FwtIQA9BSL2Aawj-j4zs3TuUjqwn3tWePA0Mi4y2msUHj3ZXrY-aKM37BOSH80O98_LrutQjcSOmZrdNEZmEdnXgfmZM7Y8nvXyaowpOyOk19SC2nEWxpCw5UK5dkCSsjyG4YUQotUHMHAcLjTwaXXhg0Q-VC1aAAcWSKoY5mfG3VbY6VdC-jGyUIQlocNnphbfrYrXIIBu8x2NaUffHUVQlE18NUg47RE9AQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
ماسیمیلیانو آلگری سرمربی فصل گذشته تیم آث میلان با عقد قراردادی 2 ساله سرمربی ناپولی شد.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.4K · <a href="https://t.me/persiana_Soccer/22396" target="_blank">📅 19:53 · 07 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
