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
<img src="https://cdn4.telesco.pe/file/B1KCVflu8tBdr83uBTCaRRnKuQp1fHd7l2Mmv1Cwzvpw-y_1_vmj2zk6dU1Cp7EMmZxPpPi6Yr7EFnvXKNcT2PQWroMs5eOZC7JITSKmsKJDcl-ju3Ad5jrE1IW8yaE0frb1zucUyyPV4rpnnBmlPswMrphc8P0aAmAfo2ouDYHDRuSGLz3Xt-7a2teE-6H2IgfZB_MQ6_LxLhRnwkNMXHGPav61IIprmTSpQE1fnFJG3fh3v1ifsjz9Ymd2jwPJAR-Yt4RGmomcouLnoh6HUENrqW6y9B9r3VX5Td9YLK8-a7j9NDdccxHa0j6tk_SE7LTFS6C1wWTBGtkIvkRfhA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرگزاری فارس</h1>
<p>@farsna • 👥 1.84M عضو</p>
<a href="https://t.me/farsna" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 حقیقت روشن می‌شود‌‌تبلیغات@Farsnews_adsارتباط@FarsNewsفارس‌پلاس@Fars_Plus‌ورزش@SportFarsجهان@FarsNewsIntعکس@FarsImagesپیام‌رسان‌ها@Farsnaاینستاگرامinstagram.com/fars_newsتوییترtwitter.com/FarsNews_Agency</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-20 00:48:50</div>
<hr>

<div class="tg-post" id="msg-461322">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">نگرانی آمریکا از مهندسی معکوس زهپاد خود توسط ایران
🔹
بعد از اقدام جمهوری اسلامی ایران در تصاحب یک فروند زیردریایی کنترل از راه دور آمریکایی، واشنگتن نگران مهندسی معکوس این فناوری پیشرفته خود شد.
🔹
خبرگزاری رویترز در این‌باره گزارش داد که ایران احتمالاً زیردریایی…</div>
<div class="tg-footer">👁️ 2.95K · <a href="https://t.me/farsna/461322" target="_blank">📅 00:40 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461321">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس ورزشی</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5869d8727f.mp4?token=ftqocHEun-XUae2v9l28WJzbYK5VDhxfBCiBc9bLy507VqGEshDWx1nuYgTsYpjmPeBIHcCSr-JHNKJfZS0JW7l2G53rECby6_9pSJYYwjqqySorD1BRVhKwpnaLQ9RehgefeSNZ1iC2NFRg126pFq3JwZNOpkS8vSz_1BbTSYuIvYkuzZ_opTtpiSv3khC76HcHSdrn1MPL4UWG9Xh-Ft7j-ngSsY_0aLNaibzT_keaKLV10uKcM2UQt1OjMsHuuXhlAAf3wloRJVjaUKPXr-a3w07WkG2ae3PTyNWllDD8FEZ9mL9QxBekV4TnGdqTqlpUIL21edtXkj_cYujtXkED4OtY12Zrj3v4QM6XBMHwxF640Fy9LUN83-cBjZgPWM13QlY76mc0W5n-RLIALye6nq4ihYIxe-URFRa_HHHx-xSyJeTfHi8XRzNH-PWY6ZPoMzDnvU_1x_6SBnf2U7VLecMT9lTzfvfANjhiXJLHy5uVFoQpFtZKtfMPs3KZ4dhy6f34mCuG1lbtazrRW_9gUPrUxLVEpoYoM-U-_73TWtddsR7o3d_kGkaVprHN5P1rZEdKJzPIqvZh7QLsyty09lwGaKGscnyyoKhYXAVCiT7z3gGh9qtifPY3Tje4TlZ5ALDVPVF2uytnnROmrOuQ0WYIxpMZN6al7QF7ULk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5869d8727f.mp4?token=ftqocHEun-XUae2v9l28WJzbYK5VDhxfBCiBc9bLy507VqGEshDWx1nuYgTsYpjmPeBIHcCSr-JHNKJfZS0JW7l2G53rECby6_9pSJYYwjqqySorD1BRVhKwpnaLQ9RehgefeSNZ1iC2NFRg126pFq3JwZNOpkS8vSz_1BbTSYuIvYkuzZ_opTtpiSv3khC76HcHSdrn1MPL4UWG9Xh-Ft7j-ngSsY_0aLNaibzT_keaKLV10uKcM2UQt1OjMsHuuXhlAAf3wloRJVjaUKPXr-a3w07WkG2ae3PTyNWllDD8FEZ9mL9QxBekV4TnGdqTqlpUIL21edtXkj_cYujtXkED4OtY12Zrj3v4QM6XBMHwxF640Fy9LUN83-cBjZgPWM13QlY76mc0W5n-RLIALye6nq4ihYIxe-URFRa_HHHx-xSyJeTfHi8XRzNH-PWY6ZPoMzDnvU_1x_6SBnf2U7VLecMT9lTzfvfANjhiXJLHy5uVFoQpFtZKtfMPs3KZ4dhy6f34mCuG1lbtazrRW_9gUPrUxLVEpoYoM-U-_73TWtddsR7o3d_kGkaVprHN5P1rZEdKJzPIqvZh7QLsyty09lwGaKGscnyyoKhYXAVCiT7z3gGh9qtifPY3Tje4TlZ5ALDVPVF2uytnnROmrOuQ0WYIxpMZN6al7QF7ULk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
اتهام بزرگ خداداد عزیزی: فدراسیون پول به‌روزرسانی VARهای لیگ را نداده و اصلاً خط آفساید کار نمی‌کند و نمی‌توانند سر صحنه‌های آفساید خط‌کشی کنند و تنها با عکس تشخیص می‌دهند.
@Sportfars</div>
<div class="tg-footer">👁️ 4.89K · <a href="https://t.me/farsna/461321" target="_blank">📅 00:30 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461319">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">ذخایر راهبردی نفت آمریکا باز هم کم شد
🔹
درحالی‌که قیمت نفت امروز به مرز ۱۰۰ دلار  رسید، آمار جدید ذخایر راهبردی نفت آمریکا که لحظاتی پیش منتشر شد نشان می‌دهد که این ذخایر ۱.۲ میلیون بشکه دیگر کاهش یافته و به ۲۸۵ میلیون بشکه رسیده.
🔹
با بسته شدن تنگه هرمز،…</div>
<div class="tg-footer">👁️ 5.85K · <a href="https://t.me/farsna/461319" target="_blank">📅 00:25 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461318">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">حادثه برای دو شناور در نزدیکی سواحل عمان
🔹
سازمان تجارت دریایی انگلیس از وقوع حادثه‌ای برای دو شناور در نزدیکی سواحل عمان خبر داد.
🔹
بر اساس این گزارش، این حادثه در فاصلۀ حدود ۴ مایل دریایی غرب شهر خصب در عمان رخ داده است.
@Farsna</div>
<div class="tg-footer">👁️ 7.14K · <a href="https://t.me/farsna/461318" target="_blank">📅 00:13 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461316">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9264531775.mp4?token=dluU27YPut71SXCbo_uL52jwoMqrtlgVt6stM5NAPCV9gQp15KCbLy5GW_rzoqOY8kQMnnM3KCk0_d6rTG2k5ga6kR4HXXscdtKTZdZWDu4ICXZrnaU-2fI-BRKbvVExenkVAwSqySQa8qy1tBqdyihAUox0boBf9W64tuC35NuitHW25lyd9SN014uUVM8CPF6g8-TnxbojE1CEetjCipPubSmTjSNOdQ2I5hS8XS3SDKVQI0of5dgjYbNPw0ynjrSpeoEqpE3koM7QSMhDa7WTuScEtTTrTP_iLaRMpWIStiaQMrTOAnL7wJ8Q4jNiEROrrkxTkPQHWE5pkochGw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9264531775.mp4?token=dluU27YPut71SXCbo_uL52jwoMqrtlgVt6stM5NAPCV9gQp15KCbLy5GW_rzoqOY8kQMnnM3KCk0_d6rTG2k5ga6kR4HXXscdtKTZdZWDu4ICXZrnaU-2fI-BRKbvVExenkVAwSqySQa8qy1tBqdyihAUox0boBf9W64tuC35NuitHW25lyd9SN014uUVM8CPF6g8-TnxbojE1CEetjCipPubSmTjSNOdQ2I5hS8XS3SDKVQI0of5dgjYbNPw0ynjrSpeoEqpE3koM7QSMhDa7WTuScEtTTrTP_iLaRMpWIStiaQMrTOAnL7wJ8Q4jNiEROrrkxTkPQHWE5pkochGw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
امت مبعوث خستگی‌ناپذیر در شب ۱۹۴ هم حماسه‌آفرین شدند
@Farsna</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/farsna/461316" target="_blank">📅 23:22 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461311">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uUP_V4wly0v6HVMO6xMm5RQ37T6mSEkVqsktaEZJZqCTKKH3pPaLLcKCoytobQMDvAkZaMEo-C4osWf0O0JR6Jr-rmubFhgobryNTXkUnwQnX_d-vx0NKXVRY2cOcIvEFB_ks4ztxlMHDbt53eVE943UXafvSFldvGkdpdydC7kW53Sba2qECV9Y1UPuQYn2sjpfu6tMIbzjJuqfNQM2vso5YBa84JWr5ngXLgEecfUVniRKy6Xihi9-my0wlh3nUAqijI9PrjU--YXbAofwLaKJ3kAUk6RaZ2VrAMJ0N1e1Jr_cq-yDP8Oibx0Vmlbg-nyZ1jAKPFmVIIj0_oD4sQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/AV1zPwG7O7ymqA_zO0REEF-0xVvEwsIp_1lQopZViRdJ2oZvZYsM7p6BI9L_27-Mizf5DBCuuJlsOIHVJUewzUBfc4hUninFvFjFLVg8zeDA8bUbJf3jIR4vDRTOkbaqCnOG0cKtKbLpDYSDqDl5XIU6NJDtisSLBR3tWn8jICVKnD5h2Ir7bxB4rFV8yrPfpLfbLzJ9EpaWgdF37Ka142-_mOnaAYN3Q8bSq1fEvEfmuC2F2uVSkeGjfTbMXQ0UVuTDptezgDPE2GYlNRycnJLTPe7Xq4G3BIDWj7gFixUueffznPDS5YV4N6CDKvf0ec7gRbi0Iu4ovrAzFzp06g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bBOHfsK3jFNG79YTVLxFysLmhH5toqqNTkiJIEnxQ1jbLjVtAemV7Zkh1Egbrpl-rox8tBvsMDlmxwDBu5HSCBkXkuYFUdoRJBU0H2RCASA9EF7wy8hgwxXwxUAeEUpLp63gOOzvt9sYTHeqQkkYSMWWUrfiBExjUh_rCzIcHAOnO9BSdnwmZEMWPgQgTUqRECOYODywyasQ8P3zbuAiZyuNf4JtIaRtXba7kFCvQgxEYFwMhrEUfAiDwMkJTfTpaGZ_V32gniksso0fBI0N2jVHT2xZnI0fRoRex74u_UE_7hHdpjZ2WrASmKNfeLex980SqAOYs182i9nvJo0ejA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VvxRmzx0UcrH2JHTSQ6kVDCsPYV7KL8K7l5SZgGfb5pwok99C8OI8LrRN9er5jNiGeMnQnsRtC11qX4yIJBTlyvEmhGtqM9-TPebXOb7_0E6x4wspcNUwTeSaEf74rCTsTt9eRp5ctVoc1jEvUE3raCbFuuRAsTl3x2EhETUaP0BSFLEC0QIKsHv3IlUqgAJIh-0MAPk4qnmi2SkMp4MJm-LpYjiOBuH2ErGiLzHS6_tRccugyfwLQ7Efu-rsfwPZGJh7PY6qzybo-ecCmoJldY4bmNHqHzcQaCbsZ9r1AlHy8EDfLQjPQXPOh7ziytuMILquOhMiBlU5HapgbAyAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gXBfFr88zCLPOZTWdVqH6X1GoJ0bndfCAoMoTZrLDbANrI5UAu2Vvw8KD34Da71bOEDwQgKKcqGrRnDWGustuOKGcn-C4Sy9KzLMNeWc9Ayh5TXrQMMIKqF9eHOQOxrzjWf9U2ieXUs4m83rFaB8EuIPJespSvo6RNrESY8symkMKJ5vlWTgRqMoKbKfAefU3JlXzG6DSkgYcBzhqZi3-Z6UcJq1lkyYdicqAnN2lvwAELsz3q4NXdoPu-O67aRDjldNCabf3fxRobgh7ln2d_hlXIjnFDtCN3Uoc60cXb5JwIthD3goG4mZujgX5aNutfm12vjpvw7LMW3uQVeXDg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
دریچه‌ای به حیات‌وحش در قلب پایتخت
عکس:
میثم نهاوندی
@Farsna</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/farsna/461311" target="_blank">📅 23:12 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461310">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">پیام‌هایی که شما برای فارس فرستادید
🔹
ما
معلمان حق‌التدریس
با وجود اینکه خود آقای وزیر سال گذشته قول دادند
قرارداد معین
برای ما انجام شود، هنوز این وعده عملی نشده است. اکنون گفته می‌شود دیگر قرار نیست این کار انجام شود، چون نیاز آموزش‌وپرورش به‌تدریج برطرف شده است. زمانی که به ما نیاز داشتند می‌گفتند قراردادمان را درست می‌کنند اما حالا می‌گویند انجام نمی‌دهند. ما عمر و جوانی خود را پای این کار گذاشته‌ایم، اما اکنون هیچ امنیت شغلی نداریم و با حداقل حقوق مشغول به کار هستیم.
🔹
ایثارگران و فرزندان شهدا، فرزندان همین آب و خاک‌اند و شایسته نیست پس از سال‌ها خدمت، همچنان به‌عنوان راننده استیجاری بلاتکلیف باشند. متأسفانه رأی وحدت رویه مورخ ۱۴۰۳/۱۰/۱۱ موجب محرومیت جمعی از
ایثارگران
راننده از
تبدیل وضعیت
شده است. از مسئولان محترم تقاضا داریم برای رفع این بی‌عدالتی و تعیین تکلیف و تبدیل وضعیت این عزیزان اقدام کنند.
🔹
وضعیت
آسفالت ورودی اصلی شهر کرمان
، از بعد از بلوار حجاج تا کارخانه سیمان، بسیار نامناسب است و چهره خوبی به شهر نداده است. مسیر از پل شهید معافی تا پل نعل‌اسبی فرودگاه و همچنین محدوده بین دو دوربرگردان، پر از گودال و خرابی است و خودروها آسیب می‌بینند. لطفاً این موضوع را پیگیری کنید.
🔹
دو سال پیش از شرکت
فردا موتورز
یک دستگاه خودروی SX5 پیش‌خرید کردم و حدود ۶۰۰ میلیون تومان هم پرداخت کردم. قرار بود خودرو طی ۱۵۰ روز کاری و با پرداخت حدود ۱۵۰ میلیون تومان دیگر تحویل داده شود، اما اکنون دو سال گذشته و هنوز کسی پاسخ‌گو نیست. جالب‌تر اینکه وقتی پیگیری می‌کنیم طوری برخورد می‌شود که انگار
درخواست انجام تعهدات قراردادی
، توقع زیادی است! می‌گویند اگر ناراحت هستید، بعد از دو سال پولتان را پس بگیرید. سؤال اینجاست که چرا با وجود انجام نشدن تعهدات قبلی، همچنان پیش‌فروش خودرو ادامه دارد؟ لطفاً مسئولان و نهادهای مربوطه این موضوع را پیگیری و تعیین تکلیف کنند.
🔹
من یک راننده تاکسی هستم. امسال دولت در ابتدای سال
حق بیمه رانندگان
را بیش از ۹۰ درصد افزایش داد. از اول تیرماه نیز ۲۰ درصد دیگر به حق بیمه اضافه شد و طبق اطلاعات سایت تأمین اجتماعی، از ابتدای پاییز مجدداً ۲۵ درصد افزایش در نظر گرفته شده است. خواهش می‌کنم پیگیری کنید این میزان
افزایش حق بیمه
بر چه اساسی انجام می‌شود؛ آن هم در شرایطی که درآمد ما رانندگان به‌دلیل جنگ واقعاً کاهش پیدا کرده است.
🔹
لطفاً مشکلات ما کامیون‌داران را به گوش مسئولان برسانید. یک جفت لاستیک بارز به ۱۴۰ میلیون تومان و لاستیک چینی به ۱۷۰ میلیون تومان رسیده است. با این وضعیت کرایه و درآمد، چطور می‌توانیم یک جفت لاستیک بخریم؟ متأسفانه مسئولان توجهی به
مشکلات کامیون‌داران
ندارند.
🔹
ما ساکن شهر آباده هستیم. فرزندم در مدرسه هیئت‌امنایی تحصیل می‌کند. دیروز برای ثبت‌نام به مدرسه مراجعه کردیم که با درخواست شهریه ۱۰ میلیون تومانی مواجه شدیم. چرا شهریه باید نسبت به سال گذشته دو برابر شود؟ در حالی که سال گذشته هم مدارس آنلاین بود و شهریه را کامل پرداخت کردیم، اما نه برنامه خاصی داشتند و نه کلاس بیشتری نسبت به سایر مدارس برگزار شد. لطفاً
وضعیت شهریه مدارس هیئت‌امنایی
را پیگیری کنید و شرایط خانواده‌ها را در نظر بگیرید؛ مردم توان پرداخت این مبالغ را ندارند.
🔹
لطفاً از شهردار منطقه ۱۵ درباره وضعیت
وانت‌های میوه‌فروش در افسریه
پیگیری کنید. این وانت‌ها به‌صورت قارچ‌گونه در حال افزایش هستند و بیش از نیمی از خیابان‌های اصلی محل را اشغال کرده‌اند و باعث ترافیک شدید در افسریه شده‌اند.
🔹
در میان کارمندان دولت، قشر زحمتکش معلمان به‌شدت مظلوم واقع شده‌اند. بنده ۵ سال سابقه خدمت دارم و با حق مدیریت، کل فیش حقوقی‌ام ۲۸ میلیون تومان است که پس از کسر بیمه و سایر موارد، تنها ۲۲ میلیون تومان به حسابم واریز می‌شود؛ سؤال این است که معلمان با این وضعیت چگونه باید زندگی کنند؟
🔹
من از اهالی
روستای کردیان در شهرستان باخرز
، خراسان رضوی هستم. چند سال است که در فصل تابستان و پاییز با مشکل
کم‌آبی
مواجه هستیم.
🙍‍♂️
شناسۀ ارتباطی ما:
@Fars_ma
@Farsna</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/farsna/461310" target="_blank">📅 22:50 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461309">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">آخرین وضعیت میدانی جبههٔ یمن
یک منبع اطلاعاتی آخرین وضعیت جبهه یمن را تشریح کرد:
🔸
۱. از شب گذشته تاکنون طی پیروزی‌های پیاپی انصارالله در ساحل غربی یمن، مناطق مهم حیث، خوقه، بخا و جزایر حنیش و زوقر به تصرف درآمده و آزاد شده‌اند.
🔸
۲. عصر امروز نیز مناطق ذباب، تنگهٔ باب‌المندب و جزایر استراتژیک میون تحت کنترل مقاومت قرار گرفت.
🔸
۳. هم‌اکنون کل ساحل غربی یمن تحت کنترل مقاومت است و مناطق تصرف‌شدهٔ ۲۴ ساعت گذشته به بیش از ۴۵۰۰ کیلومتر مربع رسیده است.
🔸
۴. شمار زیادی از مزدوران وابسته به عربستان به ویژه نیروهای طارق عفاش به هلاکت رسیده، اسیر شده یا متفرق شده‌اند.
🔸
۵. تنها از ظهر امروز تاکنون عربستان بيش از ۸۰ حملهٔ هوایی به مواضع انصارالله داشته است.
🔸
۶. مسیرهای کشتیرانی به‌طور کامل مسدود شده و قیمت جهانی نفت به‌شدت روندی صعودی گرفته است.
@Farsna</div>
<div class="tg-footer">👁️ 9.68K · <a href="https://t.me/farsna/461309" target="_blank">📅 22:47 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461308">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">گفت‌وگوی تلفنی عراقچی و وزیر خارجۀ عربستان
🔹
عراقچی در تماس تلفنی با وزیر خارجۀ عربستان، دربارۀ آخرین تحولات منطقه گفت‌وگو کرد.
🔹
دو طرف با اشاره به تشدید تنش‌ها و افزایش ناامنی در منطقه، بر ادامه همکاری‌های دیپلماتیک برای جلوگیری از گسترش تنش‌ها و بازگشت…</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/farsna/461308" target="_blank">📅 22:41 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461307">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-text">تلگراف: ایران برای نخستین بار موشک مجهز به حسگرهای اپتیکی را سمت ناوهای آمریکایی شلیک کرد
🔹
مقام‌های آمریکایی مدعی شده‌اند ایران روز چهارشنبه برای نخستین بار از موشک‌های جدید مجهز به
حسگرهای اپتیکی
در تلاش برای حمله به ناوهای جنگی آمریکا استفاده کرده است.
🔹
سپاه پاسداران در جریان حملات شبانه، موجی از حملات را علیه نیروهای آمریکایی در اردن و ۱۰ فروند شناور آمریکایی در نزدیکی تنگه هرمز انجام داد.
🔹
موشک‌های مجهز به
جستجوگرهای اپتیکی
با بهره‌گیری از دوربین‌ها و حسگرهای نوری، اهداف را با دقت بالا شناسایی و ردیابی کرده و به سمت آنها هدایت می‌شوند.
🔹
ایران اواخر سال گذشته میلادی از سامانه موشکی جدید خود رونمایی کرده و آن را
قاسم بصیر
نامیده بود؛ نوعی موشک بالستیک میان‌برد که به حسگرهای اپتیکی مجهز است.
@FarsNewsInt</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/farsna/461307" target="_blank">📅 22:35 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461306">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/87a8860a2f.mp4?token=AjjeyA4NOOWcnbjRQQCLOPtskCf3FEftenaILrsp9dHmcpMxLpvh8Za9Yphdihd1bQ-CYx0bHAad1_GTWKIUiPaFDsW-yA6XDDeCfdV1RK5FhJHDFvaLBf0QoGtxr1jJX6pNY3iHH_1iOy6gmBFicubW_OF7ryIXjnz8VyO794Qgm_Avl-Q0uAssB3xOE2XiCvG-C4cu9b3T9Ryskj_FgYhbAzaDw--PjNcOSmpOW4-JKwptHwfHwOwzhoXgNlsjU16E_Pq9oRqBu5V8jTcbYpPvg0oH9U8Bhc7g79AQdZmnAJMDC79qayfyWBZmaq78_oQyh_MOQo2mni6MRlaujg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/87a8860a2f.mp4?token=AjjeyA4NOOWcnbjRQQCLOPtskCf3FEftenaILrsp9dHmcpMxLpvh8Za9Yphdihd1bQ-CYx0bHAad1_GTWKIUiPaFDsW-yA6XDDeCfdV1RK5FhJHDFvaLBf0QoGtxr1jJX6pNY3iHH_1iOy6gmBFicubW_OF7ryIXjnz8VyO794Qgm_Avl-Q0uAssB3xOE2XiCvG-C4cu9b3T9Ryskj_FgYhbAzaDw--PjNcOSmpOW4-JKwptHwfHwOwzhoXgNlsjU16E_Pq9oRqBu5V8jTcbYpPvg0oH9U8Bhc7g79AQdZmnAJMDC79qayfyWBZmaq78_oQyh_MOQo2mni6MRlaujg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
افشای لغو عملیات ویژۀ آمریکا، در نتیجۀ حملات ایران به پایگاه مهمش در اردن  @Farsna</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/farsna/461306" target="_blank">📅 22:30 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461305">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">🎥
ویدیویی دیگر از انفجار در ارتفاعات علی‌الطاهر لبنان
🔸
شبکۀ ۱۲ رژیم صهیونیستی: بیش از ۱۱۰۰ تُن مواد منفجره برای انفجار تونل‌های ارتفاعات «علی‌الطاهر» استفاده شده است. @Farsna</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/farsna/461305" target="_blank">📅 22:27 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461304">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">گفت‌وگوی تلفنی عراقچی و وزیر خارجۀ عربستان
🔹
عراقچی در تماس تلفنی با وزیر خارجۀ عربستان، دربارۀ آخرین تحولات منطقه گفت‌وگو کرد.
🔹
دو طرف با اشاره به تشدید تنش‌ها و افزایش ناامنی در منطقه، بر ادامه همکاری‌های دیپلماتیک برای جلوگیری از گسترش تنش‌ها و بازگشت ثبات و امنیت به منطقه تأکید کردند.
@Farsna</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/farsna/461304" target="_blank">📅 22:23 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461303">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">🎥
حجت‌الاسلام رفیعی: تجمعات شبانه تا زمانی که رهبر انقلاب لازم بدانند، ادامه خواهد داشت.
@Farsna</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/farsna/461303" target="_blank">📅 22:20 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461302">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/efb40d1f9c.mp4?token=MtLlihL0nS6oI0SkrzlpojQub8HklfrOJl3y1zawp6DKUdR3dB_xr8sJ8ZBJB5W-MPi8p9LyY0rH8ERzdggUnu32WF7TnM6ZRDQBw_nE-l5t4Ni9JdUCHjHqEG-m4njG9lFz28BrjSXJk7m23lA3r_MRyAiMcnSENaaf1gvECpZM2zVSGodgiLnCVSRoG5A6uBETzedxM8E8HIxShLU515-iCtw8nf4IAU5XGaky0KPU-Gz5wEnaaT92S7KC_PkY2xDgs-aHrSBu3-BfIMF_0iWabDET0sqyswkGQkY09DrO6SqtQEZ3cFL3DbuVK7MzihABSd55dLoiwaYBtzo3kg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/efb40d1f9c.mp4?token=MtLlihL0nS6oI0SkrzlpojQub8HklfrOJl3y1zawp6DKUdR3dB_xr8sJ8ZBJB5W-MPi8p9LyY0rH8ERzdggUnu32WF7TnM6ZRDQBw_nE-l5t4Ni9JdUCHjHqEG-m4njG9lFz28BrjSXJk7m23lA3r_MRyAiMcnSENaaf1gvECpZM2zVSGodgiLnCVSRoG5A6uBETzedxM8E8HIxShLU515-iCtw8nf4IAU5XGaky0KPU-Gz5wEnaaT92S7KC_PkY2xDgs-aHrSBu3-BfIMF_0iWabDET0sqyswkGQkY09DrO6SqtQEZ3cFL3DbuVK7MzihABSd55dLoiwaYBtzo3kg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ارتش رژیم صهیونیستی: دقایقی پیش زیرساخت‌های زیرزمینی حزب‌الله در ارتفاعات علی‌الطاهر منهدم شد.  @Farsna</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/farsna/461302" target="_blank">📅 22:17 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461301">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YrFh4WQ-rUm6lxJ47puYyUCIKoSk8Tr-YmojSqPs5TuK_rsxevc62PIX1yqjjgwJ6tsy9yTv0X0f81iJexk1mww86Ls0NepM8OXI6Y0JJu_6O7fKsYOxkWqU4cYn0kzrP-7iiqI9OTMcpU_ZsW5Rqwm2zlgHLTXFG3HBFM3UYJBx2bmHan5t1wkOvs96_GHzNlVQYfVkuOcTQJr_Zxfjl4TB2uIwopb-l71ufcpR6DTXmGAZSOm7gnm_LcSHol1XJ6n79wfJU-r6EnzkVQ3H1hllJ8DOpJA_TSYPWyTDwr-FBB16EeIt1HFzVkQbO9cbV9pL2o2ef-jMosHjQWvecg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تسلط کامل رزمندگان یمنی بر ساحل غربی؛ پایان درگیری‌ها
🔹
دولت صنعاء از پایان درگیری‌ها در مناطق ساحلی استان تعز و تسلط کامل نیروهایش بر این مناطق خبر داد.
🔹
شورای عالی سیاسی یمن اعلام کرد درگیری‌ها پس از بیرون‌راندن نیروهای وابسته به ائتلاف سعودی متوقف شده…</div>
<div class="tg-footer">👁️ 9.99K · <a href="https://t.me/farsna/461301" target="_blank">📅 22:15 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461297">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/49180b3a49.mp4?token=hCWR2aWrS9oNHybxClg-9XExzAz4ELDKu7u3UNWez77gxN1sBcPwufNgsrWdACpBTkuN8WOnuUVygtJSKv-X_ZssPodno8M9uug6KthsaEP-4k5TiQfbs-gD0roURyeCqf-nRqdJ1-S6EBwU__JJcHRYVLG31YNR6XOKNG_iFHHy0W2DXpYQMkWPGpjkl4I13cRD57wwPdVZcRtQ9cpKcLrddqW_G5yejwmQnSyZomGSWWKI6j3TOyNNRFPCVMnOFPY_mcl79wyLLs2NNL2hRFjUFUfRG4pV9y9v9eiq2vKHFiZ0zjc7qcVBlfAO0QcX4YlL0ZMKhV_5D63KBuOM7g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/49180b3a49.mp4?token=hCWR2aWrS9oNHybxClg-9XExzAz4ELDKu7u3UNWez77gxN1sBcPwufNgsrWdACpBTkuN8WOnuUVygtJSKv-X_ZssPodno8M9uug6KthsaEP-4k5TiQfbs-gD0roURyeCqf-nRqdJ1-S6EBwU__JJcHRYVLG31YNR6XOKNG_iFHHy0W2DXpYQMkWPGpjkl4I13cRD57wwPdVZcRtQ9cpKcLrddqW_G5yejwmQnSyZomGSWWKI6j3TOyNNRFPCVMnOFPY_mcl79wyLLs2NNL2hRFjUFUfRG4pV9y9v9eiq2vKHFiZ0zjc7qcVBlfAO0QcX4YlL0ZMKhV_5D63KBuOM7g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
انفجار در ارتفاعات علی‌الطاهر در جنوب لبنان  @Farsna</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/farsna/461297" target="_blank">📅 21:59 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461296">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/34f3671584.mp4?token=jRWXmgbUxrU4WPKtruyowwYFg5FoGRPQSljJGzCmHA1WIZk4M3Alx4izGSNngBlGChYHcWe9hGcA6vpl-nULdotQw54qN62ouUCBaON7bDJ5ilULrjKNHpkfj2b5Tzq3Q2xzlhDNsrKLDxN_vSymUHmHfvOku0JyplsoxyViszxB-RLfAqaOdERH-YNQffAACuWDYcsAUtorLg_ixdk56CDrxmkv20lhuCci7NGSwA_W2lJST1rkpqS8N5ha0NGI4CTZczqbi8oag7LPkFmsIdsr9bhthwGFPxb4LbLQBDyD-yHhrR3BE6yxp0xl6Y9H9n0VLwID-AezBCgi2OlLng" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/34f3671584.mp4?token=jRWXmgbUxrU4WPKtruyowwYFg5FoGRPQSljJGzCmHA1WIZk4M3Alx4izGSNngBlGChYHcWe9hGcA6vpl-nULdotQw54qN62ouUCBaON7bDJ5ilULrjKNHpkfj2b5Tzq3Q2xzlhDNsrKLDxN_vSymUHmHfvOku0JyplsoxyViszxB-RLfAqaOdERH-YNQffAACuWDYcsAUtorLg_ixdk56CDrxmkv20lhuCci7NGSwA_W2lJST1rkpqS8N5ha0NGI4CTZczqbi8oag7LPkFmsIdsr9bhthwGFPxb4LbLQBDyD-yHhrR3BE6yxp0xl6Y9H9n0VLwID-AezBCgi2OlLng" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‌
🔴
سازمان رادیو و تلویزیون رژیم صهیونیستی: ارتش اسرائیل امشب تونل‌ها و زیرساخت‌های موجود در ارتفاعات «علی‌الطاهر» در جنوب لبنان را منفجر خواهد کرد. @Farsna</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/farsna/461296" target="_blank">📅 21:49 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461295">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">حملۀ هوایی صهیونیست‌ها به علی‌الطاهر با وجود ادعای تسلط بر آن
🔹
الجزیره: جنگنده‌های رژیم صهیونیستی شهرک المنصوری و ارتفاعات منطقه علی‌الطاهر در جنوب لبنان را بمباران کردند.
🔹
بمباران ارتفاعات علی الطاهر در حالی است که رژیم صهیونیستی روز پنجشنبه گذشته مدعی…</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/farsna/461295" target="_blank">📅 21:46 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461294">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/72408cebae.mp4?token=K00hhllyr6tmIyiLNpvyLRtjQNVxQHGK5kMUzGfGMUlQF9TAUMF6nmgm_RyDaRS9erLmRubvHr-k9fCbqzq2d9Dd0QdIfz6ojVOZfo1JM-D4EeBfw70QpbSd_anpnzpp9y3UGlyDXz9Ytm3qAfv5kf5lweRYovVZIQSkZ9sSClxpw6Im9ZzQuUZj7SZ7TVv_wWjGIaZX0FR1YZrsbHuqsyv_cS7R-4SJCLMgTX6d4GEMQrdTivyvn6NWH08KCHWRH01LjPJX10Q0HBNFjs04HLhLWRCQvX671fUqmf-uMkXqR-OeqqvF4no84hLI1Rtug40f-8J6cJmGZWSrhiOFVg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/72408cebae.mp4?token=K00hhllyr6tmIyiLNpvyLRtjQNVxQHGK5kMUzGfGMUlQF9TAUMF6nmgm_RyDaRS9erLmRubvHr-k9fCbqzq2d9Dd0QdIfz6ojVOZfo1JM-D4EeBfw70QpbSd_anpnzpp9y3UGlyDXz9Ytm3qAfv5kf5lweRYovVZIQSkZ9sSClxpw6Im9ZzQuUZj7SZ7TVv_wWjGIaZX0FR1YZrsbHuqsyv_cS7R-4SJCLMgTX6d4GEMQrdTivyvn6NWH08KCHWRH01LjPJX10Q0HBNFjs04HLhLWRCQvX671fUqmf-uMkXqR-OeqqvF4no84hLI1Rtug40f-8J6cJmGZWSrhiOFVg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
کلیپی از صحبت‌های شنیدنی رهبر انصارالله، همزمان با پیروزی‌ها و پیش‌روی نیروهای یمنی
@Farsna</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/farsna/461294" target="_blank">📅 21:45 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461293">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bdd560g2TO8SdsAPM3KZvLj9syHtuWvmQdBzQRjzWi_Od0rh5iPLSugNNMCOx1Xj4whXArQbbBo0704oLxIYtGDFnPajOQr0Oa3cCWt-qFIqoKP5ooQ6h668EmoyPQo7f2MTwv2FCgvv9WNgxW2_6D7qPjZ2X7VDw9j6pn-6jz860IoczrrIcdhi8yi2dqJqez-Qmb-zNNmWw4aOn2UoE3wwGmWUkwe3q8Q-Ymc5w_TfhFA1A25HokqEuxCNVjvvEF8kHtY9SqNnjQ_q1CpVSQGIOxUVwPxrfxBt3c7eML9h9YHNyG5pFeQK6ixcwrPbwANiHHEUkLsY3KnYJOeelQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پزشکیان فردا به هند سفر می‌کند
🔹
رئیس‌جمهور، فردا برای شرکت در هجدهمین نشست سران کشورهای عضو بریکس به دهلی‌نو سفر می‌کند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/farsna/461293" target="_blank">📅 21:36 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461292">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KIIpiuJOEVIwG9m6TnNPD5T4u7ZtH_kbaB5t6kb_SKYeOkPbYIsc034Th2wgxwxb7GKnxZAqSO2V9mDegQZOc6dSJOOY2IWVrdYyzd-7H4I0TwycZWgqNWzstzyytAwvS7ZazcJ7qajI314vZQC2ZJVpKMbhL5tldtOzgzSQfhnb3KRhylma0hNaGDa_uiemPPmta4eGjyVyqSK09vl6lUk4kGSaE_oQCH7vVFOOT3H9bRpDi7-wAWbJtC7_kcte4Hh0L75v0WNIOTNeOHVPgaLlI5k7gG64gbs1puUeRShje_R9nGnRih7iP-RWNMFef_QmhL_a89Mahs3kfzLyfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‌ آژانس پروندۀ هسته‌ای ایران را به شورای امنیت ارجاع داد
🔹
رویترز به‌نقل از دیپلمات‌ها خبر داد که شورای حکام آژانس بین‌المللی انرژی اتمی پرونده هسته‌ای ایران را به بهانه آن چیزی که نقض تعهدات توصیف کرده، به شورای امنیت سازمان ملل ارجاع داده است.
🔹
این قطعنامه…</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/farsna/461292" target="_blank">📅 21:21 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461291">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9b528dfc40.mp4?token=E7Jft9UoUcYhqVRBjt_kvH2DS3rGkf3Hn0xPq1ssoyAnZ0buWvWvmpTB-G-52sn6GqmB1YwN8oi8yx35L0gMIdfH-afd0tOCTBPuaPkpxWBgztkV9z9VBDMBWwkKAYl_vwdQ0HOi9yddqzL7f6uEqSgryWHzVhFgNDSA6-Tk2wu9QBoLwDQyYU6qNHOuBoXHYySeO4wvvMnxbhAwGY_F2c7ek6ghD9RoB8ZaAgpzWGu9KRqLTuLiGDWDLfw-1RL1ugbUutZ-sM-GUQNJFRpGh-lEx5T_PFX682KyE9a6QNFTTerte8t3Eb_6POebBayJwj-UswRvX7WfAMijRRCaHA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9b528dfc40.mp4?token=E7Jft9UoUcYhqVRBjt_kvH2DS3rGkf3Hn0xPq1ssoyAnZ0buWvWvmpTB-G-52sn6GqmB1YwN8oi8yx35L0gMIdfH-afd0tOCTBPuaPkpxWBgztkV9z9VBDMBWwkKAYl_vwdQ0HOi9yddqzL7f6uEqSgryWHzVhFgNDSA6-Tk2wu9QBoLwDQyYU6qNHOuBoXHYySeO4wvvMnxbhAwGY_F2c7ek6ghD9RoB8ZaAgpzWGu9KRqLTuLiGDWDLfw-1RL1ugbUutZ-sM-GUQNJFRpGh-lEx5T_PFX682KyE9a6QNFTTerte8t3Eb_6POebBayJwj-UswRvX7WfAMijRRCaHA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
فروشگاهی که قیمت برنج بسته‌بندی‌شده را دستکاری می‌کرد، جریمه شد
@Farsna</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/farsna/461291" target="_blank">📅 21:17 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461290">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c757a9d4ea.mp4?token=aGOci-ATxw4gSTnXnypEFWEmv8fVKbz1LifcsJOE3R9uuj-TIY2YD2htwJhKT3-zfPpqLtuhN8kiPmxuxs89DWkKLnUmbebwb0L4_MVGCxzDUibJsi0BEnLYD9dh9fJisInlt4KWRvn8Ving2P9YbNdY5PL21_Fyfitrv8_3bIaKKguOJMvvQ0vBKz0KbTZc1pwBSJSWPeSWelcVY2Yyp2DHk7ZrzczWhaenq4tQyrnN0OgO_Ux8vEVXZtAOWGoz2RlVFXE8bY7NbmEXkS0VJewilqcrfIx4oH-KOh1fCQhf2sTb4yKFX84s-1YJ5wbT_OKyUMZvl1bnzNoXAf9m4IWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c757a9d4ea.mp4?token=aGOci-ATxw4gSTnXnypEFWEmv8fVKbz1LifcsJOE3R9uuj-TIY2YD2htwJhKT3-zfPpqLtuhN8kiPmxuxs89DWkKLnUmbebwb0L4_MVGCxzDUibJsi0BEnLYD9dh9fJisInlt4KWRvn8Ving2P9YbNdY5PL21_Fyfitrv8_3bIaKKguOJMvvQ0vBKz0KbTZc1pwBSJSWPeSWelcVY2Yyp2DHk7ZrzczWhaenq4tQyrnN0OgO_Ux8vEVXZtAOWGoz2RlVFXE8bY7NbmEXkS0VJewilqcrfIx4oH-KOh1fCQhf2sTb4yKFX84s-1YJ5wbT_OKyUMZvl1bnzNoXAf9m4IWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تصاویر بقایای پهپاد «کاریال» ارتش سعودی که در استان حجهٔ یمن سرنگون شد
@Farsna</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/farsna/461290" target="_blank">📅 21:09 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461289">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ja7Sv9S1ksrBAWDxnOFw_S5v5kYi9cx5pDTkEaUsRq_yDOCVWQK507Sq32WCGnGY4UNcxZyfT_dx-a5pOfwwJq2YnFuiFqW4qaBa4AT0wdKifzHqVpTWR8Wt2uNSnjfqSL20GaQc6n1qRuhFOX4hToGqoGkcsuwR2CvLKEpoypbcGxUKJPoQlS25tVTC72vUGeXDeFcmq4w-40e-cDeo87aACu1sFEK7Q2Ty_WnHWuoR_qdB0GDrHUAm3XPSohonSZkheaC3VJM98JeWKxtPlyh6TFNhTGYfyAKSd_GQqLf2EO00a2hH7u8e5j_UN4q8NwqP3R-PCrnmFm-JgtjyvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
نفت به ۱۰۵ دلار رسید  @Farsna</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/farsna/461289" target="_blank">📅 21:01 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461288">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">بسته خط ۱۳۰.pdf</div>
  <div class="tg-doc-extra">3.7 MB</div>
</div>
<a href="https://t.me/farsna/461288" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">بسته خط ۱۲۹.pdf</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/farsna/461288" target="_blank">📅 21:00 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461287">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MZ_NHaKl6EmNkzdbrB-TlC7ro-t-9tIkV8fx7I8a6_ZlOgcQ3918QdNzY6-62U8IKhi1MmzFVmz5u9-VavVHVUmBOQ-Z2YBNFQbzGYtq2Ey2ftA8S8aQkw38e2slaFL8S1YZW2BHItPrJS2e89L5P7yRObnHKiTF6NxLOC608JdnF2SWM-f2kAnPun9LLrAibf7vlGHfuJI1uz3iWjgWx5gQj-YZSq3F3SyxuMsl1vzcsgXeOpKUZ_X96sD3UX_NgBXtqaPtbPEs6WwTD57DeDcBf-hWMZf4-g3EYiyT5K64FPYZ3Pa9K2sGfu4zeBUXDP6SnCP1ecBiQz0RQVqrKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎥
آسانی از روی نقطهٔ پنالتی استقلال را پیش انداخت
⚽️
استقلال ۱ - ۰ پیکان @Farsna</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/farsna/461287" target="_blank">📅 20:54 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461286">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">🔴
انهدام شمپاد آمریکایی در تنگۀ هرمز
🔹
نیروی دریایی سپاه اعلام کرد یک فروند شناور سطحی بدون‌سرنشین آمریکایی از نوع Saildrone Explorer را در ورودی تنگۀ هرمز هدف قرار داده است.
🔹
این شناور با شمارۀ بدنه ۵۸۳۸ در حال انجام مأموریت در تنگۀ هرمز بود که هدف قرار…</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/farsna/461286" target="_blank">📅 20:45 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461284">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c9bb18e21a.mp4?token=eHa-v3LV5uUutvFyfJDiN4C51VTeyn8qpHEY34lpxtbE5XqxdiwUGjTDsO372QtrRxE_FPmTGbPKtgAYjdzt0d711-sAyIw2FLz9XKz1kXAGd27iin8_NvB1bOBnvGhBB82qALaaqon98OfFJHnG-jJZFEc9_405JlE_14bTyw5IoLJ_k1BqznfjGbQkNrB9v2KwJI0Ss7W4vqJ4CoBp6K7yZcfy66nmMUY-FPA6JylVeAhOvUQlYIRL3t6X31t7icYiHH_G2JStVb6lx-M2j1nVO7mq6MfKtOqxLKmcydLqqI6PuKNhYEjT0kcWnpWBNXwT1G3bdZFhXHTsMPPiPA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c9bb18e21a.mp4?token=eHa-v3LV5uUutvFyfJDiN4C51VTeyn8qpHEY34lpxtbE5XqxdiwUGjTDsO372QtrRxE_FPmTGbPKtgAYjdzt0d711-sAyIw2FLz9XKz1kXAGd27iin8_NvB1bOBnvGhBB82qALaaqon98OfFJHnG-jJZFEc9_405JlE_14bTyw5IoLJ_k1BqznfjGbQkNrB9v2KwJI0Ss7W4vqJ4CoBp6K7yZcfy66nmMUY-FPA6JylVeAhOvUQlYIRL3t6X31t7icYiHH_G2JStVb6lx-M2j1nVO7mq6MfKtOqxLKmcydLqqI6PuKNhYEjT0kcWnpWBNXwT1G3bdZFhXHTsMPPiPA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
داور در دقیقهٔ ۷۵ با کمک بازبینی تصویر برای استقلال پنالتی گرفت  @Farsna</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/farsna/461284" target="_blank">📅 20:36 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461283">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/875cdcd8c8.mp4?token=kuDe74L0TyoKXHTdqcI74Pzx7uqJnpgzpeCAzvWcFMBRzmd7_sFzkWVduhXTNPPdFkKishPpYtOqlE26ePzWGLY6atRHceRPZ1QbKkHn4lOSgxILmfmF17tQ7G0ioyAqiHVza8SZ8Suwg8oQ5M8ppXxwWGUE3t55YN2RJrNtZ46TC8kAF2aQ6LPnj0BE5rpESWvFP-q132nIM-AOCO0OsEDS5IXA9MfmFRx6q0TRkv89leQHvd5ItdMtc4NkVAn-3s5y8UW5_erBRkh3ZNl4Q9V51OF-UPHXl-sRfAlFiRrn5k8SGT7KR9rzmINEUnpuLkRDh1IhtJgWJTBR39cULg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/875cdcd8c8.mp4?token=kuDe74L0TyoKXHTdqcI74Pzx7uqJnpgzpeCAzvWcFMBRzmd7_sFzkWVduhXTNPPdFkKishPpYtOqlE26ePzWGLY6atRHceRPZ1QbKkHn4lOSgxILmfmF17tQ7G0ioyAqiHVza8SZ8Suwg8oQ5M8ppXxwWGUE3t55YN2RJrNtZ46TC8kAF2aQ6LPnj0BE5rpESWvFP-q132nIM-AOCO0OsEDS5IXA9MfmFRx6q0TRkv89leQHvd5ItdMtc4NkVAn-3s5y8UW5_erBRkh3ZNl4Q9V51OF-UPHXl-sRfAlFiRrn5k8SGT7KR9rzmINEUnpuLkRDh1IhtJgWJTBR39cULg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
داور در دقیقهٔ ۷۵ با کمک بازبینی تصویر برای استقلال پنالتی گرفت
@Farsna</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/farsna/461283" target="_blank">📅 20:34 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461282">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4211c2eb26.mp4?token=ttW7VEEOWOU7QOXtFTA_XVxfJ2gfZP9kDcC2YEGcwlJl4a94dK10bJdDNu68JxtAu3pzg9L9aOhGDY8u_3J_LZtTSDHGsnUi5QlYShTxNpVVE4F_8ppptwa6cHC5iCNi8CMnIRD-j3vOUlVGOKyRSL8WGrw6RxeWNWphZUV6_zIlJnr6LblUw1LoNDZLPaLwZHIy_prh9mReIfmFwcBHbpCxYl0nCWFyNvF02Z0htGtOqxCqrJ13PLDfXLXpWk2pBqZ1qBhVKPdUZgdWNEwr3kvm_8D3_SlB0jwW8ZYBUyWH_f1V5Ec9XftCUQFWxR5QxY1Dtlpq4r3Pl2jLTKpksg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4211c2eb26.mp4?token=ttW7VEEOWOU7QOXtFTA_XVxfJ2gfZP9kDcC2YEGcwlJl4a94dK10bJdDNu68JxtAu3pzg9L9aOhGDY8u_3J_LZtTSDHGsnUi5QlYShTxNpVVE4F_8ppptwa6cHC5iCNi8CMnIRD-j3vOUlVGOKyRSL8WGrw6RxeWNWphZUV6_zIlJnr6LblUw1LoNDZLPaLwZHIy_prh9mReIfmFwcBHbpCxYl0nCWFyNvF02Z0htGtOqxCqrJ13PLDfXLXpWk2pBqZ1qBhVKPdUZgdWNEwr3kvm_8D3_SlB0jwW8ZYBUyWH_f1V5Ec9XftCUQFWxR5QxY1Dtlpq4r3Pl2jLTKpksg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
انهدام شمپاد آمریکایی در تنگۀ هرمز
🔹
نیروی دریایی سپاه اعلام کرد یک فروند شناور سطحی بدون‌سرنشین آمریکایی از نوع
Saildrone Explorer
را در ورودی تنگۀ هرمز هدف قرار داده است.
🔹
این شناور با شمارۀ بدنه ۵۸۳۸ در حال انجام مأموریت در تنگۀ هرمز بود که هدف قرار گرفت.
🔹
نیروی دریایی سپاه تأکید کرد تنگۀ هرمز مسدود است و تحت کنترل و اشراف اطلاعاتی این نیرو قرار دارد و هرگونه حضور خصمانه در این منطقه هدف قرار خواهد گرفت.
@Farsna</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/farsna/461282" target="_blank">📅 20:26 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461281">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">‌ روسیه برگزاری نشست شورای امنیت با موضوع ایران را محکوم کرد
🔹
نماینده روسیه در سازمان ملل: نشست امروز شورای امنیت یک جلسهٔ توجیهی بر سر موضوعی است که به پایان رسیده و وجود ندارد.
🔹
چین، روسیه و ایران معتقدند که با فعال‌نشدن اسنپ‌بک تا تاریخ ۲۶ مهر ۱۴۰۴ شورا…</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/farsna/461281" target="_blank">📅 20:22 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461280">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">🖼
واکنش معاون وزیر خارجه به تصویب قطعنامۀ ضدایرانی: در شورای امنیت هم نمی‌توانید کاری از پیش ببرید
🔹
غریب‌آبادی: به تأسیسات هسته‌ای تحت پادمان ایران حمله می‌کنند، روند عادی راستی‌آزمایی را مختل می‌کنند و بعد همان اختلال را دستاویز صدور قطعنامه در شورای حکام…</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/farsna/461280" target="_blank">📅 20:00 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461273">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/AUmUU4e3GXYyM0m9C19BkPjXtlOV2L3us4XValc6uQXB58lRznV9CSWtccUdLXkUUyOhswZ2mNgl-5pGt2CznsfQ0YpGttXP5gQohiHAmBhwqt9tDyVsy7j2NU6NBApaWiviu5oMd-zR4PISpJoaDHkWazy8t9ncKjYfGohaPc7YybZPcHb-v1IfANcrkx49FN31ltWMmSgxL5LVwpsMnvesuKX1U7lwU_GwJTllUeibN_3Zm9L-Lmy2_3kmArDos2mDkvS8G358wqpHe4wmmbvC2gkSowhenyJxlbH-dPtvQVcWeDc6thnnEqjZ9VCG61OGMni7Lr2qTLe0hPkQqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vBXKx3kdj4S5YF5A8K7IuAJ1w64klpltJ9SGLOtKDc-_BOYHHCI5SQwiuNxS6MTxe1HF5fB1f1hneAEGDX45dUTNMzwVJLi01YvYMrPd6BKLMhTfEcpiA23Hgr6F6GB4sswTZqG1CWj2azP8VCIeK1LEF7GOhE0UNSwf460GeGChnNlYAjg_cymkk3TFjGM3rz7FjaondaOFcSHBaZc1gvih3NeUKPk2yh8vnnqzhJHNpC8NpcbvCrDYXUZWONZZ-yIFHy8T-LnyK3r3A3RSiAfTAXGW7Shcywn9edx1xNSiqcjnrxSwR2B2dT2_rTs08n8UDRG-LnxgMObGpGtyPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/j_QIj9XpWaw8kXlpVJGczDPMxR2R9v2jjWs99q2hUk-joh9RY3-BaUtUICdZs3hDxeQsTE6Ph8YGujhY723Uh1x7dVsaT8nHC3uUV_2mYQhGXUl-muX2TT381DHfPDCNhui7gc0bSrK6kJfsyIICLTYvilosu7FYexrESqKK1q5YWgAGzBH9TugSd57J5dlu0REa-MDWYhDso0W7hr7MdZZ_V850VwBuPjzM6qqkrWYTUQss1gQcoJi9bEARb1gxyceXI-Cmt9C3PzlLZ5uoZFKX3Fw9aLpQfwg15FFeYZGXxQArXg2_JenmLKLFu1UZNcvso9ESmbeJ3XUwjOz0kw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jaCVLXbozmYv5b6XrHNobJ-_XPZ-LCPX2KtlJYsS3TbK1nkflr89rXny-6sGZC-MgDILprLIAo76fYxMai9G10EquPCVJBpQFz8hDUQoGjfqlyJ6OXfW2KC5FzeeRQHZtoTHgNNQyM1PnHi3h02KiYXyWPw9WTHzwn1sF_iOjgsS9-FLU9gVOF_5IpVcP4Zd8CcD3juJJfesVGYeCiLD7iqbUt2WCXMTpEjSh8eUHzf31bWM0WkLPmTBIfPTob4QUPnT6NaTHezlT4JpDpZsCxs-RXA07_caihbarTaLbZRPFd0KhKq2IhQTP7uQ4JlhKa5TUie01VNiesEij3tHiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/G7foWEBEg_oH0Lz_uZ6seFWgV7ktEfAtLy21-dChBL2A94aueX7u48XXUhXdqbz4Qror9pc_mcmfIDeDZz7bPrls2XmWpUDr_OfANPbThghbCbCBDp67sLYgI51idQp0HwYeEKjOrf-bmxCr6r4igg-TDY6I8CqM3LuRWgld1TEsGL8PaZ9KnQTX7FRsZiJz0wM7ZbzYxE5xuRvTN1XCEVyDl3Z4Kp-AFnzbKpbtG421VG-LQ5TUnCkm43rjHKxwUZIaraPhDiyfJ17nyJdvxI9JxHIg7z-bCxBJ4ttJXUJS-ewjzDTRUepvrTcSi4II8_qqM78HnmVxpoYapGw4Og.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HFZ5OwrBn6EZvkWmNjyXZLZ-1eN8CIrRGD2wwu8jvu0ZY4q5HtZMW_3MOnX8uQzYgxU3AvNWNKQT1I3owqkBHGWTGmsssci_ZYhlbdGaAGkPPBwaDXUrKhrq4T0Erz7-2sa9TXo0NqrMEoi5l-2s3UcHA9kgLE_nz1301P4AOxTpPzDqz38CcckCmmfZKv_JNSoLLxP9CV7B6A3hjCNloIlg7JGmpmH2RPzxLLzFE8kDaaIdyDYCJPul2wigYWPkqg1ysMCAoJw_i77xM0PEAafVsCCbx2UI0Gg8kdx6zkHs3fHAvUrCE0RbcgVfS01hwrZM_MgLDe8XqJcL-VvV4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MWYYqpmIA-9qNFm-VZFgdAjZxGgYKGvfUFbBlezquLMC8M3Y6gIVCHOlaDHDsfNYsESreykulfdNjL5tK8FVJFVWElzQ19QsRh_tseXask7yqzt-BbDL5T8p29UpcRy_Z9rezLdnB4-jIO1YgD0wSVxxcfsVPpdC29xiLJNOO33vYw-l48iyFWg_xuDLU5QWq_xzc7SrLoyV8m4vy3dSxE-7RygdV-ZHKcoxjaFfFNtLcWNymqWr935fFsbkoXNJM-XuQbGgiZN7JgyHYEYDhW_f31asqOURKYleAjA5mLhLHl9xWtk65Mzll4Vie3QOLSI2hArYBBttUdIgTGU50Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
خدمت‌رسانی جهادگران در روستاهای همدان
عکس:
مبینا لطیفی
@Farsna</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/farsna/461273" target="_blank">📅 19:49 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461269">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/i8Qr-xkuUD9dpTrg9O8uRpcca026r2EYfQ6Hr94gIUee3I1fo4BFz-f9SEazRv97kY1xPBomJicDF89d9J0PAzRle8JuCna0YlnauWNmnHD_tskkeqJhiK8ldPXsUESfZ2Ttmybz6L9Dih-jD9xbB1Yj1g0Qr-XnaAhUnJsclTovyj8rsmMG8gt9pbbL9A_BLEp6QN-yQqP4K_A_gxCQ0fEZsjhMrtmsQXpEEi1zn0EeAFQ0wPj1rir5tmfOlXiWpQJmbh9vMRXxddLcevC5InWSAYJWwhOVLtypmHvVRnUSoLPvVoBfRToX1EG43jafpTeVs7eTFLIfwOYoNvFRSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/e6YNZ8Klqo3xSQL94WuMaHkDwxjRRSxNEukUiZkbfYSU1SMESQyX-31tC_1_p1eBpQhSJfKx_d1ZCxv82fXq51o2SX3H1C2E06WKftJRnrPQU3JiuyhdOrVUnm6PF0Acvqb0A57cpk-I6DuJhbodMeVVhfPYXMA-UimYb6NfWACrfGNW1QSWI-MuTxyIS8jOwhbWJ-l9KLLjwcs43Ap5kizSn6LWcuXgZI2H-W7pJOwlfhS0kJYGtXBe2DoUOaSUhW-MSZG-LeJTsRvcpxyjCOzt_mrE0yENqTY5SKFsLVWrFOiXQRFd2W9n4YJ5av7J6DXMzvf0RUdKVnpGxBxSrw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/odPmVk3N27EHeAWm2cTedvbxIubXfh2yHuqw55Bs5J7o4lH6GFYLHodiMF6zvzw4SNG4q8stkQpt5gfGbmTMylsbsANSPcIGP-FMtmT3P3vuJS7m5mcgVnClRI7tSlj6UZdUxuQNGzFfgyAu-Mo8LtaM_l7z-2YrPrWqQrLv_R3MlWxKVfUdbsg0lOaT_Zz60yc8ddxwgu9lsVnXY5JkDckNk8aDrpwY9GZGrTKROZGF_HHDjaL0_9_5jUOYGpkahYvrv6802XlhnrGWCpUtDIzLNZCkG0ZxjonTpxITjvrv6436Y0XGBizOenB7Olms7k0c_d-pAIF1DzyHc5p-sA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cda3959e3d.mp4?token=o6WXULQ1QoiZqUIqx6M9GXhPJJ48AAw5rKFvamZ89TN_-JqKDDeO58M1EPzMj3ab-FKGBaTGvwLIQieuUOGLrTTktu5ASAndVFZxYHV2PK8mUqg6u8yJMNSBOMo1iL91wBCcGmb7EsIrY9BpBSxjcrDtsrscqph3P7AYqBYoK_9vva7y5etZiju4xY5i-oVndRvqit9n4HDaS46Z0b7hFlH_RHwOfPx5siCatWhdpat7SWTx-93AMWbdCw-OTTdLGmsJkq0UFPYobsIJJHRvq8pI1ie25bWEQ2LEZ5uo4lqtvAk6wtLiAeZ5QD7UVTEREqtL-7MWCbY-KqckPuiVJg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cda3959e3d.mp4?token=o6WXULQ1QoiZqUIqx6M9GXhPJJ48AAw5rKFvamZ89TN_-JqKDDeO58M1EPzMj3ab-FKGBaTGvwLIQieuUOGLrTTktu5ASAndVFZxYHV2PK8mUqg6u8yJMNSBOMo1iL91wBCcGmb7EsIrY9BpBSxjcrDtsrscqph3P7AYqBYoK_9vva7y5etZiju4xY5i-oVndRvqit9n4HDaS46Z0b7hFlH_RHwOfPx5siCatWhdpat7SWTx-93AMWbdCw-OTTdLGmsJkq0UFPYobsIJJHRvq8pI1ie25bWEQ2LEZ5uo4lqtvAk6wtLiAeZ5QD7UVTEREqtL-7MWCbY-KqckPuiVJg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
عیادت نمایندگان رهبر معظم انقلاب از سیدعلی موسوی‌گرمارودی، چهرهٔ ماندگار شعر و ادبیات
🔹
غلامعلی حدادعادل و حسین محمدی به‌نمایندگی از رهبر انقلاب با حضور در محل بستری سیدعلی موسوی گرمارودی، هنرمند انقلابی و چهرهٔ ماندگار شعر و ادبیات کشور، از او عیادت کردند.
🔹
در این دیدار، نمایندگان رهبر انقلاب ضمن ابلاغ سلام حضرت آیت‌الله خامنه‌ای، در جریان آخرین وضعیت درمانی این شاعر و ادیب برجسته قرار گرفتند و برای او آرزوی سلامتی و بهبودی کردند.
@Farsna</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/farsna/461269" target="_blank">📅 19:36 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461268">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ubk2kd7HGOYrkq9Hb_gV4OZLRwX2LCcWf1p4OtWyjTOduKMHAI5vI4mLufz0gUjcfkFFd0yHX4G26Zkv_uYXimE4sidjP6rhrxVYNpYeKJxow1qPwiMXKSBCu1W2AQ68aOF-XBRnLQ3Y2iwCNpgmhJQxYXQ5YInalmSaR9_0v6IpXNgaPT3LlNKMbEqRsorJ5XQ4_fCjnzuhtjCXNkUHgqm1oxF6qgRPU81iACTUpeya5TTPUr0fcp7scViZtbPs9s9HFlFWN704ia_7uTx03ztAocbGuOc4UvE1UWms2DnIOUMMXFPP7msSonHhIjEAT9zOnGexfW1jjSQYNLzYuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">همتی: تحریم ابزار فشار است نه ابزار تعیین سرنوشت ایران
🔹
رئیس بانک مرکزی: آنچه تاکنون توسط امریکا انجام شده در کنار ایجاد برخی محدودیت‌های درآمدی و تجاری، تلاش برای تشدید انتظارات و تاثیرگذاری مقطعی بر فضای بازارها بوده است.
🔹
فشار اقتصادی یک سیاست نیست بلکه یک خطای محاسباتی است و هزینۀ محاسباتی آمریکایی‌ها را افزایش می‌دهد.
🔹
قول پرداخت ۵ هزار دلار به هر آمریکایی در صورت پیروزی جمهوری‌خواهان در انتخابات کنگره بخشی از همان هزینۀ خطای محاسباتی است.
@Farsna</div>
<div class="tg-footer">👁️ 9.92K · <a href="https://t.me/farsna/461268" target="_blank">📅 19:35 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461267">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YPwrxa0MkARRBwtdsHpUeZxHrw4QI8yCYOr7YhhIaJbHw47j-Ffm850bTf5M-5UNXD4T6vloGnzM0AsTBqhh15inCd45cuSqFRH25J4XxHeNrci4SH_F4Ql5o2RH9uJWXVWvtZ6l0hU2hFoX0XT9zSeDAKnEEVS72C14NauVDl0wpzoTbzYrEoBJ3DpoZ5MesjjK3Ysw3X1sRvseh36enXQqIFzeCJAngrTTwVQWRNnf14YpoUdI2JWiHUtHqGZmoFTP7x7AkmK3Z88Qn5eQPw6d6KidSa_lrpjuVmMKx6Ywgs7usJuNTo68660wBVsaXUBtvTqwrco7p-1SycSjWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
رزمندگان یمنی ۲ جزیره دیگر را آزاد کردند
🔹
رویترز به‌نقل از منابع دولت وابسته به ریاض نوشت که ارتش و انصارالله یمن بر ۲ جزیرهٔ «حنیش الکبری» و «حنیش الصغری» در نزدیکی باب‌المندب مسلط شده‌اند. @Farsna</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/farsna/461267" target="_blank">📅 19:11 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461266">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">۲ شگفتانۀ سپاه برای آمریکا در تنگۀ هرمز
🔹
در روزهای اخیر، نیروی دریایی سپاه با دو اقدام غافلگیرکننده، توانمندی خود در مقابله با نیروهای آمریکایی در منطقه را به نمایش گذاشت.
شکار زیرسطحی آمریکایی
🔸
سپاه در ورودی تنگه هرمز یک زیرسطحی هوشمند و بدون‌سرنشین آمریکایی به نام «Dive-LD» را به دام انداخت و آن را به سمت ساحل هدایت کرد.
🔸
سعدالله زارعی، کارشناس مسائل بین‌الملل، این عملیات را اقدامی چندوجهی و پیچیده توصیف می‌کند و می‌گوید: «این عملیات در واقع یک زنگ هشدار را برای ارتش آمریکا در دریا به صدا درآورد؛ چراکه نشان داد حتی شناورهای بزرگ‌تر و ناوچه‌های آمریکایی نیز می‌توانند در معرض اقدامات مشابه قرار بگیرند.»
پرواز بر فراز ناو آمریکایی و شلیک موشک‌های بارشی
🔸
زارعی می‌گوید: «اقدام دیگری که سپاه انجام داد و از جهاتی حیرت‌انگیز بود، پرواز در ارتفاع کم بر فراز ناو هواپیمابر آمریکایی و اجرای عملیات موشکی علیه آن بود. در این عملیات، یک موشک در بالای سر ناو آمریکایی قرار گرفت و سپس نزدیک به ۳۰ موشک از آن شلیک شد.
🔸
مجموعۀ این اقدامات این سؤال را برای آمریکایی‌ها ایجاد کرده که ایران چه شگفتانه‌ها و ظرفیت‌های دیگری برای مقابله با نیروهای نظامی آمریکا در منطقه در اختیار دارد.»
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/farsna/461266" target="_blank">📅 19:00 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461265">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس ورزشی</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/90a8f02653.mp4?token=SCu2khOfLkITXVSGpXSYHf9qwt88eZmyjbL-jQQu-R3oT7aX975Ct8nGSKdPfpcV6m7OAwZalV7fTINt5wNn_YPQx4xyI0N_ButKGesIMkA9qu3q0VtRqDOK4NMjaAJISftpqbg-Gg5E3dTgW9OfJDbQam7ncqZeRUViCalKcwk0g-eZ5RiVxojx8OZEz_YfJgysOMrO4EK7-1nrJwIt8pJ1rBQ_DW-Ci0UiK5A7s3V2XMRvCf-0J7ALhQHcif6kskRquN09Bg4li4PlW_huyCRgg3qU3CyAMBxpYcymrp9kV3o38wWe9lFrUi1c5kiupAD3sWlnFFuGmkGl1RjNzQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/90a8f02653.mp4?token=SCu2khOfLkITXVSGpXSYHf9qwt88eZmyjbL-jQQu-R3oT7aX975Ct8nGSKdPfpcV6m7OAwZalV7fTINt5wNn_YPQx4xyI0N_ButKGesIMkA9qu3q0VtRqDOK4NMjaAJISftpqbg-Gg5E3dTgW9OfJDbQam7ncqZeRUViCalKcwk0g-eZ5RiVxojx8OZEz_YfJgysOMrO4EK7-1nrJwIt8pJ1rBQ_DW-Ci0UiK5A7s3V2XMRvCf-0J7ALhQHcif6kskRquN09Bg4li4PlW_huyCRgg3qU3CyAMBxpYcymrp9kV3o38wWe9lFrUi1c5kiupAD3sWlnFFuGmkGl1RjNzQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔹
هواداران استقلال نام صالح حردانی را که همچنان با دستور سهراب بختیاری‌زاده دور از دیگر آبی‌پوشان است و اخراج شده صدا زدند.
@Sportfars</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/farsna/461265" target="_blank">📅 18:49 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461264">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NOSVpHn8r6VqpzfAvbXf5v__6RDab2jv91zUo88W9lShe1xgOHjYQaFhst5RpBitpseRx0Xybi6_Wjp2AguWXPt0zeVeakKqBfW7vVf0fQx5zX2ymTtbSh8RXRYAC1I_mqnoeSIQgvr_yjyBYvmooXxW9GyatMQeHhOMGsVWPTvJ2RYTJtuch_5zXehK1k_yD75d6TDcUM03PAJI7UcQ6iKUKcQyOVStYkGBbzd1mMhYnIXIx7H6YznQ1NuCzzUmqv0Igfv7NNhXBDwq2vL4yDvowzALxdq4OG-rWIDnv9MwAYQ1V7nzEpfQNMoOlzrq9gQ3CrkECY0yJWWKPgRm_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دبیرکل ناتو: مین‌روبی در تنگۀ هرمز به ما مربوط نمی‌شود
🔹
موضوع مین‌روبی در تنگه به قلمروی ناتو مربوط نمی‌شود. البته ما آنچه درحال وقوع است را زیر نظر داریم و کشورهای عضو ناتو از نزدیک با یکدیگر هماهنگ هستند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/farsna/461264" target="_blank">📅 18:39 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461263">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ad94fd6de4.mp4?token=qYwNId56TRCiJNg4v8VSxAGfH4zcKntoGDOhx4S2Zwut9MJXGtGDo9NmFcN9xpN98fSsGSNmF8YUB8NPv5RymDpgkEosoV-Yo9-V9mfJ1qFTP3dSinShKLMupX8gRUsis53azGfK27pM3AQmi3YtCusr77yYv8yabAg18GE2YrVOhGQBBZsZ6EAVG3WC_ONikLYKW4C_XkZvIHN0YOEZtwJB2dLfufgQU-jIhquyzFEFtUZ8cU5YONzy3Hd70DuJ9kkuEoZ55bbC02puzRhaRC-gEUCQmk2HivKxtcu3b7tHMTzMQOCqmV93KBpdluaFIK5-11OMgM_wEXa89FqUfw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ad94fd6de4.mp4?token=qYwNId56TRCiJNg4v8VSxAGfH4zcKntoGDOhx4S2Zwut9MJXGtGDo9NmFcN9xpN98fSsGSNmF8YUB8NPv5RymDpgkEosoV-Yo9-V9mfJ1qFTP3dSinShKLMupX8gRUsis53azGfK27pM3AQmi3YtCusr77yYv8yabAg18GE2YrVOhGQBBZsZ6EAVG3WC_ONikLYKW4C_XkZvIHN0YOEZtwJB2dLfufgQU-jIhquyzFEFtUZ8cU5YONzy3Hd70DuJ9kkuEoZ55bbC02puzRhaRC-gEUCQmk2HivKxtcu3b7tHMTzMQOCqmV93KBpdluaFIK5-11OMgM_wEXa89FqUfw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
اسرای یمنی از زندان‌های مزدوران سعودی در ساحل غربی آزاد شدند
🔹
رئیس کمیتهٔ ملی امور اسرای دولت صنعاء: نیروهای مسلح تمامی اسرای ما در زندان‌های دشمن سعودی در ساحل غربی را آزاد کردند.
@Farsna</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/farsna/461263" target="_blank">📅 18:29 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461262">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YP2pQeMGdyD_Uhlx91JjhmYXBGSXB9aFSJ9q4WhklNaJFb7yB7wNVIWxQsLrLz4VrUaKIEeuU38Ta3Y7mw2i7tyyMxyrD_gK8EkfbSUrUupANh02cD4HnHSlP2Iozl_jfTx0NIlvGusi6K2_Cb85So2r9odzhfjlaPv6crfQNZvr0j_MdAtmnYA_wXufCJvxoYXAnHgkaIlG8Gyk0EWC07IKoZwYd7uAruOxwMMn1YjZbNVstaszUarHME6MEk1IiM9QSXDtMFpzDke3YZ99LQ6BXGRUZxDBoNaPOLMNecjtC_8buA5qiNgwR9Xp2WKL0Xqa3ugznrJY2CsC3IO3Rg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎥
تخریب عجیب یک کاروان‌سرای تاریخی در سبزوار
🔹
رئیس میراث فرهنگی سبزوار: کاروان‌سرای روس‌ها یک ژاندارمری و بنای تاریخی در کنار کمربندی شمالی سبزوار در دوران پهلوی بوده که در زمان اشغال اتحاد جماهیر شوروی، نیروهای نظامی در این ژاندارمری خارج از شهر مستقر می‌شدند.…</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/farsna/461262" target="_blank">📅 18:16 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461261">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b4c5d25dd7.mp4?token=hknUadWLwwHTYwgRVAPPNvK-DK-n_PCcdP47lJa5lPh8wZtV6JHf63LnFBRYjZZSdPfqxL0acxUkf8A7d268b3S-K2fSc63wWKBfVdyFOY1f8bertBM-IocXQQOTWNiNKjexW9gxGT2ckaMbN83ugC7F366jb4cSjiqgbQUf4dWj2sREiOkTr-Z_M0Yzd0ftWbnu2wp3U88ZWUsyedph2S-LYWauWZFZ1jnwBr1kiZ-XTGk4rE9ipBWKcafh6ryGIX_sUNmfeOb32szw4Xe3HW_BqfZBbuUOAXgdUovroO9UTouOVjiiTQ1E_4I7bHtqPnvyOPVNRGNmGPqV7XmONzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b4c5d25dd7.mp4?token=hknUadWLwwHTYwgRVAPPNvK-DK-n_PCcdP47lJa5lPh8wZtV6JHf63LnFBRYjZZSdPfqxL0acxUkf8A7d268b3S-K2fSc63wWKBfVdyFOY1f8bertBM-IocXQQOTWNiNKjexW9gxGT2ckaMbN83ugC7F366jb4cSjiqgbQUf4dWj2sREiOkTr-Z_M0Yzd0ftWbnu2wp3U88ZWUsyedph2S-LYWauWZFZ1jnwBr1kiZ-XTGk4rE9ipBWKcafh6ryGIX_sUNmfeOb32szw4Xe3HW_BqfZBbuUOAXgdUovroO9UTouOVjiiTQ1E_4I7bHtqPnvyOPVNRGNmGPqV7XmONzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
خروش زاینده‌رود در آغوش پل تاریخی زمان‌خان در چهارمحال‌وبختیاری
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/farsna/461261" target="_blank">📅 18:09 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461260">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c5N3No5I3I37h2I3IKNqySclZZvbXkK-4xEg9s1G99dZCcSMNkMOit6pD-gtQGbeRTJc5l6YTz1cHnALPQdWsoZ7PB5jXY7CuakdPYJlS-Wq_1YCnXxNWTe1sQRcxnLBAX1GlIlzJi3UJslOZBRikavJjSr9LmT93YdTajZT9iDKs6MjUOuwHZx9FZ6KS8_KpV0n662yZTdoG-PPFCEmD1J4Uyzy3YX2W2kUg6YbYAWG0Rvkop5H0cgt3UX4P5_JCQc-grGFLPhDL6iGVbpTy5wEm4yR9TPbkgjpy8fPO8obs0ec7V4CC2IKWAPUczP9w4aWgbGtJpDxpEv6N1biwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
رزمندگان یمنی ۲ جزیره دیگر را آزاد کردند
🔹
رویترز به‌نقل از منابع دولت وابسته به ریاض نوشت که ارتش و انصارالله یمن بر ۲ جزیرهٔ «حنیش الکبری» و «حنیش الصغری» در نزدیکی باب‌المندب مسلط شده‌اند.
@Farsna</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/farsna/461260" target="_blank">📅 17:32 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461259">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Se1gsi051OkIXG1vlyNqFatn568nc98o-NRlPPdZE61yRMhO5T_1CWrYKHNqIUlhJQ0PVxvfJAf9OGHZTHQ6EV7TpixEpDod6ke9_olyC9VwmCISI6696pyF4V_ni_EYVl9ceP0cp2gy9b6FiHXasquPx0mjap6Laxu8te8NdD7UHDr_bQhtNAfwr7QLJdLCFPrrk5gl7z8RGSSbEwric9ZXQayGFf8w46JjBRa8wk3JydpjixWphgcTC8MrLDBXZdDzQETGxQ1xdGEz_nHRuWcJeMaff_lzaC0kzyQDT5391KLBJCSS_ARCDTLLykS5KLBCfqGYM2auo2Z-m1M5kA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎥
فروپاشی جبهۀ سعودی در یمن؛ ۳ تیپ کامل تسلیم شدند
🔹
محمد البخیتی عضو دفتر سیاسی جنبش انصارالله یمن امروز با انتشار یک ویدئو در حساب کاربری‌اش در شبکه اجتماعی ایکس اعلام کرد که در بزرگ‌ترین عملیات اسارت تاریخ جنگ‌های مدرن، سه تیپ کامل از ارتش سعودی و مزدورانش…</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/farsna/461259" target="_blank">📅 17:22 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461258">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس ورزشی</strong></div>
<div class="tg-text">تاجرنیا: رامین به عقب برگردد پیشنهاد استقلال را قبول می‌کند
بند فسخ ۱۰۰ میلیونی اصلاً عجیب نبود
🙍‍♂️
تاجرنیا: به رامین رضاییان مشورت اشتباهی دادند. به او گفتند هر چه بگویی چون درخشیدی قبول می‌کنند. بعد از عدم توافق، تیمی حاضر نشد مبلغ پیشنهادی ما را به او بدهد. بختیاری‌زاده او را می‌خواست اما با تیم همراهی نکرد.
🎙
ساپینتو می‌گفت به رقبای ما از جمله فولاد او را ندهید. من خیلی رضاییان را حمایت کردم.
🎙
به عقب برگردم باز هم بند فسخ ۱۰۰ میلیون تومانی را می‌گذاشتم. اصلاً هم این عدد عجیب نیست. به نفع باشگاه عمل کردیم. این رامین است که اگر زمان برگردد با استقلال توافق می‌کند.
@Sportfars</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/farsna/461258" target="_blank">📅 16:59 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461257">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Auma13ohqgTG-jL8gaYmFJMeEAJl3WwvXRlbxW0pZNo3bpasVfyYz4b_UnpdA4iz-sI9vQnxBjlKZz8DZ2AWhGics7moEXyR_WLC-YH9oWYUbk9Lx9t9KU9r1l97u_qhelGgQfg_ShjE1MnFA23OZBjiLsR8n9Nc5vJyVx-inJlsE4vv-h_ZaucKFfaB0UDVQP3Ow13rYf0LmqaRwRwSBP48O0cRC1OLsVnoCQ2lofeCCt-W7AGUODkjfAGZZQqD3NE7C4LKETRrFZEK_Be9w0qA1KnsEDH9pbnAPzOZDZGkp7uqv9Bjl_NWcG5pqAzCLknSKbAnGbd7DVnUqBrFsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هوادار متمول تیم حکومتی را خرید
🔹
ولید بن طلال، شاهزادۀ سعودی و هوادار متمول الهلال، طبق گزارش نشریۀ الریاضیه، ۷۰ درصد سهام این باشگاه را خریداری کرده و به‌زودی مالکیت آن را به دست خواهد گرفت.
🔹
او در یک ماه گذشته بیش از ۲۰۰ میلیون دلار برای خرید بازیکن برای الهلال هزینه کرده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/farsna/461257" target="_blank">📅 16:48 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461256">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QN1kBjjTNa-dJlMWatx0ecVs7f8mdh_FJxKTVIJP9vofP__DCYb_-CZ649mGY__T-XV3a4jU0ZcxXzMCKUnPnpVEjE1vANPi7X9w4yy509vlYXfTwGAdXo3Qp2sI2RA3YR6GM9uwcIqs-KAovaFlGVEt1gocyLgLN-fkSTge2_OfHfmH2bZrtkuXPjoYGv9AzHMYCHVx0-vh6EKldgJ2Q5-fdL_bsSsmZHIgmbxVxVULRX9rMk5aJuQfgYysQL1zrmCJYYKsDSvdNZU2K-5P3bi6blZQDob2BTH2KUaZjwkbyzWDQR7H1x6Mfvl4zBnWRW69wW6AhO8ealUuTRXJ_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
نفت به ۱۰۵ دلار رسید
@Farsna</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/farsna/461256" target="_blank">📅 16:09 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461255">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/986f07d0b9.mp4?token=SEvmLXEIxms5Dgmz0uBQSFGIkkb7cvhqWkiDuu9UXFGbJhLBeUut6JttCpN1QOWiqLHixKTuTXN_t3tcqnEqcCmEYR73FCJo9_-afcIh0CLp3O3rgVa8TZMX9lhbw6xDXz41xJRKyWIfbqnnnV3f5dPuBf14_ycGSGS8wKQny9plTJl9idUf_Aq89LvRBMW2P6rsWMFDV_PjuWuURCzY6okZZ_Au_S-GJQ12YstZNiia2DMa6SQHM1VnFJBiU8YHUH4oVGXSfsqyNLRyezzkGAgfp-prATwh6Ers8dsDGHLZt0pmj2XfvgTD0ofyRgct8EiPCa9A9zGSBHMfE5j7mg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/986f07d0b9.mp4?token=SEvmLXEIxms5Dgmz0uBQSFGIkkb7cvhqWkiDuu9UXFGbJhLBeUut6JttCpN1QOWiqLHixKTuTXN_t3tcqnEqcCmEYR73FCJo9_-afcIh0CLp3O3rgVa8TZMX9lhbw6xDXz41xJRKyWIfbqnnnV3f5dPuBf14_ycGSGS8wKQny9plTJl9idUf_Aq89LvRBMW2P6rsWMFDV_PjuWuURCzY6okZZ_Au_S-GJQ12YstZNiia2DMa6SQHM1VnFJBiU8YHUH4oVGXSfsqyNLRyezzkGAgfp-prATwh6Ers8dsDGHLZt0pmj2XfvgTD0ofyRgct8EiPCa9A9zGSBHMfE5j7mg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حملات هوایی صهیونیست‌ها به چندین شهرک در جنوب لبنان
🔹
رسانه‌های لبنانی از حملات جنگنده‌های رژیم صهیونیستی به شهرک‌های صربین، حداثا، حاریص، النبطیه الفوقا‌ و الخیام خبر دادند.  @Farsna</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/farsna/461255" target="_blank">📅 15:57 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461253">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b65a2defa4.mp4?token=VOWgpiWRKOuEgVZMLQEwpYbB2vlAtjOxyNYEmKtduq4e_MJsNxLAmNLR7vf7w7jC_BV8vZ0nIr7IaC0nhHvyqV-YEC_WHtDpPu5tAfWTzbQfv2IiB4xuT_3D76iNobCeGvSvqiUGimbKU7VYKgxwnjCeXMSp205HGnAfgTICvUsZnZzmAfzCpO_fLdRw-LZirypkzwEB54ENBZF0ovLOsiVVBEA3WB3Paw3JVFlCcUUKpXPCU2Z_Ssl9RZHtgUJUjsQjF9fXo_dG0xavSIru-ccxBKWDh_c2LNiK2mlQwAXQ0xoo5uOMpTgiy-tMtnMfRjM7vDDozc9EqrjSN1rX4Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b65a2defa4.mp4?token=VOWgpiWRKOuEgVZMLQEwpYbB2vlAtjOxyNYEmKtduq4e_MJsNxLAmNLR7vf7w7jC_BV8vZ0nIr7IaC0nhHvyqV-YEC_WHtDpPu5tAfWTzbQfv2IiB4xuT_3D76iNobCeGvSvqiUGimbKU7VYKgxwnjCeXMSp205HGnAfgTICvUsZnZzmAfzCpO_fLdRw-LZirypkzwEB54ENBZF0ovLOsiVVBEA3WB3Paw3JVFlCcUUKpXPCU2Z_Ssl9RZHtgUJUjsQjF9fXo_dG0xavSIru-ccxBKWDh_c2LNiK2mlQwAXQ0xoo5uOMpTgiy-tMtnMfRjM7vDDozc9EqrjSN1rX4Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
یزد، بزرگ‌ترین تولیدکنندۀ مداد و خودکار در کشور
@Farsna</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/farsna/461253" target="_blank">📅 15:19 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461252">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e333d9a21b.mp4?token=jrhRULv-cCcUuhgatnl3XFxoSudG34U7m6ObPvtgIq8Ip6JaYz_CdhcEVCEsFNLTOh4iMjUJ0dpk9q0igP2p__xgJfM-4JGcEhXrHgXph8QXZ4L4VdYS6PBC6IPQ1e5ZrsN8fBCSU--lf-hJstVLTwnAsWFEyICQAbC0tk2T5MTbs8X5SGC9Q-QtUkv3wwZ8V2wUBb8Kt4MW9TAYL9_IhYwtbCilnQM6AEzsWCzZOmu6JjRS6P74iCHbuCZrRqkDYKKzJtTNFVqXUnUEj2hGE94zbPg1z53x0ZgerVmEMliTa5IRjLOIgO0i16lIBtRo5GA9MHuoGC49D1TNvYbJKA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e333d9a21b.mp4?token=jrhRULv-cCcUuhgatnl3XFxoSudG34U7m6ObPvtgIq8Ip6JaYz_CdhcEVCEsFNLTOh4iMjUJ0dpk9q0igP2p__xgJfM-4JGcEhXrHgXph8QXZ4L4VdYS6PBC6IPQ1e5ZrsN8fBCSU--lf-hJstVLTwnAsWFEyICQAbC0tk2T5MTbs8X5SGC9Q-QtUkv3wwZ8V2wUBb8Kt4MW9TAYL9_IhYwtbCilnQM6AEzsWCzZOmu6JjRS6P74iCHbuCZrRqkDYKKzJtTNFVqXUnUEj2hGE94zbPg1z53x0ZgerVmEMliTa5IRjLOIgO0i16lIBtRo5GA9MHuoGC49D1TNvYbJKA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ایران رتبۀ سوم دنیا در درمان ناباروری
🔹
رئیس نظام‌پزشکی: تمام تکنیک‌های پیشرفته برای درمان ناباروری در کشور درحال اجراست که برای گردشگران سلامت هم جذابیت ایجاد کرده.
@Farsna</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/farsna/461252" target="_blank">📅 15:16 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461251">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H0Dxwc3rhxfXp4IXHTWeXFHxH_YcdT-eJ4NvmbNr4WkSn7EEl9GxL8FWCAWkRxHhA618hiHxENKn_d79lCOinuX8krgNff0D8kD2UIsP1EtejCi0aMTJJgTq3A9hrUPcsWhKo9xFS2bNUb_3045U_ah8EDPqMLPfJljon3vePh26NmXUZlHQBRYpfzH7W2QKf7DltjGKc5UqBcQorP5Du5xK0hqhA9tEwirNO1FkM1FuADkPP0dxyGZF6FCWRz-cTmnwuLEZ-IgfVr1eYSm9ca8r0BMv-R1-vp8Z_nV54deYOHYrJplgvoSEBlc4uL4OqeVCjECB9OKBCmmosna2qw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تعرفۀ مکالمه تلفن ثابت به همراه ۴۵ درصد افزایش یافت
🔹
طبق اعلام شرکت مخابرات از ۲۰ شهریور، سقف تعرفۀ مکالمه تلفن ثابت به همراه از ۶۲۵ به ۹۰۶ ریال افزایش می‌یابد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/farsna/461251" target="_blank">📅 15:07 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461250">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f3e0c46974.mp4?token=YdS3Aq6mtBtdEe26jIcKxSJHB46f8fd8pduwB8EIl0DDEEypYTlOHjWkapDpSGbUMzWDnjjVy-Di_5XZhdwLYFAc-N62xNfS0TOSAstU6WIb1iC8GVd_9fPO_r9JW0cUrI5WSksNNBomt69Bvg9zYTmvfnZVQ2E5IoA8Y-yKjpjln_dpsZ-46eddyMmESRS28sN5JFuYKSmH5nSZYivCgoUbLWu973zy2yQZ5VRLvIwP-oZR35_wv0Dfbn4AnZHdR019LNB3U4wk18XZLNEo_Xlon9v9-cmFAvASwsNSmikVVUUPaoG6306L3mjnDGLUr9pcFwNXLY54NbfNAU_MBA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f3e0c46974.mp4?token=YdS3Aq6mtBtdEe26jIcKxSJHB46f8fd8pduwB8EIl0DDEEypYTlOHjWkapDpSGbUMzWDnjjVy-Di_5XZhdwLYFAc-N62xNfS0TOSAstU6WIb1iC8GVd_9fPO_r9JW0cUrI5WSksNNBomt69Bvg9zYTmvfnZVQ2E5IoA8Y-yKjpjln_dpsZ-46eddyMmESRS28sN5JFuYKSmH5nSZYivCgoUbLWu973zy2yQZ5VRLvIwP-oZR35_wv0Dfbn4AnZHdR019LNB3U4wk18XZLNEo_Xlon9v9-cmFAvASwsNSmikVVUUPaoG6306L3mjnDGLUr9pcFwNXLY54NbfNAU_MBA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
ضربۀ‌ کاری انصارالله؛ جزیرۀ زقر هم آزاد شد
🔹
خبرگزاری فرانسه گزارش داد نیروهای مسلح یمن امروز، پس از تسلط بر شهر راهبردی  المخا، جزیره زُقر در جنوب دریای سرخ را نیز آزاد کردند.
🔹
این خبرگزاری امروز به نقل از ۳ منبع در دولت مستعفی یمن وابسته به عربستان افزود…</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/farsna/461250" target="_blank">📅 15:02 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461249">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f0392dada5.mp4?token=HKFT9tcp954EBvQamlw52R9zi8wfOCMo6-5txv5J8Uj0Kpo6mA2NQ--zqawQtJ8vBU3sJk3fTcPu6JdGEOrJeUtKJTRMS4wIXvLDZXz5GmIjfiHADFfVOH345RAqNnRgeXaDtXC_EzC_rCPwJQL2EvrY0PHDTxuG6d0tfYHKJQU5uAvEd9XMr6Ay4BpoREOShdBK1ompnVxCLgGifm3E73IEnfSXWBGhsPhkHXgFf5SvsbQn519B2umwTU8b5AHGg2WyZ8XHePpTwNXbvai1UIAOR3muagyr-u36ojJWlAgumnXFq-hDDIXiTRLMrHIW1Szbqp4hfKX_nDDmgWf5iQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f0392dada5.mp4?token=HKFT9tcp954EBvQamlw52R9zi8wfOCMo6-5txv5J8Uj0Kpo6mA2NQ--zqawQtJ8vBU3sJk3fTcPu6JdGEOrJeUtKJTRMS4wIXvLDZXz5GmIjfiHADFfVOH345RAqNnRgeXaDtXC_EzC_rCPwJQL2EvrY0PHDTxuG6d0tfYHKJQU5uAvEd9XMr6Ay4BpoREOShdBK1ompnVxCLgGifm3E73IEnfSXWBGhsPhkHXgFf5SvsbQn519B2umwTU8b5AHGg2WyZ8XHePpTwNXbvai1UIAOR3muagyr-u36ojJWlAgumnXFq-hDDIXiTRLMrHIW1Szbqp4hfKX_nDDmgWf5iQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
محل مصرف مالیات‌تان را خودتان مشخص کنید!
@Farsna</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/farsna/461249" target="_blank">📅 14:59 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461248">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bb8a25e666.mp4?token=md3o69ba0TXxWnUHkiCHwrOFDmkkFQXiMSCfRlNLA38fa61oVcvPpQoddFKm0CavN-AYiyqu6OAGnahsfFruN9jb4pND4AeisCtMlkM-1Sy-rqX1i3vNgtnOitoiAVPTso8CGKRRE8qCUQaaYSYkLV_nE_pUIEhsalmM4aX2cZwbL1p7bS2YtxKp_70Nb7DLJNS8QF3lg1pW0FGC81gYyq7evD49Gb1tvtNTZSUKWjEaGIqJwVJjdKvK4c0-UGb6fcA0kbctcGogjhRrsOpOmMK3XWq4GNQA0kxuKp5VPra68C4b9TvS3ZrKk2duanQJAMzSxW9JfhFulf0sjtqaSA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bb8a25e666.mp4?token=md3o69ba0TXxWnUHkiCHwrOFDmkkFQXiMSCfRlNLA38fa61oVcvPpQoddFKm0CavN-AYiyqu6OAGnahsfFruN9jb4pND4AeisCtMlkM-1Sy-rqX1i3vNgtnOitoiAVPTso8CGKRRE8qCUQaaYSYkLV_nE_pUIEhsalmM4aX2cZwbL1p7bS2YtxKp_70Nb7DLJNS8QF3lg1pW0FGC81gYyq7evD49Gb1tvtNTZSUKWjEaGIqJwVJjdKvK4c0-UGb6fcA0kbctcGogjhRrsOpOmMK3XWq4GNQA0kxuKp5VPra68C4b9TvS3ZrKk2duanQJAMzSxW9JfhFulf0sjtqaSA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
حادثۀ مرگبار برای کشتی خارجی در چین
🔹
خبرگزاری «شینهوا» خبر داد که یک کشتی باری خارجی در حین تعمیر و نگهداری در کارخانه کشتی‌سازی در شهر چینگدائو آتش گرفت.
🔹
به گفته مقامات چین، در نتیجه آتش گرفتن این کشتی در چینگدائو استان شاندونگ در شرق این کشور، ۲۰ نفر جان خود را از دست دادند و ۵ تن دیگر مفقود شدند.
@Farsna</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/farsna/461248" target="_blank">📅 14:46 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461247">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Gg1SwQPJCQvO0UHBWiuFXD84z5rl55itr1JcTDzY9eIKO9moOBmqhHqLOa5SZL6ZOSk1hjTWPNq5CHSyrtM60DOe8DhO8iw0IpihRg_NXxIL9I7_2ZftqEOYNXOG_0RUHeGZemTIVQN4uuowz-_AUlHlfMn5uqNZGq0sZzW6goytb-gA52gPcTmzV1gapT51V82mCixAPHMYLr9tvDVZKKEfnfyu1UOoBbSjnqVpWsnKhhk7Exvp2a_8Z_XRyLlva3QkuPYfIoamZb4tYM7nVTyTk0lD86z_m_YB4ybumPEsvovswEyFuTA2_JhJvhdHR3v_CFX-VKErEFw8dxsDFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خیبر - پرسپولیس</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/farsna/461247" target="_blank">📅 14:45 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461246">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QcjUjjuc1Cp4aeLcXxdwzZVeWtVcXghCqgJ7Jvw2O_bmCwF3K0zEGicPSg_vw9AWB78UUVzBZHgXwZN80K7c-fAHzeok6ny6mJmkkitu6htAQCdYH-KqsbeQeA0nZEaoQlqXZE6PSlDvHxZ4kYN8hFn4ADp9rTD_6kHbkDvzklrme5nMrLgpR9cxoANtPL4Xy_EkEsOEcgcQiX0dihCnSGddb79lkznBpCFmjqMmYimCAWJ27x7aDeQkKHNBuuP7ZNcQeJaK4k9cEEbBXDN5QcuTiOqQ19QrN76i4dczfRvyEeDiDeTR15EuZEpSnyB1gkcnU8_MdUbIqLN-CEzZoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
حادثۀ دریایی در سواحل یمن
🔹
سازمان تجارت دریایی بریتانیا با انتشار یک هشدار دریایی اعلام کرد که گزارشی درباره یک حادثه مشکوک در ۹۸ مایل دریایی جنوب غربی شهر «المکلا»  در یمن دریافت کرده است.
@Farsna</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/farsna/461246" target="_blank">📅 14:42 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461245">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d6lOGzJiGlQDlsEIVA193mJBqSl90U1cEqeaHGAWrsbxZCRtiF-dTSCnuHZ1nafCeUDlANCxIrsmG4qiHxFLFNjg-wXtAJhDSaN8zpCNv0XKAke-eW-F1HTYCIfHWQKXXQGU-oRysDbVGmefeXqe5DuzVSxJhkVlrkrPYwlBvs80DjxpZEqxZUCkBQG569Oj2Bf5cmMkSnnGDyGMRNSwL7KSa2QLl6TYTwKEenlUbNUqdXezuZH9oVCwFcxx7WsFiN12z1c7CEIjC6VwLoWjZebUI_6MbNG4POH7SBPV8mEBTeJmFqWkfAn-YXg3mpyPcTPYVtXAKls6oAhyAgTiOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎥
پیشروی برق‌آسا در المخا؛ انصارالله به دروازه باب‌المندب رسید
🔹
منابع رسانه‌ای از پیشروی برق‌آسای نیروهای یمنی در المخا خبر دادند. پیشروی‌ای که از شمال به ساحل و از شرق تا فرودگاه این بندر استراتژیک رسیده است. تصاویر منتشرشده، فرار و فروپاشی شبه‌نظامیان سعودی…</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/farsna/461245" target="_blank">📅 14:32 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461244">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ef49ccbd09.mp4?token=OaryaMAw82iqHUjKk3EspVQwfqBdwoWzDQ9-fW_VL4SL4oAs71dLUvPXyMy27OK9311IjHBoJ4Rql5lWNtqJiGxIE0Ejnv6N7AFbdSexc_qhMdUknETniBAZ4PZ7XudFMv1a4V2BzcdWY1n7HIdSu0tOk_-W1OTA7WAqlTOIHJutRxlLnElzxxwtEuee93ICAJZ7x9WnzhkOJubCZlvOBlBXh1tgaPBlXR8Q6qNHoRAYDZzScrxKJTHcAJR7h-fWRvUXxUOp2j04cPbVOGVD1hDtRYkdoHjpKDaiVJd6omq8LEzx7VOSTt_XN8KmFhv_E4xINWXdK5EBOW-daHp4NA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ef49ccbd09.mp4?token=OaryaMAw82iqHUjKk3EspVQwfqBdwoWzDQ9-fW_VL4SL4oAs71dLUvPXyMy27OK9311IjHBoJ4Rql5lWNtqJiGxIE0Ejnv6N7AFbdSexc_qhMdUknETniBAZ4PZ7XudFMv1a4V2BzcdWY1n7HIdSu0tOk_-W1OTA7WAqlTOIHJutRxlLnElzxxwtEuee93ICAJZ7x9WnzhkOJubCZlvOBlBXh1tgaPBlXR8Q6qNHoRAYDZzScrxKJTHcAJR7h-fWRvUXxUOp2j04cPbVOGVD1hDtRYkdoHjpKDaiVJd6omq8LEzx7VOSTt_XN8KmFhv_E4xINWXdK5EBOW-daHp4NA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‌ اعتراف رسانۀ آمریکایی به ضربۀ موشکی ایران به جنگنده‌های آمریکا در اردن
🔹
سی‌بی‌اس نیوز: در پی حملۀ موشکی ایران به پایگاه هوایی «موفق‌السلطی» در اردن، چند فروند هواپیمای نظامی آمریکا آسیب دیدند که یک فروند A-10 یک بال خود را از دست داد و حدود ۸ فروند جنگندۀ…</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/farsna/461244" target="_blank">📅 14:25 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461243">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Hohe5tKQrLfXQVB1v4bm9kH84bNWuAqbazsNtw2R5EV5ueLVPLbO9oO9oCm80wYGObP0O2ICA6SNKAQuXcW8GbPS7sa5Xu83wDbfUAp4emH3yqingMCG0bLhL88AoIbIcCcScVjzpNz-aufRMRykMiPNi-riKIsz09yYuxUQKFJYj7CQXt63UsOoIg0YbUBn0_5c8Q4mQvfed_Zqi1tc-sDeMQw-36KlwdJgQXiE0g6UKYQWzyLUojinGi1zcOlaSpLutze-bhI6dUbUo7XdGLvz3CqmLdcydrQ-0Lb2VXMfmHbqOPPWdBzPeXq33ffc2ShmSiTGYQfv1_-3DDpd7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تماس‌ تلفنی
پزشکیان با استانداران استان‌های درگیر سیلاب و آب‌گرفتگی
🔹
رئیس‌جمهور: رفع مشکلات و تأمین نیازهای ضروری مردم باید در کوتاه‌ترین زمان ممکن در دستور کار قرار گیرد.
🔹
همۀ ظرفیت‌های ملی و استانی باید برای کاهش آثار ناشی از سیلاب، صیانت از جان و مال مردم و بازگرداندن شرایط به وضعیت عادی به‌کار گرفته شود.
@Farsna</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/farsna/461243" target="_blank">📅 14:17 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461242">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u1O1NOB2S9ZD8wg1dhhdMiS0KamZ89CKd58aUDcq_E9ABwkp9khLXYuEVO0lpUWcPGlmr3fQqU6aq-VJ8zfQVDVZnjzfVf4MUc2uFMRIsjU_5ESQAy7debc-JDyWbk_MnP7T95ICTTzJ3Mll6gMD2jsmbwXkP0rp05kGda-Pi-Nhjc-EbJKfP-V-2LqzzAVNs3AVi1d5ehDyvuEappnePcjmfl1BTBV-1DUZiQkJXNxitUCTdrRJP5edqrwUaMLKTeU3kIq_TRrLbT2fhtZirBkshZ0Zg6JmM_ML4MDvOpNBoepNvX0OkYTVypVjg6_nUsac73eoxCTDZ2WALl1vNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">«برق من» وزیر نیرو را گرفت!
🔹
تنها یک روز پس از وعدهٔ وزیر نیرو مبنی‌بر پایان خاموشی برنامه‌ریزی‌شده، توانیر مجددا برنامه خاموشی اعلام کرد.
🔹
مشهدی، معاون وزیر نیرو امروز اعلام کرد تاریخی برای پایان خاموشی‌ها اعلام نمی‌کنیم و شاید زمستان هم برق برود. @Farsna…</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/farsna/461242" target="_blank">📅 13:53 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461241">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WfVEJTIzcnvI_jKi8Lv5bGt5HSALPkLl7w29GP8eZ-4WDvRSBvvBHmqzAkhQVlwT1vcIuH8n-1lwhFy2vOt5vT6UqBsWE7DuSRM3JGfhCgHWijJvzH2A9NrSvY1iI_Hj_bGSXwJ-C1NT_ZSpn-QCAEIUPjnY4WQ-1zSNvgNM3CEC2YsAgRPk56jLSxTiSlXxiZ_d-I3GoB6PQWpvhoI3LWCK_82xjxK6C86x20z7r2ttQFbIlOzNyUxXAGgXmwDIECPtOyQ1yqfnUnjorOXYzU4vDm7STZwMpulXwJ5K8j0ICrk1L98wceGZuCdr62xQGyOBlDzBwdF_xlo8lh8rdw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خطر از بیخ گوش زلنسکی گذشت
🔹
نخست‌وزیر نروژ اعلام کرده هواپیمای زلنسکی هنگام برخاستن از مولداوی به مقصد نروژ «نزدیک بود با یک پهپاد برخورد کند».
🔹
پلیس مولداوی مدعی شده این پهپاد روسی بوده و پس از سقوط در یک مزرعه آفتابگردان در ۱۶۰ کیلومتری فرودگاه، ۴ آتش‌سوزی ایجاد کرده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/farsna/461241" target="_blank">📅 13:43 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461240">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">احتمال لغو چند دیدار از هفتۀ هفتم لیگ برتر
🔹
برخی باشگاه‌ها از جمله پرسپولیس و سپاهان سه بازیکن در اختیار تیم ملی امید قرار داده‌اند.
🔸
از این‌رو، ممکن است دیدارهای باشگاه‌هایی که درخواست تعویق بازی‌هایشان به‌دلیل حضور ملی‌پوشان زیاد در تیم امید را داشته باشند،…</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/farsna/461240" target="_blank">📅 13:32 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461239">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rgmJt-Ayd3EW4n7V41U7bVMABRKP5_PrOohaWSqX9K3wg8IJ7KmT4iuH96AAwJWi17Y1r9A5ozwyr2nJbWH3Yc4yK1sSquieudWkH0WKPICg3crDqLOzAhQbMXjBMoOhcmalJFH7RVov5WXouDkx2vPdwN0HWFaq3t6UCCte_81_xMYW9-bAkakxly33lbLDMwK4DikUYgBDxc0kHH3XWPYkFj2MdUtl1Vpmu27RspREOPaZhOP8Yl-b-jP8FJOFgESM_EgXQj6Tcr-KFB_aKBKprJqDx8VCo3O8Cpu04UFke86YWh9aWE_86Ds9MK2Cp9yhlb0xX3XxEypGhGbXLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سکوت آدم‌کش تک‌پا شکست
🔹
سرباز سابق ارتش رژیم صهیونیستی بعد از اخراج از فیلم تبلیغاتی آدیداس بالاخره سکوتش را شکست و با وقاحت تمام گفت: «من هدف یک موج عظیم نفرت و حمله قرار گرفته‌ام و عقب‌نشینی نمی‌کنم.»
🔹
این مظلوم‌نمایی شلو بیتون که یک پایش در جنگ علیه مردم غزه قطع شده درحالی است که ارتش اسرائیل بیش از ۵۰۰۰ نفر را از کودکان و جوانان فلسطینی را قطع عضو کرده است.
🔸
شرکت آدیداس هفتۀ گذشته با انتشار ویدیویی تبلیغاتی با حضور این سرباز صهیونیست تک‌پا به‌دنبال تبلیغ «کفش تک‌پا» خود برای افراد معلول بود.
🔹
این فیلم واکنش مردم جهان را به‌همراه داشت و آدیداس را متهم به پوشاندن جنایت سربازان اسرائیلی در غزه کرد، در نهایت مجبور به عذرخواهی و حذف این فیلم شود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/farsna/461239" target="_blank">📅 13:29 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461238">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6de0bc5dcf.mp4?token=LndcrV_iowEJlRKuCc68aWFawDLhpOgEH74SVQyBwTXKXC9Nm8M7M8n78vrO3LQ7_FobMQUGhfTy59_CmA_a_Stzpr83W3DhHZ2RzXb07E8XG6iNHfD6hJvfOdL7QnYJUAJsBaP7BxxrO0NI3jZhbM1OKLqPFnp69JwYZs9LTjYfMZ096KAvReWOito98rAe8Y2TzuIjr6x8o9T8jq5bpJ3nDg31a7jd_FnyP4hsoD8alqQCLYwNk6eUv_5WR-LQ8K6P0FhGjopHdZnpCH9QEafOjCcGQnWBPCDyujQ2BKcGBUMCNmdfPBq9WO_ln4gmzNsJ8HdBKx1Q2z8NQu1REoWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6de0bc5dcf.mp4?token=LndcrV_iowEJlRKuCc68aWFawDLhpOgEH74SVQyBwTXKXC9Nm8M7M8n78vrO3LQ7_FobMQUGhfTy59_CmA_a_Stzpr83W3DhHZ2RzXb07E8XG6iNHfD6hJvfOdL7QnYJUAJsBaP7BxxrO0NI3jZhbM1OKLqPFnp69JwYZs9LTjYfMZ096KAvReWOito98rAe8Y2TzuIjr6x8o9T8jq5bpJ3nDg31a7jd_FnyP4hsoD8alqQCLYwNk6eUv_5WR-LQ8K6P0FhGjopHdZnpCH9QEafOjCcGQnWBPCDyujQ2BKcGBUMCNmdfPBq9WO_ln4gmzNsJ8HdBKx1Q2z8NQu1REoWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پیشروی برق‌آسا در المخا؛ انصارالله به دروازه باب‌المندب رسید
🔹
منابع رسانه‌ای از پیشروی برق‌آسای نیروهای یمنی در المخا خبر دادند. پیشروی‌ای که از شمال به ساحل و از شرق تا فرودگاه این بندر استراتژیک رسیده است. تصاویر منتشرشده، فرار و فروپاشی شبه‌نظامیان سعودی را در چندین محور جبهه‌ها نشان می‌دهد.
🔹
برخی منابع رسانه‌ای نزدیک به عربستان نیز گزارش دادند که نیروهای مسلح یمن بر بندر استراتژیک المخا در دریای سرخ مسلط شده‌اند. هرچند که دشمن سعودی طی ساعات گذشته حدود ۴۰ حمله هوایی به استان‌های تعز، الحدیده، الجوف و مأرب انجام داد تا شرایط را برای پیشروی نیروهای صنعاء دشوار کند.
🔗
شرح کامل این گزارش را
اینجا
بخوانید.
@FarsNewsInt</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/farsna/461238" target="_blank">📅 13:19 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461237">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EPsGpHE-Hq4l0wJySE3s0in31E2ftg1ET1PCAU9sSV0TtaYMHVmKNylhDRbvr-KCEdI55nWJ6jBiS2StXXto-GUgEURCn2qPsR3gHfO7AK0Ld5OOaBv8bOAuQZ8rXfImKWaiNSgNFTEikINyH30XvBzwmBQk63jjo3agXnLG0sqksCXeROksYVwhlvj6UmfUGbUaW1-meODk_oMrDyzsu9OMr9DKgu-DZDJPP4uWed-hLlaRcUjRM9vB-MzPN3WkyPbyMNxmkFU_P-HXgwWlmJ0bFZFCWDO0-fww9UKoquwo7GJu7uuNGmRgTJQbmpM4Rs9dQeyX1p-HP2SxgmRINg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دولت کرایۀ حمل مایعات نفتی را کاهش داد
🔹
معاون حقوقی رئیس‌جمهور در نامه‌ای به معاون وزیر نفت، دستور توقف دریافت ۱۰ درصد از کرایۀ حمل مایعات نفتی و گازی وارداتی و صادراتی توسط ناوگان دریایی غیرایرانی را ابلاغ کرد.
🔸
پیش از این، دریافت این هزینه از کرایه حمل کشتی‌های خارجی، هزینه جابه‌جایی نفت، گاز و فرآورده‌های مایع را افزایش داده و تجارت این محصولات را برای فعالان حمل‌ونقل پرهزینه‌تر می‌کرد.
🔹
توقف موقت این دریافت، با کاهش هزینه‌های حمل، می‌تواند انگیزه و تمایل ناوگان دریایی خارجی برای حمل‌ونقل کالا به مقصد ایران یا از مبدا ایران را افزایش دهد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/farsna/461237" target="_blank">📅 13:10 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461236">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">شکار پهپاد مسلح سعودی در آسمان یمن
🔹
سخنگوی نیروهای مسلح یمن: یک فروند پهپاد جاسوسی مسلح دشمن سعودی از نوع «کاریال» هنگام انجام عملیات خصمانه در حریم هوایی استان حجه با سلاح مناسب سرنگون شد.
🔹
استان حجه در شمال غرب یمن، دارای خط ساحلی و مرز مشترک با عربستان است.
🔸
کارایل پهپاد تاکتیکی ساخت ترکیه است که در اصل برای شناسایی، مراقبت و نظارت طراحی شده بود، اما نسخه‌های بعدی آن به قابلیت رزمی و حمل سلاح نیز مجهز شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/farsna/461236" target="_blank">📅 13:04 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461234">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0f7f705f73.mp4?token=UX7D_hSXvDABAYe_TRTSpkhZ5Pg7_xxiwkjXsz5vCWInp7o3CVOTs4LgVXeFjB8qq5BMz5urjQcowqK92kRdfrtJvLfJ031bvlpJJvEn5exbVxZbOT_QMQmFPpHNgM6hc7LRJrgR_6HdQDluur6GMXAohddVhPcaX1Bc0uhbeVoA1y-0RQrwTWX_M2cBZx2dhuGUywnsSdqy3L__fPmLfD2sjPprDbDCMm08C5aBR-9l8StDfrTSvxO6og0sCdB6xGGG92TmPVGu47KLfZPNFXQhR5drE0eGfmTQJ_hVGhsIIS9Rmog3qgWIvVz8e2C22sWCDK5XmmyyWUGJslr-3g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0f7f705f73.mp4?token=UX7D_hSXvDABAYe_TRTSpkhZ5Pg7_xxiwkjXsz5vCWInp7o3CVOTs4LgVXeFjB8qq5BMz5urjQcowqK92kRdfrtJvLfJ031bvlpJJvEn5exbVxZbOT_QMQmFPpHNgM6hc7LRJrgR_6HdQDluur6GMXAohddVhPcaX1Bc0uhbeVoA1y-0RQrwTWX_M2cBZx2dhuGUywnsSdqy3L__fPmLfD2sjPprDbDCMm08C5aBR-9l8StDfrTSvxO6og0sCdB6xGGG92TmPVGu47KLfZPNFXQhR5drE0eGfmTQJ_hVGhsIIS9Rmog3qgWIvVz8e2C22sWCDK5XmmyyWUGJslr-3g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حملۀ شهپادی اوکراین به «سوچی» روسیه
🔹
درحالی که هشدارها دربارۀ احتمال قطع دسترسی اوکراین به دریای سیاه در نتیجۀ جنگ ادامه دارد، بندر سوچی روسیه هدف حمله قرار گرفت.  @FarsNewsInt - Link</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/farsna/461234" target="_blank">📅 12:59 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461233">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/281b0f925e.mp4?token=dv9mtOqTrARAA2U4_T4Kj4z0yyY6ha-DvJJ76ahc2TC4D-EVc-bIri0XKEJnGZy2BguTzY1kX8sLtoBofp14yL7B3z8Cws05jheFK92sq2OCJkqBt4JiH9ewZz-mETeh-IBnPhRCbVV2b8P9l-1LRqVi2ngYYuyUQy2rbrOc3EH0ISwsfgOs_Ut_fHNClECQ2modnDBk3zrwIdgDBCVIqsGuQHAeZ8DKgJHUrlY-SifPiNQRUIiW2pLMGJBbUN9DDWFokbO0rk5MAnKv5VTphq5xUDYGpU-h8emd901LUr1AOH_hEaMu5nT98c0c4ZJcoK-68Ui0WOHSsDwtisOT5w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/281b0f925e.mp4?token=dv9mtOqTrARAA2U4_T4Kj4z0yyY6ha-DvJJ76ahc2TC4D-EVc-bIri0XKEJnGZy2BguTzY1kX8sLtoBofp14yL7B3z8Cws05jheFK92sq2OCJkqBt4JiH9ewZz-mETeh-IBnPhRCbVV2b8P9l-1LRqVi2ngYYuyUQy2rbrOc3EH0ISwsfgOs_Ut_fHNClECQ2modnDBk3zrwIdgDBCVIqsGuQHAeZ8DKgJHUrlY-SifPiNQRUIiW2pLMGJBbUN9DDWFokbO0rk5MAnKv5VTphq5xUDYGpU-h8emd901LUr1AOH_hEaMu5nT98c0c4ZJcoK-68Ui0WOHSsDwtisOT5w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ترامپ: اگر ایرانی‌ها سلاح هسته‌ای داشتند، من به رهبر ایران زنگ می‌زدم و می‌گفتم: «آقای رهبر عالی، حالتان چطور است؟ کاری هست که بتوانیم برای شما انجام بدهیم؟»
@Farsna</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/farsna/461233" target="_blank">📅 12:35 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461232">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YpZ1nZ82lGIYotoi6jmkQhVdMvMGI2rs6RxrHMtv6QVUOmTsH3wRmEomlx0WMymuvjdom8S51MMo-YP-IShitWuK_ahbeaUa3oHiRNVp38wYjCLu_epovH0qZ3vaLEpO1QUiEO0IwOHfPTJFhPYcPlQ5Dz_N8yxsYOhbcEsly5C9T0cGwTT1N0bCDttOerN-i2Xoxveq55WJDGlsSVVv3KJZu6pFSKcJdUEIICq8iQZQODzFU_9QFRBwD6LkfZTfh9qQIf9STBXvZZI96vhdevmGLvk8YcBEgU8uLpIfHkFcuHjS_9OILpRwmjgUjpG2R8pAs8VungjrLzOMCaPdfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پزشکیان: سالن‌های همایش و استخرهای متعلق به دولت ادغام می‌شوند
🔹
در مدیریت فرایند اصلاح الگوی مصرف، دولت پیشگام است و شخصاً بر جزئیات این روند در مجموعه‌ای که مستقر هستیم، نظارت دارم.
🔹
به‌منظور افزایش بهره‌وری و صرفه‌جویی در مصرف سوخت، بیشتر سالن‌های همایش، استخرها و ساختمان‌های متعلق به دولت برای عبور از بحران تعطیل یا ادغام خواهند شد.
🔹
همچنین توسعه و تسریع در نصب پنل‌های خورشیدی سقفی در واحدهای دولتی همچون استانداری‌ها در دستور کار قرار گرفته است.
🔹
از سوی دیگر سیستم روشنایی و گرمایشی هر نهاد دولتی در فصل سرما با الگوی کاهشی کنترل خواهد شد.
@Farsna</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/farsna/461232" target="_blank">📅 12:33 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461231">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EmlNnzQPc9j8G0XMXaiIYxkoOY6XK4o-TgfxRVpj-I8M6B28F2-_2eA21KFXGvS4OpbwH4IPpHJu-aM_iEWvUAJBWGlgkyWp1yl7R7UEe2bYkDv4dz6QOFBDYdqISeROqhwcN-4_AQozQHUzg92IUhRtUd_LMO8GStBuSHQlGW62RabmWmzI0q42XnlHAQ2ueDmK8faX3kqVH40jhmBwp7I8b3JmS0q2aIvfqHfEsP90SrTNR9JVcEbkxMMrMslednSymFSdIfxDbUNk_YVpXn-LsOta88P_Budda9kMbs15Cr9UdvCHsTXzZ30Qm4q1oKYzwpMHj_8CNTi1FJRS9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جزییاتی از بازگشت پرقدرت مبین برای تامین نیازهای یوتیلیتی پتروشیمی‌های عسلویه بعد از حمله دشمن
🔹
شرکت مبین انرژی خلیج‌فارس با انتشار اطلاعیه‌ای در کدال آخرین وضعیت خود پس از حمله دشمن آمریکایی - صهیونی به این مجتمع را اعلام کرد و خبر داد که ظرفیت عملیاتی این شرکت به ۶۰ درصد در مردادماه ارتقا یافته است.
🔹
در این افشای اطلاعات بااهمیت الف آمده است: از تاریخ ۹ اردیبهشت‌ماه با در مدار قرارگرفتن فاز یک شرکت پتروشیمی پردیس و بعضی از شرکت‌ها تا پایان اردیبهشت‌ماه، با ظرفیتی حدود ۱۶ درصد، خردادماه با ظرفیتی حدود ۵۰ درصد، تیر و مردادماه با ظرفیتی حدود ۶۰ درصد، عملیاتی شده است.</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/farsna/461231" target="_blank">📅 12:27 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461230">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Jg0bkKCxULP2Nu2nrkLcanjr26G7vfbEY3z-MdI-IyamMWSJQ1hIkPIB6h-Wd6PU42iu3o0ATZhGiT-VknQnkFUNUwc2XrgxdFYFEJv7Yoq3415gg9k0KeEOPlVrUAyVrGWrC8weByh-45C6P0T03MbKtHV6b2NGLOy3yGrlt5C7wCLkoeKX60oMauNcmDjZtfsBekj0_k4sHDvFXjb5u3KJzHVtnS8J0AQP56xkPXngHI9hkIHWghamOOZPye_xvZwyxG_fT1xz1lzs4hBJOi3WyqtKmYDW2HSpheHdFZfBcyj3Eday0HbujFV4PfdHjuOcEiPxkSj-9PvBLiaEhg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎉
یکشنبه‌ها در پارک آبی اُپارک، بازی‌های گروهی منتظر شماست!
در سانس بانوان، در کنار آب‌بازی و تفریحات اُپارک، در بازی‌های گروهی شرکت کنید، با دوستانتان رقابت کنید و شانس برنده شدن هدیه‌های ویژه را داشته باشید.
🎁
🏆
🎟
برای خرید بلیت به سایت اُپارک مراجعه کنید</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/farsna/461230" target="_blank">📅 12:26 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461229">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/farsna/461229" target="_blank">📅 12:25 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461228">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس ورزشی</strong></div>
<div class="tg-text">اعلام آمادگی رئیس‌جمهور برای واگذاری استقلال به بخش خصوصی
🙍‍♂️
سرپرست مدیرعاملی استقلال: اگر به دولت می‌خواستم بروم، جایگاهم کمتر از معاون رئیس‌جمهور و وزیر نبود اما محدودیت رئیس‌جمهور را درک کردم. او خبر نداشت به استقلال می‌روم. در دولت جلسه‌ای بود که چرا مجموعه‌های دولتی تیمداری می‌کنند. من یکبار وقت گرفتم و برای ایشان توضیح دادم.
🎙
رئیس‌جمهور گفت آمادگی دارم که اگر سرمایه‌گذاری در بخش خصوصی باشد بتوانیم استقلال را واگذار کنم.
@Sportfars</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/farsna/461228" target="_blank">📅 12:04 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461227">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ptD-eD_3YhBmWv6gPxVTp4vJE-tMEQNgCPatgjAPzkDmgOyf2UzHwTnNzKmenbLXsyBQptK_SAysMaMgCnI30zO7DQ7HsZsZkAGmcXyVWhGHbWbLkHX_7Ia-cL6GlyYJWwCa7YxadSs6_cIEVIevnblbC5vJectSFMf34WW8a3fdDkRUlimIZFuApa1nBaXn5idsihTNIhWzkG5pyIVj0sHQXHP9wxASWKFc3mc4KQmQuxvkMXEyYPOcE3QcTJcCLB9HvokALQio3w-q98IrGt4mep8Ash7C3eTcVHtpyK40QunaBINSk-j-pdXH04xldVA6JDs-gsnh6oDTtRyp_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎥
خسارت سیل به ۷۷۲ واحد مسکونی در مازندران
🔹
مدیریت بحران مازندران: در برخی نقاط مازندران بیش‌از ۲۲۰ میلی‌متر بارندگی ثبت شده است.
🔹
تاکنون ۷۷۲ واحد مسکونی درپی بارش‌های سیل‌آسا خسارت دیده‌اند که بیشترین آسیب در ساری گزارش شده است. @Farsna - Link</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/farsna/461227" target="_blank">📅 11:54 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461226">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XXsP5BY2glNC5hldibPLO8r3b_IHbTY4ZnYCX2Ebx7DkMH8IomtXRh0A5egeQf8bvUzGPtkECEvEOwnIcCe2yvEustZ-zylfnsWAuJZJJu_7-O5a7XvogePAKl4UchI8pOIO2YZPKqyBxzVpHXOpaa2QNL1EiWXKg3OPtFJnU1d0H4c-Ydtloe96qeysylRxmUt3zrpAvlamFPOZANUkhyCbSBk-2oJBK01H8i2tiX6purY5z3hhqmk-mxhrCEq2IbPgX5poe21lDJwwV40pRpcZgUAQetncprxYhiNpW-gEL8iwNAZ3FCkKK40n36Fw0fs07p7fti68yf2rVEcL_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">افتتاح ۹ کیلومتر از آزادراه حرم تا حرم
🔹
۹ کیلومتر دیگر از محور آزادراه حرم تا حرم در محدوده گرمسار-سمنان به بهره‌برداری رسید و عملیات اجرایی پروژه محور سمنان-فیروزکوه نیز آغاز شد.
🔹
مدیرعامل شرکت ساخت و توسعۀ زیربناهای حمل‌ونقل: ۱۵ روز پیش عملیات اجرایی قطعۀ نیشابور تا مشهد نیز آغاز شده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/farsna/461226" target="_blank">📅 11:38 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461225">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZeXTvMG1ps7RO0pt7M9Xytu-f63ZBUmcdB3kIqzywLGKa7eH9zULxYgrLKzjwjVbCgKSuWTwkT9-NzT3EwfeY0Poovg9e2mSO9Lqn_LYZSKCC4u3yQ0zQx2MAALhhtKwJmX4DdJU2K93csl9HFG2thlub2Z5ZJeBkmYMNk4GfQHvzf0KGbHmsCgIp4wg1K2oJnGikHDgVjNKixSaQsBgDwVqhHOmaPI8njWp59Ho7zgawNSFHivSJxT7TEUQ-rJpX3thsJ1rAsnlDaqMU9Kua9E4btbOin-ljRTMubThjbRPfPlKqYmlNrP_WEi8N564ImN1NMby4xWow5WT-1Tlkw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‌ سخنگوی قوه‌قضائیه: فاطمی‌امین و ساداتی‌نژاد به‌دلیل بررسی درخواست اعمال مادهٔ ۴۷۷ به زندان معرفی نشده‌اند
🔹
در خصوص پرونده‌ٔ چای دبش ۹ نفر به زندان معرفی شدند که در حبس هستند.
🔹
محکومانی هم که در حبس نبودند برای آنها ابلاغیه صادر شده و چون حاضر نشدند، حکم…</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/farsna/461225" target="_blank">📅 11:20 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461224">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a83d26ff4c.mp4?token=W1GRVJa7J225JpOSwhokpmvb7BTiExpKju4Ot_LES95-GRYtOQeqjZO48bwSD2JsL7tCZWxgmlam1c6C8MT5W3KFZ2dCP3uBhPZztnWImI_RoYX3mHG_oHZzYAXWfRMkKBp4AH765mH92r3V0yrpseZhij-HIsEOVZ8ou1JXk1-laOuuO55wMsZRDBUUXnookCbzTpFF8FHZXtBD0YsOTKqt7uhcrhKBj0zGoyCHbv8L26RHGp_GuezOj_ie27MjZLuGd6v6U6d_aIHOjbBTKe6UECLWlBFnsYInAuhaLOkLyTs_Rf6VLu0i5fggB0gDumUN3wNzY0BwGsfacuXX2w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a83d26ff4c.mp4?token=W1GRVJa7J225JpOSwhokpmvb7BTiExpKju4Ot_LES95-GRYtOQeqjZO48bwSD2JsL7tCZWxgmlam1c6C8MT5W3KFZ2dCP3uBhPZztnWImI_RoYX3mHG_oHZzYAXWfRMkKBp4AH765mH92r3V0yrpseZhij-HIsEOVZ8ou1JXk1-laOuuO55wMsZRDBUUXnookCbzTpFF8FHZXtBD0YsOTKqt7uhcrhKBj0zGoyCHbv8L26RHGp_GuezOj_ie27MjZLuGd6v6U6d_aIHOjbBTKe6UECLWlBFnsYInAuhaLOkLyTs_Rf6VLu0i5fggB0gDumUN3wNzY0BwGsfacuXX2w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
رئیس قوه‌قضائیه: طرفدار پروپاقرص برگزاری دادگاه‌های علنی هستم
🔹
برگزاری دادگاه‌های علنی هم به نفع خودِ قضات است و هم به سودِ مردم است چرا که دانش و آگاهی حقوقی و قضایی آنها را بیشتر می‌کند و از این طریق از وقوع بسیاری از مفاسد و کلاهبرداری‌ها پیشگیری می‌شود.
🔹
بازدارندگی دادگاه علنی از حکم‌ نهایی می‌تواند بیشتر باشد؛ دادگاه باید علنی باشد و برای مردم پخش شود.
@Farsna</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/farsna/461224" target="_blank">📅 11:16 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461222">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lcMoqJqpp6OOfliPWeUTTe2W8Uzr8pD7HduCxCYz3Pk6sh5DXiNfsTYUsc8nkvfp7za0T7Wb5VJrzk2_5KqqzkgfrQK7lLTazzswTzv8Ylg1iGNAB3YhRMpTlCHojtBcD5KSXUMfNlnw7KY7nWM-yO3Dwdnvn086gfKgfUE_Rr65a-fk9J1BhUwtYlP6H_6o9b9WGpyvttfmHPSE5NopbYwzBGmPviO8dpJzrBjXz4WTjJFqhA3l0dJ8uwxlrAkAONIzGbICAWH07d6uiglYc6naHIHzXhqukyBtB1XlzReQRuddQ7kiAVE2vYxMy6txoTYOygAN2EsYd6o2tl6oPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IenqW8Mfh8d23pZa-x2Vzb_OhpRrylfDTLyVt0I9UJOKfn2UgMWTLffiKJyAXWR8jsy2F5HjffnTmitKm-OVoxEAlO87Z0w-uQD3SPvmlfU-bG-CuE2W5tazCF6pDGKCMt6PnoF5T_0Khh1_SBmwcErAzJaFRU6k6l-J92upyz8Q-_PVZbLjefw4x52pvvfpxBkMm8GD-QX8_Dla9XEig0Xaz6uvub8GZmi9I00XgRspiAKXiBwd7xUH6582yO5QzWExdUH1SJ3NI_x9ImgiEjiMxVvHAflRmHOfceAz1-XQR2ZpYV5K6AoqIlJFDBWQkwkndy2V_MgaISzuN3h7_w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🔴
سخنگوی نیروهای مسلح یمن: شرکت نفتی آرامکو و پایگاه هوایی خمیس‌مشیط را هدف حملات متعدد قرار دادیم
🔹
یحیی سریع: دشمن سعودی جنایتکار حملات ظالمانه‌ای را علیه مردم ما انجام داد. ما در پاسخ به آن، عملیات نظامی مهم و گسترده‌ای را انجام دادیم که در آن شرکت‌های…</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/farsna/461222" target="_blank">📅 11:08 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461221">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8605b20068.mp4?token=D_fQiX9V1zOyLyzN5RxUsCBY7akt--_EuMzGvScyk0hVYNzBIAi-Ri-jXAt3QbfsyraLYWhlrUg-GhUj_AFvzIsyCzUdP75f79tv0CtV1DhosNGrTxxRQ5VpCFCustpYrQlBTyyU2xgy0s5K8z_vsKV_l0Mmw_tAQTga8j4rWwZnSy-eIn8PHwq4YmtMx1dWsz87TI6HnHQsWA_8kUbcUNzdeONm0FzfUXCCbvry6yXo_vPWSgKf4mUXGxye-vVrixpCyzBMUnbeEwCBNgoe0nGDrLWNxK7C7M546tfMW6k27osHFvgQRUHgmbomzQHXbw3C7lNwm2xU3ENQYP5lyA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8605b20068.mp4?token=D_fQiX9V1zOyLyzN5RxUsCBY7akt--_EuMzGvScyk0hVYNzBIAi-Ri-jXAt3QbfsyraLYWhlrUg-GhUj_AFvzIsyCzUdP75f79tv0CtV1DhosNGrTxxRQ5VpCFCustpYrQlBTyyU2xgy0s5K8z_vsKV_l0Mmw_tAQTga8j4rWwZnSy-eIn8PHwq4YmtMx1dWsz87TI6HnHQsWA_8kUbcUNzdeONm0FzfUXCCbvry6yXo_vPWSgKf4mUXGxye-vVrixpCyzBMUnbeEwCBNgoe0nGDrLWNxK7C7M546tfMW6k27osHFvgQRUHgmbomzQHXbw3C7lNwm2xU3ENQYP5lyA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تخریب عجیب یک کاروان‌سرای تاریخی در سبزوار
🔹
رئیس میراث فرهنگی سبزوار: کاروان‌سرای روس‌ها یک ژاندارمری و بنای تاریخی در کنار کمربندی شمالی سبزوار در دوران پهلوی بوده که در زمان اشغال اتحاد جماهیر شوروی، نیروهای نظامی در این ژاندارمری خارج از شهر مستقر می‌شدند.
🔹
این بنا سردر باشکوهی داشت که برای ثبت در فهرست آثار ملی اقدام شده بود. طی این مدت هم منطقه‌ای تاریخی شناخته می‌شد و در نقشه‌های ابلاغی به‌عنوان بنایی ارزشمند معرفی شده است.
🔹
تصاویر منتشرشده در فضای مجازی دربارۀ تخریب این اثر تاریخی توسط شهرداری مورد تایید است. مجوز تخریب احتمالا با جمع‌آوری استشهاد محلی صادر شده.
🔹
با توجه به نقشه‌های ابلاغی این تخلف محرز است و آن را پیگیری قضایی خواهیم کرد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/farsna/461221" target="_blank">📅 11:06 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461220">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/31609f5c7e.mp4?token=sdDhpp-2rJcAavxoN6OH0GiHSXo0KGnrl3D51WzqynomxeB8c-fMLV7tczoS348aD3VHlhgbw7M7r7hEH4OYe-pDBCumQiZ8QgURWRk6ZSJHssmVr-QUeJVCBrbXPwDka_zt--NvK-4o5XRbaypogp870_BcpGEkTMA2NSz4BB3om8RHM8chy7XYC9z6o7IuC68gO3P_lVuPF0OBfloUMQogl0cqDkj0bdyuzvYTu5r5Z9pkMNRM9aJlhgYuckygPaFlOowk7HcO_8bt4iTUvk6TjGzOjenVhx7Wsc_yevZ6QuawLHn6L3peRxqdkRA-tksz_teSAKfh_m4q9I6kFw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/31609f5c7e.mp4?token=sdDhpp-2rJcAavxoN6OH0GiHSXo0KGnrl3D51WzqynomxeB8c-fMLV7tczoS348aD3VHlhgbw7M7r7hEH4OYe-pDBCumQiZ8QgURWRk6ZSJHssmVr-QUeJVCBrbXPwDka_zt--NvK-4o5XRbaypogp870_BcpGEkTMA2NSz4BB3om8RHM8chy7XYC9z6o7IuC68gO3P_lVuPF0OBfloUMQogl0cqDkj0bdyuzvYTu5r5Z9pkMNRM9aJlhgYuckygPaFlOowk7HcO_8bt4iTUvk6TjGzOjenVhx7Wsc_yevZ6QuawLHn6L3peRxqdkRA-tksz_teSAKfh_m4q9I6kFw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
امضای پدر رهبر شهید پای میراث سردار سلیمانی
🔹
نسخه‌ای خطی و نفیس از میراث خانوادگی سردار شهید غلامرضا سلیمانی، پس از بیش از یک قرن، پرده از بخشی کمترشناخته‌شده از پیشینۀ فرهنگی و دینی این خاندان برمی‌دارد.
🔹
کتابی در حوزۀ اخلاق و احکام که در صفحات نخست آن، نام و امضای چند عالم برجسته از جمله آیت‌الله سید جواد خامنه‌ای، پدر رهبر شهید به‌چشم می‌خورد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/farsna/461220" target="_blank">📅 10:55 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461219">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Oj4sFBNqCMjTvlXswLqxRtb4PZdlCeVKTRqikntgPlxfXWZVi0Rjxh_g5VJIIPt3mCEZoGwRMvwCeDpah7JDMJ7Wy-jNElM0fC8czpL_JX63A0bi1MANY9WVdu_EnzE-DRFtCaOr6mEoGGTbxOp9zsS9fyiIHSpRTl2X4oaIiIwfG11E2x1uTAss9VVrTdjg4ohxu-PLnj8OFj5h5t_zd0VnREPoo4BPzvMwysjC1kv2o6Gnps--ipnveX5JrMIWVngBbjXtI47GDeqNODnAvmNRINKS2bWFh8vyGUfzpH3C6v8rQ8WVn0waCipd9n59KqBX5bpg77HUMw8XIHSV7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سرلشکر صفوی: جنگ‌طلبی آمریکا، شتاب‌دهنده برای انتقال وزنهٔ قدرت به شرق بود
🔹
مشاور عالی فرمانده معظم کل قوا: جنگ‌طلبی آمریکا، بهترین شتاب‌دهنده برای انتقال وزنهٔ قدرت و جغرافیای اقتصادی به شرق بود.
🔹
تظاهر به فتح نشان شکست و قبول چندقطبی شدن قدرت و امنیت بین‌الملل است.
@Farsna</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/farsna/461219" target="_blank">📅 10:52 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461218">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">بازداشت گردانندگان کافه ازمیر بروجن
🔹
روابط‌عمومی دادسرای شهرستان بروجن در چهارمحال‌وبختیاری: گردانندگان کافه ازمیر به‌دلیل ساخت و انتشار یک کلیپ مبتذل تبلیغاتی در فضای مجازی، با دستور قضایی بازداشت و روانۀ بازداشتگاه شدند.
🔹
این کافه نیز به‌عنوان محل ارتکاب جرم پلمب شده. امسال تاکنون ۲۰ فعال فضای مجازی متخلف تحت تعقیب قضایی قرار گرفته‌اند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/farsna/461218" target="_blank">📅 10:20 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461217">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tWC_rOnvok1n38iC8t0pu5QLku13sphSxdS4aoojXcx74HgxV25qGb0EHLANE-tLi9g1qxrtVAHkoG5sElCGVtQ72C4mKyKemNmiH8D27yEkywmT-MgEsesOkyWPs9st5BwbvfrgfY_LzX1pSfXTM2FgvXn_6KMMlBsLHb9nDB2T1QYxEaetbOMTUsx1u70wEhwYEHw1oPSWC316APSGKZVRy9zdq6qnLHYuAgnvUziLMGyrf4QM1c88AEmYmhUXBAp9wQmhkS0eLvKND7cFCpZ6TpNNsHya74vO1SpEy7_JDHjiJamE9iM_TgTmPcPsLVbdd-Vt4GJF3xt62eetVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کسری بودجۀ آمریکا در ۱۱ ماه به ۲ تریلیون دلار رسید
🔹
دفتر بودجۀ کنگرۀ آمریکا اعلام کرد کسری بودجۀ دولت این کشور در ۱۱ ماه نخست سال مالی ۲۰۲۶ به حدود ۲ تریلیون دلار رسیده؛ رقمی که در صورت ادامه، تا پایان سال مالی افزایش خواهد یافت.
🔹
براساس این گزارش، بدهی ناخالص ملی آمریکا به‌تازگی از مرز نگران‌کنندۀ ۴۰ تریلیون دلار عبور کرده و اکنون هزینۀ سالانۀ بهره بدهی بیشتر از هزینه‌های دفاع ملی این کشور شده است.
🔹
«مایا مک‌گینس»، رئیس کمیتۀ بودجه فدرال مسئولانه گفت: «بدهی دولت آمریکا به طلبکاران خارج از دولت از اندازه کل اقتصاد کشور فراتر رفته و صندوق‌های امانی برنامه‌هایی که دهها میلیون آمریکایی به آنها وابسته‌اند در کمتر از یک دهه با خطر ورشکستگی مواجه خواهند شد.»
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/farsna/461217" target="_blank">📅 10:07 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461216">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AsCoCtyPRbFx3jpJ5yc_VsYDP1jsroWhjkGAhd__szbsuEpdKU7RWUDskSUyhciLciQy1-QvBV7T4CKIKqYgiGkvn_yd4Oq84YMqlz5y5gZtg4tqXQbWAGKO5_8GkUZr7jdHPw8ii4F2m4H9QOMNPbEFBpo1VrLUr4R6g9vtnD5AtINeVulSIlcXXDsP8u0LJlP5ft_Qp35Jkum1cRkX7HK5aIVQjqZM0lUJhissUHQVTHvL18sybGPm8T6RDMTAwE4tUs4g5j6IcY3zxw04qVJOkFua5zO5dPPxL5zz2x1qokbAqZwWNpmcP-7nCGnj6t8FZKNjVU_c32viA6vR0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎓
فرصت طلایی ورود به دنیای رسانه با ثبت‌نام در دانشکده خبرگزاری فارس
اگر رویای فعالیت حرفه‌ای در رسانه را دارید، اینجا شروع قدرتمند شماست.
✨
چرا دانشکده رسانه فارس؟
✔️
آموزش تخصصی با برترین اساتید رسانه‌ای کشور
✔️
کار عملی از ترم اول در تحریریه و باشگاه خبرنگاران توانا
✔️
رشته‌های جذاب: خبرنگاری، عکاسی خبری، سینما و تدوین، گویندگی، روابط عمومی
✔️
کاهش هزینه های تحصیل با کار وتولید محتوای حرفه‌ای در باشگاه توانا!  (مهارت و درآمد)
✔️
پشتیبانی از اشتغال و همکاری با رسانه‌های معتبر مانند خبرگزاری فارس
📌
شرایط ثبت‌نام:
🔹
ارسال عدد ۱۴ به ۵۰۰۰۱۰۱۴
🔗
یا ثبت‌نام از طریق سایت
futurix.ir/go/rxDxXO
🔹
پذیرش پس از مصاحبه و استعدادسنجی.
🔹
ظرفیت محدود است.
مرکز آموزش علمی کاربردی خبرگزاری فارس</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/farsna/461216" target="_blank">📅 09:45 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461214">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4b5538027d.mp4?token=v7IqmQ4-TTel2YkbjoZ36V-RTchaPpIQpVevbCKF8KsXkZzLe1dYDNg4OYulHIn_IYmsEMV8N8LKk4ybHarAPgm8v5_B86zvLftYdQnh8V7U4N538fbIi3Ymp_p0HVvABaDEhDh8GjnloNQR7_DZHDpkekGZUO3WmKGEP_90Wv1XC4rAe4AjOvfdDMxMwunI2M5U2gPrKtkJ7VPqjYIrG8KOXOJJNbvVwDS9V4Ybr2w3qRvZKPUNTY6ezQKiaIB35zXU-Adg3pbrkxe6ZqVnZSs2nkEGIOlYf0HM7v1vO827vXaiqDicGoTouz6P8gVSWA1b7x8aILa9w44neBwbRw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4b5538027d.mp4?token=v7IqmQ4-TTel2YkbjoZ36V-RTchaPpIQpVevbCKF8KsXkZzLe1dYDNg4OYulHIn_IYmsEMV8N8LKk4ybHarAPgm8v5_B86zvLftYdQnh8V7U4N538fbIi3Ymp_p0HVvABaDEhDh8GjnloNQR7_DZHDpkekGZUO3WmKGEP_90Wv1XC4rAe4AjOvfdDMxMwunI2M5U2gPrKtkJ7VPqjYIrG8KOXOJJNbvVwDS9V4Ybr2w3qRvZKPUNTY6ezQKiaIB35zXU-Adg3pbrkxe6ZqVnZSs2nkEGIOlYf0HM7v1vO827vXaiqDicGoTouz6P8gVSWA1b7x8aILa9w44neBwbRw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
آتش به جان کشتی فیلیپینی افتاد
🔹
آتش‌سوزی در یک کشتی مسافربری در سواحل غربی فیلیپین، ده‌ها مفقود بر جای گذاشته و جان دست‌کم پنج نفر را گرفت.
🔹
سخنگوی گارد ساحلی فیلیپین نوئمی کایابیاب، خبر داد که تاکنون ۴۳ نفر نجات یافته‌اند. او گفت: «ما به عملیات جستجو و نجات ادامه می‌دهیم.»
@FarsNewsInt
-
Link</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/farsna/461214" target="_blank">📅 09:42 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461213">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RjzfOkHKf6vUSIznqShazbq4W93loJYmWI1K1DLchsHWYChqPAKNGhFtWZOUkZP2bbq23xDK4pz8FpTr_XqwF7VoIRIjLi584rmJMKMzMV7qXlX89rN7L-7Q13vPclJA58gFoNCV7-xmjt_fHFsFGMkpgnAbl0E2by7k2w-TAIEkPmoPg_v7oF7VD88wIhivAO3bHgpbcIAb90f2HBgLsNRTYagksdJzOYAk41epe8I2pGrnnKttTHNc9fXuJKRHztCW0VW6GaKHQCNrL5M_sBMz1tSxxU6d6eNCFmQa64lMDiWwq6iBjuK4ykrZMUCegyz3sKF1HLrMcesxAzOAMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سردار حسن‌زاده: آمادۀ عملیات‌های تهاجمی برق‌آسا هستیم
🔹
فرمانده سپاه تهران: امروز آمادگی داریم در هر نقطه از کشور، با سرعتی بالا حضور یافته و دشمن را در هر وضعیتی که باشد، نابود کنیم.
🔹
زیرا ظرفیت ترابری سریع و عملیات‌های خاص و ویژه در سال‌های اخیر طی تمرینات مکرر حاصل شده و این رویکرد تهاجمی، پیام روشنی برای دشمنان دارد.
🔹
ترامپ جنایتکار و نتانیاهوی ملعون امروز پاسخ‌گوی افکار عمومی و نخبگان خود نیستند. آنها مدعی نابودی نیروهای مسلح ما بودند، اما امروز نیروهای مسلح مقتدرتر از همیشه در مقابلشان ایستاده‌اند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/farsna/461213" target="_blank">📅 09:15 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461212">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f53df36bf5.mp4?token=RHnHD_81VdXt9sP1OuTimq280zrKy4-EeJewvkPxa45XpemmI30Y5-I5GbW5SifRZgspoPXkul-JySSM7gW8T_gSnHqRzP0leSdnxE1z2vXDUJri3BTOm5Jb1BmIg70klTn8JRbBVGTaoI71FjJFZzTeYrm4JJv6kBVQmlbn_hJOPeuiblRyo9QPt237G4NbAfwGxky6DqSniBw3hw8gRlMWnRLQIoD2X6AtnJmBstB6n9BTcRC8J_87dd2ZA4G8JXS5AxaW06RZuqkS_KZgoIef7P9fEW9uU-O8yUi23cxw8X8DWwI6mpvaumD-bY9o-C66Bs7DmCAKYy7VZObkqg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f53df36bf5.mp4?token=RHnHD_81VdXt9sP1OuTimq280zrKy4-EeJewvkPxa45XpemmI30Y5-I5GbW5SifRZgspoPXkul-JySSM7gW8T_gSnHqRzP0leSdnxE1z2vXDUJri3BTOm5Jb1BmIg70klTn8JRbBVGTaoI71FjJFZzTeYrm4JJv6kBVQmlbn_hJOPeuiblRyo9QPt237G4NbAfwGxky6DqSniBw3hw8gRlMWnRLQIoD2X6AtnJmBstB6n9BTcRC8J_87dd2ZA4G8JXS5AxaW06RZuqkS_KZgoIef7P9fEW9uU-O8yUi23cxw8X8DWwI6mpvaumD-bY9o-C66Bs7DmCAKYy7VZObkqg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
هواشناسی: امروز و فردا در استان‌های شمالی بارش‌ها ادامه دارد
.
@Farsna</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/farsna/461212" target="_blank">📅 08:33 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461210">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">منابع عربی از وقوع چندین انفجار شدید در عربستان سعودی خبر دادند.  @Farsna</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/farsna/461210" target="_blank">📅 07:47 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461209">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rsM6jfy1rNSumucZ0GeAT3pj7Anu_Zrn2OcMQGKKyg1ijoFjZiao_5zzNPf9XVZXrFABYE0r1A3VcZNVhxPDaea7nBcRsFOtocBdViISyezpLp8M9T0UsjwK6foTOvGQjlUKo91VdFDbQO9ob9zthxU-gtMBxriVcgU6TbV9zshvszj5wNbEDFeNGGor3irFj8mxHGyUUa931rmAdISttBhziXIt7tl8Sc740HCpjq4ENdjhzInlS2D3vkRdHBrq3inf0SrK2daXIspqOKUkG9KpT-mUtPFFl_-xUDwcxXiHy5zM3m4JTUzz1dTWr61S3JSdtPFvWZU4hHZlx1AFjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دیپلمات روس: آژانس اتمی باید به ایران تضمین بدهد
🔹
میخائیل اولیانوف، نمایندۀ روسیه در سازمان‌های بین‌المللی مستقر در وین، طی سخنرانی در جلسۀ شورای حکام آژانس اتمی گفت که اگر این سازمان می‌خواهد بازرسی‌ها در ایران از سر گرفته بشود، باید تضمین‌های واقعی به تهران بدهد.
🔹
او ادامه داد روسیه اصرار دارد که برای از سرگیری فعالیت‌های راستی‌آزمایی کامل در ایران، به تضمین‌های واقعاً قابل اعتمادی از سوی آمریکا و اسرائیل نیاز است که آنها استفاده از نیروی نظامی یا تهدید به آن را از سر نگیرند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/farsna/461209" target="_blank">📅 07:43 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461208">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">منابع عربی از وقوع چندین انفجار شدید در عربستان سعودی خبر دادند.
@Farsna</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/farsna/461208" target="_blank">📅 07:32 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461207">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/99dc1cae7d.mp4?token=bXRdQD8iW0IK4BbfQ7W5kqB-B-0dbpWFWp4n1DsUBNhoFOZ_YhnOAcbqCQzhouz2c4iqwNLdTdFIcdANqCQwR_eP7t8YpVWILX--F4pDOoO6rQOjCh10MJ-V0uvMLBSC1SwP5hasgbDUi8Y4g2je5wQBpM9Un-t07o2UB5NW-SBrc3657B1xIkp7kT9vdh0Hne2_Lu_iepAUDrIHbHZ-jsIGstIKcb16zXZQr7pmiXrPLpCwbQU-ntPQ1rdnHRjcfXKrPGpfAQQ2W_ssPGK0tdtry_bC7ZE6bLurBsZuOVPIIrJt-I_d3EckkPNK8iJmHxPI587Y8M7yqi-LJEbV3A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/99dc1cae7d.mp4?token=bXRdQD8iW0IK4BbfQ7W5kqB-B-0dbpWFWp4n1DsUBNhoFOZ_YhnOAcbqCQzhouz2c4iqwNLdTdFIcdANqCQwR_eP7t8YpVWILX--F4pDOoO6rQOjCh10MJ-V0uvMLBSC1SwP5hasgbDUi8Y4g2je5wQBpM9Un-t07o2UB5NW-SBrc3657B1xIkp7kT9vdh0Hne2_Lu_iepAUDrIHbHZ-jsIGstIKcb16zXZQr7pmiXrPLpCwbQU-ntPQ1rdnHRjcfXKrPGpfAQQ2W_ssPGK0tdtry_bC7ZE6bLurBsZuOVPIIrJt-I_d3EckkPNK8iJmHxPI587Y8M7yqi-LJEbV3A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">منابع عربی گزارش دادند همزمان با فرار گسترده و تسلیم مزدوران سعودی از شهر الیختل، نیروهای مقاومت یمن وارد این منطقه شده و در فاصله ۱۵ کیلومتری بندر «المخاء» قرار گرفتند.</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/farsna/461207" target="_blank">📅 07:22 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461206">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">🔴
سپاه: آشیانۀ تعمیر و نگهداری، آماده‌سازی و محل استقرار جنگنده‌های F-35 ،F-16 ،F-15 و شلتر جنگنده‌ها مورد هدف قرارگرفت
🔹
روابط‌عمومی سپاه: ارتش تروریستی و متجاوز  شکست خوردۀ آمریکا از روی استیصال چند کشتی تجاری-نفتی ایران اسلامی را مورد حمله قرار داد.
🔹
به…</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/farsna/461206" target="_blank">📅 07:03 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461204">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ipnaR18EzhiyLdJpsRdWxgG74qQKhK_HvP5bWYfkRG5a_dhOdEPggVnTifheUgMUSqcWSx4iVr85Mi_a_ayC8WHkQlqlGhG7FEynUi6IeEDxvMj_vyf8gHmegthLsI-Dd-qJ1lJGYtrVclL_FLYN8ouEY4iW7vxLnS4RbqRqFC2fwPjD1vX2EETcl-hrfjmsrnLn6NeSpG4BX_2BnqRQOcq3JKa4gvk06OXaBs1zhcTPQxnoIYTrYG858_G8pEgLoruJ18z_sYNMz1YNM2_sJEaakT_pUL_qqfieVAQvlkvqjdFwjb3ar5D7hyAMe5JiFPP3JHSGjMv3KyENWJWJEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شکار یک زیرسطحی هوشمند آمریکایی در تنگۀ هرمز
🔹
نیروی دریایی سپاه : یکی از مدرن ترین زیردریایی‌های هوشمند و بدون سرنشین ارتش تروریست آمریکا را در ورودی تنگه هرمز به دام انداختیم.
🔸
این زیر سطحی هوشمند از جدیدترین تکنولوژی‌ها در حوزۀ زیرسطحی در دنیا برخوردار…</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/farsna/461204" target="_blank">📅 06:38 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461203">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1a665296d9.mp4?token=jJJyyq3p9n6vW32U5hrfCHnlzG90zP7gcjXv3OplIBZZI1EOl0ccp4wtCNrj7IQQYifPsdvAE33mw7sChKS3ustVgjI3lUtJmom5PPhCMscj92koJxdCCdWpnNLJKRyiBktFbkCJBnLvNcBc23c_InCSsDRJr3szOCZzLgoKRHnTjAvt30T4m7NuKmYt87ZE-FP5pJaqheyD473sN7VEQh8CbRQcJZ-yZT7HlTjo7RsKgXDpzU4HyXwJWlS4bDWs_BITgPJ176WZNnNDx4KxvHhyxBJwSr0M9rbD3EtSjdEdhO0fUs4fQyNzAaqIaUMvF9qJjrIueLcOBB5bET_n5w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1a665296d9.mp4?token=jJJyyq3p9n6vW32U5hrfCHnlzG90zP7gcjXv3OplIBZZI1EOl0ccp4wtCNrj7IQQYifPsdvAE33mw7sChKS3ustVgjI3lUtJmom5PPhCMscj92koJxdCCdWpnNLJKRyiBktFbkCJBnLvNcBc23c_InCSsDRJr3szOCZzLgoKRHnTjAvt30T4m7NuKmYt87ZE-FP5pJaqheyD473sN7VEQh8CbRQcJZ-yZT7HlTjo7RsKgXDpzU4HyXwJWlS4bDWs_BITgPJ176WZNnNDx4KxvHhyxBJwSr0M9rbD3EtSjdEdhO0fUs4fQyNzAaqIaUMvF9qJjrIueLcOBB5bET_n5w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یاوه‌گویی دوبارۀ ترامپ درباره تنگۀ هرمز
🔹
رئیس‌جمهور تروریست و متوهم آمریکا با تکرار ادعای پیروزی در جنگ با ایران، مدعی شد که باید نام خودش را روی تنگۀ هرمز بگذارند!
🔹
او گفت به‌نظر من باید آن را تنگۀ ترامپ بنامیم. ایران در حال فروپاشی است. @Farsna - Link</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/farsna/461203" target="_blank">📅 06:15 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461202">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bN-rjpuFlfYOrcCAAgsZxsMirsIuii0H2eBc6venI5Bh663hJ3qysI7Iv1949hxz1MLxzccXgdTW6zPYVgdAXhSjB4FxiQgqBw48CsrGWi263MBpL23vGjDXX-RGKL6j_LMLKNeTiH1JCh83TgU6_DpEPO-nJ24-daRCzj5Vc8W-JAPUwkoNP1BI4LPl69zSW0htsQoojOtrqFX3jEUcoQTzuMFCnRGh9t-XSvf4DCosVVdyaUH99G17XG7y_33pxKQHXEBUNCVolLLqiMw37DpuVJGy-Zk4VuZcN3QfakYybMwhAi4xPIylFog5qx3Cc3q1YN8g4AeVJJNz2WvvMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روسیه تهدید به استفاده از سلاح اتمی کرد
🔹
نایب‌رئیس شورای امنیت ملی روسیه گفت ممکن است سلاح‌های هسته‌ای در شرایط خاص، یعنی تهدید جدی علیه امنیت ملی روسیه، مورد استفاده قرار گیرند.
🔹
او گفت مسکو می‌خواهد جنگ اوکراین هر چه سریع‌تر پایان یابد، اما فقط طبق شرایط خودش.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/farsna/461202" target="_blank">📅 06:02 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461201">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VDebxjjbgZKpTNRPU6RpBRJruALcPURZM62UWJ0HolXnNDnGXDdVwPw-LxDkvtYi4BQD73x-BAa1xMGH1b2SdcYW3cfndqxbwJpF7_9TGCplgLC5tQnMjvTj7BoWRhVJ04GYD1ve_Y_mQc8NMP1DNqqB7Ycq7uu1rK8sOAlz8Axbc2Y4DNBVIuwRY2zKX-F5Xef6bFynzY23_b4LnFdRjbBdDaSBDnRzw-qkr2Dewgyc75k93zKqcMicVHbFZUsPnaO-g1Gq6DYtkE2CIp_RJCUX50ZaWOk0_PPYR5UzkNcr76C-1JFStcJ7Q8KLt8SHzUqOqma14lPBK_WfA0LJgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یاوه‌گویی دوبارۀ ترامپ درباره تنگۀ هرمز
🔹
رئیس‌جمهور تروریست و متوهم آمریکا با تکرار ادعای پیروزی در جنگ با ایران، مدعی شد که باید نام خودش را روی تنگۀ هرمز بگذارند!
🔹
او گفت به‌نظر من باید آن را تنگۀ ترامپ بنامیم. ایران در حال فروپاشی است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/farsna/461201" target="_blank">📅 05:26 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461199">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">شنیده‌شدن انفجارهای مهیب در جنوب عربستان سعودی
🔹
همزمان با فعال‌شدن آژیرهای هشدار حمله هوایی در شهرهای «خمیس مشیط» و «أبها»، صدای انفجارهای متعددی نیز در این مناطق به گوش رسید
🔸
ارتش و نیروهای مسلح یمن پایگاه‌های هوایی در «خمیس مشیط» و «أبها» را که جنگنده‌های سعودی از آنها به خاک این کشور حمله کردند، هدف حملات موشکی و پهپادی قرار دادند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/farsna/461199" target="_blank">📅 04:48 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461198">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/33ded3bb5c.mp4?token=Bt-shynPI9H2cB4xY1v2qX5LC_Lvnugd4K6o6L7JpYEA6Er83CaT-Uu0NU0oQMx2zBiTYEQlyIMXVcEeFQ7dkG7zGeExCrx_RAds0ddyjQeHYr8BsFGGFwCbvsVzZDeOv2s33zxGeEacdk64hqknYgce1ckfsw3wZJZ3CPfRMsdsxCCK00LQ0jeYhC_t2O-SX-1K-eU5VcLrKSsbJJG8XdYVio5lmlUVTKi3rKOwyI9a3PgRXEaKbjQdlWtLysIWlmVEXdxxulugNM8bASMo1_M-3NbZcQjh9XOtwy41mrzRAfxr3dQSz9ztJIbfQ6QdNcDqjLg0f_kdPV1GKVYd9A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/33ded3bb5c.mp4?token=Bt-shynPI9H2cB4xY1v2qX5LC_Lvnugd4K6o6L7JpYEA6Er83CaT-Uu0NU0oQMx2zBiTYEQlyIMXVcEeFQ7dkG7zGeExCrx_RAds0ddyjQeHYr8BsFGGFwCbvsVzZDeOv2s33zxGeEacdk64hqknYgce1ckfsw3wZJZ3CPfRMsdsxCCK00LQ0jeYhC_t2O-SX-1K-eU5VcLrKSsbJJG8XdYVio5lmlUVTKi3rKOwyI9a3PgRXEaKbjQdlWtLysIWlmVEXdxxulugNM8bASMo1_M-3NbZcQjh9XOtwy41mrzRAfxr3dQSz9ztJIbfQ6QdNcDqjLg0f_kdPV1GKVYd9A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گزارش‌ها از تسلط نیروهای یمنی بر شهر «الخوخه»
🔹
گزارش‌های اولیه حاکی از ورود نیروهای مقاومت یمن به شهر ساحلی «الخوخه» در استان «الحدیده» است.
🔹
از سوی دیگر خبر می‌رسد که نیروهای یمنی بعد از به دست گرفتن کنترل پایگاه «خالد»، به کوهستان «النار» رسیده و با مزدوران…</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/farsna/461198" target="_blank">📅 03:31 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461197">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">گزارش‌ها از تسلط نیروهای یمنی بر شهر «الخوخه»
🔹
گزارش‌های اولیه حاکی از ورود نیروهای مقاومت یمن به شهر ساحلی «الخوخه» در استان «الحدیده» است.
🔹
از سوی دیگر خبر می‌رسد که نیروهای یمنی بعد از به دست گرفتن کنترل پایگاه «خالد»، به کوهستان «النار» رسیده و با مزدوران سعودی درگیر شده‌اند.
🔹
همچنین منابع عربی گزارش دادند همزمان با فرار گسترده و تسلیم مزدوران سعودی از شهر الیختل، نیروهای مقاومت یمن وارد این منطقه شده و در فاصله ۱۵ کیلومتری بندر «المخاء» قرار گرفتند.
🔹
همزمان ارتش یمن نیز مواضع مزدوران سعودی در المخاء را با حملات موشکی و پهپادی هدف قرار می‌دهد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/farsna/461197" target="_blank">📅 03:11 · 19 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
