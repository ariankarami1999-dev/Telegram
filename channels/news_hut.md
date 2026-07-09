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
<img src="https://cdn4.telesco.pe/file/hPcx50AwDt5oNyv-C_yvlUfVjEgdqDRbv_QrwAAkl-mneZLe9IP0LG2O38v7EDn1w7TLvERJcewgzIAztRBXGIUEw0SkNN_zKHE9T6nLSD4UYEXRNJvk22yBrEIqzTdxaYKVt8GVghqnph7Na9fAyZ40luWZdggqdHtNXblQExWQdEe7k8zQlJQ-JCHCtByiDxwxcqOe65wWCMzs2-7rM5ce9AEtrkadXi7On-XvPzanoaoWX3mAZWZTxvY_FnWbSTTFtgOcoyzhuJhQ9XGWdiryG4HGnGPYX7MEqE_tcz1bFGwlag5Le3L01kxZ5urtmEnRTfg7NmTSdvQiF_EV0w.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 هات نیوز | HotNews</h1>
<p>@news_hut • 👥 190K عضو</p>
<a href="https://t.me/news_hut" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 بدون هیچگونه گرایش و تمایلات سیاسی، همیشه سمت حقیقت و مردم.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-18 12:21:09</div>
<hr>

<div class="tg-post" id="msg-67642">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V7AGy89lmKvtUxhCxFLg2qq25BZosRfqCbATCxv39gT-72sjLYg9E_tuH8DOgr3Lc7CacWCOcGK62lXt7dG3uLEVaD-coQ3EnexHIp3ZlXYmUMlWk5HxpSOvzqysQzm0UMNFMNcpx1u2cYMNPoZT8B6uUGVwyy4n_QO9n0QnFLmS6QNCtoNDq4qYNWMungJY2mLp8NPnRXBqca-kKPynjosJh32cWRozaV_Os9d_S7Tl7dV_2Grs1lVZ4IhxoHSiACf6ArGEp6n8_eacSGzwuS45a3b5NUhoo4KARv9UC6TvqePb8XMbFopamIiEWRbYjOAR51xrPEs9fCo5hMkTBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
بیانیه وزارت خارجه جمهوری اسلامی:
@News_Hut</div>
<div class="tg-footer">👁️ 6.13K · <a href="https://t.me/news_hut/67642" target="_blank">📅 11:49 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67641">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">🚨
🚨
🚨
چندین انفجار در بحرین
@News_Hut</div>
<div class="tg-footer">👁️ 8.6K · <a href="https://t.me/news_hut/67641" target="_blank">📅 11:33 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67640">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6f84fc0204.mp4?token=rhsx548K9cldnTqC77EZSpuugZND38qKH92ZXK0Q9NUeOoM-BtSPWIdbOzJusA5Oa81UhfTEvlNk1y2HK_bzw_2rrVRoCNHzV69-_5f3NdlQSdKruABuonp0pmiXU4rk5TWMCMNEA4lsAzgJND1i74-iFPtzMVZ8LrhpkctgY7i_IdpXzVLpP4fLaoEGV_Bmgejh87-CJJzDOEc3qRP9X_02Qc0tmWxnO5P_JJsckA3V-U8DDQ-2qaDUZlV_LW3liztrs3i27idvipyD-1SlxDhNwOuLjFeCDwQE_GtffGidyDH7ym02wbutjEJaM16Wn2v_SHrt4yG-sN7xgReikg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6f84fc0204.mp4?token=rhsx548K9cldnTqC77EZSpuugZND38qKH92ZXK0Q9NUeOoM-BtSPWIdbOzJusA5Oa81UhfTEvlNk1y2HK_bzw_2rrVRoCNHzV69-_5f3NdlQSdKruABuonp0pmiXU4rk5TWMCMNEA4lsAzgJND1i74-iFPtzMVZ8LrhpkctgY7i_IdpXzVLpP4fLaoEGV_Bmgejh87-CJJzDOEc3qRP9X_02Qc0tmWxnO5P_JJsckA3V-U8DDQ-2qaDUZlV_LW3liztrs3i27idvipyD-1SlxDhNwOuLjFeCDwQE_GtffGidyDH7ym02wbutjEJaM16Wn2v_SHrt4yG-sN7xgReikg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بدبخت یه چیزی میدونست میگفت شانس ندارم
😂
@News_Hut</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/news_hut/67640" target="_blank">📅 11:15 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67639">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6d7a4381ac.mp4?token=gmH9NdUoLEYQTqEnjFuLVjw7LvLosG0HJh_zw2O7RU2fCZMbRTPHyfLQVqM0eLVUhYoDzXjSpSQVb4rxWGMlHxIr0roj0wK6WCDZ3UblDYrLu8Ssz027tjcqUDhBzPqEQCU7Qy7fLWORPhmt0jKMHrgz2SUoXD74_bK4C_ye069UDm8lUYdWvXqxLxPCF0qbSrMkIXuJqPhcIZr2_iRrCGl9NnNA1XcJvNohdOIDu_or_iX4BRLFo41LXcXn9SHMbEAdTWvt2ZytnohHmQqq-xl-fUSOcOz9labxEkFqx1xn1wMdhDu_ghIuUr33vSP_pXtif4esAXpZlHeIPMWl3g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6d7a4381ac.mp4?token=gmH9NdUoLEYQTqEnjFuLVjw7LvLosG0HJh_zw2O7RU2fCZMbRTPHyfLQVqM0eLVUhYoDzXjSpSQVb4rxWGMlHxIr0roj0wK6WCDZ3UblDYrLu8Ssz027tjcqUDhBzPqEQCU7Qy7fLWORPhmt0jKMHrgz2SUoXD74_bK4C_ye069UDm8lUYdWvXqxLxPCF0qbSrMkIXuJqPhcIZr2_iRrCGl9NnNA1XcJvNohdOIDu_or_iX4BRLFo41LXcXn9SHMbEAdTWvt2ZytnohHmQqq-xl-fUSOcOz9labxEkFqx1xn1wMdhDu_ghIuUr33vSP_pXtif4esAXpZlHeIPMWl3g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏸
آخوند میرباقری، مرجع تقلید فرقه جلیلی‌ها و پایدارچی‌ها: دشمن به معنای واقعی کلمه هیچ غلطی نمیتونه بکنه، بنظرتون میتونه غلطی بکنه؟
مجری: بله دیگه، رهبر خودش این حرفارو میزد ولی الان کشته شد
@News_Hut</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/news_hut/67639" target="_blank">📅 10:31 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67637">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q4T4cvUx2wAj44U5QjBTZnmEEYit1209fAECxEb0nPn00gKi4Sov_GQnGs3rMnPmewhsZ_Wwt-BuKqQ38vg76LTlsjPGW2r15wPVJjsq9Bn5h75b0lYFiEBVX0CtUYUabF4iuwLnNwqbESxZm7LDaeDS9hl9W-VEokHf4JyCzHyH1cJFlL1vjeNu8y7qL3DEXQYNKu6eSiqjGrimeVenaoGDbzLvAEAn4RSwiKOhNhKs2lfrOa6UT_ocpYjJpo2kZSRvASol_TNPnVDF7T0p-4rwtlMs9SwA5ZVJD0Qt_cZwen082aX4SmL99Ie4dmhcjcK4IGLPtuq0E2nTYIVYxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f0eec941b2.mp4?token=vbByqBpCPUvd8BBWYImGIWk3-gMyZQEUdU6X1OSg_8xoacg3LilKKcJZn21VikOuTQ4W0sbTgZVH-hLQ3aSrjFe60AxQZsFTy9e-1OM7T93R_pN69BHTwdNycmuKWXHaQwctsr329dfOomMbTsucQexauIGKGlf_xAvAjmXI1v1LYm5wRK9wJw03zhstK-05F8AC7CJLeIO3fpVPCWrq3KiHA68MuanZ1XBMbSzS0qGGg89YTE_cecxTr-9623FL5XAVgyDPxoE3aSJ2NazqDXKZZBQgPNJo1Y4KABS0trtOf9zqwYzg4IFUP8Nfn9rhavE46FbJS2KS7FWu-uNXXQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f0eec941b2.mp4?token=vbByqBpCPUvd8BBWYImGIWk3-gMyZQEUdU6X1OSg_8xoacg3LilKKcJZn21VikOuTQ4W0sbTgZVH-hLQ3aSrjFe60AxQZsFTy9e-1OM7T93R_pN69BHTwdNycmuKWXHaQwctsr329dfOomMbTsucQexauIGKGlf_xAvAjmXI1v1LYm5wRK9wJw03zhstK-05F8AC7CJLeIO3fpVPCWrq3KiHA68MuanZ1XBMbSzS0qGGg89YTE_cecxTr-9623FL5XAVgyDPxoE3aSJ2NazqDXKZZBQgPNJo1Y4KABS0trtOf9zqwYzg4IFUP8Nfn9rhavE46FbJS2KS7FWu-uNXXQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
ترامپ خطاب به قالیباف:
یه محمدفلانی (محمدباقر) اونجاست که با بیل داره یه کارایی می‌کنه؛
ولی محمدفلانی، با این بیل‌ها به هیچ جا نمی‌رسی، حتی بزرگ‌ترین ماشین‌آلات دنیا هم تو شرایط فعلی نمیتونن کمکی بهتون کنن تا به اون اورانیوم‌ها برسید.
@News_Hut</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/news_hut/67637" target="_blank">📅 10:03 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67636">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d3353d5522.mp4?token=NRaqo06BhRuWS5eOpWWAc_bUryP4l_OdIIdJjfdRH5nbjLaVT0DLktU0rbcG_rEy6Oe3vvM8Q-pefY9do2CwOmIyjbOuV4QQGmfok2k0_lVm2l6DA-jrXciB7Fzh3ZEfXuCdwyFsvw4yUohxRXiGqTn4X9CWXo-C4wg45L_IC9borTfZsAek5npktlwWhA2-kd4VXErrIVL5hS3fYCSO3o-JEIyuXtzfC0FOR8PWIYOtSOxVklM0aitOEqrB0nqgiEFPp74nPEkgYS7OCGzgrrJCTiOa2D2HPorGCypM5025GPNsS6aU_DAheVNM5-eImbUdDRbAC2LoDrpOigjwdg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d3353d5522.mp4?token=NRaqo06BhRuWS5eOpWWAc_bUryP4l_OdIIdJjfdRH5nbjLaVT0DLktU0rbcG_rEy6Oe3vvM8Q-pefY9do2CwOmIyjbOuV4QQGmfok2k0_lVm2l6DA-jrXciB7Fzh3ZEfXuCdwyFsvw4yUohxRXiGqTn4X9CWXo-C4wg45L_IC9borTfZsAek5npktlwWhA2-kd4VXErrIVL5hS3fYCSO3o-JEIyuXtzfC0FOR8PWIYOtSOxVklM0aitOEqrB0nqgiEFPp74nPEkgYS7OCGzgrrJCTiOa2D2HPorGCypM5025GPNsS6aU_DAheVNM5-eImbUdDRbAC2LoDrpOigjwdg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
فرماندهی مرکزی ایالات متحده:
🔴
نیروهای فرماندهی مرکزی ایالات متحده (سنتکام) در تاریخ ۸ ژوئیه دور دیگری از حملات را علیه ایران به انجام رساندند تا توانایی این کشور برای حمله به کشتی‌های تجاری و دریانوردان غیرنظامی بی‌گناه در تنگه هرمز را بیش از پیش تضعیف کنند.
🔴
نیروهای آمریکایی حدود ۹۰ هدف نظامی ایران، از جمله سامانه‌های پدافند هوایی، تجهیزات نظارت ساحلی، انبارهای موشک و پهپاد، توانمندی‌های دریایی و زیرساخت‌های لجستیک نظامی در امتداد خط ساحلی ایران را هدف قرار دادند.
🔴
این حملات جدید در پی اجرای موفقیت‌آمیز حملات تهاجمی در شب پیش از آن صورت گرفت.
🔴
نیروهای سنتکام در تاریخ ۷ ژوئیه حدود ۸۰ هدف نظامی ایران — از جمله بیش از ۶۰ فروند قایق تندرو متعلق به سپاه پاسداران انقلاب اسلامی — را هدف قرار دادند تا در واکنش به نقض آتش‌بس توسط ایران (از طریق حمله به سه کشتی تجاری در حال عبور از تنگه هرمز)، هزینه‌های سنگینی را بر این کشور تحمیل کنند.
🔴
نیروهای ایالات متحده همچنان هوشیار و آماده عملیات بوده و برای اجرای دستورات فرمانده کل قوا آمادگی کامل دارند.
@News_Hut</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/news_hut/67636" target="_blank">📅 09:21 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67635">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/bjzCEhgl8xGVNk9EVsAAmwKu1CljUUMuOYmLj_2dLsvLi9ib5fj1lraHyK_1xTAclXe5ZwZclCdRXaBjyawSMKCVfD-sAUH6UFz5ilHJVeI6iBT8V2lX9vvDRePP4jyCo7Y5jUjkFbjEKF6TOmAhOQ5ZpLtV3MbLP2xrPTFRRAtW7-G7_vyOllmJfdktbNVDUkBxSka-rU41rL5leQRIfQHm2q3Sdn13hpLALFx8sTR0XpfNJCtwpWSZ9Qhg_i8LKNY8FGjGc0yXc-YVmVTr6XRV6Ai2ctSOcsoOcw84b-DrWNRzCSCYjfr0SuG-FBimg7hPT6tn78gv008RaiA8dg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
وضعیت برج ترافیک بندر چابهار پس از حمله ارتش آمریکا
@News_Hut</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/news_hut/67635" target="_blank">📅 09:07 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67629">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GB95Mab-VDLxw1hC0_qTzXlkbwhHDuppy_WAmM7dj2_qPwqc2WDpiDpUYGafhyAdkC6JTfD1arpVSg3adOG-122NZDxhtqZNMzCWGlSyZ1XqKs7YO_NoiYSvtCORJJ3WzN9EXq5UdmcP9RRynKyYVTSLsP9qB4AutsVL0uhOiR-R0ZeqwK_fU_py1doNBd4gG3muxqcp70nlfi1D20CL2-Tiy2d5FL8IgpqjfRl03ArIJX4CV0lVnAJFqPj0GbzdqwL0TVgDZF8Imad4xfvcX8YWCCFtdRqr0AYLMLWCYWq-C44qh3taDv0GGaSZwFEZHnA7stKAI5inU3oEa9vdjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pov8Vbfwz1s-GPZSPX0XmLrvPw-HR6RgzaN-vHTsuhJ0q_NbFuoJs_zx8cEpXrCY4xgVIHLY876I_y2mA8jOtLqvSdKBClYBprv1BvvtOGJ5iex5PxKQ7RaE_DnTV-sFyWqvXKnqiW9_iV6qKrcAZF6hESzyCIsV1S3k_TEzVdWa1i_7wXOA9eyZRfHk6gr3JGMPJxTCW0n8QNujFba1kohSPCNknSCeO3hDQ_IgtRg5MbyUHfac0x7Nzkpu68G2ues8f39Kygw6HbBwgsFO5Iy0L5l-yZWV2d7RQWJ-fZ5yi2eBJRJ8M27FscAyiKOITFVjzsS3AbGJ20_MGygMow.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d64ac58e8c.mp4?token=v4ZedVRTnUWmJHu5lXrnKttgTKfPYIAhoRd0OAGiUx_9pjRos_im3wHG-8yW92-X1fJTQOW5y-Ze9D-n3pxEyHFjn-EEvusGHeTiDe_6yrKgsw_hrhKRq09tU78jSKakUrrOhksN4IRgPNO4d--sLFxcHn-mWTEj5gIKwYaDaKZEgXKQXrrernOsDAB6K1GTTv6INCe2s-K1_KTmNTkXY-hNfni_R-Qj3fk30Cc5m-fYOM-_UxcD8LN_HNbxJmuveW9s6kdEDZqWALM6V7j2XBUGAcE70BRv_n4CncVxaKFGHCQRN6J_jrjtUCnIQHA2UVMcIVDFF5Zki2QoC-8khw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d64ac58e8c.mp4?token=v4ZedVRTnUWmJHu5lXrnKttgTKfPYIAhoRd0OAGiUx_9pjRos_im3wHG-8yW92-X1fJTQOW5y-Ze9D-n3pxEyHFjn-EEvusGHeTiDe_6yrKgsw_hrhKRq09tU78jSKakUrrOhksN4IRgPNO4d--sLFxcHn-mWTEj5gIKwYaDaKZEgXKQXrrernOsDAB6K1GTTv6INCe2s-K1_KTmNTkXY-hNfni_R-Qj3fk30Cc5m-fYOM-_UxcD8LN_HNbxJmuveW9s6kdEDZqWALM6V7j2XBUGAcE70BRv_n4CncVxaKFGHCQRN6J_jrjtUCnIQHA2UVMcIVDFF5Zki2QoC-8khw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
تصاویر مرتبط با لحظه حمله و پس از حمله به خط راه‌آهن گرگان در نزدیک روستای آق‌قلا، پل دگونچی
@News_Hut</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/news_hut/67629" target="_blank">📅 09:02 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67628">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FuckBet @FuckBet @FuckBet @FuckBet @FuckBet @FuckBet</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/news_hut/67628" target="_blank">📅 02:49 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67627">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/qEJU9rkz96XVND6V6EvppLj6uQwbgG3-sEKSonmcYeCMequP6zRmqwm_Ur7MK6W7PgzabUx-Vzoy43n3p7E5oTM_7n9z926sPBSQ6dBwZZwXr4D9XF78L7rGNWzZfOGoX79m0_j-insVuS0Yo_o6LpkhMXG-OTpgSDrffislbQ6tIBt2f_wVzCyfT-k7c9RB8kDeGNu8U-j9cWLQKrOfCEdcnunUoRbFMyEzoiKgqN8YJqFmBoCXHKSbUNjITwq-BlmonkVHnNw6ldFJbaPM80NPyefb05WqVO63N7SpdTI-Tv8hhfiBfBGj2Wk0J75q0JBYf43Yj9Hb7ChQJ8rQ_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FuckBet
@FuckBet
@FuckBet
@FuckBet
@FuckBet
@FuckBet</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/news_hut/67627" target="_blank">📅 02:49 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67624">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gg0rGcSO8kWazN2dmJcuR8VdfjfiqEcIW65DkwasRtl8vLmJhoYlroXxkBR4uT3cc15ox-oBdxFy773iJk1DbNX0nS30w3IH1nDNqnF_z5O4TI2o5HcmGA-s5WRb4esDefLKvAGA0SW62M_mxtfnxX0-T5ctTZzRa4UI7XaXAxcjNtJYKxonV8iUlPv31W5JOR0-Hq_ksycZA6nNDN9sXnwnkxfFEHKilCowIbEZ2opjL4pN5BvmVjC3jRFN8YrYlM9ea_kjsH5Vxmq5b1WjCpQfXd1RenA6rtEizCFgFTJ7eDH22wvMZTFAqAez0ad88l2Dl7RzKFMWWcwjVld3mg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Jgf1MirOVnZxYYapBvQCsLmPDk76ZacVegVgIiPoMKON7r7FcslrpIE2sjtAh9YlAUJ7uRQrl_txwZumRJfwuwbbw-tLEzGsKBmq-M8AVWwyD-_HFGlfDP8_u3mqXgLH70pumLBnshIZRNrN-ztjKUQbdJhRehQm_Y6sPEQxmTufHeK2OlMBydNZ3f_BiUzmr3fLoMzRVsF5xaGaWfmZOG-HGmox83EcWhi7ZCRBsmB01KLyhywko9sE2Xi7owq5Vdm-rNlClxumFHfSYwpLZ2hQ64zxHDuqEZGcZ8Uu0YEGDP0yNFjJszzAuqEHniSN0Wi9a1l0ItH78AEcnEGg5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ENzd5fv3-3CqMA1J3C8Qgamcb2EwTAJZyrHFzdN-6DVvzlEhj_U-C8iLTJUnV_FM-r3QxGBfoATcoMmVyfIXzodGUJuwI4valKSPKyrSjCwqQXTGJA44RShjXBoxnXvjOeqGi-DHfOMnf32VCBD5iyzRpXxnUJtWSbwqes5wINSfmy3gShN42rrQmYruarCdDcS4JlUHC2MjSvRC_HaTorhOi02gwSN9GmRoiqs_GfhF-WGn8c1BQCKBIp1i5rhYmOwWxdHdv9he2cPdYQyLs3Xyzyot1p4tdRvuVTiX690UnvzfUNph8LY39Hx_kvh_-_Qamj-xxBdILTUvqK1xHQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
🚨
راه آهن نزدیک آق‌قلا در گلستان هدف حمله آمریکا قرار گرفت.
@News_Hut</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/news_hut/67624" target="_blank">📅 02:44 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67623">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/be4f434f83.mp4?token=J0z6I9vm1-1TPMBZDZbILpDeQNCI9ulV6qwSERJAxRq2XmiCaE74C-RTsRQDMqHUXgJnsIEaB-staLom80ZXGF_CzGZFZp035i7BZ4ElCSIxaRk_gH_D3zNTqd0hGO4yaQK4VGG2ORMrUSJANoUjD5QLa5e9bioF9tc-6DDxkPVrIXYWzfaHuWA_sexiHV4OdfEt5M_9n907I1ePnbVXuaZyIhbxX8JOYekgkdNFacsu0DBYLyi-w1gIR47B8GAASDa4DdYACu73w60VXa_39PUxouz9T9K87IZk7A-TJb9f5BIDB2KDuMgjFzkIwBv8jGy3tIfuoCuSo3uSrGGGLg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/be4f434f83.mp4?token=J0z6I9vm1-1TPMBZDZbILpDeQNCI9ulV6qwSERJAxRq2XmiCaE74C-RTsRQDMqHUXgJnsIEaB-staLom80ZXGF_CzGZFZp035i7BZ4ElCSIxaRk_gH_D3zNTqd0hGO4yaQK4VGG2ORMrUSJANoUjD5QLa5e9bioF9tc-6DDxkPVrIXYWzfaHuWA_sexiHV4OdfEt5M_9n907I1ePnbVXuaZyIhbxX8JOYekgkdNFacsu0DBYLyi-w1gIR47B8GAASDa4DdYACu73w60VXa_39PUxouz9T9K87IZk7A-TJb9f5BIDB2KDuMgjFzkIwBv8jGy3tIfuoCuSo3uSrGGGLg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
خبرنگار: اگر ایران خواهان یک توافق است، به نظر شما چرا به کشتی‌های تجاری حمله کردند؟
ترامپ: چون... راستش را بخواهید، این موضوع کمی عجیب است. کمی عجیب است. آن‌ها کمی از کنترل خارج شده‌اند.
اما آن‌ها واقعاً خواهان یک توافق هستند.
@News_Hut</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/news_hut/67623" target="_blank">📅 02:34 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67622">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/518cba3871.mp4?token=UQohQwcvxKp3RcR-qr6RqXfd1DZOXTQfTYczVZNxBQAY5QGsFn-M6wNxrET2uQuFvVQQvHMKFpf2xPQSXJdrHVZC6SVgyxeAwRuifSQTJgi_3j79LfHt_9nRAbg7vNa0AZ89S2lNBT8RAvr3qNPmBAPu9HoSXyBv2gnjnno493lAdxiT5XgZ4SB16UUrTcJEEDlj0aZ7TBBUJ7NVvYN3_Bhtjipfq-wwHNcw9JWp30-dnlPKPHybnlGld-UAleIPsaos2bAWbRTPZeWGN-7gr84I1ztrwDSHcotHQdoZx-vzwOuJf3JUC-YDxEyiMJc7M9B-8BuPsjRUHJ6B9mzVwg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/518cba3871.mp4?token=UQohQwcvxKp3RcR-qr6RqXfd1DZOXTQfTYczVZNxBQAY5QGsFn-M6wNxrET2uQuFvVQQvHMKFpf2xPQSXJdrHVZC6SVgyxeAwRuifSQTJgi_3j79LfHt_9nRAbg7vNa0AZ89S2lNBT8RAvr3qNPmBAPu9HoSXyBv2gnjnno493lAdxiT5XgZ4SB16UUrTcJEEDlj0aZ7TBBUJ7NVvYN3_Bhtjipfq-wwHNcw9JWp30-dnlPKPHybnlGld-UAleIPsaos2bAWbRTPZeWGN-7gr84I1ztrwDSHcotHQdoZx-vzwOuJf3JUC-YDxEyiMJc7M9B-8BuPsjRUHJ6B9mzVwg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
رئیس جمهور ترامپ درباره ایران:
ما از نظر نظامی، پیروز شده‌ایم.
آنها مدتی پیش با من تماس گرفتند. آن‌ها واقعاً می‌خواهند یک توافق انجام دهند. اما من نمی‌دانم که آیا آن‌ها شایسته این توافق هستند یا خیر.
من مطمئن نیستم که آن‌ها به توافق عمل خواهند کرد. این مشکل اصلی است.
@News_Hut</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/news_hut/67622" target="_blank">📅 02:30 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67621">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4ba19bbdd9.mp4?token=R2sHnNSJCEfCIQWvRWrnxcu9wZXBBM4RKCbTEwEjC36w0N8TffvPHLJzuaj8TgXNiyUpJMwYgiwVI30q2dZtGE16lYis79GtZKcjnS-XzlxDkNkYvYLjviIrPf7IqgGhiBf-F1ROwGJae9TCS-zA_JmagrWJtHf56o1mc5syU2adLc0AGUOfVMBeIzmmTqvMg3diQjkrRPvyETQLqz-xdy3Mn4CSYq9J_Az3cCpPkYs2bOLFo4tNizdbF_cJ97uz-kvx6exFZbsIi7aGzzEU5bTO7grUoKwAkqeM73_ZSFPJMMFmcybeu81-SQiqAJXGnqJMHJy6SZod3VAxwgtzbw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4ba19bbdd9.mp4?token=R2sHnNSJCEfCIQWvRWrnxcu9wZXBBM4RKCbTEwEjC36w0N8TffvPHLJzuaj8TgXNiyUpJMwYgiwVI30q2dZtGE16lYis79GtZKcjnS-XzlxDkNkYvYLjviIrPf7IqgGhiBf-F1ROwGJae9TCS-zA_JmagrWJtHf56o1mc5syU2adLc0AGUOfVMBeIzmmTqvMg3diQjkrRPvyETQLqz-xdy3Mn4CSYq9J_Az3cCpPkYs2bOLFo4tNizdbF_cJ97uz-kvx6exFZbsIi7aGzzEU5bTO7grUoKwAkqeM73_ZSFPJMMFmcybeu81-SQiqAJXGnqJMHJy6SZod3VAxwgtzbw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
رئیس جمهور ترامپ درباره ایران:
ما به آنها ضربه بسیار سنگینی وارد کردیم، و من می‌گویم که ما به آنها 20 برابر ضربه وارد کردیم.
هر بار که آنها به ما ضربه می‌زنند، ما 20 برابر به آنها پاسخ خواهیم داد.
وقتی آنها حمله می‌کنند، ما با قدرت بسیار بیشتری پاسخ می‌دهیم.
@News_Hut</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/news_hut/67621" target="_blank">📅 02:29 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67620">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/db0d252421.mp4?token=cznnyZLYmE-2bM8pizCZEz04W7ZpWPLjaHxw7saRy7KTZ1jyNTRGEsY1D8u2YchJlPVOeimesD694mA7FCPiRjsLmpMMpdyWNCAID4iGnAgbp2jiSjqoY5s_diFKMb8zFTSA1OJW1Pj3G77Aw3umeQgYn_3yXCEvsQP5gasocHIeDlL5QHhueye6vvDiJNZ0lDTmtxr1P56fKQ0YOTGU11HgFh4TrqxGRMP-E6LcK6H-S8AwWBJo4cCVjIhg3fMyPKtpRaWiCgKtapMHg5FHkZzo3Q045fiku-NHGD3MNodIpIOftFqPwyaW7LpHdx0UyjrWpneEqeWsn1dOkHsYUw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/db0d252421.mp4?token=cznnyZLYmE-2bM8pizCZEz04W7ZpWPLjaHxw7saRy7KTZ1jyNTRGEsY1D8u2YchJlPVOeimesD694mA7FCPiRjsLmpMMpdyWNCAID4iGnAgbp2jiSjqoY5s_diFKMb8zFTSA1OJW1Pj3G77Aw3umeQgYn_3yXCEvsQP5gasocHIeDlL5QHhueye6vvDiJNZ0lDTmtxr1P56fKQ0YOTGU11HgFh4TrqxGRMP-E6LcK6H-S8AwWBJo4cCVjIhg3fMyPKtpRaWiCgKtapMHg5FHkZzo3Q045fiku-NHGD3MNodIpIOftFqPwyaW7LpHdx0UyjrWpneEqeWsn1dOkHsYUw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
ترامپ درباره ایران:
من در صدر فهرست(ترور) اولویت‌های آن‌ها قرار دارم، قبل از شما.
اما اگر من [مشکلی] پیدا کنم، شما هم [مشکلی] پیدا خواهید کرد. بنابراین، شاید روزی بخواهید شغل خود را تغییر دهید.
@News_Hut</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/news_hut/67620" target="_blank">📅 02:26 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67619">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">🚨
🚨
انفجار سمت آق قلا گزارش شده
@News_Hut</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/news_hut/67619" target="_blank">📅 02:22 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67618">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">🚨
🚨
🚨
چندین انفجار در گرگان
@News_Hut</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/news_hut/67618" target="_blank">📅 02:18 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67616">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c35f85df80.mp4?token=SzhejQl8Mcv-xGtUvYjwz24iDcsXMr7-Cd8l2LydYYS4uVwrgGsnZGzvfSRvOm5gTBrDkWTdL7CoQn_XxK2RHIsxYeeqRD3iVYsC7NuqeQZIDXFa7TbY_7K37ooy0GdgtRnlMbdU1Ouy8Bk8I-CQQCpE3XdkshGHFHGL7CAS19xQ-RsoSRvLOJlgaqqozTpYbHgvSuWfHGK9VWyDvw_R3MRPN8O0XLXasELv64jMVleZodCDj6LpIgGTsJGv1ATTb4ZyR_67pf-9jr8ut7m86OndnDwsqwWRseH80v4-4aP_08nmggFS4GQ0HIMCfVfJTBnzqRLIspWPLgE32JCvrw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c35f85df80.mp4?token=SzhejQl8Mcv-xGtUvYjwz24iDcsXMr7-Cd8l2LydYYS4uVwrgGsnZGzvfSRvOm5gTBrDkWTdL7CoQn_XxK2RHIsxYeeqRD3iVYsC7NuqeQZIDXFa7TbY_7K37ooy0GdgtRnlMbdU1Ouy8Bk8I-CQQCpE3XdkshGHFHGL7CAS19xQ-RsoSRvLOJlgaqqozTpYbHgvSuWfHGK9VWyDvw_R3MRPN8O0XLXasELv64jMVleZodCDj6LpIgGTsJGv1ATTb4ZyR_67pf-9jr8ut7m86OndnDwsqwWRseH80v4-4aP_08nmggFS4GQ0HIMCfVfJTBnzqRLIspWPLgE32JCvrw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تابوت نوه خامنه‌ای رو با سرعت دارن کجا میبرن؟!
🧐
@News_Hut</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/news_hut/67616" target="_blank">📅 02:01 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67615">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g0DTz1mRQH-_ZF3QcNaUPzPKPRTybhoa5jKovGU6haJ5EM50z_VhlHzJIf5kmiclsY3KGNzNtu4Yrd7LoFvbfcvW3YRT912g0BuZJZc-jvrra8AihadtsTMerF8W2yUiCV4dKn8KCb9e4IQEBnx8cyR6A-hY2gCVJ4K-5h0GF6NV92Hk4ia941ry31dRdMcfr27V1BOL47mNTCAhfTCuZeKzvTrYhDkxWE4oShpweRzHnTBRBT7r1Nw3gmxqS4Bj_9aWAzzLtnOENUv3ZXFUGArLc8Oj5Zx3Q_dO2-HDV_mv11yttIoZcwGM94XI_C-hnIosgI6sY9rGo_qLija78w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
نقاطی که امشب توسط آمریکایی ها هدف گرفت
@News_Hut</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/news_hut/67615" target="_blank">📅 01:37 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67614">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">🚨
🚨
سی‌ان‌ان:
آتش‌بس موقت با ایران متوقف شده است و وضعیت همچنان بسیار متغیر است. احتمال انجام حملات بیشتر بسیار بالااست.
@News_Hut</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/news_hut/67614" target="_blank">📅 01:33 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67612">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BcLoHwfiXdnhoT_0YBlBbjfdirce2X7LO3MyvpZFG6b4RFM1vmoDRs3HXCi21A7B6ZgRwDLkga8goMXF8SKWyK7QtIXuXr8grpiXtajXplVpyg_1FkPbc465WjnFnYpM4jWFFP6FGf9Oahtgv5q0F4Mn8EZhcBHfeQeRO55_EL9cQj5BOVoN3PX_sMMKsVTu9yCR4RmEPd-zVYn5-_-ajls9_F6nUug9eozmPUq8VZVwftipjOopQD3N-r9ouSLSu7YN4o74Z0HC5MY03so7eJ0d8AuhhFApR_KFfjgDz8MfXWKzH1H61R_FUwzZXp3GeT1Hu_ViVNGmL4Ayve8D7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e87cdc8ac4.mp4?token=lE1zZUvJhrMeRZMXVdJjQuLdVoLL5dJ_T02YhelxR__5szupH-ET14tj4Jclh66mMJmlf7AJdc2Q5lc6QJrIedQpB8kYi7w_wRaN_X0-DhTc7WvyCI7cQcsrfsrAlj3G6Lflo5n1Sml9WtLryyHaKj3QuKanyGaDjGgIRq5xjYDeAbPqDj8CwjgobxSZMGiFJC00kxgt84oIya6ZpbMBDyt8mY3qiIU3hBaeLkQweRAzewfInSEEwM6AQPs9N5gqv8xNrgD762E2ZgiT_WnpYqYe4Jfr5GfgsdXjMbYfBDM0hfeJase1JYRUFdlXGFAdlCVvY_AOsCq3--IAdvhlXQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e87cdc8ac4.mp4?token=lE1zZUvJhrMeRZMXVdJjQuLdVoLL5dJ_T02YhelxR__5szupH-ET14tj4Jclh66mMJmlf7AJdc2Q5lc6QJrIedQpB8kYi7w_wRaN_X0-DhTc7WvyCI7cQcsrfsrAlj3G6Lflo5n1Sml9WtLryyHaKj3QuKanyGaDjGgIRq5xjYDeAbPqDj8CwjgobxSZMGiFJC00kxgt84oIya6ZpbMBDyt8mY3qiIU3hBaeLkQweRAzewfInSEEwM6AQPs9N5gqv8xNrgD762E2ZgiT_WnpYqYe4Jfr5GfgsdXjMbYfBDM0hfeJase1JYRUFdlXGFAdlCVvY_AOsCq3--IAdvhlXQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
ویدیو ای منتسب
به
حملات آمریکا به ایرانشهر( سیستان بلوچستان)
@News_Hut</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/news_hut/67612" target="_blank">📅 01:30 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67611">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lyvQOaESy4VINNR_v5j-kfxg57gfVLkLLnaNXUlW0ecrwMka7WoohEwRbqcwLyhkORb3oK_FxD1BATxmSUguJa_RG1ydLz0K2RbK8oDLolrfjv9JCM_Amf_JMw-JSiuAzl-YEnLcKaPw4RV5HfQ2qFO6gsD1gwz5be0O8wfVCZaAEDEOqywudqHKJIdFBho5osP91064m2JVrHeiAbiUX49Cat7ehul5ScTwnGupix7u0wLrDJ0VN2SLSpcvVGkc7YTWGWUr3L8h_mlhI8LFDmQAFj5qgwUTf7ClS7Sv0J1h9_tF0MIf6YmdclH_PHx3sdC89B2pfCddkECKKtnjlQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇺🇸
ترامپ :
این یک انتقام برای بمباران دیروز کشتی ها توسط ایران است. اگر این اتفاق دوباره تکرار شود، اوضاع بسیار بدتر خواهد شد!
@News_Hut</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/news_hut/67611" target="_blank">📅 01:10 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67608">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NqoNhfh3XY2zxq1k2mjhlF0cvJbcCZa0trxhhRFJJCa8gY6TASv7NbdaH-fviopT-pFajoCNIVBZ6xlrOGKz6ivdmhUEokLzr5CVzaH_oQuu5T00ZLt593YWBc7pzhDIeSixz02wk0UbRGJaGcR-LfIEQwv8R3rkEbq5bllIInSXU8EWg8hC76DxOSzED4KrC6FeHG64sbCdgLMnLNKmgtYsOZUOTgroSqWH0V2BfhwTW582lYUb2a4l_l9J3dRk5mq5gyVOznzP6EMtq1ELMUdQEs73MEdvGCJHsABA6Zxzv80I3MZN4syLw9ryMTP3epHW1-YVKqTpuJjjmgUcyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NsKQIUIAqcD2DEZgAz9mURBqTol5Xz0h-fAY3UPXaxewfaYo5xT-wT5_LF4f-OKyWKWhskr2Yboq7qxObgoFC8uWus9wsWdK1g-eBuspIZNah_cK9JIjxiUHwbHq1yuAMmB40Gcw6khgrZ49VboXWN8u0Lga-RjJH5MUf906fB2RdgGT65vUGF8FBtLsgB4VO-EkOzfqfBA9rxjZJA2LloFc6MP79loN0arqMvLKhpjvfUQ1fH62Sj-8DTRI-mlQA_v8nXJp_YlAiGphmwOafyL6LsAQIU_MEgcxQJ0CnwonghLx1hcWO8A_vb5WmUV9HLYyj9HdKrGFYOZiZjXS6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/a-xUowJeUfUhWUH05-Q99PPgmMMjlPv7dLm0YwYN4DdBPPct6h5Qb8Iqg5tiXpaP4MtNOTR_0kBKp6QEVlLhH8ftMr4XFrn_fjF2Ow5MNz9SdKv2IEhTmBmmdYnwGVXSTCy3xZl7ZC-8d3aEUbXnoOKEmpRHPQe5mwulYMJjuQ40kI74uU1nXUmddfT2WioW_PKIGHG40mWfM4qqx745K2dbvC-1NB9xY4ein38z8s9Thr5k1IViZQglR5aVrXZqmwQj6Fm1bOdjt_giJyf6WHErJO0v0EeihZfVSxvK-TVOAwaDVT9B4WbJM7n-9qbmdWsXqdnyo3NFuCgXtCjiZA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
🇺🇸
ترامپ تصاویر حمله به جنوب ایران رو در تروث سوشال منتشر کرد
@News_Hut</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/news_hut/67608" target="_blank">📅 01:08 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67607">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">دلیلِ این چص‌حمله هارو متوجه نمی‌شم واقعا، آخه کسی که زدین رهبرشونو که از نظر اونا جانشین امام زمان بود رو کشتین، اتفاقی افتاد مگه که الان بخواین با زدن توالتای پادگانای سپاه اتفاقی بیفته؟
صرفا این حملات شرایط اقتصادی رو سخت‌تر می‌کنه همونطور که امروز دلار ۱۸۰ تومنی رو دیدیم، خود ترامپ هم می‌دونه تنها راه حمله زمینیه و اولین نقطه هم خارک ولی جرئتش...؟!
#hjAly‌</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/news_hut/67607" target="_blank">📅 01:06 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67605">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9864e05e49.mp4?token=arkpnGHhpmPcHY0MRKRvjKSr7JGg7jk3dlzhOmkss7g1czXq2Q24B9HnQC8VTEgnfnWZrG3qsZetfpAT2McR0K4GlvnG29ueeE4Q42FCtonJxR5S0MDB3sSZsxkJ72H2AZREyhIwCytpcCPCv7I4rSUtjaysED_H8tPfwrb6j-SE6_yxFEae1h_Pq8CwF_Vdz2oaxDqCWfkcYiRJh7TLacF1IdscFdOfyOhdeErHX6ARBTJuROLKHyxJZj5F9RegBYNKts6bgfLlzgNGPM389xnj1UknbNjO7mv14pEQS250aEfYUGUN0JNk4cIQAmTWrHWfccnQaU9e6ltxIH1CRw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9864e05e49.mp4?token=arkpnGHhpmPcHY0MRKRvjKSr7JGg7jk3dlzhOmkss7g1czXq2Q24B9HnQC8VTEgnfnWZrG3qsZetfpAT2McR0K4GlvnG29ueeE4Q42FCtonJxR5S0MDB3sSZsxkJ72H2AZREyhIwCytpcCPCv7I4rSUtjaysED_H8tPfwrb6j-SE6_yxFEae1h_Pq8CwF_Vdz2oaxDqCWfkcYiRJh7TLacF1IdscFdOfyOhdeErHX6ARBTJuROLKHyxJZj5F9RegBYNKts6bgfLlzgNGPM389xnj1UknbNjO7mv14pEQS250aEfYUGUN0JNk4cIQAmTWrHWfccnQaU9e6ltxIH1CRw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
ویدئوهایی از لحظه حمله آمریکا به برج کنترل دریایی اسکله شهید کلانتری چابهار :
@News_Hut</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/news_hut/67605" target="_blank">📅 01:04 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67604">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">🚨
🚨
انفجار های مجدد در جزیره بوموسی
@News_Hut</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/news_hut/67604" target="_blank">📅 01:01 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67603">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">ماشالا ترامپِ شیردلِ مادرجنده‌ی املاکی
😊
#hjAly‌</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/news_hut/67603" target="_blank">📅 00:58 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67602">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">🚨
🚨
🚨
انفجار در بندر کنگان
@News_Hut</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/news_hut/67602" target="_blank">📅 00:58 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67601">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EGsCi7EaTgb5c_O6iy90qEyzvpg1zRmiyqLQPcAFm6MufUCJx7oEnZpA8BZOVhajiFD639doyUykKY6BWXd8Raht3s_DZkShlO76v-zIjQuW_Lf6XuLy7NalMjyhqgJ3qu7lz5wrQmWWr6wFL2bdmq_8vpLQ2eDp6ClSev3nlDZ_F0AQ-eEjDDtsPBBKwYkAJ2AKPsFmwBuTUpNfZQYd6C5slDbYEL3g7EPGIjFTJ4n8W4ojYbxfKGXYjqJsDsZSxpaY2SfcJS6fBQYP9dWNA2DsnvQ9xaKuj97SuqyFtW0p3qmp0V26l49Rvwm7A2EdWMB34sQdDEJQcF-suY8cYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇺🇸
یازده فروند سوخت رسان نیروی دریایی آمریکا بر فراز خاورمیانه
@News_Hut</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/news_hut/67601" target="_blank">📅 00:57 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67600">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eOxvBRYZR7bK8fc2Lw33iTSeF3X8l6PGXVs5hp69hs0lLzrcAgftj4P9wBpZoLjrJjtTSE1FkM0zS8d85ZlyuRDws21GLidwsc-0-QGxVFtad9dZVeYxtMRQ7QUsHJk169qBIRj2VaplprlCu60YDLZZyHSeeFl5LsybejY3o0dO3Vt1fhIm9ozDIDFuy5xr4luEkSHqbAMt0lzs7Y7nepOCc5LUneOBuFX9YKgWT5x8Y9PTSbdrGH0pKlzZqd0NolfeVobCeHo2A1gFty7gzuHQ5rLS6zVZLRJLkD3y3SQhMhB1ViHYo75aiRNGeQhoSgZqrtwvrRTzSHQOJDfM7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
وضعیت شهباز شریف بعد از حملات آمریکا:
@News_Hut</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/news_hut/67600" target="_blank">📅 00:53 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67599">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">🚨
🚨
صداوسیما :
نیروی هوایی آمریکا در حملات به چابهار، اسکله‌های «شهید بهشتی» و «کلانتری» رو به همراه برج کنترل ترافیک دریایی این بندر هدف قرار داده.
@News_Hut</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/news_hut/67599" target="_blank">📅 00:52 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67597">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IawDGdJzpBxojr12FRiHriaYkSeDgrMimDso8GohogXXXwB333ppJHh9HLL0Z6lNJ-QE7swYBzuLcZuqRYeorEuOxyF6DjP3sUJryOdqfq6UiKxMdOcWDvTls5UN_1Wg3ECeP8DIhPn9babZPpxKRgM0elq4YVUo210FJ6UqTCDyIrYEJ0d64zKsv0he3NE6f208CqLanaQLYvpuqGg9gNRwUNmQBTJtrhPMgS4A3-1FvBsXL9WvdIOgAtIHuvAWBu5sBGWugdjD48OFtI2VasiziNnDaS-3fSGz_N8zTcTQ1KdGY8fBD9vOviPU2eJQLGkIewPtjeoI1P9u4UvnfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Jk9ahY0agedE-bRq8x3dEkGtLuzn_aHuXV9o7fTABOgfXlZv-M44EC2efaSo8hrBVWmFRK7CpA8TvbVvE-gpJDjC53QE8VxOiw_fH_XB--IQJKwtm7tQOsZSiOKRUHNvkY-eRsqkti0coGrDNoq5SKe1NfOSPf-0CG0fnmTjQj_0Z-lme5uYfAHCwS767JqH3axwqXRLhxSsQcxq9eMIcalRLqEv18KRM7SzXIni2BtNBegu9iiSQJkSuJtOs289_px9hZyHXIxSCO6z2T_vBLxxTp9jYca-dG56BwQ2T2Rw0i5xzGbVwbt4mQNSWOQ6mYeftara6NNN6uj5nibG_g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
برج دریایی اسکله شهید بهشتی چابهار
@News_Hut</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/news_hut/67597" target="_blank">📅 00:51 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67596">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">🚨
🇮🇷
محسن رضایی مشاور رهبر:
دشمن متجاوز و همدستانش به شدت تنبیه خواهند شد.
@News_Hut</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/news_hut/67596" target="_blank">📅 00:48 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67595">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">🚨
🚨
دقایقی پیش مردم در چغادک استان بوشهر ۳ انفجار نسبتا شدید را حس کردند.
@News_Hut</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/news_hut/67595" target="_blank">📅 00:47 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67594">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">🚨
🚨
چندین انفجاردر بندرلنگه
@News_Hut</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/news_hut/67594" target="_blank">📅 00:41 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67593">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">🚨
🚨
فعلا تمرکز حملات مربوط به خط ساحلی جنوب کشور بوده
@News_Hut</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/news_hut/67593" target="_blank">📅 00:39 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67592">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/df60497304.mp4?token=gjgLwsC9N8mLYGb1Yc1UjDvOEyRl3P8S_Hc0b5gNC4VI0EOXDfS6aCxZMabyawgj4bvihPzumVffTTEu4qPqcjjtuAXb_sR8doa6Qi77Z9MkXKeQTXD7PvRpl6SrHM1aQyY8QAD_ON-Zexedc5_8vog2WM8UpMsufBXAvaiWO7OAaOOgtkbV49ZEGOHwwBptXazNVNP1s3RkijE53OoQzHFyzGekpib58HbQYo3GTHt81Wvy6dS8XE2RkU7WZ7cYrGTjbBnHd5RycoFy8wCcOeyGqFkgdMwI9wGJEXF1m0G_G_de308yRECd0t3WrWucaxNo9vpc-lid7-nMKyDdjQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/df60497304.mp4?token=gjgLwsC9N8mLYGb1Yc1UjDvOEyRl3P8S_Hc0b5gNC4VI0EOXDfS6aCxZMabyawgj4bvihPzumVffTTEu4qPqcjjtuAXb_sR8doa6Qi77Z9MkXKeQTXD7PvRpl6SrHM1aQyY8QAD_ON-Zexedc5_8vog2WM8UpMsufBXAvaiWO7OAaOOgtkbV49ZEGOHwwBptXazNVNP1s3RkijE53OoQzHFyzGekpib58HbQYo3GTHt81Wvy6dS8XE2RkU7WZ7cYrGTjbBnHd5RycoFy8wCcOeyGqFkgdMwI9wGJEXF1m0G_G_de308yRECd0t3WrWucaxNo9vpc-lid7-nMKyDdjQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
بوشهر
@News_Hut</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/news_hut/67592" target="_blank">📅 00:35 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67591">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">🚨
🚨
چندین انفجار شدید در جاسک
@News_Hut</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/news_hut/67591" target="_blank">📅 00:31 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67588">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XtAL8YzSyNh6GO__6PAuK_us5R4yu8_NmWn1HcWapmuVEwV--cmvBplYOmZ9SEkOvIlDWlIDrByoZ9YPf9830rMjntcHOIkPPMO_SOm7EOCppdTNlK4zewUmf10s3zV35fbIQgdGCJBV6SRN8KwpmYcQQT7qzI4vYAYFWd40BjZ5mKfiF7wMi-_bp2AWr-lK2A_xLkI-Zm0u0MySxPsLwF3hsyTCE8CWaV3XthuvnntNwucW0-NXV_gp8bDkqFobQlCQfRsCjTITDTRvFQC38TOz90NwZwDUeLgnmQX47uqZyRSihLgHVrguz3vqUkSV_PDD73KPw2i_kQBI9djbXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6afb0f1898.mp4?token=f7M34OA6_2VH_mhqp2JzdhnSapgNVxsqSTwYgoLlxW5H9W0XKa2e5GpMJ9LRu4_VcTsDMm8v9h4T2fJa2fPUfjBChwa9CSjS4B2HF8GAW6yqtpOqy5zmfT2JIKOUCM4U39QwfNGRRZH6MteAwbLAjppBIWgCUQgLw1nS8hLmtTlFS-R69ojagmbNpLVU38pCyDOFRNDMGQKd8SXz1f8LpR3tzAiLLfNUpxCA__Q3ZKgXiiTN6vEhIsM8bWMjtH_0bNe43KxzNNZU54gbZSMB7I3BOb4yB6yVmVHsnjsHvgqUFq2eMxCZM0Ljil4F2sFSuVvj6C_4E3WHKBUDKAwAjA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6afb0f1898.mp4?token=f7M34OA6_2VH_mhqp2JzdhnSapgNVxsqSTwYgoLlxW5H9W0XKa2e5GpMJ9LRu4_VcTsDMm8v9h4T2fJa2fPUfjBChwa9CSjS4B2HF8GAW6yqtpOqy5zmfT2JIKOUCM4U39QwfNGRRZH6MteAwbLAjppBIWgCUQgLw1nS8hLmtTlFS-R69ojagmbNpLVU38pCyDOFRNDMGQKd8SXz1f8LpR3tzAiLLfNUpxCA__Q3ZKgXiiTN6vEhIsM8bWMjtH_0bNe43KxzNNZU54gbZSMB7I3BOb4yB6yVmVHsnjsHvgqUFq2eMxCZM0Ljil4F2sFSuVvj6C_4E3WHKBUDKAwAjA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
ویدیو منتسب به بوشهر
@News_Hut</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/news_hut/67588" target="_blank">📅 00:30 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67587">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ac1596adc1.mp4?token=nHVcnMMOInAKl7Rdfu1NLU9a5kj2OLaczZtRp1gX29F_uwKC8snrwXBL9uuhwDKMcDLgVXTzy07q190yKY_N8uYUdlkXEciYeM2nB7TJQ3Vqv95JbPiScbowIZPKnvRSAj36iwfZOjN_U7rdrBsovH3-KYLpE-2JDzqsIQABOZCQ9fOr5fuCk-6RcrXatJJVnNFCoTBnLQjDgsMBj3xGdfEfDR32FBM_NRyImFaYeiq1A8Jgta8fvwo-Ow5kn6AzjvaIptvPZLtZh9f_8LipFdaj1qfce4h3hFbpfEzHJfYpl_f6vS8Dx3xTKT2fM3urq--QAS2u4dbeKYuagOmCRQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ac1596adc1.mp4?token=nHVcnMMOInAKl7Rdfu1NLU9a5kj2OLaczZtRp1gX29F_uwKC8snrwXBL9uuhwDKMcDLgVXTzy07q190yKY_N8uYUdlkXEciYeM2nB7TJQ3Vqv95JbPiScbowIZPKnvRSAj36iwfZOjN_U7rdrBsovH3-KYLpE-2JDzqsIQABOZCQ9fOr5fuCk-6RcrXatJJVnNFCoTBnLQjDgsMBj3xGdfEfDR32FBM_NRyImFaYeiq1A8Jgta8fvwo-Ow5kn6AzjvaIptvPZLtZh9f_8LipFdaj1qfce4h3hFbpfEzHJfYpl_f6vS8Dx3xTKT2fM3urq--QAS2u4dbeKYuagOmCRQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
❌
لحظه انفجار در چابهار
@News_Hut</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/news_hut/67587" target="_blank">📅 00:28 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67586">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">🚨
🚨
دو انفجار در جزیره ابوموسی
@News_Hut</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/news_hut/67586" target="_blank">📅 00:25 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67585">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f9f9c6b6a4.mp4?token=jq_hQzKWtBM903o1LyDhm1svbY9iEo7C8gSIGjZdZ2vV8DNn_XF18P1AIXW61Jce4XJZClmTuZNYp0wAxM8YImTeUZtMeMl-sIZvzywGwNILXIzQIy-Bi98HSY2MkoVy4poXaZSnl1vnLvba6BILSjhf_vyHtN7tE8UBOaayQW-uOkaVtjuRoIJmp5wEqe372gozxD5C0HScbS_5mqTB_1fIYeFPfYRk1rTfGAjyXZcYHRV42t6h5Bvyokg47M3h3uR7spnTRpl-SQ3qGBj_Di1vvWbo0zvtMISZYBqescTYHhIjeI3y6196KpJ1vY7GeXVD507eeW1uZrHOOzlIXw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f9f9c6b6a4.mp4?token=jq_hQzKWtBM903o1LyDhm1svbY9iEo7C8gSIGjZdZ2vV8DNn_XF18P1AIXW61Jce4XJZClmTuZNYp0wAxM8YImTeUZtMeMl-sIZvzywGwNILXIzQIy-Bi98HSY2MkoVy4poXaZSnl1vnLvba6BILSjhf_vyHtN7tE8UBOaayQW-uOkaVtjuRoIJmp5wEqe372gozxD5C0HScbS_5mqTB_1fIYeFPfYRk1rTfGAjyXZcYHRV42t6h5Bvyokg47M3h3uR7spnTRpl-SQ3qGBj_Di1vvWbo0zvtMISZYBqescTYHhIjeI3y6196KpJ1vY7GeXVD507eeW1uZrHOOzlIXw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
هم اکنون؛ آنتن زنده شبکه خبر
رئیس کمیسیون امنیت ملی مجلس: آمریکایی‌ها بدانند پاسخ کوبنده‌ای به آنها خواهیم داد و امنیت را در  هر جای دنیا باشند از آنها سلب خواهیم کرد
@News_Hut</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/news_hut/67585" target="_blank">📅 00:23 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67584">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/36b350a9ac.mp4?token=WZUIcFVPSfQPUwIh9Zqfp1TIfxIFW_ecCbntju-tL6PbWWm_WflCwEz6xYoYx-CbxSjNcee1jChZDO1DpKnk4-2dOn6sBP-ZLDYpifMDg1SIKjVULnMv7lJ0ulUIJJ0eOWg16qU7o1hyZbWPvAu-QzKyzm4HsBSoGAoOgYHButQGDaC-lKMrnoT-ToZLbOuAUl8NAhcup7AQ72sCzPlTgrEKzfawpupA6oNn1xDbfPBpcMymfFIb5LYHj1xHL0ek50PjGeoGjwtz_MSKNdYwTQtVHJHWpWAiw4DC4UHZydO21nm3BU5gY6mcI0uncWBE6bRzYZLZexeSTOHt-d5gBw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/36b350a9ac.mp4?token=WZUIcFVPSfQPUwIh9Zqfp1TIfxIFW_ecCbntju-tL6PbWWm_WflCwEz6xYoYx-CbxSjNcee1jChZDO1DpKnk4-2dOn6sBP-ZLDYpifMDg1SIKjVULnMv7lJ0ulUIJJ0eOWg16qU7o1hyZbWPvAu-QzKyzm4HsBSoGAoOgYHButQGDaC-lKMrnoT-ToZLbOuAUl8NAhcup7AQ72sCzPlTgrEKzfawpupA6oNn1xDbfPBpcMymfFIb5LYHj1xHL0ek50PjGeoGjwtz_MSKNdYwTQtVHJHWpWAiw4DC4UHZydO21nm3BU5gY6mcI0uncWBE6bRzYZLZexeSTOHt-d5gBw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
لحظه انفجار در چابهار
@News_Hut</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/news_hut/67584" target="_blank">📅 00:20 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67583">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b02d221609.mp4?token=QJ2NMPlzHiQ-unUspxLkhjDdTzvPcR1n4SFAvlTXMqCN4WLQLVRx13hfaCHSPEMim8rDrSbi7pNROvXifyeIzIIiFPeuZ65wCDpfUT8Msx5B-vzUgi0rxv1DGecrjqdlu0YRA6XNvT6o6CpEhmHBVq-Se_Q0pGei5039Ru-_nn-sBGYMSmexsWSyazNHpzp3G53l0TUCEAbvZU9UZwDglUyfeQOR_e4jdogO8AOJilHfB2HzijEQeKJwiNHU3Dfowovro9sk6HjqhlkXgU6ivWS56Ev1vsiPM7PPPdUHrNapJmhNUVH4b-xtDVA8iFPTFiv3pYMluO4gm6Lj6oVoAg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b02d221609.mp4?token=QJ2NMPlzHiQ-unUspxLkhjDdTzvPcR1n4SFAvlTXMqCN4WLQLVRx13hfaCHSPEMim8rDrSbi7pNROvXifyeIzIIiFPeuZ65wCDpfUT8Msx5B-vzUgi0rxv1DGecrjqdlu0YRA6XNvT6o6CpEhmHBVq-Se_Q0pGei5039Ru-_nn-sBGYMSmexsWSyazNHpzp3G53l0TUCEAbvZU9UZwDglUyfeQOR_e4jdogO8AOJilHfB2HzijEQeKJwiNHU3Dfowovro9sk6HjqhlkXgU6ivWS56Ev1vsiPM7PPPdUHrNapJmhNUVH4b-xtDVA8iFPTFiv3pYMluO4gm6Lj6oVoAg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
منتسب به بوشهر
@News_Hut</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/news_hut/67583" target="_blank">📅 00:17 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67582">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">🚨
🚨
نور نیوز  :
به زودی حملات ایران شروع میشود.
@News_Hut</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/news_hut/67582" target="_blank">📅 00:16 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67581">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5c578ded4b.mp4?token=AYgwgbQoBGKGWBP-JPoyEhnDWYJrMOkcTF1RuSsu7yt0PTTSJtbMrKIJ2nhAKnyidy2K0oDYP1dwGcQOdsc2PBZgJdcIaCQUnvyavnQu-NAcF-IskLYxvAlhqIojiUTs5bMxY29R6K3mtQvc7_KZcQJ58pbV-zbT6LYAS4iPeJob05G0D5etSZGr3eT_Tet1AbX86oYobcDyMr4fYekHZGkz1ytmNm2DiAb3v4dzOMy5ERURqcblACai8NJOLhowoIiqwi8tayAnR77rxHsbXZ45fSk9b0F4_C7nMulq3uzfpjUYVg6PFcdUSUm3LUZfWeQD6YaLKSnG-2u_pG5fYA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5c578ded4b.mp4?token=AYgwgbQoBGKGWBP-JPoyEhnDWYJrMOkcTF1RuSsu7yt0PTTSJtbMrKIJ2nhAKnyidy2K0oDYP1dwGcQOdsc2PBZgJdcIaCQUnvyavnQu-NAcF-IskLYxvAlhqIojiUTs5bMxY29R6K3mtQvc7_KZcQJ58pbV-zbT6LYAS4iPeJob05G0D5etSZGr3eT_Tet1AbX86oYobcDyMr4fYekHZGkz1ytmNm2DiAb3v4dzOMy5ERURqcblACai8NJOLhowoIiqwi8tayAnR77rxHsbXZ45fSk9b0F4_C7nMulq3uzfpjUYVg6PFcdUSUm3LUZfWeQD6YaLKSnG-2u_pG5fYA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
ریشهر بوشهر دقایقی پیش
@News_Hut</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/news_hut/67581" target="_blank">📅 00:11 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67580">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fce96b4303.mp4?token=Mrr-c_CLUJchhtDvEcoZzf8kI5JAeZd3duT33I3lIrR-xNBLcyux8DDHMt4CkK3WPCiU8o3_ttyl6h6IsH5e7fXr41Y4wx6-kQgRIRpWoTgL9eTQfdlr4u5_ZMA49uMv1SchLuaF8UtGo4WshpdAjm20EnCQTyPHfpI8xGwJz63VnyI8N152Jbo5fiHG0HtHc-5a_0emoiRiOQt-9VJUz4S9k4XpaGzmg9-LOnSVE29o9AmL2xXNBF4gXBg2SM86ADehAyROLTQjQKqQ9Weo0weNQK4EMi2OABoeDVN7aV4Vm8l6BL5JrrIB1h6yvWGa8oRtJL5HRj2SFm9afLBhRQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fce96b4303.mp4?token=Mrr-c_CLUJchhtDvEcoZzf8kI5JAeZd3duT33I3lIrR-xNBLcyux8DDHMt4CkK3WPCiU8o3_ttyl6h6IsH5e7fXr41Y4wx6-kQgRIRpWoTgL9eTQfdlr4u5_ZMA49uMv1SchLuaF8UtGo4WshpdAjm20EnCQTyPHfpI8xGwJz63VnyI8N152Jbo5fiHG0HtHc-5a_0emoiRiOQt-9VJUz4S9k4XpaGzmg9-LOnSVE29o9AmL2xXNBF4gXBg2SM86ADehAyROLTQjQKqQ9Weo0weNQK4EMi2OABoeDVN7aV4Vm8l6BL5JrrIB1h6yvWGa8oRtJL5HRj2SFm9afLBhRQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
لحظاتی از حملات آمریکایی به شهر چابهار، ایران.
@News_Hut</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/news_hut/67580" target="_blank">📅 00:09 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67578">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/D53LIkMV6X48CMB1B5G4ZjjKvTVW225-e5Bis8qFbJwj_7LlsYrvMvW6GY1yU8VIAUmG8e1XWdLfEKDLEy5VHqQek8aSd3MUsquEyF4ohNyzd5OKuINHdqoC4q4mjGCv_VPdpTZ8ZsVacBBMP0qN7hFmbzGkpLJDlpyKI_5kHTXQa1R2yB7w0qcHvr8rtq3r2BuTKUg9XarEfKQ6s0K8CM6EDCZyT-ihWBw6C9iPXlUpupqxBRk0M7FOfO7-4YrAUzK2n7WSJiF5muaATzSnUiOPAFjVbmXUXilapV2VgJjUIzEiDG1GjzmqmZrTvv8XlBQbBcupGKpzuKy9wdncog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IaSoZAIJ5SVw5yxtQE56Tvg3PdWHQHGCJOHpYlQz9iK2LFN5su9hMHtdemq9pokNBQwNJzg-7f8qewQzkFMtvtR0JJb-EOiCPE9DIjXxbVbvcpmxhxy0uP4_daS_uKm_k4Anw1ttSh7GU5LKmgLPgYEZZs2t_ytbUNREqqmUDVsWZcuzybSg7Q6Cd5QPAOT5yU1eGl5y7YcQj9CHgfzN2CgfdQ1MpjuS_x1awxDifwPkhT7ylrO_YRZ7g4AdSQVDFC7CQc87JxPT-tRXV5bjXs7rHRerMkZLOYxYWRny03EJavg1UIp3I9iASiaEWTbzkgY062fZ5OYrW9ie7kCzGQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
🚨
تصاویر منتسب به نیروگاه برق پایگاه نداسا در چابهار
@News_Hut</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/news_hut/67578" target="_blank">📅 00:06 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67577">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/56e60a602e.mp4?token=bKnoEdxX_SXn3NWvzaBr2Gb5gdIT62lad3lq_Kp-N_n0I9Qmg7ExP62A1yHGMx3ZLr-H-ZBpc5Kq6TKPaQN-oD4RoYZYABONs3qx_76ZNbg6HuJlW7bcicLhmxK2MTLfRhMYa5nA6YQV8xtG6PZI6dIdPQlhWcRQQeSHO4t4CIyeURJapgU5fmCINU8szLnq_GMtw4aPcyHdpQZTcsl-cCUCnRUEoVSGyEKnNa9exGdn_dw7NKdFkUMoiBjH7OZoJAA8WPnTlkDwLctcXG-Ycw9yPMiPb4Za6rysAjPuJoes7d4ooXhYBBzqdYQnbUqWhi8Ke9J4NwnJi6yIBmXycw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/56e60a602e.mp4?token=bKnoEdxX_SXn3NWvzaBr2Gb5gdIT62lad3lq_Kp-N_n0I9Qmg7ExP62A1yHGMx3ZLr-H-ZBpc5Kq6TKPaQN-oD4RoYZYABONs3qx_76ZNbg6HuJlW7bcicLhmxK2MTLfRhMYa5nA6YQV8xtG6PZI6dIdPQlhWcRQQeSHO4t4CIyeURJapgU5fmCINU8szLnq_GMtw4aPcyHdpQZTcsl-cCUCnRUEoVSGyEKnNa9exGdn_dw7NKdFkUMoiBjH7OZoJAA8WPnTlkDwLctcXG-Ycw9yPMiPb4Za6rysAjPuJoes7d4ooXhYBBzqdYQnbUqWhi8Ke9J4NwnJi6yIBmXycw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
آتش سوزی در بوشهر
@News_Hut</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/news_hut/67577" target="_blank">📅 00:05 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67576">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">🚨
🚨
گزارش‌های اولیه حاکی از آن است که هدف آن‌ها نیروگاه‌ها است. قطعی برق در چابهار گزارش شده است.
هنوز تایید رسمی نشده.
@News_Hut</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/news_hut/67576" target="_blank">📅 00:04 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67575">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">🚨
🚨
انفجار های پی در پی در بوشهر و کیش.
@News_Hut</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/news_hut/67575" target="_blank">📅 00:00 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67574">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">🚨
🚨
آکسیوس به نقل از یک مسئول آمریکایی:
حملات به ایران، رادارهای نظامی، پایگاه‌های موشک‌های ضدکشتی و سامانه‌های دفاع هوایی را هدف قرار داد.
@News_Hut</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/news_hut/67574" target="_blank">📅 23:58 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67573">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">🚨
🚨
❌
گزارش‌های اولیه حاکی از آن است که یک پالایشگاه در جزیره لاوان مورد هدف قرار گرفته است.
@News_Hut</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/news_hut/67573" target="_blank">📅 23:56 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67572">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qTNdqD7GYspw_kKzfYF5dnHoHed9HQv_zQciyIJQBx86651kSh08x23ZmM4feeK59qIgqa61YH4es-b8v5eVD6wvmbPIEqiS7-WcR9q4m1Vh6HK_XWpQ9yqYeetywdYp2rs6Lv9L-F0hsPuW7Bm22tVkRU6nXzgRK1KUqNkKaBjF2eT5yZHOVxusG73U5VCFb_AXBGNS_61jZ6C-TcgMG0aY7m2JJfVhbJY9If1IwjOOuFzXjI6hzPBaEkd4VNP__rpOvtRAJ_jUZC55mEZl3naLnoPMUwyTUPNQ7PMAISEOs1e8gM82oh3Y6QamQvk5lwC-q-Wq6MsmzL0guWg-rQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
حملات آمریکا به چابهار
@News_Hut</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/news_hut/67572" target="_blank">📅 23:55 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67571">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">🚨
🚨
🚨
انفجارها در بوشهر و جزیره خارک
@News_Hut</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/news_hut/67571" target="_blank">📅 23:54 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67570">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">🚨
🚨
🚨
چندین انفجار در چابهار
@News_Hut</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/news_hut/67570" target="_blank">📅 23:52 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67569">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B880f0Wi3vHOZIJ89BR5Rb1AMZqfVi1z0cOxem2fVnBtNKa2dxMspcx8cKYay0Kn-LCbrqZgyzAzjPsjfzBKgM5Vszxjummdc_7sVdu2Bb-QIcj1dEkEbmpgqd25u87WocL3HqlhR9wTlCpQCLzquKw11RP1Fp5AYGCg6pLIpOR9IErlB0Ir-AxlajTRF_Wszp6Mr56-Pc7g-2XmpZDFqdWnvIMEWX1geQwdKEHBE8xOrJAPZsDOfQ7Hb89rRNhe77wyRGfNmMSN9sOCDi7NI4W-BKc89hDtqI4FCbNowNjufUWuT8wlPQH69Z-rvKJQjL56rISECSYzToAvnFzVXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
فرماندهی مرکزی ایالات متحده:
به دستور فرمانده کل نیروهای مسلح، نیروهای فرماندهی مرکزی ایالات متحده، عملیات‌های بیشتری را علیه ایران آغاز کرده‌اند تا توانایی این کشور در تهدید آزادی کشتیرانی در تنگه هرمز را بیشتر تضعیف کنند.
ایالات متحده، ایران را مسئول اقدامات تهاجمی اخیر و غیرموجه علیه کشتی‌های تجاری و خدمه غیرنظامی که به صورت آزادانه در یک آبراه بین‌المللی حیاتی تردد می‌کنند، می‌داند.
@News_Hut</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/news_hut/67569" target="_blank">📅 23:50 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67568">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">🚨
🚨
🚨
صدای چند انفجار شدید در بندرعباس
@News_Hut</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/news_hut/67568" target="_blank">📅 23:47 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67567">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">🚨
🚨
آکسیوس به نقل از یک مقام آمریکایی:
ارتش آمریکا در حال انجام حملاتی علیه اهداف نظامی ایران در تنگه هرمز است.
@News_Hut</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/news_hut/67567" target="_blank">📅 23:45 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67566">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">🚨
🚨
پادگان ارتش در کنارک توسط آمریکا هدف قرار گرفت
@News_Hut</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/news_hut/67566" target="_blank">📅 23:42 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67565">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">🚨
🚨
دو انفجار در جزیره لاوان
@News_Hut</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/news_hut/67565" target="_blank">📅 23:42 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67564">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d1d5e85683.mp4?token=h749GJaa13FLyduTWAEtxdH-heqC2gcnEIBpHQ7zsSOcGeKARCKkqvTfYta2E7r-gngcMEcdiXM9Va49Ww_FnVNmQels4-fbIphcsDk8hdcO6pGRZLoOKCUPV4dzlKH8d8nkeVaYt1QP9zhktaNtt8exhwNCaYURjDmahtMQTKVtJZ_Omh0EYAno4_BNEnQs5QDfteLA-6zlxhEW7ImEmw38u7pKwL7yNB7uJJawAiBMIqzshs9B1CXrBK-HWytfEQfPYQqNkY9FQDMXSXn7FE7Wa01rtQTo8IU9m_FWlN-vKCL8NyPUzsYsjQ_JEfqfq6mc3dXV3wmCIHeS1BjH5w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d1d5e85683.mp4?token=h749GJaa13FLyduTWAEtxdH-heqC2gcnEIBpHQ7zsSOcGeKARCKkqvTfYta2E7r-gngcMEcdiXM9Va49Ww_FnVNmQels4-fbIphcsDk8hdcO6pGRZLoOKCUPV4dzlKH8d8nkeVaYt1QP9zhktaNtt8exhwNCaYURjDmahtMQTKVtJZ_Omh0EYAno4_BNEnQs5QDfteLA-6zlxhEW7ImEmw38u7pKwL7yNB7uJJawAiBMIqzshs9B1CXrBK-HWytfEQfPYQqNkY9FQDMXSXn7FE7Wa01rtQTo8IU9m_FWlN-vKCL8NyPUzsYsjQ_JEfqfq6mc3dXV3wmCIHeS1BjH5w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
حملات سنگین آمریکا به پایگاه سپاه در چابهار
@News_Hut</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/news_hut/67564" target="_blank">📅 23:41 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67563">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">🚨
🚨
🚨
حملات آمریکا به بندر کنارک در چابهار
@News_Hut</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/news_hut/67563" target="_blank">📅 23:38 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67562">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">🚨
🚨
🚨
گزارش صدای چند انفجار سنگین در بندر چابهار
به پایگاه امام علی در چابهار حمله شد
@News_Hut</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/news_hut/67562" target="_blank">📅 23:33 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67561">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">🚨
🚨
خبرگزاری آکسیوس :
ارتش آمریکا امشب حملات بسیار سنگین تری رو به ایران انجام خواهد داد
@News_Hut</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/news_hut/67561" target="_blank">📅 23:31 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67559">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EBVySozG2o-kBhHGdxPrsWjvT20AkgQs8a6F4oWvyuUaYFkxN5x6geW3825Gg10Gz7lMnbn_RVXJHUWTfWgmh3lK3AmETbjHHZ_sxMEbijsKkdl34pY8xpy0xYoxrqKRUGOMAWvKqfLHC9EqDtDeyVkqibwJKiv2Ecrvc6-dABY6scbhcgEyl09q0v3CL9TJblhErWaHdqfq-7NtTEqXJ5Q4a4U_dkfEDTG4Ut3NaxD3SB37R0FD05drmoZg6fo7vzjffatyYkiCuPGiLmMVhyCxvwMYXhr_IpBeiulRnyExKHTyNd3EtFzOfVpZXbpWOy4X_DbiC2X3xrOBwyQkrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RWbunUp_5AGR5XaXzNrE2SE5Vs_9CWt44KVieVhPmZahC6wyBKFFZcscCPTSiIMIdGJAPB6ywM_ITw9EbthEyAPZZEZMLqNjTYCSoMw1Xh4oUt5jFHzZ8hvV2VLHeFvCBpZRjRGgyZU9l_vsDQxZ--D906B873Dj4QROqIUUvOLLQqHj8xZUkXGzmUxzT6oV20lQkvFQsAKOvOBkBky5CrQk50_hL5LgsMfuzcD-c6BSwRU_mmWOn_TjZ2xc3ka73uV-pUKonn91dnZ4XF29RDI0I0Q_ZQJ3h6hbRksSvPJzqZVvPxmzo3k3Z9WFRORKMi55tHNtiHS9f-6SoP-MJQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
🚨
بلند شدن سوخت رسان ها از تل آویو و امارات به سمت جنوب ایران
@News_Hut</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/news_hut/67559" target="_blank">📅 23:29 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67558">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">🚨
🚨
🚨
فعال شدن پدافند در سیریک
@News_Hut</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/news_hut/67558" target="_blank">📅 23:26 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67557">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">🚨
🚨
🚨
مجدد انفجار در بندرعباس
@News_Hut</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/news_hut/67557" target="_blank">📅 23:23 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67556">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">🚨
🚨
🚨
حملات آمریکا به سیریک هرمزگان
@News_Hut</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/news_hut/67556" target="_blank">📅 23:19 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67555">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">🚨
🚨
🚨
❌
شنیده شدن صدای انفجار در بندرعباس
@News_Hut</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/news_hut/67555" target="_blank">📅 23:11 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67554">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2c65cdf89e.mp4?token=wBm15tqPrS7yYBSYzh3c3x9StYbXPsqhnf3jSLsv6ju6-qqI9CZ_PwPGuqbfI6eaXMIPynJPRcZPQUwH7QBmyiE1LFY_yH6WDzSAGUBEqeOFZzZFoboZsBy0RBbgVQtGLpuP8u12_4ED45GvEGq4yaUvRUcXGSmLgIHWiPP0qbv7n6s6lV11iKMJEhDWS8gJyRDGKFNHbO-sGZUWLXkSVnI8t_6P0AF5R8JxXXZQWk8-IiCMLKgy0UquUIvenjvREJRIDQDsRiywTdlGYdHppwRSE-srnHZTY5xCUfZt1bwkOQgIKpixX3YLM1ZbKFn8rYju9QyMed9iIFBHpIVeGQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2c65cdf89e.mp4?token=wBm15tqPrS7yYBSYzh3c3x9StYbXPsqhnf3jSLsv6ju6-qqI9CZ_PwPGuqbfI6eaXMIPynJPRcZPQUwH7QBmyiE1LFY_yH6WDzSAGUBEqeOFZzZFoboZsBy0RBbgVQtGLpuP8u12_4ED45GvEGq4yaUvRUcXGSmLgIHWiPP0qbv7n6s6lV11iKMJEhDWS8gJyRDGKFNHbO-sGZUWLXkSVnI8t_6P0AF5R8JxXXZQWk8-IiCMLKgy0UquUIvenjvREJRIDQDsRiywTdlGYdHppwRSE-srnHZTY5xCUfZt1bwkOQgIKpixX3YLM1ZbKFn8rYju9QyMed9iIFBHpIVeGQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇮🇱
خبرنگار: شما امروز با هگست جلسه دارید.
نخست وزیر نتانیاهو: احتمالاً این اتفاق نخواهد افتاد.
خبرنگار: آیا این شما را ناراحت می‌کند؟
نخست وزیر نتانیاهو: چه کسی گفته ناراحت کننده است؟ شاید معنای دیگری داشته باشد.
@News_Hut</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/news_hut/67554" target="_blank">📅 23:04 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67553">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/176e4f444a.mp4?token=YNYCwBiKJdSE17V7zsphrhdlI0Ta1LT9dLXlGKSQSWNYu40unw-AINgFB_8knsYw93oNOuX54J1yD2b4IC9uSOM6WVTBOQ-0XKQft35adjdRKKp68nE65ryF0BsFgRMhSW1nJgs0YtGAwmp_Ia_7LVtcwjaAiIkb2w4WHjArx4qZWzHGbIxto150G4JZApbCJtI_Rqe-GZ4xnsBssdBVQm8DGhBAF7zp-uRE6TFd-pPeJyqT4j-ZFy6wIkuAGhYqQqloGPYz3kC5SSqY88saLv5sghcTINMyKJ8CPP1vfivqOKm7Ok5GNeLE6JMPGVgpJxX5n537TwFTbtQ8eVMIOw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/176e4f444a.mp4?token=YNYCwBiKJdSE17V7zsphrhdlI0Ta1LT9dLXlGKSQSWNYu40unw-AINgFB_8knsYw93oNOuX54J1yD2b4IC9uSOM6WVTBOQ-0XKQft35adjdRKKp68nE65ryF0BsFgRMhSW1nJgs0YtGAwmp_Ia_7LVtcwjaAiIkb2w4WHjArx4qZWzHGbIxto150G4JZApbCJtI_Rqe-GZ4xnsBssdBVQm8DGhBAF7zp-uRE6TFd-pPeJyqT4j-ZFy6wIkuAGhYqQqloGPYz3kC5SSqY88saLv5sghcTINMyKJ8CPP1vfivqOKm7Ok5GNeLE6JMPGVgpJxX5n537TwFTbtQ8eVMIOw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
سرنگونی پهپاد MQ-9 آمریکا توسط جمهوری اسلامی
@News_Hut</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/news_hut/67553" target="_blank">📅 22:17 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67552">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/697775e593.mp4?token=qSOhfPPQZlLEmhTxBTd62M8BarCpDRFxjpowFZSRYigLbemGk_sblk0i8K43mjBQ0OMUTXcQn0FPPOxoy8qvIMD4NNlWoG5SC0jDsC7oyncXCeWQyjDDb4sgBzB4eJ-y-ec1E1Y4chn27obdQb_td2UM8xi5U3aiVHifDYM9qdhBtNS3rDnXBAexeoYYVBV1wUKAvvHndIuuRp-my4YbDJOWBNxdxUqiCUr-QWxyd9ffceDHqIpQ6X-J-CIfM3BhePOU5nhi2kN2HWXmxrFITQX0fNfNYfGPBQWjTAWZxJ-ApLO_dnX5lVg1xg71CQEacMdx5T12r962jNLujQdpiQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/697775e593.mp4?token=qSOhfPPQZlLEmhTxBTd62M8BarCpDRFxjpowFZSRYigLbemGk_sblk0i8K43mjBQ0OMUTXcQn0FPPOxoy8qvIMD4NNlWoG5SC0jDsC7oyncXCeWQyjDDb4sgBzB4eJ-y-ec1E1Y4chn27obdQb_td2UM8xi5U3aiVHifDYM9qdhBtNS3rDnXBAexeoYYVBV1wUKAvvHndIuuRp-my4YbDJOWBNxdxUqiCUr-QWxyd9ffceDHqIpQ6X-J-CIfM3BhePOU5nhi2kN2HWXmxrFITQX0fNfNYfGPBQWjTAWZxJ-ApLO_dnX5lVg1xg71CQEacMdx5T12r962jNLujQdpiQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ترامپ پس از پایان اجلاس ناتو، ترکیه را ترک کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/news_hut/67552" target="_blank">📅 22:17 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67551">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">حوصلم سر رفته بود این گردونه صراف رو زدم، 5 دلار داد
😐
😂
گفتم لینکشو بذارم شما هم بیکارید یه تستی بکنید ببینید چی میده بهتون
👇
https://r.saraf.app/s/agrd068</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/news_hut/67551" target="_blank">📅 22:17 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67550">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kc8suES1wMu_BCYn-Ggj1vyY6RCVruZZp5BMV9wufzZBywt9lHx9copEVSPou589V7Q48zUI7onJDcQ-ldMylxcVHFE_luck5dKWTy8RkWl7YTelNif1sy2m_WRh64o-l9ytWd5DofHOW5wSxmjWLd03Im5Gr2c9kuVG-FYUnTJo76gMb-Yw08Gt5kDjiJ6Ni8bowwwRadfgGlpd39R6j9MgBjIgIwqOuRJ-VWxVXBgxomVm8DFvIyFraMAt6ixPl_IHNdietsEvhRkJZCmhvCE3yXqX3XQCEN93j0GUiwFhFhHrqJiWW4AicV6DQ09VYNUA9CsGAkB2_46fNpZkOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇮🇷
عراقچی:
صحبت کردن با لحنی تحقیرآمیز با ملت بزرگ و شجاع ایران، از عظمت آن نمی‌کاهد.
ایرانیان به خاطر متانت، فرهنگ و ارزش‌های اخلاقی قوی خود شناخته شده‌اند. ما به بی ادبی با بی ادبی پاسخ نمی‌دهیم، بلکه با عمل: با شجاعت و با از خودگذشتگی فراوان.
@News_Hut</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/news_hut/67550" target="_blank">📅 21:27 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67549">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">🚨
🚨
گزارشگر: ماه گذشته، شما گفتید که رهبران ایران بسیار عاقل هستند. حالا شما می‌گویید که آن‌ها افراد بیمار هستند. چه تغییری رخ داده است؟ ترامپ: من آن‌ها را بهتر شناختم. آن‌ها بسیار عاقل‌تر از سطح اول و دوم هستند.  @News_Hut</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/news_hut/67549" target="_blank">📅 20:43 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67548">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/412c846bfe.mp4?token=oZm8faMB5wIzslRk9hAiioPCmuvlicnDBApq9TPOSYL0sGXpwL1wo_DH6dI4ZVgQSG4d8XshCbXbXwfnAn4Kjo8OjQlNubQfnXzavosSoEj1oUuOSeG0rptDBPlBbh3NqWrDQKn2tUmwOFIAliutC2A7UQWHEqj2Vvvww4lpr7Zyfeensz9yg3VEd1CK-gKFhVpuo9J79Io6zgoSYmOCdLE8qjzByvfoQANonTfcL0uTVY19YatjPrTdANT9MzchAwhwn1ukYqOF-V21cYkd70xjpF0xcW9gXI-lOojwfiq0iGw4ssJhE-SEMOGyS-jH0BUUtxBrxEiHA4vj13rLXw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/412c846bfe.mp4?token=oZm8faMB5wIzslRk9hAiioPCmuvlicnDBApq9TPOSYL0sGXpwL1wo_DH6dI4ZVgQSG4d8XshCbXbXwfnAn4Kjo8OjQlNubQfnXzavosSoEj1oUuOSeG0rptDBPlBbh3NqWrDQKn2tUmwOFIAliutC2A7UQWHEqj2Vvvww4lpr7Zyfeensz9yg3VEd1CK-gKFhVpuo9J79Io6zgoSYmOCdLE8qjzByvfoQANonTfcL0uTVY19YatjPrTdANT9MzchAwhwn1ukYqOF-V21cYkd70xjpF0xcW9gXI-lOojwfiq0iGw4ssJhE-SEMOGyS-jH0BUUtxBrxEiHA4vj13rLXw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇺🇸
ترامپ خطاب به ممدباقر درباره اورانیوم:
ما دوربین‌هایی داریم، که بخشی از نیروی فضایی ما هستند، که می‌توانند نشان شناسایی فردی که به یک سایت خاص می‌رود را بخوانند. محمد، چیزی آنجا وجود دارد که با بیل و کلنگ در حال کار هستند.
بیل و کلنگ به شما کمک نمی‌کنند. بزرگترین ماشین‌آلات دنیا هم به شما کمک نمی‌کنند. این موضوع بسیار، بسیار عمیق‌تر است.
اما ما این موضوع را زیر نظر داریم و اگر کسی به آنجا برود، منفجر خواهد شد. بنابراین، هیچ‌کس به آنجا نزدیک نخواهد شد. در نهایت، ما آن را تصاحب خواهیم کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/news_hut/67548" target="_blank">📅 20:39 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67547">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dd8dc7e8bc.mp4?token=cfjAphQm1P2czFcOI0aLW-2GfAZ9ALK5rDLc7vXYdxlAgzGIBBWAcCo75bS0aGL8hupMgtvh_i7hiy4AP3iKJrEasZ7FNNTWIXQJuztG2IKv2muB95gjdWY5fmj7gFwUzlUk5Y-BbZB0rcXcuwv7uIdDWTT72sShagKrO1DhCAL2ZliFaG0KKedGGC3F9OE5uNUqh-BjdjtyvNU4WSX6y4SMqJWb_kqGPIqbyMbtyfgp8I9qr6SdcSLYGwvdY4i22kPJ65lMraljE2Z5gHAC6V4kJzbCIpczsH_JPqQ96d-jrzywYHuZoothaiOEFrFeO6E-nOgxtMiLX86hi_DmPw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dd8dc7e8bc.mp4?token=cfjAphQm1P2czFcOI0aLW-2GfAZ9ALK5rDLc7vXYdxlAgzGIBBWAcCo75bS0aGL8hupMgtvh_i7hiy4AP3iKJrEasZ7FNNTWIXQJuztG2IKv2muB95gjdWY5fmj7gFwUzlUk5Y-BbZB0rcXcuwv7uIdDWTT72sShagKrO1DhCAL2ZliFaG0KKedGGC3F9OE5uNUqh-BjdjtyvNU4WSX6y4SMqJWb_kqGPIqbyMbtyfgp8I9qr6SdcSLYGwvdY4i22kPJ65lMraljE2Z5gHAC6V4kJzbCIpczsH_JPqQ96d-jrzywYHuZoothaiOEFrFeO6E-nOgxtMiLX86hi_DmPw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇺🇸
ترامپ درباره ایران:
مطمئن نیستم که بخواهم با آنها به توافقی برسم.
ما می‌توانیم بازی‌ها را انجام دهیم، اما مطمئن نیستم که بخواهم به توافقی برسم.
فقط بیایید این کار را به پایان برسانیم.
@News_Hut</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/news_hut/67547" target="_blank">📅 20:34 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67546">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a1d009a331.mp4?token=WQyepfyd-L42lCH6XfWCXfSXEWP6ZLJn_ycao587Gsz7Zzed46bSIo2dh6-0rIMYCr1JDwbLGdf-1hUqNkjMjl0QRc1gKhx_ule-IHhLFPx_Z8uto7kyjzcJOHbFqebZH9irz7Ic1oyT8Ux-G2AbzEfy6wjgQsmPWzwpqGEhVY1qDcT-AXKjta5OrSgSUd3YYmV8Mker2lMiB18dZzRBXX39cID6Lj-pPJKnaHw9fsDkis_sk2XhPhjXrOlTtn2x9-JofvdFTNc-rv7Rr2RW41bft4w43Dx30Cfq4n6AjvhDer9Hsgbj_6JnVHpzHyI1IH_BD8QzqDi9c5YEX8GAzg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a1d009a331.mp4?token=WQyepfyd-L42lCH6XfWCXfSXEWP6ZLJn_ycao587Gsz7Zzed46bSIo2dh6-0rIMYCr1JDwbLGdf-1hUqNkjMjl0QRc1gKhx_ule-IHhLFPx_Z8uto7kyjzcJOHbFqebZH9irz7Ic1oyT8Ux-G2AbzEfy6wjgQsmPWzwpqGEhVY1qDcT-AXKjta5OrSgSUd3YYmV8Mker2lMiB18dZzRBXX39cID6Lj-pPJKnaHw9fsDkis_sk2XhPhjXrOlTtn2x9-JofvdFTNc-rv7Rr2RW41bft4w43Dx30Cfq4n6AjvhDer9Hsgbj_6JnVHpzHyI1IH_BD8QzqDi9c5YEX8GAzg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇺🇸
املاکی درباره ایران:
به نظر من، جنگ با ایران دوباره آغاز نخواهد شد. وقتی آنها حمله می‌کنند، ما ۱۰ برابر قوی‌تر پاسخ می‌دهیم.
شاید امشب به آنها حمله کنیم.
هر اتفاقی که قرار است بیفتد، خیلی سریع رخ خواهد داد.
ما به دنبال یک راه حل بلندمدت نیستیم.
@News_Hut</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/news_hut/67546" target="_blank">📅 20:30 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67545">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">🚨
🚨
🇺🇸
پرزیدنت ترامپ:
من می‌خواهم این موضوع را در مورد ایران به پایان برسانم و با رهبران فعلی بازی نکنم.
@News_Hut</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/news_hut/67545" target="_blank">📅 20:22 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67544">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/966c88b1c6.mp4?token=OZVeNjmwODOcdibpx0xbX3Y9goweTUfBCvSwKfHcazTtk9jKjGFLb_6segsheI64kxO8ACE0GWkFvFDJmPc6X21xnDmCYez4GHA_5jztNsiHtX_glBUK9rqCXMFh_Jf1FIGiHPmg7pajkdY36dljT4S-P5yhaxI1wsrR3BiFwCQvs3SC_yRuq_BWm1sKQR5UZSe6HXF0J-LTDmzWc0GKOXToWCvBieXWDEKXG8uMbAXfGFez5uC75yEcL038jR2dWy4eX8_EBZKORi2EmshwZ2C8v4rOgR63CAz_IkGMXwhEDLuaQcnQ84yOBnWoyRdd54ntqKpy9d6yaGNlJUamgA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/966c88b1c6.mp4?token=OZVeNjmwODOcdibpx0xbX3Y9goweTUfBCvSwKfHcazTtk9jKjGFLb_6segsheI64kxO8ACE0GWkFvFDJmPc6X21xnDmCYez4GHA_5jztNsiHtX_glBUK9rqCXMFh_Jf1FIGiHPmg7pajkdY36dljT4S-P5yhaxI1wsrR3BiFwCQvs3SC_yRuq_BWm1sKQR5UZSe6HXF0J-LTDmzWc0GKOXToWCvBieXWDEKXG8uMbAXfGFez5uC75yEcL038jR2dWy4eX8_EBZKORi2EmshwZ2C8v4rOgR63CAz_IkGMXwhEDLuaQcnQ84yOBnWoyRdd54ntqKpy9d6yaGNlJUamgA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇺🇸
ترامپ درباره ایران:
هر اتفاقی که قرار است بیفتد، به سرعت رخ خواهد داد.
ما به دنبال راهکارهای بلندمدت نیستیم.
@News_Hut</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/news_hut/67544" target="_blank">📅 20:16 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67543">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3ce02ad2ec.mp4?token=mlfvdprbBUP3wI65QrT7e3NptAna5itASch7N8HCmwuD_dEDP4cAhpvmc4qM24GgKo4LzajAPLoB5KSsuXBmYNXnM9BDFYGcwSXgXQKta8Y6QJ5ojSN57shDG05d_ziFOWuNC4srsWiXgMoQWSWqZwe3Fj8XLUkq5BEYRAGjgLORezinPdvCKQubVJCeRxhb4Odoh5KxTVB2xTn6nXDYIw_E730STOwR7Soh3m7PdDwb9LPu-Z28TIEkCHenpWnqZkrYNv43zX1dbFhbI1ObiCKvtjVV775E0Pf-qrjYlLdxaY-vMccrCJwdPFVN12ZX-yHBUCxDmDf0x7DHZmJxrg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3ce02ad2ec.mp4?token=mlfvdprbBUP3wI65QrT7e3NptAna5itASch7N8HCmwuD_dEDP4cAhpvmc4qM24GgKo4LzajAPLoB5KSsuXBmYNXnM9BDFYGcwSXgXQKta8Y6QJ5ojSN57shDG05d_ziFOWuNC4srsWiXgMoQWSWqZwe3Fj8XLUkq5BEYRAGjgLORezinPdvCKQubVJCeRxhb4Odoh5KxTVB2xTn6nXDYIw_E730STOwR7Soh3m7PdDwb9LPu-Z28TIEkCHenpWnqZkrYNv43zX1dbFhbI1ObiCKvtjVV775E0Pf-qrjYlLdxaY-vMccrCJwdPFVN12ZX-yHBUCxDmDf0x7DHZmJxrg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
گزارشگر: ماه گذشته، شما گفتید که رهبران ایران بسیار عاقل هستند. حالا شما می‌گویید که آن‌ها افراد بیمار هستند. چه تغییری رخ داده است؟
ترامپ: من آن‌ها را بهتر شناختم. آن‌ها بسیار عاقل‌تر از سطح اول و دوم هستند.
@News_Hut</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/news_hut/67543" target="_blank">📅 20:15 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67542">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ac6daa8309.mp4?token=QjZGBlsF7TjueN6P6p1MEv6iUT-6lDh8dwEmur-vZKLjn_dblTAb2Gfju2mP9RLLj4kL03FSogFrhTEfBLHgECoeQjtq9YKbtj-p39dWcnrLMjrsC81HBTzK6p5-JNcGzNaVpBCnHEf2xh6sWqBBEaE-8PFoQ_moE2LLniATpiJ7xtHbEd3M20kMLvvMwTKuEG4MYItcm86wzW4cODgLJvvD6GlyBPKYVZpUT5vmfKKDj3DLJVDSH7jvbJfaokShs_BQn05Lvs2OTA1-HbUFlMkWhkN8O-ruit71z15_0CO6RGbE9vaPX_M3BWc5cyRWGyIkupEIbGrmR5HMo8hY6Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ac6daa8309.mp4?token=QjZGBlsF7TjueN6P6p1MEv6iUT-6lDh8dwEmur-vZKLjn_dblTAb2Gfju2mP9RLLj4kL03FSogFrhTEfBLHgECoeQjtq9YKbtj-p39dWcnrLMjrsC81HBTzK6p5-JNcGzNaVpBCnHEf2xh6sWqBBEaE-8PFoQ_moE2LLniATpiJ7xtHbEd3M20kMLvvMwTKuEG4MYItcm86wzW4cODgLJvvD6GlyBPKYVZpUT5vmfKKDj3DLJVDSH7jvbJfaokShs_BQn05Lvs2OTA1-HbUFlMkWhkN8O-ruit71z15_0CO6RGbE9vaPX_M3BWc5cyRWGyIkupEIbGrmR5HMo8hY6Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇺🇸
ترامپ درباره ایران:
می‌دانید؟ ممکن است من هم دیگر نباشم.
من هدف شماره یک آن‌ها هستم.
@News_Hut</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/news_hut/67542" target="_blank">📅 20:11 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67541">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0540439bf4.mp4?token=KhJKZePr81tyjsEUl3FTEioH7YvU_vywSjUUpVI6CkJLCYLZUxuhoStpuKM4_1vYeE10vDzluSmTaBu8lWgmH-7YQ6kN_l7UEP23BSOH0c5kZDcW5ZwSihcEkWdsof1q6IEOVpW09tacCuT2O3Zwd1x9YQUYX1sZby9M_8peghaSv2dmeVQ_rd7lL3D1ltyDnbEI1iVL4GV-NyO-sGgylIzG2lEaI6Wuq0qTijerYZtqO8m3HkDeB0OXAqtf96PR_dENElzMs15UIF2Rk8KskktZLu1n0cdaKnMci3VLpLeGjqv8r1uzMXMys3dZmQSvlVcwKJDda3D_0q70_Yg80A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0540439bf4.mp4?token=KhJKZePr81tyjsEUl3FTEioH7YvU_vywSjUUpVI6CkJLCYLZUxuhoStpuKM4_1vYeE10vDzluSmTaBu8lWgmH-7YQ6kN_l7UEP23BSOH0c5kZDcW5ZwSihcEkWdsof1q6IEOVpW09tacCuT2O3Zwd1x9YQUYX1sZby9M_8peghaSv2dmeVQ_rd7lL3D1ltyDnbEI1iVL4GV-NyO-sGgylIzG2lEaI6Wuq0qTijerYZtqO8m3HkDeB0OXAqtf96PR_dENElzMs15UIF2Rk8KskktZLu1n0cdaKnMci3VLpLeGjqv8r1uzMXMys3dZmQSvlVcwKJDda3D_0q70_Yg80A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇺🇸
ترامپ درباره ایران:
ایران می‌خواهد به توافقی برسد، اما نمی‌داند چگونه باید به توافق برسد.
و سپس، شب‌ها به کشتی‌ها حمله می‌کنند. من این کار را دوست ندارم.
@News_Hut</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/news_hut/67541" target="_blank">📅 20:11 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67540">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ff03b3210e.mp4?token=O30C8nSlw6tP7vTBxtNDooFoJRI9tAMKpalsyJxlVjGDRLlguEfzHZIpPGVUskhL4dKskx39EXG9NxtW3di4VZ4kZnCu2t5E23oM6-VOOC64alkVLvHrU0sDH_DDIQMeKaY6GQ6jtuSKG1IkMyilKlGJ-L9QlMTB1axScjSobz8Xwn-eMcwD6W4uzwErb3aY5Y0O2Z10FqgDpbUldjeb3BY4jmgPajkQFbEo4RGLxeCLXgKhLq7FidH4K6RDmpSY55x_6GsRzXEH4-0L8EA_nDbM3ay0Uu7g-udW5vO3P_acmvsn33ukQtidiCKwKfyH_PkFOJIdqtC3Pk7ahJcWYA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ff03b3210e.mp4?token=O30C8nSlw6tP7vTBxtNDooFoJRI9tAMKpalsyJxlVjGDRLlguEfzHZIpPGVUskhL4dKskx39EXG9NxtW3di4VZ4kZnCu2t5E23oM6-VOOC64alkVLvHrU0sDH_DDIQMeKaY6GQ6jtuSKG1IkMyilKlGJ-L9QlMTB1axScjSobz8Xwn-eMcwD6W4uzwErb3aY5Y0O2Z10FqgDpbUldjeb3BY4jmgPajkQFbEo4RGLxeCLXgKhLq7FidH4K6RDmpSY55x_6GsRzXEH4-0L8EA_nDbM3ay0Uu7g-udW5vO3P_acmvsn33ukQtidiCKwKfyH_PkFOJIdqtC3Pk7ahJcWYA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
فرماندهی مرکزی ایالات متحده:
امروز، بیش از 20 فروند از ناوهای جنگی نیروی دریایی ایالات متحده در حال گشت‌زنی در آب‌های سراسر خاورمیانه هستند، در حالی که نیروهای سنتکام به ترویج امنیت و ثبات منطقه‌ای ادامه می‌دهند. ماه گذشته، ناوها و هواپیماهای نیروی دریایی آمریکا به صورت منظم در دریای عرب حرکت کردند و قدرت نظامی و توان آتش بی‌نظیر آمریکا را به نمایش گذاشتند.
@News_Hut</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/news_hut/67540" target="_blank">📅 20:02 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67538">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">‼️
ویدیو ای که سپاه از حملات دیشبش به پایگاه های آمریکا در منطقه منتشر کرده.
@News_Hut</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/news_hut/67538" target="_blank">📅 19:30 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67537">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/735f956d53.mp4?token=sCSAxYnguBdu2XKWJMg3KhJ3KO7seEvXMoj-BmOP9hTPkyM09UsIgFZTDFMTOX752xoDfT0gWLDQHNPyXVAQ7uTAW_12zFmnDJl2i6NJigY9tBw9O0mSSrTe0wewnWlYVQrcNUjIGQukAY0bDPArOKUXoAyBRYlmrJqH7njbFgzZs9Nw8LNGKKqhI51R5CQO0R3_GtyBZbq9DyyMTEeHA7m6rwGIV73fOpt9XF9scmvZ7QKn7k33PiFa-GYVyq1HmDhZS1yKuBzLsrkIMRIjqEW3LYDq1z9fUi6TVKovw36X4SwCWtt4j_FuHtrjoc1VcjQbA_ZIsP0g9JlJVMqHHQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/735f956d53.mp4?token=sCSAxYnguBdu2XKWJMg3KhJ3KO7seEvXMoj-BmOP9hTPkyM09UsIgFZTDFMTOX752xoDfT0gWLDQHNPyXVAQ7uTAW_12zFmnDJl2i6NJigY9tBw9O0mSSrTe0wewnWlYVQrcNUjIGQukAY0bDPArOKUXoAyBRYlmrJqH7njbFgzZs9Nw8LNGKKqhI51R5CQO0R3_GtyBZbq9DyyMTEeHA7m6rwGIV73fOpt9XF9scmvZ7QKn7k33PiFa-GYVyq1HmDhZS1yKuBzLsrkIMRIjqEW3LYDq1z9fUi6TVKovw36X4SwCWtt4j_FuHtrjoc1VcjQbA_ZIsP0g9JlJVMqHHQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏸
صدا و سیما و رسانه خامنه ای برای اولین بار فیلمی از حسینیه امام خمینی در بیت رهبری جایی که رهبر جمهوری اسلامی مورد هدف قرار گرفت را منتشر کردند.
@News_Hut</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/news_hut/67537" target="_blank">📅 19:20 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67536">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">🚨
🚨
یدیوت احرونوت:
نخست‌وزیر اسرائیل، نتانیاهو، و وزیر دفاع، کاتز، حضور خود را در یک رویداد لغو کرده‌اند و در حال بحث و بررسی مسائل امنیتی مرتبط با تحولات مربوط به ایران هستند.
@News_Hut</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/news_hut/67536" target="_blank">📅 18:55 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67535">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/62a14b7982.mp4?token=esQxTCAqAXjwG25XLBqWoR2nvHKPl8girqHz6eGbzuivHm4u6X6aGqgxR-RE_YGVRutH95BxiBlhsLP-ao9fgpNX0KD_FvyITdiIQ-gpRH3D50wu7HyrIcDyG47PcDdy7YfxVt31199avlorpMqqIzbFyehiHwvOcX-7qiPgFgTmZ-B-2S9S4MfJJ7dLrCcUW00aM2-Y6jBcthE1cSMr2OTUunvW3-cEe5lebMz1HWRTGX2eOf4r_czUmIVBh5hKU7q2F1TRhWJQQwtO-zSeeSXDRHJBHAgv7brZvTDIowCIPlHv_HxbVYIwxOhAQUhnzJPJtOYyBoL5MSu6BPtyPQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/62a14b7982.mp4?token=esQxTCAqAXjwG25XLBqWoR2nvHKPl8girqHz6eGbzuivHm4u6X6aGqgxR-RE_YGVRutH95BxiBlhsLP-ao9fgpNX0KD_FvyITdiIQ-gpRH3D50wu7HyrIcDyG47PcDdy7YfxVt31199avlorpMqqIzbFyehiHwvOcX-7qiPgFgTmZ-B-2S9S4MfJJ7dLrCcUW00aM2-Y6jBcthE1cSMr2OTUunvW3-cEe5lebMz1HWRTGX2eOf4r_czUmIVBh5hKU7q2F1TRhWJQQwtO-zSeeSXDRHJBHAgv7brZvTDIowCIPlHv_HxbVYIwxOhAQUhnzJPJtOYyBoL5MSu6BPtyPQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
خبرنگار: آیا برنامه‌ای برای اعزام نیروی زمینی به ایران ندارید؟
ترامپ: چرا باید الان وارد عمل شوم؟ من زمانی وارد عمل خواهم شد که آن‌ها کاملاً از بین بروند یا به یک توافق برسیم.
@News_Hut</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/news_hut/67535" target="_blank">📅 18:38 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67534">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2479db8c8d.mp4?token=h1Wge6i32cgqZgraBGCCsVROIBt0G09-S8ukoXPaxAbjVP3ThqRFUJk7EnB2wCVeIJ4j8p6I4iZVGCSz3biz5XS9WrGfrGC52HJpou4BDnAZisvbTn8-fDtY0mHBMgmvSoTd3HfsFEQFoTvOSB4kcxIbk6rAq2tEMiHJLQU152w_vnpLeX0jMhL7RKObHy08KN547DNhI9lFPPkY6neI2JXCYDl4_ZYC9tqqDCnR5b7e7qqQc9AxZre1HMypi4USAJeNizS1HGWGp7ODLWe5sY1TFgymjL39JYOmGAAUelb1ETQJUHpGRWpdLZT6cHMbaNKQGKrSYUAsSk7wWrbCGQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2479db8c8d.mp4?token=h1Wge6i32cgqZgraBGCCsVROIBt0G09-S8ukoXPaxAbjVP3ThqRFUJk7EnB2wCVeIJ4j8p6I4iZVGCSz3biz5XS9WrGfrGC52HJpou4BDnAZisvbTn8-fDtY0mHBMgmvSoTd3HfsFEQFoTvOSB4kcxIbk6rAq2tEMiHJLQU152w_vnpLeX0jMhL7RKObHy08KN547DNhI9lFPPkY6neI2JXCYDl4_ZYC9tqqDCnR5b7e7qqQc9AxZre1HMypi4USAJeNizS1HGWGp7ODLWe5sY1TFgymjL39JYOmGAAUelb1ETQJUHpGRWpdLZT6cHMbaNKQGKrSYUAsSk7wWrbCGQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇺🇸
ترامپ:
هر زمان که ما به ایران حمله کنیم، قیمت نفت کمی افزایش می‌یابد.مشکلی نیست.
@News_Hut</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/news_hut/67534" target="_blank">📅 18:29 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67533">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/72f85ab468.mp4?token=J7wl_15O5yHeyCV0Y8auqgjzMUhhgUY2Q4lPYaGnLIQLknOmeA5q5tCtYONOGZCwaDCPfKyrJ7WwfzlW3ahlrXO8b6Odp34twimsckjAw-xkQVze94xsfurvbqZRaENa5ZY0apKdiEJ1FnF2dmjFiNNVXdJlxmTtY0DKcHTQVpYQ-t0yVfBPVEajhyHxfvkfAddXoGlFucbvz3Xp16v6X5GFuhawvw2VHXVnQiVkje7oJVs35fQD_5qQO1VvGh6LYba9-hrvcK_hiHmp0-00V1n2RPuAZdDV1KcNOO09G9ztt_fjpsrDenbLtt5vxrVBnLLppK6RjFkYZN5f3dja0w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/72f85ab468.mp4?token=J7wl_15O5yHeyCV0Y8auqgjzMUhhgUY2Q4lPYaGnLIQLknOmeA5q5tCtYONOGZCwaDCPfKyrJ7WwfzlW3ahlrXO8b6Odp34twimsckjAw-xkQVze94xsfurvbqZRaENa5ZY0apKdiEJ1FnF2dmjFiNNVXdJlxmTtY0DKcHTQVpYQ-t0yVfBPVEajhyHxfvkfAddXoGlFucbvz3Xp16v6X5GFuhawvw2VHXVnQiVkje7oJVs35fQD_5qQO1VvGh6LYba9-hrvcK_hiHmp0-00V1n2RPuAZdDV1KcNOO09G9ztt_fjpsrDenbLtt5vxrVBnLLppK6RjFkYZN5f3dja0w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇺🇸
پرزیدنت ترامپ درباره اورانیوم های غنی شده:
این مواد تا این حد در زیر زمین قرار دارند که هیچ‌کس به جز ما نمی‌تواند به آن‌ها دسترسی پیدا کند، زیرا ما تجهیزات لازم را داریم.
این مواد در اعماق زیر یک کوه قرار دارند و اکنون مشخص شده است که برای دسترسی به آن‌ها، به ماشین‌آلات بسیار بزرگ نیاز است که ما در اختیار داریم و هیچ کشور دیگری این تجهیزات را ندارد.
@News_Hut</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/news_hut/67533" target="_blank">📅 18:28 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67532">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0911dd57d8.mp4?token=hAYYSQVCnAlZj_pMmDzPgPXGOw6YVkxO5ax65rG-q9YdQKyRDvnvjyd22_QXJ09f_kCfBcuLHqf9Ewuhc7PlL9M45_E__D_ChZo8igLC1Y0GaM8PsAhSKK6GRCHbr0v9bj9LAcKRJL_02HS2-xzJvW0g53nbsACn7lHQw-etRSP0HuS_GcnyXzTP_MD8g9FiGPEBDMnr_0s2bf5p3Bed8-GsO__9pkjRP8cRiPIB8xNvrK1HrxjpXSPXgt9GwYh4DPhu8XdNiJOmDUQTVyrrz8Ruj8ExbSLaKt1gGvTsQK6pK-KTXZ0PE0yOlSePjkQJ-xaEiflhsrW9WilTXTh8ig" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0911dd57d8.mp4?token=hAYYSQVCnAlZj_pMmDzPgPXGOw6YVkxO5ax65rG-q9YdQKyRDvnvjyd22_QXJ09f_kCfBcuLHqf9Ewuhc7PlL9M45_E__D_ChZo8igLC1Y0GaM8PsAhSKK6GRCHbr0v9bj9LAcKRJL_02HS2-xzJvW0g53nbsACn7lHQw-etRSP0HuS_GcnyXzTP_MD8g9FiGPEBDMnr_0s2bf5p3Bed8-GsO__9pkjRP8cRiPIB8xNvrK1HrxjpXSPXgt9GwYh4DPhu8XdNiJOmDUQTVyrrz8Ruj8ExbSLaKt1gGvTsQK6pK-KTXZ0PE0yOlSePjkQJ-xaEiflhsrW9WilTXTh8ig" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇺🇸
وزیر جنگ هگست:   «امشب، اگر نیاز باشد، با دستور شما آقای رئیس‌جمهور، حتی بیشتر و عمیق‌تر حمله خواهیم کرد، زیرا این همان پیامد است.»  @News_Hut</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/news_hut/67532" target="_blank">📅 17:48 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67531">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/db8877d1b1.mp4?token=fyn6ZUiP4JRvL0F3EBRKGC6uNNA94jnzjnM6oZSuD1M-FeqKCCBxXX_nkRiD8WK7zqsxJl7lMpTyYtNVu2mmZWBiQC7DPx0uccoq5cQ_I-i3sMoo4mJvYhkIR7juWxtNxfIwbs2B-XQ1R6bk2eYBrl4_NwHxHcoM0Vx4Gc-JbAOzSp-QWDqYyEuocbh2KDTRZCLpzZWU8twGVoMfo5qdEiASqh8o8LMPRIZM8PRBl7YzkgxFfge1Wn6XcEBmeDd_-KyZyM3IAmjujdBW-dSCRzCLO0BDWr7yIUS3Qj7olGllWLK4CEXm0L05-B9DuTbEQnHRRUQJrHWsu2bujUeOlA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/db8877d1b1.mp4?token=fyn6ZUiP4JRvL0F3EBRKGC6uNNA94jnzjnM6oZSuD1M-FeqKCCBxXX_nkRiD8WK7zqsxJl7lMpTyYtNVu2mmZWBiQC7DPx0uccoq5cQ_I-i3sMoo4mJvYhkIR7juWxtNxfIwbs2B-XQ1R6bk2eYBrl4_NwHxHcoM0Vx4Gc-JbAOzSp-QWDqYyEuocbh2KDTRZCLpzZWU8twGVoMfo5qdEiASqh8o8LMPRIZM8PRBl7YzkgxFfge1Wn6XcEBmeDd_-KyZyM3IAmjujdBW-dSCRzCLO0BDWr7yIUS3Qj7olGllWLK4CEXm0L05-B9DuTbEQnHRRUQJrHWsu2bujUeOlA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇺🇸
وزیر جنگ هگست:
«امشب، اگر نیاز باشد، با دستور شما آقای رئیس‌جمهور، حتی بیشتر و عمیق‌تر حمله خواهیم کرد، زیرا این همان پیامد است.»
@News_Hut</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/news_hut/67531" target="_blank">📅 17:36 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67530">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">🚨
🚨
🚨
🇺🇸
#فوووری
؛ ترامپ:
به ایران هشدار میدم، دیشب ضربات سختی رو بهشون زدیم، اما امشب قراره براشون سخت‌تر باشه و حسابی بهشون حمله میکنیم.
@News_Hut</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/news_hut/67530" target="_blank">📅 17:26 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67529">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5f1152c373.mp4?token=UeurP_eGvp7jlQE0Fw-YnAWeaEFC4qv7j-xnyB0LnFGWUFPL1wiVu5ZTbSkKIUkqgF-85SqXGLQOfz84j7rMY8J1CiW2df6R450viwwj6gz1SwL6KDU8CqSMFG6qQMROKil4euxAdJdokIbprCF3M3QQ2KO4LaiLntvxV2hQ-QYLKH3IbGXuFL65EHGdK5wqfPeLUTZV9sZz7KLTveLVlGScrKb9cL4daBa7RKQIGFppM2L-cC0HsBITUKHHGoe32j2QrIpJsdiPwxbXg_ToAUsw60tJ49vajKX2cpjzw5VSuizwlTPu-iNw074q2WY8P6KJnNYw91jxB7p-yiHMIA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5f1152c373.mp4?token=UeurP_eGvp7jlQE0Fw-YnAWeaEFC4qv7j-xnyB0LnFGWUFPL1wiVu5ZTbSkKIUkqgF-85SqXGLQOfz84j7rMY8J1CiW2df6R450viwwj6gz1SwL6KDU8CqSMFG6qQMROKil4euxAdJdokIbprCF3M3QQ2KO4LaiLntvxV2hQ-QYLKH3IbGXuFL65EHGdK5wqfPeLUTZV9sZz7KLTveLVlGScrKb9cL4daBa7RKQIGFppM2L-cC0HsBITUKHHGoe32j2QrIpJsdiPwxbXg_ToAUsw60tJ49vajKX2cpjzw5VSuizwlTPu-iNw074q2WY8P6KJnNYw91jxB7p-yiHMIA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇺🇸
ترامپ درباره ایران:
آنها توافق کردند که هرگز سلاح هسته‌ای نخواهند داشت.
و سپس، آنها به بیرون می‌روند و می‌گویند که ما هرگز درباره این موضوع بحث نکردیم.
چه کسی باور خواهد کرد؟
@News_Hut</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/news_hut/67529" target="_blank">📅 17:25 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67528">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ff51c5e950.mp4?token=PtQZjGUJt0LB5WHGfPCZIVIVqDxWKWf0G8_Voy4TF89lSyIPtlbd-8tXjTmpM8Rglf9lEQZKOB92Waqu6oJZ1DT91TgMzYvX9b0XwOu_UXyr4HZbZ1CmlEuRNuOhwABd8lqycq2_vYz4X7nnXv-_D9vmMrmmQ73Vf7V118JyYFlm5eWKPi8COiTcZIHTZPK2gyuSvvOW1Rpv24cJsD-e0B11Tb_3db2sggpiHwh2dEvgeOrBBK18ao3WTztWw1ONMYcQJn60MQvkDVCQYXu-NzYZB2n_6Ow4zjfFU2q-kLBPn6QVEqoo73WzykREPql4_7H-qaWTD8SIaL8lJeNAGA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ff51c5e950.mp4?token=PtQZjGUJt0LB5WHGfPCZIVIVqDxWKWf0G8_Voy4TF89lSyIPtlbd-8tXjTmpM8Rglf9lEQZKOB92Waqu6oJZ1DT91TgMzYvX9b0XwOu_UXyr4HZbZ1CmlEuRNuOhwABd8lqycq2_vYz4X7nnXv-_D9vmMrmmQ73Vf7V118JyYFlm5eWKPi8COiTcZIHTZPK2gyuSvvOW1Rpv24cJsD-e0B11Tb_3db2sggpiHwh2dEvgeOrBBK18ao3WTztWw1ONMYcQJn60MQvkDVCQYXu-NzYZB2n_6Ow4zjfFU2q-kLBPn6QVEqoo73WzykREPql4_7H-qaWTD8SIaL8lJeNAGA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇺🇸
ترامپ:
جمهوری اسلامی ژاپن دیشب به ناو هواپیمابر ما حمله کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/news_hut/67528" target="_blank">📅 17:23 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67527">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ac18509fa8.mp4?token=AfcPVpt9yH8GscT9Flxz307CM2VhBO3RyQGAe4oU1OgpJ82_DdDOKWvI89OJ-7Idx5Y2iqmrdE1sp6RClpU6lsXyYTFJchqDiN9gO7qJYsd68kuVnEaOaSbnqBbXn587cW3MOMi3q3o1x65qgcAF6KgKemKoK_bayNWaBQzTkrWKq92v8shivj05yBv6St5qVVAedJ3gKtzbc3mregQNoRHZJ7FNpWdj3AWgQPo4jpUzNGoA4L7ucWYsGfUxhRSPPiFM8_mBeLba0To_41Qe6b6Fur54dEqoq5qvp2pugmwKmryt0CDJ8pd0KEBwsKXoytBEuK-cMClepjZUXBkSOw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ac18509fa8.mp4?token=AfcPVpt9yH8GscT9Flxz307CM2VhBO3RyQGAe4oU1OgpJ82_DdDOKWvI89OJ-7Idx5Y2iqmrdE1sp6RClpU6lsXyYTFJchqDiN9gO7qJYsd68kuVnEaOaSbnqBbXn587cW3MOMi3q3o1x65qgcAF6KgKemKoK_bayNWaBQzTkrWKq92v8shivj05yBv6St5qVVAedJ3gKtzbc3mregQNoRHZJ7FNpWdj3AWgQPo4jpUzNGoA4L7ucWYsGfUxhRSPPiFM8_mBeLba0To_41Qe6b6Fur54dEqoq5qvp2pugmwKmryt0CDJ8pd0KEBwsKXoytBEuK-cMClepjZUXBkSOw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇺🇸
پرزیدنت ترامپ:
ممکن است محاصره را دوباره اعمال کنیم.
@News_Hut</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/news_hut/67527" target="_blank">📅 17:21 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67526">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e08b208584.mp4?token=snEp8kEWe3rKHjlEjsyXgugG0fYNM7O4QZ6SbM2XcCeUdMzSZcPiZf2p0gDoTwN9weHuHHsOQb5T9tgn4QxV81PXukvsVrACOUy0iitnQC3ZMc54OqYJgCaQqrHPFkcxI4d7PextNdOXJQZ9IlPbHY7zhdaVs_BAQgQyNdeZvU28fuf3sOF3T-iHGHTOE1_gCUL9ZoAe0jngu6mfv7qnufk9stWHHWW2MDiB73cbqQb5gdzrntJq0KGT0m0yNeziP5EOUcHuaF-fpBSK0srBvIDv4wFH8vzxprFBl9PoOqiZTxezjazoNXHCnPthMHUvOo0g9YRUpnw1Sundk3R1gQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e08b208584.mp4?token=snEp8kEWe3rKHjlEjsyXgugG0fYNM7O4QZ6SbM2XcCeUdMzSZcPiZf2p0gDoTwN9weHuHHsOQb5T9tgn4QxV81PXukvsVrACOUy0iitnQC3ZMc54OqYJgCaQqrHPFkcxI4d7PextNdOXJQZ9IlPbHY7zhdaVs_BAQgQyNdeZvU28fuf3sOF3T-iHGHTOE1_gCUL9ZoAe0jngu6mfv7qnufk9stWHHWW2MDiB73cbqQb5gdzrntJq0KGT0m0yNeziP5EOUcHuaF-fpBSK0srBvIDv4wFH8vzxprFBl9PoOqiZTxezjazoNXHCnPthMHUvOo0g9YRUpnw1Sundk3R1gQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
🇺🇸
پرزیدنت ترامپ درباره ایران:
آنها به ما گفتند: لطفا در مراسم خاکسپاری ما را نکشید. من گفتم که این کار را نخواهم کرد، و ما هیچ اقدامی انجام ندادیم.
و سپس آنها به سه کشتی حمله کردند.
@News_Hut</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/news_hut/67526" target="_blank">📅 17:19 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67525">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0e9aa8bf24.mp4?token=o30Q-iwK3pZSt7ypuGTa4FFIiQ1j11F_nM7MUjiUsjHyENE26Oqj3Geudh-KouYl2gmRQNzndVRJcoej-Uaf20YbI_J_PKWxM0zpc7VoJWNf0EJIOVpdheadUBRSexM91G4xmrm3DjyeRnZ3GKGdwKXG5i5eAxv1HYvnJm9iH84ucqMvjVCddeAhlRkAv8S0_K7lWNyeJTfY9VdFt6t0njjQsDCQ5bn5nCS3UO6kqtpFkVyQqB-IZTGe6HAG664JKbMfIGfgwjDW2fg2f1BfHsbX-iRbQFyRTfTZtF3yPWItSUE7lgUY8W6JILf8AV6BmRYHuCFLmI3t2nS5RZKH5g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0e9aa8bf24.mp4?token=o30Q-iwK3pZSt7ypuGTa4FFIiQ1j11F_nM7MUjiUsjHyENE26Oqj3Geudh-KouYl2gmRQNzndVRJcoej-Uaf20YbI_J_PKWxM0zpc7VoJWNf0EJIOVpdheadUBRSexM91G4xmrm3DjyeRnZ3GKGdwKXG5i5eAxv1HYvnJm9iH84ucqMvjVCddeAhlRkAv8S0_K7lWNyeJTfY9VdFt6t0njjQsDCQ5bn5nCS3UO6kqtpFkVyQqB-IZTGe6HAG664JKbMfIGfgwjDW2fg2f1BfHsbX-iRbQFyRTfTZtF3yPWItSUE7lgUY8W6JILf8AV6BmRYHuCFLmI3t2nS5RZKH5g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
🇺🇸
پرزیدنت ترامپ:
ما شب گذشته به جزیره خارک حمله کردیم.
ممکن است کنترل جزیره خارک را به دست بگیریم. هیچ کاری در این مورد نمی‌توانند انجام دهند.
@News_Hut</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/news_hut/67525" target="_blank">📅 17:18 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67524">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/204bddd9b7.mp4?token=Isse0qtXLiQ2iDkzqu9nGkTIOrFUdj-ZGSLiY7qP6JWA5yo0aH5j4MJL94tEBqiIIS5RpudJ8pNJ4kXlHsG_eckTxyLM4bPva2WscSC8f44QS9ansxMCkwT-dhtpKpiiIadZc4x7t3VCt8iEfe92mna8ivbGdw--JWUwN5iSPjzte1SkxBbUhc1_Z5PdvcSVyShljdLqX5HxpzrDbPOWMkhv5FoNlp1hckLhhvi_krlg_Q5zESIk14AZTpRJIFghXKAG_onhJO1bpmsQSTJtr1xF7MtRbJRYOFa4dHatSL0aCS61dLs2sXtO8x7FL7S4DxVd0iBEQLBVivJHlo3o-g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/204bddd9b7.mp4?token=Isse0qtXLiQ2iDkzqu9nGkTIOrFUdj-ZGSLiY7qP6JWA5yo0aH5j4MJL94tEBqiIIS5RpudJ8pNJ4kXlHsG_eckTxyLM4bPva2WscSC8f44QS9ansxMCkwT-dhtpKpiiIadZc4x7t3VCt8iEfe92mna8ivbGdw--JWUwN5iSPjzte1SkxBbUhc1_Z5PdvcSVyShljdLqX5HxpzrDbPOWMkhv5FoNlp1hckLhhvi_krlg_Q5zESIk14AZTpRJIFghXKAG_onhJO1bpmsQSTJtr1xF7MtRbJRYOFa4dHatSL0aCS61dLs2sXtO8x7FL7S4DxVd0iBEQLBVivJHlo3o-g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
گزارشگر: آیا امشب قصد دارید قایق‌های بیشتری از ایران را هدف قرار بدید؟
🔴
ترامپ: معمولاً این موضوع را با شما در میان نمی‌گذارم، اما می‌دانید؟ آن‌ها هیچ کاری نمی‌توانند در این مورد انجام دهند، بنابراین احتمالاً بله.
@News_Hut</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/news_hut/67524" target="_blank">📅 17:17 · 17 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
