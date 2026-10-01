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
<img src="https://cdn1.telesco.pe/file/nAtot4PDcDskHZi0ptuWYzZwG-qiRrg2zDXzYRSQfiW40T_u4hhLtFa2PMEIpGRG0dtNj7XAX792yF0c27x7UfWLiekg__YN1UamBSBoBmGFQbbGPu3PfdLZ0QwkNvjdV-Ng-h5HAdxp7LQdBdwe3MSL1iOwbuUoOdO_ZzyJZCHSZkEves2FZLqtzeohOzdQ4uXWe2dPPYCpgTWCLibRsG-TEMYLpAA_bIcg1D5pWfN9mNRHt0uVMBWcbgfC3Rrrfrqo0k3T-y5jWytmVhjmLJOir6liE76EKSv1bqEXO7eo-V9Eib9hbTMqljeSc-vC3SLincaJ8ldVas1Vq8zf1A.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Matin SenPai</h1>
<p>@MatinSenPaii • 👥 154K عضو</p>
<a href="https://t.me/MatinSenPaii" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 متین هستم و کامپیوتر رو دوست دارم! در حال یادگیری هستم و چیزهایی که یاد میگیرم رو سعی میکنم به شما هم یاد بدم اگر به دردتون بخوره=)ارتباط با من:https://linktr.ee/matinsenpai</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-09 09:45:22</div>
<hr>

<div class="tg-post" id="msg-5456">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/bWU5lIZzVq2_sydpkfCbh8IoveaJ-sVNhod-a6mIuCEAHINT_dMEAoRkVf40Sl6YCxxp-llJPVrB5c-DQ136X-DCee12NB2uM859jM26zbGItJmbTwXwxTY4wYv3JrHbDwhVTRx2FUyrf_AO1KpAOhbDJJ0H6H2U-Xf7_uzl5VMXoY85dXYYTArwCjLaz7Eb4NzVu1of4tr2izgmOlEqijiJDFL09xd9L6onTvztwpNF-JeazLvgWo7EBoqoG_bThoweav28C1MQoeU2dIp9VgnSBLA1Jupc2BHCltabxpbI4a_LE3o8vs3GWj6oV2m_iSDWLQi1NVVb2Vw-_lMvOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این هم به نوبه‌ی خودش عالیه
Hallucination یعنی توهم زدن ai
که این یعنی جمنای 4 به ندرت از خودش یه چیزی رو در میاره</div>
<div class="tg-footer">👁️ 5.42K · <a href="https://t.me/MatinSenPaii/5456" target="_blank">📅 08:35 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5455">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">کلا هر مدلی که میاد
این قضیه‌ی Benchmaxxing پیش میاد
نگران نباشید
میگن توی کدنویسی اونقدر هم خوب نیست انگار و باید منتظر موند و دید تا فردا پس‌فردا که شایعات و تست‌ها به کجا می‌بره ما رو</div>
<div class="tg-footer">👁️ 7.16K · <a href="https://t.me/MatinSenPaii/5455" target="_blank">📅 07:43 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5451">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/NJR4SZyajLQgLfhSncVwiAtaj5tXQAe3gV3cktaRvthVjBmmB0EZLBHqrDUUSGBzVD9RvkseoCDND74mYSso_a1z0nnIA01gbbEfKrJ3yotnaIP4KkFmZtpzrf91IalnrmJ5ZO2GDUzINRQt7S29RthKNof2KFdUP0FlWJ92ryl7nyUGPvlAzccz-3cqKVQ7KCOCJsGDmBaKcsU5T-teT9kmH29j50LxNcQvehyIvDzlhNNrBLtsBSsOmFXFKLlQA0s9x6_RDSqcbtLOxrfDTF7EcN25aUQIt0jBv-w-5s2BlF27s0taavC63yLpl8C2nUj9lg7HoUm4FKY3Ke95xw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/uqMy5pK2Do2A-4AmNqPHrvR9BVwCmD85b8x7deWCaXUhRp7tEdgV9YpnzEmnoPgmtMpRta3pgXwlTUfE_bxH7SSX9_UrIyCGxL2lNGLrC2IxjeIBiLe-NKF274EhWQ8iwWmAwVXqL1OtkUGzGWL6ipvNae44c3cpXeWxoSRJ-bGUIpYwBAhfGGfqDIY5a02o1Mxo58L9Kq4AUbowJ5CC6GmUVy91jpoqKb6w8IRWfH3TWXfJj-cgbpUVjoXC3LM2wNO-8xpf8LDlitj6KMx8WqPm7gAQFkax_Gg8uv43LMEXnthFZgBZByB9fhumsjynkJoZhIcapRMpDIkyHcDaog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/CDFew6PSAqBvCh8-f02Q-aIW5D_3Xsyl3WSqaHZPTKAnn_YBbnKWVhgRmKvpFwr2y1ZGHxsrcdC2ok8Pv4vOQ0pTf3-s9kG6VJhlNv4sKCABF9SejYm8zASxW8cJi8xNcNUX--Y-ZGdKxg7cCFkg46urEi9ODG32fBhkvi1px31dwMbyzNOn_jvupzYWPiVGvwOej7qY3HLUtPkdaNXhG3u2aJvXFWfh5EzHyafa8_DObi9P-Iit1kdKhUFd0-E8iUyvyXbfCaE4c0G8zp6ijkqv7-w9gH5UrpEuhJRQ65Bnw1vbcV-3FtTA_ZUMDf37zXUV1IWe6SQFKTAUwtHvNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/GiIjkJK8Dgjv2vAJx0BKrTNs6zHStXo4bbS9zJ8NAHg4dnRNUQQfe1KaImT0QZlqhs5l7gGAsVTNuQOhwqfs43g8NsjAsWiE0RPFlMuQxNg_vpBN9kwxfkZzER0qaYnxOxB_NVsTjIvuUqBg-s8pTY-phIup-39NEW3uAnXBKn-oEbfhIhY9qHMi6YMmLYyq4I636ZlwkhLjd88_z_gtBvBe8pvEBLQbCHPSLu05ynrWccsPxAsNOx-GowODEsj_pLhJlAf24R4ZAcDCIqtK1JLkztaTZ7sdbaZMlXtp6bn-_xsxH_wRhaOmpaN8l0HCGpXMSEouAEn0riOYmQ1H8w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">گوگل از Gemini 4 Argon رونمایی کرد: تمرکز ویژه روی مهندسی نرم‌افزار و امنیت سایبری  گوگل دیپ‌مایند نسل جدید مدل‌های پیشروی خودش رو با نام Gemini 4 Argon معرفی کرد. این مدل خروجی وحشتناک تا سقف ۱ میلیون توکن(پنجره Context نه ها. Outputای که همیشه 128K بود برای…</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/MatinSenPaii/5451" target="_blank">📅 01:25 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5450">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMatin SenPai(᯽マティ️️ン先輩)</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9eb66b496c.mp4?token=Yr5yiPsw7-Cx_By4yHnpMBe89UWp3b8TeKGHYnOg-Eaw_0yufSrjW_USTcY5GCg1T1SsteM0a41Wp4TExEmeKSe4-h9kkl80yDsQlRutkMRj3f7Bs2bNJJRbkYQVm2m49edBrTecFW7zWudqCGq5i6aswEcRpHM-kgc9mojRCfWRIur6KPP_74Uvc3E_OpyNgBPCjp5WJO7V_5ghJh8LGQ2DIow7tuy2E5veC-gFJhcEVGFC57BB7u7fzLAI2FTe6563rDhSA06PgL9VT4gOT0j-DMYBndDsmvJ_3BwxfLZQ5VVbso77VJqJ94A5JX49J_Ov0g9j-bHu8t4u-GVSOw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9eb66b496c.mp4?token=Yr5yiPsw7-Cx_By4yHnpMBe89UWp3b8TeKGHYnOg-Eaw_0yufSrjW_USTcY5GCg1T1SsteM0a41Wp4TExEmeKSe4-h9kkl80yDsQlRutkMRj3f7Bs2bNJJRbkYQVm2m49edBrTecFW7zWudqCGq5i6aswEcRpHM-kgc9mojRCfWRIur6KPP_74Uvc3E_OpyNgBPCjp5WJO7V_5ghJh8LGQ2DIow7tuy2E5veC-gFJhcEVGFC57BB7u7fzLAI2FTe6563rDhSA06PgL9VT4gOT0j-DMYBndDsmvJ_3BwxfLZQ5VVbso77VJqJ94A5JX49J_Ov0g9j-bHu8t4u-GVSOw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گوگل اون پشت در حال آپدیت دادنای مرموزانه و کار کردن روی مدل‌های Aiاش و بیرون دادن شایعه‌های مختلف:</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/MatinSenPaii/5450" target="_blank">📅 01:11 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5449">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/rezNiVpAwsKjSNkSS0Ijp5vvkc7DVX3YdEyEHvYlwzvxzD1uSr-NCQdI6KWxalALEK9GU3jjdCxpzk2UWzeE4pmKM2n0Sv7wUQnB_H7XjWAAGhFvusxoOfNQdTm4DuDVHtVYHm0oyOgGzCO2bxWaPZ67YatVuFkHrY8SsUzFgAODgMXFCbt34zfeQVOCjplsOqCxUR_xUSQJy7VcFLOVwSZaccr6-Ookomc4F_PY8hiJhHWhkJyYmOnk8HJPsbdYS4jWLgEoef_UqALbejP-KbdADWLhqm1P28CFiy_mLO0thmyWB6Skkaw519ig7uFn06mw5gIDvNxdPdS9geACwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گوگل از Gemini 4 Argon رونمایی کرد: تمرکز ویژه روی مهندسی نرم‌افزار و امنیت سایبری
گوگل دیپ‌مایند نسل جدید مدل‌های پیشروی خودش رو با نام Gemini 4 Argon معرفی کرد. این مدل خروجی وحشتناک تا سقف ۱ میلیون توکن(پنجره Context نه ها. Outputای که همیشه 128K بود برای اکثر مدلا) تولید می‌کنه و توی بنچمارک‌های مهندسی نرم‌افزار (امتیاز ۷۷.۹٪ در DeepSWE v1.1) و امنیت سایبری پیشتاز شده که به زودی می‌ذارمش. آرگون با هدف کارهای سنگین کدنویسی، تحلیل دیتابیس‌های حجیم و کشف خودکار آسیب‌پذیری‌های امنیتی طراحی شده.
هزینه‌اش برای دوره معرفی، قیمت خیره‌کننده‌ی
2$/10$
و بعد از اون،
4$/20$
اعلام شده. با 0.1$(بعدش 0.2$) برای هر یک میلیون Cache ورودی
دقیقا هم‌قیمت با Opus 5.5
باید فردا ببرمش زیر تست ببینم گوگل واقعا پرقدرت برگشت یا هایپ الکیه:)
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/MatinSenPaii/5449" target="_blank">📅 01:03 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5448">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">بیدار شید بیدار شید
جمنای 4 اومدد</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/MatinSenPaii/5448" target="_blank">📅 00:52 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5447">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/kx-0bLitRiZ95J11isgggArG_qcmb7pNf6KnqVh3rCYpVza_fqlMzAwKQ1KJ0yql8UQ3W8Gzg8W7sFGkqlrnQepVSX0uCGT2wtlI4L5JRo5aQBOpuj76RPc6m6CQvq6-xjEXnoCg5DBKJ_ORGFqWUrIWeSsWYWINR4-q1elTdc7ifHkVEPgFkoxotcIST45Dr-ckRjg9cKTuKLL__dD2FgBZxlAPfTfkQKnqj1hUbQJ-rpPt48lHoJ8oWPMoQjK0OvSwFzJoBZi7cuqE5jZWOT_mWDHEi8KzkCQer8hpyhdoZmy3HC4bfgPrU24kaYDdo9LaiftzINn2kIWDOyTOWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کاهش هزینه‌های هوش‌مصنوعی با Auto Router در Cloudflare
کلودفلر قابلیت جدید Auto Router رو به سرویس AI Gateway اضافه کرده. این سیستم توی لبه شبکه (Edge) پیچیدگی هر درخواست رو می‌سنجه و به‌صورت خودکار بهینه‌ترین مدل رو انتخاب می‌کنه؛ یعنی برای پرامپت‌های ساده مدل‌های سبک و ارزون‌تر رو صدا می‌زنه و فقط کارهای پیچیده رو به مدل‌های گرون می‌سپاره تا بدون افت کیفیت، هزینه‌های پردازش به‌شدت کم بشه.
🔗
منبع
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/MatinSenPaii/5447" target="_blank">📅 23:17 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5446">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">من معتقدم با مدلهای رایگان، مدلهای چینی و ابزارهای رایگان هم میشه به خوبی کد نوشت و ابزار ساخت
و به زودی برای اثباتش، یه سری کار انجام میدم
چون میبینم دور و اطرافم کسایی رو که هیچ کاری نمی‌کنن، تلاشی نمی‌کنن، به بهونه‌ی اینکه من اشتراک Claude یا GPT plus ندارم و...
و این کارو انجام خواهم داد که شاید انگیزه‌ای بشه، و شاید ترغیب بشن یه سری افراد که شروع کنن ایده‌هاشون رو بسازن</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/MatinSenPaii/5446" target="_blank">📅 21:10 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5445">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">ویژگی‌ای که Dots و Cues و Grok Bot دارن نسبت به هرمس اینه که اومدن قابلیت‌ها رو محدود کردن!
بله درست شنیدین
همین محدود کردن قابلیت‌ها خودش فیچر خوبی بوده(برای اکثر مردم و برای مارکتینگ خودشون) و باعث شده کارهایی که میشه باهاش انجام داد ساده‌تر به نظر بیاد و سرراست تر بشه. از اون طرف، چون با LLM خودشون سازگاری صد درصد داره، به 99 درصد ارورهای مدل‌ها و api و... بر نمی‌خورید. VPS هم که نیاز ندارید دیگه
اونور قضیه، هرمس به شما "کنترل" و "هزینه صفر(روی لوکال)" میده که اون هم ارزشمنده برای قشر عظیمی</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/MatinSenPaii/5445" target="_blank">📅 16:23 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5444">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">بچه‌ها ما قراره استریم داشته باشیم راجب دانشگاه و انتخاب رشته
اگر سؤالی دارید، می‌تونید به ایمیل matinsdungeon@gmail.com سؤالتون رو بفرستید با Subject استریم
روی استریم می‌خونیم سؤالاتتون و جواب می‌دیم با مهمونای گل</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/MatinSenPaii/5444" target="_blank">📅 14:54 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5443">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/J9-bNHHlfk_pF34iIV1bt2iLgJGLC8K3ke1KoikUewDq1gJLxXZsKQV0AP1DahwgWFy1dfOKmqO5vi-g86lVv4EWWOqk-qTRMrHffE0Tok9SfzhgkMffEWvNQojpRgND8SUKpujkuBrShfFPEhOmuxL3XiVaMAsICVPvIIJcdv_urUwAR-bMPtHQmwCJaoVumS-3LW9cI3mmQ4t3sZreDnYPnkjWND0jK7RZyroo9lzmyRqYMHzJEXQiqpxSrrP72uph4EpYhcNUg4ebetL7ZD-CJeWFaqyIXwmctmDcrxMIx7Fct42zCzJ9gdYZZCBxzl7cpzqIVhO3fT367EKUcg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">همکاری رسمی OpenAI با پلتفرم Hermes
در اعلامیه‌ای جدید، همکاری رسمی OpenAI با اکوسیستم ایجنت هوشمند Hermes(Nous Research) تأیید شده است تا قابلیت‌های مدل‌های جدید و ابزارهای کدکس به شکلی منسجم‌تر در اختیار کاربران و توسعه‌دهندگان این پلتفرم قرار گیرد.
🔗
منبع
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/MatinSenPaii/5443" target="_blank">📅 14:44 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5442">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">بچه‌ها پدی 2500 دلار کردیت OpenAI داره که میخواد باهاش یه اپ بنویسه به انتخاب شما
رأی من زمین بازی سیستم دیزاینه
😂
❤️</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/MatinSenPaii/5442" target="_blank">📅 14:33 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5441">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromPedi | پِدی</strong></div>
<div class="tg-poll">
<h4>📊 کدوم ایده رو با هم بسازیم؟</h4>
<ul>
<li>✓ تمرین انگلیسی با Shadowing</li>
<li>✓ زمین بازی سیستم‌دیزاین</li>
<li>✓ تبدیل کانال تلگرام به وب‌سایت</li>
<li>✓ ایده‌ی خودت رو بگو💡</li>
</ul>
</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/MatinSenPaii/5441" target="_blank">📅 14:33 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5439">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/hGB2PMNSIdxe1zJBZ6X9UBBEsnm9eDqlGY17Kj83A0h_Y2CXCIRFAVn6wiB3pObfQ10z9JJdJ--tUynNvtpxhVYM7VMFf1ig7qgBSC0j6lEsIVjegGKIexOjPP3ySPHOowAm0ykOCiJxberDUSmg3YrKblEF0nwEYbvgaxTktTvjjTg4XDHpdHHd3hoLN3K_iU9tG8N-CwoslgkZxSUK0MBKZWYXugvPwmyGKSy-d16cTMxNjRIkMqtmbLqMKUc_k3aeu1tQbpBv9gR45EabwsjrSj6O7P6yt_whJitMk3IKrjbrsmrUWSs10ra0qs0lmIhVvKZQr_t7IyQOHtMing.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/kgWfmQGC021aueyBcB2hmVOvp4PTMVp-OEDbUWpumQxxjfe-g-MyUfbKzFc6_UP6Cr1CTTvQ0jn8WHobbb5mjWRhHi2OzhV_fOpHIYHFKUE3CHdAMHdRuaAvlX1cz6p4-I6Jj-QroxCtLznpI5Yz-tl6CJJxYfVzP5j_DX4D_gLBcfGQP5eXbO5rQlVGWBMs_NomcFEi-LPgQmD9VSI8gvhQvCwXg3zxU_HfmTLz1gl9GYUDFfZWwl9UoLTdj3Bae1i0c-lqoRQzmwP8MhIJ6pDDuuGRhCHRtIIRomWIbtvdcdGnTD678g_yYdAF-1wZFUIQlJ6NJKJc30AGJW5J9Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">قبلا برای این کار شاید 20 دقیقه زمان می‌ذاشتیم.
پیشرفت ai واقعا عالیه</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/MatinSenPaii/5439" target="_blank">📅 14:28 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5437">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/HavspNSVUJwmDdQe2YiIoBiLsNwastHFquzjwNa_VkR-pV3lqYGvTqyvElfjS-u4LsCPX3gZVeYqpsyYsuYXtxpTkfZ6usw4f73odSRsdBoCtTEXmf5XsC5WqJsF7P6CSeAX4sDEKhUMze2bRn8ge345z9JPgBSm3NaBv2St4qRpaeB3cXeTgZA6UwNo0oo2eSFDwnohkGfxm2Umrm3Ix9XkflzIDkdkqiVFZoXbEL836sYvnxCZls9LkvSPL8C_eaudfrM_ZN_GYMh1UW6USmfrH5ag0gH0lzkQA3R68OySNwPk6AflFETWVWb5zcYtQTJelINcAAxZurafKyVChg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/HqEv2MnqEWfVF7XXfZh3i9jC2SvTOkhQf_YuWC5p0HasNlrFDSVL8gX-Oz2BhBSwdqoiwL-gdBko4UbM8kkuUNGTojrqd0SCX2I8b3W2PS2oBSIytb4zodFnvIfJNajHoh17fR_qIrZJLyGm5SHmzePM4PzYu7dUWXK6rgPGl2j1rqX7SQkorK1LjgKYsvUJMjlopWuVQ3kwxdjUiO2x3qEK5LjWHi82FSdkEz9UXoEi0-KMjfr30urZR81mk2jv6OXVgTAPuu7vp50K0bMfah9T1xiJnkkx2UybPCvjewwp1GTll_TpTMSJTcBK_2BmPGq-5TBlM3dZZoQLw6u9gw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">دیروز Manus پلتفرم Cues رو رونمایی کرد
چند ساعت بعدش، OpenAI از Dots
و طراحی بصری ساب ایجنت‌های بامزشون خیلی شبیه هم دیگه‌ست
😂
نمیدونم چه توطئه‌ای در کاره</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/MatinSenPaii/5437" target="_blank">📅 12:41 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5436">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">گویا همه روی GPT 6.1 Sol مصرف توکن کمتر + قدرت بیشتر تجربه کردن</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/MatinSenPaii/5436" target="_blank">📅 11:34 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5435">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">عرضه نسخه ابری OpenAI Codex در رویداد DevDay
اوپن‌ای‌آی بالاخره بعد از شیشصد سال که رقیبش آنتروپیک این قابلیت رو آورده بود، توی رویداد DevDay بالاخره مدل Codex رو به فضای ابری آورد تا توسعه‌دهنده‌ها محدود به اجرای محلی روی سیستم خودشون نباشن و بتونن از راه دور با گوشی یا هر دستگاه دیگه‌ای ازش استفاده کنن.
🔗
منبع
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/MatinSenPaii/5435" target="_blank">📅 10:03 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5434">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/cd71a513a3.webm?token=PNkqBLz39rNtRP8uL1F0e3_ztdbfad-LEgsOQtkknX7EcnCg5tXCjrOYUlzdD5-N9rVyM1u04WZgtwduFUvzPyNxNqyieq98kV8tZKa6wZmba2YVOGjoVgBIpPb3iqJlJ_MoeTGkNvmSK-nX_ETkLd4JxL544Sf00--kzHIYzqXEi6mFL-tN3x9l_AZZ2_jng6KCRAErpTjucfETxwCoDnyl1h140mKNViN8n6glZzmqP5NE6sutUVaj_TEPAPNvFRgGHmeVzg61T88XVznr6RqqF8hfaC19qcqCvDvsEyBDH3f_qyTjuytGNlTKvqNARXVP6QLfFDVEwGmagrhrCA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/cd71a513a3.webm?token=PNkqBLz39rNtRP8uL1F0e3_ztdbfad-LEgsOQtkknX7EcnCg5tXCjrOYUlzdD5-N9rVyM1u04WZgtwduFUvzPyNxNqyieq98kV8tZKa6wZmba2YVOGjoVgBIpPb3iqJlJ_MoeTGkNvmSK-nX_ETkLd4JxL544Sf00--kzHIYzqXEi6mFL-tN3x9l_AZZ2_jng6KCRAErpTjucfETxwCoDnyl1h140mKNViN8n6glZzmqP5NE6sutUVaj_TEPAPNvFRgGHmeVzg61T88XVznr6RqqF8hfaC19qcqCvDvsEyBDH3f_qyTjuytGNlTKvqNARXVP6QLfFDVEwGmagrhrCA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/MatinSenPaii/5434" target="_blank">📅 08:12 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5433">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">حس می‌کنم یه رقابت خیلی سخت بین سرعت ریلیز مدلهای جدید AI و بالا رفتن قیمت دلار شکل گرفته</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/MatinSenPaii/5433" target="_blank">📅 08:10 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5432">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">خب انگار یه چیز دیگه هم دادن به اسم Dots تقریبا شبیه Muse، یا Grok Bot https://x.com/OpenAI/status/2104984504133918973</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/MatinSenPaii/5432" target="_blank">📅 00:49 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5431">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">مدل Ember-1 از Fireworks: کارایی Kimi K3 با 40% توکن کمتر
تیم تحقیقاتی Fireworks مدل استدلالی Ember-1 رو بر پایه‌ی Kimi K3 منتشر کرد. تمرکز اصلی روی حل مشکل بزرگ مدل‌های reasoning بوده: تکرار بیش‌ازحد مسیر فکر توی خروجی که گاهی بخش اعظم هزینه‌ی توکن‌ها رو می‌بلعید.
چیزی که من خودمم توی ویدئوی کلاد رایگان، سر اون بازی سه بعدی تجربه‌اش کردم و واقعا افتضاح بود. مدل توی thinking خودش گیر میکرد ده‌ها دقیقه.
امبر با بیش از ۵۰ آزمایش و ۲۰۰ ارزیابی جوری آموزش دیده که شاخه‌های غیرضروری استدلال رو حذف کنه و بدون افت کیفیت و دقت کدنویسی، همون نتایج بنچمارک‌ها رو با حدود ۴۰ درصد توکن کمتر تحویل بده.
🔗
منبع
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/MatinSenPaii/5431" target="_blank">📅 00:43 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5430">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">خب انگار یه چیز دیگه هم دادن به اسم Dots تقریبا شبیه Muse، یا Grok Bot https://x.com/OpenAI/status/2104984504133918973</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/MatinSenPaii/5430" target="_blank">📅 22:32 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5429">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">خب انگار یه چیز دیگه هم دادن
به اسم Dots
تقریبا شبیه Muse، یا Grok Bot
https://x.com/OpenAI/status/2104984504133918973</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/MatinSenPaii/5429" target="_blank">📅 22:15 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5428">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/oz8yEuIGxKcQ-i7DnOcobCGeKFC7QLigaFwyBlESC4UQldS6OykuM8C7UK8dQti18oI802Ti8xh1nWfXo81GWj3pt3ROWfUGh9dFVxyaeoFnyLaRM03SyAjFU1yWJ0Y74W7xYqYTDeG-M4GomeNoVNy5Tc69kOGBe3pAZcaGfpyrHPF3MgLM_gAVs_9uLjylfIrRlt89mzROTAL2QBI_RXOIDKu-ljsAhHPmf4xCTtmxZ-IQ8AhVOYBo9lb75bE4bL_CfokOOMQERDPy2BfeyJq9a9RgWKyu3e9DvXxu-qkNBVUx2hKLAXkuNUbhdQZIiC6oosHaO2kdueGrgFT-5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خیلی خندیدم
توییتر OpenAI کلی گفته بود که امروز به مناسبت Dev Day قراره یه چیز خیلیییی خفن بیاد.
کلی توییت زده بودن
هایپ کرده بودن
حالا حدس بزنین چی دادن؟
GPT 6.1 Sol
😂
😂
😂</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/MatinSenPaii/5428" target="_blank">📅 22:10 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5426">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/ubkc2tL822Bo6IZgRHDAEL6PppbhwTmB3wrIgggtRCSTLTE6veDuoA1iGDG73t4WH2g96AFHSzIh9b-TER46lWxtPXUyTWEIksSJxKvhbhG6NuzF7JU8lrnAsGgHFd3kiHNM1R-s0j4lVlaSDiQTyhJWdJWFiLhUYHbION4iSwpgjVnv4dYxVzIT2xVZYbCVt6FZ6DK5RVFMBe7YdfHCLw-njqBpMN5bUCFpMAlj_g8VRNZrVGvl99lKcL8EEZqM72l-fhsoDzI-DIOGIf3xPVy_s7EEGSETxDbNkVDEajBkDoW5EEBBHlz4PT-pVTQd6Wt2i69yWXJElWYgxobD1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/oWDMTXCdaPwqYW2AjDnsZ0APT92GUaaNnlyUjN7qkNLzo36YiLpCJaEb5A8WrCrQ9rCXZ88Qc90Bn_Daj6n-RPZmTPGqEMNDoku5NrluA3NNJ9xgRN3i85jVQOLtFq795JCNDSv2HE-Dx7cBvIAbrjGMWWP1idtzhEFdiMDmnEKszwIJpLPd54AufI9Kk7FKvg3gCZeheD0AKTla8V64GAv1kBKEUWjquTBOuMKjAZP0gDznmrzwDoF6G46nsQ_2dB77y2BBOMsHYTVKkspkma9KYz5Cpgo3pfgCx5eGsJHi2mxRHLki3SR6ZDReM7OLTe4dnUaUm7ySaBD-tlP0Dg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">کلی ارتقاش دادم از دیروز که الان داره با یه مدل خیلی ارزون، کارایی انجام میده که Astra نتونسته بود. یه پنل تحت وب نوشتم براش که اینونتوری رو ببینم، یه مدل سوپروایزر براش گذاشتم که بالای سر پلنر باشه و تصمیماتش رو هدایت کنه، بهش حمله کردن و دفاع کردن مقابل…</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/MatinSenPaii/5426" target="_blank">📅 19:44 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5425">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ZdBhicqChYmo6nDRmpJYFbPyNqa4fwaZR5KXKPBk4cvf-8idsO2hZT7do8phnKCUc0pssUiJ5fNsK0MIs8Px9PWs50Up30g5uNf2NHngV5C_Md4D3DI2SDWSuIoNlIDQstiMRLU1Mrk32qHKT5nt7mbArBUQYDdrx8O14Aagq-ac6fI0wUybyWgNAtIrxvHXYrafw_wlRv1H2dAtzLmfl12qeFSq4B3IskKXHyDew9Eea3IrMB2PKva5DtLlB4TrhGefD7hTiVRm9Spb9DXTvgYwmKwxVrdIxgayAO1kLb9M5x7k1iHhB8ANMjBdLYGqeH4tuzTkFgIxNLapEPvbCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دستیار جدید ماریسا مایر فقط از روی عکس‌های گوشیت می‌فهمه کی هستی
ماریسا مایر، مدیرعامل سابق یاهو، بعد از راند ۸ میلیون دلاریِ seed بالاخره Dazzle رو معرفی کرد:
یه دستیار AI که برخلاف Muse و Instinct، نه خبرنامه‌ات رو می‌خونه نه تقویمت رو؛ کل context از Camera Roll می‌آد. از روی عکس‌ها می‌فهمه چی دوست داری، آخرین سفرت کجا بوده و بچه‌هات به چی علاقه‌مندن.
مثلاً از عکس‌های خود مایر فهمیده خانواده‌اش escape room دوست دارن و چند جایی که نمی‌شناخته پیشنهاد داده
😂
😂
کمی ترسناکه حقیقتا
🔗
منبع
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/MatinSenPaii/5425" target="_blank">📅 18:08 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5424">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">ایده بیزنس: یه سایت بزن و یه ارز الکی بیار به اسم "طلای دیجیتال" قیمتش رو با طلا بالا پایین کن، خالی فروشی کن، و از کارمزدا پول در بیار هروقت هم سودت کم شد یا قیمت زیاد نوسان داشت، برداشت رو ببند و با تاخیر برداشتا رو تایید کن و خودت سود کن این وسط بعدش از…</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/MatinSenPaii/5424" target="_blank">📅 17:14 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5423">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">ایده بیزنس:
یه سایت بزن و یه ارز الکی بیار به اسم "طلای دیجیتال"
قیمتش رو با طلا بالا پایین کن، خالی فروشی کن، و از کارمزدا پول در بیار
هروقت هم سودت کم شد یا قیمت زیاد نوسان داشت، برداشت رو ببند و با تاخیر برداشتا رو تایید کن و خودت سود کن این وسط
بعدش از سودت برای تبلیغات توی کل شهر استفاده کن و دوباره پول در بیار
سرمایه‌ات که رفت بالا و بالاتر و مردم اعتماد کردن، یهو پول رو بردار و دفترات رو هم جمع کن و فرار کن، همه چیز رو هم بنداز گردن بانک مرکزی و فرار کن د برو که رفتیم</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/MatinSenPaii/5423" target="_blank">📅 17:12 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5422">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">در مورد آزمون تورینگ و مقاله‌ی Computing Machinery and Intelligence سرچ کنید و بخونید. جالبه. با اینکه انتقادهای بسیاری بهش وارده که دوست دارم یه روز بشینیم با هم صحبت کنیم راجبش
و دقیقا پرسشیه که اوایل سریال West world مطرح میشه.
"If you can't say I'm human or robot, does it even matter anymore to ask this?"</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/MatinSenPaii/5422" target="_blank">📅 15:34 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5421">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">یه جورایی حس مور مور میده ویدئو
از شدت پیشرفت علم کامپیوتر، اینترنت، ai و...</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/MatinSenPaii/5421" target="_blank">📅 14:18 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5420">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/b452f6f520.mp4?token=oG627_BDzmYHlE3PFpajYxSj3OVB7wIi2j4ErgABPbTLD0K2hnfVupI-WYSQuTYECrz99fxfW5kA6Za3jve0ySbBAlGJXOQ69fxgtWDWkfL8ll9nv-Ppz0RMKrfpPcUqMNLFpIAOVayO_wb6QzJqV6TUoR4-_iOy2T6mzN0XM5O5XxWBfpPnObPIvGLqtAeC6zbUi1Yurg2gm_SPUNa7Kwy58z4q4lybjWyIQXekdoFijKV763Kbg3Szh56HLSlmrlLvjOQHn6QQddefW9JML7MLTPMVvFy7avclwFUWcYG_Yo-_cDUJDNG0oAFfCOtI5thhBF-9Md97rV9IJYllDw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/b452f6f520.mp4?token=oG627_BDzmYHlE3PFpajYxSj3OVB7wIi2j4ErgABPbTLD0K2hnfVupI-WYSQuTYECrz99fxfW5kA6Za3jve0ySbBAlGJXOQ69fxgtWDWkfL8ll9nv-Ppz0RMKrfpPcUqMNLFpIAOVayO_wb6QzJqV6TUoR4-_iOy2T6mzN0XM5O5XxWBfpPnObPIvGLqtAeC6zbUi1Yurg2gm_SPUNa7Kwy58z4q4lybjWyIQXekdoFijKV763Kbg3Szh56HLSlmrlLvjOQHn6QQddefW9JML7MLTPMVvFy7avclwFUWcYG_Yo-_cDUJDNG0oAFfCOtI5thhBF-9Md97rV9IJYllDw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">«کلاد ساننت 5.5 این رو ساخت. فقط با کد»
این داداشمون
این ویدئو رو توییت کرده و اینطور گفته
ویدئو در مورد پرسشیه که آلن تورینگ، پدر علوم کامپیوتر مدرن و هوش مصنوعی چهار سال قبل از مرگش مطرح کرد:
- آیا ماشین‌ها می‌تونن «فکر» کنن؟
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/MatinSenPaii/5420" target="_blank">📅 13:59 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5419">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/3a3bcc7a3f.mp4?token=pNzKGja8Rw5Nl3AaeHUM8aNucI-ZUxACmZOSpKg1kpNMSN5l-KC-RFMjY-tTt-Wdau1-LsrZZWQnbPK4zk0ljjz1j3hcVBdTKfIh2dnbNVNrWuViDsrokdA_fCOqXLl4TqmWLfPRVGHuV_JmX7X2VRdyV7R-IUKo4k2BkHDNCl-iF7xdQr1gi_UhRd9m4iPKCXDgZ0XzHc532-JXnbOdgHwuglZHj3h7oFBnvXLt8ZL229idp6So-pOlLVJ1MkJlWkqU9bcrnmXq-un3y2OCEkxzfLrrOv34DnwzY_ifyq4z9zG5HKQJmFJ_HZI0B1Ye6eQwWt11KK3YsVf68P00mQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/3a3bcc7a3f.mp4?token=pNzKGja8Rw5Nl3AaeHUM8aNucI-ZUxACmZOSpKg1kpNMSN5l-KC-RFMjY-tTt-Wdau1-LsrZZWQnbPK4zk0ljjz1j3hcVBdTKfIh2dnbNVNrWuViDsrokdA_fCOqXLl4TqmWLfPRVGHuV_JmX7X2VRdyV7R-IUKo4k2BkHDNCl-iF7xdQr1gi_UhRd9m4iPKCXDgZ0XzHc532-JXnbOdgHwuglZHj3h7oFBnvXLt8ZL229idp6So-pOlLVJ1MkJlWkqU9bcrnmXq-un3y2OCEkxzfLrrOv34DnwzY_ifyq4z9zG5HKQJmFJ_HZI0B1Ye6eQwWt11KK3YsVf68P00mQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مدل Claude sonnet ۵.۵ توی بنچمارک Terminal-Bench 4.0 نمره‌ی ۷۰.۶٪ گرفت.
بعد این پرامپت معروف بهش داده شد:
«یه کد به HTML بنویس که یه انیمیشن دوبعدی از یه پلیکان سوار دوچرخه رو با گرافیک SVG نمایش بده. نیازی به تست اضافی نیست.»
توی حالت xhigh: یه SVG سالم توی ۴۱ ثانیه، به قیمت ۰.۰۵۷ دلار.
اما توی حالت max: تمام ۱۲۸ هزار توکن خروجی کاملا خرجِ فکر کردن شد، ۱.۲۸ دلار سوخت، و SVG‌ای هم در نیومد.
گاهی سطح Effort/Reasoning بیشتر، فقط یعنی «شکست» با هزینه‌ی بیشتر.
پس الکی درجه‌ی Effort رو بالا نذارید. برای مدلهایی مثل sonnet، همون High-medium کافیه واقعا
🔗
‌
منبع
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/MatinSenPaii/5419" target="_blank">📅 12:22 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5417">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/MfI2OesaThKs1_XgmebnxeMrLZnwlImwsh-VaC69AGZdZqSFqF_RYSxlW0kOmMn6VeH7znAAbkdd048WsDJwGh3kZMApLwqcqYD9nzcTcCY9jhgIJDKmHOMBoG22lZ_RDKDeSQfzK0lfcKbHqay0NF9hGU6S1Fe-W5EQbGQTdsCLL9HbHuajUUBq7lHJG1BdskstqjrSkGrzVmQb0egKFiHTTOpzuD5ILZH16vmtQ-W8QaAbWQM3JSVE_ilkOucf0cN-OKy_6jABOgxSS9p9v7a0kkmHKoXUbAMFRLa0HX_2ooRBa926fS9uMlPyAJdp4hCdz6JMSplziYNw-Bw9qw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/hFZUXk11NeuFJ-qTcpfYbBdsAMv1nRVl5MWJW5MEjXgS80G4-BGGh1p0T7O6kZgLePREoRM6Fca8J0Xg0Sp1ty0hqvEk69oZVH_hugA7ZoYwwebIatiD3IY1Pl7N7FpiZnk8cnCntiA2q14H6CMqXTX6cxeoPSh3IpSkym6OJhfUD1_lrVNpEUGBJMVDzuxT8tI-DF7p-Jp1mK9-5IZFJouKlZhlYetUcBHF9cCahxod8aWrKspShRfhZ9sH2E-GhAl8gx9kH5DA35MzH5yXeXztypD4rnT7EX-4_JQq_UkIJie2JAqsX9s-4GF6rbtG1VViQ_LaWJ-i-dqHycU8Ug.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">با این نسخه از WhiteVPN می‌تونید مشکل فیلترینگ ورکر رو دور بزنید</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/MatinSenPaii/5417" target="_blank">📅 10:32 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5414">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">WhiteVPN-V1.6.10-arm64-v8a.apk</div>
  <div class="tg-doc-extra">38.9 MB</div>
</div>
<a href="https://t.me/MatinSenPaii/5414" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/MatinSenPaii/5414" target="_blank">📅 09:50 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5413">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/o5TIPP6LArpD8sUlSjtGupujI2sPTH6G72pplzxWYknMK0L5Sjd0kcxa8GtYHuF6bbRqwLMuEw02Y9eOJgqz6LqBQUztEGJQWZtgZnvZg0iRspXM5FibK4-t0_EtGmrUy49vcUhL-fAWFyzxjNIdN2UvN3McBSppN4FI7nrRF_zKfzVcAqnZCvtjjspSAXW4iVhnI3GD3VKMxMS4FlqBA6wT0G6hdGilUsmEB9XQrmUbstIqT6lgl-wBruNsxdmHJiQ68QzpHdy6ZIezyKybTIPS_qUvyDZ9mVvCJIpnN0G_gR23NfL0dntj_dy_yR3J449mJkj9hdKAN7GdhJ1RCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
آپدیت جدید WhiteVPN منتشر شد (نسخه 1.6.10)
در این نسخه، مشکل نمایش وضعیت «متصل» در شرایطی که ترافیک در شبکه‌های دارای فیلترینگ شدید از تونل عبور نمی‌کرد، به‌طور کامل برطرف شده است.
تغییرات و بهبودهای این نسخه:
تأیید واقعی اتصال:
وضعیت اتصال تنها پس از تأیید نهایی دسترسی به اینترنت آزاد و پایدار ثبت می‌شود.
سوئیچ خودکار هوشمند:
در صورتی که سرور تنها پراکسی محلی ایجاد کند اما دسترسی واقعی به اینترنت نداشته باشد، برنامه بدون وقفه به سرور پایدار بعدی سوئیچ می‌کند.
بازیابی خودکار اتصال:
بررسی‌های ناموفق مداوم پس از اتصال، مستقیماً وارد چرخه بازیابی و اتصال مجدد خودکار می‌شوند.
ثبات سیستم امنیتی:
حفظ و پایداری رفتارهای قبلی در بازیابی آفلاین و مدیریت خطاهای گواهی (Certificate).
افزایش امنیت اشتراک:
الزام و اعتبارسنجی دقیق لینک‌های اشتراک خصوصی در بیلد‌های رسمی برنامه.
📥
هم‌اکنون می‌توانید نسخه 1.6.10 را دانلود یا به‌روزرسانی کنید.
https://github.com/WhiteDNS/WhiteVPN/releases/tag/v1.6.10
🆔
@Whitedns</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/MatinSenPaii/5413" target="_blank">📅 09:50 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5412">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/a4ZGj1OD3XlQRQ5A3id02ajC9kDqY_XE7ATCPm0niRg7JN17__hrVEWs96MEDyFddu6uhn9D-_gi2ljafsyMF8U4DpmFEwGFMXSYb5oofrcez_vOt2cuNd8MNikd3hrOtEXumTA0sGYCGn-NoyBSHC_YwnqaDGo_6YnwEip_0pK5v7gZ4dZ3RTSvZKBi96ZfNU-9t2sH_Cbptqcer0zPvNjhUwXNlquFO1n7V0XahUWQIy9fCN94-lT-hQlWKbcweo-kTH3yDdVVvrfMsZdQUh6duPnnMpv8Sa25mQjoUxwQmoKf6m24kmR5CtBUy5NgHt1apDRqbanJleljnIoIcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">10
اسکیل برتر OpenCode
جامعه کاربری OpenCode فهرستی از ۱۰ ریپوی برتر Skillها برای ایجنت‌های کدنویسی جمع کردن که شامل پکیج‌های اتوماسیون تست، دیباگ خودکار و سینک شدن با دیتابیس که کار روزمره دولوپرها رو خیلی سریع‌تر و روون‌تر می‌کنه.
(حواستون به SuperPowers باشه که خیلی توکن می‌بره)
🔗
منبع
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/MatinSenPaii/5412" target="_blank">📅 07:47 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5411">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">Matin SenPai
pinned «
اگر کانفیگ‌های کلودفلرتون از کار افتاده، با این روش می‌تونید دوباره زنده‌اش کنید: https://youtu.be/dQKfkXnThCE  به زودی یه ویدئوی آپدیت سعی میکنم واسه اش ضبط کنم
»</div>
<div class="tg-footer"><a href="https://t.me/MatinSenPaii/5411" target="_blank">📅 03:52 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5410">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/pWGJ93kQabHDkFAgE4RR-638cPjhXU7gPGmsVIEbxUsdmJMPhZhf6fRxZQsMTNnMBhmaksLOi4v6E1YTAp__kkTiGtFJgtcbdHzhY5P6eCqfcT26t4JvRmKo3r83rN3AmHJbStMzmy-ZGXu05FeJBW4qzyZ4WhHCQvWcuw7KhjeMSRcaIcLMS__pFUJKaplNgS_ShD67tsCopeH2uxLncD51HOM8QeTpFs_IPH-IZrT9xoU7yhBihXxziSKjJcwYGt12cPN-MOwPtGMBDk07KLw21Yp-VdQOnkGwN4QgHKG8dHOvGvkUFYxbBGxe_szt_-Fh-YihLHmRW5IO0aqtaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این قسمت ویم واقعا بامزست https://v1m.ir/compare</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/MatinSenPaii/5410" target="_blank">📅 03:17 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5409">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/sckO41WOhXSSBunOkjM8OF7Dt04tGahBK-YiPRtyzpOWmjMd30UN13T5VQSGFLVf10kZ-YqFJ95BjdLTBee-tL9GUkOfocu_QtmmhVKEaKG5MTX-fYH9xH1uMeN1cHFr1EgIVFl8gdniz1b75GE-wNDl28sUzoul0z60Dk8YZauHv9fc8dTod0Aggd-46I7MgQcOkh5e1K7wsssGjpGcJyekjg_0BbPVwcoAZjbZsj75bwGhLLZSGlbkRaEsIGioYR5H-__pDGBk68a6xgErPuczFwHi0z9EtJSXQXyG2eIDL4XY13Bqqc7jY3-Hi5TloEKC039ctdMO7JjufWJOfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این قسمت ویم واقعا بامزست
https://v1m.ir/compare</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/MatinSenPaii/5409" target="_blank">📅 00:54 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5408">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">هرمس خوبیش اینه که سمجه. اگر از ترکیب هرمس + مدل رایگان(مثل mimo) استفاده کنید، واقعا غصه‌ی توکن سوزی یا انجام کارهای سختتون رو ندارید</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/MatinSenPaii/5408" target="_blank">📅 23:49 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5407">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">مدل Claude Sonnet 5.5 معرفی شد. هم قیمت با GPT-6 Sol، اما به شدت قدرتمندتر! نزدیک به Opus 5.5  • $2/M input • $10/M output • $0.20/M cache reads 1M context + 128K max output
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/MatinSenPaii/5407" target="_blank">📅 23:01 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5405">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/qK6DuLFnXZ4w2rERZzb5LVssbVBbqWlmzZLNVGKo4SJOSf2hNpav4cVxT1dINX3NlECVevTcRRvcL5eQRHtREolCFfJjKFUGMT3on6gT23N93kUov0wpAFBmVohktM4z2MY18Vq44pVllWbgN_e_Xdsj-Sn-CxCe1HDYzhW0UMYgRcvR_-87qlNLv85j858nu0QoCCqHNc3Y_V5La6DjodFI_ZNfBUTTSIjuykKFGDraU6bMQ-YCTNBLZUOArxQXRJxjm15xmX-PAU-H-U7gXxFHZBLXomzThIc3rdboPOhd9D5S2V44DLHje6SCdyBDchhQHjjk35MLaFIHXsE0nw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/HGhQ2mqgGn3X8c44itKVwK14Xzh4DjpnNw8iSKEYU3MGeEkxCVCqoZG5OO1uZ9v9CuDkcEfRn2RBKnphGpwW_qISBg7esnNcZc16y5SLfHGEvS5dpuVr18HoNqMiZzve2g_2x5NvbO_6fb83xcU-e6GZ9qrIeKMrJAsd4VboYIQ5c9vl2ToOXWGIiK0JCRfy4GBJyxS6PW1Q9KK0s84leUnMmYL1H197kem8gMtbmQctKGcQBWvNICjbf_bYLp7V8IhE-JhBrK4vdV3AQAbYyKL1SOqXhIdiT3D1LhvllmfMd05wIt6vwCPiScJ6oSBSj0Jf8_x6k32zDzTSnwDBsw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">طبق لیک‌ها و یه آیدی تست، امروز و فردا قراره Sonnet 5.5 منتشر بشه و گفتن که از GPT 6 Sol که سر تره، و نزدیک به GPT 6 Astra هست با همون قیمت Sonnet
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 30.2K · <a href="https://t.me/MatinSenPaii/5405" target="_blank">📅 22:22 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5404">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">389 تا ویدئوی ساخته‌شده با Opus 5.5  از موشن‌گرافیک و ویدیوهای توضیحی گرفته تا صحنه‌های ۳D و بازی.  هم ویدیو اصلی و هم ریمیک رو می‌تونید کنار هم ببینید، پرامپت‌ها رو هم مستقیم کپی کنید. https://skillry.dev/ai-videos/opus-5-5
✍️
ai_ba_reza</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/MatinSenPaii/5404" target="_blank">📅 21:30 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5403">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/82410567b8.mp4?token=HdvnuoweLI50do4wqSDjsU8WHTB2EvD8b93eR3WzmWP00QZwo9mxbX6wy15lLxIxUe3NfMKO_PqmAppK9B66CZFWAePfVQUehrrgHUzmG5L2gEXWmyPRzpYpI0kXavP0XtpjED14LyfYUnMjTAz8j0vc5a2NbsbUbQJT3xl6gny62LsS18JQdo4QNNQGhOyhVTMPwqI5eshcXlXwD_Q1kkgjRafyYl84BxWhRqNQwMSk0GOHlO8e5X9Q7UDMODq8SUUJowytU-o_qbm4sYZX4h3_X_BXR8axHdU-o9wYiKJDwjivmf1MWIWOx7B35Tza-Z_0gkJxRFxRh-IE51QQmw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/82410567b8.mp4?token=HdvnuoweLI50do4wqSDjsU8WHTB2EvD8b93eR3WzmWP00QZwo9mxbX6wy15lLxIxUe3NfMKO_PqmAppK9B66CZFWAePfVQUehrrgHUzmG5L2gEXWmyPRzpYpI0kXavP0XtpjED14LyfYUnMjTAz8j0vc5a2NbsbUbQJT3xl6gny62LsS18JQdo4QNNQGhOyhVTMPwqI5eshcXlXwD_Q1kkgjRafyYl84BxWhRqNQwMSk0GOHlO8e5X9Q7UDMODq8SUUJowytU-o_qbm4sYZX4h3_X_BXR8axHdU-o9wYiKJDwjivmf1MWIWOx7B35Tza-Z_0gkJxRFxRh-IE51QQmw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">389 تا ویدئوی ساخته‌شده با Opus 5.5
از موشن‌گرافیک و ویدیوهای توضیحی گرفته تا صحنه‌های ۳D و بازی.
هم ویدیو اصلی و هم ریمیک رو می‌تونید کنار هم ببینید، پرامپت‌ها رو هم مستقیم کپی کنید.
https://skillry.dev/ai-videos/opus-5-5
✍️
ai_ba_reza</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/MatinSenPaii/5403" target="_blank">📅 21:15 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5402">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">اگر کانفیگ‌های کلودفلرتون از کار افتاده، با این روش می‌تونید دوباره زنده‌اش کنید:
https://youtu.be/dQKfkXnThCE
به زودی یه ویدئوی آپدیت سعی میکنم واسه اش ضبط کنم</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/MatinSenPaii/5402" target="_blank">📅 19:34 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5401">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/dNhaKGaCWo8evbW63aAzJpkLfEF0408F3Ef5i921mv7OkRJ0P8gsTn37sJGbKG6XjhnSg1ukHKNE5k4euBHz480l5W0w9zMn3zx85QRhfKs4rOYKvUrgNSJDfPSc_Vfvc9rYXuWSukm-moA40kuoVislBvBYnpE0WZfAH6GMtM_82zP0boLS1b1MMgqA0BMih6vlvX2IDltJsLinf0mhfMmPIkOaFSdt_4p4blzLvwrkjOZX9u5KNv65h9N9EG3M-yQv3WWVJznPNG-NO2jtrYJBfbIoNFPzQ4rrrWPSr42fV6eAvA2NKJMiOXl8NgwT8N8iehZxkN-d3yGsCjo8Sw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حافظه‌ی Hermes: از
MEMORY.md
متنی تا گراف دانش
نویسنده این پست ردیت گفته بودش که مثل خیلی‌ها به دیوار
MEMORY.md
دو هزار و دویست کاراکتری خورده بود (۹۹٪ پر و مدام درگیر نوشته‌های کهنه‌ی توی کانتکست). پس برای همین تصمیم گرفت plugin مربوط به ارائه‌دهنده‌ی حافظه‌ی Hindsight رو توی یه کانتینر Docker جدا راه بندازه؛ بعد از کلی تنظیمات مختلف، اولین اجرا و تجمیع گراف تموم شد.
که این باعث میشه:
1- دیگه محدودیت
Memory.md
رو نداشته باشیم
2- سرعت خوندن از حافظه وحشتناک بالا بره
🔗
منبع
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/MatinSenPaii/5401" target="_blank">📅 19:10 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5400">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/OBnbRifHr08eE6JmP5P-wgwp5AeoHAcCToYTAnRCGICiz92fRm-yeNoxcltKBBzQ8heIqtOqkjiaUvUyz-A_q2eHLgjvop9cq_wAd7aH-1qL47B_lzRtOGkb0EPzUg8YGn5vhPnupmhLGetL3RcX9Agr5uC_lw7gco2Ts7kzFx5vQVOBEW7VGLRaWh02q7P--DdLCI3_r7GmPJjuhWGhphkCyuUiTiQnKTOq3r7VlyEsldADtgUiCcYWstqnmFbWxB36c6JvHseU-zChaJOkhD8R473bUcWDWY9iVhWk6ECl87VJskhWS4GulkaZp7aCWFy5L8c7SQRcb06bgxyKPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فکر کنم گوگل چند صد میلیارد توکن از نسخه 4.6 ساننت و اوپوس خریده برای Antigravity و نمیدونه باید باهاش چیکار کنه
😂
مشتی 5.5 اومد 6 هم به زودی میاد ولمون کن دیگه</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/MatinSenPaii/5400" target="_blank">📅 18:40 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5399">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/YC1mO4YSU9V39Hxfod4z9r3VdiJ0IMSe54uu8gksBh3VWVOdkQCN_uCCHih5qv-6ERuKswORXbzlX8iEf4DorTx1F1g-cuFsUv66WRvJCxoGkgABJfjhU_rIqbxMC7S4ELBRFOQHopEe8-STFAuwtqvk8AdqYFUvHO9UgmCJ3NQomhfi8RgEZTaHqBU1i1qMxHgeQwgGjb6pgaL8zttokx7PTlsYyB-FSJoDFrHvRmeD1aEscavIc5UY9ITQicFT-N9sMDcEzL_f5LXluJhed6-1qxFvNOvfTh0AGVk8_e64yoUxTWJa9YxQvyIBj3N08FeGZkKlQFI7D8uiEymWWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هوش مصنوعی ساخت نرم‌افزار رو آسون کرد، دیده شدن رو سخت‌تر
قبل از AI برای ساختن به توسعه‌دهنده نیاز بود؛ حالا آدم‌های بیشتری همون چیز رو راحت می‌سازن. ولی تعداد کسایی که حاضرن پول بدن، یهو چند برابر نشده. نتیجه: وقتی ساختن برای همه ارزون می‌شه، مزیت واقعی از ساختن می‌ره سمت توزیع، ایده و شناخت مشتری.
🔗
منبع
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/MatinSenPaii/5399" target="_blank">📅 17:50 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5397">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/sYhMEeLBXF6aMUMI6JMFIboSCS0L0pA3FeEmJXa54KLKCl2hzQppicxzi7Qzhj2vqJHNZhD_EGj0oFVnknr4p5oi7LRl1rKkIQ2RLtZ1DQ6pZZUvokQwTjYe0o6CFRe8jDQi3g3uydPQ27_63TQYx4q7eYumCZQh53Q3m7LeAyDj4rjgs5tRP_vtwvBTBvTUZns-z_vsmU1u-X__FBjWLzYC52w6ylHnzGqdSoJDNX9zUYXkDl2LcOGrsozxLhXCY68-qpsg4uJy0eZoP-7h3o8dQjg2ZH0-zbZ-d4kqqOarBGf7l6uzrC1kkK9j4LnJMXdGyds6ql0uWrLNcboGKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/JsIUUYIs1oLW1svZv_XOMnR_y9dsBiBMVHLylo655OeQQV_YnqAT1j9fWbci7jHCGsG6uVTZteWfABzMDCiFmkr84yNnKTqazypliZdqBh8eHrut5Zr9tuNWRVe7kRaxNxfP0SHJu7BRiEMwaCUAj6J0b45wSDpPFnedjfpKXg3kS4sGS-a_YDWfYueEk9_DxBaugKmPBVFH6pvYwFXK9qmFql_b5osQ9ckKyNqiEnTQIa6eteGd1W5VS4PTdRTE8iba69mNTZUYlg3GJnnGHgw_tlDYP1TUZy9YLMXGS-0S7VHe4JoE6QhTAhMIuObhZGuoI2uvDjzxrWwdPytzWA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">این فتوشاپ اوپن سورس که مسخره‌اش کردن یه دوره، سازندش اومد توی ردیت درآمدشو از دونیت‌هاش گذاشت و گفت محصولم خیلی پرطرفدار شده
😂
لینک این فتوشاپ اوپن سورس که اسمش Photon هست:
https://tenzen.studio/photon
لینک پست ردیت:
https://www.reddit.com/r/SaaS/comments/1wsac6d/i_replaced_adobe_photoshop_with_a_free_better/
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/MatinSenPaii/5397" target="_blank">📅 17:31 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5396">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">طبق لیک‌ها و یه آیدی تست، امروز و فردا قراره Sonnet 5.5 منتشر بشه و گفتن که از GPT 6 Sol که سر تره، و نزدیک به GPT 6 Astra هست
با همون قیمت Sonnet
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/MatinSenPaii/5396" target="_blank">📅 16:38 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5395">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromPatt's Channel</strong></div>
<div class="tg-text">محدودیت آپلود
۶
پکت رو دوباره دارن اعمال میکنن.
از چند روز پیش برخی سرورهای شخصی دچار این محدودیت شدن.
از دیشب وبسوکتِ (alpn/1.1) کلودفلر هم برای برخی دامنه ها مثل
workers.dev
.* دچار همین محدودیت ۶ پکت شده.
در نتیجه کانفیگ‌های ورکر کلودفلر به صورت عادی در دسترس نیستند.
با ech ,
fragment+fingerprint
و چندین روش دیگه میشه این محدودیت رو بر روی کلودفلر دور زد.
فعلا تغییری در وضعیت warp هم مشاهده نشده.</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/MatinSenPaii/5395" target="_blank">📅 16:04 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5394">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/RHXBKWP4z3VsI-Vd0tDR4p6ojA6Ms7fRGfcwe9YVHUpTodoTwxJ2vjegiSu8QVm6X2jJ_ybGCwEisuxnBlW4O68lpfcIALpyNbbteVFK2OrRX9Akuza1ss87QACbPYYZnpOQLjqLB_O4CqwUUmQ8GidV3g7bSFG2fq7BvYGMvIMv357SImQULAbNfFZQwDcKf0V6v2S-qmMeIDl3z4QS2wLF705DO6mipelMnPEiTCUUgmWEeeC-R-UtAvr0MCufBYcZFO85X1So9UwZWNQmnVWaYwMWXbYnCTt9RnszvYXTUdGF-W5PtEcS8GhjPuyDSFpCHnesTSw0MRRTN6GVXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رفتیم توی ویت لیست اپ Muse متا ببینم این چیه که همه ازش تعریف می‌کنن</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/MatinSenPaii/5394" target="_blank">📅 15:34 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5393">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/IW4N5X5XwBqSKAma9X0MAxhc4uVmgUJs9EzP_ScIO-wncuT9ddYuBbSuAdJHL6-1TL9ZW_wX27bH7Mtw_hnmVq6OZiD39Epwb1oDQ1SywEIiqqlUI1bA2ZV1Bl9sj09c0HgdeanIIMqbRh1QhjClVyKq7qs8VWoL7y5yqLqUqsoRlZJKpZPruPOgl7S_E4gdugYj1sBuve3atNfmtss0BUG2yblO0zvqFOdHXZhDsOZ6mI8dTNBA_dkprqHiVJfJWkaqXUT_P35vosmxUCUK5aFYwcuy2vdCFVH89h99C2BBNcYKu4dZn1Mj2FXUGXEpHQhzBBqE5Cw96zA-8gncnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بنچمارک خسته‌کننده نمی‌خواید؟ بشینید جنگ مدلها رو ببینید
🤣
سایت TinyAIArena یه صفحه‌ی ۸×۸ هست که چهار مدل توش دارن واقعی با هم می‌جنگن؛ نه یه جدول امتیاز خشک و خالی. روی هر مچ کلیک کنی می‌تونی تماشاشون کنی و ببینی بالاخره کدوم‌شون باهوش‌تره. کل پروژه هم روی GitHub عمومیه. البته این صرفا سرگرمیه و جدی نیست، اما همچنان برای دیدن اینکه مدل‌ها توی یه محیط محدود چیکار می‌کنن بامزست.
🔗
منبع
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/MatinSenPaii/5393" target="_blank">📅 07:54 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5392">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">قضیه‌ی «انسان در حلقه» خودش داره از دور خارج میشه
مارگارت مچل و همکاراش توی یه مقاله استدلال می‌کنن که راه‌حل «انسان رو نگه داریم وسط کار» توی عصر AI، اون‌قدرها هم ساده نیست:
هم طراحی فعلی ایجنت‌ها نظارت مؤثر رو سخت می‌کنه، هم استفاده‌ی طولانی مدت از همین ابزارها، توانایی‌های شناختی خودِ ناظر انسانی رو هم کم‌کم از کار می‌اندازه. پیشنهادشون اینه که نیازهای ناظر رو به‌اندازه‌ی توانایی خودِ ایجنت جدی بگیریم؛ تا هم توی طراحی محصول و هم قضاوت انتقادی تمرین کنه، و هم توی سازمان‌ها با پروتکل‌هایی که اثر اتوماسیون رو جبران کنن.
🔗
منبع
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/MatinSenPaii/5392" target="_blank">📅 23:44 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5391">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromxsfilternet | فیلترنت(امیرپارسا گودمن)</strong></div>
<div class="tg-text">بعد از ماه‌ها که برای کلاینتم آپدیتی ندادم این مدت روش کار کردم و کاملا بهینه و بهبود یافته. UI/UX  کاملا بازنویسی شده با متریال گوگل. و خیلی فیچر های شخصی سازی داره بخش "رابط کاربری" از تمام هسته های حال حاضر پشتیبانی می‌کنه راحت میتونید کانفیگ هاشو اد کنید،…</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/MatinSenPaii/5391" target="_blank">📅 23:26 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5390">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">سندباکس‌های ابری Docker برای ایجنت‌های کدنویسی
داکر سرویس Cloud Sandboxes رو منتشر کرده: محیط‌های اجرای امن و میزبانی‌شده روی زیرساخت خودش، با ایزوله‌سازی microVM توی سطح سخت‌افزار. با یه دستور میشه سندباکس رو بین لپ‌تاپ و سرور جابه‌جا کنیم طوری که فایل‌سیستمش هم منتقل بشه؛ یعنی کار رو محلی شروع کنیم و قبل از خاموش کردن لپ‌تاپ بسپاریمش به کلود. هدف، ایجنت‌هاییه که ساعت‌ها کار می‌کنن و می‌خوایم چندتاشون موازی پیش برن.
🔗
منبع
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/MatinSenPaii/5390" target="_blank">📅 22:39 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5389">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">گوگل امروز صرفا ۶۰ تا اکانت مرتبط با صداوسیما رو به دلیل فعالیت‌های فیشینگ سیاسی و پنهان کردن هویت مسدود کرده</div>
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/MatinSenPaii/5389" target="_blank">📅 16:40 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5388">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dwVVti6wqjUNpCNVQ60cPqyZ9BFGWUo4E9J9BZW3m5I64erMPmtA6R7g8xkrmhm3w47Ykv0iKYaBq8uHpAuhvUyAVWui8xuKt57yQFmP0oCohtjdNvs5jGb-CJPnxn9ailAMl204pDP6RoKgKHVH5hC3Oj3CINHinOIwANJ3PVY1t7X5dT1wA1N6UvgWBcwCqHTAJTLeLym1nJV00BgtlWuC9bMQaCUZ2OK5tW9MTI1HdFCymwv_GmCyzKH8bYUvVFYrXnmduIC0L-x5e78LB_f9QVZ6e9cIeEpRaGVIA-x0NY70mJ0RXAbqAHc_37db2AzLuDpiu4IWHgp4KAciXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کلودفلر بلاگش رو از WordPress کوچ داد به EmDash
کلودفلر جزئیات کوچ دادن بلاگ اصلی‌ش از WordPress به EmDash — سیستم مدیریت محتوای متن‌بازی که خودش داخلی ساخته — رو منتشر کرده. EmDash با TypeScript نوشته شده، روی Worker خود کلودفلر اجرا می‌شه و تا ۷۰۰۰ درخواست در ثانیه تست شده، در حالی که بلاگ معمولا ۷۵ درخواست در ثانیه داره.
🔗
منبع
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/MatinSenPaii/5388" target="_blank">📅 15:37 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5387">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/A3DhvAbD97nx8sWhfgT-wWycCXi7Nv4R2hYO1wAaoDVo0ChmHho2lZMGi9YX0PKnMYYS5_RBuAGhwDX42-40-u9z1MlIMQ8VFlnNk0jOjACaDzk7aApcMtmjxrBad6t66JFh2-DZ5kJEjMyDdgCBX0HtiuXclqeQHurAZSPBO8QCT2SK663XZxL90AqEEUGMpuhBIxqBmIfPeQGC-G0woQf902HmsIAbanlz71xEUEomT81j99A-KbZh5F8stWDBVvODuA0PWCi6aFHROe-Fp7ALJMmLljndTbzBOF64nlrq2eo2oiLYqOpjHZNi40enjXN1OvdPSmWi8wTbPQRFSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چرا حس می‌کنیم هر مدل جدیدی که میاد، انقدر از مدل‌های قدیمی قدرتمندتره؟
باید بگم که این بیشتر از منطقی بودن، «کلک» شرکت‌هاست برای مارکتینگ
اگه یادتون باشه، 2 هفته پیش همه‌ی این بنچمارک‌ها(خصوصا سه بعدی) جوری از GPT Astra تعریف می‌کردن و چیزای خفن می‌ساختن که انگار خدای همه‌ی مدل‌هاست.
بعد که Claude Opus 5.5 اومد، خروجی‌هاش رو جوری نشون دادن انگار اون مقابلش پیامبره.
حالا این قضیه برای هر دوی اونا در مورد Gemini 4 Pro داره تکرار می‌شه
به این کار اکانت‌های بنچمارک و Ai Enthusiast ، قضیه‌ی Strawman Fallacy می‌گن. یعنی مغالطه‌ی آدمکِ پوشالی
توی فلسفه، Strawman fallacy یعنی از رقیب قدرتمندت، یه فرض پوشالی بسازی جلوی مخاطب، شکستش بدی، و بعد خودت رو پیروز جلوه بدی
هم خود کمپانی‌ها، هزینه می‌کنن که اکانت‌های توییتری/ردیتی این کار رو انجام بدن؛ هم خود آدما خیلی وقتا این کارو سر هایپ و ... انجام می‌دن.
چه شکلی انجام می‌شه؟
1- مدل رقیب با پرامپت ساده یا بد تست می‌شه، ولی مدل خودشون با پرامپت بهینه‌شده.
2- قابلیت‌های رقیب مثل reasoning، ابزارها یا context بلند خاموش می‌شه.
3- هایپرپارامترهای رقیب به درستی تنظیم نمی‌شه ولی مال خودشون با دقت tune می‌شه.
این شکلیه که می‌گم هیچوقت به بنچمارک‌های این شکلی توییتری، نمی‌شه اعتماد کرد.
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 31.4K · <a href="https://t.me/MatinSenPaii/5387" target="_blank">📅 14:20 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5386">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mTO1IP5dc0wN9YU2yGNGJmNuKiGnNI-9Azx4tFNQ2BjbHlkG-NX-FwYjDI5Cd2rUzP_JLDZk0a60hIF09RIPe04x-ClZIMyMDMzGL3ETBUH7oBWO2foVKTXdSGFMQeC5mApQSHjPpRQzOFj_9hE23dTMPVqdnBeVuCWCPPoXSJd9wksvEF5gk-3FfwD344ARLairX1fx5NaMXAlFOl-i_0W0SjlceKhECkOQGFYuDcKza0LsKyYZlzUu9SRvZxcY4KVarheOHJn-dgJK4AHBt3ljD6uRtVxlBkLoab3MyrJoO3w8M19dQR8aYBmSEug9dgCkxzWj8lzxSlUtt5Qp6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۱۶ هزار دیتابیس Supabase داده‌های مردم رو لو داده
پژوهش شرکت UpGuard نشون داده حدود ۱۶ هزار دیتابیس میزبانی‌شده روی Supabase بخشی از داده‌های شخصی‌شون رو عمومی کرده: اسم، آدرس، شماره تلفن و گاهی پسورد و توکن.
و بین اینها دیتابیس یه کنسولگری دولتی توی فرانسه هست، پلاک هزاران خودروی یه پارکینگ، و دیتابیسی که برای دریافت رمز یک‌بارمصرف کلاهبرداری استفاده می‌شده. Supabase که امسال به ارزش ۱۰ میلیارد دلار رسیده می‌گه پروژه‌ها پیش‌فرض امنن و امنیت یه مسئولیت مشترکه.
بخشی از ماجرا هم کدهای Vibe Code شده هستن که بدون پیکربندی درست، داده‌های کاربر رو  لو دادن(شبیه یه بنده خدایی که یه بار پروژه اوپن سورس گذاشته بود با به به و چه چه و بعد دیدیم apiهاش توی کد فلاترش هاردکد شده. (طرف مخالف سرسخت ai بود و میگفت به کد ai نمیشه اعتماد کرد)).
🔗
منبع
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/MatinSenPaii/5386" target="_blank">📅 11:07 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5385">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/e71f3ca5cb.mp4?token=JvNNKsTAi5Q4RM5OFWC8FjqsPs6ir86FYJYXzcBUxjihYTnMjrfq4d39lWq2_ajRvLaqumqVk8Gm56Ypj2CZ3TiJh58iBBDKVHcKzd7IFef2LTKAxvG-BzrGk_V7CC2MYWfS0Y8hq7rV192ajQVHU-6YHrw9x1lW_rvjHymv7nuB9tAcvMD1joDmfgdYTks0K59EfX2OXIz7Sm0BGCWSKDIPiDRoHoGMJIPCQf0S5T_ATgnCBZyhTLKN1vTRhz1-yYWy0E8rhFtCteWtXQguT6elf5B7Wppre8Yg1HGVXSP0envloFdjouLwtPIYyIjckM914zgUNBnsclD6udL72yq3Svgh97Pt2hEq_AcMdttRL-xgCfPmO640OTrftPbeKK_77YFV_ezD4OLYaNcWZdPrvcmm66HZ0f5vC4Np_MLO7thCLFbvl3PiWeysjBMk6mzDo_JNiFdWUwxLuuFTymXHSaELPRFzR_nOx4qSpj0fNq0UyJZNDBktS-5tbIXbSzFYbNYFcWOgbkDbcAg-X8o5gcgaZLa32zy_UNEom59DKVN70-AAo6fEth9IWIKIOmKk3EWIc-IdLSbuX-EwjnQNSs6tIxSQmjS5hj7bXSJ8OfKibzp0db2hJKFMHb-8e79Epuyx46EMyU-53f1scYfMLHl-r_DUp_JhLADuY4w" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/e71f3ca5cb.mp4?token=JvNNKsTAi5Q4RM5OFWC8FjqsPs6ir86FYJYXzcBUxjihYTnMjrfq4d39lWq2_ajRvLaqumqVk8Gm56Ypj2CZ3TiJh58iBBDKVHcKzd7IFef2LTKAxvG-BzrGk_V7CC2MYWfS0Y8hq7rV192ajQVHU-6YHrw9x1lW_rvjHymv7nuB9tAcvMD1joDmfgdYTks0K59EfX2OXIz7Sm0BGCWSKDIPiDRoHoGMJIPCQf0S5T_ATgnCBZyhTLKN1vTRhz1-yYWy0E8rhFtCteWtXQguT6elf5B7Wppre8Yg1HGVXSP0envloFdjouLwtPIYyIjckM914zgUNBnsclD6udL72yq3Svgh97Pt2hEq_AcMdttRL-xgCfPmO640OTrftPbeKK_77YFV_ezD4OLYaNcWZdPrvcmm66HZ0f5vC4Np_MLO7thCLFbvl3PiWeysjBMk6mzDo_JNiFdWUwxLuuFTymXHSaELPRFzR_nOx4qSpj0fNq0UyJZNDBktS-5tbIXbSzFYbNYFcWOgbkDbcAg-X8o5gcgaZLa32zy_UNEom59DKVN70-AAo6fEth9IWIKIOmKk3EWIc-IdLSbuX-EwjnQNSs6tIxSQmjS5hj7bXSJ8OfKibzp0db2hJKFMHb-8e79Epuyx46EMyU-53f1scYfMLHl-r_DUp_JhLADuY4w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">+ متأسفم اما AI هیچوقت نمی‌تونه همچین چیزی بسازه. - عاااااشقش شدممم. با کدوم ابزار ساختیش؟ + الکی گفتم. با Opus 5.5 ساختمش
😂
😂
😂
😂</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/MatinSenPaii/5385" target="_blank">📅 09:59 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5384">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/p6bY-Nz21IePaRngIYvhPQMQUQyH2wzIlURYA1meG6Qm142RpyDW_fhs541wpa_mRUWbWyPZJMj7ae1cDx2zc3wi61vSS5K1bZftAc2sCVKBaib0MaBAyTEoOh8vx0xlHA04sriNo7MbyrpkFIzhHs6dbJsjLYZjJ-y9JBqqai9I9gjG9idHJQxKi1g3kgx6ws8INr54D1FLVwt4urt0cBaA-GXGS7M8PrcBuOz-mxvqKCWg9SxUP8qrlywef07xpw8xLHW8WpMKepM2IjjCGhS1igheU3gP5asWCGZ2Iq5iefu6ezGPgXkyfSm0ZLejVJsYs6qGjI5t_eqph6H9aQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">+ متأسفم اما AI هیچوقت نمی‌تونه همچین چیزی بسازه.
- عاااااشقش شدممم. با کدوم ابزار ساختیش؟
+ الکی گفتم. با Opus 5.5 ساختمش
😂
😂
😂
😂</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/MatinSenPaii/5384" target="_blank">📅 09:46 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5383">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NYiOhz4JU6ndiK0z8A26IXXNh7EXS0brChPGKAqKL7x_dgu6Q8BZEnZcA-1lt9wq4ZqRdonSVWqZ6j-m80eyz_JurqigmcW0QpT7PxpRPO4GK_jKfTNMxisM69ZPK1FLM6DUFOlE75HTpode5QKhzKTA2WePRJo1WPngnRlc1JbbnshNkgXwAhWawkSAte9TEq_g_Ky3jI9FqVAq_6F6fQN72kC2JKMGBD0uMJ7xOGOjTn8LH1gYt82eS276ZGvsO2AfUfTVsLLL2mD6YwUHTvYybbF2tYC5tQTSZ3eUdjyB3TdHYe6vzFHmq_RSO-d1TpG3-Hw0c_EMZnApLEDygA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اولایا (Ollaya)؛ مثل Ollama ولی برای مدل‌های تصمیم‌گیری
خود Ollama، اپلیکیشنیه برای اجرای مدل‌های Open Weight روی سیستم خودتون. حالا Ollaya، همون Decision Models که Jev ساخته رو می‌خواد لوکال و متن‌باز اجرا کنه: سوال تایپ‌شده از هر متن یا JSON میدی و جواب کالیبره‌شده رو توی چند میلی‌ثانیه می‌گیری. جواب از یه پاس روبه‌جلو میاد، نه از تولید توکن‌به‌توکن: حدود ۸ تا ۱۰ میلی‌ثانیه برای ۵ تا سؤال روی RTX 4090، در برابر ۲۳۶ تا ۲۷۶ میلی‌ثانیه‌ی API عمومی Jev. با API سازگار با TypeSafe کار می‌کنه، پس SDK رسمیش بدون تغییر وصل می‌شه و مدل‌ها هم همونطور که گفتم، open-weight هستن.
اما یه بحثی که وجود داره، API خود Jev انقدر ارزونه که فعلا من با اینهمه کار باهاش 5 دلارمو هنوز تموم نکردم. لوکال اجرا کردن لایا هم خوبه اما شاید بهترین گزینه نباشه
🔗
منبع
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 30.5K · <a href="https://t.me/MatinSenPaii/5383" target="_blank">📅 07:25 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5382">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/oo11S_yXRYrI3p-zYRJaLwUFG0UwKlmD37IJhfNxSGSycS-2ekZsQoqpQXbQSzDK8Gx3nvsMvPyHKdbuRuqTm8LDfgsLIuZx9E3BxUVuMis3h8CezaaWrsJ-aRJ5XhlD35jKLSQlnw9xvuH7mNEm5IrlSozrre14Lz3eM71fVjkrXh3-Io3qJl9rZp2-lwdljBT6xGVVt3VywCQeV1opWKprID2RzZrJ2obRUyEUKZgV3A7EUpiBkhM_jWxhWbWIccAWg78vyafD3p26pzMdi7GaNWkzIpoe4ZXo9YU3qyt-kZHWj3YZ6rMGylGgkRsUnxNbVUonvsoMSrj9bTfCUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این خبر فیک هست دوستان.
گوگل یهو ایران رو تحریم نکرد. سالهاست ما تحریمیم
گوگل امروز صرفا ۶۰ تا اکانت مرتبط با صداوسیما رو به دلیل فعالیت‌های فیشینگ سیاسی و پنهان کردن هویت مسدود کرده
این خبر هم اشتباهه
می‌تونید ایمیل بسازید همین الان با گوشیتون و نگران نباشید</div>
<div class="tg-footer">👁️ 52.2K · <a href="https://t.me/MatinSenPaii/5382" target="_blank">📅 00:48 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5381">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">تانل با دو سه تا یوزر و سرور قوی هر 40 ثانیه یه بار ریست میشه
معلوم نیست دارن چیکار میکنن
کلودفلر هم اکثرا کار نمیکنه واسم آیپیا با نت همراه. فیبر وضعیتش بهتره</div>
<div class="tg-footer">👁️ 31.9K · <a href="https://t.me/MatinSenPaii/5381" target="_blank">📅 00:26 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5380">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">وضعیت اینترنت خیلی افتضاح شده
هم نت هم VPNهای تانل</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/MatinSenPaii/5380" target="_blank">📅 00:12 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5379">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PO_TLovds3jmvf7qEEWDFrlDlqpyNSpdO94ZgkunwDJY0bzAieXhbMwTJiTnuHY_Z8BXRhxplcuz3WwRqJBONzTObcMLmFK-1Mhn3f288N1i8DG6FKX8VkgLa5buRxmDrSOyyujU9f39hfgK5Lb5-7ziXnSbXmhTy-lIiXzB-ehrTLw__aP4Uap-2Wl4DyXbWzWFYkt9FYpVzgOLgpIAMZZjekjEWhHsu73vsaeDKgGpg4yoEGEEkpLFTkEAcuB4_JufYqzbsoMQm2ublvnivWxhYSebdzQhgjBW0fYNb1LOxIybtbWH_WQv7z6_75VWgAXsSNh46FiG5dzhieZKcg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رابطی رو که توصیف می‌کنید، ایجنت براتون می‌سازتش
گیت‌هاب توی اپ Copilot یه قابلیت به اسم canvases گذاشته: به زبان ساده توصیف می‌کنی چه رابطی می‌خوای و ایجنت یه سطح زنده برات می‌سازه که هم خودت می‌تونی استفاده‌اش کنی و آپدیتش کنی، هم خود ایجنت. هدفش اینه که وقت کمتری رو صرف تطبیق‌دادن با ابزارها بکنی و بیشتر کارت رو پیش ببری.
این کارا فایده نداره گیتهاب جان. پلن‌هات گرون و به درد نخورن
برو این دام بر مرغی دگر نِه
🔗
منبع
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 32.9K · <a href="https://t.me/MatinSenPaii/5379" target="_blank">📅 00:10 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5378">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/lTw0X5MCGVtQyh-EbTbZLZ4cJCpZJzm1fONmls-9_2b5Ax4AeIa9jshOx8Yq6ga66V4Qe1SrAkgWIHCjF4EbtI1lRaplfH-YDfAmklYFCWlm46nVsAa_InR5RyMLzpEfG-XgVzsMDTKg-0PFWSEAqSq-0fnUbulQeGtW815AT_62RLLmiFo7rn6J3-gXmEPpWUHkC0UL_YU-ccTkEjfY-1W_0X5S4elAzRuT3o5Ozz-BFmHP7MFdUm52FKQWCdWbopllzywa2MHoWbDSodaeG4n1rVPw3jdM8pzvYYfOjc1ap07KRUlqDOlMlYd2EMjrlAEdPZ1BopF647pBFYLFwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">(باید برم ببینم کپچا فارمش چطوری کار میکنه)</div>
<div class="tg-footer">👁️ 30.4K · <a href="https://t.me/MatinSenPaii/5378" target="_blank">📅 23:26 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5377">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/BHcwOAH67B0w-efgha3moOjjR3Mpob_yKgw5V9dhOP4XdEvVLB6Xu8gmLulZuYE6jHf7lJaKdfL1z_Nuze-lrdG65HaDHaW0G3o2hegvbmnsq3mkHJNAXboKr8tMcLDBpt0P2pZRnF8xIbxWFaSVn8i18gcDdKfQ9VcVh0zAFZHoUVI9HgIk0d2sTaXpQ98G7F6DxoNU_leLMzrPQQp9eOZkf-Ck4wXhn_gOAdhkPis5vSAy5V6l8LSe8DjWSIoDjnzrLo9-vG7vq4Dvld1p9F9fFPKqFEbkwf-sl15HaASHRsFl4TRzlooDyQ7vHkx6DcYUIZo0Dejy1xHRrJIDYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هر سایتی رو برای ایجنت‌ها به API تبدیل کن، بدون Browser Automation
💪
یکی از توسعه‌دهنده‌ها توی ساب ردیت هرمس ابزاری به اسم
agent-data.dev
معرفی کرده که ایده‌ی جالبی پشتشه.
حرف اصلیش اینه که برای خیلی از کارهای تکراری وب، مثل چک کردن قیمت پرواز هر روز صبح، دنبال کردن آگهی‌های شغلی جدید یا سرچ توی یوتیوب، browser automation رابط مناسبی نیست. ایجنت باید سایت رو باز کنه، بفهمه چی روی صفحه‌ست، هی کلیک و اسکرول و اسکرین‌شات بگیره، و هر بار که لازم شد کل این چرخه رو از اول تکرار کنه. وقتی کار در اصل «این سایت رو با این پارامترها سرچ کن و نتیجه رو بده» هست، خیلی منطقی‌تره ایجنت یه API call بزنه و JSON ساختاریافته بگیره.
حالا این agent-data چیکار می‌کنه؟
1- یه کاتالوگ از APIهای آماده برای سایت‌هایی مثل X، Reddit، Zillow و کلی سایت دیگه داره
2- اگه API مورد نظرت نبود، URL رو می‌دی و توضیح می‌دی چه دیتا یا عملیاتی می‌خوای؛ خودش API رو می‌سازه و نگهداری می‌کنه
3- از طریق HTTP، MCP یا CLI قابل استفاده‌ست، پس برای ایجنت شبیه یه tool call معمولی می‌شه
نکات فنی:
😟
به‌جای HTML selector، endpointها رو روی همون network requestهایی می‌سازه که خود سایت برای لود دیتا استفاده می‌کنه؛ برای همین با تغییر layout کمتر می‌شکنه
📱
خود APIها مرتب تست می‌شن و خرابی‌ها خودکار شناسایی و برای تعمیر صف می‌شن
💰
زیرساخت proxy و CAPTCHA رو خودش هندل می‌کنه(باید برم ببینم کپچا فارمش چطوری کار میکنه)
سازنده‌ش گفته قراره نشون بده این روش در مقایسه با browser automation چقدر سریع‌تر، قابل‌اعتمادتر و از نظر مصرف توکن بهینه‌تره.
🔗
وبسایتش:
agent-data.dev
📌
ردیت
اصلی پست
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/MatinSenPaii/5377" target="_blank">📅 22:24 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5376">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">این ویدیوی موشن‌گرافیک رو با مدل Opus 5.5 برای یکی از دوستان ساختم. و باید بگم با ۲ خط پرامپت و یه ویدیوی مرجع برای گرفتن اطلاعات و متن ویدیو عالی عمل کرد. عالی  حدود ۴۰ دقیقه زمان برد و دقیق ۲ خط پرامپت با چندتا فایل فونت.
✍️
Saeiid</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/MatinSenPaii/5376" target="_blank">📅 21:35 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5375">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/6a18edb9ea.mp4?token=N75u5JzqIfzV9wfLEaGO86yBhVUIlkKGiOG_sAuSXqCUho1WEj6ZD-R5TLun_MpxGYnhw5LMzEW6o9kDvugMtXRIl7ezNGh-qaS2L63a8VLoY6pqBUzcohynDP9YMBQ1GacHL5zDdU0BjoiBGnSZjkOLu-TuntV9qz0bNOoor0CWPOB9xrF33j5bEkQvdX7LjRrDS_r2KwWNXu8BPHINI9R5nq0LxYLsqNSbECuUTd03TKF9z5_3p6jPhglJpSPZ6fNOoqJkaWaYQRwK-ZJH0SC6DfXnGTLGMa09pIuIzG6o3kQzr_gJfPiQHq0nFn6ll3fjE5_JjUXXmuK8OQItAw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/6a18edb9ea.mp4?token=N75u5JzqIfzV9wfLEaGO86yBhVUIlkKGiOG_sAuSXqCUho1WEj6ZD-R5TLun_MpxGYnhw5LMzEW6o9kDvugMtXRIl7ezNGh-qaS2L63a8VLoY6pqBUzcohynDP9YMBQ1GacHL5zDdU0BjoiBGnSZjkOLu-TuntV9qz0bNOoor0CWPOB9xrF33j5bEkQvdX7LjRrDS_r2KwWNXu8BPHINI9R5nq0LxYLsqNSbECuUTd03TKF9z5_3p6jPhglJpSPZ6fNOoqJkaWaYQRwK-ZJH0SC6DfXnGTLGMa09pIuIzG6o3kQzr_gJfPiQHq0nFn6ll3fjE5_JjUXXmuK8OQItAw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هولی شـ... گفتم برای وبسایت MatinSenPai.com هم یه Showreel بسازه با فونتای فارسی و اطلاعاتی که ازم داره.  جداٌ از کارش راضیم</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/MatinSenPaii/5375" target="_blank">📅 20:49 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5371">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/aD-CijuMD9W8gqnSIuBEToCXLoeH20F9DT1jiKUbEIO_msJj8CUqD059YrjEOYGlbrJ3YjA3o4ukpICiV3mQ3YzEdU4SDDi2ej-Yxak5m3xmTexdqhFCpo_H1WEnDdo3dpBzaB0qCkuYJsjtIg-edFQB1h8w05NDD034lwxr-zvWn5y9kgvaPPVSGd28gRc6xdgyqcuI-zNFGwu_EQwIPjY-e0MxmkFBrsXWQ8oZukNR8ypXN6hya8eBsjDH0xh2iN7Lg55sgCCEMIobevc1S_ZRoDe7eYLm4Iy2RDmGF0oXCbMv9d8vg9KU7sYkcnbldSgUfjluNyJaZUyJuBv9MA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/Wsd5qowy0T7o__nn75sLTJbB7kv0UpdTKEaq7OElVlyM00gW4yEe4e2cChN1i56ax40wPS52CeMMAkLWQHyuVCEeOdbDpOsfMh7wbDgp3uTQIC89pXiItysrLPW039aLh6NSzYWd4eSQxmpAbmSuOEGR0EzjpMs530LKoU6RYdYm-KQHxXgAkAQ1xk7OtP5gBvdwOnHq5356givI7Qei3UyazhDMzWNrS4-Gngqm68ITqBszB1czKqxmTwAIG6g7zKTw3hdxpDideTKIMkb_qfcRNVgQH-18vxQvxKP0LLUNmQUTB00JNLboMUYNRx0Uev-rebNJg4ceIQoB0avtxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/d-DWLqt98xn1AyRthOHDC7uxlvEoqmUjjL7SqPrD9PRO3Nmpsbmez4gPL07sdNfzqkDGTbLiJIm4mHcehJMVFw6J-7ek1IjiWWJFC-uLF_21K14I3zWOrtsiV4ZPeYZ_R4IiwIaV4vKP4X1_dP8k3ZLB2g0SM_asp7CV8e1kegBE_NKBau-VAcM9C2pdiS3c8k7NDvjs1EQiKTLMLlJTYdWDVmNjvS5py4YAAwu3-Ek5cPeovf-DRdD18AXlnKph_68VoswZ0H0GCYAVMM3Nn4IV2HJjj3SH8Q1KhdZ02U2ERHaIzErxd4ugaqh6tKQ1G6UXtCZsmCnbHUEWNoG_QA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/Vwo8vB-w3J_1TmyaRfFRtiZVRWtp7UwXFpJkgmFZkndIYEm8ZJBzGZXpldSEmC-KNa8N-sT6PkfOwjS0-UuyUn0MN4X0rfTFNVeTKbfwy6fX43VjFxs-4WN-oy2YxhG75LSvAQcH7Wy1w8HzLX82rj_l-YhQaZP8_61YSmFOr-d9UMB-pe6rtCuWFoy6o-OWyO7W1dp8UwlBnTOcypi9h6TiIM1fEoNXiOqzynpeLvXdoiVSw03CWwJ7llj2bdfTauuNsPdCPVdY3D6Y6JOT7vE30SiRgnmNC1xIAdCDYrZnpFlp9grtV9ZAXcYFvtvQSCYNciSc4JoxuTzmxvBDLQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">اروین از توییتر
یه سایت بهم معرفی کرد شبیه به Mpay، اما بیشتر برای بیزنس‌ها یا کسایی که تراکنش نسبتا بالا دارن؛ با قابلیت برداشت مستقیم از کارت و کارت‌های تبلیغاتی برای کارهای حساس مثل تبلیغات گوگل ادز یا تراکنش‌های سنگین و گرون
از اینجا می‌تونید ثبت نام کنید:
https://finup.io/?code=MATINSENPAI
لینک، رفرال هست. اگر دوست نداشتید میتونید کد آخرش رو پاک کنید. برای شما سود یا ضرری نداره
نقاط قوت:
1- برای ساخت کارت، MasterCard داره به جای Visa(شانس قبول شدن آفرهای رایگان معمولا بیشتره)
2- قابلیت برداشت ازش وجود داره به ولت کریپتو(هنوز تست نکردم که KYC می‌خواد یا نه اما توی مستنداتش چیزی ننوشته بود که احراز می‌خواد یا...)
3- آدرس BIN آمریکا داره
4- از ارزهای مختلف برای واریز پشتیبانی میکنه برخلاف mpay که فقط تتر داشت
5- دو نوع کارت بیزنس و تبلیغاتی(هزینه‌شون یکیه) که کارت Advertising شانس پذیرش بالایی برای کارهایی مثل تبلیغات Adsense گوگل و تیک‌تاک و متا و... داره
6- کارمزد رایگان روی برداشت و تراکنش کارت‌ها
نقاط ضعف:
1- هزینه اولیه ساخت کارت 10 دلار هستش
2- برای KYC شرایط ثابتی نداره اما توی تراست‌پایلت نمره‌ی خوبی داره
3- حداقل هزینه واریز به خود کارت(نه ولت)، 50 دلاره
و اروین گفتش زمان واریز مراقب باشید از صرافی‌هایی که امریکا تحریم کرده نزنید. ترجیحا بریزید توی تراست ولتی، جایی و بعد بزنید به ولت این سایت
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/MatinSenPaii/5371" target="_blank">📅 19:20 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5370">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/39d63885ad.mp4?token=PHqJfmv9yyrvUHa20h3ekF3M3Xf37_t4wfYf_7COY9RZ424NqoiEfFVkCthkFia_zlvWQFoxCgWECuk91NlL5-ZEj-LIZ6RuzGkonmYUFJkr9qslGkPBrU8X5pHub7Sm02lpzzQx-sBowHAIYygBQ_WeGA_vnpVB3zgu6tZIvvJpu1Uz7t0KSipD9h_kurFbT-v62FvIpnPA2cyyVmGiFb3b97XpQ9aUqjflYPZ6G0C-4aBbH-ky3PddKBsCTVexuNBfGxCx9jscEmlMRIRMtsww3S9xzRSbA42mwW4ryTaj6cMfFcxXJBj4tmIwUoWfJEB_272oews2n5LAx-5NnLFtf_NNY4RgyP2p3gUU26BQGMSzKqhUStGpJL7ZN7-Fq_83ZrgwASNWnzgCIfipormM2CQqvzMCLiUizP3Nh5TEdRRysKRC3O3CJK5epn2jrSYhdzeSPyPZcDF-TVP1zKjkuxmlyA4ky6G-c3Wx-JPh-_CeihxGJEm6mK8REPFUHkUzRSaSLv9G8wITtB4CRxvJ4zrd226rBkkmr3RzbtBnkYYG_8YRl-yOxdAu32YmC-Aq4CWdQXH1jbJ48u2fynuTnmyemiuby0kNqFeA122qUqc2Cmv1AJfjXqRF-LxhsUgHdxYYyFTpPHwNHb11hxpAxuBO8A1KOJACTTAzGzw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/39d63885ad.mp4?token=PHqJfmv9yyrvUHa20h3ekF3M3Xf37_t4wfYf_7COY9RZ424NqoiEfFVkCthkFia_zlvWQFoxCgWECuk91NlL5-ZEj-LIZ6RuzGkonmYUFJkr9qslGkPBrU8X5pHub7Sm02lpzzQx-sBowHAIYygBQ_WeGA_vnpVB3zgu6tZIvvJpu1Uz7t0KSipD9h_kurFbT-v62FvIpnPA2cyyVmGiFb3b97XpQ9aUqjflYPZ6G0C-4aBbH-ky3PddKBsCTVexuNBfGxCx9jscEmlMRIRMtsww3S9xzRSbA42mwW4ryTaj6cMfFcxXJBj4tmIwUoWfJEB_272oews2n5LAx-5NnLFtf_NNY4RgyP2p3gUU26BQGMSzKqhUStGpJL7ZN7-Fq_83ZrgwASNWnzgCIfipormM2CQqvzMCLiUizP3Nh5TEdRRysKRC3O3CJK5epn2jrSYhdzeSPyPZcDF-TVP1zKjkuxmlyA4ky6G-c3Wx-JPh-_CeihxGJEm6mK8REPFUHkUzRSaSLv9G8wITtB4CRxvJ4zrd226rBkkmr3RzbtBnkYYG_8YRl-yOxdAu32YmC-Aq4CWdQXH1jbJ48u2fynuTnmyemiuby0kNqFeA122qUqc2Cmv1AJfjXqRF-LxhsUgHdxYYyFTpPHwNHb11hxpAxuBO8A1KOJACTTAzGzw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اینم یه ویدئوی جدید از مقایسه‌ی این مدلی که فکر می‌کنن Gemini 4 هست با GPT 5.6 Astra توی یه انیمیشن ساده(هرچند بنچمارک‌های این شکلی اعتباری بهشون نیست کلا ولی خیلی وقتا درست از آب در اومده این مقایسه‌ها توی قدرت دیزاین و درک سه بعدی)</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/MatinSenPaii/5370" target="_blank">📅 18:45 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5367">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/ad410f0702.mp4?token=LAgSxLclDj6M-driFLnTM4VNJU3psNB1ctDqFGTgJnhIg8fs4qcI5w0zKF88UHJK5MebFocYo-DyH2_RGql6G8fFGG6IYdh9eCE4716hqXZEP4vP7ifbrZKhyMmB5neZNuQs72vjX8LltrwcW1wyDf0jOj9h7FNwXpPEV6MpiSt7uJbJxm4Ub1Vv7c0EpicfIwsw0UbPd_KgIqzRrkKnjQMCQtBrqCmEf6VXcPQ4Miyk8f3FcfOeO4ScwcTPgmQDHGuwRH8w-8DFheztakghhJ0aaq8FnW_pH0uDi-3J9NfO5RY84AYFEA5mY18igjNmb7Q_Y89a3Va_6ug9HJgBDQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/ad410f0702.mp4?token=LAgSxLclDj6M-driFLnTM4VNJU3psNB1ctDqFGTgJnhIg8fs4qcI5w0zKF88UHJK5MebFocYo-DyH2_RGql6G8fFGG6IYdh9eCE4716hqXZEP4vP7ifbrZKhyMmB5neZNuQs72vjX8LltrwcW1wyDf0jOj9h7FNwXpPEV6MpiSt7uJbJxm4Ub1Vv7c0EpicfIwsw0UbPd_KgIqzRrkKnjQMCQtBrqCmEf6VXcPQ4Miyk8f3FcfOeO4ScwcTPgmQDHGuwRH8w-8DFheztakghhJ0aaq8FnW_pH0uDi-3J9NfO5RY84AYFEA5mY18igjNmb7Q_Y89a3Va_6ug9HJgBDQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خب، انگار توی Arena همه جا دارن تست‌های این مدل اخیر رو به جمنای 4 پرو ربط می‌دن و شایعه شده از Opus 5.5 هم بهتره</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/MatinSenPaii/5367" target="_blank">📅 18:13 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5366">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">خب، انگار توی Arena همه جا دارن تست‌های این مدل اخیر رو به جمنای 4 پرو ربط می‌دن و شایعه شده از Opus 5.5 هم بهتره</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/MatinSenPaii/5366" target="_blank">📅 17:37 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5365">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">تیم Tokio نسخه‌ی ۰.۹ فریم‌ورک Topcoat (یه فریم‌ورک فول استک برای Rust) رو منتشر کرده که می‌خواد ساختن اپ وب با Rust رو به اندازه‌ی Ruby on Rails راحت کنه.
توی این نسخه ری‌اکتیوی سمت کلاینت جدی‌تر شده: توی macro مربوط به view سیگنال‌ها و عبارت‌های تایپ‌چک‌شده می‌نویسید که به جاوااسکریپت ترنسپایل می‌شن و توی مرورگر اجرا می‌شن، ولی بقیه‌ی رندر و منطق می‌مونه سمت سرور. نکته‌ی جالب‌تر اینکه نویسنده میگه راست بهترین زبان general-purpose برای دنیای توسعه‌ی مبتنی بر AI هست، چون قراردادهای مشخص به مدل کمک می‌کنه با توکن و خطای کمتری کار کنه.
🔗
منبع
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/MatinSenPaii/5365" target="_blank">📅 17:03 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5364">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/v_vKrcbJvPFfUmzDvJuGyLeyCboxZBKwrnf8i9bHn4tTIAF4U18jSbJ0VmtrBAZdlE3IHmogtLF2V2BsI5FEno_6VwX2tFr5sTQmEbV70VuV2jwGdMwzHUVnkOSNn4DSFeclKOwff7qJgFN7eF82B1RjNNbjNKc-6Sl8IHB_x1YWx6Ur2e3pHcs7mQyVK-wBhgYKQEWoK_MRHu2Mc-CmIp3oLaED0q9rGswT-GgZQPp3Jw-G6mpZZv48cx_-AIA10cLqVD_nH4rGbuhvO84IDHxQoCg-UcAQd7Yu6dVaTKJUXQN-GXdI5uwfMVjDTUPdoJUa-b3wyMLM3s56-LwVNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">با توجه به علاقه گوگل به اسم قناری، خیلی طول کشیدنِ Gemini 4 pro، و چیزای دیگه حدسم اینه که ممکنه گوگل پشتش باشه
کاربرا فعلا گزارش دادن که به شدت کنده...</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/MatinSenPaii/5364" target="_blank">📅 13:28 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5363">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/IZuJ2-dDCUu-nLtOMbLGJHLsTzcvH7V3mtXq8pgctlrlkdqLKdLc6_SFXhgldWfUXmkzkiGqUXap4CiZz_V6sX9-oEpDc68N4hzZcqlV578X21jVE6GFn1Jxsj4fLRxvfmSGHF_VBrvdBsAqDR7ddVyqLgDQffdnIPfcdnpcZ9CnPgo0q8sU98at8I2Nt2Gh_AXK33Y_BMa-GgnTBpZM0zQlvHtEJVTA8jI87u9wRHl_9hwVnt65c__rcoml4cKanJNXKvjhy8FeKR9CQnyWWk1TJHzEs8SAaqOSkW70KQji84eiCbcST0_2za_UWPQh64KvkhKd1DMxkwc0PIbr2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مدل Gemini 3.8 Flash روی Cline رایگان شده آموزش استفاده ازش: https://t.me/MatinSenPaii/5099</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/MatinSenPaii/5363" target="_blank">📅 13:13 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5362">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">زبان‌های برنامه‌نویسی توی عصر AI چی می‌شن و چه بلایی سرشون میاد؟
خوزه والیم، خالق زبان زیبای Elixir، یه مقاله‌ی فکری نوشته درباره‌ی اینکه وقتی ایجنت‌ها بیشتر کد رو می‌نویسن، سر زبان‌ها، ابزارها و کامیونیتی‌هاشون چی میاد.
چند تا نکته‌ی خلاصه از صحبت‌هاش:
۱-
کامیونیتی:
هر زبانی دور یه سری سلیقه‌ی مشترک شکل گرفته؛ پایتون «یه راه واضح برای هر کار»، روبی «خوشحالی برنامه‌نویس»، لیسپ «تغییر خود زبان». وقتی دیگه خودمون کد نمی‌نویسیم، حس تعلق به این کامیونیتی‌ها چی می‌شه؟
۲-
اکوسیستم:
فاصله‌ی اکوسیستم‌ها کم می‌شه، چون پورت کردن کتابخونه‌ها یا پیاده‌سازی الگوریتم‌های یه مقاله با ایجنت خیلی ارزون‌تر شده و زبان‌های کوچیک‌تر سریع‌تر به بزرگ‌ترها می‌رسن. ولی از اون طرف، وقتی ساختن یه کتابخونه ارزون باشه، چرا کسی بیاد روی یه کتابخونه‌ی مشترک همکاری کنه؟ خودش به ایجنت می‌گه دقیقاً همونی که لازم داره رو بسازه.
۳-
سینتکس:
سینتکس‌های خوشگل (مثل optional chaining به‌جای چند تا null check) دیگه اولویت نیست، چون ایجنت از boilerplate خسته نمی‌شه و از دیدش همه‌چیز توکن ورودی و توکن خروجیه. به نظرش زبانی که ادعا کنه «برای ایجنت‌ها ساخته شده» و تمرکزش روی سینتکس باشه، داره حول محدودیت‌های امروز مدل‌ها طراحی می‌شه.
۴-
کامپایلرها از بین نمی‌رن:
اینکه ایجنت مستقیم اسمبلی بنویسه منطقی نیست؛ کسی نمی‌خواد برای هر معماری یه نسخه‌ی جدا نگه داره. تازه هیچ زبونی توی همه‌چیز خوب نیست؛ Rust، زبان‌های اثبات قضیه مثل Lean، Erlang/Elixir برای سیستم‌های توزیع‌شده، SQL، هر کدوم تضمین‌ها و سطح انتزاع خودشون رو دارن.
۵-
تضمین‌های قوی‌تر:
اگه ایجنت کد می‌نویسه، می‌شه trade-offهای زبان رو بازنگری کرد. مثلاً type inference برای آدم‌ها خوبه چون نوشتن تایپ حوصله‌سربره، ولی ایجنت حوصله‌اش سر نمی‌ره. نوشتن صریح تایپ‌ها اطلاعات بیشتری به کامپایلر می‌ده و دست زبان رو برای تایپ‌سیستم قوی‌تر باز می‌ذاره. به نظرش زبان‌ها در آینده با این متمایز می‌شن که چقدر تضمین می‌دن: از طراحی‌ای که حالت نامعتبر رو غیرممکن کنه، تا تایپ و اثبات، تضمین‌های runtime، و تست و fuzzing.
۶-
دیتابیس برنامه به‌جای LSP:
پروتکل LSP برای IDE و آدم‌ها طراحی شده و با فایل و خط و ستون کار می‌کنه، که ایجنت‌ها دقیق دنبالش نمی‌کنن. پیشنهادش اینه که اطلاعاتی مثل سیمبل‌ها، رفرنس‌ها و call graph به شکل یه دیتابیس با زبان کوئری در دسترس باشه. آدم حال نداره برای پیدا کردن رفرنس یه تابع کوئری بنویسه، ولی ایجنت راحت می‌نویسه، حتی کوئری‌هایی مثل «همه‌ی مسیرهایی که یه مقدار می‌تونه nil بشه». برای همین هم جادوهایی مثل monkey-patching که کد رو غیرمحلی می‌کنن، بیشتر مشکل‌ساز می‌شن.
۷- در نهایت
Observability به‌جای دیباگر:
breakpoint گذاشتن و خط‌به‌خط جلو رفتن کار آدمه. ایجنت می‌تونه سریع کد رو instrument کنه، trace جمع کنه و اطلاعات رو کنار هم بذاره. پس باید runtime و state سیستم رو جوری در اختیارش بذاریم که بتونه برنامه‌نویسانه کوئری بزنه، حتی روی پروداکشن. اینجا هم طبیعتاً یه اشاره به Erlang VM می‌کنه که این قابلیت‌ها رو از اول داشته.
جمع‌بندی خودش: زبان‌ها قرار نیست از بین برن، ولی سؤال اصلی عوض می‌شه. اگه دیگه برای «آدمی که کد می‌نویسه» بهینه‌شون نکنیم، برای چی بهینه‌شون کنیم؟
🔗
منبع
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/MatinSenPaii/5362" target="_blank">📅 12:01 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5361">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">AI
فقط یه ابزار نیست
نویسنده‌ی brettcodes از این جمله‌ی تکراری خسته شده که «AI فقط یه ابزاره، مهم نحوه‌ی استفاده‌شه».
استدلالش هم ساده‌ست: ابزار یعنی دریل‌برقی که کسی ادعا نمی‌کنه ده درصد شانس نابودی بشر داره و اگه برعکس بچرخه خرابه.
اما AI یه صنعته، یه محصول اشتراکیه که قیمتش بالا می‌ره و مدلش بازنشسته می‌شه، رهبرهاش مدام حرف‌های عجیب می‌زنن و پشتش مراکز داده و منابع عظیمه. به گفته‌ی اون، تکرار این شعار فقط داره مسئولیت استفاده از یه فناوری خطرناک رو از بین می‌بره.
🔗
منبع
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/MatinSenPaii/5361" target="_blank">📅 10:37 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5360">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iMvKcDJNmN8mjiMHOdytBu7kW7DOJqtNUzW9oxZRYxh2bCkQHhHUlxFVT0q-J3qN-SNUSaCqmxJoOPzgqKUHaZKapHdoaWGCchSp_-9iTMNmNCEZRn32LONGscWjewfalTEe-hr1PvLSuYfvamlU1RuEovZauD61ay8hrbihKoE3X-KV53HAntELclKKMGC8KbmrDIjjUiCz-c2dtHvfVG2-rpP3udz7jABEX-ev84dlBwAKDsxf2qXmFIWtNx9Rr3uOoLS948RmtF3cjatiuzNij_LZrbOntM-PQRrzftqtvxg4z8q9gXIr-aOO97Qxp8IsfleR0vCuVe6e8gVsMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کلودفلر وارد بازی میشه تا ایجنت‌ها امنیت سایت‌ها رو به درستی تأمین کنن
مشکلی که کلودفلر دیده اینه: خیلی‌ها ویجت Turnstile رو نصب می‌کنن ولی اعتبارسنجیِ سمت سرور رو جا می‌اندازن و عملا سایتشون برای بات‌ها باز می‌مونه. Turnstile Spin یه جریان کامله که به ایجنتِ کدنویسیِ شما اجازه میده هر دو طرف ماجرا (ویجت و فراخوانی Siteverify) رو پیدا کنه، برنامه‌ش رو بده، منتظر تأییدتون بمونه و بعد انجامشون بده. از داشبورد، Wrangler یا یه URL مهارت شروع می‌شه و اتصال‌های ناقص قبلی رو هم تعمیر می‌کنه.
🔗
منبع
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/MatinSenPaii/5360" target="_blank">📅 07:22 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5359">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">هولی شـ... گفتم برای وبسایت MatinSenPai.com هم یه Showreel بسازه با فونتای فارسی و اطلاعاتی که ازم داره.  جداٌ از کارش راضیم</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/MatinSenPaii/5359" target="_blank">📅 23:25 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5358">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">واوووو چه باحال
😲</div>
<div class="tg-footer">👁️ 31.4K · <a href="https://t.me/MatinSenPaii/5358" target="_blank">📅 22:44 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5357">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">هولی شـ... گفتم برای وبسایت MatinSenPai.com هم یه Showreel بسازه با فونتای فارسی و اطلاعاتی که ازم داره.  جداٌ از کارش راضیم</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/MatinSenPaii/5357" target="_blank">📅 22:34 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5356">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">اینم موشن گرافیکی که Claude Opus 5.5 ساخت توی 18 دقیقه هیچ ابزار خاصی هم نصب نبود جز ffmpeg و اینم پرامپتش: make a dynamic 15-second motion graphics video that shows what an incredible motion designer you are, like it's your showreel for a résumé. go all out.…</div>
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/MatinSenPaii/5356" target="_blank">📅 22:31 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5355">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">اینم موشن گرافیکی که Claude Opus 5.5 ساخت
توی 18 دقیقه
هیچ ابزار خاصی هم نصب نبود جز ffmpeg
و اینم پرامپتش:
make a dynamic 15-second motion graphics video that shows what an incredible motion designer you are, like it's your showreel for a résumé. go all out.
که یه کم بالاتر داده بودم.
روشی هم که ساختتش اینه:
۱. هر فریم فقط تابعی از زمانه
کل ویدیو یک فایل HTML به اسم showreel.html هست که یک تابع renderFrame(t) داره. این تابع زمان رو به ثانیه می‌گیره و همون لحظه رو می‌کشه. هیچ حالتی بین فریم‌ها ذخیره نمیشه و حتی موقعیت ذرات هم مستقیم با فرمول از t حساب میشه. به خاطر همین میشه هر فریمی رو با هر ترتیبی دقیق رندر کرد. تیکهٔ «Rewind» هم ساده بود: فقط renderFrame رو با زمان‌های قبلی صدا زدم.
۲. حرکت‌ها از چند اصل کلاسیک انیمیشن میان
- Easing: فرمول‌هایی مثل outExpo برای ورود تند، outBack برای کمی رد شدن از مقصد و outElastic برای حالت فنری.
- Squash & stretch: نقطه موقع افتادن کشیده میشه و وقتی به زمین می‌خوره پهن میشه.
- Anticipation: قبل از جمع شدن شکل، اول یک لحظه بزرگ‌تر میشه (inBack).
- Stagger: حروف و ذرات هرکدوم با کمی تأخیر نسبت به قبلی حرکت می‌کنن.
- Motion blur ارزون: به جای نقطه، برای هر ذره یک خط از موقعیتش در t - 0.02 تا t کشیدم.
۳. تکنیک هر صحنه
- ذرات: کلمهٔ «FLOW» رو روی یک canvas مخفی نوشتم، پیکسل‌هاش رو نمونه‌برداری کردم و هر پیکسل مقصد یک ذره شد.
- سه‌بعدی: بدون هیچ کتابخونه‌ای. چرخش و projection پرسپکتیو رو خودم با فرمول ریاضی نوشتم.
- مایع: با metaball ساخته شده و داخل یک WebGL shader اجرا میشه. هر حباب یک میدان r²/d² داره و جایی که مجموع میدان‌ها از ۱ بیشتر بشه، سطح مایعه. نورپردازی براقش از روی گرادیان همین میدان حساب میشه.
- جلوه‌های نهایی: یک shader دیگه chromatic aberration، grain فیلم، vignette و فلش رو روی تصویر اضافه می‌کنه. شدتشون به ضرب‌آهنگ‌ها وصله.
۴. صدا هم کامل با ریاضی ساخته شده (audio.mjs)
هیچ فایل صوتی آماده‌ای استفاده نشد:
- Kick: یک موج سینوسی که فرکانسش سریع پایین میاد.
- Clap و hi-hat: نویز سفید که فیلتر شده.
- Reverb: با چند delay که بازخورد دارن ساخته شده.
- Sidechain: صدای بیس موقع هر kick کم میشه تا ضربه‌ها گم نشن.
- زمان‌بندی صدا با تصویر یکیه (۱۲۰ BPM، هر بیت نیم ثانیه)، برای همین همه‌چیز روی ضرب می‌شینه.
۵. رندر نهایی (render.mjs)
اسکریپت Chrome رو بدون پنجره (headless) باز می‌کنه و برای ۹۰۰ فریم (۱۵ ثانیه × ۶۰ فریم) renderFrame رو صدا می‌زنه. هر فریم به صورت PNG مستقیم به ffmpeg فرستاده میشه و ffmpeg اون‌ها رو با صدا به MP4 تبدیل می‌کنه.
۶. کنترل کیفیت
وسط کار فریم‌هایی از هر صحنه رو رندر کردم و کنار هم گذاشتم تا ببینم. صحنهٔ سه‌بعدی زیادی کشیده و شلوغ شده بود، برای همین طول ردّ حرکت و زمان‌بندی تبدیل شکل‌ها رو کم کردم تا واضح بشن.
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 31.2K · <a href="https://t.me/MatinSenPaii/5355" target="_blank">📅 21:28 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5354">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">بعد از Opus 5.5 واقعا دردناکه به هر چیزی که GPT 6 Astra طراحی می‌کنه نگاه کنی.  به هر دو مدل دقیقاً همون پرامپت رو دادم: "make a dynamic 15-second motion graphics video that shows what an incredible motion designer you are, like it's your showreel for a résumé.…</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/MatinSenPaii/5354" target="_blank">📅 20:42 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5353">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/EfBui-lHgduy3yF0D0NVHmm5MmXV1WB4Ecn4CpjoXv2DNy_jfN8bGqzSEodXZTcrhqX60zlfRvd1fkNcl4pqzTPNbBwKK4CBh6bUmoqv7KUcH5DKsUvWSREG3rzvfEtcQnkPOzhGm9IeCHhx0A-Jg0hGddx8tAujhvGBNeoXC1OgAeEB7WkfPukRyJlHLbZnzdhAWEeVlANp3YO8wfw0iFBDKv2Mq06Ek5q68aeCTuyFIFa396ZL9r60cZ2LXOUgfT9XyVUiHSETkOyba9w_Z8uK4NGtEn6BOgaTvPzaKUAt64YFl6kQhJ0xxk5EEP296U0dR5XJKQVI6C4sWkCP8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خب خب خب
کارهای جالبی قراره اینجا انجام بدیم:)
matinsenpai.com
فعلا لندینگه. به زودی لانچ می‌شه</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/MatinSenPaii/5353" target="_blank">📅 20:26 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5352">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">بعد از Opus 5.5 واقعا دردناکه به هر چیزی که GPT 6 Astra طراحی می‌کنه نگاه کنی.  به هر دو مدل دقیقاً همون پرامپت رو دادم: "make a dynamic 15-second motion graphics video that shows what an incredible motion designer you are, like it's your showreel for a résumé.…</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/MatinSenPaii/5352" target="_blank">📅 19:02 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5351">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">بعد از Opus 5.5 واقعا دردناکه به هر چیزی که GPT 6 Astra طراحی می‌کنه نگاه کنی.
به هر دو مدل دقیقاً همون پرامپت رو دادم: "make a dynamic 15-second motion graphics video that shows what an incredible motion designer you are, like it's your showreel for a résumé. go all out."
آسترا حتی نزدیک هم نیست؛ خودتون ببینید. GPT اینجا صادقانه بخوام بگم، فاجعه‌ست، OpenAI کلا بدسلیقه‌ست.
✍️
shneural
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 30.2K · <a href="https://t.me/MatinSenPaii/5351" target="_blank">📅 16:31 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5350">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mnhStTtIpSLzra0UXszJAeIqd0KzI_Yacsol6td-QL2uHklVqEGjRlJGKAKCOvTqfxX1xLDWbbKWqlUrORaIk5RbgP67MRXspm0NirEGK4VZ1HU_ZtEZduew6O_5gkty86rmvKFsWSMiKmMqGeL7qlxETWO5ByNjWddTl5ZMEzXlkPBkA2J7idqVPRnMEDBb5_R6gjPtw7yUiHGY2Q4abItUrJdW2QGk3caS7w3BefKctMthMJ9NYPodtim08Q1Ucf5ljRBjdvboIZGCEDhpHr6cJqpwIx3CZGRZ8Px0RsbQUyOMKx3lHw6YwFk2fFWjentvN-uyRwq6rk0wEiT7SA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بازبینی کد با Jev؛ Diff خام دیگه در کار نیست
یه ابزار متن‌باز که پی‌آرهای پرحجم ایجنت‌ها رو به جای نمایش خام دیف بر اساس اولویت دسته‌بندی می‌کنه: فقط تغییرهای P0 پیش‌فرض نشون داده می‌شه و بقیه P1 و P2 هستن. توضیح تغییرها به زبان طبیعی نوشته می‌شه، لوکال اجرا می‌شه و چیزی هم به گیت‌هاب نمی‌فرسته.
🔗
لینک ابزار
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/MatinSenPaii/5350" target="_blank">📅 15:33 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5349">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/o6-me03lzDdBy1sPyLT_VvGq43iiJbKff2FeQc7dnF1P65PdWUByu7mqf8pD6m7QpMQs5Xlntl7J6p8mc54j4coaa46CkaaCp_wOnRO_DWZeJ5LWTspjREzAnoaggUdnJCKvALD3ij-qMfS1dINnNaqGf3Raz0lIT4f7LnuZI157mejeRp_9sLtroRDcfMZ9aqgegkSNVu7REzr3K0OV8RRcQQcRIMPj9dEDp8B7WT1dXCir_bfOqzU0yF9FCxgnljdwFm-sT5A2P8Z9i66TUa7uqpuk2NliIZPXY72OqevKL6u9zEFXynmVT_8nvcSnBqp--3Sc_2NW388NEp9tww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آموزش استفاده‌ی رایگان از GLM-5.3 Flash توی 9Router:  با این روش، با هر جیمیل روزانه می‌تونید حدود 15 میلیون توکن مصرف کنید.  1- خود 9Router رو که اینجا آموزشش رو دادم باز می‌کنید 2- وارد پروایدر Cline میشید. دقت کنید، Cline Pass نه. خود Cline 3- این مدل رو…</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/MatinSenPaii/5349" target="_blank">📅 14:19 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5348">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B9IJElrEimwcXWyJXNB4SbZmc4iAzvRL0zbhnWIHXAYoE2soEbjaWasvVPBuey6UtNNyiYMQ_i3nuL0RF-EXIxy4rfGbAOKzRsEY1AV_l_ui_-3Xvit1Ey5xHbIzC_kG-AEX0kdStu-_PJnr21krOK1AxCq70qA0KBQKbz13Ejn1EI-ACCVZW4P-ZUnTFVhtkaaxJtSgdp_KiX81K8SAqfSB5ICr5Xs6doiSzSGKyDQHPRKBFWUWFR-sqMVgsmEHRgHQS4nVgf3shqyzV-Yj6kxVE_v-lvNeCQ_PWsE_8efQojq_UvY972e7ELa1x-fCaFR6HWJagRhkWUBJh1wewg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسکریپت‌سی؛ تایپ‌اسکریپت اما بدون موتور جاوااسکریپت
ورسل لبز کامپایلر آزمایشی scriptc رو معرفی کرده که تایپ‌اسکریپت رو بدون نود، V8 یا هر موتور جاوااسکریپت دیگه‌ای به فایل اجرایی نیتیو تبدیل می‌کنه. نوع‌سنجی با خود کامپایلر تی‌اس انجام می‌شه و خروجی می‌تونه C یا WebAssembly باشه. نتایج اولیه استارت‌آپ سریع‌تر و مصرف حافظه کمتر نسبت به نود رو نشون میده، هرچند سرعت اجرا هنوز پایین‌تره.
🔗
منبع
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/MatinSenPaii/5348" target="_blank">📅 13:14 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5347">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">https://youtu.be/qNYT3eoyJ-c</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/MatinSenPaii/5347" target="_blank">📅 12:10 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5346">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">ویدیوهای بلند بالاخره هماهنگ می‌مونن
ریسرچ گوگل یه فریمورک مولتی ایجنتی معرفی کرده که ویدیوهای بلند چندپلانه می‌سازه و جلوی عوض‌شدن ظاهر شخصیت‌ها توی هر پلان رو می‌گیره. لایه‌ی هماهنگ‌سازی روش Gemini و Veo سواره و SynthID هم داره. چهار فریمورک به اسم Co-Director، CANVAS، A²RD و VQQA پشتش هست که دو تاشون توی COLM و EMNLP 2026 چاپ می‌شه.
به نظر قراره ویدئوهای هلو و پیاز و عشق آبدار رو قوی‌تر بسازن وقتی این تکنولوژی اومد
😂
🔗
منبع
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/MatinSenPaii/5346" target="_blank">📅 11:38 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5345">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/nKxsBycbpNHpQp9EAvNOrDJLDPRpjVpD8LZYI9Fz8USLqMjBI4DawU-UjYDrViMn1ZxjrTlIpwko3I5v_KvOSxTqCQ1nXW6bOCJaHAjLUOXk3jSzjJAewhvb_saf0V3lQBfgvZ-q9sjs093n540Y_xGE-mD96chmGn72WTAhIDuHs_XiXMv8qJpYkBilgED114BWANHIfMOJDTty76Y22RiMVwsBzJ1Jia1_A-r9Szgapa4Z5Ock_P22k872hjbwMlP_dDHsKeCEGzMYsuTJM8vOOb-EMKWw9DE4LmfdGNnWa0BQi4rUQzH63P4Nyi9G8fNu-ZQhN-12aYamBf2Ogg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بنچمارک آرنای توسعه‌ی وب مدلهایی که اخیرا ریلیز شدن.
طبیعتا Opus 5.5 با این هزینه، صرفه‌ی اقتصادی خرید پلن کلاد رو خیلی بالاتر برده. و نمره‌ی پایین Luna 6 توی ذوق می‌زنه حقیقتا. اختلافی با Qwen3.8 27B لوکال نداره:)
که آفرین به برادران چینی</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/MatinSenPaii/5345" target="_blank">📅 07:29 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5344">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">مصرف Opus 5.5 به طرز عجیبی پایینه و همه توی کامیونیتی ایرانی و خارجی هم دارن میگن.
خودمم که دیروز توییت زده بودم راجبش.
روی پلن 20 دلاری هستم تازه و اصلا تموم نمیشه به این راحتیا</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/MatinSenPaii/5344" target="_blank">📅 00:26 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5343">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/1cccff5f95.mp4?token=YpGpz8frPe3YDnza90yiFehdDFczbHBhHCyU_5uJBbLId3WqV4Ls37-GdKBtlwQufJHmiuGn5QFZ8Gc-KdsKjdsY1H9D8RzUjF10X6s-cGxELmy3f4JKhnnmtb8tXTH3YEJVz5AGF4CJiYijSl7mRKIQ5nrqblh-Hx2yySLDxR6OuLUNanWxQ6FkSRD25lIj5_TXO6sz8BKK410HnAepIBdhDim9GYlekuoOBm7M6kpuLQuTiLQ3t1QelTBugGrzQxlzyCpS2F_jqjFE3inBgTfVJ_cdbVVJxGsGDutcGMn6wOaYwocgF82TiWJLmozyZbUxFNJOKZITjfbwxeETPg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/1cccff5f95.mp4?token=YpGpz8frPe3YDnza90yiFehdDFczbHBhHCyU_5uJBbLId3WqV4Ls37-GdKBtlwQufJHmiuGn5QFZ8Gc-KdsKjdsY1H9D8RzUjF10X6s-cGxELmy3f4JKhnnmtb8tXTH3YEJVz5AGF4CJiYijSl7mRKIQ5nrqblh-Hx2yySLDxR6OuLUNanWxQ6FkSRD25lIj5_TXO6sz8BKK410HnAepIBdhDim9GYlekuoOBm7M6kpuLQuTiLQ3t1QelTBugGrzQxlzyCpS2F_jqjFE3inBgTfVJ_cdbVVJxGsGDutcGMn6wOaYwocgF82TiWJLmozyZbUxFNJOKZITjfbwxeETPg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خب، Jev از زمان عرضه داره روی GitHub منفجر می‌شه و همهههه راجبش حرف می‌زنن؛ و اینا چیزای باحالیه که مردم تا حالا باهاش ساختن و شما هم می‌تونید بسازید:
- پروژهjev-trader — ربات معاملاتی واقعی که سفارش‌های limit زنده روی هر بلاک ۳۰۰ میلی‌ثانده‌ای Monad می‌ذاره و فقط Jev تصمیم می‌گیره. ۱,۹۱۱ استار
github.com/jarrodwatts/jev-trader
- پروژه jev-ultrafast — ایجنت مرورگر که هر کلیک رو خودش انتخاب می‌کنه و فقط وقتی واقعا باید تایپ کنه، مدل متنی صدا می‌زنه. ۱۶,۷۵۸ استار
github.com/browser-use/jev-ultrafast
- پروژه jev-doom-agent — Chocolate Doom واقعی کامپایل‌شده به WebAssembly؛ دو موتور روی یک نقشه، Jev هر فریم تصمیم تاکتیکی کلان می‌گیره.
github.com/lukaske/jev-doom-agent
- پروژه jev-t-rex-runner — همون دایناسور کرومه که هممون هزار بار بازیش کردیم، حالا کامل توسط Jev بازی می‌شه: بپره، خم شه، یا ادامه بده.
github.com/joshlarsen/jev-t-rex-runner
- پروژه‌ی typesafe-chess —خود Jev در برابر یه موتور جست‌وجوی واقعی، دو بازی با رنگ‌های جابه‌جا. موتور جست‌وجو هر دو رو برد، ولی حدود نیمی از حرکت‌ها نظر اولیه‌ی Jev رو وتو کرد.
github.com/TholeG/typesafe-chess
- پروژه jev-drone — یه کوادکوپتر شبیه‌سازی‌شده فقط با دوربین مسیر مانع پنج ایستگاهی رو رد می‌کنه و Jev نیم‌ثانیه‌ای یک‌بار وضعیت رو قضاوت می‌کنه.
github.com/RomanSlack/jev-drone
- پروژه tax-doc-classifier — فرم‌های مالیاتی IRS واقعی رو با دقت ۱۰۰٪ روی ۲۶۱ فرم دسته‌بندی می‌کنه، با هزینه‌ی تقریباً ۰.۰۰۱ دلار هر صفحه.
github.com/kyotofin/tax-doc-classifier
- پروژه killmyidea — ایده‌ی استارتاپی‌ت رو توصیف کن، Jev از هر زاویه‌اش امتیاز می‌ده و بعد kill، fix یا ship برمی‌گردونه.
github.com/monteduro/killmyidea
- پروژه jev-curate — ردیف‌های Parquet و JSONL رو با قضاوت‌های typed با سرعت ۱,۵۰۰+ ردیف در ثانیه پردازش می‌کنه و فقط چیزایی که از حد رد بشن نگه می‌داره.
github.com/AkashPriyadarshii/jev-curate
- پروژه pg-jev — افزونه‌ی PostgreSQL که بهت اجازه می‌ده به Tableهای خودتون سؤال انگلیسی ساده بپرسید و جواب واقعی بگیرید.
github.com/realZachi/pg-jev
✍️
imryven
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 32.3K · <a href="https://t.me/MatinSenPaii/5343" target="_blank">📅 22:04 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5342">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/X35uUKtz7KgauZDG4Wbcy3f7DkGU99unQtg6NGs3rKfM63We35QpVCpI8ZbNoESa7n3ypeLF7KOgSsfF_hfaP5ABBA1YPq-vIvedbgtra8_DiShi4UVxhpPqVDoy81b0sOnvql-bs7dzMPDBB7vEKdGGXCATpOtsG68bTpVAsDgG4GlJV58j52hrB_wtZhlU1I4RdP49CEWfScMDzMXnKpEWWDzK1oolL2IJumzoCBiQe5jjRrXG9vJkSO2QgkjylDrYT5ZrSBmMM4sFTUeUuvypE5q3g-mdJ_qm3J_GxpuV9n9logJslUbuOx827I5oo-S79fA_sRcjG0NhMbGycg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">«داداش اینا که AI بود»؛ ناسزا جدید نوجوونا
😂
گاردین نوشته تحقیرآمیزترین عبارت امسال بین نوجوون‌ها شده «That's so AI». یعنی وقتی می‌خوان بگن یه چیزی جعلی و بی‌کیفیته اینو به کار می‌برن. جالب اینجاست که بین عامه‌ی مردم، خودِ AI داره به نماد بی‌اعتمادی به محتوا تبدیل می‌شه، نه فقط صرفا یه ابزار.
🔗
منبع
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/MatinSenPaii/5342" target="_blank">📅 20:26 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5341">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">هکرها چطوری ChatGPT و Gemini رو کردن دستیار کلاهبرداری
🥸
یه تحقیق تازه از Vigilance Security نشون می‌ده یه کمپین گنده (اسمش رو گذاشتن Dark Sourcery) داره جواب‌های ChatGPT، Gemini و Google AI Overview رو مسموم می‌کنه.
قضیه اینه که: کلی پست و PDF و صفحه‌ی پشتیبانی فیک می‌سازن که با تکنیک GEO بهینه شدن، که هوش مصنوعی شماره و ایمیل تقلبی رو جای «اطلاعات رسمی» بهت تحویل بده.
تا حالا دست‌کم ۳۷۴ شرکت قربانی شدن؛ از Fortune 100 گرفته تا Delta و Lufthansa و Bank of America.
چطوری این کار رو می‌کنن؟
1- شماره‌ی فیک رو با فاصله و نقطه و ایموجی می‌نویسن که فیلتر اسپم نگیره، ولی مدل راحت درش میاره
2- شماره‌ی تقلبی رو قاطی شماره‌های واقعی می‌کنن که معتبر به‌نظر برسه
3- محتوا رو فوری می‌نویسن (جابه‌جایی پرواز، قفل شدن حساب) که هول کنی و سریع زنگ بزنی
4- پست‌ها رو می‌ریزن توی LeetCode، اینستاگرام و حتی PDFهای سایت‌های دولتی و دانشگاهی
پاک کردنشون هم فایده نداره؛ کمپین اتوماتیکه و روزی هزاران پست جدید می‌زنه.
بدترین قسمتش؟ Google گفته این خارج از scope‌شونه(
😂
😂
😂
😂
) و OpenAI هم گزارش رو بسته، به این بهونه که reproducible نیست. چون عملاً به سیستم خودشون حمله‌ای نشده؛ فقط خروجی AI دستکاری شده.
۹۱٪ آدم‌ها جواب AI رو چک نمی‌کنن. شما جزوشون نباشید؛ شماره‌ی پشتیبانی رو فقط از سایت رسمی خود شرکت‌ها بردارید
چون به زودی شاهد همچین افتضاحی توی ایران هم خواهیم بود متأسفانه.
🔗
منبع
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 31.9K · <a href="https://t.me/MatinSenPaii/5341" target="_blank">📅 19:25 · 02 Mehr 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
