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
<img src="https://cdn4.telesco.pe/file/hifPu5GDa8jtfV0viVJp9frf4UCPGdMol0Qdg98lNebRu7rTO-o5EIqIiEk8r5jsr6hJCX0A55l7Z7yi41xrbjoB80k6cSkpmBdjXqg90xGwHy57ZFRemzfZwRCM19OzfmsYKXtfUNuVHynWqjevyu0ILe4CTBCg3AoqxjCWWDZ9jzXUQqN3PPhSy8tUFvxmVv25XCShb_-rrrHQOmDDQ5z3S2L6A71_He3z-kTM6iUwforljftFbDTaE9hdsHQ2ah4n0pVH_psXs_kP5qYJQBgCOhB4uzY8oTOx9zBNYbubpCl0Tj5QuZzKy-CT7p7BUDDmHOWlVZaFdx3jPjjZvw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرگزاری فارس</h1>
<p>@farsna • 👥 1.8M عضو</p>
<a href="https://t.me/farsna" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 حقیقت روشن می‌شود‌‌تبلیغات@Farsnews_adsارتباط@FarsNewsفارس‌پلاس@Fars_Plus‌ورزش@SportFarsجهان@FarsNewsIntعکس@FarsImagesپیام‌رسان‌ها@Farsnaاینستاگرامinstagram.com/fars_newsتوییترtwitter.com/FarsNews_Agency</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-03 19:27:26</div>
<hr>

<div class="tg-post" id="msg-452505">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q1wxiiV2rI1hNgxSfiGo6_H-sg6D0YaByNZa4rklSbDPeAsK6uD6ILFPlR0ku5TSMnQeaMwehjugHuzhpsjpkSkCRswJGNiWoeodcvvLzJ6A30boKmwXd3GAcKL7QSu_VT3foAEjGw8E69FkaNXy2-a71Tb0F6Qne50mPspl41ZZg8y-2B44-3VTWQgsl4SIcl60wAPCj_U2gkLFShupyInh69rdeoD6Ev_apXZkNN-bAKElq4lH5UeN4Rpdhx-aVIKKee9iwt--J2-JwcEzm9qgCE4-PxyXfUBvKQnTcoqgL3qzmkTN0DhD9RperuwhghC9MCNkK05R7jsKw3M2EQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‌
🔴
سخنگوی نیروهای مسلح یمن: تأکید می‌کنیم که تحریم دریایی علیه دشمن سعودی همچنان ادامه دارد
🔹
گسترش اقداماتمان را در چهارچوب معادلهٔ «تحریم در برابر تحریم» و «تشدید در برابر تشدید» انجام خواهیم داد. @Farsna</div>
<div class="tg-footer">👁️ 2.72K · <a href="https://t.me/farsna/452505" target="_blank">📅 19:15 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452498">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rP0S3V7YWsfycZExVVfOqEVr7b5IUafPaxFPApYTQW1u9-9NNGlSZQZtBy0E5alBtY-JsNnQ1c_ql1HmETcBvY2owIrntrlvsre8itTyKnEWa619JuwYvMULWOXPtAJEqJX-jxqHaq3War74PGIjsM1TpWdR7bCxyZ59peB8GU0jwQGatLBZfB-0LV3yKfEMBEfUcC5LzZapiWN5L-cSmnv2CAEylvBNtJZHQrukFAxwifBYuqFRtI7YQZbv88-va3May4R6oobizr33RsGOr6gYbXYuMh8oujeGst8I5Cea-LVA7Pa6onHyOIt1UR-9E_a3Z05s5ZwhKtgAQCcxqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hDaRyWi1uPyBg67FhTI4enedPFfYNotbHLeHLG7OOIuX2S1IAKDYAZWRtTsOhfRqgQ27X1l-JSG9xc3jiaQKjqijQ41xZe_QJQsQ6eGYgAn7MHGEbsRa8-tQ4lircOjMBUi74AmrMUT3W_2OKzD6s-ft7Qf6jlCfTyQXebYmc0q9icMmQsBA-0IJAZyLENzUyp4e31MlAqTVTDoNV6YjKYt7GBnhadDPVvabOa3Mqi5mXAAsy5LvetaxwHdsfW0mcgn7zjUp161EkmTjWFnb5dsdUfNVjvFjCGn2n65hGHLKNMutdGeoSRra79d2xdVxSCXKnyIGWBaPhofq_sp3Zg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hb0pyNb9o1ayJYuPaio5a9djNN4LfEEau5ZHVp2Lm3Czm_SbSH2K_q6whzpsBrw4NpwEMCe2grGC5febNJFRGIC2b4QVAPkhXvhQ46WsEo4aXDk99g1SX3Ug43avo2MkvTOb0Q9QAvL0UG1QA0j4c8m8cDDufPV18d-lt-o9TAfZb6mzxT0MefHyI811N43ksIp9rKQNwne1n__rbkDaedpRMcda1hLn5Hfzm5Aq3531hI5lbfziCex3blatM9Wpx3NyhRFqij20twggsd5Xjh_9ZclDMKx6neQaHJEk1Nj-Zmm8cOLQGbKr4-sSKabsVl2vmw6FOPFWSMNrnqtANQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uf5gK0n7AB_iZkKMC7rtHwH4X-_aAiyDY5U_oyJnQf3zJ13vX2jlr6FHKFZK9-AFinC190DS07A79XJ7dhmrFoQRvQY5qPfh1leZQtmUzip8OxxhpG7BDwotXtbQSqD2K1su5pi3vmwysyi5GqyOeCB_HupbrCu-5BkhQyc3EU1o6icLr0OkLyMLcAwNjUCVFBLtCqJVlMOBg5Arqgc8735CqGSvGfB0J8vh6sBdKjIHzJ9e6GYciLeTCkfKzKKuPpGhLS2fcl_H1MBetKqERVz2EQvxBRbGoTxSgQetQRqDqvekxpQv0Li0uyDAV79ZlLFRMa3LditAS4IAeoB5fQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BkuSvPk9g16QpX7L_tVc9eefF5VVbGcqniORSpQR33wq9Beap9vd6TffCK7REDUvcDHgEQihLrepHw_gaOfxmM2i-_Is336oCAWSEwn1hIavcNUJuv5r5DVhTOBmoM952KyD6WYtA0LEVaNykGAT5_VGiw3-NTghASGZ0v5c52GUIkGenaULiVap5Eyzk4qRRJCjKFHh7H4_D5tchWSJE_n7Ua7p0Z_aB8bRCYJNN5p8os0tfKjl7ifJeZcSSLMbrUTGP6PMRlhya60GGyEl1GdbVeSrjRVEdLHQq8k7OXhWerVBSoGULYHY4LEfffACSJEW85JaoMyw8oYdvGr0ww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/P4yaMLlyAbHBir8IwpPBV63YxZEdK200S1uIwJDxvPkaESh7ZzWuD-UAoAOZi6DEm2Re0J50Pq2TDepA3hVkttDPERe8X9bfjY_ahN6NiJFIkNo9fNDfHPo__yRlhcN9S9KhQEGZvlOfeo9Stdh3xoD-DHLIzj32Vi210yW4czZX4_clFlqS58I6BR_b8VvQ3TFUu6IjakqfNOiS2guR5kz9D9DmAKJAM6cBocD0Jr7vrfdnwgUsVANAsd4fQspxrLORyaQdgqwS5OaJmZ4yHDX4ARD5aUwnZ11MTxEYD-_sWmsCjnQw4CWl2Sf7pXETn6V7Is4WNcckUcrNvoo1pw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Yqwzkdw0cHydod9As5r1aDt6PV0JcxJa-vwikdsOgdj8zXt4rhdHghSjgg5dbaFe7W15tH8sMHb4M-gUrqn5X7jMo3wnslnwMiSyZIMk0CLM-YIIMSlGagQovh1wn_jSIbO4mwzmC_cfEj44SdiTZAJxdrq3q8Rq25aDKrDc2_8BG-jEf3d9bUtdWMfvjsJ8Wn6j4o2JW3DYZLzPcF0bwI-QUVJdPB0BXXZvU5kZnUztpXdD-J-f-m3h2ssLGeFr7Y8zphavd2-HKkGE1qSFFMgCcPCzJ2DolwnGBNnPKtCdwNroNA72cWOtID5hDGCT9hQJ3e0VeLCM9IKPPYt3JQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
شلمچه از قاب کودک و نوجوان
عکس:
فریدحمودی
@Farsna</div>
<div class="tg-footer">👁️ 3.09K · <a href="https://t.me/farsna/452498" target="_blank">📅 19:12 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452497">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VxuUHsXt0KnfMUmNXmzUko37gDaVIFMGC2K04764WLgTctKRvVK5pGUG6fEfdxB2ddIvIPu5RoF9IlvwscYQBniCOnv9qDBWx50erj7F7EtGr9sYgUQY6-FqTVEb3825kNWHPydv2xAkezXKjBVvFerdZT8a2bvi5P7trURzl47aTRd8mtRhpqVOvpiWkaYrDOXHjYo4rfzp_UM6hscAhHaS1x85iPM-3yUA5297DBZX8OcKytHfSjtYXxJZJF5ofIZn4v5zTK0vEFZp5ONPhV8Cg3fZNtWkEOOOah7vF5kg2skdR_HVQr6oIZH4gQtodf_Zp4CyO9SaG5iP4BE6nw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
منابع عربی از حمله به پایگاه آمریکا در نزدیکی فرودگاه اربیل خبر می‌‌دهند.  @Farsna</div>
<div class="tg-footer">👁️ 4.15K · <a href="https://t.me/farsna/452497" target="_blank">📅 19:01 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452496">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">🎥
سقوط هواپیما بر پشت‌بام یک خانه در آلمان
🔹
آسوشیتدپرس: یک هواپیمای کوچک امروز تنها ۶ دقیقه پس از برخاستن، در پشت‌بام یک خانه در شمال آلمان سقوط کرد.
🔹
پلیس شهر اولدنبورگ اعلام کرد در این حادثه دست‌کم یک نفر جان خود را از دست داده و یک فرد مفقود شده است.
@Farsna</div>
<div class="tg-footer">👁️ 5.49K · <a href="https://t.me/farsna/452496" target="_blank">📅 18:53 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452495">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2f080bfe89.mp4?token=D9LbjTel-JkCTVJ3TrjsidwjNF4dvuW1b2AZt63ZB5adqpiellqrrBTd8psrNpETLqaGVpHgonhGP6MYtcv7p0KVgVmAMTaqe0NshQTAZMCic2Wm8gCl3glWWt2ZzVqUzTlpvQDomZbJlUi91QCEOOeYLfZBVuInzY4ko6MxUg8aJv0n6P0TzYHOJfSsJ_1Fp0lx0UNGL_gQ5Y8e5YpbDV2N-c97JHZSx9x_8CjCGD400c5Cc8y-2ujaUcBfhwNxD0IP23RYRqKU8cd5dlvNPzzVTEJMSNkb0qxxNVezVJGxEhFF_taftX8PnuHVhEfkMj8VPipXMxxdPwAn7W_yoA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2f080bfe89.mp4?token=D9LbjTel-JkCTVJ3TrjsidwjNF4dvuW1b2AZt63ZB5adqpiellqrrBTd8psrNpETLqaGVpHgonhGP6MYtcv7p0KVgVmAMTaqe0NshQTAZMCic2Wm8gCl3glWWt2ZzVqUzTlpvQDomZbJlUi91QCEOOeYLfZBVuInzY4ko6MxUg8aJv0n6P0TzYHOJfSsJ_1Fp0lx0UNGL_gQ5Y8e5YpbDV2N-c97JHZSx9x_8CjCGD400c5Cc8y-2ujaUcBfhwNxD0IP23RYRqKU8cd5dlvNPzzVTEJMSNkb0qxxNVezVJGxEhFF_taftX8PnuHVhEfkMj8VPipXMxxdPwAn7W_yoA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
شکوه مسیر پیاده‌روی اربعین از نمای هوایی
@Farsna</div>
<div class="tg-footer">👁️ 5.85K · <a href="https://t.me/farsna/452495" target="_blank">📅 18:42 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452489">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Jmo5xR61Y3itxKo-YCyfb1E4PCI0BhreTWqSi70r-obN731ZGANi4_tEMxDBb-9HPHlwqAOWPcLNCd494c4dbiEircTv-gWfraBK7_SC1H1VUdCLjLw4GXNaIYAuB5qFCt3eP-MApBq9SRYdl_WZsAIY8LYUiOLapG8Hygt1mtWtcE4mvdgUbMWMCq2gmlXvSS4LJNE3raBtqUBdNzc57cz1EzpNBJtxgkDtOnfJhtCEU2JJdCOPzNVnuZQ44GkjjEna3akSePmTZ8Usz6OOAwK28Kt5-1SBM_kCE8VSam7iiB6OQVL18CIeuhO8Qfkjr2E6A6_o8P_6LuzbS2i-SQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Mi3xKI2TuPGTn509RW7JDdZlvqIcx1s5T37e4bRkmatnw-Wpscpj2QnjSDj62A9Hv2ZNEpWq6DFRhnSfG2Qeb3WXPy5m4UkVsnMsiiqne19s22QMOHvWAYfN2Y_S41FdYhtg8xTurZW77LBHhhgBbHDRdspb_agEQ6z16DqPNI0Xm_hpMCy6MRiVWv-PI65YwIx4hH7LfAz7TexzS9TuZXVdNvTNEPfGvPAfUPhut0EtICpYjQnIWZ_dA9pafX3Eoskq86mx2PxA7-SxqF6i6i2jLzRZTU5M9V5R--aiF8T4F4xHhnCAM7E_9obW7isbIUEG0c59oimP3Ik8pu37Dg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pwdVMI6JvtHE0v7sVwiYLctUwjSW9KkSwUB0ub72Vovl8YRLh-Mb-Uvqn_fTt8UtFnkQaryJ0xFE-rp1lHg0Dl0kLKNoi5eXDbzY1SRtUbOFFh9i_7p_PitxssIIWrSE3QsbtPMS5__cgPgwfv5Y47XmZjMSTSqh7ZmDLNyLaeYhIiXnqGCVxfX36W7lsB9MVV_4wy2OvLpbaLhK6PPBYaXUKDWQ0TpLG7bcQLu_xd5SeA2QeWwQVF6UyJ0iwU4Prg-4rUOiw5ZFYdG_qkq2qAxIWUQ_NyC5NtrKDV6nbsIspRiUgxNlB55mqJjxxOJfGlRggzjQPwdHlasFG1etIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/haVyKWgtPxFlPJs7uKGFPuz0i4VpvfAECnpPDpdPDuIl9eJK0VEymnJ-oN_FhicIhKBWfB6EbfATHPSPSIlSHIfH9J_JmVOKrzMcZ5KQxiRFC2OpKYKgKgvd0nyBQt5cjiAnw-FfeXdqWjVoLQtXQeHC5YIiDPJnc_MyyIEG_JX29IHSTkgGG-YgN4r8Mmy_HcETa1UABOFjV6F1s-a1zz15AYNSg-cp89ExdDOz-WR5U3IH-Jlicih2nl1yA2LEK3-Y1uKb5pe0X1Z29kDeAYX-5UrmuQDMhEq8DiJ5WZdzGIAAvZAZ1c71z7_EI06QaJp9FhdIKYvUg23LOwnMGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Pe7x11YvGVUs7KV5wBkOPHyk3NI14Gb_TXH1Qt80d9mrkRcf1wTBypCzu2QlA5INyLZBPZ8spdAi__qQXpsgb-1uVGpNjbcXJQORyx4RgyI1F-p-NZXQF7EeqEq6wrmGRwLAOVwDrpekXlFRWw2dkT2paQgq8ZJKNARp73Z7cqvt3qHTeFzND4m2oqKO4lgqhJJ534n-REzcYQRwfhtKPopRI1aiMhTzYnWLRXb55hY63KR_Z5g0uYZbvzA3k7CAlDeXR9TbOZfS_RJZ-sXw4u9yvw7rCddtmDHHga21BAIC4QjVbKdrMdyGu7IpsM7qPgrcEhaDkLStl9CLN1rX5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sfs44bdvbD-PTvu9pyG-NQ4n8olNmfyNavp0sMQFbbLBvW6xDT4JHUVLOBnGprdGVGwb80vdwPA4OG8WaOgVVDFToyDZMjcRdOLtiIUPhGR8wrnx_plfjBK0H4tmjtCyPi1UkNV2B_oDG8laYg5kAxHvc9lyarausgNBVidhlL7dYNqu6Ehwl345qSxyN9u5BR6PdmSe0vSKkatr59oWMJzyERqe48Q1o_6pJ5N7dSt20R3IqkCpg3I7SZq5hztB-afWgF5qjjrfqOU4iy6JP20udqxyoTW1nglpzQyVysBvgnGlYq-UtKxkiaTeMoFw3_7X491ZeYgDaW3J38hm5A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
هیئت نوجوانان آرمانی
🔹
تجمع «هیئت نوجوانان آرمانی» با محوریت برنامه بدرقه زائران اربعین به نیابت از رهبر شهید، امروز در حرم حضرت عبدالعظیم(ع) برگزار شد.
عکس:
میثم نهاوندی
@Farsna</div>
<div class="tg-footer">👁️ 6.23K · <a href="https://t.me/farsna/452489" target="_blank">📅 18:33 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452488">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0ac1ea01dd.mp4?token=NuDCRjNlo8W2rBnTv5DD3yU1Tf4b_pfpZ_Q1JkikXthDowZ03UYxOS4xOvTRkGbJEn4i6lLDMgXYhFnp47XShrd8gq55U80h-Tq_Z6Q0I3JLnfSE33RqoCRy52H3Mpl1ENHi9YKa-iir7C_1ZfqXc_ywm-vq_6_CT7Q_8Ja00jalgIsJpKyvOdqE1d_4jlierwlKLyjpowY0V1ADq0Cn74qlLDEtb6ikZJd3YoQTOmBtA8strleETvh_0Zg9xf_gw1NblwdaCetPqIxH-rhkztdo3EFu2vh1rnUH4SScNQrkEiAFgr9eAJr0xmiKmtVT285U4tUA81SzovrFXBW_CA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0ac1ea01dd.mp4?token=NuDCRjNlo8W2rBnTv5DD3yU1Tf4b_pfpZ_Q1JkikXthDowZ03UYxOS4xOvTRkGbJEn4i6lLDMgXYhFnp47XShrd8gq55U80h-Tq_Z6Q0I3JLnfSE33RqoCRy52H3Mpl1ENHi9YKa-iir7C_1ZfqXc_ywm-vq_6_CT7Q_8Ja00jalgIsJpKyvOdqE1d_4jlierwlKLyjpowY0V1ADq0Cn74qlLDEtb6ikZJd3YoQTOmBtA8strleETvh_0Zg9xf_gw1NblwdaCetPqIxH-rhkztdo3EFu2vh1rnUH4SScNQrkEiAFgr9eAJr0xmiKmtVT285U4tUA81SzovrFXBW_CA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مرد عراقی: شهادت امام خامنه‌ای مثل شهادت امام حسین(ع) رمز موفقیت اسلام است
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.86K · <a href="https://t.me/farsna/452488" target="_blank">📅 18:30 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452487">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ur_IB5xeyTpysGbpT0eQiuMT48IJZJ7uuympdU-RgV5JlLJ__X871wCZ6KCBdh_dAQDaxZ943vGUAc-CdnDmp_SKX3abC-S1sVAGqOqU7PleRjzl1F7A3UCNsrwq0LQxOoeJIDFp-X_S2zs3I7iUXz0Hyl-jQXnM5_ehqbVGjbeQNbaAXwfHZMPZoPmdh7J6Nl4lsF_V9rBUh5Zb7OnJzqNwkKFBFKWMeVGIvd_gi6PJq7wSReVnAwHQE2OrrLjJ1ZKu9cfwCiX_ryH1QCgAFzXofTtY-OxJzcmvI5hN1GcYXqnGaSqpeItCe3clszTJMGSoy5mYAXul6FwkjKb6kw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نفوذ هکرهای حنظله به زیرساخت ارتباطی ویسکانسین آمریکا
🔹
گروه هکری «حنظله» اعلام کرد در واکنش به اقدامات اخیر آمریکا در منطقه، زیرساخت اصلی شرکت اینترنتی
SupraNet Communications
در شهر مدیسن ایالت ویسکانسین را هدف حملهٔ سایبری قرار داده است.
🔹
بر اساس ادعای این گروه، این حمله موجب اختلال گسترده در خدمات اینترنتی شده و هزاران کسب‌وکار، شرکت، شبکه‌های دولتی و مراکز شهری با قطعی یا اختلال ارتباطی مواجه شده‌اند.
🔹
حنظله این عملیات را «پاسخی به اقدامات تحریک‌آمیز آمریکا» توصیف کرده و مدعی شده است که این حمله، آسیب‌پذیری زیرساخت‌های سایبری ایالات متحده را آشکار کرده است.
🔹
این گروه همچنین با تهدید به ادامهٔ عملیات‌های سایبری اعلام کرده است که حملهٔ اخیر «آغاز راه» بوده و در صورت تداوم سیاست‌های آمریکا، حملات گسترده‌تری علیه زیرساخت‌های این کشور انجام خواهد شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.53K · <a href="https://t.me/farsna/452487" target="_blank">📅 18:14 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452485">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f612840789.mp4?token=L0EGcE21DlQ1L99kBuBQ3rq3hSQ_TY6bre62Mlk48qdpN1ossm6EDWKYVg0JpXL3i1INjlqmCe9rpUON8BCGnom4uPJiuNd8750s0JdUpP_xIp0VZyIwKVLZZ-EPur30ASD_-oWFE3SvZLAUamR25k21I18ziovc_otTy7KVKhld8yEaRYKnnbXJLYXTT65Mol0CrlbYwlRq_dQH8qA_LRXnE3UyNhM-VaVtdOgc0zjTef9WQDlZhvNz5Fe9pHZ0qKfktMV-qCIHSWa-VsT9QDvCFcZqbG0IkDznE_w8GSQ_Mr8ffu3qARbalRipS8s5iCV0JzN8qlKFd0cPGk5iJA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f612840789.mp4?token=L0EGcE21DlQ1L99kBuBQ3rq3hSQ_TY6bre62Mlk48qdpN1ossm6EDWKYVg0JpXL3i1INjlqmCe9rpUON8BCGnom4uPJiuNd8750s0JdUpP_xIp0VZyIwKVLZZ-EPur30ASD_-oWFE3SvZLAUamR25k21I18ziovc_otTy7KVKhld8yEaRYKnnbXJLYXTT65Mol0CrlbYwlRq_dQH8qA_LRXnE3UyNhM-VaVtdOgc0zjTef9WQDlZhvNz5Fe9pHZ0qKfktMV-qCIHSWa-VsT9QDvCFcZqbG0IkDznE_w8GSQ_Mr8ffu3qARbalRipS8s5iCV0JzN8qlKFd0cPGk5iJA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
راز نام‌گذاری سیریک چیست؟
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.9K · <a href="https://t.me/farsna/452485" target="_blank">📅 18:02 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452484">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/19d35bbfb4.mp4?token=eVAQ1YouglfGbM4bdklcLp5x3pg2Y8HIBYIqNxwosFzjwVZohfoyHsEqcVAwuzCt0vNstHC8HN-4QgBfVhPMHnpX-QK67g89lBtkfiRdy4vr5iOirF9kpWD1RJYpJPn0HlqkVSIzc8W05XRw5Si0CsiqhW4agsRUombPwtgb3Yv4AvBp6csjFgDAdamyTHLaaLdjKTUb61vGso6DQ568kRQST0GmQmEkrVoBRi25_rGAXN0ykWZqIOn47A4invwBnviHRZNQEvGY_YDk1v6vq5VqejR0gFZEFLuoue2gm_O_jiHtiBf9N-X9_q_60X9EeoveQLafUFVVYXhIdAtRPA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/19d35bbfb4.mp4?token=eVAQ1YouglfGbM4bdklcLp5x3pg2Y8HIBYIqNxwosFzjwVZohfoyHsEqcVAwuzCt0vNstHC8HN-4QgBfVhPMHnpX-QK67g89lBtkfiRdy4vr5iOirF9kpWD1RJYpJPn0HlqkVSIzc8W05XRw5Si0CsiqhW4agsRUombPwtgb3Yv4AvBp6csjFgDAdamyTHLaaLdjKTUb61vGso6DQ568kRQST0GmQmEkrVoBRi25_rGAXN0ykWZqIOn47A4invwBnviHRZNQEvGY_YDk1v6vq5VqejR0gFZEFLuoue2gm_O_jiHtiBf9N-X9_q_60X9EeoveQLafUFVVYXhIdAtRPA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
زیرگذر میدان سپاه تهران افتتاح شد
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.91K · <a href="https://t.me/farsna/452484" target="_blank">📅 17:54 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452483">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">احتمال شنیده‌شدن صدای انفجار در زنجان
🔹
سپاه زنجان: احتمال شنیده‌شدن صدای انفجار کنترل‌شده در غرب زنجان، روز یکشنبه ۴ مرداد، از ساعت ۹ تا ۱۲ وجود دارد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.91K · <a href="https://t.me/farsna/452483" target="_blank">📅 17:47 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452482">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a2f5e69327.mp4?token=EwEPkyN1yIDNjiVfxfVVQT6zN86y1ZZTvu0timw3gkI6ZZ3IiUbIl0cWVuyZEdLTViLDYET8bzMleHp7LjWkoYSclfUMTAhEYvVew_Xzp1dJ050nqal276ndAczJIX-Jj7nt9a83JQu5TdPqV8Q7CGENj4hOqexAffRX_STdFQS2iCtLt5ba_7q-7RxI6QMbJtjzmkwbC2xA7VbevCUc7Od9mHOUuet2NOitNOoyrcDGokD-6CERBk7ZCVYgNVA8mf79tIP6N1qtseiSie4gt8iIgJkjbG87j-ifa28mihUM47wTvf8S7jkYqpV-VYRXgXQP2KWXdL6M84NM9rXkHQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a2f5e69327.mp4?token=EwEPkyN1yIDNjiVfxfVVQT6zN86y1ZZTvu0timw3gkI6ZZ3IiUbIl0cWVuyZEdLTViLDYET8bzMleHp7LjWkoYSclfUMTAhEYvVew_Xzp1dJ050nqal276ndAczJIX-Jj7nt9a83JQu5TdPqV8Q7CGENj4hOqexAffRX_STdFQS2iCtLt5ba_7q-7RxI6QMbJtjzmkwbC2xA7VbevCUc7Od9mHOUuet2NOitNOoyrcDGokD-6CERBk7ZCVYgNVA8mf79tIP6N1qtseiSie4gt8iIgJkjbG87j-ifa28mihUM47wTvf8S7jkYqpV-VYRXgXQP2KWXdL6M84NM9rXkHQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
اوج‌گیری تردد زائران امام حسین(ع) در مرز شلمچه
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.2K · <a href="https://t.me/farsna/452482" target="_blank">📅 17:44 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452481">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/568ec4ada3.mp4?token=h99jND6A-3T-u3LDCj-_WNn0rE9GbMfE94GXkeglXbSvhlbgRbZNos-lCXppyviZDV0nLcSXPMq390wFS9nCGD9gKebjsNygbTtZ-zwS1cz22grlIw8SHxVzjnirdYSCGSGBAH5UqfmxdnaMF-rLWKkdFjVuTnMnNF59SJ4np9ps0ruUzW4PQAoocxflppSAcrYZC8i1zfYQ9XseBU475kJHsMJM0UHO6DnX2J9rng5ViF78QI_7U4hIC-NE1RAqyHLammQyRZHwYamEs4s4HsMj4wJql-oSoimm_PcHQRtfrZr-8AT72dT-eWpE_iPu-YLfofz6rFVurmwIKIuY5w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/568ec4ada3.mp4?token=h99jND6A-3T-u3LDCj-_WNn0rE9GbMfE94GXkeglXbSvhlbgRbZNos-lCXppyviZDV0nLcSXPMq390wFS9nCGD9gKebjsNygbTtZ-zwS1cz22grlIw8SHxVzjnirdYSCGSGBAH5UqfmxdnaMF-rLWKkdFjVuTnMnNF59SJ4np9ps0ruUzW4PQAoocxflppSAcrYZC8i1zfYQ9XseBU475kJHsMJM0UHO6DnX2J9rng5ViF78QI_7U4hIC-NE1RAqyHLammQyRZHwYamEs4s4HsMj4wJql-oSoimm_PcHQRtfrZr-8AT72dT-eWpE_iPu-YLfofz6rFVurmwIKIuY5w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‌
🔴
سخنگوی نیروهای مسلح یمن: عملیات دوم، اهداف حساس متعلق به شرکت آرامکو در شهر ینبع را با چند موشک بالستیک و کروز و چند پهپاد هدف قرار داد.  @Farsna</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/farsna/452481" target="_blank">📅 17:31 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452480">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">‌  شعبه‌های ساعدی‌نیا همچنان پلمب هستند
🔹
دادگستری استان قم: هیچگونه مجوز بازگشایی و یا فعالیت مجدد برای شعب ساعدی‌نیا صادر نشده و شعبات این برند تجاری همچنان پلمب هستند؛ موضوع مصادرۀ اموال ساعدی‌نیا در دادگاه در حال رسیدگی جهت صدور حکم نهایی است.
🔸
از ساعتی…</div>
<div class="tg-footer">👁️ 8.58K · <a href="https://t.me/farsna/452480" target="_blank">📅 17:30 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452479">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kP0-vYV8Kk00Hn7qRMYPFqJWZ5jl0umI9P0Kkcg0hZRUW2lwXrnvjsP0uooEpKTvwFrpsAEabeUiUYTkgdD7YFBnQ0chbNFEgw12GAey0taeLnlPi3VhztZhyCo13DTkGJYzSImqiXnEjdcTftgWnQLJYi12KOt81H-vSRIq7fKIA_OpTA9jhQFfTCj6oM3JlNidu20SqhiAPVbDFtoC_pHf6OvQimRqMILg3hS5gtfiLUfuKLvOdfRxe4e9zYAItsLsEZMugtifeyVI06Q9g9PdwOLF3OZTAewKsRWv81pjVjji-leyWEq6cBj7zKACiQS_ambmPR21dOwRy58mPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پلیس خوزستان: مراقب کلاهبرداران اربعین باشید
🔹
فرماندهی انتظامی خوزستان: افراد سودجو با ارسال پیامک، لینک و صفحات جعلی و با وعده‌هایی مانند دریافت ارز اربعین بدون نوبت، ثبت‌نام فوری ارز زیارتی، در تلاش برای سرقت اطلاعات بانکی و هویتی زائران هستند؛ از کلیک روی لینک‌های ناشناس و مشکوک خودداری کنید.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.61K · <a href="https://t.me/farsna/452479" target="_blank">📅 17:27 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452474">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pJ0dw4yoB9Wh-gPNgequsSNrKSi5xBGSLYVWrKtlIe_SBTD6mJ7gr0rFrZBHbeVZjf0iCfUQ_GW2K_0puw_k-iqxYztVMfcOfFdSHwjKx334idpy7efrKN5TIqcMheqtugrp6y0U65uU3fjthgwHF6vVh2YHvB4E8jMeye2OcJoX6sZbGB5hfxWlIYfC6-28BJuqIDnuygw4TQcYBgrNDsVIdZkeGALsMHqIoLnntaiFnoDWpQbPaJKCdYLCgwUYsZqMA3LiIkAEUtxvWRpZyB52UsnA8el7ExTxQ1Np_XicbCJ_ksGMWwpYsx-GkvpkpvkTbulapRcNrPqUzSOEfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vLr6mGsL50P3XCeXcHxyuJHS1jCIlHApIwAA-ui0TaL5uqZNhAjPUHSXEXyzrxmE9WbNYrJPv2ZrsI5wldNbcV0by9iQ9_z63gOZ9d6S4oevt9LJo0BTwD4Uve6l-nci8o_MaMosxL9ajToVsrOf05krD_gnsSzWM0oWJEcWIGT5jj8UbIhmKtQ2GJneBwjxcSsap10rOXtKudlY0itkXnH51oqlp7WN6IL_7MZkiZyYbXcOgv2iXo-qxeQ4NS_AITlAsffKKlI3jYp9fH2toxj-m9xYtQT4hWAHN764O77W1_dTXMMyvoIdqnuxwG-3QZko4h7bOqaXzk57Se9TTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KLc5D63AqAxIw6WeKFR82xGbRcvni18x78f9PBcyC0DJFwc8YHnS1DQI50OxphBcJF-aIZJg-9WJs-QEnyZrHIE3LQM1XZ8Mgvf2AgZA9zTe0q4Cd0u9QbbHv1zZvgmzXR38qwEELaj4zU86hOvhGXBB6tSsDvgnNNHQgIoKjOLlE_lOGoxhG6KK2EBNWZRX64SsCQgoGdiUwUrxAIH89rQ9EtB5GiD2rWgshK1QpBK7aFD6n33tayzIJlNuhqJJ90v4Cq7SNFVEgwBzFKl2KXxbmwoI94D7Z7hjYLoziWau7hFXOplAhWWfvP_VHZCc36Fy9baIdVtkFk8J3Y-aAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WOMw7SyGwyg5LSnnlXUwMsJ4-_86vnjuY_d55SwPczvJ_qbyLXGpI7utUeV5XmYAX5pCl-gBNpE0m09DmBC0MCs1GNQX4kdI7-qB-iBUR8lxTRTo2vSC0lQkRiAcaDRaBzmsYVufVujmSRCXZdOX__P6JlZKmd8UJvMMLHc5CsNylZY-zrzkWQBRg5dYDJYfweehtohGAsUcwuRnkl9_He9BWn5xN2WfnQy9Y6BH-sJe34oOBI1jcTDWrxtTd8ufY5N7I2f5vukXAYuWz92AdvBBQ4sAa0-awBCFayZDER1ZVGZ3K9HireGxdYOc-s9S9wXRlLcbTpf4O93BTPQ3sA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YkZ-B4RoPL24K53KymVCVEBG0Mzchy_YzkoPval4FQsXFCDCpp78AR8dxqwWIZa6P3JU5C-rYe_VKILlUZCxyyM0XZtDtcNHyzIBroAO9Oml23Q0L7QVcnUr4n7ILNA1okPFWBcNoWDdSYV8Jszy3IjOVy4ndTLNjlgYgte8ZL01DLzHFAOiJhGa0YOV5IBv35pmV6gGfDNDGythRvZwFhesNkGwfxnAQ3ZrFftToSfyFM4uCNXJgWoZauyMzEIG83XqACMF6v4Rk0enoyRzaJX3F2hwOABubG_OiCfhLhBoDYvXwzw7kF2mi5vnHYZGFaA1D3Fca767P4uOgjJ76A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
برداشت گندم از دل مزارع لرستان
عکس:
نگار ده‌دهی
@Farsna</div>
<div class="tg-footer">👁️ 8.99K · <a href="https://t.me/farsna/452474" target="_blank">📅 17:13 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452473">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/31f50f57b7.mp4?token=XzoTlSMHltWD0D2X7EGkAhT4L_y4U35fR-Pcq4dH_oBcn8Ex6PHMg3vZ7I-JQR-rIP5H79GMnMhZZT0THS9MabhYKTpLYRHu3daQ7HKf7Ik483iASrx9H1cUMWvIL_nwbPrhJ_u_NoO25r63ZiPZmMT_BwOi_hcm6C_hys1ue0mg9ClgtP8ZRlpa8nHrIABA_BA7UMk7zrAs67py8HtSrBh39Rh0Z6gNyvtpHSqI9uKhdYu1RMbopzMX5F2-6iUuYHAMvbeMBANTqbrhzyDqgk5Ueufe3qgtk4liHCBcnPUDWI0GDTsVRB9KN5x1np9gSRw2ASNxnB-8JrUac2Kh8URcMGnnNCNTfREbynwBjTl46cR9du__DsE68w0ct_IQbQvBRl7jlllalXmTyADDyav5Nqe-amwFeJDb2uJ9Kzl43F6iBYqFjcSI2aC5lxz6gC8OXoJXPN5fvTNHpvrYGvEto5pbz0ZWYeUpeOAi-8r1Welc8_EimoekAzUm8_YpP3gWc-XpqYUTF1QPHLlS0jNmcu0Zc64IlcE4HfzN4xeRkoSep5DnR7nLaXDKssGAstlcvrfvWZUPgCRQ5WsOon8klaqXiNQFN6FdDmnXCLTdR1JfZeP5ZUBjaL-FTlfe2bPNtRmZg-k2R-drPafPZzw0WSsZCRt1zsfIISzArDQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/31f50f57b7.mp4?token=XzoTlSMHltWD0D2X7EGkAhT4L_y4U35fR-Pcq4dH_oBcn8Ex6PHMg3vZ7I-JQR-rIP5H79GMnMhZZT0THS9MabhYKTpLYRHu3daQ7HKf7Ik483iASrx9H1cUMWvIL_nwbPrhJ_u_NoO25r63ZiPZmMT_BwOi_hcm6C_hys1ue0mg9ClgtP8ZRlpa8nHrIABA_BA7UMk7zrAs67py8HtSrBh39Rh0Z6gNyvtpHSqI9uKhdYu1RMbopzMX5F2-6iUuYHAMvbeMBANTqbrhzyDqgk5Ueufe3qgtk4liHCBcnPUDWI0GDTsVRB9KN5x1np9gSRw2ASNxnB-8JrUac2Kh8URcMGnnNCNTfREbynwBjTl46cR9du__DsE68w0ct_IQbQvBRl7jlllalXmTyADDyav5Nqe-amwFeJDb2uJ9Kzl43F6iBYqFjcSI2aC5lxz6gC8OXoJXPN5fvTNHpvrYGvEto5pbz0ZWYeUpeOAi-8r1Welc8_EimoekAzUm8_YpP3gWc-XpqYUTF1QPHLlS0jNmcu0Zc64IlcE4HfzN4xeRkoSep5DnR7nLaXDKssGAstlcvrfvWZUPgCRQ5WsOon8klaqXiNQFN6FdDmnXCLTdR1JfZeP5ZUBjaL-FTlfe2bPNtRmZg-k2R-drPafPZzw0WSsZCRt1zsfIISzArDQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
وضعیت پارکینگ‌های مرز خسروی
🔸
مسیر ورودی شهر قصر شیرین تا محل استقرار پارکینگ‌ها در مرز خسروی در کمال آرامش و بدون ازدحام است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/farsna/452473" target="_blank">📅 16:50 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452472">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N0xZ8zfdUjUJYqdLvU9-L3g9WttWrZ3FXMDDAfgusy_eP0VUfVwkM0dBVn4xfeujB9Q6xHYqFNlql0KHwAoIX-giiAGYpijsKweJCz6CkJmuz-o3nr5L79yHaM-OzJ2-WtKHLk9jKb7wMeqnWsJGGhAWsvGDIvQjwf2TWo3awuAX08VkdEUQXwcUiLw-1sTSIp_y9IFznBxhwCoDpkrkFd6yiAJnHJUvZles-feLlajkbU3cPxpLsMIbJ4q-W2omrIVLSGVPugb07K03-ZphjPq1vUweRRudSTcUP67vpMRQz555bfMj4gj8gZ5fpbn0nn-mTCov3wMV8HXKoNMy7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بیمه‌‌ها عربستان را گردن نمی‌گیرند
🔹
هم‌زمان با تشدید تنش‌ها در دریای سرخ، شرکت‌های بزرگ بیمه‌ٔ دریایی مستقر در بازار لویدز لندن، از پذیرش درخواست‌های بیمهٔ‌ خطرات جنگی برای شناورهای مرتبط با عربستان سعودی خودداری کرده‌اند.
🔹
این تصمیم که به‌نقل از فایننشال‌تایمز اعلام شده، شامل کشتی‌هایی با هر پرچمی می‌شود که پیش‌تر در بنادر سعودی پهلو گرفته‌اند.
🔹
بر اساس ارزیابی بیمه‌گران، کشتی‌های سعودی در کنار ناوگان آمریکا، انگلیس و رژیم صهیونیستی در گروه پرریسک قرار گرفته‌اند و برخی شرکت‌های بیمه نیز در حال لغو قراردادهای بیمه‌ای موجود هستند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/farsna/452472" target="_blank">📅 16:25 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452471">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">🔴
منابع عربی از حمله به پایگاه آمریکا در نزدیکی فرودگاه اربیل خبر می‌‌دهند.
@Farsna</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/farsna/452471" target="_blank">📅 16:12 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452470">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/019e07e598.mp4?token=UL5Enu1zxlghtAlcJjQZkV9eo0lTzXpzqfJWrGsl7rvHQooyH-tvDzCAF6FuZMdAFx7YgGS4R7im-PQQRtWnFlXcmLqWdBY2kWnwjCuFsAiryozXf0Wht1JTcVQGRXuhwW5XZZVrJ5aUjUXJZjtNerjUshEIsembFRsL2ZET_-jqKT9EbymiRLsW18ubq2a9AnU6b1Cfw9PY4BboNxRRudBDDL6mu5l6gPOBWXpWd7eBKtLYr9HeFniOMZItKxFrnlLIe0fCpjaqFbbmAtwLGjFG4KsY67vYMWdYhNoEtiuxErHqMgvP8DsMsqJ2MAREdzvgaELQ0w1tOlcdOIr-w1X7SmZZ1vCae0CsTktz3hKkS76AEu73mLTzv6aaR_Ir_nj_SRlz4KYAyGX53umgi5JK8SVtkUI9mkY-JeGJyG10FDHschzEoJk8iUhA-GrqRXiU81uxqON_Z-fJ2c8cfgM6EDl17dZldsFlDY9KE1Ccbm_YU_eICkdJ550l5mlCVWSUIwAexPAsmQ2D9nCphnIHAVze0V6HwRjPEOEagwIDyZM-a_tsTJGlZYGWPVEFQWmyGa0NfLb-JAaf5XcpoLiFkFH_XzqaNZJGpIog02RqHN7tambNbLl_-kPsRQ9y_8MmrPFIpUVnbxbpUsSm49maJ8uzZF4GhU7_-ucJTQ0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/019e07e598.mp4?token=UL5Enu1zxlghtAlcJjQZkV9eo0lTzXpzqfJWrGsl7rvHQooyH-tvDzCAF6FuZMdAFx7YgGS4R7im-PQQRtWnFlXcmLqWdBY2kWnwjCuFsAiryozXf0Wht1JTcVQGRXuhwW5XZZVrJ5aUjUXJZjtNerjUshEIsembFRsL2ZET_-jqKT9EbymiRLsW18ubq2a9AnU6b1Cfw9PY4BboNxRRudBDDL6mu5l6gPOBWXpWd7eBKtLYr9HeFniOMZItKxFrnlLIe0fCpjaqFbbmAtwLGjFG4KsY67vYMWdYhNoEtiuxErHqMgvP8DsMsqJ2MAREdzvgaELQ0w1tOlcdOIr-w1X7SmZZ1vCae0CsTktz3hKkS76AEu73mLTzv6aaR_Ir_nj_SRlz4KYAyGX53umgi5JK8SVtkUI9mkY-JeGJyG10FDHschzEoJk8iUhA-GrqRXiU81uxqON_Z-fJ2c8cfgM6EDl17dZldsFlDY9KE1Ccbm_YU_eICkdJ550l5mlCVWSUIwAexPAsmQ2D9nCphnIHAVze0V6HwRjPEOEagwIDyZM-a_tsTJGlZYGWPVEFQWmyGa0NfLb-JAaf5XcpoLiFkFH_XzqaNZJGpIog02RqHN7tambNbLl_-kPsRQ9y_8MmrPFIpUVnbxbpUsSm49maJ8uzZF4GhU7_-ucJTQ0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حال‌وهوای مرز خسروی کاملا اربعینی شد
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/farsna/452470" target="_blank">📅 16:09 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452469">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t82HvPAsbzxXlJaaLTwicgx8hBT0gB-o0-fhhsQ-fvWDb_3q8idkO9ysq4pr-Pzx2-WSYhTP47D5N5quUh3aY4iLaWVluQWGu_MiFJzkbdi6D1zaj--aWy1SpbkX9bdF5EY0FSCFFR365DMmMuZ3WxoP-PS_QyuH8jpBoee6hpQfDXrqTcQZuVBwCip6kGopGhYh-Qn9cFAsg8lVX3KlUBB7-v_DCAS1fsRN1njbHDyB0E7PIly8idDdRp76uZefy_q4tCvg2icx57nrW8IGPACdIcbnvM3FwzpVEgs1CFed7vNmdqrBaV14jsN814Lok9PJIFtIjd2yN_YFvwDcxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آمریکا با چینی‌ها هم به چین نرسید
🔹
در المپیاد جهانی ریاضی که به میزبانی شانگهای برگزار شد، چین عنوان قهرمانی را کسب کرد و آمریکا در جایگاه دوم ایستاد.
🔹
نکتۀ قابل‌توجه این رقابت، حضور ۴ دانش‌آموز چینی‌تبار در ترکیب ۶ نفرۀ تیم آمریکا بود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/farsna/452469" target="_blank">📅 15:57 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452468">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nqmr0KpVXFuxsnnh4LhWDPoSrV7upnRv4VZ2ywoO3AnOT4MUie2M-DVR6CXCVblfJjKY2I5ou-WPounMOsn2fFb3zZSa1i9AcIwZdSi0_ZwaL2O8EcdqA6N-z4WqxRdqKj1HHrsiJtaIhq8-AMzPCHg2hRfTtg9SOr_QdT4iKw9frQPR3u-SkUxtrRy4498GiEftSocifWh1EwITGWVHPYGWKh3tNX2D6QDC3SL2U1g-08_yrebngYh_HphLpmOqr1b0pu5gqeIJW03J7Q9bjn6LKTax2qo2_-RrqLCvSaAEHRfmUy0LSjJ72LJLvPX7g8S-rBrDuF2BQ6Qo_y14Uw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پایان همکاری پرسپولیس با اوسمار
🔹
طبق اعلام باشگاه پرسپولیس، با پایان رقابت‌های این فصل فوتبال، همکاری با اوسمار ویرا سرمربی برزیلی به پایان رسید. @Farsna</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/farsna/452468" target="_blank">📅 15:51 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452467">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">‌
🔴
سخنگوی نیروهای مسلح یمن: تشدید در تجاوزات، نشان‌دهندهٔ اصرار دشمن سعودی بر ادامهٔ محاصره مردم ما و نقض حاکمیت کشورمان است که این امر قابل‌قبول نیست و مردم آزاد، مؤمن و مجاهد ما با قاطعیت و تمام قدرت با آن مقابله خواهند کرد.  @Farsna</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/farsna/452467" target="_blank">📅 15:37 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452466">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">‌
🔴
سخنگوی نیروهای مسلح یمن: به لطف پروردگار، این ۲ عملیات با موفقیت اهداف خود را محقق کرد و اصابت‌ها دقیق و مستقیم بود.  @Farsna</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/farsna/452466" target="_blank">📅 15:35 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452465">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">‌
🔴
سخنگوی نیروهای مسلح یمن: عملیات دوم، اهداف حساس متعلق به شرکت آرامکو در شهر ینبع را با چند موشک بالستیک و کروز و چند پهپاد هدف قرار داد.  @Farsna</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/farsna/452465" target="_blank">📅 15:35 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452464">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">‌
🔴
سخنگوی نیروهای مسلح یمن: عملیات اول، اهداف حساسی از تأسیسات متعلق به شرکت آرامکو در جیزان را با ده‌ها موشک بالستیک و پهپاد هدف قرار داد.  @Farsna</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/farsna/452464" target="_blank">📅 15:34 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452463">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">‌
🔴
سخنگوی نیروهای مسلح یمن: دیشب ۲ عملیات نظامی مهم علیه تأسیسات آرامکو در جیزان و ینبع انجام دادیم
🔹
این اقدام در پاسخ به تجاوزات سعودی علیه شهر و بندر حدیده و جزیره کمران و همچنین ادامهٔ محاصره مردم یمن و نقض حاکمیت یمن صورت گرفته است. @Farsna</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/farsna/452463" target="_blank">📅 15:33 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452462">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">‌
🔴
سخنگوی نیروهای مسلح یمن: پدافند هوایی با یک گروه از هواپیماهای دشمن که وارد حریم هوایی شده بودند، درگیر شد و از انجام جنایات بیشتر علیه این ملت بزرگ جلوگیری کرد.  @Farsna</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/farsna/452462" target="_blank">📅 15:32 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452461">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">‌
🔴
نیروهای مسلح یمن: عصر امروز در بیانیه‌ای جزئیات عملیات نظامی گسترده و مهم را اعلام خواهم کرد.  @Farsna</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/farsna/452461" target="_blank">📅 15:31 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452460">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Uix64kNHalk_aYCehBjOjHZhxVDsQrj8TYd-oAP6D9Sn_Eq-3kBFyo18cTxIDMDm-yV1MzkbRebLcrOTNOfpB0OIbakdVk0fKsOGIWGbtQRS860VpGtktb9vLOLaBsfedghImu00IdE2TW90D9ZTYqrvGSAVx40nQUj384QflP67tIoRySBP5i2iO6BXPw9D20dCuN0clycxKFJKDV1uTrVHx_2R-RouMwimDL83Z8SlchBkAQLE3octn8lZLgJM3Cs3ROZo2duDq5zJe76xLSkfqWbzhdGjbkq-njSVeZBRBb11AaSu1BN37tcCC8GU0VEkR4n7k2DKBRvX8ESarQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کنترل جاده‌های اربعینی کرمانشاه با پهپاد
🔹
پلیس‌راه کرمانشاه: امسال ۲ پهپاد به‌صورت مستمر گردنه‌ها، نقاط پرتردد و محل‌های احتمالی ایجاد گره‌های ترافیکی را رصد می‌کنند و اطلاعات لحظه‌ای را برای تصمیم‌گیری سریع به مرکز فرماندهی ارسال خواهند کرد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/farsna/452460" target="_blank">📅 15:21 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452458">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8d560d16c5.mp4?token=FWOGHa_ZKh0rKxsJCYZn7grfIQbtRqIFe_V7SgkJvOBp-c5878Brhcuyv6h6Sq2E0Mgmpl3NALNyBFsfJpwOnTN2ngyTa8bJmiIFCJJA7t2VmYE01D3enjF_LUqbLLJ3cNdBrBCH4_Q8I9sZTvcxcBtGt_TBpTPtVJuE08EqUULOGDFU8_9aMi9JKL0VbixA9LyjmKYGmDW3yw7f6tIDIPHMwq8Aum52IPPs5TBgxIRbz7PmYM3R7RLTQfAvqmyagMRdzAsUHPE2rCbeu4NQ9xHeTVmyra91SRvDzZ9MI24x6jjuDoCXTAvJyhl3Yr0h8m4u_f9i5PJf009h_x_M9g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8d560d16c5.mp4?token=FWOGHa_ZKh0rKxsJCYZn7grfIQbtRqIFe_V7SgkJvOBp-c5878Brhcuyv6h6Sq2E0Mgmpl3NALNyBFsfJpwOnTN2ngyTa8bJmiIFCJJA7t2VmYE01D3enjF_LUqbLLJ3cNdBrBCH4_Q8I9sZTvcxcBtGt_TBpTPtVJuE08EqUULOGDFU8_9aMi9JKL0VbixA9LyjmKYGmDW3yw7f6tIDIPHMwq8Aum52IPPs5TBgxIRbz7PmYM3R7RLTQfAvqmyagMRdzAsUHPE2rCbeu4NQ9xHeTVmyra91SRvDzZ9MI24x6jjuDoCXTAvJyhl3Yr0h8m4u_f9i5PJf009h_x_M9g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
۳۵ کشته در تصادف دو اتوبوس در سوریه
🔹
بر اثر برخورد دو اتوبوس مسافربری در یک بزرگراه در مرکز سوریه، دست‌کم ۳۵ نفر کشته و بسیاری دیگر زخمی شدند.
🔹
به گزارش خبرگزاری دولتی سوریه (سانا)، چند بالگرد به محل حادثه اعزام شده‌اند تا مصدومان را برای مداوا به بیمارستان نظامی حمص منتقل کنند.
@FarsNewsInt
-
Link</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/farsna/452458" target="_blank">📅 15:15 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452457">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7a8a8ccc7e.mp4?token=G2kQiYH8KwkwXiBRo9ghyxDFL1Gi78OOklKk6taDL5ZPq7FP0LziH0KKw0xGMtT-ddMQg5oSQPhYi6cvguuBSxl4pTPAZloXgZBXtGN8VFMywRTs4tO4bM3ugcs2EKoHdVVdV64cWjF0O3fpsuwiWg2zZ-gmlhCOs1RYd2KgfSPTARRYQBbwRrOjXCYgSRgyVi05rLF8pmgaXxLySHsaQ8_iK99SZJhzK_lrYC--QhllVOAy2HZDAfsAg2AXGULoe4zQA8KjPu4bYqazZ6Jyw0ex9pvLih4HtUmG3rzD0k5vE429l4HhYpJlMkkN0IFDaGlhw49_WH9TRrcZ2MnfdC2DngLjua12X_-s06ox0iBDDgzTzHsQWHiVqo9z5w48cYpMuKbbb2A6XBzL9CK4d-7SWoYADJzSiuFitavGjrgRRWUtIcDyypRF1EZITvY-mNJMVqo9F4XBBS_D5QfK9hlzMOTMZs3QuJhujxkYfQq2AcoJG8EEQEwBWY7L_TLEBVYYUmoHVYdsE9MZeyDKeYxkGGwu6CpVt5vx57U2EKCnoj4qnVf2pG5s2AnbhMAf-24zA0O13sIsNWN2SpKo_hITrt9ErxeYNGuXNxpBJE-LKg-hjU-h0iCQoMQnGPXJEoG2KdCaUR2SRVqqi1WiFPPEFffio28cxg7RZvU9Z_0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7a8a8ccc7e.mp4?token=G2kQiYH8KwkwXiBRo9ghyxDFL1Gi78OOklKk6taDL5ZPq7FP0LziH0KKw0xGMtT-ddMQg5oSQPhYi6cvguuBSxl4pTPAZloXgZBXtGN8VFMywRTs4tO4bM3ugcs2EKoHdVVdV64cWjF0O3fpsuwiWg2zZ-gmlhCOs1RYd2KgfSPTARRYQBbwRrOjXCYgSRgyVi05rLF8pmgaXxLySHsaQ8_iK99SZJhzK_lrYC--QhllVOAy2HZDAfsAg2AXGULoe4zQA8KjPu4bYqazZ6Jyw0ex9pvLih4HtUmG3rzD0k5vE429l4HhYpJlMkkN0IFDaGlhw49_WH9TRrcZ2MnfdC2DngLjua12X_-s06ox0iBDDgzTzHsQWHiVqo9z5w48cYpMuKbbb2A6XBzL9CK4d-7SWoYADJzSiuFitavGjrgRRWUtIcDyypRF1EZITvY-mNJMVqo9F4XBBS_D5QfK9hlzMOTMZs3QuJhujxkYfQq2AcoJG8EEQEwBWY7L_TLEBVYYUmoHVYdsE9MZeyDKeYxkGGwu6CpVt5vx57U2EKCnoj4qnVf2pG5s2AnbhMAf-24zA0O13sIsNWN2SpKo_hITrt9ErxeYNGuXNxpBJE-LKg-hjU-h0iCQoMQnGPXJEoG2KdCaUR2SRVqqi1WiFPPEFffio28cxg7RZvU9Z_0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
یاد رهبر شهید در مسیر اربعین
@Farsna</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/farsna/452457" target="_blank">📅 15:07 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452456">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8c09242037.mp4?token=hqwtYrNvijjHdevhr-9o7poM5_79EtVIo4G8GDJZqjnEIlooTU_dthQbzfK0gdNLIdnm51d0TejgdIMNKoIhKwLNc0cXULzdEfgZIAVj3oMfh7TnfHunpxTf0vu__675OMBrdOvX2nYgDxL7aJhYBNZOEhbXrnuNt_Ha7DZK4lTwf8879ctNN5tuHlAxfrXqqlGdzn58zAMNN4sFHKPA8oP__BysbEiic_A_6pOL0BQkq9pl6trVCOoP2kV69p9GiEPLiauKNu_leteVd70hOd79HhWujOEA1cN7VJYABPcPdZewqVdl7VuPKCwYULYcsLvlRdwUMz9sLM39cbRQnQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8c09242037.mp4?token=hqwtYrNvijjHdevhr-9o7poM5_79EtVIo4G8GDJZqjnEIlooTU_dthQbzfK0gdNLIdnm51d0TejgdIMNKoIhKwLNc0cXULzdEfgZIAVj3oMfh7TnfHunpxTf0vu__675OMBrdOvX2nYgDxL7aJhYBNZOEhbXrnuNt_Ha7DZK4lTwf8879ctNN5tuHlAxfrXqqlGdzn58zAMNN4sFHKPA8oP__BysbEiic_A_6pOL0BQkq9pl6trVCOoP2kV69p9GiEPLiauKNu_leteVd70hOd79HhWujOEA1cN7VJYABPcPdZewqVdl7VuPKCwYULYcsLvlRdwUMz9sLM39cbRQnQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ایستایی زائران در مرز مهران به ۵ ثانیه رسیده است.
@Farsna</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/farsna/452456" target="_blank">📅 14:57 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452449">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Xxl4aSFNTcg9fXi-mV5g2GYpO7F3YM5QmUpyCRj1tFf0VvFiR2UN45nSFZQ_21qzeNxCtknrRW9wkszcWoBJEpqt5_tQ-RIiryktuourK_j0_8CMRC_OOD5l2MwKX8JmEQ_G-bLdyOv01Sir2c0jHwSHxrKTd3PbyzRRj8LcXHCDhxe6QOktOJWc4XT8ksuVyVZxFo4bSyuF-xwO2XZBqE7pZ3rnbNtIG63YwtcMJQrxfs92DpJgK-BCXcFu56LWG46yEGXQMJM48vamNSy2mlbH5p2zA9dSonQDeMe_q9JWbTsyNshVV79mV2Fn4Q_iYeOeKOb8CHAhynBXNd-mpw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SqG22Lr-bvyMMOM8KpHy-9clqr7w0BggBLeUl1jxAobtQ03EnjTlcjAT0K4NnYkvQENsbW9o4gxWIHq68C93jNEV0rWphwtB_BLdMkVAoDKizhiFSjLApqCxiKIfcqvRe90DGChjdgesZgcx3Jsm14oH5WMVF1-idDbyqcKipUXotVyPHMSTAR_XZ2i4qbGVY9WsQIa7U-_kfGERU-VjxZTNJaJRd86mDdyPxP4Nx84bytuq--OO62GRe9olGrezRb5dFjAJiSHXeUFAHnLMuHEgOtc9cxeZXG5I5hS3LRUAjTPvRAhCZX_09L7IR9zzXzCxwMTUYksWafG2jH7E6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nws68adCyourqgYvKgW8E-waSIHp2PYR9Aclf7BrKKnXO5iaqgq26FehdOOaxCQLEtd7xWWhpNrP4PuYPf5okHnQOhrcAVrt6ipLSdZ-gGgoEBJhgWC-_1kYnqO9_9cYkcyHTnY8j7GL9FgoLsFe5k5ympccuPU6goSdgyH2k6lZ5_UfUHXZUi8rXOutIqu6TybUJu_sisCvpv4W0qNVTmVDYj2jfkKfCajhGzqPHCNuVOM-I1eF3OnLtVdDf2aUxcrcFubE85PxbxWlItQwz94SfLhAh3Y7ZlVis2jpWpASXNgTWj9YWO_6dQrws5GFXJ7LWldov90-tSRekqXYGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RcO9XLEfkjR8OKyB_44IMU0TYqeAZoQJX0PjLQuHFGxcbN7oCmR8Fu_1JB8N41bzS4CN70mD8Wt0cx45fMCQA9vR7DT4CeMzMQenTIzB0gPzcDVMGRwmYA96uFUuCepAJBL8llSE3j-00EQ6eEGTOD3QG3sFxS-E21vNFXC4gs0adf24xcDT-_1pjObvo9XqZ4EhTJ8jz4QRYDIPcfdiDYZhByJweinScas_Wjj-LVyBMuAzV0Gq-dtR4_YVgSJGp8Ih9UfAfJnLP7wWSXPGqc5W6PEK6Vu7C7jOoKW5wBV_YTifn2KgUY6OYDw5jhSMiS6h2og44qRcMAU09GaqpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/P0lQ3CTgyI18VNOIsVtEHbfHeblUvRkPeNT5RWtBJsh_fTyXCsvAEfid2YousQIU8GFgR9A87JATqd69xRQBx3LMrVlCr5FfnxKm-mwkNYIkQ6hiF7TSzKRdI-E5BrI4sM0cgNVxZ4OAK86sLfRekxDDA1qUREdXj2IlF-el5CsA2PozC7FXE-wTXqT2nXXwOnw1FOz2VBqBMB4vHuJQsKsghLAkykPILZthHb41pKE18dwEGgqRjhtmqB5Yx4Vs58LIoE-UXl793pIXDSYaZa8G5aJfKpOGI9yw-BDX80lmOUvNRWBjFf1Tqws54ZmRxD4ny7g5XBIG4tS_SnqELg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JrvrJPrKfOQhMjE8sCweHep-AtXYcpnCt92g2yVfcvnUM40LFaVwIeNrEPium6W_e2IG2k1epL_KhuvUj-BIcsj4y_AeOzAHMiZeVGUMBc-Cj_90dLJSB0rNiR7h-KNt8z_ckIXtmTptDWEFIFIlpsmWSb-cyrywrJokCCA8KwvBiwMKi33R57H_WiIWhEbN-3AjkDnMVU6Zq8FyNrcNBl0QAFwBKSEz4paxmvU4i8XJ2u5QVm71jmCOXpGai0bJnX-kCG9UTzf--A3FlftZJLugKzInKzQ25A7tYi73iwjK2A3Oi8DicMphI-EKqYF_XD0olpAUrvfQ38Bax2iDSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Qpvb1TNntc4Jmpq_TP_BoJlouAcwwYIRIwgSn7OaFGARw94x87RnIEe8KGySI1Hthffz4NJJi1j3-HO4TtYuDKlRu9kO1QcyMKrvS9anh0fi2BdbqPsjT49B52duuOm0ltrX2OpnYxumSRA1tD8K3t4nHLSGvqKPK4qGTO_zelqJ3ji_SKKW90sKcbTZWlKIGmy3GoDuahk80JnPUCmoi62LI1y-TFEwhY8BDyvhWCSsNgwCT0MfwnoKJxF3M1pCIg1pLgfstXwPmUJFMhvRn6kbY5j7MXahzN1yJ6av6fY4drZMJEAUGM7Vomk-H7uYKXIjnkam-mYXY2he6_bIOQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
تردد زائران حسینی از مرز خسروی
عکس:
بهروز احمدی
@Farsna</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/farsna/452449" target="_blank">📅 14:45 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452448">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/502d70608d.mp4?token=WtFLuUcWSso01RZVXkuu_Fq8ssNMeoJ1QCR4qSQV-tJ36nS-dWec5t7ZhQAJ_b9SvjFPrZk7zUMnQTxsPel6-toeqDmRT2Sv63_MQSREuQjei5gb7OZDX2TeoUTdPhVx2YpCKY0dLZjfYe6Xcu9cSbNFWskDmsar90RjPt-EtCyia8j9rm-iWYyNr5pXAAvTZ0MNjSlITtUuWes0dh6h7NZBLcfe3CmifpZZHNcjVDNuX1Ev9gczBQDj3uF-ptGJr0Tw2bPyVInyjidWzTj5i1nKHRWbGElCUO_ajoyM4XMXhbNkeMdMwcUYENr6dCZvElqo45GuLCHwegq0ifM-zQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/502d70608d.mp4?token=WtFLuUcWSso01RZVXkuu_Fq8ssNMeoJ1QCR4qSQV-tJ36nS-dWec5t7ZhQAJ_b9SvjFPrZk7zUMnQTxsPel6-toeqDmRT2Sv63_MQSREuQjei5gb7OZDX2TeoUTdPhVx2YpCKY0dLZjfYe6Xcu9cSbNFWskDmsar90RjPt-EtCyia8j9rm-iWYyNr5pXAAvTZ0MNjSlITtUuWes0dh6h7NZBLcfe3CmifpZZHNcjVDNuX1Ev9gczBQDj3uF-ptGJr0Tw2bPyVInyjidWzTj5i1nKHRWbGElCUO_ajoyM4XMXhbNkeMdMwcUYENr6dCZvElqo45GuLCHwegq0ifM-zQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
امیرعلی جداوی، دومین جاویدالاثر مدرسهٔ میناب
🔸
علت اینکه تا به الان اسمی از این شهید منتشر نشده بود، درخواست پدر او برای باخبرنشدن مادر باردارش بود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/farsna/452448" target="_blank">📅 14:26 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452447">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b4c910168c.mp4?token=btvC-Z5-uUco74mZhoXzCim9LL-DVtMZh4CkWnHLwNw_1r-_HZGDbvS79bV0QI3gIYuVdRWGmkGvSdkje82ArVi0QN91jujTjpOyQzitx3p1xTeRuM5hwoO4EZPzS4ddfQxwdAqAQm6merZTj7ED3tgtzO3zDtMeBTehFpJI3n0LxgxNnjUCT2XD37vxTh-_zg-HDSzR0P1yKGBSU211ppo3a2dP8lL2Avm6IcW2PQUCzaSDwlKUqGcogUNFWGTDnkdOyL3QtHQI4ZbkwZkjL1O9ufy1_Pk-lUt9zVw-wiWYSF05Wqs8X7VfplPTYkH0Eea4j_rjpLsYJ164Z0Dy4A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b4c910168c.mp4?token=btvC-Z5-uUco74mZhoXzCim9LL-DVtMZh4CkWnHLwNw_1r-_HZGDbvS79bV0QI3gIYuVdRWGmkGvSdkje82ArVi0QN91jujTjpOyQzitx3p1xTeRuM5hwoO4EZPzS4ddfQxwdAqAQm6merZTj7ED3tgtzO3zDtMeBTehFpJI3n0LxgxNnjUCT2XD37vxTh-_zg-HDSzR0P1yKGBSU211ppo3a2dP8lL2Avm6IcW2PQUCzaSDwlKUqGcogUNFWGTDnkdOyL3QtHQI4ZbkwZkjL1O9ufy1_Pk-lUt9zVw-wiWYSF05Wqs8X7VfplPTYkH0Eea4j_rjpLsYJ164Z0Dy4A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مردم بندر جاسک اسلحه‌به‌دست منتظر آمدن نیروهای آمریکایی هستند
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/farsna/452447" target="_blank">📅 14:21 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452446">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UmJmldPnBcwx2aqohJMoPC9Xs_CC-_jqoEGwtWoVrmKKkDPp59jP9YcNjHFCcWm0cDuLY-uCTanNRy40V9lQAbYyZzqM_jBpL-3qplqXzsz3gW3TEN-STjuWfQ79aBiL8r17v_g_0c6bI6-MQqWHcIseeh-PJERo8PWaEl_xzgnK1jg91ZDBBraUYss-wXKi7hdGgmmQ2GrP-05LSCoT_ObxtCGfuscx5h2YTN6Mlg5jg7hjbLUMUinBUzDLQ_zro9Q12SX07ZuJ7Lk2-Itj_zyyWwH7sm1X7L9uqgbMP-3CgtrG0sr8PVEd5Ep472g1_o2cLpIDKZxzup6I-QMOiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">زلنسکی: به کشتی‌های انتقال تسلیحات از ایران به روسیه حمله کردیم
🔹
رئیس‌جمهور اوکراین در گزارش عملیات‌های جدید علیه روسیه مدعی شد: در حملات دوربرد به دریای کاسپین، کشتی‌هایی که در حمل‌ونقل محموله‌های نظامی از ایران استفاده می‌شدند و یک کشتی جنگی، هدف قرار گرفت.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/farsna/452446" target="_blank">📅 14:14 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452445">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bhUweGw4_aJU3JBMTScO2RUbs_7pdDVi90q-sdId6jPmkQy1XRuYzpyDCsU51MslHQrdZgdZe0mhgOit6j2cFjcLMwcSYgZos4z9cld_MMuUKtkRGWGU7ISSnL1YRKYDMNhSEO0MclIp_LYwiFz7aqCmFKKhlIKrbP5-pOt9k1QGHwgkFt8fBIr_JvcaBFPhYwCJl3yVmgBnLm8GhkkG6nDaJI9Przx8AE563JyjgzrIYPBl9kzP7FbkM9uaQZP-qTD8kST8xeslb-5_SEwWLAZGzTFvhupMLYcczQ7L1LLIv5LIma5Gcvv9MlinqYmlXILgTWXhzckvs8zvGLYPzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
بذرپاش: جغرافیای مقاومت زبان حسابداری خودش را دارد
‏کاری که حماقت ترامپ با تجارت جهانی کرد:
🔹
افزایش مسیر ینبع–تایوان: از ۱۹ به ۴۸ روز
🔹
افزایش سوخت هر کشتی: ۱.۶۱ میلیون دلار
🔹
عوارض سوئز: یک میلیون دلار
🔹
جمع مازاد هزینهٔ هر سفر: دست‌کم ۲.۶۱ میلیون دلار (بدون حساب افزایش بیمه و کرایهٔ نفتکش و...)
@Farsna</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/farsna/452445" target="_blank">📅 14:08 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452444">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">حملۀ هوایی عربستان سعودی به یمن
🔹
شبکۀ العربیه از حملۀ هوایی عربستان به استان‌های مأرب و الجوف یمن خبر داد.
@Farsna</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/farsna/452444" target="_blank">📅 14:02 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452443">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AtHdASrU1aR3mitYTaHTdeLmLeJyDZpROpIw7v6Rv9-B_ayAUb_p5eXUHVG_dewu9lYZB5fuSheT21rW7hZEXIWmQi5TthLMH3hWpbSbjnQ7ofAEkPMOcSjMo1d-GnAeii0w_pmNvLhmV48wDv6J4JQjJplAGT2yjE2GIMmySeNZiuzcmJaDzJKtDdZJ0lP5QJLTHYoOs3YH3G8a2ukaWwycGJw5m-FuVTr9xPLGE7fsXG1VPopEnARN77qgOv4Oa4WQ0Wl83v3rzZ5ai9ifwEWa2Kz8DR24gaLsqxNuMnpayq4pNT96Uvn1-nknAj5Vulinktjxo0q3uV2coSdzxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ در فکر دور زدن قانون اساسی آمریکا
🔹
درحالی‌که در آمریکا هر فرد فقط ۲ مرتبه می‌تواند رئیس‌جمهور شود اما دوستان ترامپ در واشنگتن نقشۀ جدیدی برای ریاست جمهوری ۳ بارۀ او در سال ۲۰۲۸ در سر دارند، طرحی که در واقع گول زدن مردم و دور زدن قانون آمریکاست.
🔹
«ان‌بی‌سی»…</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/farsna/452443" target="_blank">📅 14:00 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452442">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/90c4603615.mp4?token=A9igX2CxeXEGG1nMPjLzprBHiXOy2nYyF_mwZMYyenIpU46AclyaYYESnrvRHVqJScyIqQn2tU6UXiwSVc0DMOg1_BPyF1O_nwxHDOLuZdiRlsLgyWECuQsuLDJQPK6Hn4nF2Rvjj_yzraXiL6gpH5ySIq6ETfJF2I6tNPYOBW0MWlJy44XfBx8krQcmsFHea6gOEavW22eppeeZWxBLkHDzvBeCenryW9ui1XP1bLFEEUgXHHRZ_QD_hWP66WDJOxP8X3F_eRa7wLD7kresY8_zlWCSO0m-ezSS8qWpg9boCgNt_FPk6RGvqmsoOMiAx_TfzMtynyrw6XwEi8KZg1C8OQpI0JEq0T3KnfQeq_RljrLXZzAE65ol_DYl62ZNH3--Qy43mZqrF8yKlbMgqgN77RK0cU5vAgMS4H2YEKMenk-DgBGNeBGjSYb8Kerlz7_Q-uk5xf6n2eba3DU1Obkd79ZqVU2-D3j_ClzRHiTLnI6gFkiVKvgdPRW0_acJDT7zK-HsSWW6Dc5NmmIHvQJWjFW3pqSxTIMwoIPWnFvZuP1T4aQpqdl9qzG-NhnSjyv4cwsLTPfUs_fgqGdPL1eser59q86coF7z5WZeYvlChw3AndsXlbAZ8hQ1EZUzrts4DjQrLQNOkAzrm_fVrFz9mQgkj7VeUT_Sj5OBdhw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/90c4603615.mp4?token=A9igX2CxeXEGG1nMPjLzprBHiXOy2nYyF_mwZMYyenIpU46AclyaYYESnrvRHVqJScyIqQn2tU6UXiwSVc0DMOg1_BPyF1O_nwxHDOLuZdiRlsLgyWECuQsuLDJQPK6Hn4nF2Rvjj_yzraXiL6gpH5ySIq6ETfJF2I6tNPYOBW0MWlJy44XfBx8krQcmsFHea6gOEavW22eppeeZWxBLkHDzvBeCenryW9ui1XP1bLFEEUgXHHRZ_QD_hWP66WDJOxP8X3F_eRa7wLD7kresY8_zlWCSO0m-ezSS8qWpg9boCgNt_FPk6RGvqmsoOMiAx_TfzMtynyrw6XwEi8KZg1C8OQpI0JEq0T3KnfQeq_RljrLXZzAE65ol_DYl62ZNH3--Qy43mZqrF8yKlbMgqgN77RK0cU5vAgMS4H2YEKMenk-DgBGNeBGjSYb8Kerlz7_Q-uk5xf6n2eba3DU1Obkd79ZqVU2-D3j_ClzRHiTLnI6gFkiVKvgdPRW0_acJDT7zK-HsSWW6Dc5NmmIHvQJWjFW3pqSxTIMwoIPWnFvZuP1T4aQpqdl9qzG-NhnSjyv4cwsLTPfUs_fgqGdPL1eser59q86coF7z5WZeYvlChw3AndsXlbAZ8hQ1EZUzrts4DjQrLQNOkAzrm_fVrFz9mQgkj7VeUT_Sj5OBdhw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تردد روان زائران اربعین در مرز شلمچه  @Farsna - Link</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/farsna/452442" target="_blank">📅 13:53 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452441">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/af7pgKMVsCsmekK5vALuR65RHNnSDWcEGTQuTTgPl05_lBPlc9oTkEvl-eqzPKMVDmG-ClkHn3evpUymXPR5l0__0XWIBqJOrr4JACDcByX7SiCVAktiI1A6cIekDdt9hV2f-MbPNLF0zdbD4qfBBNl-YkgeNTQ60JueUyr94BBtoxjmkIyrz1Cvv7fK9gIwx9EOb3bl-q42vjqcHtVC_HFYIh46Ff8HZnfN6YOrfGEpinTvXOrnIxlIWYjPTnGX6w17TIwq8YJSRwa3wC9nf6ebRhh2FIr69W23YOgoQOJ3n5vNLo7ZedwLCPM_T5RzvrR9bKQ3zOKVcupyGqB1Vg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
دبیر شورای‌عالی امنیت ملی: شلیک‌های مداوم رزمندگان ما، تا تسلیم کامل دشمن و گرفتن انتقام خون کودکان مظلوم میناب و لامرد ادامه خواهد داشت
@Farsna</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/farsna/452441" target="_blank">📅 13:30 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452440">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SjVFdGUTeP_Ogp7-zwT-De48t374XMxutzfzAlvBOFZ3HmpZT7tjvmeMB1lWqT-Wt5z4gnTUCeXfaTQ5-ZXlRDCDFGtwwWPCqfCrEuitKD7OTXICCKKFlFewrqkPo5kh_oVmdqjuw3NYWo7D6jcrRgzNj22m1paouCTQSStLK5f9X5qClsmL0tH4F_v-Jm8gepn39KrsPx-UQObNXKXkoJ5vDjyt9D0VDTs4Tsc_SLmkmz2yLdvMNQB-Gd3Wi2pedjM_Q44tf61gZWMqq4hkX97MTho44vTQnRus7XhXbYc12vdBP8UuEYw4z8bPDcjgAyqS-QhnTfXFJD_QHB7vpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">انیمیشن «سفینه نجات» در راه سینماها
محصول جدید سینمای انیمیشن ایران
«سفینه نجات» تازه‌ترین انیمیشن سینمای ایران به کارگردانی هادی محمدیان و تهیه‌کنندگی محمدامین همدانی پس از ۲ونیم سال تولید در سکوت خبری به زودی توسط پخش بهمن سبز در ایران اکران عمومی می‌شود.
محمدیان پیش از این کارگردانی انیمیشن‌های «فیلشاه»، «شاهزاده روم» و «بچه زرنگ» را برعهده داشته و همچنین محمدامین همدانی با انيميشن‌ «پسر دلفینی ١و٢» شناخته شده که فروش ۵ میلیون دلاری و جذب ۳ میلیون مخاطب را در جهان رقم زده است.
@Farsna</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/farsna/452440" target="_blank">📅 13:28 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452439">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromمس‌ پرس</strong></div>
<div class="tg-text">🔸
مجمع مس ایران به روایت رسانه‌ها | ۷
🔰
مس ایران، در مدار آینده
🔻
مجمع عمومی فوق‌العاده و عادی سالیانه شرکت ملی صنایع مس ایران چهارشنبه ۳۱ تیرماه در مرکز همایش‌های بین‌المللی صداوسیما برگزار شد.
گزارش گردهمایی سالیانه سهامداران «فملی» را از نگاه تلویزیون اینترنتی «معدن‌شو» ببینید.
#در_مدار_آینده
#مس_ایران
#فملی
@mespress_ir</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/farsna/452439" target="_blank">📅 13:27 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452438">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/farsna/452438" target="_blank">📅 13:26 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452437">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YUP3ndmSfyS__WaYJu8HA0s2Kwzw5-T4K_UN-vonGCOgQjKjHCV-FJEEvJGAEEmnOKny9NaSczgDDS0fukLbgxsD0pkOcCnsQV8pwC6HTZ6bEs6CsqDIT6ENU1CaUh9tqYTTnd7NgA-IrpTRwl4sOF0cVl6vq0z2E0fcX3lle431RUnidH3IMgsXw84eeD8AiQr1zbX9n_oPacZPM0TdLvc3saw-CVQ35DnUK_VtyGnU_eGkzpp77EE0OAPUv5hROqHf_M6UuRx_juSXeZoUbXFMYKpE6OLDcHa0IpaoU4yAvaitNm4NPUa74xsAgaGm_i-O7DN-UvJnIioTYPq2cg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
ساختمان باقی‌مانده از شرکت آمازون منهدم شد
🔹
سپاه: ملت قهرمان و به پاخاسته ایران اسلامی؛ حماسه قیام بی‌نظیر شما دنیا را بیدار کرده است و دعای خیر شما، پیروزی‌های درخشان رزمندگان اسلام را تضمین کرده است.
🔹
رزمندگان اسلام در موج ۲۷ عملیات نصر۲، در تکمیل عملیات…</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/farsna/452437" target="_blank">📅 13:04 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452436">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nPh_l4VPQ6nI8LoKnHSdTfBmVVTWYWnEj_Hl3293fpvUCU2GKs73dEYCp769nYXRXIuXnWKAAcRS_J-IruQJIsojFzPl-jcYqnYSSR7a9MDtz0ScvOvBdRts1j1YkqkV6kUhGEN37E-wQwljG_nbK6ONneTARhGqtmoklmbMZdIISLXrQEctVJ9dXhaxs6jcAuu5S3IaiC6HiFe2Mkh6Kf53slOq00mGoyRLsPUxoxKzwI9qzjUDn9lQPixhHOp-kW26yhdYPHOdhgLnPf0hSV0fiEeeNRo7fYxJWdeG4OvumD_y_kPHf-b5i1MviC4f6HPMYFl2E_aVvF5VsZfYVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
پیروز قربانی سرمربی آلومینیوم اراک شد
.
@Farsna</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/farsna/452436" target="_blank">📅 13:03 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452435">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BVlrTSeElUHXHvRdte9CklWY59D8kqPtrVfptx-dw9hUccVKQ4PVOaiaELk7ORe-1dCQpssaZzAtLOsJ5ZOws_VXCJzfw-QDTXZ5FSxQz1C-f20jvdZqDrJqxGQDswxNmOAVVBpR_MGgI_qMQZBasE-Ku6HOrxrvIQpVAMuvxYkCRcUCS674Gbo3gMxJ13raZooqKzi-fv5LQrktLdnB5qRAQlS23fCYHaZwqc44mcwCRF0xmHvetgqL15b1lqmgPyBHdOLgRPQHFssYScU3jEic2gytzWJCg2yncOISYIhP-06OaivcUAktq1Z1Pl8aMk-oE4cBSpHINa8zWr_5qw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎥
لحظهٔ اصابت موشک به پایگاه هوایی ملک فیصل در الجفر اردن  @Farsna</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/farsna/452435" target="_blank">📅 12:47 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452434">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/46fbcb92eb.mp4?token=ps_7gUyMYJap3hUnptiYqndRCyMjig47ERdKVMxv3tTFjmBVct43S0h5Xlp5c3dS7LwkRPocG7639PMECcyPRQnCL8xs-2Wc1K4UUwHqArAOaf3QgFjEenrtDqbjNR-FTgTKgl2fsUIxYkbHFxJofNotKnoDS1pG955zIPsp01zAGwdcgl7BEQ3xSn5mem5dGu13TZuIDmziYrLrpQ_5ZIAlB-osiDk3msWXTOjTBUEhrcPfKzT3c5r7AN0zs8Bod92k_ceTEeOLeXMDvBd3UlE8Z3cQv_GHMcCVR2yXtSQi00wfltDrJ67sY4DHIBSVsyKQL76afPr_EGDyGeLC7g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/46fbcb92eb.mp4?token=ps_7gUyMYJap3hUnptiYqndRCyMjig47ERdKVMxv3tTFjmBVct43S0h5Xlp5c3dS7LwkRPocG7639PMECcyPRQnCL8xs-2Wc1K4UUwHqArAOaf3QgFjEenrtDqbjNR-FTgTKgl2fsUIxYkbHFxJofNotKnoDS1pG955zIPsp01zAGwdcgl7BEQ3xSn5mem5dGu13TZuIDmziYrLrpQ_5ZIAlB-osiDk3msWXTOjTBUEhrcPfKzT3c5r7AN0zs8Bod92k_ceTEeOLeXMDvBd3UlE8Z3cQv_GHMcCVR2yXtSQi00wfltDrJ67sY4DHIBSVsyKQL76afPr_EGDyGeLC7g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مرز سومار از فردا آمادۀ میزبانی از زائران اربعین است
🔹
فرماندار گیلانغرب: زائران از فردا می‌توانند از مرز سومار راهی عتبات عالیات شوند؛ مرز مندلی عراق نیز آمادگی خود را برای ارائه خدمات گذرنامه، پذیرایی در مواکب و تأمین وسایل نقلیه اعلام کرده است. @Farsna…</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/farsna/452434" target="_blank">📅 12:39 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452433">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UAVdGzLZ43MObi7pdwQoyyjNtmDc0VPivi9CeMvCQVgefaQVhZq7jkNDThoQxFgHnzijrxodHOSWPg2fXaNDylg--RjwPv49BfDlCcJIEpOsXybafqE4yiyXeg_nMfH6XKBLJEjLhb0JpSP0T6XNt4E0x4bBnEHQWObIaNG9F30KflvdrvD_ldtJEgkaqwo8nLedVaqkAm7iP4rhvW-qtPzKAjVxNFDR_MOZQIxpjz6chGCWE-qIDw2on9kicrUHW2olQ6AIss9vPrBGflM1_pH1GyBXcf6i9iLLG_eMB5Qs0f2L23htbMK7lXKf7rl5F1sZlUAs3eXaBplaC3QDaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شاخص کل بورس در پایان معاملات امروز با رشد ۱۰ هزار واحدی به ۴ میلیون و ۸۹۴ هزار واحد رسید.
@Farsna</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/farsna/452433" target="_blank">📅 12:36 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452432">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kkX2V7cc1LjQKasRzY7vE76Tlg2CoFfPSe0byhqJs4W2oQ6ktsUEugfgcHpsMKxu4rINuI6Gvvxg6FF4Br2h5jQamWiwy5hMk2B_QxyTdAM-QuPu45IKavGW8xInFMa-gTGdQnusWPy9Zq4w0VaVOr5G9CzYIiOvGI_GwZOvfdGJTJnHg87IxGxEXzc-517YVA2GdVmvf7eaBbrQQpXKt-bqn3TuBW1qAbHQ1Tt6T-fAKZgmEOtBwAEkxbGYQqhCHu7x5WHEaEp4eg5jU-zSTZ-u9EVZKVqYPC_Z_WhE1pdwFtmRagxcBcypVQaCRRODmlO67p_MX-KwnhhlKfCUgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
حادثه دریایی در دریای عمان
🔹
مرکز عملیات تجارت دریایی بریتانیا (UKMTO) امروز اعلام کرد گزارشی از وقوع یک حادثه مرتبط با یک نفتکش و نیروهای نظامی در دریای عمان دریافت کرده است.
🔹
این نهاد در اطلاعیه‌ای که در ایکس منتشر کرد، افزود مقامات از این حادثه مطلع هستند و تحقیقات مرتبط همچنان ادامه دارد.
@FarsNewsInt
-
Link</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/farsna/452432" target="_blank">📅 12:34 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452431">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">ادارات مازندران فردا تعطیل شد
🔹
استانداری مازندران: تمامی ادارات دولتی، نهادهای عمومی غیردولتی و مراکز آموزشی فردا به‌دلیل تداوم موج گرما و ضرورت مدیریت مصرف انرژی تعطیل است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/farsna/452431" target="_blank">📅 12:21 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452430">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U3K_pDhwajskNKyMC0L9q5K_mWj9IGJhggy1mrh5BurPbFxDb_cQc4awnF3NaDaF3kzEkbU_u97ampkyDCTVH6NlKGrSoZYaVVbG7ztKcL61GeWWzp0q5nKESo-8OfLI2Y-5_CckGEVaAq3tzfR809nEMBDiNu6p3-Mj_NzhOAUFvJ9ZaRQW5pYKF9Dbug3P-455JgqXT6h9qj6HZ0RCMLAYBNikrMvSWSTDv_omJOL7kGDUtDToa9Puf2xQijjuCaKl8J5dIk8QNSrfRBdi8ztNUxUiwByMSsXt93Y3Hvq3e3gheB27b1fsF5SpiWzn7nsxM4ZvJHfsja8aQQxR5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دستگیری ۱۱۷ نفر در مهمانی شبانهٔ غیرمجاز در رامسر
🔹
فرمانده انتظامی رامسر: درپی دریافت گزارش‌هایی مبنی‌بر برگزاری یک مهمانی شبانهٔ غیرمجاز در جواهرده، ۱۱۷ نفر شامل ۴۹ زن و ۶۸ مرد در محل مراسم دستگیر شدند؛ مقداری مواد مخدر و تعدادی آلات و ادوات ممنوعه نیز در بازرسی از محل کشف شد.
عکس: مرضیه سلیمانی
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/farsna/452430" target="_blank">📅 12:17 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452423">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/twVe9bJrdzhBuo_8YSaRw264qY_zhR_rK04CKefaXEYiXVUaLlV94W99ypd8y74Oynz34G0p0DcwFiDgNzCNIVj3Ljv3wC_Ou26mGUV44b5qSo7eDcBgdHUZySy7Y9WrIxvNOiv1kLrU0fByO7Z4xflRycnzewC_WdvZwHy1RdS2_fpNDX3xXJBxYFhzqg9zwm6YH_YhiA3M29kpt8WnInxZscTyLCHU75zDMQ4JKfTPLkM13XA4L7YAz5KFeH2YtD7PzAuK4b_2YFK20QkKF3GD5gN3ihZDBFV53ThaebYYwVrx26XAsxg0QI2FQt6o0AaYmgU1XOETUCPQf7PL9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/urB8zVgO7stk5zfw4wnXRGT_9KCWqrfZ-IsMR67cSz4uVIChdgL0e-_bNRxDPNvNuEfJngHaX9Ip0HIeqidNDoz0SkNfL6YNHBELHq3FPs_OU0CoFfJToSp2wBLyV0Ftz7HmBiShbGSkg56tScyra8c8AFHZ0V5sDcfMDUT0qgpNih_JKA9YuZfaN9WKFLUXnvmSkUPnpGNbpdmuTr6hdYB29x4VpfCDaAlUFbSS7_5nUBmcB-nfdji4VW7drOP5OdvctRXiVXRPGS4AZ72vbOhkqFTmSyFoxOL5aJa7YKzMjK-MJnYnDN-kZPubD4zcqi2FzfpYuteL-0fFzmEJEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GEPKq8rNL4VM1fX8uY26xQ4fv0Dfv6ThIDlSIAuvFEe12vaUj--FEUUxqYGR7P8XG5-yrIWYJUVCM6nI3NoveZw_IOTviPblizxm35kK4mLsd8xHyODDQS0eo-ez8pas7gcCdAhExVSlAPdyuThg4RU1OhsduTZ5YPX1sqkRPuIR_WbreWg0wySI4BE4akDAjr98fVkFJmruiyZNQk7UL6vE5j_SHknNFc855X3LukDR1g8-XWerjiD5gylTxZYWTpCYaXELAkopmjYlm3JaaXzS5-0KO0A9ua_0_6Tj4CprzwrPs_7mCFkcFoJu65wxGbxZVVSXEdIVYpGSHPORyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/L874mccNGLNc4roI-H0o_P8saRdyo5zW8kfygx9S-rN9n2lWXzdfis-ISYkYlSLG8JyJyot4flLwY29oQflCPzTCZm2uXdER_Uob6zuOvxV5KWPBiiku18qP1MwOOSuJwqM3W7U9nQo7nnjdS3esoOGA0VAnFRw0TTPU8KKcTPcVbD6t_LiXQM8hjFJa8dM7UolhpTUB2OCF3HlWpEk0Y12HRdqlcMuZCo26-zxbPX9no5RFVaGLb9yCmFkGDOo_fqBuWN6ff70II-q6LI5Ks-EK2D8pXM1PgJ1DobKsHNjbprXK6Su-S2Xn3nnfv3lRCCz4p1gD-4s3XaT0I-SCJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/taU4nxrGndknEVD3VBehWm52IEzjYdtY3o3CxoI63HeRobPf0bsyLloJQkFgTny6Ob2pdxpXFuqaC9nm7rBrBTdsXj-aiVLGUwVySuw5ceQg8SxdCAHKtgoS_fn-_KFlTIYFhmtPu-l2kY7cewT-1IDrcq3XuzdTvu271Z5tLds9FR8rk2_btJwVLy8FcAOlxcLBIuuFCAncuO03Lpeemnr2fX7e51Uim8lt1hDzbCSgUqLfIv1k4WMxHDOjGLNJquE8W0rDLBshtLUSMmvw2_O7IlHQjHOxCT-8RsTp-ssGLRowXEUdCGvKatxiziNclIdT1Cub7ZBmXk0ZwNvGTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Vu1AjyX1j_Df9uuz8F2OGQq2_0AWRR8yQFvHUFqLX3mXn-dMdJFWICm8-IkCUJWFtJbSLkTiuaYsQyedOZDtQhc95TPbk-lbS4MeSvOJX9eC-bQRqmimOHBTRv1CilufVbXq_dRaEcNTWh_PPaGRj21dvkwTde3SCxxLsA1FZu6iWM52XldPbc5D9sdMcOLlM44b0KPFi_jaMdHwc1-8O2I5ZD0HvJxnHECKgroqDWnBNew11YQn14jnNI8IZqCCnRq3FhWf9mRv9EfO0bNLG39mDa7Pz0k3jHnyy1KQ5ac8Nf9gcsFpfXfyB1hXmEU6xBMTrL7pDRfCzSCLqXFd4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/O2huYNtfOkEVYe7_OcIjKH4RFDYZdIXKEk2XAk91jaAoDj_-LNnSg6wbpjjv9305-KjkJdCIOpX1DLMGZhosLolZLtYZyYz_UkvVlTZ36lxk0d7q2qskEY-lNoZroFCIIpVI41YnxJgV3Zj_DzrZu08-9FQwO6hsbW1vHu5Ns-5D1qMG_2URtOs6K6u50pgAhlHScnXSQ1LEvXNAhlHPKrkWI5FWImtHE0zg-FA2-1FjrrzfxRRQZtnG0IaTFzy1cCEm-jS7UAs3Wv88soepLq5vwyI9xneq3dVs9VLJi5OTC_2eSpMOKGGTOUQUWpS-ArJjEvIGD1lAnoKmdTjB8A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">فوت کودک ۳ ساله بر اثر حملهٔ سگ‌های ول‌گرد
🔹
دادگستری کردستان: درپی فوت یک کودک ۳ ساله به‌دلیل حملهٔ سگ‌های ول‌گرد در امروز، ۲ نفر از مدیران شهرداری سندج دستگیر و علیه مسببان این حادثه اعلام جرم شد.
🔹
سایر عوامل دخیل در این حادثه که مرتکب قصور و ترک فعل شده‌اند،…</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/farsna/452423" target="_blank">📅 12:12 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452422">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CtaSdylGZu3QLIAPyWYOKlMEJacV1t_6RezazaFFKVHIK8ajptH0gMOO6R4iT_QiTPOud95GsHGInYQe8NkUjrZX7rajmdh9y7MiRJls5omMY-AHVJ0AR4MenpYcIyZIxuRoTKo4LjrXEb_OqOQACjMrcmXTmuvL-WUYSRsb6UvYs--hFXT65lifpON4OGO8kybGzv-w_3W5nAG3JFukI087jDy86dh_oT_7LxWb4_w1sdy8NA3b9mvaiZUVrgA689JrASTpqNFpS6uplNK6S1QbuXWT21zlVrLXT8J06gOwUPKdvWJ330llGCsgHCetxK6yVdpx0Mg943NXoW3V9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سرلشکر عبداللهی: شهید خادمی چهرۀ تکرارنشدنی اطلاعاتی بود
🔹
فرمانده قرارگاه خاتم الانبیاء: رئیس شهید سازمان اطلاعات سپاه از نسل اول سپاه به‌شمار می‌رفتند که با مهارت‌های بی‌مثال، اشراف کامل به ساختارهای امنیتی، زحمات طاقت‌فرسا و ماندگاری را در حوزه اطلاعاتی رقم زدند.
🔹
به جرئت می‌توان گفت که شهید خادمی در مجموعۀ اطلاعات و امنیت کشور، یک چهره تکرارنشدنی و غیر قابل قیاس است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/farsna/452422" target="_blank">📅 12:05 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452421">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/225fcfe9b9.mp4?token=gfNEChcef_h6YLTDkYIblX0AaxX44iKFxRWVc_X3o0r26glCakr45sTRlydauq5PjMTpy0fqFyi8mMK8njtoYyx_qrDvzWY3glG_SBKkNqVV2sduOYV-p4Ux9f2QrnEFEHjUgbwtvXvcaL_hhNhpJDbh5QrpXdA61cAIwBuF-FsroB8D3_kCkuRCqrev_xXLBjPt9yPbdsNZVp9Lsvlm9obhDyL93-s4BvQQALA7OotBhSxojNr_xzOJoigpmzDRRkN3S_xdt9XcnyN54Rg39X1NWZ1cYTMGPuB3SnSM4hrq7y_acHJZP_jcQJo3C8h1Fp7BneZA60uvAjHR7Ft9sw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/225fcfe9b9.mp4?token=gfNEChcef_h6YLTDkYIblX0AaxX44iKFxRWVc_X3o0r26glCakr45sTRlydauq5PjMTpy0fqFyi8mMK8njtoYyx_qrDvzWY3glG_SBKkNqVV2sduOYV-p4Ux9f2QrnEFEHjUgbwtvXvcaL_hhNhpJDbh5QrpXdA61cAIwBuF-FsroB8D3_kCkuRCqrev_xXLBjPt9yPbdsNZVp9Lsvlm9obhDyL93-s4BvQQALA7OotBhSxojNr_xzOJoigpmzDRRkN3S_xdt9XcnyN54Rg39X1NWZ1cYTMGPuB3SnSM4hrq7y_acHJZP_jcQJo3C8h1Fp7BneZA60uvAjHR7Ft9sw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
برخورد صاعقه با موشک چینی در حین پرتاب!
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/farsna/452421" target="_blank">📅 11:43 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452420">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">🔴
یمن از فراری دادن جنگنده‌های سعودی خبر داد
🔹
وزارت دفاع یمن اعلام کرد که پدافند هوایی این کشور با شلیک به‌سمت جنگنده‌های عربستان، آن‌ها را فراری داده و مانع از ورودشان به آسمان یمن شده است.
@Farsna</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/farsna/452420" target="_blank">📅 11:15 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452419">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ab5faf50be.mp4?token=Z7sTTPEXDKLPQKFzRVLMjD9uF_KmOv8kJuGHz3Raem_ND4uBUSwTes-kBkLZFa0DNMducjRTwZKK6tefy-JnhtZFS5dqZf2rWw9zPdaAyrbbC7TROrJahKLbvopVAsy0kmGgaX90H8PHnPTZ9aO4klKbL09bd298p2JE5XClgR4bQbaaWT5Df0L4veeT_JCY0YxXObqbLx7n3k6mLik88dw_c6_F31GIorvpStxyEXg3CZq5Ax7g_hqwoAxd10_WuQs3xMhe1grbypftZJF-q5BGq9wiAVAl_RacR9sLAT6IxeNSjaV7VD1Q7J0ux-AIaEaQ5xVfYWxec9ykve9nlg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ab5faf50be.mp4?token=Z7sTTPEXDKLPQKFzRVLMjD9uF_KmOv8kJuGHz3Raem_ND4uBUSwTes-kBkLZFa0DNMducjRTwZKK6tefy-JnhtZFS5dqZf2rWw9zPdaAyrbbC7TROrJahKLbvopVAsy0kmGgaX90H8PHnPTZ9aO4klKbL09bd298p2JE5XClgR4bQbaaWT5Df0L4veeT_JCY0YxXObqbLx7n3k6mLik88dw_c6_F31GIorvpStxyEXg3CZq5Ax7g_hqwoAxd10_WuQs3xMhe1grbypftZJF-q5BGq9wiAVAl_RacR9sLAT6IxeNSjaV7VD1Q7J0ux-AIaEaQ5xVfYWxec9ykve9nlg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ترامپ در مراسم شام خبرنگاران سوژه شد
🔹
دونالد ترامپ در جریان مراسم شام سالانه انجمن خبرنگاران کاخ سفید چند بار با چشمان بسته دیده شد و به نظر می‌رسید برای باز نگه داشتن چشمانش تقلا می‌کند؛ موضوعی که به سرعت به سوژه رسانه‌ها و کاربران شبکه‌های اجتماعی تبدیل شد.
🔹
بسیاری از کاربران با یادآوری کنایه‌های پیشین ترامپ به جو بایدن، او را «دانِ خواب‌آلود» (Sleepy Don) خطاب کردند و برخی هم این صحنه‌ها را مایه شرمساری توصیف کردند.
@FarsNewsInt
-
Link</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/farsna/452419" target="_blank">📅 11:11 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452418">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">احتمال شنیدن صدای انفجار در شهرستان ری
🔹
فرمانداری ری: به‌دلیل انجام عملیات خنثی‌سازی مهمات عمل‌نکرده در امروز، احتمال شنیدن صدای انفجار کنترل‌شده در بخش خاوران ری تا ساعت ۱۶ امروز وجود دارد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/farsna/452418" target="_blank">📅 11:06 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452417">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NbuD73KzhLG5xF039Rso0A1CSL60fhs86ruFnNBo7KmEAFds8X42G87EVt_vdqhn30u9P0mW4vae6g4TU_YvlgmxIPMwqpTYO5rNa-PuxN_uSEzdbkSdloDbkc7891zZOPJRlPrx0oCCVqDuwUADdPT5UbOKZpc2Qds1kURAVmhHtG1-Q4krvGZ1omIWPeUBnTnh6OyoIORml8RRqYHWo7bHOpHU6IIdkzWxJl34uYsfL7jcNHBqOSvpG-4AC_JfBpeG7L08AR2eLWwIBNSnNw9IQj2UE3CGfMCWG7QS4W-FWi4JsfqFsTsVOYJG275TdTt7MfZzSr8XBdmTaWOYag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نرخ جدید حوالهٔ ارز در مرکز مبادلهٔ ایران اعلام شد
🔹
دلار آمریکا: ۱,۵۱۴,۶۷۵ ریال
🔹
یورو: ۱,۷۲۴,۳۵۴ ریال
🔹
درهم امارات: ۴۱۲,۴۳۷ ریال
🔹
یوآن چین: ۲۲۳,۶۸۳ ریال
🔹
روبل روسیه: ۱۹,۴۱۱ ریال
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/farsna/452417" target="_blank">📅 10:55 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452416">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/57a8a34369.mp4?token=A3iqEow3XpgWgL2bFRDllZMolBMdnf6n3KPjPUaclDn_LejLn8v2OPOzj14Ai2jqmRzVrFfYtJfGH_PkTlfqZ97cBs6yTiPvd2Ow_OT2TAfMHkeVrhGzzhgzsyQ-JALogidCHniYBQF5Z2hTdJHEFZtE8XO4rQKSll7kTaDA1aJLPUHGv-zAwkejv9sJcX7QEH-VAgkNaauIfdUOIk-NxmjCxRrUu0LTt6yuubo1vcjPVFSLqKyEQAgDq6RQ8OnodhRiu3mQVvWqdE3LBplxiVSn6CNa0EwFhHpDPjo07fhgJbnHitCVtOf8POpOfPA__RkH_lV4tdosdeBQfFovGw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/57a8a34369.mp4?token=A3iqEow3XpgWgL2bFRDllZMolBMdnf6n3KPjPUaclDn_LejLn8v2OPOzj14Ai2jqmRzVrFfYtJfGH_PkTlfqZ97cBs6yTiPvd2Ow_OT2TAfMHkeVrhGzzhgzsyQ-JALogidCHniYBQF5Z2hTdJHEFZtE8XO4rQKSll7kTaDA1aJLPUHGv-zAwkejv9sJcX7QEH-VAgkNaauIfdUOIk-NxmjCxRrUu0LTt6yuubo1vcjPVFSLqKyEQAgDq6RQ8OnodhRiu3mQVvWqdE3LBplxiVSn6CNa0EwFhHpDPjo07fhgJbnHitCVtOf8POpOfPA__RkH_lV4tdosdeBQfFovGw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
‌کارشناس اینترنشنال پس از ۷ ماه: کشته‌های دی‌ماه ۳۲۲۲ نفر است
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/farsna/452416" target="_blank">📅 10:50 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452415">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rnz0G3PX3fE_w1ufaIC4PpcTpu0os8XVKm936ccA4CJTge6Hq-x7COeUE3zVWiNgpdcHOF6-T9v7K1ZZzk4KBEZi8FJuCgNGJEQp6ZrvgSlXNqdTWg5waSDVgjejwmdypINq00RsbkpSL1PUh6Vr-6aNPeVirCj5Xr3q_sQ5DZxRNpSulXqgZt9tn6_Cy6IVSaizPb7yWaUhf3Bw2h9zKTeSAlyAfiuqP1vJMystYnn9ivamK7d8JZsRb26ABi5EIICaW0MAaUO_bRBWBVo52NPHvBPr1npjKYE6EdBHbm5Sdh27E500mFioghcsBR1vn6zYMD4cBAQEM-NsceqlWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فرماندار پیرانشهر: از آغاز تردد زائران اربعین، تاکنون ۳۳ هزار زائر از مرز تمرچین به‌سمت عتبات‌عالیات عبور کرده‌اند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/farsna/452415" target="_blank">📅 10:45 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452414">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">احتمال شنیدن صدای انفجار در اصفهان
🔹
استانداری اصفهان: احتمال شنیده‌شدن صدای انفجار کنترل‌شده در جنوب و غرب اصفهان، بهارستان و صفه و ابریشم تا بعدازظهر امروز وجود دارد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/farsna/452414" target="_blank">📅 10:40 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452413">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MRhtxpEjdSnLktIyZ-ArCFsTrmhpHegPPO2OK4kp_bR_uAn1-2Ut94DSLg1h_Rau9yA7VglLijFau_JcNVtrQ5Dtqj_tTsb7nc9MyoIWKfa3FDGw62MPnvgWIBFMMLrga4KHqch56p5QKnVc76BjtiUQU4iIWCfNzXNj2RLna5UyHVIIAkTIZ3JbGps0DthgYJoKWkrIWNMONJ8199uSWeDdlGqZf8l4tD3NI6sII_LcnaZKqDfGh6uqAzVHwqngQ7wfktKoLFT_v6gS1bsIngf7a2v9chw1FS7oD02x6nutiQGmSb0azFSIkpijtCiXG_tDGRNJ6A-cNpJ8lfka3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گزارش عملکرد ۶ ماهه چادرملو؛ رشد درآمد عملیاتی و جهش سود خالص به ۱۴ هزار میلیارد تومان
شرکت معدنی و صنعتی چادرملو با نماد معاملاتی «کچاد»، در گزارش صورت‌های مالی ۶ ماهه منتهی به خرداد ۱۴۰۵، از بهبود عملکرد عملیاتی و رشد درآمدهای خود خبر داد.
مطابق با داده‌های منتشر شده، درآمد عملیاتی این شرکت در نیمه نخست سال جاری به ۵۳ هزار میلیارد تومان رسید که در مقایسه با مدت مشابه سال گذشته، رشد ۲۶ درصدی را تجربه کرده است. با وجود افزایش ۳۶ درصدی بهای تمام‌شده کالای فروش‌رفته، چادرملو موفق شد سود خالص خود را از ۱۲ هزار میلیارد تومان در دوره مشابه سال قبل، به ۱۴ هزار میلیارد تومان در این دوره افزایش دهد.
همچنین بر اساس آخرین سرمایه ۵۷ هزار میلیارد تومانی این واحد تجاری، سود محقق‌شده به ازای هر سهم (EPS) برای این دوره ۶ ماهه، ۲۳۹ ریال گزارش شده است. این ارقام، نشان‌دهنده پایداری عملیات تولید و فروش در این غول سنگ‌آهنی و توان سودسازی شرکت در آغاز سال مالی جدید است.
@Farsna</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/farsna/452413" target="_blank">📅 10:40 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452412">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromبانک تجارت | Tejarat Bank</strong></div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/tT1N2fCObUFyLnvs4IG4qoQaaLP5vi1zwQcRVfDSNlnHxavoc1DDJZJuWZuW6qak1J63cZP8sQbbWm7Kk1QwOkmgo3mCO8mL2aqaP5QcahQsN7WF3NCCL6e9gABFzXseC-gNzIR5-s5AVD0DTst7PdV02Rz2xts0VyC2DTFezeT5bLxH2gN8z8coO7Q1L1TkKNb24MulRvyYORr-hQk0dfNDIbx8dKKKCVzT4AL4q8PGY-bbZHHgGsjZ6pZjjYddl2cWP0wlcgTIo-FNYllbDiftK-yXD3fMHQ6Op2u-xEyEKlM3ahbSRzorWc4d-EKb0z5td_LgvYH_QiccFhs5xw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏛️
مجمع عمومی عادی سالیانه بانک تجارت با حضور ۶۳.۱۱ درصد از سهام‌داران برگزار و صورت‌های سال مالی منتهی به ۲۹ اسفند ۱۴۰۴ با رای قاطع به تصویب رسید.
✅
این مجمع با حضور سهامداران و نمایندگان قانونی آنان و نظارت نمایندگان وزارت اقتصاد و سازمان بورس اوراق بهادار برگزار شد.
✅
گزارش عملکرد هیأت‌مدیره توسط دکتر اخلاقی مدیرعامل بانک تجارت تشریح شد.
🤝
از همراهی سهامداران عزیز در مسیر پیشرفت خانواده بزرگ تجارت سپاسگزاریم.
📱
tejaratbankofficial
📱
TejaratBank
📱
TejaratBank.ir
🟢
TejaratBank
🟢
TejaratBank
📲
TejaratBank</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/farsna/452412" target="_blank">📅 10:39 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452411">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/farsna/452411" target="_blank">📅 10:39 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452410">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">توقف فعالیت فرودگاه‌های جازان و ینبع عربستان پس‌از حملات یمن
🔹
براساس گزارش‌ها، درپی حملات یمن به تأسیسات نفتی آرامکو، فعالیت فرودگاه‌های «امیر عبدالمحسن بن عبدالعزیز» و «عبدالله بن عبدالعزیز» در ینبع و جازان به‌طور موقت فعالیت خود را متوقف کردند.
🔹
همزمان…</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/farsna/452410" target="_blank">📅 10:34 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452406">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dbd31d411a.mp4?token=he0ptv73QPp5i2QkYNeKsHYFiYx-m29PEy42srl8rtRLLWHRdxwjJTXnYuhB7zbuR9gzZHeXWy54oyurbgaB8dmjWhbTYjH0hd93Wu9xlS6Q6Hk1gRwiha5mXu9Lfg0WUvWAFV3I2QkFfkh_cSFc5luspKCVf2sh5bSj7rQdcWDFQwnWPaxczHfKoUtCogASPa_wy_w17XcyqIlJP5jYZ2OWmwUWK3RHYXWzovhQCfFWQi_bS8vzOtro1Qu7u0HwOsJugBUMdefBlsAkuKl-btEPro3lGEg97ccvLNHK5v5wdZX3NIjAfSECzbJQOVKTZkL84hV-mQ3KdtSlgV7p1g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dbd31d411a.mp4?token=he0ptv73QPp5i2QkYNeKsHYFiYx-m29PEy42srl8rtRLLWHRdxwjJTXnYuhB7zbuR9gzZHeXWy54oyurbgaB8dmjWhbTYjH0hd93Wu9xlS6Q6Hk1gRwiha5mXu9Lfg0WUvWAFV3I2QkFfkh_cSFc5luspKCVf2sh5bSj7rQdcWDFQwnWPaxczHfKoUtCogASPa_wy_w17XcyqIlJP5jYZ2OWmwUWK3RHYXWzovhQCfFWQi_bS8vzOtro1Qu7u0HwOsJugBUMdefBlsAkuKl-btEPro3lGEg97ccvLNHK5v5wdZX3NIjAfSECzbJQOVKTZkL84hV-mQ3KdtSlgV7p1g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ماجرای دق‌کردن دختر سه‌ساله در جنگ رمضان
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/farsna/452406" target="_blank">📅 10:15 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452405">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-text">انصارلله: عربستان در همه چیز به اسرائیل شباهت دارد، از جمله در دروغ‌گویی و تجاوزگری
🔹
محمد عبدالسلام، رئیس هیئت مذاکره‌کننده دولت صنعاء و سخنگوی جنبش انصارلله، حمله هوایی به فرودگاه بین‌المللی صنعاء را نشانه‌ای از ادامه سیاست عربستان در جلوگیری از بازگشایی این فرودگاه دانست و تأکید کرد که ریاض همچنان اصرار دارد فرودگاه صنعاء تنها با اجازه پادشاه عربستان فعالیت کند.
🔹
عبدالسلام افزود: ریاض از یک سو بر ادامه بسته ماندن فرودگاه صنعاء اصرار می‌ورزد و از سوی دیگر با صدور بیانیه‌ای مدعی دفاع از «حاکمیت یمن» می‌شود.
🔹
سخنگوی انصارلله تأکید کرد: «عربستان در همه چیز به اسرائیل شباهت دارد؛ در دروغ‌گویی، تکبر، کینه‌توزی و تجاوزگری.»
🔹
رئیس هیئت مذاکره‌کننده دولت صنعاء همچنین هشدار داد که ادامه لجاجت عربستان و خودداری از پذیرش واقعیت، پیامدهای خطرناکی برای امنیت و اقتصاد این کشور در پی خواهد داشت.
🔹
عبدالسلام همچنین اعلام کرد که اجرای محاصره دریایی، نخستین گام در «نبرد محاصره در برابر محاصره» است و تأکید کرد: «ملت یمن از حق خود نخواهد گذشت و آن را به هر شکل ممکن بازپس خواهد گرفت.»
@FarsNewsInt</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/farsna/452405" target="_blank">📅 10:11 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452404">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/58b7e22d39.mp4?token=j_fYjXbFEDXe4V7czNN_gJyejrcG33OdsGAsZVXMKTSigtnraMB9AhlDE1b9GgW4VyPLXnt8ErXOxwl9vV9YK7--3ur3eW3OyDSvm5cvasX-_PzBc3iCAElM2nanc__PjKEYabfVlNO9WBmWkBIrpqfKvS07iT4hvjWNVmwXih77A1cr89REMqP5NJTn_c05lHPgZbUXJ6cu7wa3VO6uMSEmGE0v4mzTgEjdVIJRKn0CDzGn-qMmuZsL-M84VfNLGdqQTgvAHOF8q0wv2ElE4ZbEpzN1EZ5-hXoxhzsrUOQ5lKHaTo1DVWSKQBUQPtS_roCw_91Z80CGTzT1UaJTng" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/58b7e22d39.mp4?token=j_fYjXbFEDXe4V7czNN_gJyejrcG33OdsGAsZVXMKTSigtnraMB9AhlDE1b9GgW4VyPLXnt8ErXOxwl9vV9YK7--3ur3eW3OyDSvm5cvasX-_PzBc3iCAElM2nanc__PjKEYabfVlNO9WBmWkBIrpqfKvS07iT4hvjWNVmwXih77A1cr89REMqP5NJTn_c05lHPgZbUXJ6cu7wa3VO6uMSEmGE0v4mzTgEjdVIJRKn0CDzGn-qMmuZsL-M84VfNLGdqQTgvAHOF8q0wv2ElE4ZbEpzN1EZ5-hXoxhzsrUOQ5lKHaTo1DVWSKQBUQPtS_roCw_91Z80CGTzT1UaJTng" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">منابع عربی از تعلیق پروازهای فرودگاه جده و ریاض، در پی حملات یمن به عربستان خبر دادند.  @Farsna</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/farsna/452404" target="_blank">📅 10:06 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452403">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DxAw1Yy_nPiCdLKdlENH--V9DJWrhW5ODyHytRB7jPsF6g7iGdmDA6-Kplfl1_fgJU-_mQbbsRA-EsbinQyxsyJeiP8jYEwYgCDdoj2awuuEuepbtn21nrWlseR_5-m0MQWSBW1_e076o4GF8TUVnsqXyIxJelw3remMcYbUgylMbEOng9_vkkrF5nCcF3p5mKquQCj-j6K4PY5hf2GXi5Ky8SUxsB_PvRBs43mKStXKoAz-2vxwNj3eOtyhUkSFT3FXRykik0iOoHWeb4YSS4_ByPo-VH8sRekuWD98St0VGFMFN2f9D4UURf0hs1MiJqt44BAd_UyFG1sJAFG6Lg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎥
سخنگوی وزارت کشور: تا به امروز یک میلیون و ۳۰۰ هزار نفر برای زیارت اربعین در سامانۀ سماح ثبت‌نام کرده‌اند.  @Farsna</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/farsna/452403" target="_blank">📅 10:00 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452402">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/06c3d1583f.mp4?token=NrlA0-7DrWpURtYsmu5NQRbVdLLCOjMwMgjT8TKwjG8yWJIldQRBlReI1zXZIStf_2W204cIyOBg68TaI1kyjqgCMxZ35AdZn-bMx1ozB33yDun720K_0vW1KoF2tgRd5e6KJ-vfTYXLBWpjvtIE9n-tzGhBzSreSrkLqfNYSkmsoawVNAb-Z2yrMBwfOhke9RLR-_X5tSs_3yMeNZ9Rl0SrRA5KoIxiR-WVjAty9NZ_208rXgj0WNo2WhqzfV7STviApby9b1AC1TkV_Yxg7PZkpMkUmT_hvnTalXveNyqnuOeR10HybqIU0fdAI3eRuUPs1v6fBn2RwCsshc-XQA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/06c3d1583f.mp4?token=NrlA0-7DrWpURtYsmu5NQRbVdLLCOjMwMgjT8TKwjG8yWJIldQRBlReI1zXZIStf_2W204cIyOBg68TaI1kyjqgCMxZ35AdZn-bMx1ozB33yDun720K_0vW1KoF2tgRd5e6KJ-vfTYXLBWpjvtIE9n-tzGhBzSreSrkLqfNYSkmsoawVNAb-Z2yrMBwfOhke9RLR-_X5tSs_3yMeNZ9Rl0SrRA5KoIxiR-WVjAty9NZ_208rXgj0WNo2WhqzfV7STviApby9b1AC1TkV_Yxg7PZkpMkUmT_hvnTalXveNyqnuOeR10HybqIU0fdAI3eRuUPs1v6fBn2RwCsshc-XQA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
دمای هوای مرزهای اربعینی امروز چقدر است؟
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/farsna/452402" target="_blank">📅 09:30 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452401">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Mnf1yO27lOSn5rIz8RrqwE15W6CmtxZI0lBuIb-QVp6PMQvy1fhw4zodWVgLuub9DZVgFm_qABHPunN6BcrqXvNRoYVE7-3RZ582bVst8HqU1NM1WVAkP0XcDkwV8GqpZtxSn3Ss49sS-60ym0gqE_CSzHbXORny5RLWhFmPpfxFiUGkI9pcrCvPlARRk4TSF0ML0V71sOBa-5egRiDhjVCUtw0RhhtgIIa5kOeh8O9WutBJAy7pPi3e3HjA_Y-D68QFI5gBI-K8dKyP9f8Qv-kkfCrh-tRdTIL8DA4ca_wmtragXMmK82qbR9VdTEgrEdnCSM4i_BK1BK1rtsEolA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎥
ستون‌های دود همچنان در آسمان شهر جیزان عربستان دیده می‌شود.   @Farsna</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/farsna/452401" target="_blank">📅 09:01 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452400">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2773cf754d.mp4?token=QULNmRt_Vb0CNW95M4EYooG9G17AtuAC1z4XnrFGQzjHwn_qKFUQANHhjGPJDcFFwuFgyW72ZX6M3HcoTfZajSB48jbkzE2QfetWcLu6SJ-FVnXcYP4BafPm_WhaVEkxUnvDDk_KZxvTVVAH61gS96dhXe4OgZhD3co567w2a8iW5OMWt6VtIg8gMQCGbDFsJ6mZpsEJRoAu546mD_mw_5qdpI64LYYYk3g-_jlXrtNBCQ5mrEa15GpEsmmYvIVB4qYFvnHfb3Epjx_vGtXbjqTbvkXRF25XYW9IV3QCrcSLkeSm2KCXnadiAzo1xLccjBXu4xumE0cmdzZFidtDdA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2773cf754d.mp4?token=QULNmRt_Vb0CNW95M4EYooG9G17AtuAC1z4XnrFGQzjHwn_qKFUQANHhjGPJDcFFwuFgyW72ZX6M3HcoTfZajSB48jbkzE2QfetWcLu6SJ-FVnXcYP4BafPm_WhaVEkxUnvDDk_KZxvTVVAH61gS96dhXe4OgZhD3co567w2a8iW5OMWt6VtIg8gMQCGbDFsJ6mZpsEJRoAu546mD_mw_5qdpI64LYYYk3g-_jlXrtNBCQ5mrEa15GpEsmmYvIVB4qYFvnHfb3Epjx_vGtXbjqTbvkXRF25XYW9IV3QCrcSLkeSm2KCXnadiAzo1xLccjBXu4xumE0cmdzZFidtDdA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مسعود ده‌نمکی: پیکر اکبر عبدی روز یکشنبه از مقابل تالار وحدت تشییع می‌شود  @Farsna</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/farsna/452400" target="_blank">📅 08:26 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452399">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZGlZndTrPSwQqTAYB5eDSqsp8OD4wsIQUDEk3YwCgxm1Bnv_O6NFtNSfXn7zzqUcl2gQE6E2gicDi_PfjsueMWciakBTmTqQi_Um-DpF45l7lqprsxYPjxjkf4ppQzG2FkaAjPezuAH-R4-hQmjmTgPiGJHZ8CnFuLutSP7p1Vjg0IHHI4MToEofuEjV3ieRSUAZ2-hfqHt86Zk4f2pFJlepsi-F-6oX_rAXNjLiPYRBuxCohXyX2idTyHjsEAdvCUcTa049KapOMG7PFbvN4rcGb6o7AhB-v01LLP14NyWz1Rqxiwoe0w564fRKebnWSE89e-IwbI53i54DcU02rg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">طرح ضربتی پلیس برای برخورد با تردد موتورسواران در خطوط ویژه
🔹
رئیس پلیس راهور پایتخت: طرح برخورد با تخلفات موتورسواران در خطوط ویژه، از امروز در خیابان‌های آزادی، انقلاب اسلامی و ولیعصر(عج) از میدان منیریه تا پل پارک وی در ۴۰ نقطه اجرایی می‌شود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/farsna/452399" target="_blank">📅 07:55 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452398">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">🔴
منابع عربی: شهر ینبع عربستان دوباره مورد هدف موشک‌های یمنی قرار گرفت.
@Farsna</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/farsna/452398" target="_blank">📅 07:46 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452397">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bdf62abd56.mp4?token=oz2oSEKgQLbQFrvxkuuW-J4WY7Wbzi2hjwM5FMaT6xU-CdQqIX-QtR2v5ZfbIeaWWUpIZJCWrrFeqBVMCLlclR2XnCourSVaICHQXGPXCWswtgPDQqV72Z0NHHnbI02DZz4tmUa-h7wLCUzugyJAdGFTkDaXTByVpz8nF0dgBNEQw1ndZdf1vMIND2mQc5twemkj1xVnq_O36_lPcn048CkENst8fRZt1ZUgmSKRcocy8MUoaZkyHrga9sWO6Wayndal1K3ZyfrcPbu4XQzRD0T7MN5Fav9gFuHaKXZ51z5PxVXy4CWHquOIdMjoU39nmUVVvnfK8d7vhrgtUu6EIg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bdf62abd56.mp4?token=oz2oSEKgQLbQFrvxkuuW-J4WY7Wbzi2hjwM5FMaT6xU-CdQqIX-QtR2v5ZfbIeaWWUpIZJCWrrFeqBVMCLlclR2XnCourSVaICHQXGPXCWswtgPDQqV72Z0NHHnbI02DZz4tmUa-h7wLCUzugyJAdGFTkDaXTByVpz8nF0dgBNEQw1ndZdf1vMIND2mQc5twemkj1xVnq_O36_lPcn048CkENst8fRZt1ZUgmSKRcocy8MUoaZkyHrga9sWO6Wayndal1K3ZyfrcPbu4XQzRD0T7MN5Fav9gFuHaKXZ51z5PxVXy4CWHquOIdMjoU39nmUVVvnfK8d7vhrgtUu6EIg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‌ منابع عربی: یمن، یک تأسیسات نفتی متعلق به شرکت آرامکو در منطقۀ صنعتی جیزان را هدف قرار داد.  @Farsna</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/farsna/452397" target="_blank">📅 07:32 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452396">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">منابع عربی از تعلیق پروازهای فرودگاه جده و ریاض، در پی حملات یمن به عربستان خبر دادند.
@Farsna</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/farsna/452396" target="_blank">📅 06:43 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452395">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">رسانه‌های عربی:
چندین انفجار شدید بار دیگر عربستان را لرزاند.
@Farsna</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/farsna/452395" target="_blank">📅 06:41 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452394">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">منابع عربی: انفجارهایی پایگاه هوایی خمیس المشیط عربستان را لرزاند.
@Farsna</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/farsna/452394" target="_blank">📅 06:14 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452393">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">رسانه‌های عربی: موشک‌های یمن منطقۀ «حی المطار» در نزدیکی فرودگاه عبدالله عربستان را نیز هدف قرار داد.
@Farsna</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/farsna/452393" target="_blank">📅 06:06 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452392">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">🔴
رسانه‌های عربی ادعا کردند که یکی از تأسیسات حیاتی عربستان در جیزان مورد حملۀ موشکی یمن قرار گرفته است.  @Farsna</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/farsna/452392" target="_blank">📅 05:38 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452390">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Gv3nrgP08ISQ2TX1qb9UfW2dD-rGQt9c-vd-MBRZgD2IZ36-NbPDkwk2DDL0eVazv9pGiHh0jpq6iAyBY9Z0qFJWnYgv5H44DmAOF10mxK13oJm5-sRuECtdYGHO-ZZ5Olx4x_zay-nDDXLlAyudr3lrEzGcQTq_tPL_SCV2uaHnjJB67Og5AoukzBpGrWXwuXLfX1a7AKZ8Y_-JmEkOAY0u15-Gg2iBT1e2lKvtdgZAkYtYXkFUZsnw6hC6cU4QXt3MufaAWqgiiq2MxWM0epXSwRQR9SKeAeTfF1t1rowgqNboDlQnR-CUQ52iek22QxukMh0lR_B-z4QzFqdTcg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c019742750.mp4?token=XoaB2zISvPc2Dgl9Na-zM8u8KvzJQqf1Qj-eNYSkrQY-gWCl_dA0IkZ81JAZH6r70SGY9TxEggJzPV92yGqwYdhA6ZHHatT0kwGy3RumBEHEXmJP2JGtzkzOejH3Ou06DlDV1uVunRWjtR7x3aaB_v7zxMz7hcWPZ-5tOE20nbVW_0IeOG3NPEUOz2jl3SPoJ7ade2VHrt1WDYE93QOVUiGOk5V-mltEsKk8ZCvvfdMj9xVS8NfwT63hrxsdCEd9-Y4yqahulJ_89RrJp-rPO1lLjP2aBXg_x77MPIczA7YWyexmKf_Ky0W-9Db8z297DWHzQ_tld2GVgHzx-nHr2w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c019742750.mp4?token=XoaB2zISvPc2Dgl9Na-zM8u8KvzJQqf1Qj-eNYSkrQY-gWCl_dA0IkZ81JAZH6r70SGY9TxEggJzPV92yGqwYdhA6ZHHatT0kwGy3RumBEHEXmJP2JGtzkzOejH3Ou06DlDV1uVunRWjtR7x3aaB_v7zxMz7hcWPZ-5tOE20nbVW_0IeOG3NPEUOz2jl3SPoJ7ade2VHrt1WDYE93QOVUiGOk5V-mltEsKk8ZCvvfdMj9xVS8NfwT63hrxsdCEd9-Y4yqahulJ_89RrJp-rPO1lLjP2aBXg_x77MPIczA7YWyexmKf_Ky0W-9Db8z297DWHzQ_tld2GVgHzx-nHr2w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‌ رسانه‌های عربی: در پی حملات موشکی به عربستان، برق مناطق مختلف شهر جیزان این کشور قطع شد.  @Farsna</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/farsna/452390" target="_blank">📅 05:30 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452389">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">‌ رسانه‌های عربی: در پی حملات موشکی به عربستان، برق مناطق مختلف شهر جیزان این کشور قطع شد.  @Farsna</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/farsna/452389" target="_blank">📅 05:27 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452388">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">🔴
حملات موشکی یمن به عربستان
🔹
رسانه‌های بین‌المللی از شنیده‌شدن صدای انفجار در عربستان در نتیجۀ حملات موشکی و پهپادی یمن خبر می‌دهند.   @Farsna</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/farsna/452388" target="_blank">📅 05:21 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452387">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7cbbaa84cc.mp4?token=Ok5V6meQsi63N4zvCtXYZ8A254ITe804u-gKBIjiSnTlhqvJViwYhyjUtuc_NITXTm3i881vHvjCMgIv-F9dfGvFpcr52PnlS5tEkrQVN42w1RFTe-B64xUddlHxVOLYotJtFRqdD1dzUacG-PPTcqcSzXNgsCtrs8fntWWErh5umEyprtxc6UrV7pMLVSwr8bHIFleLVQyh9pzyJ_eShxxrqivmomtk0wn6nqF-NLNIMKYnTlmXf44QEmYp5MgzK7ths0CM99pDYQkhjjK9vwgRhAOE01cl7yllRCgq3j0uALLGCpBRY1BOakueGEM-N7c_Au4nyrXHm2tWF5CkBA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7cbbaa84cc.mp4?token=Ok5V6meQsi63N4zvCtXYZ8A254ITe804u-gKBIjiSnTlhqvJViwYhyjUtuc_NITXTm3i881vHvjCMgIv-F9dfGvFpcr52PnlS5tEkrQVN42w1RFTe-B64xUddlHxVOLYotJtFRqdD1dzUacG-PPTcqcSzXNgsCtrs8fntWWErh5umEyprtxc6UrV7pMLVSwr8bHIFleLVQyh9pzyJ_eShxxrqivmomtk0wn6nqF-NLNIMKYnTlmXf44QEmYp5MgzK7ths0CM99pDYQkhjjK9vwgRhAOE01cl7yllRCgq3j0uALLGCpBRY1BOakueGEM-N7c_Au4nyrXHm2tWF5CkBA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‌
🔴
منابع عربی: بیش از ۵ انفجار ناشی از حملات موشکی، شهر جیزان عربستان را لرزاند.  @Farsna</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/farsna/452387" target="_blank">📅 05:16 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452386">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">📷
دیدار عراقچی و لاوروف در قرقیزستان
🔹
وزرای خارجهٔ ایران و روسیه در حاشیهٔ نشست شورای وزیران سازمان همکاری شانگهای در قرقیزستان با یکدیگر دیدار کردند. @Farsna</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/farsna/452386" target="_blank">📅 05:15 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452385">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">🔴
رسانه‌های عربی: گزارش‌ها از شنیده‌شدن صدای چندین انفجار در جازان عربستان حکایت دارد.  @Farsna</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/farsna/452385" target="_blank">📅 05:11 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452384">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">عراقچی در دیدار با وزیر خارجۀ قرقیزستان در حاشیۀ نشست شانگهای: جامعۀ جهانی باید خواستار مجازات جنایتکاران آمریکایی و اسرائیلی شود
🔹
جامعۀ جهانی باید با درک پیامدهای خطرناک قانون‌شکنی و نظامی‌گری آمريکا در منطقۀ غرب آسیا، یکصدا با نقض‌های فاحش منشور ملل‌متحد و حقوق بین‌الملل مخالفت کرده و خواستار مواخذه و مجازات جنایتکاران آمریکایی و اسرائیلی شود.
@Farsna</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/farsna/452384" target="_blank">📅 05:09 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452383">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">عراقچی در دیدار با وزیر خارجۀ چین در حاشیۀ نشست شانگهای:
ناامنی موجود در تنگۀ هرمز و منطقه، ناشی از پیمان‌شکنی آمریکا است.
@Farsna</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/farsna/452383" target="_blank">📅 05:05 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452382">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">🔴
رسانه‌های عربی:
گزارش‌ها از شنیده‌شدن صدای چندین انفجار در جازان عربستان حکایت دارد.
@Farsna</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/farsna/452382" target="_blank">📅 05:02 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452381">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O1tgrWBfODJOD6lSrv03Q9yNiK_l6T7aNkjUWTuFqi0q_k_Cos2OaLbBJcqIoI0D-QU55iIjGNeTG3EFwdMlhr6XMKpWNGdvacHIa7yTrwPXsi8x-vC3D8NwJlFm3zJiZtn0zP9RUov6JUGHbXhlf5GtI2sSutJMzRfJaz-ri3HhufZAo5unCJDjIuzyTwEfZW4ZYhRSe2zN03WCLmoo55aXxt5caQCDgPoV7wpwuVIog7zaAsMHYFlqNQMsGStLiuG1OY096Vhr5WP2mH39lnFd2t-fMCZQ6nDpePga-x0SO6OFfi_S_0-6gjI9GwY_3aoprUrKuWd7znudhebdTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">باب‌المندب، گذرگاه حیاتی کابل‌های اینترنت اروپا و آسیا
🔹
تنگۀ باب‌المندب حلقۀاتصال دریای سرخ به خلیج عدن و اقیانوس هند است.
🔹
بیشتر کابل‌های زیردریایی که داده‌ها را میان اروپا، آسیا و بخشی از آفریقا جابه‌جا می‌کنند، پس از عبور از این تنگه به کانال سوئز و سپس دریای مدیترانه می‌رسند.
🔹
طبق گزارش‌ها حدود ۱۷ کابل زیردریایی از این تنگه عبور می‌کنند که بخش عمده ترافیک داده بین اروپا، آسیا و آفریقا را جابه‌جا می‌کنند و این رقم معادل حدود ۱۷ درصد ترافیک اینترنت جهانی و بیش از ۹۰ درصد ارتباطات اروپا-آسیاست.
🔗
اما مهمترین کابل‌های عبوری از باب‌المندب کدام‌اند؟
اینجا
بخوانید.
@Farsna</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/farsna/452381" target="_blank">📅 04:49 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452380">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس معارف</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1877ec5443.mp4?token=OltqucPZaZiQPge4mHQuhgnoXj7vHKBMZQVnUDmoeqn-XWI-9n4cVRcStoA0QsB67kC28dqixCAyDrbONvkSCT39Jr8E8ksrJYHBYb63mZUYBzcb3EcyUujqfXCq4id-SKtboHa7yFG2tZD0B5l-QoydLZ18ahE3olnRWYKy1NRTCnlgLayxap3TWHSCa9Iwv5aPi3E7f2ee_BXNvOfUYX9OKH9eD96tT8aBAUr4vhXqNF9AJIDYQ1P6aHZzBl8F7BH4-roi5_JKqJpzr3i7kzuP6Jh1Y3_vLT0mkb28xo6bCdVOFKxJkzlVBeJ3xvT7uyXEhFPP7Up0L_ji3oaJYg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1877ec5443.mp4?token=OltqucPZaZiQPge4mHQuhgnoXj7vHKBMZQVnUDmoeqn-XWI-9n4cVRcStoA0QsB67kC28dqixCAyDrbONvkSCT39Jr8E8ksrJYHBYb63mZUYBzcb3EcyUujqfXCq4id-SKtboHa7yFG2tZD0B5l-QoydLZ18ahE3olnRWYKy1NRTCnlgLayxap3TWHSCa9Iwv5aPi3E7f2ee_BXNvOfUYX9OKH9eD96tT8aBAUr4vhXqNF9AJIDYQ1P6aHZzBl8F7BH4-roi5_JKqJpzr3i7kzuP6Jh1Y3_vLT0mkb28xo6bCdVOFKxJkzlVBeJ3xvT7uyXEhFPP7Up0L_ji3oaJYg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مومن شیرین گناه نمی‌کند!
🎙
حجت‌الاسلام رمضانی
@FarsMaaref
💠</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/farsna/452380" target="_blank">📅 02:48 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452379">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Cg2QVyI6xoV-WgAC2wRlNWJsPD3NoeTEFQL3og_XA90p4apzRS3CZhYB7KD9Mj0aMs-RFq3DCPXhO3nLbT6aCxkHiTcbhCVCWZqE9hP6dYmmTq8F-k4bzcZAvOM7xRHfSIYS-M9Aa8ivNCIuggARZroglO8O0--fmB4KPhzZFvJKCIkWxQu8iV8ZLxeFdwVE62scLgj7vECjz3L7YcwbkXcZxon5YlNdwnVUyRFcCzA_Inp3LMnJgUsvPCo1aMoqoK0LwcLn9gLKUO1GPfxWN0Cvzbr8a9XFSPamBuHtSG7a0nk3uSqEQbVzwOKwfYFot_PM_Mbqroqgdaj1gjpeOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رومینگ ایرانی یا خرید سیم‌کارت عراقی؟
🔹
با نزدیک شدن به ایام راهپیمایی عظیم اربعین حسینی و آغاز حرکت میلیونی زائران از ایران به سمت عراق، یکی از مهم‌ترین دغدغه‌های زیرساختی و رفاهی زائران، چگونگی دسترسی به اینترنت و برقراری ارتباطات تلفنی است.
🔹
همواره یکی از سوالات پرتکرار زائرین این بوده است که آیا برای تامین نیازهای ارتباطی خود باید از داخل ایران اقدام کرده و بسته‌های رومینگ اپراتورهای داخلی را فعال کنند یا بهتر است پس از عبور از مرز، یک سیم‌کارت عراقی تهیه نمایند؟
🔗
فارس با بررسی تخصصی، مزایا و معایب هر روش را مقایسه کرده است؛
اینجا
بخوانید.
@Farsna</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/farsna/452379" target="_blank">📅 02:13 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452378">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">حملۀ ارتش تروریست آمریکا به یک کشتی
🔹
ارتش تروریستی ایالات متحده اعلام کرد یک کشتی تجاری دیگر را که مکرراً برای شکستن محاصرهٔ بنادر ایران تلاش می‌کرد، زمین‌گیر و از کار انداخته است.
🔹
طبق اعلام سازمان تروریستی سنتکام این دومین شناور تجاری است که از زمان برقراری مجدد این محاصره متوقف می‌شود.
@Farsna</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/farsna/452378" target="_blank">📅 01:43 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452377">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/623461967c.mp4?token=V6ent683uljUt7rVdT_BFgnXI_ENWP7bZKB4KqCOalkv0sFD3D61mpa9CQl_nvfZt8TiEvj5DsRQ-OfTdmWV5_qK1yhoIz6gpZdFzrN1qM1qZ4oVd3U1tW5zNt7BLJGphKv_9KBUXSYq4R1vC30KuBngIPn7BiNPlLHGLD6mXvIh6Hk6_lrPh2Y0cSiOCcPdh5Tt1a8GnmuPOO6cwOvjkxkt8Oa84P78N7UFdG8rLKhXItd9wb5yPOBiaLYhf3Bwyx2Oc7xxwJcuMPUxtKe0HbGZf9KVA7GywOwq5AfowuOeP_jyntIP29k0Ii3vHaox_Uf7eon22mr8HFMaE3EFPA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/623461967c.mp4?token=V6ent683uljUt7rVdT_BFgnXI_ENWP7bZKB4KqCOalkv0sFD3D61mpa9CQl_nvfZt8TiEvj5DsRQ-OfTdmWV5_qK1yhoIz6gpZdFzrN1qM1qZ4oVd3U1tW5zNt7BLJGphKv_9KBUXSYq4R1vC30KuBngIPn7BiNPlLHGLD6mXvIh6Hk6_lrPh2Y0cSiOCcPdh5Tt1a8GnmuPOO6cwOvjkxkt8Oa84P78N7UFdG8rLKhXItd9wb5yPOBiaLYhf3Bwyx2Oc7xxwJcuMPUxtKe0HbGZf9KVA7GywOwq5AfowuOeP_jyntIP29k0Ii3vHaox_Uf7eon22mr8HFMaE3EFPA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‌
🔴
منابع عربی: در پی اصابت مستقیم موشک به پایگاهی در بحرین، ستون‌های دود به آسمان برخاست.  @Farsna</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/farsna/452377" target="_blank">📅 01:40 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452376">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">‌
🔴
منابع عربی: وقوع ۳ انفجار شدید پایگاه آمریکایی الجفیر در بحرین را لرزاند.  @Farsna</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/farsna/452376" target="_blank">📅 01:34 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452375">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9fc835bbbb.mp4?token=I5ei8PjxCM-sHvDyCwL_LCcvEruzvLOCKijJibPbHfIh8NA0tFbz4-8EqJQ_9wn6W9OP_UZbzQP2FI-QX9OSHppF3sf48x0H6YfSxchgDAxVp-oUtZwDC_9hasWrKRTP_ebPgzygSDVeJ6iLwqTSHWCDx-RMsZmbhrGWzvo70ZSJf5m63fVSgnY2BzTwcQKPtlNTqnigdeMmNx--w9_u1RTsTQaOk9NuwbIZca3E3DStv3U3z7IjE_4QyRqwwHQijLEjv0w_CTlS3MxpBaIDboCgyGX66HtzX_6HM7pcO0sgkhzBVtdSDfPOWPOKwDfPv_adveyN1ZpRKiGi-msijg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9fc835bbbb.mp4?token=I5ei8PjxCM-sHvDyCwL_LCcvEruzvLOCKijJibPbHfIh8NA0tFbz4-8EqJQ_9wn6W9OP_UZbzQP2FI-QX9OSHppF3sf48x0H6YfSxchgDAxVp-oUtZwDC_9hasWrKRTP_ebPgzygSDVeJ6iLwqTSHWCDx-RMsZmbhrGWzvo70ZSJf5m63fVSgnY2BzTwcQKPtlNTqnigdeMmNx--w9_u1RTsTQaOk9NuwbIZca3E3DStv3U3z7IjE_4QyRqwwHQijLEjv0w_CTlS3MxpBaIDboCgyGX66HtzX_6HM7pcO0sgkhzBVtdSDfPOWPOKwDfPv_adveyN1ZpRKiGi-msijg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
انصارالله یمن ویدئویی خطاب به عربستان سعودی با عنوان «تنش در برابر تنش» منتشر کرد.
@Farsna</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/farsna/452375" target="_blank">📅 01:23 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452374">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gPX6RK93oWpjq7ZCoAUxtAPqw7ehgvrso2axvY-bMSXdP_FNtVrcgmSz0PMnS6zauugbws4gxQL6RrxpLjmcM45ZvrXHZyh6hXvUbWNhxCLN3I2iZChil1wKWh4la0myc26tX-2MOl88-PPiJpFTOhuyA7pajS5wzYL8QBymIamnE-6IVgFhOQ_xf-S8Oe_-aqLgMShSRO9uqgYlHx9T8TvjPGpdHQ3o-kVCFDVe_Zey7wuU4PR-OpZE7CR2J25QM58fOs3f6-XFJyo5fZlb2bnBiLYXE-dh5YM_zIsdQHMHvsXIfQG8V9LMkeh96lKorQkhW9-PS_akuA2gWpyeTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نخستین دستورکار صحن مجلس پس از جنگ تحمیلی سوم منتشر شد
🔹
نمایندگان در روزهای یکشنبه، دوشنبه و سه‌شنبه هفتۀ جاری، به بررسی لوایح و طرح‌هایی از جمله لایحۀ مقابله با جنایات بین‌المللی خواهند پرداخت.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/farsna/452374" target="_blank">📅 01:09 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452373">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">🔴
منابع عربی از حملۀ هوایی عربستان سعودی به بندر الحدیده یمن خبر می‌دهند.  @Farsna</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/farsna/452373" target="_blank">📅 00:55 · 03 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
