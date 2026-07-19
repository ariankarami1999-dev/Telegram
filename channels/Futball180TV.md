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
<img src="https://cdn5.telesco.pe/file/S6hPPIUn8MKcCYJO4BYRBwmt2v8WL5tK-MeO3XvnJx6VXGmIvKs73K6whbguU45t3uC89LWRsADwWvhGCLvr-7UXzcgLgAY26Cv3fZl8rO4s8Y2RSHR-pviQ0uHwKQ24M16uI8EBod3zuKEw23BJvuCbYsvLEC8Oz95XDSFfFhTrLDRed85sCpNOeGHRDSuw8mgFPPwe-VHSaEdQwspRcHstzsXps6fnDbgFvoHJGpoJPLbDTsHmp3ypAalHeLnji-Eia74lpPvizKkh1LKuqSh1PTI1U9YmV85Gsv_IoUZghVoSvgHnPbBt8mRAhkZY4VC7I_5CKtrSfj9PKr1hjw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 جام جهانی 2026 | فوتبال 180</h1>
<p>@Futball180TV • 👥 557K عضو</p>
<a href="https://t.me/Futball180TV" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 In the name of God; The only popular sports channel on Telegram: All for Iran...🖤We respect the copyright laws and follow the laws, Mr.@Durov...🙏🌹Contact ads:@TivaAds</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-28 14:34:53</div>
<hr>

<div class="tg-post" id="msg-100961">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/opHE98aUIX7tgRPXQtBzyDa-5VuCNMQ4fT4m-rrgHrGlapPBrVYCPnNJf18S_EbhxO5N2ukFTmnEwZ5fbEYRptV2FYw0N0DKr23jLqhLxIHKIu8Bn9hHHPuM1MPEKpTCyI50cZWKYM8c4bM0cw7NaVnpgYncph6quyLa_qZ4jlvotO1KdkLFhqe8Y2VF9uZVadysiPag-yZi8coA0izQXsM060FF38V0_9YbHDQGcBAIkGFO7xWd2oulcni67jmtfQ4OoUSUXktpyMwR8ckzYFEl7sHaBHuj0U4cQ9tSqvMw0vxnL3zakZ1D39iD6PmE3r47242ndomZDrFJlhofrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پیشبینی پیکه از فینال جام جهانی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 2 · <a href="https://t.me/Futball180TV/100961" target="_blank">📅 14:35 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100960">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">🅰️
🅰️
🅰️
🅰️
🅰️
🅰️
🧾
امکان ویرایش شرط ثبت شده
💥
برداشت سریع با کد پریمیوم ووچر
💵
شرط بندی بدون محدودیت، بردهای نامحدود
🎁
جمعه و دوشنبه‌ها، شانس بردتان را دو برابر کنید
100% بانس میکس ورزشی تا سقف 30 میلیون ریال
🎁
با واریز کریپتو، سقف برداشت خود را به سطح جدیدی ببرید!
1️⃣
لینک بدون فیلتر
1️⃣
ورود به سایت با فیلترشکن
••••••••••••••••••••••••••••••••••
💠
لینک اخبار و هدایای سایت
👇
👇
🔸
https://t.me/+ioIBrQfqMLtmMmEy</div>
<div class="tg-footer">👁️ 315 · <a href="https://t.me/Futball180TV/100960" target="_blank">📅 14:35 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100959">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PBpO0jqoq8IkZsFojAdfQWZD8SzEZKkco0TN51crLIr0sm1Oif4J_40uYDHxkloo4jSqmSdl8TuDXb9mYyNb07gUtIsaNh1-MBL2ID6S4wsWEaNRyM4AtgUOxaeGQvKG4IlWSsw0-fdQPY37I8-0of_tfERybyB9qjz7iOHnjjcgqlUjt24kk_UvD5UDWnm335IDEojYdIyF1BeHa02CQozGgup1NXmPtgdyaO-rPO2eNJmHx2vgAq6UTr4aH5haSkiPaETUklEMo5juhtya9LJzSFj7qppEXGFwxA-B0fs3Ze7UB7UthJP7JofGCUB8m5rH5Qqnwmzx1K7j30hnMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
فینال جام‌ جهانی 2026
⚽️
اسپانیا
🇪🇸
-
🇦🇷
آرژانتین
⏰
شروع بازی ساعت 22:30
✔️
امکان ثبت پیشبینی با مبلغ نامحدود
🫰
محاسبه نرخ دلار با قیمت 2.200.000 ریال
⭐️
فرصت استثناییی چالش‌های پیشبینی فوتبالی سایت یک توتو، با جایزه 500 میلیون ریال
1️⃣
لینک بدون فیلتر
1️⃣
ورود به سایت با فیلترشکن
📲
@yekbet</div>
<div class="tg-footer">👁️ 310 · <a href="https://t.me/Futball180TV/100959" target="_blank">📅 14:35 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100958">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f2d8141062.mp4?token=sZtFyyChV0bl8ZELxXWlXlKS5jMr41H2VMJ0CxX5ATWC0zI04RwNKoDSUQ5fmdVNoTykjEC8lV_Qn3_CijApKowcvqVXrnpIt-dY4ckbOeTu9Zo3vFVUE0rjfFOFAmTpVbBa7aP-r-nrRDWM3KO9WJZ3fNJyyht16Qijg4csGFIK3oVN-Djrf_VpDf1QHURR_2MywzdGC46cStQr1aFgSVOEskWOrC3hH7-Rpa7diJStRF7B-NAxxHF5WaoNui-YCNRh5DIjKoxqNf2fh0jMO_qqMLWF-qdnZrsfBtcirm1PgJjPdf29mbrCVzLoaC5YOeP6AmfxaFu8XuAqQEbzHg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f2d8141062.mp4?token=sZtFyyChV0bl8ZELxXWlXlKS5jMr41H2VMJ0CxX5ATWC0zI04RwNKoDSUQ5fmdVNoTykjEC8lV_Qn3_CijApKowcvqVXrnpIt-dY4ckbOeTu9Zo3vFVUE0rjfFOFAmTpVbBa7aP-r-nrRDWM3KO9WJZ3fNJyyht16Qijg4csGFIK3oVN-Djrf_VpDf1QHURR_2MywzdGC46cStQr1aFgSVOEskWOrC3hH7-Rpa7diJStRF7B-NAxxHF5WaoNui-YCNRh5DIjKoxqNf2fh0jMO_qqMLWF-qdnZrsfBtcirm1PgJjPdf29mbrCVzLoaC5YOeP6AmfxaFu8XuAqQEbzHg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خلاصه که خیانت آخر و عاقبت نداره
😂
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.37K · <a href="https://t.me/Futball180TV/100958" target="_blank">📅 14:20 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100957">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JhmeF5_heFVzkW9exhFX_8eQdnV6rdEH_LU3m8eK-JNJ53COlbSwJubhdmXYXWkyfSENhTPsUE0d9-ITPWLY6GCsBWcjV65GqKWyx1IW__xVhXEZJLZIzvHgByaqMfUt0rL-Z7YghY94FSgre9bAXWKDatIEgjPlDInpLTy5vVs9ROpM03Og0NVwz2BePaCbpWZHYlp1zlmkrUHQcuk1Iacc9T2cezEMdc0IvzuVq_wfmdMW6RAgEsQT2j9vLfCMLvE2trP6lnel3wb8nCDdjx4W2hfXDl4ZkSJ7HxdWRLqGMdeL-gFa5wVIvYLkDbb3xWkL8SDzqjqQevKfUzByAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">استایل جدید یامال برای فینال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.82K · <a href="https://t.me/Futball180TV/100957" target="_blank">📅 14:04 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100956">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/71c23cc08b.mp4?token=FyHlGJe-bVkkfwLXWGbRWA0Mp0gsgCn8Jxn7TJC2L9m67RcQr0lce-0EvKVHKkZq-HBVp7xCFYxbXKIKmUW-ILCZkQ3JcWR8OC1eO9IHAj8txzEhJpw1wdIHgtIXiaVYDdrVnSHF9UK0XNe5pkkMHVSTF1XkNowt0gWsTx6Dqb5JSNCuuVY9nzGvgcAMOiTcKW54lAB9pSzswB7z0vtqpPgpY48hkcwjSVGsE_m2Irl8-SW5zLTOtHGV3NbgMtrGBoriNcRzcbohOFCqB0gOnOxGnJ3FschzcEOjZxjdctZ9Cbc1BhSIsRAVg_t7BRpNy-49f2PaHqgWQYJDsWpCvw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/71c23cc08b.mp4?token=FyHlGJe-bVkkfwLXWGbRWA0Mp0gsgCn8Jxn7TJC2L9m67RcQr0lce-0EvKVHKkZq-HBVp7xCFYxbXKIKmUW-ILCZkQ3JcWR8OC1eO9IHAj8txzEhJpw1wdIHgtIXiaVYDdrVnSHF9UK0XNe5pkkMHVSTF1XkNowt0gWsTx6Dqb5JSNCuuVY9nzGvgcAMOiTcKW54lAB9pSzswB7z0vtqpPgpY48hkcwjSVGsE_m2Irl8-SW5zLTOtHGV3NbgMtrGBoriNcRzcbohOFCqB0gOnOxGnJ3FschzcEOjZxjdctZ9Cbc1BhSIsRAVg_t7BRpNy-49f2PaHqgWQYJDsWpCvw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
😛
یادی کنیم از دلبری ها و لاسای سمییییی بیرانوند با دلبرجان
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 6.73K · <a href="https://t.me/Futball180TV/100956" target="_blank">📅 14:02 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100955">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sAS0vpRwbDzc1PX6NGx1yCurN9crH0Bxerat5p4DZjKSFk41jncjglzv3QTCdI1KS7D1KalsD9AZqngi2uCDlsDni-ovUGAz18ArVZmjwBZm6SpD1jICH07uAOlWgJ3iRGlhtcS7OCPedQJwMNJzaQpm0VSwMdMj9hQcON75OXM5T4WS-iX50Qd0ALi5BQflN3snBIz5Q_2wEcF1neLL2jVqrs2kp85Zq0d3YG6W6AxfrIDEhWHTewP5e8eLwkITpfYY-mXJnsFoIfylD5UNYnv1aYoaksWREG8eFC2n3RoFlDCPKJea6PHCh7p_qLJaMuoS_aiil3b7yhlUzuAqZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
😍
استوری وریا غفوری: مشکلات داخلی یک کشور، با دخالت بیگانگان هرگز حل نخواهد شد!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.77K · <a href="https://t.me/Futball180TV/100955" target="_blank">📅 13:49 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100954">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c09af135ae.mp4?token=DtbN0CsmSOQFFMTgsfG6G0hN0hDL0CL34lONmPA-ERS8NCXSkUYafm2WYBTVsgVt4g-zyhcf13slOM5auGgygj_9ccNhObIu9KZnPPkyq4VUTIqnMzPUQbBd6q1qyXyKBAP0bVeGHBbLh8z8QaMubr8_puMhWVREK2bHNyg1RGt3Hbe4M67Ln1UhGwJgwanl2G0mCqEVbpLSfuZuks77y-Dor0iMj2eVHIceefNEOjVo1V_PucwRqJpY5dUyZ8nI9OyQpMECyrtrSgLubRvqS1CSbskd2qxuhXbqp1uACu1XWlu3hFp2_152eOwZZRlaQkgGf0I5SHYMOamSSqA3_pJhR6g996zPdMC6E7smooUmFcMtLu6k9QG9FElVPKx7Xn2CwDmjgWgdvVjByek71bBIEKPy3wZWAlWZPuaU3nbuqwbZSvkA6c4czba_h6OLJxQu9XgbFS5qSG-mhdhL1zv5O7Jr7je4DJUr98N0ewv1yevfRczdgvy86T9wekr1gmroEqYRneplE_ZOOwvIYsQlwDF8dGMsN_UFQVhAaerL8ePzW-qRLAfwA_cNZSsEonZoiAJmPX3eidWCmDAPGicsxxHaS6uvThrmc6eXENuvC1MuxNh7xflle4pH-J9sspVvgHiaCgGaapD3UQCVMVQ9wQ6U051YWmNyZ6lSEhU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c09af135ae.mp4?token=DtbN0CsmSOQFFMTgsfG6G0hN0hDL0CL34lONmPA-ERS8NCXSkUYafm2WYBTVsgVt4g-zyhcf13slOM5auGgygj_9ccNhObIu9KZnPPkyq4VUTIqnMzPUQbBd6q1qyXyKBAP0bVeGHBbLh8z8QaMubr8_puMhWVREK2bHNyg1RGt3Hbe4M67Ln1UhGwJgwanl2G0mCqEVbpLSfuZuks77y-Dor0iMj2eVHIceefNEOjVo1V_PucwRqJpY5dUyZ8nI9OyQpMECyrtrSgLubRvqS1CSbskd2qxuhXbqp1uACu1XWlu3hFp2_152eOwZZRlaQkgGf0I5SHYMOamSSqA3_pJhR6g996zPdMC6E7smooUmFcMtLu6k9QG9FElVPKx7Xn2CwDmjgWgdvVjByek71bBIEKPy3wZWAlWZPuaU3nbuqwbZSvkA6c4czba_h6OLJxQu9XgbFS5qSG-mhdhL1zv5O7Jr7je4DJUr98N0ewv1yevfRczdgvy86T9wekr1gmroEqYRneplE_ZOOwvIYsQlwDF8dGMsN_UFQVhAaerL8ePzW-qRLAfwA_cNZSsEonZoiAJmPX3eidWCmDAPGicsxxHaS6uvThrmc6eXENuvC1MuxNh7xflle4pH-J9sspVvgHiaCgGaapD3UQCVMVQ9wQ6U051YWmNyZ6lSEhU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🎙
🤣
بیژن‌مرتضوی در آستانه فینال امشب: مردم می‌گویند لوند رو بزن، شکیرا برقصه!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/Futball180TV/100954" target="_blank">📅 13:37 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100953">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">🇦🇷
🇪🇸
تیزر فوق‌العاده از تقابل امشب فینال جهان
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/Futball180TV/100953" target="_blank">📅 13:26 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100952">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/194b426cce.mp4?token=bYPbfgek2cziUyMNHWuM_sA5RmAwhDgMWgOsSTqbVIt-z3w_frQD5_NyoBwVgt0K-GjrLvQXOqV2UHVzdY-pAfQELrMRlUKtkTBM8atPRTZnddY8yjjjVps9-2XY-f4DlaspgIXeixvWK7il2wiXRp7vLp3fKiN2SfMJYb2NSGVVhs6bL3tzeP_2zZEnlu23CM0HhXjvWQSEYcyTFUi2FJAW8HjWUMjcDbXy_7mJm04SWaHDYsPye6MS9jRYZH7ZnmWnX6PY6kBS__h6JVqscAHcB-nxQRRWMrIr5y44twCLmpn8V9obc6E2avo6Qt5j_J3e0MgELme40tn4tK5VEQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/194b426cce.mp4?token=bYPbfgek2cziUyMNHWuM_sA5RmAwhDgMWgOsSTqbVIt-z3w_frQD5_NyoBwVgt0K-GjrLvQXOqV2UHVzdY-pAfQELrMRlUKtkTBM8atPRTZnddY8yjjjVps9-2XY-f4DlaspgIXeixvWK7il2wiXRp7vLp3fKiN2SfMJYb2NSGVVhs6bL3tzeP_2zZEnlu23CM0HhXjvWQSEYcyTFUi2FJAW8HjWUMjcDbXy_7mJm04SWaHDYsPye6MS9jRYZH7ZnmWnX6PY6kBS__h6JVqscAHcB-nxQRRWMrIr5y44twCLmpn8V9obc6E2avo6Qt5j_J3e0MgELme40tn4tK5VEQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
فوتبال در دوره‌ای که سیستم var نبود :)
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/Futball180TV/100952" target="_blank">📅 13:20 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100951">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fdf595645d.mp4?token=L7IRkGFaD4il_F9pEwpsf2b1HgaQVfwifEYw0LURwrqQtUXzF7InQOKPseL_YLVk-1dx-cu9lzgeWAxVYr-aJ5ElYtf6Bn_CWb2lXB_FIDIt24EuS-oIye-Ohysoseb0JaI3Wd8LexLwpyWBs-XNTHpJAc4qw2640NNoXy4GO8mhyNwH-PKIo9pdI4jx3nOAa1Q359m1hFhcvc3Y11WnbhGmFHWz5a1rs7KVmjIt6dtJhQjmJIgh6RdTubBnBJw0pAdB2Vcb0cWIbrImOpZQ5BkhyOFeOWkZKITcuYjn4qITkq34LOOAz6Xl44JpM3EfLlVZI7ydqu_duwCTvojrXA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fdf595645d.mp4?token=L7IRkGFaD4il_F9pEwpsf2b1HgaQVfwifEYw0LURwrqQtUXzF7InQOKPseL_YLVk-1dx-cu9lzgeWAxVYr-aJ5ElYtf6Bn_CWb2lXB_FIDIt24EuS-oIye-Ohysoseb0JaI3Wd8LexLwpyWBs-XNTHpJAc4qw2640NNoXy4GO8mhyNwH-PKIo9pdI4jx3nOAa1Q359m1hFhcvc3Y11WnbhGmFHWz5a1rs7KVmjIt6dtJhQjmJIgh6RdTubBnBJw0pAdB2Vcb0cWIbrImOpZQ5BkhyOFeOWkZKITcuYjn4qITkq34LOOAz6Xl44JpM3EfLlVZI7ydqu_duwCTvojrXA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
▶️
امباپه هم اکنون: بهترین گلزن تاریخ جام جهانی و بهترین گلزن جام 2026.
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/Futball180TV/100951" target="_blank">📅 13:00 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100950">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">✔️
💥
استادیوم مت‌لایف در آستانه فینال امشب
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/Futball180TV/100950" target="_blank">📅 12:40 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100949">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/772126c267.mp4?token=kSDk1VclZlpnWIXWbf6TedND6D5w-k_WYF1tfgZISt-rO8Pye4qmlAKYkWOedImx9UlP1CozJ6J7MQ8CPS7PjBb0GnK0b4BnKBTskuOlr4Ieynm-NWou9o8wO0CxI4aI2FpsaaCCTS_42q_ZyUHnG7wUkgsfWQ7VlYguE4dVEWMyWq_gI9B_ae48aIQf3hVmqn4zrrbllVPQJdPP_Qs5NU6zIxZRfzjaumpLOIEawaxNiFyX4XV1tsOEk-XJ4X7DZ3nhclydtxvDAws50mVgWN6DEj0MNvW4nkmPLk1s9KrO2lX396uj1hxFg6nzSfze-rAIoyYeK45Kg6bxf0QIr1vER7ontAOBCfg0K-FYnjbgPmWAyxwW3dwrF8ozQ9biu2o-UC0ZeV9Pcm4HymsNCE1Gf86gRpW2ccDRSfNjBsO2KrCKpyDIydeCffrHN4VbngrXGHi23lHsQYDrA8zJb4IOeaca3Y5K3_hs1Vq0Mdv4ZPaPp8BxRqFbCZH7sB5DzCoDq_gSaO04iDAPAIGQnHKg4RLfSqNQmYKFCKjhcALeOGemEawBeoC4raphCERIr8dHAFjLdiH-9C8uvlczkejktQu83NMGdzxYjLp7cCtH7bguQqqKR6ChHnzX7tEzJfEySgK2yQcYHtcQVv7T1rUTrT0-73_fnKBJu1haJD8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/772126c267.mp4?token=kSDk1VclZlpnWIXWbf6TedND6D5w-k_WYF1tfgZISt-rO8Pye4qmlAKYkWOedImx9UlP1CozJ6J7MQ8CPS7PjBb0GnK0b4BnKBTskuOlr4Ieynm-NWou9o8wO0CxI4aI2FpsaaCCTS_42q_ZyUHnG7wUkgsfWQ7VlYguE4dVEWMyWq_gI9B_ae48aIQf3hVmqn4zrrbllVPQJdPP_Qs5NU6zIxZRfzjaumpLOIEawaxNiFyX4XV1tsOEk-XJ4X7DZ3nhclydtxvDAws50mVgWN6DEj0MNvW4nkmPLk1s9KrO2lX396uj1hxFg6nzSfze-rAIoyYeK45Kg6bxf0QIr1vER7ontAOBCfg0K-FYnjbgPmWAyxwW3dwrF8ozQ9biu2o-UC0ZeV9Pcm4HymsNCE1Gf86gRpW2ccDRSfNjBsO2KrCKpyDIydeCffrHN4VbngrXGHi23lHsQYDrA8zJb4IOeaca3Y5K3_hs1Vq0Mdv4ZPaPp8BxRqFbCZH7sB5DzCoDq_gSaO04iDAPAIGQnHKg4RLfSqNQmYKFCKjhcALeOGemEawBeoC4raphCERIr8dHAFjLdiH-9C8uvlczkejktQu83NMGdzxYjLp7cCtH7bguQqqKR6ChHnzX7tEzJfEySgK2yQcYHtcQVv7T1rUTrT0-73_fnKBJu1haJD8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇦🇷
🔥
میدان تایمز نیویورک در تسخیر آرژانتینی‌ها
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/Futball180TV/100949" target="_blank">📅 12:20 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100948">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0afa3e469f.mp4?token=Z1oV7P2XTE47Hw-l6ujGKJmBktEh2sX4Vc0R_0RsqYjqeqen8NBDkA9EjhmbwN6Xy4DaE-0s1T4job8oOWmeUQ3yAzWMjxFGtu7pUbQ--LSoWj-W6MnAh_4L8ZcHVmDczlk1h35SftFPa1WBUnnpHHjog0f38m2hpebXTTNP4vgA44QCdmXy9Db2yN_vNpbpiDWjDl_FNSYqtvN9hS51mCvZksWzTdMnAXBBhgfnUMNDLXie0ivwaQ4HC8b4HqbAuQG4wzNsWMOYNrFjsV6ig8p7IXW_9gyYgvZ2yN3Ym_ncFgun9Y-S-iFxpkekhWoI5ZL9B4Ds1L9hTx61A-FCe2DYxGB1ACmcm8nicTckigRSgYUrEYCme-27w17YKXY0NT0d8mTQ7OCw0O6b7KjcK9N6ZecSNPUdgMJLJMvz-s7tIUKP5rBZqyhRViq7oFxv49HVHCeSHPmODX2qma0N1FFWKg2RSljJrvgHAGZa6bqf57RMhE708a2B1syqyLN_mn-3pYbs3qdXrHdG-CA-OVRxR31WosFoLxbisgpNBTF6wiOZVAuWdHGf4Pg7st3ZdVYBYTeYluql7663LHRauBeG8sA7yf4rSHOeSWPYxnUSzOs5zyS3YAm-jtfYx418fw68j5t3rcvbRd_NFwQupNBlefU6VwHu37FuhvbxcaQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0afa3e469f.mp4?token=Z1oV7P2XTE47Hw-l6ujGKJmBktEh2sX4Vc0R_0RsqYjqeqen8NBDkA9EjhmbwN6Xy4DaE-0s1T4job8oOWmeUQ3yAzWMjxFGtu7pUbQ--LSoWj-W6MnAh_4L8ZcHVmDczlk1h35SftFPa1WBUnnpHHjog0f38m2hpebXTTNP4vgA44QCdmXy9Db2yN_vNpbpiDWjDl_FNSYqtvN9hS51mCvZksWzTdMnAXBBhgfnUMNDLXie0ivwaQ4HC8b4HqbAuQG4wzNsWMOYNrFjsV6ig8p7IXW_9gyYgvZ2yN3Ym_ncFgun9Y-S-iFxpkekhWoI5ZL9B4Ds1L9hTx61A-FCe2DYxGB1ACmcm8nicTckigRSgYUrEYCme-27w17YKXY0NT0d8mTQ7OCw0O6b7KjcK9N6ZecSNPUdgMJLJMvz-s7tIUKP5rBZqyhRViq7oFxv49HVHCeSHPmODX2qma0N1FFWKg2RSljJrvgHAGZa6bqf57RMhE708a2B1syqyLN_mn-3pYbs3qdXrHdG-CA-OVRxR31WosFoLxbisgpNBTF6wiOZVAuWdHGf4Pg7st3ZdVYBYTeYluql7663LHRauBeG8sA7yf4rSHOeSWPYxnUSzOs5zyS3YAm-jtfYx418fw68j5t3rcvbRd_NFwQupNBlefU6VwHu37FuhvbxcaQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👍
حمایت کودکان آفریقایی از اسطوره علی‌دایی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/Futball180TV/100948" target="_blank">📅 12:04 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100947">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tek0pe2vMLSF8VN7idkQq0c6BlZnqFF98jveogx1gZWfiWAps9DMxDkU1n4a2uG-wSPeogH3O_u4xBFTechAgrbyd-JAhr52e5Nk3ogypoGkOcZagRBTY0pKAbRbtKtVuUd0Ku6825eMJ97v7vOx3CSuO51Tp4cQ7Qung4Zam_xZ_SMvXa-zAo1GuyUUMowW9w12Ks-x_R1g_t3rawWA_2wygyU4w2Ww2j9MM6h5i0UypLB5CydVSr-PwGkyZK-kLWyaIs-dzpZ-kBDVwWLShucujGwBqDwzPHqNSPO5NlFYrRbSznx7wlDjdkNdZ6PgcBdKQXshkjfZd4DEE1O-AA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😛
تصور اهالی فوتبالی پرتغالی از جام‌جهانی:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/Futball180TV/100947" target="_blank">📅 11:40 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100946">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KAdBqWbtbyxI7Y7rwxI464kJjGw1iIR2NSgUPcR8U9ucLWVqSBRNrREQpNJJiRwQIUdGXoz04JRepxgtgUUFsu00yGFZe-WVRTipRUYa_LYXA0iLTfxMSyj2A0NFUJpQ8jEZVilfUGLxN_6uOUTErblBw0VsK0arzrYVbppw0kK_zP5-bYsOho8qEmhP6AII3RorX0bQDK0hAUS5d3tpKffK45aYxSYqVmBZAmAIRRb6Q1KXvvZenD_BRQ4XI9KSd2ceR7ZqLyDMBtT-mqdoSzO-uUkA5MV_BDb-mV25AaEuDEvk77PDYriiq986rOPhNFhpdNs_yqNJbLhyhLXmEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
📊
کیلیان امباپه در جام جهانی 2018:
⚽️
7 بازی
⚽
4 گل
⚽️
4 پاس گل
🥇
قهرمانی
⚽️
در پست وینگر راست
🚨
📊
کیلیان امباپه در جام جهانی 2022:
⚽️
7 بازی
⚽
8 گل
🔴
2 پاس گل
⚽️
10 مشارکت
🥈
نائب قهرمان
⚽️
در پست وینگر چپ
🚨
📊
کیلیان امباپه در جام جهانی 2026:
⚽️
8 بازی
⚽
10 گل
🔴
4 پاس گل
⚽️
14 مشارکت
4️⃣
مقام چهارم
⚽️
در پست مهاجم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/Futball180TV/100946" target="_blank">📅 11:27 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100945">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e1a0fbf718.mp4?token=D7armeisdE_-TuFP9fm_CUrKR_ZsEEuEWivN7Jc8cjz8Cd_A1Em8gIcsNwZA0DEUTEET-905Y283mX40fnAJ9yGTHL00hjnFlxZw5w42C1HbKNPB0q0Cr_aGoXLTOvRp2VJdg5VLcaBbRPs12RZqGjE9UFQY6isxfDuW2oDaYwQBqTpS3_uPyTJngeKgi4SxiyiIU_Z4dJdNbtu_qI2uHEOJccYnQlRI8CrbGte2SpDXloI3YRVdtpPzg6RLXnHbVFVzWbWxANvlAqswQWLS0ST9mR9waHzoECVAMAmpu3szkqyBGWVHL9kxMv_qJU8oOOsRtDnu5WtmnJXzn94ItA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e1a0fbf718.mp4?token=D7armeisdE_-TuFP9fm_CUrKR_ZsEEuEWivN7Jc8cjz8Cd_A1Em8gIcsNwZA0DEUTEET-905Y283mX40fnAJ9yGTHL00hjnFlxZw5w42C1HbKNPB0q0Cr_aGoXLTOvRp2VJdg5VLcaBbRPs12RZqGjE9UFQY6isxfDuW2oDaYwQBqTpS3_uPyTJngeKgi4SxiyiIU_Z4dJdNbtu_qI2uHEOJccYnQlRI8CrbGte2SpDXloI3YRVdtpPzg6RLXnHbVFVzWbWxANvlAqswQWLS0ST9mR9waHzoECVAMAmpu3szkqyBGWVHL9kxMv_qJU8oOOsRtDnu5WtmnJXzn94ItA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇦🇷
🏆
🇪🇸
تنها چند ساعت تا آغاز فینال جام‌جهانی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/Futball180TV/100945" target="_blank">📅 11:20 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100944">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GfhCKIqLlDYbLR4bLvi-k1_NBOqIr9ddNtofZ6baf-1mN6gySE2ZAiypzFpd-lLW3HNMRzSePH27n6bwebufCi6fTUpf7x7O2xvsp14U8Q6kF4u6NgogT8ZJkzUuGzpG4w6PshSwEx-ystokVcE3508c0h62YUVgAgck3-rqkXfXNP9WUxAV737_IlGpaJI3DsyNKNkwalOb5wy2UhK9xlxLfKA93pt8SmwKduumC-sahuaV9F0jAJ23emrX-pxiajN4B_wBHZg30yNusTAS_OTDQPLwRZpcSh_AQVa4yq0ykoZkwB03oydzf50Tj31_Taio-1cOEZ1iyC0jEtHB5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇫🇷
بهترین گلزنان تاریخ برای تیم ملی فرانسه
کیلیان امباپه به تنهایی با 66 گل برای خروس ها میتازد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/Futball180TV/100944" target="_blank">📅 11:03 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100943">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">🇦🇷
🏆
🇪🇸
آماده‌سازی نقطه‌پنالتی استادیوم مت‌لایف برای بازی حساس فینال جام‌جهانی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/Futball180TV/100943" target="_blank">📅 11:02 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100942">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/40b0455cf0.mp4?token=ClbbcT2Hc64-EsBSTCJxU6PSKElAMDtFczb9X48URati_3Pl3OC8iU54T2ygAWouJ1utJebi1FmGz0FrGAPta0ZH1Bcp7_sH-5qSD4VQ9KTf3pIbvTvcC8qlFJZCkNHvsmmp859bziks6A_U-p-IqImHN4XceRBimVYtbDSe_pZOlX1AY2dhaI3XNrBY7Zs19Ri3nhRpRa-YEdLtSFmR4AFmDaRJnkf2X4M6L26hDgdMCOjrKKGCNt_iakj-GDS2405oO9JdXdtrrNmUYEEY4DdYkYintTk-P1due-y-Uz3Flf967bpvzl_UwIEOM4YdByLN9u-QpZYmzGE52XG1-g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/40b0455cf0.mp4?token=ClbbcT2Hc64-EsBSTCJxU6PSKElAMDtFczb9X48URati_3Pl3OC8iU54T2ygAWouJ1utJebi1FmGz0FrGAPta0ZH1Bcp7_sH-5qSD4VQ9KTf3pIbvTvcC8qlFJZCkNHvsmmp859bziks6A_U-p-IqImHN4XceRBimVYtbDSe_pZOlX1AY2dhaI3XNrBY7Zs19Ri3nhRpRa-YEdLtSFmR4AFmDaRJnkf2X4M6L26hDgdMCOjrKKGCNt_iakj-GDS2405oO9JdXdtrrNmUYEEY4DdYkYintTk-P1due-y-Uz3Flf967bpvzl_UwIEOM4YdByLN9u-QpZYmzGE52XG1-g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
👀
اولین شوک فرهنگی جهانبخش بعد از خروجش از ایران: من تو ۱۸ سالگی لژیونر شدم و رفتم آمستردام آزادترین شهر جهان؛ وقتی رفتم دیدم اینا بدون شورت باهم میرن حموم
😆
🤣
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/Futball180TV/100942" target="_blank">📅 10:40 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100941">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NZjO3e537Mx9Sr-TP2qubrJBq6Yjrd17-yEUcZAVcncBD2X6CigHhQgUOD8PpLcC7VHiNoET-VKkeGwfMy9507n21JpWkVKsRyks7TKjojtiOYZ-yx7TI2Th4j8BWKKH1wAL3PPns3DlJC20pCk3kmURGEOmmDefZdFit755F_As3nqVcFF3HUhX3ndwNsCzMGblSSp-i1Yo0Ug5vuO9Ly45fgaPOwLgYeHJiqsJ8yiS5xwjYDIqRB-s83VONRjKRINZ4Va3LoiHsveg63gn4DCeLbM5VgLBKFV8ZKQ5XTVPS7_dA1JK5OT7WLO0U19Z_jqWyZY1D78q8iy3zzJdQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کمتر از دوازده ساعت تا فینال جام‌جهانی
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/Futball180TV/100941" target="_blank">📅 10:35 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100940">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K5LLuKFk_2elQqU23Ov2B-yw7YWqHh8xrLfDCisZStY3g8dtpFruniN3r0_t_NcuVduoAso_dposh9shHqolRt152z4tPbvkzT3DPn9AKjJSd0_IFuBlip42Ul2iAxe9XRRwzHEnZdjx6chsBOfkI7h0TGn0kFe7leO68kekvjSa1-YvCegyg7Eg7Knc-tpt5fts2mD5-YEYBg3Ij9TCVrlC4Bry86azOyS6K2fIrqlLrQcm1dL1hFHXnX-tC3pJVdpgeXtzL9qUwuOLu-Civ5XJBEs1_9zcTBWEZKadfjUQAxjOch1RjrzQi2yqoPJHBL1ibzXPA-5lcPPmBZ6g7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🤣
جوری که امشب اسپانیایی‌ها فوتبال میبینن:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/Futball180TV/100940" target="_blank">📅 10:26 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100939">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jcfYkbkB5KdjMe_GY_joHgsnrDBgv8eGzNeow2Ic6FSupVznJXcBHNBAp4ymprCBRKF9YUS4BdJ0AUDGYgKmhTlqnl0dh7ZiL0GrmhVtwfFVgYtktBl8M69Py7S3Y3MCzJusnSQHqPxBKvfHDXiOgyeOUnZ0cpJNEAUTv36WWyqed1ANAYphYa71svUkxVsiyUqXaoZRGmh4R9lhOnBwJMxl50c1uL1nU5U7BIVoBRMB0AtTF69hDU6yRGahgxzml-B7aAwg8o09q6gxfM7MtPKQmXDfv3BdeG0WpYkBXCvkAYUZSdv8fEr0B2LsdKiEBYP3Hzd12BTswrq51pbRwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
رونالدو نازاریو:
فکر می‌کنم اسپانیا به‌راحتی آرژانتین را در فینال جام جهانی شکست می‌دهد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/Futball180TV/100939" target="_blank">📅 10:22 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100937">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1b1e84c807.mp4?token=Q-6v8ojhS8B6HnJHQPYlZWg6Ov6bQq-xJthCS0RGadPRg0eyuLKAmxDu3vaV2-dKdZkcIsqA67Za9iFmZwDH662IWoNQl4vmgUFLhZmL_TrJpv3jaBvqRdqE8hhC-Rn7nzyAxT_kaHHHFjuaZHiE3uvntGNuwMcdimJdFrZHletIXqIH9O_8v-9q4jQ2-Izb0wb7AlHbf8kW88HmptwAfcm1F4uzAgjr4Z_34VkYlUA2cBaFkkZo_kikMfPUGoKYFLsiebkEMBYg5h7pohZb3hkyBT11ufJvz0n8V8Y1lKmm_b6k1kiIWL4zwtAslv2lu2dSb055cj9UIns4n7oLCmqTXk5eYDI53ah1dWZSgE-NezUoL-9sYtGCEAWsd9ToBWVuGmRkglVz9y1hb4-HUYoSpf0UDLv7u9B8o3BI8Fduxc2ttzsGgJi372Bt0hzpTtDcXCK9EIktUtUBh55AEbuvwnwHr6lWHfDPOOi7RnizpZj4_R0lTiZLRko0vDZLDNbB92MXm1Io1MUrQZULgwxv1kGxMVfyMdacP1Gm6fUJT9vu7Fw944F0FJXt1qPoJtkuApYZCzORwYl0xvHFOjLvy6soV0Vpbqz_V0_hrHEvLmjx0GNLIOhsNjcGxEWjwKceap0EjF2vVfUyzehEHeJnnt7SWrbkb7sSknDyfbo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1b1e84c807.mp4?token=Q-6v8ojhS8B6HnJHQPYlZWg6Ov6bQq-xJthCS0RGadPRg0eyuLKAmxDu3vaV2-dKdZkcIsqA67Za9iFmZwDH662IWoNQl4vmgUFLhZmL_TrJpv3jaBvqRdqE8hhC-Rn7nzyAxT_kaHHHFjuaZHiE3uvntGNuwMcdimJdFrZHletIXqIH9O_8v-9q4jQ2-Izb0wb7AlHbf8kW88HmptwAfcm1F4uzAgjr4Z_34VkYlUA2cBaFkkZo_kikMfPUGoKYFLsiebkEMBYg5h7pohZb3hkyBT11ufJvz0n8V8Y1lKmm_b6k1kiIWL4zwtAslv2lu2dSb055cj9UIns4n7oLCmqTXk5eYDI53ah1dWZSgE-NezUoL-9sYtGCEAWsd9ToBWVuGmRkglVz9y1hb4-HUYoSpf0UDLv7u9B8o3BI8Fduxc2ttzsGgJi372Bt0hzpTtDcXCK9EIktUtUBh55AEbuvwnwHr6lWHfDPOOi7RnizpZj4_R0lTiZLRko0vDZLDNbB92MXm1Io1MUrQZULgwxv1kGxMVfyMdacP1Gm6fUJT9vu7Fw944F0FJXt1qPoJtkuApYZCzORwYl0xvHFOjLvy6soV0Vpbqz_V0_hrHEvLmjx0GNLIOhsNjcGxEWjwKceap0EjF2vVfUyzehEHeJnnt7SWrbkb7sSknDyfbo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
💥
🏆
شکیرا رفته بهترین کسانی که چالش موزیک جام‌جهانی از سراسر دنیا رو اجرا کردن جمع کرده و قراره امشب باهاشون برنامه اجرا کنه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/Futball180TV/100937" target="_blank">📅 10:13 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100936">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0c3ca27f4c.mp4?token=lZvetoxQEqzS-sryvc8i33mLTS-1jq8bYa_tm2r36zwbDBi0iYtE_S5VZnSgk1vTdL8V0TFN_s7Wco6gQ73_m1-86pA1n6bsClC63pDE7RhzVcdW0LYlWMwHLRsXpV0wQw-wLZck7iFr_R8PBMFtpOYWxosLvDK2FAh37FHCuibJCpw322jOM8-GV-Qbsy_RaAO29SMnkMRTFDfXauQk-hI7qb9qVi9tIk852bIoBEC7QKKXezZcNpxSRWMZ2Oan5Naf5_9bEHdIL5qqaTXO6epOuUwBNlHAf7lHYTqNdL-Liz6e6Z1_qpK_1Sz_z-lX_8WC8JLsJTEeFt4ZOxRN4Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0c3ca27f4c.mp4?token=lZvetoxQEqzS-sryvc8i33mLTS-1jq8bYa_tm2r36zwbDBi0iYtE_S5VZnSgk1vTdL8V0TFN_s7Wco6gQ73_m1-86pA1n6bsClC63pDE7RhzVcdW0LYlWMwHLRsXpV0wQw-wLZck7iFr_R8PBMFtpOYWxosLvDK2FAh37FHCuibJCpw322jOM8-GV-Qbsy_RaAO29SMnkMRTFDfXauQk-hI7qb9qVi9tIk852bIoBEC7QKKXezZcNpxSRWMZ2Oan5Naf5_9bEHdIL5qqaTXO6epOuUwBNlHAf7lHYTqNdL-Liz6e6Z1_qpK_1Sz_z-lX_8WC8JLsJTEeFt4ZOxRN4Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
👤
علیرضا جهانبخش دیشب غیرمستقیم اعلام کرد که طرفدار استقلاله و اگر روزی به ایران بیاد برای آبی‌پوشان به میدان میره
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/Futball180TV/100936" target="_blank">📅 09:56 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100935">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/de2d1332f8.mp4?token=idHYZzszAoUfCTUWFvo9nEKetvMpy6DkvifMoCbXF7aTfMIBoi24VyoYVDU0jeHcu9ZhzRZWre14Ni0RB9QvAXdYK5lgHBd3OcS8GP0ZVjVdt8nwjHHuYqgfaiKZj8uBsfKT_DVBTES_ka5I9Dd_cMk5Ed4WuQGHn8xYl5zA2owFGPapoGoGbZXqbzqkkZHJM5VTG78Jg6P5mAAHQHLnP9vz0IWBIFBxUeGjMO2BMcFqWR_jMgWQ1DpPQ4DxxdOcy6hOlxkyRrbcSRWXerNXgVr8bNG0xGHJrTmYCiItUkxZKhQJj4LruTEimU3PtifNM_fUaNEFbbbWrFqJqD4Z9w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/de2d1332f8.mp4?token=idHYZzszAoUfCTUWFvo9nEKetvMpy6DkvifMoCbXF7aTfMIBoi24VyoYVDU0jeHcu9ZhzRZWre14Ni0RB9QvAXdYK5lgHBd3OcS8GP0ZVjVdt8nwjHHuYqgfaiKZj8uBsfKT_DVBTES_ka5I9Dd_cMk5Ed4WuQGHn8xYl5zA2owFGPapoGoGbZXqbzqkkZHJM5VTG78Jg6P5mAAHQHLnP9vz0IWBIFBxUeGjMO2BMcFqWR_jMgWQ1DpPQ4DxxdOcy6hOlxkyRrbcSRWXerNXgVr8bNG0xGHJrTmYCiItUkxZKhQJj4LruTEimU3PtifNM_fUaNEFbbbWrFqJqD4Z9w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
صحبت‌های گذشته بیرانوندی که بیشرمانه به اسطوره علی‌دایی حمله‌ور شد!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/Futball180TV/100935" target="_blank">📅 09:42 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100934">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f5e2e3c171.mp4?token=bfQUW-L5gxF8_y3GR_M_EkVG07DMi-lFIfD1BuAj4YFi-UaVbIa9f2qa11YpccvHCjk3rFMc5CLFn7Bk6tTFnD4vUzZMTtkrW2Bx3zU2pjvvTR-R6PZHdlnyNs0qHGzi8HPKnoqX4gyllieyAuoTA6ikudEXk_RVX5CayDgeum1B7jEwmZND9_WTSxLCiq85tN5pWsBer1d6iGvJ9om-en3DiuTyLdblcUNzJOzRjXdUSotn0P8yO5JJ8fhjqqQLDzLbajSDtnsaxla1_B7gD1Qi-O7MN4skl_-USFphjgySOc3X1F2odO-jfx9ZXpbq1RZYNiQQ5-NIaKDZ6XIs6A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f5e2e3c171.mp4?token=bfQUW-L5gxF8_y3GR_M_EkVG07DMi-lFIfD1BuAj4YFi-UaVbIa9f2qa11YpccvHCjk3rFMc5CLFn7Bk6tTFnD4vUzZMTtkrW2Bx3zU2pjvvTR-R6PZHdlnyNs0qHGzi8HPKnoqX4gyllieyAuoTA6ikudEXk_RVX5CayDgeum1B7jEwmZND9_WTSxLCiq85tN5pWsBer1d6iGvJ9om-en3DiuTyLdblcUNzJOzRjXdUSotn0P8yO5JJ8fhjqqQLDzLbajSDtnsaxla1_B7gD1Qi-O7MN4skl_-USFphjgySOc3X1F2odO-jfx9ZXpbq1RZYNiQQ5-NIaKDZ6XIs6A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
صحبت‌های گذشته بیرانوندی که بیشرمانه به اسطوره علی‌دایی حمله‌ور شد!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/Futball180TV/100934" target="_blank">📅 09:20 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100933">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ff910de710.mp4?token=t0TR3AA0yBbkQWjckd1TLph9rrWS2TFgKBE0ogMY8iaEfJ-x_9SXQ0ZHChwT2azWKNqEaGa8dNasmqOsJj4LyGWgb8uhOlApVyB24Jt3uNqg0LiNgy06OCGTQpX-UoY88TCfdYLj-8WpPX06lOmatC0Ey6AP6EokgaGSupOOqHGb7gYsqFMG3MbyNJPvNX-Fam8LGl-2Zmq9Ctn6CS_FdUmSkWoXSRT9SGM9Alj2DzHUU5XCMkGIDZTnu9KbWOZqAUvIMqVyCk5le72ZrOBhRrCITibS5bybfUoTa77bA2maLPKLLiqJw4tKP_Wfo7xPM32xvDG9r3jS0N7q38Hkb2J9qL1_V0rjqtsNebJpfnOn8scFiNc_gQIv1MP4tWVQdJ2oqx9FEtxBn8Q2tzyBDIy1C9O9Y41wR0TwjrOievYxKiA8JLInQO_320-CCzolwQhk_tC0lUJVishVvbtnp4aveZzpKb1e34ebzbaf2tk4w3RfuFmHCK7qnrkbD995UefPIcEIfSbsiLNfDBr3kLNn-tZ-exoO4dT5frktso6UkSelLi_WyU-Ku7jvYDbX25aAiDNxmqlIxhqo_s1RIqS0LRAM1bN4QnnwPvl_hmp4_Idl2F5uASiOoG3ShyrgRO1odZeEkSuBUwpETweRQTykEtXZUeuPYfom8Uze-Bw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ff910de710.mp4?token=t0TR3AA0yBbkQWjckd1TLph9rrWS2TFgKBE0ogMY8iaEfJ-x_9SXQ0ZHChwT2azWKNqEaGa8dNasmqOsJj4LyGWgb8uhOlApVyB24Jt3uNqg0LiNgy06OCGTQpX-UoY88TCfdYLj-8WpPX06lOmatC0Ey6AP6EokgaGSupOOqHGb7gYsqFMG3MbyNJPvNX-Fam8LGl-2Zmq9Ctn6CS_FdUmSkWoXSRT9SGM9Alj2DzHUU5XCMkGIDZTnu9KbWOZqAUvIMqVyCk5le72ZrOBhRrCITibS5bybfUoTa77bA2maLPKLLiqJw4tKP_Wfo7xPM32xvDG9r3jS0N7q38Hkb2J9qL1_V0rjqtsNebJpfnOn8scFiNc_gQIv1MP4tWVQdJ2oqx9FEtxBn8Q2tzyBDIy1C9O9Y41wR0TwjrOievYxKiA8JLInQO_320-CCzolwQhk_tC0lUJVishVvbtnp4aveZzpKb1e34ebzbaf2tk4w3RfuFmHCK7qnrkbD995UefPIcEIfSbsiLNfDBr3kLNn-tZ-exoO4dT5frktso6UkSelLi_WyU-Ku7jvYDbX25aAiDNxmqlIxhqo_s1RIqS0LRAM1bN4QnnwPvl_hmp4_Idl2F5uASiOoG3ShyrgRO1odZeEkSuBUwpETweRQTykEtXZUeuPYfom8Uze-Bw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🎙
پیروز قربانی: «هنوز هم می‌گویم با فجر نیوزیلند را می‌بردیم»
‌
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/Futball180TV/100933" target="_blank">📅 09:03 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100932">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Vhf65D3pnFP-i7wKQfuvpKmIsJziHXI5Dg6UeACgk_SiNCq03_YsQxcHnXSsrZgzWnrv9tnoG3MINkLuYolVfXIRlUIkxygClXmkRf_-lV7Sj0HNEHIoFIQTCJrMWTd-XGHsM5jomQCR3y9cTWAHWiOO2LUpwS5nkLTTQm-qBe8sUHJZ76l0Zh63fjC-MKMxrVdidFrMmbHZwIttbrYppVhbsRkg112ETgXR0fyiy8OEoMG_3b-nRCBN2FbsdjyaYL7F_0ORJgLHMHIwUggO2Q8_x2YD4zlt4bg9wduOnZ5BuaBMtZEwBYxqvGEEPPSmhVNnhVl-cvjgv4Tbocbb6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🏆
پیام لیونل مسی، قبل از فینال جام جهانی:
🔺
زیباترین بخش از تمام این سال‌ها، هرگز جام‌ها نبودند، بلکه کل این مسیر بود. همراه بودن هر روز با این گروه، مبارزه با هم، ایستادگی در لحظات سخت و لذت بردن از هر قدم در این سفر.
🇦🇷
از تمام هم‌تیمی‌هایم، کادر فنی و از همه کسانی که هر روز تلاش می‌کنند تا تیم ملی آرژانتین را به یک خانواده تبدیل کنند، سپاسگزارم. مهم نیست در فینال چه اتفاقی بیفتد، این گروه از قبل یک فصل از تاریخ را رقم زده است که هرگز فراموش نخواهیم کرد و هیچ‌کس هرگز نمی‌تواند آن را پاک کند.
🇦🇷
سلام آرژانتین
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/Futball180TV/100932" target="_blank">📅 08:56 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100931">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d65552b958.mp4?token=L4xS1Hq7hNiAPfVCDjuiilabtzCktDKrGnbzccOoCiP2kDcefNy9DmS6UFn2VDcO9yz4JOQvOmBv7daYmQ7i42weMS17W8KU_b-rBsNzmWUAr3C8t6-vpSoQKhxc69ZW8KZaNSwfbakv3mblx7TEwh9GvpdOcTCWuSGZCqHfhYBFTuHZn7ZfUQjsivHZkxwBn97grVLAl6rIVP6p0H3mQn83Yb6guJbArQ85oN_Q-h4wiDH8Q7FLdicmfK4fetlMdr1N2f0PWK6T4RhdqifqWuCMQNgROUmqGyrtxTAa9mvM0hDd92vT3p3aoaNozPJy1B2G6DMGYamlxa5tUb3vJw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d65552b958.mp4?token=L4xS1Hq7hNiAPfVCDjuiilabtzCktDKrGnbzccOoCiP2kDcefNy9DmS6UFn2VDcO9yz4JOQvOmBv7daYmQ7i42weMS17W8KU_b-rBsNzmWUAr3C8t6-vpSoQKhxc69ZW8KZaNSwfbakv3mblx7TEwh9GvpdOcTCWuSGZCqHfhYBFTuHZn7ZfUQjsivHZkxwBn97grVLAl6rIVP6p0H3mQn83Yb6guJbArQ85oN_Q-h4wiDH8Q7FLdicmfK4fetlMdr1N2f0PWK6T4RhdqifqWuCMQNgROUmqGyrtxTAa9mvM0hDd92vT3p3aoaNozPJy1B2G6DMGYamlxa5tUb3vJw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📈
🧠
صحبت‌های زیبای هادی عقیلی درباره جنبه‌های دیگر بازی لئو مسی؛ تعریف متفاوت فوتبال در دنیای مسی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/Futball180TV/100931" target="_blank">📅 08:40 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100930">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pZlHjM1Ut_RKEvjOLdoI3qwPNeupuhkHujqqyunTKNq0GAhpM_PK6_k5vSNgDaQD-ukGxzLsu2s6knFlPnbMq9GdvANv2_9fHrVXGT1LD3Cqs48GOYlVwgw0Z6wSPYD99c9610qu4xVydv1JCaKocRIkv8cUr7GRE5G9_1JY4a1RhKo5n6xN9vQ_geXZngorzu0h-66sFK3cjR5MKzlYTMAo2h1AaUf7Yd9lBP6NpqF6z7fGTMokY-zARZq3LUK5s1DPDQxEzslfRNBDNVr-AmhZvOY7EMsP4uR2kyyyAwCuDG4lhxhs0QdN6F8CTD28MQc4AWs2NuBwMMXqipp5XA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
#فوریییییی
:
✅
⚽️
خاویر تباس رئیس لیگا، تأکید کرد که بارسلونا اکنون تونسته به قانون ۱/۱ برسه. این یعنی آزادی نقل و انتقالاتی بیشتر برای باشگاه بارسلونا در نقل و انتقالات
‼️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/Futball180TV/100930" target="_blank">📅 08:11 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100929">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1802a702ca.mp4?token=lk1Fd0I_hz9uRyhCLVP1dEj6bnX_s1oKBViclmUf2161yY-JoyWSGEVCpGRDmk2Zsc1zW_iQGtWFcgV8fUr7HJgv7gfhL0ytHtuEObu8No5jcMuP7EwDyINOLAdcxpTPYrfAQHrYvyzf5UFs5M7VUKIGaKkF0gGEoMiVUMJMcubzqXklU6aL6keyAANo8L9GCJXBNSHMBq12U11FKPg1fOZO5HWoPKl5vpN8GI_7MbpuMFj_fRPl1GpSFh1SOhhM2sSB5qkN1KCHyeEep9FXEo-Qrv9BBG8aDUkbnKzj0Y3FJtD1bi-rPtx5AtuPhlFrcKiHKEa8FxEmJm25YDXBkg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1802a702ca.mp4?token=lk1Fd0I_hz9uRyhCLVP1dEj6bnX_s1oKBViclmUf2161yY-JoyWSGEVCpGRDmk2Zsc1zW_iQGtWFcgV8fUr7HJgv7gfhL0ytHtuEObu8No5jcMuP7EwDyINOLAdcxpTPYrfAQHrYvyzf5UFs5M7VUKIGaKkF0gGEoMiVUMJMcubzqXklU6aL6keyAANo8L9GCJXBNSHMBq12U11FKPg1fOZO5HWoPKl5vpN8GI_7MbpuMFj_fRPl1GpSFh1SOhhM2sSB5qkN1KCHyeEep9FXEo-Qrv9BBG8aDUkbnKzj0Y3FJtD1bi-rPtx5AtuPhlFrcKiHKEa8FxEmJm25YDXBkg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رائفی پور ایز دت یو؟
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/Futball180TV/100929" target="_blank">📅 07:24 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100928">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">🚨
🚨
#فوری ؛ زلزله‌ ۵ ریشتری شهر سالند-خوزستان را در عمق ۱۲ کیلومتری زمین لرزاند.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/Futball180TV/100928" target="_blank">📅 07:12 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100927">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">🚨
🚨
#فوری
؛ زلزله‌ ۵ ریشتری شهر سالند-خوزستان را در عمق ۱۲ کیلومتری زمین لرزاند
.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/Futball180TV/100927" target="_blank">📅 07:07 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100926">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/472dab2e65.mp4?token=Hs1hYvK5mU42nI0mW8DnHQ4h7Pqk-6g8oHXbL6fkHV7OgTV2RIqcnebjZbOEdP_qsiWhZJfYcEs0As80rvll7NEF6XKmG4SHgRNxThH101FX_RmtrkVHg_SYwHRyGeZCaV4JuzdpIdw9k-wpH91G9lCXUkX80IUhjqepM2aNvndjohnfC_uJxcWj-yTWSqTLEq-OzOJGVoSWmtXzcGGzjcXCSQlIJs-wjHeeyiipiMcoGxeEnGbf0ehiYgfkMf4cbcVedZC-MhpBRH18sFTAxocWhuRb03ngOi_eLCoLY-_diambv_8eYBN9PxG4F-KUIrmQ_RujDOMq9gmOOLQGKA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/472dab2e65.mp4?token=Hs1hYvK5mU42nI0mW8DnHQ4h7Pqk-6g8oHXbL6fkHV7OgTV2RIqcnebjZbOEdP_qsiWhZJfYcEs0As80rvll7NEF6XKmG4SHgRNxThH101FX_RmtrkVHg_SYwHRyGeZCaV4JuzdpIdw9k-wpH91G9lCXUkX80IUhjqepM2aNvndjohnfC_uJxcWj-yTWSqTLEq-OzOJGVoSWmtXzcGGzjcXCSQlIJs-wjHeeyiipiMcoGxeEnGbf0ehiYgfkMf4cbcVedZC-MhpBRH18sFTAxocWhuRb03ngOi_eLCoLY-_diambv_8eYBN9PxG4F-KUIrmQ_RujDOMq9gmOOLQGKA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🛑
گاهی بزرگ‌ترین ها آن‌هایی نیستند که بیشتر از همه دیده می‌شوند؛ بلکه آن‌هایی هستند که بی‌سروصدا همه‌چیز را برای تیم‌شان فدا می‌کنند.
🔺
انگولو کانته‌‌ی با تواضع با دوندگی بی‌پایان و لبخند همیشگی‌اش به یکی از دوست‌داشتنی‌ترین هافبک‌های تاریخ فوتبال تبدیل شد. او از بولون و کان تا لسترسیتی، چلسی و الاتحاد مسیر پرافتخاری را ساخت و با فرانسه قهرمان جام‌جهانی ۲۰۱۸ شد.
🔺
امشب، آخرین حضور کانته در جام‌جهانی به پایان رسید؛ نه آن‌طور که خودش و هوادارانش آرزو داشتند، اما با همان وقار و جنگندگی همیشگی.
🔺
خداحافظ، کانته؛ فوتبال هنوز هافبک‌های بزرگی خواهد دید، اما بازیکنی شبیه تو، به این زودی‌ها نه..
🔥
👍
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/Futball180TV/100926" target="_blank">📅 05:52 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100925">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4cd61ad475.mp4?token=LCVUgtR0mFfBYuVtlJohUaVlGTp8jUh6LB63l7Q-W90CU110lM4jno65_A1I3TZdY9hpUcFO-0KXM6pi_sGAs6LeoIXz3TTIxBUa-8LSngzh0VPnpypMOfqioHAARiAiJEko60Im5K8QP8iTtaNZRgZuqFDL1y7f4rJu_dzXVwt7AjFPgzIc1Lkq8fdldbETrzwrmxmTRftNa8VTU-F6MZaR0xe3oEdUgdg3LuTxoWGrDsKTfBQ9UdF3eaNUOWPOkD7n7GOOV5cyqnYJafOFRK5Z3SDxdum9JpsPOVEW7FxI3_skd9TPaf-Tqi8Oh6iKq3wiFT21MIH4ldRn9M9S_Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4cd61ad475.mp4?token=LCVUgtR0mFfBYuVtlJohUaVlGTp8jUh6LB63l7Q-W90CU110lM4jno65_A1I3TZdY9hpUcFO-0KXM6pi_sGAs6LeoIXz3TTIxBUa-8LSngzh0VPnpypMOfqioHAARiAiJEko60Im5K8QP8iTtaNZRgZuqFDL1y7f4rJu_dzXVwt7AjFPgzIc1Lkq8fdldbETrzwrmxmTRftNa8VTU-F6MZaR0xe3oEdUgdg3LuTxoWGrDsKTfBQ9UdF3eaNUOWPOkD7n7GOOV5cyqnYJafOFRK5Z3SDxdum9JpsPOVEW7FxI3_skd9TPaf-Tqi8Oh6iKq3wiFT21MIH4ldRn9M9S_Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وقتی بین دو نیمه بازی فینال منتظر شکیرایی ولی با این شاهکار روبرو میشی:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/Futball180TV/100925" target="_blank">📅 05:12 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100923">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YB8JmMfNhcRVger-PDf-ZCg5RYop6TmBCo8dnHgbCL0cmMs6E9G5YwEf3oG2l5OgLlCl1fYhtKKWdomx85mfk25ojHn5ctfnwYovuCRJhdBu74F6bb4PYcGCLMUv6CSKAktEJyJim3iSG5DGL-f8p2Iv3VpmWogp2mqJ6f690En78PifZ6QGC2nb2yU8YJm470BK87o8m0wlaSVt9NB-gPWE06e_BQ3jFMhWcjiJ0WPEl-J8M3tt-bkH1GNzriDcYlQHalni-R_6PNETR9lQ9VX3HWVswW9PdoOKqoi-VMvv5vvEZygWeqmSZhhBot7Xx9H2y1EudADtqKtofIazbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WrZpsxrBSSAeb3hoIbqOqnCa9cYJyV5nGjGt-7cgLY8DZHIbcFFt0KRcTUqbcuJl6LlRN2fMIyrE1pCBQNdQ-Z6oTP63N2G49Q9MhBjeVwWMlgjsk-BKkd69ucXvNqfIOfhxJ6MLCpbDFeasdtq0t0nsyHrDOop25oL75xuXztqbIEPEObomRiW71r6gA4n9_zKcDOaT8nEnSAS862pYyDUmD4Z7rZ-GGN0iuXQEoYThzlezYRhXg4dRmNznrn0MZK3tXQoZwOhJlkVIpF4s12kmAOri9CoYw83eXMFvuwXooTvIVdPFaCgY_XhRq_eEOkPAjzLrNSoJAIsVtbK-zA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
📊
🇫🇷
اگر کیلیان امباپه در جام جهانی 2026 برنده جایزه بهترین گلزن مسابقات شود، به اولین بازیکنی در تاریخ تبدیل خواهد شد که توانسته در یک فصل به افتخارات زیر دست پیدا کند:
•
جایزه بهترین گلزن لیگ اسپانیا
•
جایزه بهترین گلزن لیگ قهرمانان اروپا
• جایزه بهترین گلزن جام جهانی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/Futball180TV/100923" target="_blank">📅 04:36 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100922">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q8Q_nBgi8rFR2bTMqpugMHGGPBKQ1jOhgxxyGVZEqDfbZFKmv1xTOO1cj9mgk35ydVV3MbJ1ei0dLQEOaGIh68D737oeNE4srOaEYiMfASJ2LpssyKe5oiHeq54bQgy4Xb7c5xsh9sDS5QdP2nqybCE6E7WqyDYhhQkHFl6yNE4ti0ujkD6veSyoffQ69-xkTo8uFzHoAknguH2ZhzYCIDjayHo_0cbPfCkOWrZYCgno1-Km47nuyB9RcgfSfsSfifi1fENQ9EBJDGlTtg1PLptqS9z3CjQTknc2h78aT7MW772tBIHQkMZhIaVONgzXhcd365QrAuxo6yqsiqu6yA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">☝️
تیم منتخب جام‌جهانی 2026 از نگاه ESPN
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/Futball180TV/100922" target="_blank">📅 04:26 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100919">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/AcWV2Nlkt2VZmyY4qH3nYv50DhTEbHqm7pTsOK6zWyItvoyomAK94SMODPYlF88qbMSEdcj-vunHBKZTRJZIzTy1yAkgpw6bT1oSFDx7dluCeSlrksQOMEoqu88sKptgBeYN8gYh4JtjFSDD_j86ag31r75fiSZozaZQHhkdPckyQzyj9-mcG6YQneXmZOBJ3Xh86xBLHXJab2rvtu-dSYoE1niqVKUYSpo2Gix3TbERY_M4F35mxs_VYNscBX05JFHP3-36iJT1rEvfOpfa_QWYLkJTbKz9JfU9FzKDDmnZB2btVI0tn-xgDjvYbyxMv65yg0k31MopjI5j04FAGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/khJRNVOjO4PcVa-JAbPoPCxZub_1ScQtLqcJe78W7jAUW2UbO6M0uBY6weUZNja6ofFR_9M3ZpUf6bIT8N-GoPiAY6m5fzCghQm2rGWwQUeCFOT-iyrPRebs0Ohit4wM4ijHYfgyFBeRkYMHRCT7CMr4umMdbr8sj8cP1dXQ4jKk4DMCkjWXGw7uuHEfRqtHNAPyVY3ee-GslgRe6TG4IAyesRTgtCsNPZ3Kxsq1T0YEBvi0UrW6rnjxDz6qH9usvW0KKWIk95qGbbGvySICJm9d_SI28afV7ddHP2MbieAfekqiknnx9sbwS_x5FDetktlvWEavHdpEL4JrDMaBSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ooPm39Up1xAZzt6uvabH8ycOpvzpDy3D9tmLZqCzrIYNrovJGTRKCGV_xpAFH72w3e4tR8znxteAjWuPauIThqF2z4hdXykWMiIqJoR-6Qhb6lJobCkGmWuEuBovzMnZCACLRaIr4S13wXhR6pcgibLIUsuarYd09fWppDmAoltaBIqZmDKt62VFyJ3APlMexVbTVArf3hY2wevC7_m0n7K-1yzqy9yel8sHJGQwluRldp0FjcaSwY_dM0ZgjhYoPcAGZCkE0KWjvSMO8nyWBHMspZngcl1bEUT5EC7BP3jsNaLpIO70mNQ3ot57c-pjNn9QR-JFt-0mLDA9JRzOYg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
📊
🏴󠁧󠁢󠁥󠁮󠁧󠁿
جود بِلینگهام اولین بازیکنی در تاریخ تیم ملی انگلیس است که در یک دوره از جام جهانی، 7 گل به ثمر رسانده است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/Futball180TV/100919" target="_blank">📅 04:18 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100918">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromجام جهانی 2026 | فوتبال 180(𝐄𝐬𝐦𝐚𝐢𝐥)</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uUKF-Y8qVEoLa_MQvwq83oX-XvD908t2AXIntzdc9PjA6QmWVmn5prlmsh-1lumuseaqV7KGe3n27tWF3pwcAkLBSWrVJAZnUXRXQ9ELVka8TdfwRC3guxhvhPWNEBOjbzlxApafPQFHcGsRILgVnoDtZ9gwgBqRIoXVJJ9EsCSV_3YPRNfyxY04BY-KZBqwDvH0jAcaIavjbzKcWyeRqy0hrN3UqlUvVd87fK_cVHbIKn1I-Q-pAvCq5QKklURlB8ygWfdu08-Kf703gVRxupGJ-O1iPPHp4VFO2DnqLoVkuQKAPYFYpfbKApSWxPo1E1Kb4Qp44pBuf-KdzadZMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
🔥
فینال جام‌جهانی ۲۰۲۶ فوتبال
🇦🇷
آرژانتین
🆚
اسپانیا
🇪🇸
🗓
یکشنبه ۲۸ تیر ساعت 22:30
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/Futball180TV/100918" target="_blank">📅 04:00 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100917">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m61oZQuVmjIEsGE0TT8ZGAthN1E79YXzQfH6mepbdmNLrO3R2UX0lkH0w39DJuayXVE7xHL5vsJAo08qJ0KVb5nJNpkDLSjzwqfwYyI7nYayKJvedHJCTjRLhjWMwkikp3VHMeHNqa5oTbnBopwgy2lKe70sgTPKZXJYwQpBS_yPKXQURIQHk4g0Yph4dKSN8PboFi7d9WGmqrGqDiMED81FNv_v0ewEeWz4jipoKJM39erQ-OyWguqyrdeNdGGHSoZiexox-fU-4us1eqT5bwWcSewzUMMKOR__7uTO_KsWbV91Kai-y1_GsY7lh8pm5atIx9f_7otk8LSGUhOfPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
بوکایو ساکا:
"در مورد پنالتی؟ جود توپ را گرفت، به من نگاه کرد و گفت: "برو و هتریک کن."
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/Futball180TV/100917" target="_blank">📅 03:47 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100916">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TddMTS5H8V8ulutjL3QCHiYMyqABoBSFFjeyRCNSpuKcm-_KI-pwG-D71hNinflsLQP6H9pihCmHH_hw9DCk8is0g6xL1WLrVpaAsBjYPf88wkyOJrthed15ytrAf8EpS-o1reyCGUmLkJhev7dBUqJ-paHWad0wj5pwJeUM6E3Zd8DFlTDkV9lhHtQOYbKA31nFp6NJX5UmnAYXoDUzEXyavvx5WyVe7kIj-XQLeFwe6Hf65hg_Im2HCxuBEtAepTJGSCGD1oyc4osyOxT77Swn0kzZMHMv37NiHwfjbG0UTsEvL3UfajVqgzyWmaCe1ldNCtj1tKGNLQx_sf9SNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
❌
‏
| هری کین فصل را با 73 گل به پایان رساند، اما نتوانست رکورد تاریخی لیونل مسی (82 گل) به عنوان بهترین گلزن رقابت‌های باشگاهی و ملی را بشکند.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/Futball180TV/100916" target="_blank">📅 03:37 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100915">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VaFcVPdHg6w5KQ8OYlVxrXEhU0V7u68ti0x5pFu9xoAQz7uu2BHsx22e8GvNKcXra2Q1BPcmGHOxdXMzcShlvFs-mOeyLWvMBNIYU4CouosoS56aJTK2KeWMo053C8k5g1nwFHUwZRnwEOMFTgkI5kUGT6OpQHvrP39hDToIwAv5oIhx4Q9T-9aDjUtXQ74yXAEeuV_HsnncydawSXD2JzptGthkogUOE70aNQOP0gz0ftBNyjcVVd9PDsq2iGBITb4_hfSDkNrRpNnj4hjyVPfPPH2_-ExD637cFx8XDP3K1q7R3w4UDN2V39ZFpXjbb0_8P3I4UnGA9-zHgKgm6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇫🇷
🏆
| مایکل اولیسه در جام جهانی 2026:
✅
او 7 پاس گل داد، که بیشترین تعداد پاس گل در یک دوره از جام جهانی در 60 سال گذشته است.
❌
با وجود زدن 20 شوت به سمت دروازه هیچ گلی نزد، که این بالاترین تعداد شوت بدون گل در یک دوره از جام جهانی از زمان لیونل مسی در سال 2010 است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/Futball180TV/100915" target="_blank">📅 03:34 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100913">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VC4gKC2uzSQKWZtzTB6qyS-k7j0PzloLsH0mv_-g_cTOezt3K8t9S5d-fN3XDSgwdOHyzHOZ6j8N5daxaY-FUN-FlNIP3dH_xnDJSDR32A-p1Z7sYyIVWFDIIqCZaVVsFA1X9Httca42D8-Ebs_dHquvkTITTY6ia0QVkkAtfbzq88E8g6Y2CxIK0W6mzWIoTym4a06NHyCYG-GRJ8Q9oK2y-Yp2I07qVKfhbJhYP33Gv18WOpkS1fdNUJcGskLwRZ7rH-J2KpefAMUfSdL-P9Wd6sRZWLMD-lAr6xVFb7WohuJfWimgKuVOimf6gYAr59w1ietFpEd1THv8xPgS_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/t9tPMeWFWw4UvkkoRJt75iiwDDBbap0YZyD1m2RtnQSbhAHEs37uByk7-lkEzw_RQlbi6fZ6zQzXI4ndQPmys7a6d6MTqynK8lNa_i2JtcJjIkL7jqRzgKEiG6nqwFWFcgxH6M3tib7531GsTyEPwTDYTKSbvwlEo4_7n9ptvWb78l08icFy_P5o75aTuFwfP683Laja9GTeLGT3caPGKbcW-G1imW4uyz76_6mz6s7Jou3Ad_W2ht2DQejAYBCctAMPrWv3XxgYLNyWiJ3LfP3pSRXT4YpACU-usbIENgycow6WNn2GRGUSX5754RhM-QQQZ3hlIeoKowaTOEqlUw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">جوری که امباپه برای فرانسه صدشو گذاشت و نشد...
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/Futball180TV/100913" target="_blank">📅 03:24 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100912">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pNLGI937ezD6HszvdPT1k6Q48Xm13hVwiRYCpfU-ckrg0b782PBwZeLfzuuJY-_wWoAEHoFFZds48TYyKX77wPE2tu-YT3qrpWOlWm2grevshQF4WQfjRKkclg6mDc2N01ywz_NMu-lC59V5UzpOR2K6PgBHCdtJcJ_fo_JTRtbPnB6ExR4j5HceKbLPXVFWUMKQl6VtW2TOG_mswCu7E4BENe6rKVrajVfRw2En1QbWWE5ypkGUPL9gGzqkQK4HSjekB_7xHoWRctBuC-cujxbY_pIQ_ND-0DscNJnSVhXD7NvWFun5ghUvLQL2NizGytJ1aZ5PIckslColYohb4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
🔥
رئال مادرید رکورد جدیدی ثبت کرد و به بیشترین تعداد گل زده توسط بازیکنان یک باشگاه در یک دوره جام جهانی رسید.
⚪️
بازیکنان رئال مادرید در این جام جهانی ۲۲ گل به ثمر رسوندن.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/Futball180TV/100912" target="_blank">📅 03:19 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100911">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X_mKaDQu9v87dQZc7dwCwZiB2CENwRM432b9K6W7HLlU7EIBZFYpFxTDubH9zh8XmqhzdIPfB_OL2VGJpibE6l9sxzn5kPfQQC9EzUvMKak4xxJfTfrO_mCHItrocuKzrSjzrxAbEop7tK6xHQvxNPzx3GhqdemPy8HkWP458HZPyaL8kCTcHC8434WTie_GvSSRn86brIATavRfhUjwmVc7tBi_STp81yb1K4B_dKuOh2bvUhTfBQ83gsHKAMbO_dMIy6LIoJPMwr3C7q-2Fu3r3aNLPNhq7nx91ww-yfkXG_lztnEysSUI9itR3r9U17uT5NOmTVOoQ2FlnZNJGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
📊
🏆
گلزنان برتر جام جهانی بر اساس تیم‌های باشگاهی در طول تاریخ:
🇪🇸
‏رئال مادرید: 99 گل
🇩🇪
‏بایرن مونیخ: 87 گل
🇪🇸
‏بارسلونا: 83 گل
🇮🇹
‏اینتر میلان: 76 گل
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/Futball180TV/100911" target="_blank">📅 02:58 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100910">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WuZseBnaWEo5zqtcJt4UCLM-AuHNu9YbTzkpXRfp-6XuEnilTZTsfZroEM_7QK9YVRQm2aenG3ujXOwNd6X2ntW7bumZ5WjLcYe1z3zVcw8v3PvFHsVow64jOtHw9Uk_stGGPn0dhTOHzbkybw6V8Df0yAu6hYvW-LN6Ek5CFxHxVPsf4ZLQP6pnoVrWkJ1Dup7BaSU_RP_ufqz5V2tT_3rricZ6r-gyyq6XMpv7cf-UrCrtXakEk9fAZx0Z_DEJUu22JEE5gzr6ad7oSYXiKsu7_zvJC1_9LIhBkYxr8ngNA4XfiVkhUVGDdvfpBuVWCEOlWN76-KUOrLjJfdRDcg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👋🏻
🏆
🥉
اینهم از پایان مراسم امشب رده‌بندی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/Futball180TV/100910" target="_blank">📅 02:55 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100909">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/veVhoLiHbBdk6PoWSNcsHIsncOLhSzHs2QAWAE-yuHgHMm4_izOPLB6Nbhi4pqu1FgprUtlW6hdp8UkoKgAiEzr2aumiaF_O77iLlCgibGu3u6TtMqAL8sGByxJweNfEQFLLznzSKEzgLohjny-eHFAczNdHMYuBisibukxbQahf65j6THNrtP6xwdGGfDeHn1xoEbKTzdzy7eJpwNloT4EHnSbnnFvLHjglXJgq1bUzq1zX3ChDa88t66zB4IelMqyXZ3Ka2Ccond0UMbdnAywmfA66PSYYypTSYetWi8tOlkAaRQ5u_Vo2D7jowDyosf_uvC5AfPKbPvebosnsZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
🚨
👀
🏆
حالت‌هایی که لیونل مسی جایزه کفش‌طلایی جام‌جهانی را برنده خواهد شد  ‏• به ثمر رساندن 3 گل.  ‏• یا به ثمر رساندن 2 گل و دادن یک پاس گل.  ‏• یا به ثمر رساندن 2 گل و خروج از زمین قبل از دقیقه‏ 78 (امباپه 698 دقیقه بازی کرده است؛ مسی قبل از بازی فینال 620…</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/Futball180TV/100909" target="_blank">📅 02:49 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100908">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JLB2wlS_jYNRQl1Ez8KkTJB72_guKVNk4QFRJiz72aJSThGZNnfNv48whiZvODW_whntwjTv8bnhQXVn9v11NPc18nrHvRJPEvy8KmfRkDcJUS-PeY1j5pZnEt1_9fF_qi6P4z4yRusfHflNHZDzqokomJHg8aPAJq35C9_YdP7lhEU28NHu4Lc3Hxs0rFIMlxWNcnX_JdJr1j20mS_HVXfKSlhYQREDm6wsa0pCAWGYCxoaibhsRd0YOxYcQm3QXDbe26XMcMKwxNz6rLjSlf8l4zu6unEUEOyDAjfrDRrT6WIXSrd4ueCSPJ3IBTwrI_6m_lDCLj8HbHQzPNdwQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
🚨
👀
🏆
حالت‌هایی که لیونل مسی جایزه کفش‌طلایی جام‌جهانی را برنده خواهد شد
‏• به ثمر رساندن 3 گل.
‏• یا به ثمر رساندن 2 گل و دادن یک پاس گل.
‏• یا به ثمر رساندن 2 گل و خروج از زمین قبل از دقیقه‏ 78 (امباپه 698 دقیقه بازی کرده است؛ مسی قبل از بازی فینال 620 دقیقه بازی کرده است)
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/Futball180TV/100908" target="_blank">📅 02:47 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100907">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t0yOeqtNfEfTYgr46hVExtGnyXImQxZOHZ00kANRUuGpjY-dujJ_xnJkTTI8o2ghGNejaV6x4QvL2GrMOKay9DuT-l5gNLF6QBLdd4VBcy2TUQ4NetQm--FL2mFFVD-yfqg1F1zvxuVNQOLczC4-eFQTFvan_rqw-zTyRSgxeoEhlyHvp-0EsLhAcGvVGJ2b6R_BIkbMleRlmXK2o0g21xcJ6UipOf5h0SpkFowhL_6aDjg5GuGbTGF-IK7sSIfTtkrf-fE_be7YVtlHLptVSeabGVHq75cv05nJW9aFYNNw-2kBImj0F2aHnOakM3z3ToUx2MJd5fff_BWPjXlo2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
❌
🇫🇷
پایان دوران مربیگری دیدیه دشان با تیم ملی فرانسه.
‏ـــــ 185 مسابقه
‏ـــــ 120 پیروزی
✅
‏ـــــ 35 تساوی
‏ـــــ 30 باخت
❌
‏• قهرمان جام جهانی 2018.
🏆
‏• نائب قهرمان جام جهانی 2022.
‏• قهرمان لیگ ملت‌های اروپا 2021.
🏆
‏• نائب قهرمان یورو 2016.
‏• مقام چهارم در جام جهانی 2026.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/Futball180TV/100907" target="_blank">📅 02:45 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100906">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j--uIdG6pumLjKZMBSwYPg6NBZYbq16ynM7NwBZgl4ozczuk3XVZVxP3Rv_5sqi1o1-SMRxgYMtHgKQpoqaCiAdo8IdoFfCplQHbTMxFBYst4RSjU4AsQfPRVcGc9Hg0P_yyA8iswIJSKSYG0Y1AuD_8rJrLPDn_AwWFLpPmjtfkYDTNHXofE6WlZm17obonWOY-PytLfe84M3Yx9IbnUA7VA4MIqjmUxiC3J-tyjCbEp9vojdXd2602G-yo5Iyr6_oU8LgiU_PpD1O1e9xoWo5EkCOZg22pCST6f_KtwOip6CoZvmqz4w6Ue_TkB7q_CCUNRpMSMZEfHIARp3Q7Hg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💵
🏆
🏴󠁧󠁢󠁥󠁮󠁧󠁿
تیم‌ملی بدلیل کسب‌مقام سوم جام‌جهانی رقم ۲۹ میلیون دلار پاداش دریافت خواهد کرد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/Futball180TV/100906" target="_blank">📅 02:42 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100905">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hXK92CfnShT4EKoPFJ2LgdRizuCtWLQIQM3Ad5S_dmpJX_HKQMM9VpCW8y0w9xI7Cek6DbC4MTcBtfy4rMMSEs5xI1KRJPbHb710brWvsZl04JNZoWSdb3bRRC1YYTPi-i4pZ74fXWLtvKdddvfyMNmEZZzV6-d1FMiTNEb_i-VJSjOivfDSRj4Lg16ayRc7GqjbszT8qNgTVEpxaI5Bp-_uUVIE_fVNXkf-9K0uaMfIrt8uYRTkA6n4mfAms2bobOkbWj3glxR4b3k1NY92isR9auaZwpXoum1Nn6iw_-RK4gUMMfPRR0oeVWUYMSEgNb6dVheTlQ5jb9_PRwLXsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
📊
🏆
بهترین گلزنان تاریخ جام‌جهانی؛ لیونل‌مسی فرداشب اگر گلزنی نکند، امباپه به تنهایی صدرنشین خواهد ماند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/Futball180TV/100905" target="_blank">📅 02:40 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100904">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WUCSWjsa2exQUajymKDwL03kceh5kteoboegZk6yFUSu3fkupO-cvNybRgMMWghBcsec0xggcmeLnpDBGXxqtEQf-iSUvNOsyg3P_jj6J5R_aCg5z4TU6SrDpC5NgmuvMFAGF_qVrmucnY61SXjbBA1p-LNW4dvyW-o_Z-1TYWkuoGq7_kNpkHAdH45h8rB5HylUt3fl1rvxJryi-h7VDDnq0urbKwLSn6_Fno7bHa1SeN3Smk6xPVVaY4KwNYCgYgav9otfki0tpIFQD6iikE3vUTQvMawDcyKWpXoI9vTe4fmS0EAkrxGhSsxtpwNQ2byBas9AFqun3_5Fhi44sw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
📊
🏴󠁧󠁢󠁥󠁮󠁧󠁿
جود بِلینگهام اولین بازیکنی در تاریخ تیم ملی انگلیس است که در یک دوره از جام جهانی، 7 گل به ثمر رسانده است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/Futball180TV/100904" target="_blank">📅 02:38 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100903">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JBhUGzx50yPyoBUk5aDT4RSiD2sBz26wB0qDX_C_jksRYaXUSLJmc9ftlyGZU4WuPIkyqwU-JuOoSXRRV16ib2zhqkpZvOx7_7IKeLWt9aicWcDnqMQ99hNsnXtiTPLyIIOgnwryLu5MhDl2Jhe963zPasPEIUZZt-zHF6yatSdRiPJYGiOiI3uRBFGZiJMiIHq_Er7EZgFufVYxh4tKixOQYLKBazWJBBnFvuuB2mgCIubIdOnMJ4JfusXOjYLf1wx4IF669P6MzG1nr20sy6Glo4kXn9GWlSlVb747GGbCXiQ3RmOBOGyihv1EuTR56PbZl0DWlHUS9qr56lEY2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
📊
بیشترین مشارکت‌ مستقیم در گل‌ها در تاریخ جام جهانی:
🌟
• 33 مشارکت، لیونل مسی.
🇫🇷
• 28 مشارکت، کیلیان امباپه.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/Futball180TV/100903" target="_blank">📅 02:37 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100902">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PbOUyGI1Mw5A01op5S3hMQfvirp44-0We5fQxcF0AF23dezc7Af56HAAyCMA4EJ7_iNpwE2L6ptmcpdg17wBKMFhcQ1uk4HPRKBcxsHwpXYc6WhlYOz_W3rdJ3n2bo3-tmmRD2_QXtxJ2FCzch5Yh1RMy_XhKOPfph45kwa-b3ZN6GBGMbvQO1PYKH7nrEdVBczab4EmFC5vClnl_XWX1l8pAgWuF6pe7zlF0uNDz7XAxJK-0CAPKgtX-8xa5kW8pADYfxzLalcU5O0ede9s7Hxh1xETQvIys4WVTb3o-vcb2_YdImdWUZIlRBcIEQiWabNc21dxJ7Iq-NR6MBmdQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
📊
✔️
ساکا بهترین بازیکن زمین شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/Futball180TV/100902" target="_blank">📅 02:35 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100901">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uqgnzicPdhk_4UKV4M_x7D3VDvBE4ng5IEYzJHqIy9SsdSZfppkfVaxPslTDZ8z9LjeIGqbAgwnk0xFujhPA-Py4SWfrklsnQMvLQF-oAqvFARFmKHU3kOmWbBIS41zVHF8Q0D31SJoXn3sBrU8LbkaoJ7x2FP3i4x7NHF0xMLikzVk2s9wSmFgc7DO0gi2eXsmztTohRQ3IeXGH4fX6GyGTFFzQR605Zgxj_r2B_tvXTBzSWtrg9hKdZ6Ic90bysXQoACr2yRRXnoQcZxENZ4jLeYgV1Y1PPPo8iy5rpXymsUT4b8xVpkTrAs5GSIv698TGp484JusNZsJTUQRWGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
رده‌بندی جام‌جهانی فوتبال|انگلیس برنده جدال بازندگان در یک رالی تماشایی گلزنی؛ دشان و تیمش در روز رکوردشکنی امباپه و اولیسه با مقام چهارم با جام ۲۶‌ام وداع کردند
🏴󠁧󠁢󠁥󠁮󠁧󠁿
انگلیس
😃
-
😀
فرانسه
🇫🇷
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/Futball180TV/100901" target="_blank">📅 02:32 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100900">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">گلگگلگللگلگل ششم انگلیس بلینگهام</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/Futball180TV/100900" target="_blank">📅 02:31 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100899">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/95a47532f6.mp4?token=eimRodfJZePddh_emlif9oWYt3x63isNtnjuYaEhOoCzmUlzJOiql200gs_XVm016rE-1RjL72zjsvdrigNn04EIqR03qlZxfwhXKaVK6XhVD1FKm_HdPAshuQxLL9kkkG76V6vqreWvZF1Acl5GPsMhIj_1PA2j4nKYRtGTXaWsk-JP3OMo9LMdGAQ1SALNCuqBfh01xXJns8oVOF_iOHGvpuCaMR4ex3swskiR1t2oH-KxaGQ9RTCgtUVkDNYflOTrwNivHhiCJRd52FDo3O56-AhNfC20nY7pqQgni5P90d7C-g44WZQd2fs1k1M3EeM0zPbT1uCdIF9LdjdguAUgJRtd4nREwdzp8AlQMKwW1sDokupotGKrtRUnw-uolkHb725uOdivVsWEnpgWBYgZ7Usdeu4DfRUjSD7eirsrN045KSEj-0_sPEpnfHWGoK15rNXKkO-J8-L0R7f4wxZHGJ-jm-OO1nm7thv45A-GR-TlZrtSoF-33gjz0wZu6JWAgVTiKBfN-4HD_9R0BZ7ec7Z9r3lwp-o6o8d__lzMsUjJbfXPMmVjh3Kb4Mgld6yYIazhBgMHx5Qjvnfcvbo03PPP2N2Sr5q82Bchn3re6Co5mnuN8uqKZVh9rWSHef1NO2SnIHLv6Sx2M1aK22bi-YNA0nQpr5Qk4W4Oh_A" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/95a47532f6.mp4?token=eimRodfJZePddh_emlif9oWYt3x63isNtnjuYaEhOoCzmUlzJOiql200gs_XVm016rE-1RjL72zjsvdrigNn04EIqR03qlZxfwhXKaVK6XhVD1FKm_HdPAshuQxLL9kkkG76V6vqreWvZF1Acl5GPsMhIj_1PA2j4nKYRtGTXaWsk-JP3OMo9LMdGAQ1SALNCuqBfh01xXJns8oVOF_iOHGvpuCaMR4ex3swskiR1t2oH-KxaGQ9RTCgtUVkDNYflOTrwNivHhiCJRd52FDo3O56-AhNfC20nY7pqQgni5P90d7C-g44WZQd2fs1k1M3EeM0zPbT1uCdIF9LdjdguAUgJRtd4nREwdzp8AlQMKwW1sDokupotGKrtRUnw-uolkHb725uOdivVsWEnpgWBYgZ7Usdeu4DfRUjSD7eirsrN045KSEj-0_sPEpnfHWGoK15rNXKkO-J8-L0R7f4wxZHGJ-jm-OO1nm7thv45A-GR-TlZrtSoF-33gjz0wZu6JWAgVTiKBfN-4HD_9R0BZ7ec7Z9r3lwp-o6o8d__lzMsUjJbfXPMmVjh3Kb4Mgld6yYIazhBgMHx5Qjvnfcvbo03PPP2N2Sr5q82Bchn3re6Co5mnuN8uqKZVh9rWSHef1NO2SnIHLv6Sx2M1aK22bi-YNA0nQpr5Qk4W4Oh_A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇫🇷
گل‌چهارم فرانسه به انگلیس توسط دمبله
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/Futball180TV/100899" target="_blank">📅 02:31 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100898">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">دمبله زددددد</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/Futball180TV/100898" target="_blank">📅 02:29 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100897">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">گلگگلگللگ چهارم فرانسهههه</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/Futball180TV/100897" target="_blank">📅 02:29 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100896">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">۷ دقیقه وقت اضافه</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/Futball180TV/100896" target="_blank">📅 02:24 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100895">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/b65d918250.mp4?token=omY7PsRMuT7IxQiwbEaLCMfhMRvlKXetiK2Ok2VTF4DlTyZRzPzZg3Pvuq6HXKO5SZhAdeQSvuqutBlm9EJd0TvXQomI5bmcWOcFtywofTcZxgb2ScaFA2_p74zd59_HiW17m5hSd1Iyx1BTW10ksX0vJRJ5xWj98Qijjo3bcicLzLk7rLxZqpeRctCwcwdpZksfCJGTgMvaIl_B6tllWwGRznHMvm4OyiLRlL-9m6cmD_yxMtqPzTysqNg111UgncCTMpMBMMewSn2UzjxiUyrDVEpXWR91UsHmFh1v_qnjKoFr5s0AILpfTjAN1g9FWcUCIkF-EqfjMTG6XN2XZ4TTbcRQLp_ir-UWkMZz6goyLD5xw3LOQjawnOwe9DHRX9zjP58zLilMgukAxyW_cM_AwPTqyIXO_uX1eGbtd1SNzqa5TIwyHYCjdIezhUZjsJTgMVcUy6CdbZiDr6J1ag489wGKgjd2fO8i3cJUAdbQfxUTnOnJvHMcPmc0ftgyV4hbs6gJf54MJuNMy5dfKQ54gNEGT3SlB2HGlHSd2pOR_B0GN9W93P1x-x9FbrhD_lRQAzgiurynggGl8xl5u74T-jsgDF1umeKI7_uMwUe7tRHc7VhOqu4Vtl5Wuq8Cm7iFbShCM8a7xJ7QJflWt48ftaxk4ES0G7eUWVlUo_A" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/b65d918250.mp4?token=omY7PsRMuT7IxQiwbEaLCMfhMRvlKXetiK2Ok2VTF4DlTyZRzPzZg3Pvuq6HXKO5SZhAdeQSvuqutBlm9EJd0TvXQomI5bmcWOcFtywofTcZxgb2ScaFA2_p74zd59_HiW17m5hSd1Iyx1BTW10ksX0vJRJ5xWj98Qijjo3bcicLzLk7rLxZqpeRctCwcwdpZksfCJGTgMvaIl_B6tllWwGRznHMvm4OyiLRlL-9m6cmD_yxMtqPzTysqNg111UgncCTMpMBMMewSn2UzjxiUyrDVEpXWR91UsHmFh1v_qnjKoFr5s0AILpfTjAN1g9FWcUCIkF-EqfjMTG6XN2XZ4TTbcRQLp_ir-UWkMZz6goyLD5xw3LOQjawnOwe9DHRX9zjP58zLilMgukAxyW_cM_AwPTqyIXO_uX1eGbtd1SNzqa5TIwyHYCjdIezhUZjsJTgMVcUy6CdbZiDr6J1ag489wGKgjd2fO8i3cJUAdbQfxUTnOnJvHMcPmc0ftgyV4hbs6gJf54MJuNMy5dfKQ54gNEGT3SlB2HGlHSd2pOR_B0GN9W93P1x-x9FbrhD_lRQAzgiurynggGl8xl5u74T-jsgDF1umeKI7_uMwUe7tRHc7VhOqu4Vtl5Wuq8Cm7iFbShCM8a7xJ7QJflWt48ftaxk4ES0G7eUWVlUo_A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
گل‌پنجم انگلیس به فرانسه توسط ساکا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/Futball180TV/100895" target="_blank">📅 02:23 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100894">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">هتریکککککککککککک
🔥
🔥
🔥
🔥
🔥</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/Futball180TV/100894" target="_blank">📅 02:20 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100893">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">ساکاااااااااااا</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/Futball180TV/100893" target="_blank">📅 02:20 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100892">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">گلگلگلگگلگلگلگل</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/Futball180TV/100892" target="_blank">📅 02:20 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100891">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">پنالتی برا انگليسسسسسس</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/Futball180TV/100891" target="_blank">📅 02:18 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100890">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">🚨
حملات به مناطق جنوب ایران آغاز شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/Futball180TV/100890" target="_blank">📅 02:16 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100889">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">انگلیس کووووون آوردددد</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/Futball180TV/100889" target="_blank">📅 02:13 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100888">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">واااای</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/Futball180TV/100888" target="_blank">📅 02:13 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100887">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">بلینگهام ریدددددد</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/Futball180TV/100887" target="_blank">📅 02:13 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100886">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">اولیسه داشت میزدددددد</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/Futball180TV/100886" target="_blank">📅 02:07 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100885">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">واااای</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/Futball180TV/100885" target="_blank">📅 02:07 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100884">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/caX_quuc0ms78e3fesHZNmlQkAaoNclZhvn6UqJhbQe6t0cAu54b9_tE0rw5AdwkpUhq3ZSN7F6rL-jIWizsyMpGEWbmsiwu5NioYLJCKmt4i8csBRgE4XUWK9-TAvterc7ISNjcm87EUmlohsm58IUVF2vtvo2Gri_S71kaLU9zY--vg_FJDcTDRZctLoN8zjTeGXUET4g5doa8-9PJ_qWe8MPoS-W9oJoXyq-5dKBo71T0_Aex7SBSAHkSxpjaTVV-lJSMTx8tl4S9Gv0BJY2d2BelR8-dNYBYPs-6BqF9QEhQGfttO6K4siIcmfHrLJ8nwaRsZFvBKwzk77m4_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇫🇷
گل‌سوم فرانسه به انگلیس با دبل امباپه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/Futball180TV/100884" target="_blank">📅 02:03 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100883">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">🚨
🇫🇷
گل‌سوم فرانسه به انگلیس با دبل امباپه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/Futball180TV/100883" target="_blank">📅 02:01 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100882">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">🚨
🔥
🏆
📊
مایکل‌اولیسه با ثبت ششمین پاس‌گل خود در جام‌جهانی ۲۰۲۶، به رکورد پله در ثبت بیشترین تعداد پاس‌گل در یک دوره از جام‌جهانی رسید
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/Futball180TV/100882" target="_blank">📅 02:00 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100881">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">پاس گل از‌ اولیسه</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/Futball180TV/100881" target="_blank">📅 02:00 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100880">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">امباپهههه زددددد</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/Futball180TV/100880" target="_blank">📅 01:59 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100879">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">فرانسه سومییییییی
😐
😐
😐</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/Futball180TV/100879" target="_blank">📅 01:59 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100878">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">گلگلگلگگلگلگل</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/Futball180TV/100878" target="_blank">📅 01:59 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100877">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QYR8cKqVqtubcxIDFZTVdWBrq0rBXJovaSpRf3bV5KE-yBsFBAUMh0pRvkeZafh2hLVfx1WEJpEBra3S0FreswoL5N7RaF5O8vjJyOscD5AkkldlPqIE-qJ91ULkEZVSAlb4dMtsMQ2FrLyTWe6ZYk5GAOph5I0SBReJBcP-Spn-alE96r-mAlsg6leRV0ZgjfXiBamjA99axep4RU_tBUTH38mzOdSoPybBs33iUtjR6UP5YJuxI2H6Vf5dyRR8j9iYTuV27htQ130d_y3ENxswTiHLhUq7WrJAANVp-NhEGXdosT38suSOx7ADmSHzvLz8Ftn5u4qSdijN2IsYCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔥
🏆
📊
مایکل‌اولیسه با ثبت ششمین پاس‌گل خود در جام‌جهانی ۲۰۲۶، به رکورد پله در ثبت بیشترین تعداد پاس‌گل در یک دوره از جام‌جهانی رسید
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/Futball180TV/100877" target="_blank">📅 01:58 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100876">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">🚨
🇫🇷
گل‌دوم فرانسه به انگلیس توسط بارکولا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/Futball180TV/100876" target="_blank">📅 01:48 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100875">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">فرانسه دومیییییییییی</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/Futball180TV/100875" target="_blank">📅 01:47 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100874">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">🚨
🇫🇷
گل‌اول فرانسه به انگلیس توسط امباپه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/Futball180TV/100874" target="_blank">📅 01:45 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100873">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">🚨
🇫🇷
گل‌اول فرانسه به انگلیس توسط امباپه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/Futball180TV/100873" target="_blank">📅 01:44 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100872">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">امباپه یکی زد</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/Futball180TV/100872" target="_blank">📅 01:43 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100871">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/MfPfwwpm_qd7w3SuHW52WOXDKVYIIREjTbENsA1h6pr3BTjjczlJkSY0hKh21Dz_cGcIls1UwLTFFa73GL3TFBnbznxQLsWY3bf3FctEdz-XFZxgNTiuyOz0Nn18UC2l20MR9BHm4T57oU-8pHkgWV8uW5guy-jVRWMhpVRaBEkeUGVA-O2hthwVGRBHFhwfhfoCKfuVqxgG9tB546OVXmPycgxA8NRL9Un2JbHib4sJAhH_cNi4w2WU2IdlM3WUIExi6HXOqS6Kewqts3dm48ToIOBFh2iH2n87Rv0_Uoa7lu0TyIow0fkq8FbqRtF3iLaJEMc-Bg5LT0ZWxhxWSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
❤️
خنده‌های امباپه در کنار توخل حین ورود به رختکن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/Futball180TV/100871" target="_blank">📅 01:32 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100870">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DJuQwVbao_zHW6aJ2pSoPSNoNIfU7C4iRDZsMZtqJbeWhbhOGFepZmMexw9ruAPGdjzEpNj2ym3RXfOBcQhp2HY-1wg7iV61U7KbaHIjvM_k8kbl11hKFLKIJB5uTFw5ugKwRp8q_mNXl2zEpmzHemGuQQJsdLfCCZNL9_DHrX0-PC-8aHTpQT59PXF3UH-yBePWrrzYJ7Zg81PmFf4HoLjkMfUVsVvZeVZ21jN_TWwcoCYB_cPDVsoa7BEj1EKjqJdp72DQQU4YW6AgGfy1fh0fU1k86ppBgL-WtyWcZPAy82VXTJNg6oxQa9lVlFjQzDHSZ5aBwT7P8np-MC_cKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😃
اکسپوزیتو درحال تماشای کون دادن زیدش امباپه جلو انگلیس
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/Futball180TV/100870" target="_blank">📅 01:28 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100869">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p1UwcbbVZPLCCGYFubYZhVHQfPVg8zbk_-36-3FD8fOCMhEZHsjaFearvQQUVC0Za8qTAlX9U3SdvshLUCEWqDA3jbq8BE1TL5hmSNhyCNerWfiXDUU_9OknC44_FSeHgDOzXQCU0-9Ss8vvVj8CmgKoCIp0yb25TGE_x6X1M2dfN2BeGQYXucSnJ4mzffmv4vBowuqC7CviII3rZtXO9pejLNME-QR75Cw1kKyhBJQEXa0YClsObMy0nfGUEu7tI17LK6FPhdoKe2I8zNbtzdivcXH58UxHBrb8y_gB_Bqcuv2I7D2IUZyrTZi05WeVuLFmiho6gjFK-fAYnwxQQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
🇫🇷
فرانسه برای اولین بار در تاریخ خود، در نیمه اول یک مسابقه بزرگ [جام جهانی و یورو]، چهار گل دریافت کرد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/Futball180TV/100869" target="_blank">📅 01:26 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100868">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">🚨
❌
نمرات بازیکنان فرانسه گویا همه چیه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/Futball180TV/100868" target="_blank">📅 01:23 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100867">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RTcS6W6sR0SiFUfFcSbiaGYKNa8bGiA9a2TVyd99uWlqZzPMyGgwF-Hzxt5HIsKf-BsoaO853DPm9O_xa77AZ5tjnd_IN1VHxX7Va_R146Ir9GDQoaY4KIHZZYcoIwbnUdxWGc8Y3jy69QEDMp3Jdfuzfs6TtwipnPukZsfbTNqJ_dMtQeKoSaiycLQnBg0xNJfA5VHg6tBLO72LP-ml8YnQuQLvUU1XNoTGWk5W59Njii3WoFO0qhKOsVmIFUeMjd41gwFKrnPV-bC9a2NtXI0MXHsyVjyNKvkiuvXi_nOQHVk6zTxPfX1cbCHM3K3E43AfEym6PpMTCO8kmQIGKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
❌
نمرات بازیکنان فرانسه گویا همه چیه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/Futball180TV/100867" target="_blank">📅 01:22 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100866">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">🚨
پایان نیمه‌اول؛ انگلیس
😀
-
😏
فرانسه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/Futball180TV/100866" target="_blank">📅 01:20 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100865">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">🚨
🔥
گل‌چهارم انگلیس به فرانسه توسط ساکا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/Futball180TV/100865" target="_blank">📅 01:18 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100864">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">کسب مقام سومی رو به انگلیسی‌ها تبریک میگیم
❤️</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/Futball180TV/100864" target="_blank">📅 01:17 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100863">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">دبل ساکااااا</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/Futball180TV/100863" target="_blank">📅 01:17 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100862">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">ساکاااااا دبل کرد
😂
😂
😂
🤣
🤣</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/Futball180TV/100862" target="_blank">📅 01:17 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100861">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">انگلیس چهارمسیییی</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/Futball180TV/100861" target="_blank">📅 01:16 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100860">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r3NatvoRXP5gsMT194ccsZkKfJ3qQKXCtiXkcPxeSnABIWpsuYkKDYBa4lqRXpmUdFIpXq3Wsx9RCqE9Q31h064DSquwmrveuWnwrcbNA3Ha4sb30DOkmKuk88RRzRM4F6-wZAYHulVM19zCu9LIUBBsGn-Z17JaZZVTcvSc1cqLBxW3O7CrZ8yVUQm0_zvdjn4bR-hd3qKG8Mg26jaBwx8j7JaUER1vzNZkDraJ80wo-UxALr3rEUR7QtV1OqvPIgBBJ_9uHiUIzsKRAvMHAY7cOz7CqvKRumRzTbHxCGvSXbNeX1HoncWulROQekFOoPMUxjJMjg0HJXR__b-IVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😃
اکسپوزیتو درحال تماشای کون دادن زیدش امباپه جلو انگلیس
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/Futball180TV/100860" target="_blank">📅 01:16 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100859">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qZSo5BoqE8IDlCwXw5YN8Vb86DHOlxEjtFLfGBtozh-AmsfEQUM9ahPv8UUECpM32a355HAymvNfDgUUEdY81jcv3EAFJKxa8N1q-JSH3FKhapou1XFo7XgengB2e3DgXm8zy8g1JwAO4JitIRhgQkX7tjOuRIg2q9zT7bybKWaeHMe9s9Yn-3DdqClXKOluop_uHy4NpX2PRWz5jn7KubsDn-SNynsAH4XTNgT2_fZF4haJ1OwtQFp0fb-sm2xypyf0F7xLR7SxVPHNrteRwUZAYSgwaHvYSLpiz3cVvNioBwv7x0-Cg2zUYWqr8dJxxwen54Wg_o_l_ZiiD2D_Nw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
😔
از فردا شغل جدید اهل دلا مشخص شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/Futball180TV/100859" target="_blank">📅 01:13 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100858">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QB1TE_HHsn_TDcpQvfdsrbkXL-9y-1TM-WH3j7gTvs0hBxyUXmmXDmNMs2Q7vyjyF9LltqsRadtPONsiBu1jEjWu4ocznAwE54qzHv-3Gn-qgGOUP-Gi0oqyiQdlh_H8IfeCr1ZU0xuyJBjaX6F629CIsnSzldh-UTYSSR886jVj3QWsmMyw8LhFxa4ZJL6ZeV59MXLp9qnD4MvLvgObXa-TnMoHmzhKtSkNbmUFwSWaIhd2mCY6oHyHHmOadasHHE_GPVDDaW5RdXcaEEOHSlbl-grE5rZCcHc6DiFAyGKldhrf-7Pxfq_P01kcw0l92lZHVgvIYHpfJWyx9NLOkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دفاع فرانسه رو
😐
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/Futball180TV/100858" target="_blank">📅 01:09 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100857">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/6441bdd49f.mp4?token=EUz8Dpd6769QFW_IuIn8SD_voOfACDckSyD69FtyNCKBZagkM5Zb4fyCsO8Xi2kAVmTNLrJHzzG-7Zha4ZH8GxX-n2p71GcbebVofvJfytVBNYl1-nipX4wVISAvG-bcpk5FbRQiAsq1jc3SEXxSIUZXk4Xp5iO8kZXM3Awg3ZAcTW6oEMbgZxneConFuYyzskjge0EKEmm65ri4pJGm7K3e3imvZzubARt49Ht7HIS9Ev3iSyW-r1zxByWIsGZHfws7SEn3QRCst3t6gIJvw9kESeBr1g4J6XC4DjDi9pDdqXaorpI98J2v7QpYCYTHJ2nJzIC6ls1b8ZgB0tVIKBOxUUb3ffnNn_2vIncTSOTOtFAszc2A0eDwMbDZK0ClJFvtwi2qXMJoQhEXb47UBEZB5k3CFfAmy1miHWMdvlHJJJRmLQx0CglQqNZExijz2yzb0JcaCnS-EU9j79XDYxXHQCmCwlaAfEkfvbqLeRg6-cH78AuIYzdnKOIqcGDPdZIRmTXl2A1oQgp4WqQQbSlIb3rYlx5XGo1OXtbOZTtFeQCPcRSVv_PA4gcKeXFyoWelQHq91tVHrYHDudQOIkWQEnDYxzstaVZg-IooHLZipaxcCyMBfpT9VwqJSV4Iz3lAXpiT5jc83NssWq-i8g2cdiEWx6b2u1_nJ_CE_os" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/6441bdd49f.mp4?token=EUz8Dpd6769QFW_IuIn8SD_voOfACDckSyD69FtyNCKBZagkM5Zb4fyCsO8Xi2kAVmTNLrJHzzG-7Zha4ZH8GxX-n2p71GcbebVofvJfytVBNYl1-nipX4wVISAvG-bcpk5FbRQiAsq1jc3SEXxSIUZXk4Xp5iO8kZXM3Awg3ZAcTW6oEMbgZxneConFuYyzskjge0EKEmm65ri4pJGm7K3e3imvZzubARt49Ht7HIS9Ev3iSyW-r1zxByWIsGZHfws7SEn3QRCst3t6gIJvw9kESeBr1g4J6XC4DjDi9pDdqXaorpI98J2v7QpYCYTHJ2nJzIC6ls1b8ZgB0tVIKBOxUUb3ffnNn_2vIncTSOTOtFAszc2A0eDwMbDZK0ClJFvtwi2qXMJoQhEXb47UBEZB5k3CFfAmy1miHWMdvlHJJJRmLQx0CglQqNZExijz2yzb0JcaCnS-EU9j79XDYxXHQCmCwlaAfEkfvbqLeRg6-cH78AuIYzdnKOIqcGDPdZIRmTXl2A1oQgp4WqQQbSlIb3rYlx5XGo1OXtbOZTtFeQCPcRSVv_PA4gcKeXFyoWelQHq91tVHrYHDudQOIkWQEnDYxzstaVZg-IooHLZipaxcCyMBfpT9VwqJSV4Iz3lAXpiT5jc83NssWq-i8g2cdiEWx6b2u1_nJ_CE_os" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
گل‌سوم انگلیس به فرانسه توسط ساکا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/Futball180TV/100857" target="_blank">📅 01:08 · 28 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
