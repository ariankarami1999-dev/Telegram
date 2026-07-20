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
<img src="https://cdn5.telesco.pe/file/azStJDTFKUSNZkWUALg_zugCGkUySLRdgeTgKzlE7R8oCOp5WZ1gNsKtQkZYrIAvC94oCQdQLCdVa2QDrnNnvYFtbD1qtrX3DV6sVtRukGsrT3Tuy-Z9XFX4OA0ocfc-2V9x5Qqnht_-NKvErhMHitUpLz7Q1ijfi5fMgQuH8mDqwINJhsbWE9oFv4lEFEwknpsZERVhUUO0pjmrPdVp7v1AoIViCfIIdNjxxlCYaxXsHLpQzaAXomXlyOAaY3HA8abqIfwhYb5lDZ1Kew3TwDLmwHsmCdkrvAVeBbprKtX-dOHXop0g3soItUznqNZUs2TTFZk29Ly7SkxLQgPz7Q.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 جام جهانی 2026 | فوتبال 180</h1>
<p>@Futball180TV • 👥 552K عضو</p>
<a href="https://t.me/Futball180TV" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 In the name of God; The only popular sports channel on Telegram: All for Iran...🖤We respect the copyright laws and follow the laws, Mr.@Durov...🙏🌹Contact ads:@TivaAds</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-29 14:49:00</div>
<hr>

<div class="tg-post" id="msg-101318">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FwXKJa6JFOU9Recr8_K2QsYlVVxfyEd2rAW8DKO9fwG2LmCzohE6oZevXS2DhYA7RDrwUvaaa3OQuk7RLIXt78MBfUy1_W0W6ZULXMk5fNfSd-SJU2Jaarxs643l59xbMpSds2f5XOmU7GTqvlW6V7MVaFUwMMWq1gbsP6wazT8riQbiNLMbr7K9WYKcSpfLHT3QxOlnmEdmnE4PzV3mvP7-KmuniuwAqi7j0m4m3kVfh_J4b1GOYJ-9gz4CFep4VxzMNol8c1Zp7qN0RaySzVTmdp55prxESerQFagFh0mZlIHf2H-Ll3lVqLXG-JgCL3qj5xXa6q2nfK2CPvT8_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
کیلیان امباپه در فصل 2025/2026:
کفش طلای جام جهانی
کفش طلای لیگ قهرمانان اروپا
کفش طلا لیگ اسپانیا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 1.53K · <a href="https://t.me/Futball180TV/101318" target="_blank">📅 14:43 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101317">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">🅰️
🅰️
🅰️
🅰️
🅰️
🅰️
🎰
لذت بازی در کازینو و کازینو زنده با 30% کش بک بدون محدودیت سقف
💥
تسویه سریع و آنی جوایز شما
💯
اسلات‌های داغ و جذاب از برترین برندها
📱
اپلیکیشن اختصاصی با سرعت بی‌نظیر
🎊
وقتشه با کازینو یک بت، برنده‌ی بزرگ بعدی باشید!
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
<div class="tg-footer">👁️ 1.53K · <a href="https://t.me/Futball180TV/101317" target="_blank">📅 14:43 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101316">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u1S1xL4LngVTeJGnozEXcGRF2cYr_wO66LIUmrP4NJ_cHvlHFXuAe5QA6TdU8EzAdvUsmeacW-1oC8oiSskaLM788Gt1OWajMAEzAEtccuWgj8D5g0Vv-F9h0lzJTn1HDha2mlN-co-5xB4-YMEcXVnp8xSgr-5RQ0kAhkRwOQrt5YT3og7RKh3hbl3UW1nd6jL8J7VtT5JyzGT4wY6sdnqOeRmPTnEzfhqAgWW8bP_6gVdeeRv_L0857jOPSwRgS9BybAlO0zhUcTigGRE3_GedYQ6H2d2pIXidq0NNO5l0r5kCKYpB3zzqXF31gBk99WGTvjts03gVH750C17ETA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💎
سایت پیشبینی
YekBet
💎
🌟
کازینو آنلاین، دنیای هیجان و برد
🌟
🎁
100% بونوس خوش‌آمدگویی به مناسبت اولین واریز
تا سقف 100 میلیون ریال
1️⃣
لینک بدون فیلتر
1️⃣
ورود به سایت با فیلترشکن
📲
@yekbet</div>
<div class="tg-footer">👁️ 1.53K · <a href="https://t.me/Futball180TV/101316" target="_blank">📅 14:43 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101315">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c6a9e5cdee.mp4?token=Oqy95XQaKTJEW_3OXAlu9aXWMF33nzTFqXW45CzRK1xU3VjUPWanq0mkKWuy4UHkrNDygt2xe2XyZXXVULRSKirIyHaTmoZ3XzoWInwJ-FMcu14eWFOAUp8EiUVb4BrJRqYEiIn0k0Vl1HXhCCa_klgzjsmfm7sLdZBv8540Iq5nFfGibCh7xI-hJyR9eMaE0B-iL6QETkuLnXH4bObPAf1Nr4_Iyy6BlfOXSagPl5RPkM4n2KeCmN9a61DEmRh9ER87kS7Ocu232A1aICK82ZdmCcx3_feIG9khBUT4Yy5prwh5OEQIaw93lTmKdbJ-NVX9TjsTPFb3W3doBOleLA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c6a9e5cdee.mp4?token=Oqy95XQaKTJEW_3OXAlu9aXWMF33nzTFqXW45CzRK1xU3VjUPWanq0mkKWuy4UHkrNDygt2xe2XyZXXVULRSKirIyHaTmoZ3XzoWInwJ-FMcu14eWFOAUp8EiUVb4BrJRqYEiIn0k0Vl1HXhCCa_klgzjsmfm7sLdZBv8540Iq5nFfGibCh7xI-hJyR9eMaE0B-iL6QETkuLnXH4bObPAf1Nr4_Iyy6BlfOXSagPl5RPkM4n2KeCmN9a61DEmRh9ER87kS7Ocu232A1aICK82ZdmCcx3_feIG9khBUT4Yy5prwh5OEQIaw93lTmKdbJ-NVX9TjsTPFb3W3doBOleLA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
دونالد ترامپ دیشب طبق معمول صحنه قهرمانی بازیکنان اسپانیا رو ول نمیداد
😂
😂
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 2.44K · <a href="https://t.me/Futball180TV/101315" target="_blank">📅 14:40 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101314">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a12a251e59.mp4?token=GEFeGp39KQ6EsMkvTtb7NIcF4JN3yW13ERQmZbEk-0lIvUi4_Ubc6j6rVuQVJFrRuoGWR1JTN4fTq5zfOa2UJcgh3qp_SISxbaj0aFD0WwJskaKiHZwcDjyyu0e2Wookwcsp-xtLGKc5ACi1AzOMXLq9DNLZQp9Soi4HUc2Ow4mnRAjetzW9J3J8HxRseES6g9qLcn9tK7q787X2HozaMWJcBQtXVUZiFPnss8aV8Kfx1yEqLSZONtEDjTvhkGA6ACl9392T5A4q-zSbAma7ffvVHiB2jKCSXhd60mRFVlWjhmmsOXua9HwUddxw_jDwQuLqbik8VAj6hXyba3pyWA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a12a251e59.mp4?token=GEFeGp39KQ6EsMkvTtb7NIcF4JN3yW13ERQmZbEk-0lIvUi4_Ubc6j6rVuQVJFrRuoGWR1JTN4fTq5zfOa2UJcgh3qp_SISxbaj0aFD0WwJskaKiHZwcDjyyu0e2Wookwcsp-xtLGKc5ACi1AzOMXLq9DNLZQp9Soi4HUc2Ow4mnRAjetzW9J3J8HxRseES6g9qLcn9tK7q787X2HozaMWJcBQtXVUZiFPnss8aV8Kfx1yEqLSZONtEDjTvhkGA6ACl9392T5A4q-zSbAma7ffvVHiB2jKCSXhd60mRFVlWjhmmsOXua9HwUddxw_jDwQuLqbik8VAj6hXyba3pyWA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🙂
🔥
وضعیت کریستیانو رونالدو هم‌اکنون:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.5K · <a href="https://t.me/Futball180TV/101314" target="_blank">📅 14:20 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101313">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d483e9b5b0.mp4?token=eoBUJ5AdG48ixUm4a3weYVSQnwpxNKLSM8xfqdJZi-WKNJtr_NVmaiwrbJerInkpc06T_xOiG04K1vPpsBOt9i6SXMWJs8Fa6HNzXOd-lTW-d8ygVF9e0bYwuSKTd4MnyaK6NQ0G_gpA3F4TTTi5w_Yt5e5r_8vLwqzByMRvDHznj2ROl3wLwnIuzHJd4ywo2vjqU7uKNZtBcr1t10z2g1xtX_VQCBgn1mPPouisZVyCPZdoEWwOFCxwo768WXg-aMpmnolSmQLuXCDKEkM4jkHl8tTUtkYs7KRl--Fi-HbZ8WOeKYzTrZL5yVsYG8-vSZzTPm3hkEwqTaCNtmzSXQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d483e9b5b0.mp4?token=eoBUJ5AdG48ixUm4a3weYVSQnwpxNKLSM8xfqdJZi-WKNJtr_NVmaiwrbJerInkpc06T_xOiG04K1vPpsBOt9i6SXMWJs8Fa6HNzXOd-lTW-d8ygVF9e0bYwuSKTd4MnyaK6NQ0G_gpA3F4TTTi5w_Yt5e5r_8vLwqzByMRvDHznj2ROl3wLwnIuzHJd4ywo2vjqU7uKNZtBcr1t10z2g1xtX_VQCBgn1mPPouisZVyCPZdoEWwOFCxwo768WXg-aMpmnolSmQLuXCDKEkM4jkHl8tTUtkYs7KRl--Fi-HbZ8WOeKYzTrZL5yVsYG8-vSZzTPm3hkEwqTaCNtmzSXQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💎
The end of an era..
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.81K · <a href="https://t.me/Futball180TV/101313" target="_blank">📅 14:15 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101310">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KSI3M2rnbrfnwAag4iisiJtBdhOI6e3lBDXGvzClKdMeGbLkVfaVojI5ZlvyYNmmGlXp50aTAGRwMVN8a-BUBccT8ghRCy-hvQbup-R4brdWiDozdLxaHFMN1GZTnJLghKs_TTDVEHLm8ZBrHnwMD3dcfls9F2KDJuZYRMtBifL9OuZJewXsX2uSTmITVEoAPWPS8Fs9_rMGyt-gIU79eA1miHaJWTOBODpcSfXE_cbesGVVsS4MELS4QvjVuUSUdq5CJ_rio2RfjtM1WkFdIf5eVI0MtfQ8bre8oXx1JUPUfYnJF22GylT0AMBNut4-qJNwDe47Br_dr7KPZTkEAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ke-RdnBeRH3Sg8swG2Qnb3sxT_kEZaQUsKa5SCiT2ztkBrm1VWNAld3_ihI4zonQSkI0GnXCWtW2doTulHMRjpAfbMa0_v-KlgRowthEQQblQSzg8rJ4MqVvq2rUh49a1AuLKIjEndkmBuaYlwh-k4v6MfXdnGNpcIx4QuXgtyZ1CKnZzHWUohy3NfNgb-0EYMY3ozT69oGl03WetwpkqH3GnBvTemTJVq2ZR3PWaqZysuzU7nYIRCZJa6BJ32AUdViXUdIM6jDFUoiZOS3nmrIa_FDkN9WDPhI77aFoUVEFSY48openyasfTpdcYJH5Tdo9jPr4Vg8CmldlbjVkxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/h6w1M5X8uKPE6xFxA3LkAoxUzYBABCw3tlONno5PS7dE8tZTaASINyjzWoPuzcoTI8Q-_IAYejggEF_1YMLkY38T-tZ35otM1cbZuZzzzDgFA6GB9IO5OqIf_jat_7p5kTZpQ7LR4v4kyrDYwSiv330Yq1jygK9JLnll6GWiqx-ZTj6V3IM-q2OrlGDqD9lveXWqLjOyDnE_Pm0RJ78Oq62Bu35694LisBsocwpofYIb_PQMsGNLEqrKe44Rj074iXao0ipuBu4XoRpcDyWGAr3G1lCDXY9x6qXoyepG0J04euMMHKLoPkU3JcKavG5CnPsargKdBmmBSUtDIftReg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">😆
🔥
کوچولوی دیوانه رو داشته باشیم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 6.72K · <a href="https://t.me/Futball180TV/101310" target="_blank">📅 14:07 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101309">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rGKtrkTbtstCFHxhmcyDgOaa7Xx0UML6MKwIFRgZ2dc4hZGVfY6t_U5SC_zfxGL-CDIJZjdrtAxn2_FnzFrQOP41p2b0kzSGlkXEPMVXH9R33hDFpGteEqcA9JewF15Exu6Atnfy11e_oho_6zxRkBuOt486fMFYJn8-M629xaA-JKvFeE7Og9TM0JVrd4Bk3ryjgeeLXHhrRW8tFkfKAnUmhi7CrwbGqqeCV1H9QDWKuhy-hqc26MBjiicJORchAKoK9iySv9cgSybR9pQVRfUCdAaC3pbpJi4T2_8MktOpoKoFjLHcsDuk-tuaUW3ujvm2YOrJOc1-NRiMl9ZmRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📆
😔
🏆
تنها 1420 روز (34,080ساعت) مانده به آغاز مسابقات جام‌جهانی 2030 فوتبال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.95K · <a href="https://t.me/Futball180TV/101309" target="_blank">📅 14:00 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101308">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/367be64c4e.mp4?token=skY-rrVMpHuH663vmg1GVEyf0IkaqdUXH77vd8YAX-NXVZy2c_eySdfR6c9NMhTHCN_XBIawVXL2dt51efwRMtwqv5pyioyo-MKxjnAxrlvveWoUEz47PkWOmwdJgpnLAiIjSM9zlV-pSzbit7zFd8QSpfzIOqq1E_Gtt3qi52AW9R82Np5M434nWeg4CU4rCfnDabnU1nUUGn8f8kRdMLteHorXgWfV7_6UgGcGzofCdh1LNk8XsNCSCLGxQ7fYwS8PsRTFCvsB9M2IOrCpDAbYUUFbv578izhyKMXKpDASLwFD5M5hA9zS0RrSJrQnOWRV6Har1Ml2J-cz2KnoFQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/367be64c4e.mp4?token=skY-rrVMpHuH663vmg1GVEyf0IkaqdUXH77vd8YAX-NXVZy2c_eySdfR6c9NMhTHCN_XBIawVXL2dt51efwRMtwqv5pyioyo-MKxjnAxrlvveWoUEz47PkWOmwdJgpnLAiIjSM9zlV-pSzbit7zFd8QSpfzIOqq1E_Gtt3qi52AW9R82Np5M434nWeg4CU4rCfnDabnU1nUUGn8f8kRdMLteHorXgWfV7_6UgGcGzofCdh1LNk8XsNCSCLGxQ7fYwS8PsRTFCvsB9M2IOrCpDAbYUUFbv578izhyKMXKpDASLwFD5M5hA9zS0RrSJrQnOWRV6Har1Ml2J-cz2KnoFQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شکیرا روی صحنه ورزشگاه، پیکه روی سکوها
و ساشا در حال تشویق مامانش، در حالی که شکیرا روی صحنه غوغا به پا کرده بود، پیکه از روی سکوها فینال رو تماشا می‌کرد. و ساشا هم با تمام انرژی مشغول تشویق مامانش بود.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.95K · <a href="https://t.me/Futball180TV/101308" target="_blank">📅 13:57 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101307">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b927fa3e3a.mp4?token=UM3Y3YNDfMy22v8P495cFWmND1-blbxrlawGkPfRKZDAH87EuuHhnPQJV5FUjxh0awlbssoCleJ6p9JA3TzCfn_IwGnHjrrOv2Y2pXRwsby11QgejcTiPbS1DpuVy9M0jzwPcGni_Oh_Ewb-YDT_LkTiIJYGHGAW7gNbF0PenMzhOqlE2z5baUyYBDdPLdtvaPZaqdP6Jr-txP6c-CgrWi0P-Y6n3vck1fSAVdu1DHw5dAY7okqGeYNzYA27nDGG6h84nTW8GcAPlj95Oy7U1j3yyH87ITP9rZ1HuAH42SCNv02TK_ooPSVrJ6Zx9xUUuM6gLheS7eQyhsGvics_YQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b927fa3e3a.mp4?token=UM3Y3YNDfMy22v8P495cFWmND1-blbxrlawGkPfRKZDAH87EuuHhnPQJV5FUjxh0awlbssoCleJ6p9JA3TzCfn_IwGnHjrrOv2Y2pXRwsby11QgejcTiPbS1DpuVy9M0jzwPcGni_Oh_Ewb-YDT_LkTiIJYGHGAW7gNbF0PenMzhOqlE2z5baUyYBDdPLdtvaPZaqdP6Jr-txP6c-CgrWi0P-Y6n3vck1fSAVdu1DHw5dAY7okqGeYNzYA27nDGG6h84nTW8GcAPlj95Oy7U1j3yyH87ITP9rZ1HuAH42SCNv02TK_ooPSVrJ6Zx9xUUuM6gLheS7eQyhsGvics_YQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
🇪🇸
اساطیر اسپانیا در هنگام گل‌اول به آرژانتین
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/Futball180TV/101307" target="_blank">📅 13:40 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101306">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AXYHOv50bVoLkep-qb3k3Ze4wEiPGIjz3QSijwBRdaDW6BBitBv7qovS9uoPCzueoc1u9nJR4uuJErY0sNyjrdyvQGN-erKTUpel3qX1dnM1JdgvlxiMljNoLrUi7tqev4op7ieNEPQa5d0_OzVa3593EfWJDBd89bE84TIfIvWiJlWI5zjLVIAsMiNBf-nBuFl-dKRNc-0-yuHNfRxo_pYeZcdhVDfqhlP-drUXbv_W3m0_Jxu0E6M7kGXeXEtoAiMDX37HbcyPNXaqqzi_A70SOrU6WusK2jMUM5NvROiKWQsaCWEWCXTloKYvpxsdh-DPueogkrKN_mdNyVLsZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🟠
رومانو:
رم در حال آماده شدن برای سومین پیشنهاد رسمی به وستهام برای جذب کرسنسیو سامرویل است.
پیشنهاد دوم به ارزش بیش از 45 میلیون یورو نیز از سوی وستهام رد شد اما رم قصد دارد امروز دوباره تلاش کند.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/Futball180TV/101306" target="_blank">📅 13:38 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101305">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/98cd4848c0.mp4?token=FpPgA5YIxia4ztIolNWI-tuaMIkHd2Cx7EC_HoS5et5Ehgon9JXxIqvml0HfL3jHgNuC6-PP4VF0ZON3XGSNrQnG_OeqCYgUlRxWcWS125N6cLRb48hsu6kF1dXZ-c9l32wx8znxrQ37Mk0-Ey1d0WWHg84qjmGYrt3cvM17n7308n9r655VeHAtuLWx2GoZqACLBJanbhDrRwdEL_4RC7Lh89-tJoXM_WXHNXqw62Z0QyqvQXLza42f0_rGn7scArQvpZKB1KJWRcvlshaswCFrnI8obSsC5Iz2JBpvQos1sSAyTnK7lPo7Hnk1Jt81jIF-ixv4st9TQarRvbxl_Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/98cd4848c0.mp4?token=FpPgA5YIxia4ztIolNWI-tuaMIkHd2Cx7EC_HoS5et5Ehgon9JXxIqvml0HfL3jHgNuC6-PP4VF0ZON3XGSNrQnG_OeqCYgUlRxWcWS125N6cLRb48hsu6kF1dXZ-c9l32wx8znxrQ37Mk0-Ey1d0WWHg84qjmGYrt3cvM17n7308n9r655VeHAtuLWx2GoZqACLBJanbhDrRwdEL_4RC7Lh89-tJoXM_WXHNXqw62Z0QyqvQXLza42f0_rGn7scArQvpZKB1KJWRcvlshaswCFrnI8obSsC5Iz2JBpvQos1sSAyTnK7lPo7Hnk1Jt81jIF-ixv4st9TQarRvbxl_Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
▶️
خداحافظی جواد خیابانی با مسی و میراث مارادونا با شعر مدونا: هرگز انتظار نداشتم اینگونه شود، برای من گریه نکن آرژانتین، حقیقت این است که من هرگز تو را ترک نکرده ام
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/Futball180TV/101305" target="_blank">📅 13:20 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101301">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kcYrkk1fMEOrWnytYoWHR9tWk7H_ZfFfARjGouiesdrsy4papnyiqC3UkN_rJfZCEq3Wc1BznLnu60RI1G_3xJKzGT3k68_L2586g7malFONrKKC-nXMf_kCPDUBhC8NzlTNwmAbcGXeOhb-GyIBvIyb2XYUMCE0CoxzJgpBlq1HZb-tCR1QDTeisala7n3lip1SDl4AVhmvmhq67nSNyYkI_TtS32T61G_dpZRA49vS7Uy0ALjGrLgCQfQuWfAaNrQGWF8-L8QDWNtIVMzio4HWTMn0DS0AhYUSRJAZXuNmJDrsu1Em5x9fAQHGyXPOtDZr6jYpZiqWKfiZCRnARQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UyvT3g1IZcMeguRyse6R2DilUiRM-Foh1fLmslXRvBgBBuNBerPipBIXXKlhJJXd4Kzfd6mMKZo8QpaPvwFg21cYFvw37xj8YO3HyypqX-R0xu6CJxMq4z1U47GOaErlTDtyN-r5u2oDfVX8xsEmUjZ0ZK6wxoaQB4KCrrL_U7FHEfYuHcJOlanJPxSf0fFGlCdCIt0sDoq7MnoUfEuPGr35xJ2LPtHtdkn-FTg5P2Qv1eLHndiKf7NZeHCggc5Z35Ox4UyvfHmvJy-xOlPq4xzRGnn25xPh9luqi2961-1AtAlYPdKoSz_zMRwk_-_O3Doa985-_r81Z8IXBsRbqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WmeCdKuptVleB2k39uy6CgkaTKL1gaFr9Nb-IqXI6jhvx5ej1uXSj0GK_DO2iswbspwaqWQT9ZoZD6dBkqA-UTppeuQJU008pVeW3xzI8uri-AvIkRYHM2dauJjIRcrvSMdJKg7EE9lKrpPyrjOvNhFt8_RjI7WdeP32LQT3jkmVZPK58lVwheUJ95F53FHs1jqiYC2Vw8SucU3ALn27y7xWXsOeQktAuLsPypp7Rjn95ed8_y_x7VUXyrCl0PgbAaYziS2aRhkEIoR242kfFNlBY8E-gV4dfW7gkPPTh1qEGpzg7jhKe1ypocfB1C371inAIpCsTnzJ8lc273YLIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hEaPK_nMydDIZrJtnVAtuKQEX_w_B-By0YTFhKTSLrYtoYzdWKeluXUTkYCTcJlYEWDkbQmJlROOKtj8MWM1FcFyKYQWEC-PAgKja5HD30tswGOMR0HPAXsVpHsfllTDE882dlBzZc-pd5_amQJQHUTkB6YoZGmunF3XibBIoCjkJahHEBQcTy8ehwhFdb1HyovQxTKm3a3PnZe6-RcX7e3KpTIMcMzMPscojizHYyFDRNDozc4FfdijXFvgVMbItJa6NzMym2KpXkZOxG-2tt4sa53hpHWwT0ggfg1kglrBRlsm-BY5JGx57U4sPPOOK3OHwNEvePVcWnbzZgb4sA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👀
👍
پائو کوبارسی ستاره ۱۹ ساله اسپانیا و زیدش بعد فینال دیشب
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/Futball180TV/101301" target="_blank">📅 13:04 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101300">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ad81ee87a2.mp4?token=vU3ZyT6sFDqQfH5Qn7AlptiIP0c5_3YfvT0ujknm0TjdtvsWRF3xsjQdoIdbPatkm0jpIeXo3kKoH7uxbKF4YrquTsGbieBen9YPPs39aj7KXHoLZES_vIj_x558Nk8psLeA6_j7WGl-jw7FUbxZWa53cSQ-p3THlZrN97eKxAff8tjQESQ3iLiPqSZ3xgTjNyshuhArFXBkG4QvQ7myPoQKnkBG6E9Vq9t7FdvhJKuM5WwpKgkwVx6Y1qo-7vV5H0sErjHGHUZCiKj_lAlELteZ81xOLGyn95qWZAnQTYC-Fn4oPU39rQLm503UjRnGyZ9Run9y9oWQoRnkDcwuaA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ad81ee87a2.mp4?token=vU3ZyT6sFDqQfH5Qn7AlptiIP0c5_3YfvT0ujknm0TjdtvsWRF3xsjQdoIdbPatkm0jpIeXo3kKoH7uxbKF4YrquTsGbieBen9YPPs39aj7KXHoLZES_vIj_x558Nk8psLeA6_j7WGl-jw7FUbxZWa53cSQ-p3THlZrN97eKxAff8tjQESQ3iLiPqSZ3xgTjNyshuhArFXBkG4QvQ7myPoQKnkBG6E9Vq9t7FdvhJKuM5WwpKgkwVx6Y1qo-7vV5H0sErjHGHUZCiKj_lAlELteZ81xOLGyn95qWZAnQTYC-Fn4oPU39rQLm503UjRnGyZ9Run9y9oWQoRnkDcwuaA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شما با دیدن این ویدیو یاد چی میفتید؟
😆
😆
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/Futball180TV/101300" target="_blank">📅 12:54 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101299">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Qpwg2MyBwqDN6jC7IQY82S3Obh4gDn95PYcKJFnB2oj_ky3YBnPLWs1Ze9Edznq_oQUjYWyBO2ZtaDPqjkdhzrqwTjYe4vkfF5omRPl5k1w5xzbtWYs9EZ8C38mHEgu5n0XRuF-892v1nPPzmyF2zC4U9dSp6oqmgRX3225eYK1arANh6sdP0WjWV3Rk1CP3_kykJ6_Q8ClQUh2wIFFCVQ6Dp1-xBZEV5z2cur9DRc7SV848YQsD1VYcKYvNFt1AuRb5TsFhLWelvEcvA42xCXII__wAEVU9gx3gLWGkhZjG6AaXCpXcg2oV8LIEL_xVsaPETxAih6a_CiZSKgHw6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تو نوزادی مسی کونش رو شست
تو دوره نوجوونی کلی جام با بارسلونا برد
تو 16 سالگی قهرمان یورو شد
تو 19 سالگی جام جهانی رو برد
این وسط هم بالای 10 تا دوست دختر داشت لاس خشکه میزد
این بشر دیگه از خدا چی میخواد؟ چی روش میشه اصلا ازش بخواد؟
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/Futball180TV/101299" target="_blank">📅 12:43 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101298">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5934b1abe1.mp4?token=U1-NiThxVxsiJpMtAfWANJbVRcCFJ47OitO-F03hGLyzZ_s5Y-GQRNaTth9hdC69VIGJ9zU8qiOUSsZtFmcZNqoOJwfgrO1-2lRNC1Z0OSjb_KHc5OCAzYvlj5ko9RHBWtdIlSqeEDAulkEG2omMpugVLifq1l4gUKBmNas9CU-Qio1h9OBEDbQnTLjdTW2gqLveDGYCHLBmreA3HtVZCMzaKKLWlPoYa87H52OtkOJ2BUKIyIOxJo6gMPBGQcis4AEDmjnk4dHLiJ70iw7O902qqDtyZj1OjtKr6AEoKK4PlSdE1dMyGZpc1xIUjaY38nAFkxdtgiMIbBrW2eoi6HjQAXDlq7FwoJnjlXQR-1p_MSzKbXDPWTYU_y0frpBgRSGOPOOrKA4j14XMqYGABgP1RMehALpk95PAg3t378l1ShMq7KXQE3WR50VLMzMQTcHGsFK8aYwM234Oe4vcCxN_yJdVUXkrZUUQdMGH7cyG7XGWJt6nT_MNu7h4wM6QQAbeNaaYYKL_A06gwTyqXuPqIKKGQE7xIKZn8QXmfV_79HSpIQYAEEEF1OP8yuR4jj5hizsQG02jvY5G7_tYRj1dkmifT3ihq8DVUBT1bhJvwF7UT-EJkfsPT4qeSjwtHPnSXpGLyn0epclEqCa_Xtkms1bjwqWYvrlnp6Tsdug" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5934b1abe1.mp4?token=U1-NiThxVxsiJpMtAfWANJbVRcCFJ47OitO-F03hGLyzZ_s5Y-GQRNaTth9hdC69VIGJ9zU8qiOUSsZtFmcZNqoOJwfgrO1-2lRNC1Z0OSjb_KHc5OCAzYvlj5ko9RHBWtdIlSqeEDAulkEG2omMpugVLifq1l4gUKBmNas9CU-Qio1h9OBEDbQnTLjdTW2gqLveDGYCHLBmreA3HtVZCMzaKKLWlPoYa87H52OtkOJ2BUKIyIOxJo6gMPBGQcis4AEDmjnk4dHLiJ70iw7O902qqDtyZj1OjtKr6AEoKK4PlSdE1dMyGZpc1xIUjaY38nAFkxdtgiMIbBrW2eoi6HjQAXDlq7FwoJnjlXQR-1p_MSzKbXDPWTYU_y0frpBgRSGOPOOrKA4j14XMqYGABgP1RMehALpk95PAg3t378l1ShMq7KXQE3WR50VLMzMQTcHGsFK8aYwM234Oe4vcCxN_yJdVUXkrZUUQdMGH7cyG7XGWJt6nT_MNu7h4wM6QQAbeNaaYYKL_A06gwTyqXuPqIKKGQE7xIKZn8QXmfV_79HSpIQYAEEEF1OP8yuR4jj5hizsQG02jvY5G7_tYRj1dkmifT3ihq8DVUBT1bhJvwF7UT-EJkfsPT4qeSjwtHPnSXpGLyn0epclEqCa_Xtkms1bjwqWYvrlnp6Tsdug" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ملاقات اسپید با گروه BTS در فینال
🙂
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/Futball180TV/101298" target="_blank">📅 12:40 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101297">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/242475ed92.mp4?token=g4aaZ5YMb51i0AJF-u2Vu3W-LZ28XH6v_woqCIDHJ4sct3qwpjfDTCB1u7X8pb3XGiL7YkNVgrxRkMxlZBq8j_JdI9HFrrqrmOoo-GUSXalhNtihNcggwJQpqEvpjJyWtV7wkZXDK30iGOjKfbBoLfN95UrXehjAf5XenDBG09cEYxco7hyVHJ4tozzrw9QYOvidyZ4Pgk0IARpjXlNVjfIcQjVn8ON3sCWhBhZDiQeAqZI_EmRc8J5TAQBsR-kfxy5-M4kG9Xl465y1ID-DFApE8VL37hGgjSf4E8jeWKYw1dtzv_V-YXdSJhwXQc6UxeT8xYnIzfYwvSiNNbmEzA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/242475ed92.mp4?token=g4aaZ5YMb51i0AJF-u2Vu3W-LZ28XH6v_woqCIDHJ4sct3qwpjfDTCB1u7X8pb3XGiL7YkNVgrxRkMxlZBq8j_JdI9HFrrqrmOoo-GUSXalhNtihNcggwJQpqEvpjJyWtV7wkZXDK30iGOjKfbBoLfN95UrXehjAf5XenDBG09cEYxco7hyVHJ4tozzrw9QYOvidyZ4Pgk0IARpjXlNVjfIcQjVn8ON3sCWhBhZDiQeAqZI_EmRc8J5TAQBsR-kfxy5-M4kG9Xl465y1ID-DFApE8VL37hGgjSf4E8jeWKYw1dtzv_V-YXdSJhwXQc6UxeT8xYnIzfYwvSiNNbmEzA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کوکوریا با نایلون داره جام‌جهانی رو میبره
😂
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/Futball180TV/101297" target="_blank">📅 12:27 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101296">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2c93fe59da.mp4?token=OszNyOe4N_rrRXbpOgfBcQ0oOSF00fM3r95AbPRJGfQoolSLs9ncq2esyzCnTIFaCCt6j9OgsSrt4yHElQ4pPgIKYS4TlLNqmDl-ms_TPI0chmCFRUxQmlpS4gNmGnyp6Co5ieMkGaboBGF8YAobfCguJD3AuHXky78nqNVKSeWXtAc3BJALxx4vCTOxQShpgwPsn56e8RKrlMDOBfBOUinIXtpu-FSxa46QwK8nT0BBoTKnccVmQIZkA5PUKYGRSFna87q1UOWcS02J8DZ8aHCCZ0nblHG5TYVbhWZZ7Gi4I12hS-PtNdEZ3FCSQ5yc_M_O_u47Ga9rGUsurIL8Ug" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2c93fe59da.mp4?token=OszNyOe4N_rrRXbpOgfBcQ0oOSF00fM3r95AbPRJGfQoolSLs9ncq2esyzCnTIFaCCt6j9OgsSrt4yHElQ4pPgIKYS4TlLNqmDl-ms_TPI0chmCFRUxQmlpS4gNmGnyp6Co5ieMkGaboBGF8YAobfCguJD3AuHXky78nqNVKSeWXtAc3BJALxx4vCTOxQShpgwPsn56e8RKrlMDOBfBOUinIXtpu-FSxa46QwK8nT0BBoTKnccVmQIZkA5PUKYGRSFna87q1UOWcS02J8DZ8aHCCZ0nblHG5TYVbhWZZ7Gi4I12hS-PtNdEZ3FCSQ5yc_M_O_u47Ga9rGUsurIL8Ug" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
👍
جملات عادل فردوسی‌پور درباره آخرین بازی لیونل‌مسی با لباس تیم‌ملی آرژانتین
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/Futball180TV/101296" target="_blank">📅 12:20 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101295">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bE7FWcM0I8dJey0Nu7yIcqk9jBL0gNC-whKKhmR9TCnPXx84WvD_Q_2O3Twmeh2iVjj5DBp11FWZWceS-tm-dE8w7DNCw688IG3XrkmFZfmPUUyvzyU79U9iNYeJKZfKRHBkvMeMekmdUtPTawbKTyPqMsG6HHVWXBdyfYmpwSlvu9h1BLTIa3knFNwHovQJ1eYpTNUSLnqBKKpiaFsJgMJRGqFgayeYSK-l7OoaThrXE0qjlGhP0J_R4LTnfp7VMPt2FfBt9dSjQNmcUOi5-6gsf2xzH85-wR6tTxx-o42o2A0dRYfl8T6ORmxFOTC80Se1TLOSPEuoxN3KAyHZnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
⚠️
😢
امروز امتحان عربی یازدهم بوده، توی امتحان بخش ترجمه چی داده باشن خوبه؟
فَشِلَتْ خُطَّةُ الطُّلابِ لتأجيل الامتحان
ترجمه : نقشه دانش آموزان برای تعویق شکست خورد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/Futball180TV/101295" target="_blank">📅 12:15 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101294">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ln5jV3xM5HwlD_1Q_dfaWdh1YOkBfGXKUCvZKOAp_c98M5ccaHXRErF0LF2XVubK5EHhZ5B6GREVeUDItBxrPLI3FjaPAIDFgrJWikHaeusHEfP0VBxYJS5nBZ180EgQJZycqr-VGCwxklRHEzmGkrE-28Bgu71ksAD0y4dauCnuqYmKAAI-J6UNZxmpFutYpm8CHxWKlGkAmRRjSmSnkblawK9RqvB6uYpoAU8EfNNsAbaEWv73ALSGNMbhOJe9WcNHNhjvW_qz_YUVic-qlL0_NVxPjM8wYkyWaLLLbX_NHWr--AUizbv6jdHXHdVK3MGKHqcdUjBbH97yuktW_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
👍
لامین‌یامال و بانو در مراسم قهرمانی اسپانیا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/Futball180TV/101294" target="_blank">📅 12:10 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101293">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v9dRi6G5upGGG_GoS7ja0PtsFmDTrqg031JS_uBICllsY_SYiHFq96Ez6y3iivXOdF-Z-LqrMmALXewh04nNsCkY-RItHbdu0SuX3z0ngJh6XVO_cbwwqQf5NukFC2Y2F8FkOc-AhKOZ3oI5LkoxoFDoQaIAbfwM_ZEZhv78mQC3VhZJ9oFtozzDhYF37Cv9B88nSFlj75Hz4aau0rHM9pds27VZpEWUOowfjD25GlrCm1i_M7qXaBnk1-RH8rBtE4EaIiEpayPhQSUGTf7GAXEFiNNxM7ZBLV5eA5hx0wy0Hcz-MLq7DK2DjVX702nxpcWKdpEt1aYRT7ViQzkKGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
تیم منتخب جام‌جهانی 2026 از نگاه سوفا اسکور
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/Futball180TV/101293" target="_blank">📅 12:06 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101292">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HTahRu3vG45Ezwt1_th2QSzlub0gNsN3csR7JB8-0uyP_5LXYjZ7HuvQ3V2tVriW1U0J6mx_QMq6iKrok2ttagcevho44C2bIqh_xTcQGVf8wGfzTJwZ7xYpkdhrA6cKc57FtCCymjJ-4btjG97s7mkVO2OpzhLKg8vn0arKd5B0RBhRGn-wGF07zCwb4MDTU1lRAK5YXQDsjjdZi2T0nE14YUbEZNwLuSHuHObOqgQya7j1i-dZ89t3v667-zAFDzI6OU6I383cdT8BRlNMn_XbqgCeFD1TMAhIrJAvMBowuu95CM2556-EmPzlwFFCTWraa_SIuVn8tZ9HoL2fHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
وبسایت سوفا اسکور برای دومین بار متوالی پس از جام جهانی 2022، لیونل مسی را به عنوان بهترین بازیکن جام جهانی 2026 انتخاب کرد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/Futball180TV/101292" target="_blank">📅 12:05 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101291">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Su5_htAznFZ0z_QE0hPfDkUkR8c2VHFwUXZ1EQlOCrTkZ3V33Oz9uPgGntdiQdlr5nISKRVy38_JSPsXL82cgYkNyjhfm88ER3hqrn7YiurMv2DjJNRy0WDQ0bRiJIw-IIAyof_yH6KBINdq2duGqhhSLtbyPsn3TaV0AFIJCzS5N3Fo-W1NrMzc1lCHRbKyXPoGGQfpd_slWV4kRrlVB-v68XWXGW20-bakLn99JSf0610wQSJ0-cbmy7bOsXWKtSnEWD7GihZ1zSF4WVlfpU4M8zEdfzr9tl9t5wJENQsegZ13N9oEyb14jRwk_AtneXmg7gQ4cc0uy8JxUlu2sg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇷
پرزیدنت مسعود پزشکیان: شادمانی ملت عزیز اسپانیا، شادمانی ملت و دولت ایران است
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/Futball180TV/101291" target="_blank">📅 11:58 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101290">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/06fa95c026.mp4?token=AT5HYEIyGc0TlI-c7wdF7UW11YJVb1XwANDRPwj82Sf4QA_mFbfaosoLkODiv54xCJ_XvRqTmA248M0_k1xKLjTUCUg5Q-N6w1hy77eakWuRYCCumpwbocEn4jW-juUlOnF3D2AHDFdKJRQNJwbQCRSBB-4Wbl_yLvmgwAyjSwFDRKBtF8IXOi2g4ddRTpt9dgt-RkPv2Y2uMIOg8PSYhU5JQWGu3ry6BST-nw1bazBPR01Z4PU-RdraNbmNdw7IXsTQp7y2klHCzWn7ele45OBiUl8uYre3mQhrIYYnNpy6RPcLjP5bKq2jaDDvC7IFwy2ccExbiBkYorvNhoJH6lVqnawsi-ZNeM1BKjeRzyrDK-DCjLdGb2NdHXz59aELOzIktiDD3Rt_LJlJUQH9l5Xq39SfxyASB0iEFPzEuCQISnrpqpGl_vZzawZfIrEWn6AvmO4anK4PbhpUmlqfpjmFfPw2ypY_c_WsAPFasTSyxGbB7LnibKAw4FTHrTlZnKrs_4FdSLrVbHjE_WnHN2dXrGHBzo7hn5HaK0VY6EJcfrHFBIDO_dAjH6vucT9nt7Sad5kMkDMdrRMyvxg5M62fNSLcMg7iX9K7gQnAJnALXsk1BJtU8PYtffksFQOtd-hydgzRMCyq5Jh1wNOx6P4HSO__hWh-nE7DbLkV-wE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/06fa95c026.mp4?token=AT5HYEIyGc0TlI-c7wdF7UW11YJVb1XwANDRPwj82Sf4QA_mFbfaosoLkODiv54xCJ_XvRqTmA248M0_k1xKLjTUCUg5Q-N6w1hy77eakWuRYCCumpwbocEn4jW-juUlOnF3D2AHDFdKJRQNJwbQCRSBB-4Wbl_yLvmgwAyjSwFDRKBtF8IXOi2g4ddRTpt9dgt-RkPv2Y2uMIOg8PSYhU5JQWGu3ry6BST-nw1bazBPR01Z4PU-RdraNbmNdw7IXsTQp7y2klHCzWn7ele45OBiUl8uYre3mQhrIYYnNpy6RPcLjP5bKq2jaDDvC7IFwy2ccExbiBkYorvNhoJH6lVqnawsi-ZNeM1BKjeRzyrDK-DCjLdGb2NdHXz59aELOzIktiDD3Rt_LJlJUQH9l5Xq39SfxyASB0iEFPzEuCQISnrpqpGl_vZzawZfIrEWn6AvmO4anK4PbhpUmlqfpjmFfPw2ypY_c_WsAPFasTSyxGbB7LnibKAw4FTHrTlZnKrs_4FdSLrVbHjE_WnHN2dXrGHBzo7hn5HaK0VY6EJcfrHFBIDO_dAjH6vucT9nt7Sad5kMkDMdrRMyvxg5M62fNSLcMg7iX9K7gQnAJnALXsk1BJtU8PYtffksFQOtd-hydgzRMCyq5Jh1wNOx6P4HSO__hWh-nE7DbLkV-wE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇪🇸
کاملا جدی دیشب پرچم اسپانیا تو تجمع مردم ولایت‌مدار مشهد به اهتزاز دراومد
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/Futball180TV/101290" target="_blank">📅 11:40 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101286">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OEFY4k7AyMcaqC9XvMANfA4QVDuV3-2BuhZsd4BDYdKLNTULS2bKZs1bY1HOKuKPTDmNk1mnxb6LakD7w4fkP5pb6psV05fKUYTITfyvMX0oXVp69BJ105OwVdrtOyV4HQ-B0BTaAmAFVR-t1y0Sd4I9Uk_bw5gnMC9zLRtu_L80-DYubgJvpFTDI3j9SRRW5HYT_IXfXr-GoyPyvUIN9zsV3FeTXdyygGVcvs0fq_sKnCxxd0a7zvUBCmigJetfo1iTHdTn6HtGxDlD-Ba2_ylxqY075Vwio6wBamjHWIaOMw5AT_Msk4XtAMUH3cuI8yOPAJsC5M0DhWVqv9lwBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Kj4Qw0f-YJbMRcF8z7RliHV5UVsfIMA7aARNSzLsSTzgva5bliCn7ShijXcsXJDGd2XyqtQfQrT1Vlm2I3tHRlxszk_lBu5t4v7D021vysQNRos7AOKCD0RMwa2E9hUNq2-bc26uu61m_7WdqZM6mZR7oku9PXAIvks27i-1YF_4-6bH5tC99ZUGCxkJVDrLoQ8e2eoATJVlBu7ewkL8Q0xa_QLtgbWcpbZ_gy92CAK-K8mmo51xt5j-sh4l1hPuMnuLJ2vp9gBuTcCagBX4lEwgrwjy5Nl68gbzGlRl3SWkvYbThtjqIGC-QcaawTjFyU6OWOkmBMThN_wwftZY6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GUoJMoe4vKsibKysbsFnGO3Qzwbo_wsVsvGPhKKc8OlJgp6VxAvUL3xVXZHLSSE-50pWGZgmPyauamSOBHvBV7Krpk5qhQG8uGiJ9WKG0JvNlJTCvTdYOOi9oIZtp0i7kAKvutZSlRTDmsfchqivpONXlg3gYK4BPTE6EevQJc4AoXjTEMNmq-BJ_PslxC5h1bZh_32_uQeZV87lMWzdN3hqRN5OLJx8-gqPURH2Lx04qC6PLzTweZ0PA93d--rdg4JheOpYsPLQI_98bRVAIDV0b7irIpMWf2bl4T64CUMw-VyCrOev3XUkkLVplfzh4pyUzGrYbMECdU1bJuxxuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/K9XP-UaRMPAQy-VggKxZrirNGZV-yhTSF8dLsaSAdXXy5wNzKlAuR-Axwawv5RJxEMkPIUsF-kmrmHDSVMHwDaLNrKIFzFIJ6l-Nzi8z5snAYnivaQFsq7dJCgSwbPy1PeIBPAyDiTZUQSuyaFWIYCbUcyB_XX2YzmXXzo_n2MV12-bKYYcW-e6T6imFYFhY7t0uGI9-U3i_5MA-uAaNnlzb4gNCnHar3fe2j_I02GoOH2QTOJBUx2LY_veCjnn7Lu9wWO0d5cyI1RgyOdtzrnsF_XVwg-wnMmUt3NP8riGkzJnP8-Kq5AwIwwo_Nnf4WVRbbKWgJ31EtiMNU67gJg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">⚽️
رونمایی بایرن‌مونیخ از کیت‌دوم فصل‌آینده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/Futball180TV/101286" target="_blank">📅 11:37 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101285">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/33ff615c2c.mp4?token=X09VqPWqY9pD6m-k1jT7yCrx_Mw2uEe0o1_V8t5EMLtXWjKw44ysZSPbdC8q9-cn6y2Hr5suLQXcZR50LCgFoWOhB8WeXQJMw5QxcmSrUuwmMKT9UX0RXCiUqSr205pSfqOZfzWY1uJCodJepF-hr48M2traHAVHTmPTaKgPpq3ZgAGLAXznI1glRO3PawXuPpjKCrGU30BYc3h_qCIyUFpEL0eD1gsnZpp-u6TQUdFeNYkvKeqcXlqEriJiOJM7R3lXBD2Een59AAZLqlk77iH4ucuMdXqm0Pf1htUkHV163_VLghHnKh3NcgESLL2ypEJBr1TLMQei0FweaAHSfw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/33ff615c2c.mp4?token=X09VqPWqY9pD6m-k1jT7yCrx_Mw2uEe0o1_V8t5EMLtXWjKw44ysZSPbdC8q9-cn6y2Hr5suLQXcZR50LCgFoWOhB8WeXQJMw5QxcmSrUuwmMKT9UX0RXCiUqSr205pSfqOZfzWY1uJCodJepF-hr48M2traHAVHTmPTaKgPpq3ZgAGLAXznI1glRO3PawXuPpjKCrGU30BYc3h_qCIyUFpEL0eD1gsnZpp-u6TQUdFeNYkvKeqcXlqEriJiOJM7R3lXBD2Een59AAZLqlk77iH4ucuMdXqm0Pf1htUkHV163_VLghHnKh3NcgESLL2ypEJBr1TLMQei0FweaAHSfw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ریچارلیسون بعد قهرمانی اسپانیا
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/Futball180TV/101285" target="_blank">📅 11:27 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101284">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7e24a7448c.mp4?token=PssBYC_ybP5adwPdqsuA4aoP3SLfjWw0J3bcGKBeS5ydCCl943PjRPhZ-U4xHYY1fW4dyekCHbn2d9jtmc8BPC4FjeYNxke4FLlFxacMRcV_SdhJiBaUybelbEK3wODo87HoIoNsnmfuAJVYdHf9OVxmLIlH0ps6OWE0B1KO5dMp4vdNBWMi6MWZBWCSKd7Saoir4j3i90RFT39hSiRqhHxOLeUdHgQ0lfTOl3CPbziGYsfMBytnwOSyPl3Q8i9RpMFy-EXDACznlbmQmjYfZ2NsyAFx7bXjaRySdDgcLqIhR2ylXh9AQXObVSZAvU1gA7ghEWKFXb2AUBLz1G0LAQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7e24a7448c.mp4?token=PssBYC_ybP5adwPdqsuA4aoP3SLfjWw0J3bcGKBeS5ydCCl943PjRPhZ-U4xHYY1fW4dyekCHbn2d9jtmc8BPC4FjeYNxke4FLlFxacMRcV_SdhJiBaUybelbEK3wODo87HoIoNsnmfuAJVYdHf9OVxmLIlH0ps6OWE0B1KO5dMp4vdNBWMi6MWZBWCSKd7Saoir4j3i90RFT39hSiRqhHxOLeUdHgQ0lfTOl3CPbziGYsfMBytnwOSyPl3Q8i9RpMFy-EXDACznlbmQmjYfZ2NsyAFx7bXjaRySdDgcLqIhR2ylXh9AQXObVSZAvU1gA7ghEWKFXb2AUBLz1G0LAQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😆
😆
😆
🇦🇷
🙂
مسیر آرژانتین تا فینال از زبان عادل فردوسی پور
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/Futball180TV/101284" target="_blank">📅 11:21 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101283">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/05de87eb61.mp4?token=f7S8NEZkCGGyucWqu91Rshd4EnpfJH7gIQ4CPz4cXdlQIEoVxuJ3NMk--z4Z22DP374_1mvDL2D5CoeqOHx_rVimwv5LXXsfpB1otGAJQKohl2ZUH956GykTgqCeRYMbHtd5q2L8dJ1Gjs9gO0wesumX_uw6tJEX1ZXwt2HOyuBsXXm0Db8riVcwlu9QDAwbXejklQyiSqoUYA2Bb17Njoocu4PxZgv63ZkqfkcO-xmCh3pGYy2lJrMgzlDmWyyMVwsIVbJaTgHmNkDKZG3YMWURnLUicg2o2IlSkBJocOj7TXpTSPaQTBVXHEB7Hh4PdWuOkVOa9ZuWgl56oZM6Gg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/05de87eb61.mp4?token=f7S8NEZkCGGyucWqu91Rshd4EnpfJH7gIQ4CPz4cXdlQIEoVxuJ3NMk--z4Z22DP374_1mvDL2D5CoeqOHx_rVimwv5LXXsfpB1otGAJQKohl2ZUH956GykTgqCeRYMbHtd5q2L8dJ1Gjs9gO0wesumX_uw6tJEX1ZXwt2HOyuBsXXm0Db8riVcwlu9QDAwbXejklQyiSqoUYA2Bb17Njoocu4PxZgv63ZkqfkcO-xmCh3pGYy2lJrMgzlDmWyyMVwsIVbJaTgHmNkDKZG3YMWURnLUicg2o2IlSkBJocOj7TXpTSPaQTBVXHEB7Hh4PdWuOkVOa9ZuWgl56oZM6Gg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🏆
میثاقی درباره عدم پخش مراسم قهرمانی اسپانیا: «حالمان بد می‌شود وقتی مجبور باشیم چهره این جنایتکار کثیف یعنی ترامپ را به تصویر بکشیم.»
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/Futball180TV/101283" target="_blank">📅 11:02 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101282">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iunm6RoTbQh97nugA1prLr98LAXpdjtlkJ-we9l8vK6iGiGbiHVLwiMlL4ewJy_7BQPWg72F_1hmALPCytd6AhiiqWUoqMy3iuZwuUrPeFhbA5P0N2T4OtOlZXEqIkslC3NtV9lhnFwFEmwil5x8St2FS51GGh4-aMMyqbZ_i4mCXD9P2O5WEfovm5FqvAemgXtXfLhofNJOJnvCgtGzjzzzxT2djvoOqSClzrlVruDG7r_Q2TAyoT-Ga2LvRx8B1eJHFS3pQuKUOUESxF0FdXN0HvGCSiylFmw_P2RUHEmT2CYlrpPIbBMdlvnEn23vcDSzxJ5YH9UcW7vRKHRUEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">لامین‌یامال هم سیگاری شد
😆
😆
😆
😔
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/Futball180TV/101282" target="_blank">📅 10:36 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101281">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YAMdT56_sH7W3k0rjIeUlhbRxnO3YiC7Bu_U2goXp8cVZQbuZ4pht_uEFMBTOrSQ1z6Sxe7ZrNbJ34z5AqZczbqF4F71CtK_tJ2DL7_qw3VDWdNtjDGPtboxDz2tpxppPCaXDK2cdH8RXs6jfZUkKaauyDa4cDJ7tFL2R29s4el5k50Gg1-GK2vtUdbtEu39rKCkHCSYEylc6TeRqwNIPxm1O_S6hmAQrcVhYsEifU8wkhlgM98gT8IMv6igbYWdf0ak1KJfPXFTdGZhJMxNnF74rba3tJEl5gtHx06N52vEvF1lOBtKKvX6cN7wRP_fKC6mAsY-2wwP2i7m4Q7JWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
🇺🇸
🎙
دونالد ترامپ:
"این یکی از بزرگترین رویدادها در تاریخ بود. هیچ رویدادی مانند این وجود نداشته است، نه از نظر کلی و نه از نظر فوتبال. این رویداد چهار تا پنج برابر بزرگتر از هر نسخه قبلی بود که توسط فیفا برگزار شده بود، و ما به کشور خود و به تلاشی که همه انجام دادند، بسیار افتخار می‌کنیم."
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/Futball180TV/101281" target="_blank">📅 10:34 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101280">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e28c62d68d.mp4?token=ura2guB4zpN3srfT4zcxoAEsDJvSpU5-DSQZXzoRO_LeqClU-61xWQijlGZsvp7oFszYKKe_gIdBYNOQohDtbRHGfwYjL6QmIddW6g_1M7Zxfd4S9Y-1Z0YifqcDub1JkbBh2YX-JVDdVhpOJR3_abzoyaUaqhFyrDRZ_7Hh4puk6D0Sho-A-nc3O5K3SF7TwNd14BwEUKgfJkvE5gcB4du2mMzMER4Z3n_P9xsMe0jJ1lo1GIAVASnPw-QVUc2gYyRY6KI2VAaL2ORCI7HLTDwW6_Q-Qa8cqTYlWGzQRtojswD-5n06ZwCPWF9gnYf4ezINDdrh4bhDK4UYi-BS9g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e28c62d68d.mp4?token=ura2guB4zpN3srfT4zcxoAEsDJvSpU5-DSQZXzoRO_LeqClU-61xWQijlGZsvp7oFszYKKe_gIdBYNOQohDtbRHGfwYjL6QmIddW6g_1M7Zxfd4S9Y-1Z0YifqcDub1JkbBh2YX-JVDdVhpOJR3_abzoyaUaqhFyrDRZ_7Hh4puk6D0Sho-A-nc3O5K3SF7TwNd14BwEUKgfJkvE5gcB4du2mMzMER4Z3n_P9xsMe0jJ1lo1GIAVASnPw-QVUc2gYyRY6KI2VAaL2ORCI7HLTDwW6_Q-Qa8cqTYlWGzQRtojswD-5n06ZwCPWF9gnYf4ezINDdrh4bhDK4UYi-BS9g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇦🇷
تنها موقعیت آرژانتین مقابل اسپانیا!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/Futball180TV/101280" target="_blank">📅 10:20 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101279">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bf91e3776d.mp4?token=SPTS2BnQKeQ-qSQd4oUtQrqqnz2Y3TwyFT_AQUDxzEhaVrbgo2wn6Ocwc-xq4ro2D3SYA4auahyEwzv3RgnngcNHRZQy9zG6WH0xl0Z42E16oLuAhwGwfSse6cGsESlWmLbebRoxpwgG_ZW7-_3RR6bSlY18FdYJjn-AqcvtTYzSVXKiWATVsLrHMHpBzsQk2qFMwpMY6KPN_GtDYzKGE_FhMslH_9U-Xr_eD5QIPWMkPc_SccqmjRMsKNoWQlm9zEEBL1ur6rI6vsf5xOL2NdizuTVGTSMc1aZYmRlYh9DD0VdGZdwHTuT642KKN_kvSeK5iam4mhZmcGBaQhBN4A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bf91e3776d.mp4?token=SPTS2BnQKeQ-qSQd4oUtQrqqnz2Y3TwyFT_AQUDxzEhaVrbgo2wn6Ocwc-xq4ro2D3SYA4auahyEwzv3RgnngcNHRZQy9zG6WH0xl0Z42E16oLuAhwGwfSse6cGsESlWmLbebRoxpwgG_ZW7-_3RR6bSlY18FdYJjn-AqcvtTYzSVXKiWATVsLrHMHpBzsQk2qFMwpMY6KPN_GtDYzKGE_FhMslH_9U-Xr_eD5QIPWMkPc_SccqmjRMsKNoWQlm9zEEBL1ur6rI6vsf5xOL2NdizuTVGTSMc1aZYmRlYh9DD0VdGZdwHTuT642KKN_kvSeK5iam4mhZmcGBaQhBN4A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
👍
و حالا پس از ۱۹ سال، لیونل‌مسی ایستاده قهرمان جدید جهان را تشویق کرد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/Futball180TV/101279" target="_blank">📅 10:02 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101278">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d3de45ea42.mp4?token=QMznZvLiyrIF8XPBYreCqkarGGZbPQz12v5WB2VRJ5by23R0uCCMCZfux1eXwUdRVsRzXyeSs25Z7tQb0iLt-_OwuLJ7o_b3W-1jvxkWmrFHx3k7UaFTt7eqvcFaHpIVUcd9FbAvjXNFPF5nhbjpYNpSjZbqhoKcB_oYIQvKHZix9ivXHfQk_00YU7WLxGptpIVBNBfsxVrbOaEacy6uR9UW_IbgfMpFGtB5o7_G7ErrfqjKxeD5u6yQfQyCuoH7oup1zWrYKoeqgP6tKo3h4JECAYWgg8zwlNK3ymUOpLOhsvK7XI5RdqlNn0c4xn9PdTjRrduZsBqUqEuLNEoMVg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d3de45ea42.mp4?token=QMznZvLiyrIF8XPBYreCqkarGGZbPQz12v5WB2VRJ5by23R0uCCMCZfux1eXwUdRVsRzXyeSs25Z7tQb0iLt-_OwuLJ7o_b3W-1jvxkWmrFHx3k7UaFTt7eqvcFaHpIVUcd9FbAvjXNFPF5nhbjpYNpSjZbqhoKcB_oYIQvKHZix9ivXHfQk_00YU7WLxGptpIVBNBfsxVrbOaEacy6uR9UW_IbgfMpFGtB5o7_G7ErrfqjKxeD5u6yQfQyCuoH7oup1zWrYKoeqgP6tKo3h4JECAYWgg8zwlNK3ymUOpLOhsvK7XI5RdqlNn0c4xn9PdTjRrduZsBqUqEuLNEoMVg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
نمایی دیگر از جنجال دیشب پاردس در فینال:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/Futball180TV/101278" target="_blank">📅 09:40 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101277">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HNhOG2PbQ5hyRIYFQZgIe8XRSRUwPfUo06bT-BTDp-2njdoI-pRmYc5sjfXuaeUdeMHNzLU2gTYjlLtmFx_nFyjpUD1clJFhmWDR9lJhMg1GR1haqX5zaO3-49HYkVCx-c5nu1-nkRHVK0U-4yvX8CMjhl4zSNbUlCBRSXojR-15mI5O-cp2c5Op1JXSMXxCIPTNL-j4sqCaUI3YvFLIf42Ve5TMxEyUukJSNDfvw3RotfrXR9YyzioP-QwGATkQtcE43G8ZqTCHvbyj-y-J2NTdgJ-pzsz7rPYWoWg0BnYO8wbncQggh-koY-aGe3LxKaVV_mBP_kPFC6K0157nXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سرنوشت دلافوئنته اگه تو ایران به دنیا میومد:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/Futball180TV/101277" target="_blank">📅 09:35 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101276">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/61d46d00d3.mp4?token=BCG0O0nrX34GtBnYUKia7zSv5TJmim_fA6hPojGL0LbbX1WA-Puqcp8yBu2nT7b9bpwWcZcXO-inLNn8sFrWqLmyW6DncpW34CqTFJ-fGGVXj8OpcOUXyklvXc2Bl8VnJJypBF09odWXeCr_NY1-i57IGAjba6RsLbJwQGdR3MZLEhH2tZQv7OWdSR-x5rbAfblvOdEiakvusJY2ta6hAyLx6WR1K9y00mwapvFl8wTKIqd5GDZfe1o6qkPpxZPCq0vmvakYxqg-OB1l6lCTpIiXAHaIoPZzWpXTJ7dEw7t6yOsYIVPrKjMLrrilYBUzvmUQOd-qIpI_P4RzDpjTGw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/61d46d00d3.mp4?token=BCG0O0nrX34GtBnYUKia7zSv5TJmim_fA6hPojGL0LbbX1WA-Puqcp8yBu2nT7b9bpwWcZcXO-inLNn8sFrWqLmyW6DncpW34CqTFJ-fGGVXj8OpcOUXyklvXc2Bl8VnJJypBF09odWXeCr_NY1-i57IGAjba6RsLbJwQGdR3MZLEhH2tZQv7OWdSR-x5rbAfblvOdEiakvusJY2ta6hAyLx6WR1K9y00mwapvFl8wTKIqd5GDZfe1o6qkPpxZPCq0vmvakYxqg-OB1l6lCTpIiXAHaIoPZzWpXTJ7dEw7t6yOsYIVPrKjMLrrilYBUzvmUQOd-qIpI_P4RzDpjTGw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👍
گاهی فوتبال فقط یک جام را می‌برد، اما بعضی بازیکن‌ها قلب میلیون‌ها نفر را برای همیشه فتح می‌کنند.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/Futball180TV/101276" target="_blank">📅 09:20 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101275">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0a634e3021.mp4?token=sTT1u_MPVTsjWsarT4D4e3ELrzOXQ_e3JVGUgJp7mjneJbGfaoEy3rRfor52q0Ik3p1n4TNG4hcO6Vs0iorJnQ_9LqeTT8GRFpqaqSxYSne7DyrDOiqcoANgbgYLF4ltPHXH2SXIBqzX0MV-_3iym5LOiSJjHou_UXXjB_sCtUBoYzLYY6VIaMnC8jNuV6FNoYGK_H2S-YSQYlW_SRTvy8rNXbdhVPfcSpNbIPev31Ec1VqmEdmAw0CWKBhkQeG6kAlaBtdzu5eKvigAq2rAQrlmFGA7l6N1SQKsa8_ZZOURA3l7Jkzm2akkGHVeGAUt-tLULRVRZpO7UQEnv-TJh3crATzwkkM4-u00L27ZMV2nMDEkc-6YnGRTodIluouJ1Co7NyOO063WI6-NzcYH0FhWcR2dfprQ8caUezvWdCc76a_Tf8UXg6wiDMUVYSu4gt7C9xf5hNSptdFDD7L_R0fCb5hM0iWmQarWrUyXxrZ6J0tfc_duJ5Dt3n1nHKMyeUBGZdWqE2Rz0yYtZ64toq2BxX1aAW23y73jY2L24hk0KZhdtB_6_tscHVH8UQLLkZpy1GWsvsePyYmo4s3h5rK8RLmhd_Icma0w57NCh1gI2XwuagyayDlmd3rGp936ylKrcFIBfRhR6dwXYZJ7b8E0X81xwdNQaQV3wVn0MNo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0a634e3021.mp4?token=sTT1u_MPVTsjWsarT4D4e3ELrzOXQ_e3JVGUgJp7mjneJbGfaoEy3rRfor52q0Ik3p1n4TNG4hcO6Vs0iorJnQ_9LqeTT8GRFpqaqSxYSne7DyrDOiqcoANgbgYLF4ltPHXH2SXIBqzX0MV-_3iym5LOiSJjHou_UXXjB_sCtUBoYzLYY6VIaMnC8jNuV6FNoYGK_H2S-YSQYlW_SRTvy8rNXbdhVPfcSpNbIPev31Ec1VqmEdmAw0CWKBhkQeG6kAlaBtdzu5eKvigAq2rAQrlmFGA7l6N1SQKsa8_ZZOURA3l7Jkzm2akkGHVeGAUt-tLULRVRZpO7UQEnv-TJh3crATzwkkM4-u00L27ZMV2nMDEkc-6YnGRTodIluouJ1Co7NyOO063WI6-NzcYH0FhWcR2dfprQ8caUezvWdCc76a_Tf8UXg6wiDMUVYSu4gt7C9xf5hNSptdFDD7L_R0fCb5hM0iWmQarWrUyXxrZ6J0tfc_duJ5Dt3n1nHKMyeUBGZdWqE2Rz0yYtZ64toq2BxX1aAW23y73jY2L24hk0KZhdtB_6_tscHVH8UQLLkZpy1GWsvsePyYmo4s3h5rK8RLmhd_Icma0w57NCh1gI2XwuagyayDlmd3rGp936ylKrcFIBfRhR6dwXYZJ7b8E0X81xwdNQaQV3wVn0MNo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیو کامل‌تر از داداش یامال در جشن قهرمانی اسپانیا؛ دیوانست قشنگ
😂
😂
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/Futball180TV/101275" target="_blank">📅 09:03 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101274">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TWAIn89VfVWgNN9JozekdpH0aDtenKbtLxElT27qy1KVypAHruFaPO_mpO9bEFnHE1x8DaSMwqAdT_OCrA6PKl35dL5BLvxbK_qJkD2lV6HYoBM1XDFgfkqnnHna2LJNzIwvdPnTJgmiSRQhSDHAISOH56eDkCEqkcEJfylIaOh2SkVHdtXO6Esxchd7Tk-akurvUNMs59VW1Rk_TL9YO05HRBHk8qGPBpk4--nxrSB4UUi7BOsmkTA3BLJq8rbYsbesGWf6ESByrLYL0X9PFtSLARmsQWbuUwV7cF0DPXhqpIqcoPLwiPrm14cYDtjz63Lkq1bdEykvORjytvYUCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔝
رودری یازدهمین فوتبالیستی شد که قهرمانی جام جهانی، لیگ قهرمانان و توپ طلا را کسب کرده است:
🇧🇷
کاکا
🇧🇷
ریوالدو
🇧🇷
رونالدینیو
🇩🇪
فرانس بکن‌باور
🇩🇪
گِرد مولر
🇫🇷
زین‌الدین زیدان
🇫🇷
عثمان دمبله
🏴󠁧󠁢󠁥󠁮󠁧󠁿
بابی چارلتون
🇮🇹
پائولو روسی
🇦🇷
لیونل مسی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/Futball180TV/101274" target="_blank">📅 08:55 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101273">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/deea9feba7.mp4?token=YwmpbZNqx5ZpHEYM75ctK3zfSuHdTwwot6grDUmv4v5QOnw56-6sRxCet_FiayCgGHsLeOFg6iJl-pcv6P3urbQSvFmyVcovm_vew72Q__NhwE02671w5LASxmjmNqnLiR0x6GHrRrVHurV5J_oVaYyKDSbwtiqUwSahzkpVd6ikdMz-NfdrqnMQbUEaAtV8JWm40I_U3jKDv9gWRJK2mJEyFOwqxzcuQZvlEqnNmc4SoQA_NZ3b_aA7OfbtzLXugbpYvrjO-xOdFCxCkzr3cEaSM1qZITS5GmTilAPQwzPFAAlYoa_0kh0t5YkVt3-Kv0ThpzzdywSIFZkcI0e-KQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/deea9feba7.mp4?token=YwmpbZNqx5ZpHEYM75ctK3zfSuHdTwwot6grDUmv4v5QOnw56-6sRxCet_FiayCgGHsLeOFg6iJl-pcv6P3urbQSvFmyVcovm_vew72Q__NhwE02671w5LASxmjmNqnLiR0x6GHrRrVHurV5J_oVaYyKDSbwtiqUwSahzkpVd6ikdMz-NfdrqnMQbUEaAtV8JWm40I_U3jKDv9gWRJK2mJEyFOwqxzcuQZvlEqnNmc4SoQA_NZ3b_aA7OfbtzLXugbpYvrjO-xOdFCxCkzr3cEaSM1qZITS5GmTilAPQwzPFAAlYoa_0kh0t5YkVt3-Kv0ThpzzdywSIFZkcI0e-KQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سیسی که داداش یامال با جام گرفته خداست
🤣
🤣
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/Futball180TV/101273" target="_blank">📅 08:49 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101271">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SGtHg_3-hYlmNoIQgV1wbyTD-RvAvNMARR-hwb--1tPTBdJnV_kU95F9Lz-y6ABP2BJp857N75sCLyng3qQg-VK-i_kL4ky5Rpk28luBFG5IZEx3K6DHQx0dxJDHsc2VM1RCIdBH8aql8NCcyfDflLAx2u0t6U6V4rJnNNEY0xP41us8x6lQMwSIFQxjYg9twWniNfMMk96CkAAdeAYP3w1fhtMraH9U9Z1KSI0-WwOpEh_h7oGy5JQ9mm-SVjBe0lS61vSF79Ub2doQgMJL66Yc3zLeVkqdiftyZFvyIM4ywiKA832J36pCcnwY2MQsJ019VyLF-WcYEXbsSkiIDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/h6CZ3NYUrDRXMWsr1C4Q2e-7C4LFjAZu_CqHAIGPeIKzJO1o3fggCGW25BLY7tEZlnc8O5R2EwZqOyPeJvEeBk1PPBzrBAZRkx1L4A31Ioq97eEAFdUhZ1Q-h8FGt0cMU2OX8TGf422tC0XGuTKs-jEafiQRj_TYtq-9Le3UX14XlvFlyFbhMC_t3FpxPm-7dnBZ70dfIViW5alGpEbpx-TY0idPb-mDBXc9fpAhRXCmXtfJk0dm3OxQtozgF8WCHgZl52dKkB8uTxQT5mgQmsLa7hhvSp3R_yVUqUPgnqLfkWyBeRoPxCcKiUUjTz3ZGvp476hOH4x72I7uy58bKw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">کوبارسی و بانو تو جشن قهرمانی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/Futball180TV/101271" target="_blank">📅 08:28 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101267">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dduMp1C1vNt5sNL4lFbfaL7HKX0p8thNnFYjAore5ZVG65hso9hzpsi8Y3S2YaUodYBzz-JXHzc1jQXXtjElcogD6wL_nAc5K_--Uu0VilR0gBUU9g8TTkUxHxN9YSlklCgQZrMTo3geVLWN2AOs-Dz3FfZYrH_tm8i2fGPVp53JTsQIToTCEwa3Ig0-nBq2jzUwsR4K6bey5JLUGQWtAu0ZywdSLI1MER_X_hmN7CnNZBrIGpK0NgOkD22sd2bBZ2qPF6--aqJDoHol2uIkSsv1d0T25HtKNW0J5Bq4XQCC5yQ3lbsB32Ux-xIw2ztnDJs5KB2ays8HYqLkKhM7ag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/j3igihZbxi-B_HTuO6_EERYYGYX6DAhDfJVh6-i1JlYJyH0Lpi_Zt_Y5VRxlWCdzPWnS_zK5a1ah6dtxCrRJRyDyiTSDVTqhGOEYhdp2Yml69nr4qV2F4ZDaIBQbKpSH-Ak7do6pqPJBVbEMynngaqM0NDSlV4xe399BLKrWOOHoS2glxWRn5s7P-4S98TaC4SNBeIPqWVEQDL27WDlXlmVEjjgD9RUrF7kSOLYmEFM1a6gtPgOx0PVvSbIwHt1aPh95SAJxmsZ2MTD_a9QXsfMkja0DE2H7DfwrkdMzpyM_5Uay6Hw9pDWLPSstizTauS5Lo1gBjdLPh7SUNLml6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vCwLJg8srAZ15NLc3YYij5FeVuMil1C8htCvyQ-tfJkcGx6zpoBF6zvrrL0T9C4BKBztB1NDb35fwQb0RoYccAyZGBvZFrUV2MQJwfgZUwxF-1P4A00HRXcN4AFwgwVFJFHG8arz8D3x0G8YqLwbjwN06mPJzVCAbWZ3_OirzCF-Wp1CHNlGZK-855NM5yBf5lwn3W9I5QfrGCTHiFJOMzew9q4czYhLUBvp0e9K_7zG5sFQg3lEfzRuZO9jG6AUpnLIUN7Is5LlnI-kUQ8MjRTF3C10D1x93oeCq3gf28nzBRXGlcC1mRh4FEhVGIeOa9-UoxHtDprMOEXeouZIUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eKWkTt6VLbPucKKrw3KeOCUGCsQjMOulVh8BAKH8z11AedycoKVoMxdlVkDXLk17UxtG8c36DI-pZ7ljXj4SmN5J26DG_hAcevVh38WcT96ArJXjicWz9SCmkQjqEFA-1edVKuCwcBPgmm_GMCOj4TMs-teV9coA6bKX7ka64aPc6ine9MRoVRnD_nG01ad8HtbgLnhFsKO1mA-FCMmvVAHzzycP82MNh0crqaQjdH1mpMP630X1ooRkwJFAUrEz8lz9Ll7rZN1gJxvqZ6BFnNq0ZvrS6BCVtsdalo0BaPufBhMetERQB3NiJJHpbayChWIorHweUPj6Wxr4e2kwFg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">اینم چنتا شات از یامال با جام قهرمانی برای نیازمنداش.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/Futball180TV/101267" target="_blank">📅 07:40 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101266">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/79dd52c94d.mp4?token=JbuZ2ku1z6evfRqA1boKyjNL2GZg551A-i2rvQLYu2I_-u6U7c5umlu_1RtN0Yf0E4uYdjryCdjAQK0COtwJSX4-FJQHnyusip6YfGqu9CYGNparQW3Dc-ikHRcGVJCvr4-eFBdyFXtBNKwFde1qXEHc45fLtN_5rBOkE9hlWNfy9mDkC92RHWcM5znycHfI93t_7nIUvAEKT5N48hGYMKr0DdbD7Gp6F43vhACHEbrIel-jM9J1OeasrgBWo5RKfqkSd_enc3UdZOgnthLhhDymftUivn3An6H0zjQSA91YtLW8pxocJmu4onFsroEkcYo85lXjEQIyQ1NM5XYiaw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/79dd52c94d.mp4?token=JbuZ2ku1z6evfRqA1boKyjNL2GZg551A-i2rvQLYu2I_-u6U7c5umlu_1RtN0Yf0E4uYdjryCdjAQK0COtwJSX4-FJQHnyusip6YfGqu9CYGNparQW3Dc-ikHRcGVJCvr4-eFBdyFXtBNKwFde1qXEHc45fLtN_5rBOkE9hlWNfy9mDkC92RHWcM5znycHfI93t_7nIUvAEKT5N48hGYMKr0DdbD7Gp6F43vhACHEbrIel-jM9J1OeasrgBWo5RKfqkSd_enc3UdZOgnthLhhDymftUivn3An6H0zjQSA91YtLW8pxocJmu4onFsroEkcYo85lXjEQIyQ1NM5XYiaw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇦🇷
💔
اشک های اسکالونی در کنفرانس خبری بعد از بازی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/Futball180TV/101266" target="_blank">📅 07:38 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101265">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b524eb5176.mp4?token=Xmqllm9G2BFi8juLmwzZKdCjVqStqUXGIetp2QM0Uq0h9hZyKTsxT7XCKpyjEYD3qIlcAx0JmcVaGcS5KKyDo0iQulxWzv9rmcMFeLQkMj4qfDEcg-2NVgMbGfFxn1TyZTvGqTDrENhjU01g8kq4m0aTHZqTsj8Rx_TwTx2W4Ajp1mhx8099__q-u2JfeekKxRrZCQVAJ_TOB-GSsPT3JigeLMJ4CMSJcw_yYj_JMB48zTyhiaJSVnTaeY7O5l-_3mgSgxvmBrSvMg1ZwFdkA5WkCBQEviIuoXUmudkICLLj-_723mzVfB9SugOjoWNTkkVE9ShxtlAhJJqIb_lLyA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b524eb5176.mp4?token=Xmqllm9G2BFi8juLmwzZKdCjVqStqUXGIetp2QM0Uq0h9hZyKTsxT7XCKpyjEYD3qIlcAx0JmcVaGcS5KKyDo0iQulxWzv9rmcMFeLQkMj4qfDEcg-2NVgMbGfFxn1TyZTvGqTDrENhjU01g8kq4m0aTHZqTsj8Rx_TwTx2W4Ajp1mhx8099__q-u2JfeekKxRrZCQVAJ_TOB-GSsPT3JigeLMJ4CMSJcw_yYj_JMB48zTyhiaJSVnTaeY7O5l-_3mgSgxvmBrSvMg1ZwFdkA5WkCBQEviIuoXUmudkICLLj-_723mzVfB9SugOjoWNTkkVE9ShxtlAhJJqIb_lLyA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
🔥
کارلوس پویول: "من فکر میکنم اگه این تیم ملی آرژانتین به فینال رسیده، همه‌ش به خاطر مسی بوده. به نظرم اونا به مسی تکیه کردن و اون بود که تیم رو تا فینال بالا آورد. من به احترامش کلاهم رو برمیدارم. همیشه و تا ابد از لئو مسی ممنونم."
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/Futball180TV/101265" target="_blank">📅 07:00 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101262">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uIvGg93PUb7HlNqd9WMSq-T932fvzSGEG1amY7HVgIKBi5ah-Bytq1Cb7WgEwqwZ-B1bkRnbMXelxJyyTONq3CoRXGKsXqAA1OL55X-tPyD_Roof-cy7JHxq5XSS1wwhQCyMDCvXYnq0Y3r7mRAqIix0VNy5De5hbA8H3GCFlMGQhgEtbN-t-U4ezOwFIdxlsr0CwH_CLCaLkjFNYij7tC2eRlgfqi_hhPcWfVhOQc3uvzDj1mJ6JAWiY7onpmYXfooPQEAfF6BGFmhoCYCcZKKnnMGs2GCZfDzBx-vRCE-ICUpvmF0Hudxz5oGO3RbwYxCYwf8qs8RH1NSvf77FBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ORrxScsmg_tuDb5fMubRuioFDBDdX76mss3btk0nUtpnWx092jsl_atipOSSghcZQCebVfZ_0oVUlo-bJPGwIpSEHwYTwBnH-jcBNzvfdkniG6TgprU4GvNiKkYwRfuGy2P40Qk9JEo6QKjXRLsuz00b5SUudLioYPzZwENx0S2eEZrIEW8zI7mm4VtjDGNcj8gakoyM4yEd_BB-6A_SlsM_iajiA8gRYsh56TDPeCpsgW3mhuHQZ_AYGsDP0kFr8jMs3M4OFonOMOysk-qKhDV6q7jzvned3-JiQu52kC8VB4wvOy6ejcP3wUMfsB5oZkKizBqJu787qWFbiDfaeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NmvRH2nXESK3Vgf2Q2VUR5OcksPNVTIIsIWr8C5IIkN2fA5trKEBBQ2P_CLsI5aSwjNtqwK0UKtzVTY6CRWJOn73NUv70K3wVVFNNFVRBsaf-KD2ChpQuRVs3shTo_9mq-G_nFpINWJX2DdUKu7wtqMwqVxyXd__nusmHr6PGCcuH9fPuDSQDMm681YxNbNKdELzF2db-OMhtbiJ7dpW4xY_Vy0foVyOopQfyfIvOxX4EONHrbe_hOJMcu8kT9aTflpMoq8JeOsa6gCnOp8ZPML2d3jqU9KFKNhx4SKff61UJ2AUezVTmN5ng1Eokvj_oV2mVWdes5uwSo5JBvZugw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇪🇸
❤️
مینی یامال برنده ویژه فینال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/Futball180TV/101262" target="_blank">📅 06:52 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101261">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MYG5iQfKWnQXsc3AbZ9WQ1hJ9mCoCjK8yIOTnIRY9moQajFNNp_e1euADvwgChZSi1KGHqneG_f9u4f-LnsIxxnH_8sPT-7yqaJcwyXN7HLp6ABeqixnIDY-5_EIf1Ow3hiOBR5Zz5d73i6ioESFz0tE_YI30AFbHYuyvAKD576IGr1qwj7BTLnV5VjSDeFcBKVLDSsUq8mAIdn5HFCeEIYzcc_jgjgOHs_6Etrh5aw0GJifcAf_2nwh447mYVXT5Ot3y4VHWT2pTN9gAbm7DuEsMYmfHHy5wYsGwQPrMXj2zdJwZX_QF5MP-bdbhPRipwesKmsx2TbOsMZSbaRd_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
میکل مرینو:
هنوز هم در شوک هستم... ما قهرمانان جهان شدیم و این یک دستاورد بزرگ است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/Futball180TV/101261" target="_blank">📅 03:48 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101260">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZD1vsAzSgL6YWiqCvLL0hQfwrsRqe9OJX4H9sE7CcHApfZKSl8-fJ2hostAtEtCYIdF2Dfe5rMrAcjeQUZcKr6ZqGV6zpBf-GAfAmUPreJBo4muRUSClaO0NwOwGsphrNJEVBXkoQgE1fM2ryrfzAAXQkMMsPQLG57dgax7-yGMBsujh-uT2BYHOBMQDHLfNzVPMyzKVtCYNOSHJDxjffJd29BYvncR26ci5646X_5aNYo5Sez38QKi14H3FHJPufvOgVWN2cI9D862KJ0265fFMFtfJ6wA1-IxKsy4qOvDVHHqqiSsmJukni4NnpHRjcNcda_JJAEovThlmxZ8Klg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
دلافوئنته:
رودری بهترین بازیکن جهان است.‌‌
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/Futball180TV/101260" target="_blank">📅 03:45 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101259">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ecc89e4277.mp4?token=RPvPZjdbHfRtA2gl9YmKUIMI_IY-HMID2HZoNjUNV9YMZpyERMrDWwgKVS-W6Kfj2kOQ-cLMtDDdNQdKZth0i2bGo8WyqQmEMTF423SiRu6aI3Fyi-U8SdX22elh-38eLVqBTKpYSbmJiZHnZU9y2EzJhhCvys3-L4BOw6k65qNTaD9VHOscvZnMdWuTEEEshMxVFevvqXG07HcCsl0N-h69KEUMuVkwiIb9X8WfgTxhJbZdaBAx1wz0vjMQoBnPXfrJuXX4VRSAnN4yyWhrYa-qleqJBMPzw6iknG3RCAIxqGhELHFATBcDaCtoQFrqDMrnO4nNjBtHWh9RLBP7iQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ecc89e4277.mp4?token=RPvPZjdbHfRtA2gl9YmKUIMI_IY-HMID2HZoNjUNV9YMZpyERMrDWwgKVS-W6Kfj2kOQ-cLMtDDdNQdKZth0i2bGo8WyqQmEMTF423SiRu6aI3Fyi-U8SdX22elh-38eLVqBTKpYSbmJiZHnZU9y2EzJhhCvys3-L4BOw6k65qNTaD9VHOscvZnMdWuTEEEshMxVFevvqXG07HcCsl0N-h69KEUMuVkwiIb9X8WfgTxhJbZdaBAx1wz0vjMQoBnPXfrJuXX4VRSAnN4yyWhrYa-qleqJBMPzw6iknG3RCAIxqGhELHFATBcDaCtoQFrqDMrnO4nNjBtHWh9RLBP7iQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
نمایی دیگر از لحظه بالا‌بردن جام توسط رودری
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/Futball180TV/101259" target="_blank">📅 03:15 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101258">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pHBcUGfFxMnX99VJvsgTrb4yGQvKhi2MwRYF9xAWGtrDkuHsVhKcIPzBqRbSukHPj_TNc2gJW-cpk5I_eR5oee-J6UcJh_Bt03V8KWOuSP7lTsHyQTvT3NoaDFj3MPCqKd0NEtfNYewKsmJDoPco5Q8G-xV-H-WT3t6VJYo5Pf0JPCebGHTHEPdBGcb6eMx4Pq5RXmy22ltYEHLuVYlVvU7WN6UTxZu9t6xylQ_iYGABm1gAIo7-cx69clcLtT34BuAx91UzZHN9_14ky8EFB5QZKMvwgrRQXv3elZy4dOIHC4lvt3vePguGcHb9OIzXC2MLxxQIaxDYyaORL3sasQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
لیونل اسکالونی:
مسی بهترین بازیکنی است که تا به حال پا به زمین گذاشته است.‌‌
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/Futball180TV/101258" target="_blank">📅 02:58 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101257">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iUWBbZsPiDtlSpCkCWfRN4uHVe8XzbbN1RKcOnZb8QrksR7P97F-RRtCEZUZoeQFxb5KdYc5CjOZF2Gx67H9bmAjD4O3FdOopZknBUZuNdmI6jUw46dYsqW6A6XCBmsXdP33UetYUGAEG6AAblMRUWqrbQNXvJ6fAHXUTYx5zM54pxcUlwzguViI9Z0MIrtrOeqrRlGD6s6qk7EfSHOKvsE23YJvuRdmtpt3UoCxwbnODvrDYy3MiddU9Ivj6xgEmP3jqL3NAkrtSM2Ebv1qvufA-NChvkPbonacytw3aX4pr4kzc5RG94lyYdE0O3uNDnQeWydLscAx1W5UG5UMtg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
😍
لامین‌یامال و برادرش پس از بازی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/Futball180TV/101257" target="_blank">📅 02:55 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101256">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mkPApSqj_4SP0rXCKQ7sOpDP6jZpyGcB_WHuTx0zj99mDlUQ9txkZPBGR8ZCz9mKisxqv4K3e5qSC_kOjrGD-DAhDtnoWRg_4m7XJK6CgHtMfcvJy3w8vN1VUoYI6gNxO7HLH5WlCiCOrJyyAKLpGXLEsches1clcvH8epFGpK7HBmO69wTJWWQKtzl0CRZnXbjGUgLH3ZVzfamxcxb5pLcJEd5QLJRkvyTnURPaijGhXoJIHN19iQylxJ3yea_FdPIZ2F0oZb_0x2tAxQ8xOJJyxl4FrunPeuu8XyqQhqIWnd8iwpUTByQte1dExEEFSGHmkkhx91izJYJC59uO0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
فران تورس:
دوست دارم همیشه در موقعیت‌های سخت گلزنی کنم.‌‌
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/Futball180TV/101256" target="_blank">📅 02:52 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101255">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CYkoM3GMM7AhYNfDgpPGHMTxC9b0fe1zx5Ae4djELcKu9IkgcPPv64aRm8ymcjCn4j9HI8y_TnUOwLhIhPsYILqQ65xjxPyNHj88QZfoI4ZRAhmqdJad8ZRFwiV7rmGkFKVQBWW5vcUIpNEZVl7X6q3wpjCRJ_s6G5jfdqs4RD5nh1u9Sl1s58TbvKwMVokdepMvAMQXZc9MBeQrsDvNctoRbLcYwvADkn9hml5nKeFJ-XnhzjF7KgKzkW37MlWzEhNiVlUKYGg3JmRE0Uvfy_1cTXBiRkxS2YUU7Z9W75jimxFJSe8tDzGDhJ0FETU0vWWGU8d6ytnUw7pcN0WlyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
سنتکام: حملات ما به ایران برای نهمین شب پیاپی آغاز شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/Futball180TV/101255" target="_blank">📅 02:51 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101254">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">🚨
چندین انفجار در تبریز و ماهشهر رخ داده.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/Futball180TV/101254" target="_blank">📅 02:49 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101253">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7fd06e84d0.mp4?token=WeYJE5ASzGXqGxBk2xQ3hMSA9852NuHysG178TyxytxY53jMbV1gfwcBbM5iOUIYdgqfFpArTNFFtikFHExxGzy9OyPdIYtPqFNFAkARxWfNHQiBSUbc6CoqaGF0V8eLjslNbDmgRKxW0u09uIE3_Esdo_9wLcA12WG9uw89EWJ_PG9B4niL48kH50xhZxm7IKzeXGMXu8mnoL0cWuEX57_lI31LEt64mB71hVxkYKrRYMpz-S2b41ryPp_avUo53oQ1fpLQyI61HjVqyzHnp4196m6QaJFyvqzz1-VviHV98MfIqn_2TRbFQNDEkG0FahTboAX534vqmZhnJuXMrQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7fd06e84d0.mp4?token=WeYJE5ASzGXqGxBk2xQ3hMSA9852NuHysG178TyxytxY53jMbV1gfwcBbM5iOUIYdgqfFpArTNFFtikFHExxGzy9OyPdIYtPqFNFAkARxWfNHQiBSUbc6CoqaGF0V8eLjslNbDmgRKxW0u09uIE3_Esdo_9wLcA12WG9uw89EWJ_PG9B4niL48kH50xhZxm7IKzeXGMXu8mnoL0cWuEX57_lI31LEt64mB71hVxkYKrRYMpz-S2b41ryPp_avUo53oQ1fpLQyI61HjVqyzHnp4196m6QaJFyvqzz1-VviHV98MfIqn_2TRbFQNDEkG0FahTboAX534vqmZhnJuXMrQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
🇪🇸
🔥
اثر جدید و تماشایی حمید سحری از قهرمانی اسپانیا در جام‌جهانی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/Futball180TV/101253" target="_blank">📅 02:45 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101252">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mQGXXPYXbGL7_oz5cu03qFF6tHSnbN4mqiQ1Wu1bF-MXPDNN2pLyhWCVO_tkRDmTF8yhAaNFIL8YO2zKaI5D_YySta685vA6JjPe3pgeCW3J0gDVEeL_ZTKfdSAr5GgYjbfJQAdU60IeQQkeUHvUEP17vZbGukTuUhYxVywV1fizblkpNtEHpVvtXihjqWmEQ1uy5fspn6Gpd1UYfO5udVYpKF66-RFgh1Bi_04utnU1flE63YO0KurZ5h-zMJV2ckhgBrir2bhEpK6U_2RQp6DmjWtiKY4Vf6qHDF0sdXq91WOa4k87fD_Toia4RHSTOr1Ol_U4i3WOvNGYbvDcFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
⚽️
بازیکنان بارسلونا با جام قهرمانی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/Futball180TV/101252" target="_blank">📅 02:37 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101250">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dx-nxtNfRywJrIwkSi3xVTkddhRj1S4VK0bmsCpWhX0tIBLnVGtDqExh8vLZAF-Od0qdZxBoVHmhFo4r-8KwhWaX8yzljVcWdnfFhsTm-51g_Jj3J2Wv5s4unf06qZ0_OlFNFTvQP7HHsTZAZOOr1gb7XAxtfoI0frKW0v_S-8uvIz0mYGB4sv3GEpon2WZnt_hd7Ai3XEEfgl63ZOarnGRhBAkiEmPHgo1MEkCOK5sqRAOoBOU7NkuCztetXhCNxQapKm8LX5IgaSOVoYQjEu-yKjfyiamN3gff7D4Grs8Z4RulMe_8wdRh9Y1Kgs6Fe_XqyshBQfZ3eHaine9Y4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
🥶
🔥
مسی به این شکل جام‌جهانی 2026 رو به پایان رسوند.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/Futball180TV/101250" target="_blank">📅 02:37 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101249">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">🚨
🎙
👍
لامین یامال: "لیونل مسی، بازیکنی است که همیشه از کودکی به او علاقه داشته‌ام. من بزرگ شدم در حالی که او را تماشا می‌کردم، از او یاد می‌گرفتم و رویایی داشتم که حتی اگر بخش کوچکی از بازیکنی باشم که او هست."
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/Futball180TV/101249" target="_blank">📅 02:36 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101248">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Coh2v67ysDqPTzpmlqGuGtruPMvtgWNX01Zc5vqYKPk74iQdoK1tm2znvBBNSZ-6a48Yt3HHyryglIp2qSZRtr2riXE2Fr7rnvMWHFFxmPQSdSpnEK_697DUB4LI5avEqdJkVlYwpbNfBQX3c4tJKDbtJGW0EtCLKrcJFTVmtiixZAafBVPvyQMKsAfcMtozWU5RXaOgJTHn7nmg5Tp1wvTglAX5RtsEC69ea_5189vdSePDoLm3O8RTq-IRjHchRKIYCBzHYUjAVvvB5RT37ozXMlmQ9vVLH-vG33ND0yw8qDgi9RhCXQ4yOZ5d_BFtuclG4nQ_4S8zz1wWGuy09g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🎙
👍
لامین یامال:
"لیونل مسی، بازیکنی است که همیشه از کودکی به او علاقه داشته‌ام. من بزرگ شدم در حالی که او را تماشا می‌کردم، از او یاد می‌گرفتم و رویایی داشتم که حتی اگر بخش کوچکی از بازیکنی باشم که او هست."
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/Futball180TV/101248" target="_blank">📅 02:35 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101247">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HVQCOU_0PihVQpSbUM96_fFugKeqzaDbviK9ShB4TGbnq1-9XaOyhRqBebyrpAm0xHIz2wZn3kNP9d8JY7NtniwKTTPXHtJaw9loBUQXZJCxmLOAMfmvpP6--x11wd7g0Ejf1VvUGPtAYfMj0gj2hyMV2ao8zdZYLyzRqaTh2BSQhmyP8166Jff9BQD9gK2FHmnEI1qbN-WKb9_Dd3zdd74jBpk-UMLRTvQA4QzlXI2J99MvbtGbg0lrkYugvfD7Pi3wKf5bdGzrzX6O17Q31gnuvi40OwjnjQuwOitg2x23P3C7h5hUM8PoDv1g6pnwwX7Mea3jypaUPr0ttx2YeA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
😆
بعد از بدون شکست بودن قلعه‌نویی، ببینید از دومین افتخار ایرانی‌ها در قلب آمریکا و جام‌جهانی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/Futball180TV/101247" target="_blank">📅 02:34 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101246">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EtiEfguSPAVXhbgZHp_OO2Yh70dXMZxUaPpocWYh4YrgoYfZv-wnSPbDEwFI5MA-4IewztikArXWYXJ-hwC1wkYIspWRL9JKyHvRgTb4IvYZNE8da4DEg9S_Y-vlgb3rHGM5wd9DeUyVkBgo043NrOfq6Xklf5L3FYGcMi3k1uD0EhFjvsdO0TrQLBVRiQYYiRpxxuwvNRjTDUfEZTU3f8gdea3jzlH7UYvtHGQtQ56zoHJnmWE5ESwAB0EcJasGiJNYokHkB-MbXeemNyTYJ-8zINX1s0KX0HwqXSZWLJRq_WcuobAUFjPxFHHri3BWGj8oFmxTGbuyOYrFUvwR3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔥
👀
بانو شکیرا در حاشیه فینال امشب
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/Futball180TV/101246" target="_blank">📅 02:32 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101244">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YoQN0-0953MVnYFUKnnV_BG6ldwXMJ7xmWNDRLXnBJ3MND-mq7UWp4101jx4SgkvG7MuB5krmJMm3sALna8-COkaD78FWjplIinpCA3gK-KWYK7caHSEliFkjRt25tNECAC8dpE7-zdnAd4iJk19PygTtZZf6Pt16fk1Rf6tzrg4xrCHHU2eHJNZN6ArxXbo-9tgjRfYlPaUpuTqWKjfj0van0iwj69IDl9Dj2ujOFOGI5S74z7QSWcNreTgsa9AnXZ6B2i5GUJCr2QR22QIGClbk6DiPVaowVvuYz1uXxRkmtl0Wz4ED0KK7Azxa9Rf-K_zBzeDucqjkRKN4uUm2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HZT26dzI26XcWaYkuUD1pEaE8Z8RpZYNG8u8xstjWRJcFPne4QLeKwro3bY6l899LTN5DM6-MGKCVhZLyOqHqe04QbSfmKHzrYALjjlrpHvyJw29ulr3UoGo9D7zQMjMPYnzCFP-ZbrAXqs8okLzK68v6XM-jSu3fba7Gq9b3-wy5nSTyNBZKqm2Z9eOaDV3yNfMm4oQtH3MG2HhgalDv2Rh7C73mB3XTZGrtw2MbLa8QGUf1fxTPSF_eCbCmURiCchz01j6AuZq8sm_gGXdaLEDsJeyiNYXEHbf6YuAYF0w8hEDbqQ6GTI24AUT3QcSjsQojHUwcJXs424YrGNngQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">شات های جذاب برای فنای فران کوسه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/Futball180TV/101244" target="_blank">📅 02:29 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101243">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HfxmW6LQXW8sL1oSoYfXKqa9hq7Frw9reMF2j-ykWB9uD4f2-SvdeDXCZvrV4stJKUmHfLNNX_JKTfpvzelseCnKAxyWKTyW5TSKqZVsUxqWgog_H1l4VBAHwEDAM7mDHvG3jputMcvR-Kr43ECHPQouEy56ExjMMZEq7DHLfa5oICzNrevNJOpTxTJ99itHbVhvigBTWc0h-G00QGrYc6zsbrseME86WPxR5BldEQBomN0rwDhlgyqYstpca8MrcZVxFtCwZkPjQAMzXUkPGyU3tEq0oIdKXZbHi8IUDmO9zJjPXI-jAW8Yn0EGCLU_Fh2X473Aigzo9FcDAJIE3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⁉️
🙂
بهت گفتم یه بار پوتین بهم گفته نابغه؟!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/Futball180TV/101243" target="_blank">📅 02:27 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101242">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e244c0b930.mp4?token=qvq61q3ltatds0-ccsZxncoL7xqKZGKFejECYDLdH_TxxcW7TMaY1Msr-DyJHZ0ZsKedbfrIMz-hE9xFLv7hfj6U-LILU_GRAbJw1MWBezcoZqG8krJk8UIW8UiV9ol6u_iXRgu4bWf9oyGtcp58kfVJpeVPX7wf1XbuqRPK_9MD5T5EQ51IUmi5P7SbfF9LUkmYCtb1TeYNYunjTCQQV4DXO58JEbUP75NTusQvC8l3QOSWV5Uwg7Km-V30kDQjjh7TjZXD2atjOTy30uZYl7QIiCI-hEFhT0DrQrKDN_IFjW7YluM8k_1QhgOumHzKSfI-CTeF8fWRRyfWnMtwug" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e244c0b930.mp4?token=qvq61q3ltatds0-ccsZxncoL7xqKZGKFejECYDLdH_TxxcW7TMaY1Msr-DyJHZ0ZsKedbfrIMz-hE9xFLv7hfj6U-LILU_GRAbJw1MWBezcoZqG8krJk8UIW8UiV9ol6u_iXRgu4bWf9oyGtcp58kfVJpeVPX7wf1XbuqRPK_9MD5T5EQ51IUmi5P7SbfF9LUkmYCtb1TeYNYunjTCQQV4DXO58JEbUP75NTusQvC8l3QOSWV5Uwg7Km-V30kDQjjh7TjZXD2atjOTy30uZYl7QIiCI-hEFhT0DrQrKDN_IFjW7YluM8k_1QhgOumHzKSfI-CTeF8fWRRyfWnMtwug" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خب دیگه بریم بخوابیم که جام‌جهانیم تموم شد
🤣
😆
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/Futball180TV/101242" target="_blank">📅 02:26 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101241">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mqv50XTXieppJz2B_H4xKFNvLIhzdoV8lX-aC0ECOUontcd9nZPVTEGmYs7cFySGACQkXlR5rGJaywKzcd89jvddFOK6vS7n0xF7a2LEwKFx0z8lA65DKi3M2Nl0g4EZeeeDAI7fFnS3fnbaBGgb28RSTM7xBAm-QSkNKauChKeVQc7awKQw2uqYCtPscMh_mcxz8pQQMxoFcXiBDuSeJRBFT-Kk1p2TAuNEUCNoYHNEbUxBpp3r78wwJf6NaTk2v9eyzgIQ9ZgnUK4s4u69AIoZ5hlVpbSGVPd9SD-_5TwTga-UwwtzfnCSd0bFaMsXPKj2TZKDMO8UlMYRUqJxlw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">لوئیس دلافوئنته با جام قهرمانی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/Futball180TV/101241" target="_blank">📅 02:26 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101240">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PLDqKyhEWC2MZLyvY9xB2jD2gHFjxCW3Wfbk-TtDwH5ihdeWVoyjCM8Sd5tFAlyt6wd7gH1sRIAghAD1ySnUPVifWfM2FU6NVEkuwdjXJBLMPEnvk5dDZTLU6iYiw_R1_9WwTXlsii_CCQjcu7vq-713DNho66AlaX_3U7Mg-5jVfgYfBgwSGX6yXkgWktazwiEItXPiIxT_mnBvKremDM76gZDgeySGyCKhWYkq8_6ltBnja_wYcoMkapCb92CHKtPI_AifTOv4H755JxV6-_zLSSNhG8_-4Qz7HASZf5e2ItneDbxPfWM5MdTdcfpvlufTObxZjtJ26rrr7rjNdw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
اشک‌های شدید املیانو مارتینز گلر آرژانتین
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/Futball180TV/101240" target="_blank">📅 02:26 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101239">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sKWk8tAZoaeCrYVPM2nz0gEVnsXITVSqJEbxwYL6n1qz8Q0hpepnNTn30ACCcE7LMyvenzvcc47SZXw352WVe0Ye_wEp-ldX-kDZ8ZvgrTuUZsa04-WKBj5ObCxjrM4xDZC3s776w4BTOLR9DHjHbZjNS3KTJILKdqyyDXrVfcRXjrlUtfU__Cu4LS_mDPnPB-d_T6j9J9cGWXIq2GGYZHP7_12_fdkVIDyDAYhzSIYFFJbiHyQiE-q7knTg2Vj4YcdHKjK8gml2aA1T4CscOj3cXA4P4-1p1Dpp-HUsNdn97Kxj_khPkTtxxneqSg6kyFrWWHtpXo1McAzdn2pmjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😆
😆
😆
😆
۱۰ سال دیگه فران‌تورس قراره این عکسو نشون بچش بده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/Futball180TV/101239" target="_blank">📅 02:23 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101238">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/thydWJ08_1u9VcAuOkfdoxEFq_BHV0_r00lLYc8IrThFCiIplu-uwwvAGh_q5pfuJk2Hpp4tZiTjNUX93KMuPqq5tioh5eXPkELl3gKQzIYxk1H1YKek1RSE2KvD4hSbIskFNU8OwFxfXiPbMolV3iGT5KUbnrCcE-ffVOid58Z0VaVnSS-eGFSVfyNv1gA8Kg2wMm1je-q21i5sqaDDqY4vFSEZg8Kyy-h507BTliUiN__ho3MvrgF1m-mE4fgMGdiUUqA55c9VRvdD3QFMaIGo0b867q9VcguBAMiZyHmQ22V5oHEUHk5beuNGCbPOEUIgUZsyG4VqY67yaCAsZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
اولین قهرمانی جام‌جهانی در ۱۹ سالگی برای یامال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/Futball180TV/101238" target="_blank">📅 02:22 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101237">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/de6713412f.mp4?token=PYrQfHISRZA0FqaZS53cptZ-q045qYH-RA57hYu8sv9nGn6R_l02rP_vBgVgOUMacqvsW0B1Ym4a1s1FOZH_wpp0CHU37jnmTtC0KViuo42o3xsqRmmBLmIJVls-nxocrQCkew5ydaqRdiPZTpzknHRQCB_zxFqvfjbike88s7y6b44566pECf6aQauGEHEjQYujh3obfAU85Cp-wgRTnftvTHjjaAmQ-hijyReZo6zA0i1HBVFnhvejswu0bWYubdgm-lP-P3lsKTlc-JnPaa87KgLD6TKz8wbTEhMk4hLcPXDf0pQdHv933TaS0BwpbUclOwespMPiSGlaQ-uDlQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/de6713412f.mp4?token=PYrQfHISRZA0FqaZS53cptZ-q045qYH-RA57hYu8sv9nGn6R_l02rP_vBgVgOUMacqvsW0B1Ym4a1s1FOZH_wpp0CHU37jnmTtC0KViuo42o3xsqRmmBLmIJVls-nxocrQCkew5ydaqRdiPZTpzknHRQCB_zxFqvfjbike88s7y6b44566pECf6aQauGEHEjQYujh3obfAU85Cp-wgRTnftvTHjjaAmQ-hijyReZo6zA0i1HBVFnhvejswu0bWYubdgm-lP-P3lsKTlc-JnPaa87KgLD6TKz8wbTEhMk4hLcPXDf0pQdHv933TaS0BwpbUclOwespMPiSGlaQ-uDlQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇪🇸
لحظه‌بالابردن کاپ قهرمانی جام‌جهانی فوتبال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/Futball180TV/101237" target="_blank">📅 02:21 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101236">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/NxOZnojZ0Jhyp5D_N2HKt7G5Z5wBmHOonJx3uj2bQXpp_H52LnEBB3hkKvwZym43JRkPgSj8KCJyXfhkXOAkVzKxgUdiJa04hZw9m1axr9N2v64z1pKB_zRvO1eS2kqEbmkWkLfMBRtbjtJcq1ymmI2o9tJ9xhZzowdcJJzIdGVoSo_Q54exytTAj8R7vV1hejl2IsBiry3Pt37Y1JC-2Ku2hIOrUNW9fWbg8IJkenFcy7jts_CZ1TS5EOCbhYp1FzChPV5hZw4GlGeYZdx4QBgoBtUC4dYy0ryjqXHA_Wr4VvKvk25wkoDg-xan66NM7N6eHtEwP9TfqcsmrxcovQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
👀
📊
با قهرمانی در جام‌جهانی، شانس کسب توپ‌طلا توسط لامین‌یامال در سال ۲۰۲۶ به بیش از ۵۰ درصد رسیده!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/Futball180TV/101236" target="_blank">📅 02:19 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101235">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lcTaqGFA0K-8jA2riBzINV1esl77KcIrmr2In96obyHNJNXkJ8cD3qWOBnLjC9joMrjoPE7i1nROXT0WjcwyDZFdfzpOSZWyl_-KmWOWNN4tT-sBwDgV5hNGQfUvXrIxuWtQ3coIuxlY6YuRRovS5whF2sg1IOYzn7jROJ6_1UMv3rnO-0t1mjWbWDTiwfQDngXV3D-dJqEBsociTU1b1zOZIaECJ9pAqxQofdWHhPJ3zK3g1oG_aATzk_9rNBKStE-iOc4huyAvrBFfCDXT83Csz0UP3BN2NCnB2jT7FuapO0aL50a0Mug_KUSQqIaBqa5oJw7_bi4oiBY_3J7iPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇳🇱
#رسمیییییی
؛ تیم‌ملی هلند برنده جایزه بازی جوانمردانه جام‌جهانی شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/Futball180TV/101235" target="_blank">📅 02:18 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101234">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ab00af27c2.mp4?token=P4_sDBOfRDIptGU_h89YqzaMz504ylqm0CMcvepnWoLj63zbZ23TD8VbWSI210fzF5ByCYLLjV5-MilOC_coR7Zj2_Qbh3OYGRfRuz4r-yDw65jec9UrS4gZno9QHJdQMlWo8pTX49Pm5aKzHR2MrvtDqvlrX6M7noLhSyffmsHNMSDjJfi24SATcJucfyNIY4BVedpIoU_upUvs5DhGgOu1hcDWpG8F-DN8y-vCIceJLi640PXhCvj0QlnPGpe8tlg5MBbtEvEs6I9g8OQ8XjSK_HMvG55XQ4_4XiH3Syw-jZgblc17NtgcnX5JAgxSPSMgZgWXcva9hvrNVDdmbA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ab00af27c2.mp4?token=P4_sDBOfRDIptGU_h89YqzaMz504ylqm0CMcvepnWoLj63zbZ23TD8VbWSI210fzF5ByCYLLjV5-MilOC_coR7Zj2_Qbh3OYGRfRuz4r-yDw65jec9UrS4gZno9QHJdQMlWo8pTX49Pm5aKzHR2MrvtDqvlrX6M7noLhSyffmsHNMSDjJfi24SATcJucfyNIY4BVedpIoU_upUvs5DhGgOu1hcDWpG8F-DN8y-vCIceJLi640PXhCvj0QlnPGpe8tlg5MBbtEvEs6I9g8OQ8XjSK_HMvG55XQ4_4XiH3Syw-jZgblc17NtgcnX5JAgxSPSMgZgWXcva9hvrNVDdmbA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇪🇸
🇺🇸
اهدای مدال طلا به بازیکنان اسپانیا توسط پرزیدنت ترامپ
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/Futball180TV/101234" target="_blank">📅 02:17 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101233">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lxXr6mkj9cWpAktv2lkw_Chkh_VX-zTafoyhkJFPlrbSMwElbjBcTPeNtCjGVa8fjSGTlRkKWAyIgGSV9ImY-NmZK0VuTFPwWsL4S-EncbgOjQXh53slOMG7L1dqZow4CY9UH0Kev4uu4lNNP69D7k61hnIcNwygSsPCCYCGz8A47_Xr38G6fSpeStFsnU7Q6ECDGxpLml_PncwSi4cEBAM7guSnla99BAb5H6xu2x0YFQIToo1us8H2bx7JPjT84khwUsdW2QjH0AjoYnaIhMMGVavodlCfqoZsH8_UHSmbRVBR5KucAFUSkDhfpqw_Z2h-HB4LFNvNJOGGbg-nWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
🔥
🇪🇸
و سکانس پایانی جام‌جهانی ۲۰۲۶
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/Futball180TV/101233" target="_blank">📅 02:16 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101232">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">لیونل‌مسی همچنان داره گریه میکنه
😭
😭
😭</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/Futball180TV/101232" target="_blank">📅 02:15 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101231">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Rv1P1KlLBfJhNySc7M-lgzPDh6YU-Z5mXltSic0_qsHk0pt6sC3b_wwEl4gsvcjCZFqztDG7xkmafIIxULCoBH7hsgsWVDSKkU3NssBxlkQGbfk8i0mAdeCggakqUzNPC0BRb3Y3Tq-6XR0ke9yYePyhLFZtV93aYQALjurw6eSkhve0iAJLjSLIO_wyJAFe_T4HzovsX9PUvfodwDuUBLsp41Fy5orjMfOhFrMHt187FA7VKhrg3jFEDhNIHaEloCQuO4sK3-YWjWcGt9UMbHPfCIA3akWJKkicJozvYgHdOP4fqposNCLt63ErBmlDgrbQnUznPsltoEIEVVJnfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
🔥
🇪🇸
و سکانس پایانی جام‌جهانی ۲۰۲۶
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/Futball180TV/101231" target="_blank">📅 02:15 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101230">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N4f7cqdU6bwse4FXAv88hX5s30alvqagivj8loBlMyJey9h1IFEhdFXkQEqJOPgqDwln6v9nUCGh-5svTxD-fAkla_0SwZfLgPi_WyYYJKzRiS1Bj_pA-GF8-zCDQNQHkJ13v9io11ssOsoxwll41J35il66j0aAkcZRIQE-BtDNNvxE-AFzzwu9Ny_EimH1TLbwHCCOXwz6LY1jdDcF0Dc4olxyvmDIvVgFC-i29jc91iOW-JtwkitELEa9ZB5PVZKSUetXCi1jkjET9YYNnK87_F0QYN7qTzflYSjoNbZFucH_bZ2TI-CLIFslnyimejxYMBaPlyH54lGRIHk4IA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
یکی جلو داداش یامالو بگیره
😂
😂
😍
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/Futball180TV/101230" target="_blank">📅 02:13 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101229">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fb8a66352a.mp4?token=KuCwbdhcbNAfRvYw-lbMGhQ8o0xo7561gPz5a0JCVRI4zFt0FzMm8cxawcEZBrWJ5RuXz8LdqtqSP9W9ONH6ht4VxyA0XdhnuwhkZqNwUa7nBWcbU0NFJy0dDpxZOI7k7PJJ_6zcPsUmwdD_OYgIdE0ubDvsY2HFxjQQUqP18l-Gp-jKdmVzENYAwuG3Rv5rRLyL388MTcLQ1HrkcPO-uiMKJdoK7HRlkQJdXuuOzXOgc0OWU8PTt2-VpP0a4vbHLNRb46fuW8P1Ip3aVCv3w4cweqZ9bvcDtRo84e86LdiaNAXfIWeqaCkbqq-_j4-EyCf6PpCRdHadIMWeauD-aA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fb8a66352a.mp4?token=KuCwbdhcbNAfRvYw-lbMGhQ8o0xo7561gPz5a0JCVRI4zFt0FzMm8cxawcEZBrWJ5RuXz8LdqtqSP9W9ONH6ht4VxyA0XdhnuwhkZqNwUa7nBWcbU0NFJy0dDpxZOI7k7PJJ_6zcPsUmwdD_OYgIdE0ubDvsY2HFxjQQUqP18l-Gp-jKdmVzENYAwuG3Rv5rRLyL388MTcLQ1HrkcPO-uiMKJdoK7HRlkQJdXuuOzXOgc0OWU8PTt2-VpP0a4vbHLNRb46fuW8P1Ip3aVCv3w4cweqZ9bvcDtRo84e86LdiaNAXfIWeqaCkbqq-_j4-EyCf6PpCRdHadIMWeauD-aA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
💋
ترامپ مدال نقره رو به مسی اهدا کرد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/Futball180TV/101229" target="_blank">📅 02:11 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101228">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e5ecf5e7ca.mp4?token=UgY042zKqGkpfYOu3LGvfO-Wx0rQI9m_QqN_VbwWhEQvMX3BuWrN_RtWPQl_rkldx8W0PqGj7AdfUchxnUx4GWKUJEBPdjdQvg-XYXUE1C-duUWOtYtntfSKfBmsmHld4XT6AHFnTpLpvzc6veyKr1rJGihV4L9Mkz4A-Mj-9XD6lrAL7T-EiyKeoGslYJZLNpigT2s1C7lxpGOd5BuBWYchw8AG6rKRRPxx9MWaxOfnsoRdkI69mHylCto19G0Le_7IAs4F3AKk2EwNPB_APr_38an5uoRjQkg4OHcNMZb1XC7IVYRrACZCdhQnH6tbc99BuMTI5jfVKMl6j-E-yg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e5ecf5e7ca.mp4?token=UgY042zKqGkpfYOu3LGvfO-Wx0rQI9m_QqN_VbwWhEQvMX3BuWrN_RtWPQl_rkldx8W0PqGj7AdfUchxnUx4GWKUJEBPdjdQvg-XYXUE1C-duUWOtYtntfSKfBmsmHld4XT6AHFnTpLpvzc6veyKr1rJGihV4L9Mkz4A-Mj-9XD6lrAL7T-EiyKeoGslYJZLNpigT2s1C7lxpGOd5BuBWYchw8AG6rKRRPxx9MWaxOfnsoRdkI69mHylCto19G0Le_7IAs4F3AKk2EwNPB_APr_38an5uoRjQkg4OHcNMZb1XC7IVYRrACZCdhQnH6tbc99BuMTI5jfVKMl6j-E-yg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇦🇷
🇺🇸
لحظاتی از اهدای مدال نقره به تیم ملی آرژانتین توسط دونالد ترامپ
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/Futball180TV/101228" target="_blank">📅 02:11 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101227">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Cz6_FN3Tb97jj59LZfAvzQ9BOGEPs3YePDte9vEy9OpvxZq-pW0YKNj0HBZSin3T9fTM_Sw1uOCOMUAj59qPf-g0qcGhzs5oQ-qYQFzONOvG2tD0vZt0OTjBtXjq2rhpsnWCuyHJluiOPZuFn8BYajuNXcUIHF728FFD1k12Fz9T71Z9M6iwrrVNBQ9j8bI3KBssXc2jROEMkn_e1nXz0XdMSRF3j7Cjz20gOz3OsqKJG9G0Xpl7CFT3s-Kb0Wm4B8wIGqW_wYAg26TpWGTQH0LOMWZXKiADIP9iBBbGuvHZLs5G1It45bGHOJX3uueb7ATI3iTRGWHjWcJUn-gfwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
اسطوره فران‌تورس درحال دریافت مدال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/Futball180TV/101227" target="_blank">📅 02:10 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101226">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p-hbC8EmYjqDb-9hQh3f_4cOBVSh7KSjXlQPUnuJmEbzgf-N4z2V4fzoFvo6RR37eP3tzDaXIYT0IVkFGmyNW6MepNDnfnB-gLPYOsY62PLaXmCbiN9BDlML9nx5v5Jx05YmeBTRukU115NwPb0TmVKImcclP_SCdkYrtaB9WxKRgRGBHl0OlASktUT9rQdneY5I3GdckOVhqbyqr8ASmGYiny6F64WEfgENelf5ZxBUY2PczK7-ItHcFbUD-Rwinq3ysOsh-BUjenkk0X45Sf57LE5cd9fhtTB2_SONwMYBFCXD-O5Krfi4XJjVhWUrCnBExy4QSsr1226hcDbriQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😃
ترامپ چه کسخنده‌هایی میزنه دیوث
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/Futball180TV/101226" target="_blank">📅 02:10 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101225">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H3rRZ9_g_CTuj9C9blX2VnQAbA-iORfTnCd2hDrRQzg3tlsnJwfOucVra_IMX5awddOy09TofzrA1wA7JmKYeRT-n8nGjoHZxUvjW-WDd4GS5u_CnpJj6l1RvhN_vZ3NXMvIrS9Xyt5nhKYUIwapK_AQUMBMtVul06na5YEtYnX1dk0hl8wdg8zWe3yHG3CI7KV9N4gmBSDqRcVEjfbLjXgN7Y5h1dFEr61bwFx40Qf8py8JFxL51nxBjvfLBpgU7PBvByChZTR7W0Ut7-uladMSEN6aoGYrbnlf4gYcoy1eipmq19CQqa6cpxBu7QX8Nq0FJpoHf6FVwbLB2Qeh2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
چه اشکی میریزه اسطوره
😭
😭
😭
😭
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/Futball180TV/101225" target="_blank">📅 02:08 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101224">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mR4IxRof6qbP17q7giZGOrJdH_zUF2xSCbZ7VBETfi8UPVizTku6SlR2HprTTdIJc4PnS5JcxZm7tms7pdcGbRApdy6R4WBUhF7C0LB5-Xlhz116ytGnVreP0tHKIAZ2o7ooQ5koPoM-47n2d1mTjwpOC8eFbEBQr_wM91e4e2GIQsgXi-vwC0bBCNNlRiZmF84kcpO1HdPb4OWQ2d1NroLAY9n-DPW53qg2PbIWee_YNyDgFv79z5m97hfQm6BeLMT1LMhYnJ1cje3ccDEzgbrPzrg-kh9H4mA6oxrRqc4kNF18UVlM1anG-fRsw29Q9HzYJTkMlJyU45W7Q-61mQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
گریه‌های شدید لیونل‌مسی
💔
💔
💔
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/Futball180TV/101224" target="_blank">📅 02:07 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101222">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Aio5iUso9XqPB9jUbm_CxzVRBzMnv2WPUxSbYn_oAB8eSPxWQMAV0rzUlIO_LLsJu-iou8UWydoVGa9tFOSiCfuxpojScuDPd6dpjncJjqRiKwIwBIZmHWeeErwwsWrZeMbds-9mDFi4wk6tlJi8jsnNRn6GdUK8AvJmWetNCakAIufDTtdGLZummJSvtJa8chcNWlUXz-DeCr4WvLChusoOvTKZvm08sTQ8R1Q6Ubz0kolaIdv4kKbphWFZXgNBaS-4oixh4nWSZG96zoE0LKSqm3q5rqH9F-VsGk_cj2W1qD5pCLE6URFGfovC0PHgign75jvzcFOEKMEF2Qwc7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
🇪🇸
جوایز فردی جام‌جهانی در تسخیر ماتادورها
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/Futball180TV/101222" target="_blank">📅 02:06 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101221">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sjrDx9H6m_X2-nBYFG6f_7t0C-IEzBe94nI9FIuezzYjQmqbjNmc7bvUAk7ZLV4D6LwflTQFbhUSP7ZKgezK8RE6da_oQxqgSuKhNzO_fUM_xSXNISGXWMq2etV3NbMR-CKdzv2Lwhntp6TQIxOZQozg9apIjTBPr-daKonTtavfPFS8GJmHa-l4PXIngkjRvrtH57k6fPnVU4j-JC5-Y6fll1e4_bVxrXErkPNV2u8k5BaPTw-EmonQ4zql_rtPg0r8nBq0qYqqTJ584aEQz9tSWrbD6MFA5M0NOYZ6TGgsFT9AIMb4k6DG82JG6NbulW8DRiywiHT-dJ4i4J4t8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🇪🇸
#رسمیییییی
؛ توپ‌طلا جام‌جهانی به رودری رسید
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/Futball180TV/101221" target="_blank">📅 02:04 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101220">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XsK5UW0HPqeCH8rVgbrEdJTEmdshE2STkO5iWZXiQuj7p5PF4J6dYSProfwtthlgzAC2MNt8qGuO7kG8pUFiUxMupoEzkgG0j6vUCZVdn_79a6-QtsmH1qNtmNNM4Z-jHEFVrJZqVps6BCktn0WHK7h6H0xjBslwvNtu8BKA6pMZHmsvuw8xhKibjKRY3R-dr5Os0NXiHxiYEFa7YRTAv1hYGvKnjZl3h-peyt1lp2ais7uq1MCD0WkEHGi7SnA5aUIk-QEFO-AIcw3f4AHaYa8Qa6-0P_ugjY-aHccJtoVIgFQmbCWXfpCkMCCB74vxvImDFwtwJfssvHEGfetqeA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🇪🇸
#رسمیییییی
؛ اونای‌سیمون برنده جایزه دستکش طلایی جام‌جهانی شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/Futball180TV/101220" target="_blank">📅 02:03 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101219">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vUIOZ_8GBL8cxjbvPCovfsb-Q76aMKMqHtL-xpPwENJxOkcuLxrMjWtO8Ph99wH5CEXpH5QASNrD_bFGSPfPO7gkMdlF_4sMhRvos178jKDqVoEiIyMOwtucfx2nV-jTESs7qrlu5lGCier9tDvX6ISvygEwbYe_Kxeob5-BhxcCjsQa4hy-Iz1ZOEr2P2OQzzlL9_-xEj791nD7EEX2FAmd21A376gm--6ZhBWScfR0M3XJ0ijVqBVjia3Qi4GDze-HthEU55DBhFYssY3hni4xIqQsUfep57DvDp2AifZ2q4HB3OPUMBDkzjLNhRjIcJTHK6q1tiwQ0ibJWsqtBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
👀
دکلان رایس تو اسنپ چت
😐
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/Futball180TV/101219" target="_blank">📅 02:02 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101218">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Wsf9vZxdT9vW_CtBD_tnquU86UR6ZLdJRctc2MrWlWcF1fcLzymMkvbFiod0Q_Hx6Qe8ZI5Uy2V_JXaT6K7aPcyYellE3A6DmC2lioU85aR8LaifKJgm6DzSOE1JnmSO18YZnwL2UsP3W8BAanr2zMWcizM_y__b5THRE7gFh-maWZ--swKpk5vNfj4Nd5P7NMhPBxdbImQMho9ZlqouQOwnYSIg9lHg6diAd64Fho8jMEFFwusjiBGJOvQffCsOKXEu0sBDQwFX1OqUkGEkEXSOmb3JVx8VyO0yxuqL8d_Fd8PpdbGUUdg776Y3b2E1mMVbPGZU2_s_4LJ-9G8B-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✔️
🏆
داوران فینال جام‌جهانی با مدال‌هایشان
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/Futball180TV/101218" target="_blank">📅 02:02 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101216">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">ولی مسی اگه میدونست قراره اینطوری بشه همون موقع میشاشید تو اون تشت.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/Futball180TV/101216" target="_blank">📅 02:01 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101215">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">اسپانیا به رکورد استثنایی 38 بازی بدون باخت رسید
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/Futball180TV/101215" target="_blank">📅 02:01 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101214">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lKII_cfQe9h1aR0cNix__U2IVhTa6uHWACYfTfc98t-q_JRLL7TZxde3c1TS8FvXoZGIp3GvFYtIw-jw3w9TKEzynmy-z-d31gwoPNLH71Dj6jExJxJpiGjonE6ZkFeUKlIDLclyXbqPlnKizmCwgXCYAQDjpA1hOTDLQc45gl7GLsgvr_hjY1cUMKjwQCBoikMSYWcOD3WdUE4gsRIlGygD0MdHz87Oc_PYUCi8Q7wgm8fBjQWS_p1lILhvYZJNk5AO6yzwFe85u1cpaOz7eWe-XbClkyieWjcRSawSUVYGrU5dejHY5JbicKhLGgQV_AVCxqF3GshR-z7jTZxhUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🚨
🇪🇸
#رسمیییییی
؛ کوبارسی ستاره اسپانیا بهترین بازیکن جوان جام‌جهانی شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/Futball180TV/101214" target="_blank">📅 02:00 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101213">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M2xSrPubVmvvtlxOEHxDqJEn-wZKGJLHpN-LlFdI33WXfgsor-jEpPVJmhYslZ06o4VBdxfyzPgq8A6HBJHcwSmS0fKQNd7xj6S4fFJxfjU0nVfYUEEjYMVX9hEmHrmpOG6C0NQE50lnK-O9XY8wNg3htqt5lD-A2inCnX9pAW6ISBM2oKKG3A12Z_5e6XPhqKg3zQ70pTc5fz_OqOauBKaVcuSIal1zT5pJmLkw_XmQNzJlwEWBdlFCqCJ7r2xi7s4YiSiCB1Vc3PolNbwek6niOuQyEUplv8MJIXGU_CNkfebuPrVQqN7KkRPilDUpJSjN63qzi_GBQe8oC87jkw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
🤯
برای‌ پنجمین دوره پیاپی EA SPORT(سازنده سری بازی‌های  FC) قهرمان جام جهانی رو درست پیش بینی کرد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/Futball180TV/101213" target="_blank">📅 01:59 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101212">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/knov_zMS_TqNclPqgZQwzmepkhgRro-98CHm_YKFMuQJjjLuB9NIzFa_kx8_gWCkkmTsv6jCyev9nUxl18OU2WtmCx4MOzFBl7vh2aIXfPuIDhXlM-nZeX8-qHSugs4GXtoZ-WFI-Hso-wTJ59vvjfYVq_oGCI1K04zGPdvKoaMYg4UXJKEeL27zEWkilrZRBLWwfQu-oltr5cOvS4aZVBcLCf6DHOHVtPdDsf5yAcgdv57p8kNjPHey8ibpwlkWfO_Vv3BoytVFkVyZ7bjtIBCjy9_gGW76SkfKu4xGXTYHse0HTNotXVBT2y51fZBlg_Vw7Ss1PgXtnYEyu2_NaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اوووووووووف
🔥
🔥
🔥
🔥
🔥
🔥
🔥
🇪🇸
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/Futball180TV/101212" target="_blank">📅 01:58 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101211">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nWoUo9_8_9MIHEFEU63mzzGecOWysRb8V0ZogVLIab0mMXSHzRTvp62LfO6UbY2zAYxMLVKJuKo0JWPUoN_luZQRvr9TK1H0jSmPQpvmpXFzEM_QMBNrbd7FUFFatn9YYsBWyOsRhH3XOI2anMuedtMDX88DJVfKdhWX4usKg9Piq5L0T1jNNsdEFTAdrrQoPb0DL3W3akqbJOzX-7OiJzb6GVahSiPt0uRQ2hsiyuH5clgmhBdimqhOiKjJZfdnPI9Rv3YpJdwCAz7TDOqV6sRATRqFzweYJlOGhk4fWw04u8H2EQhNH8tUD_1qvdk4K_v3UdkC76vPc-8Wuun38g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
ترامپ اومد جامو بده اسپانیا.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/Futball180TV/101211" target="_blank">📅 01:58 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101210">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EMGb3VP7tKcOC0T3SaCOYFBI6v1a6vUqUqKUGMPIqoqFfeiQZWHbX-890VVeQOoLC49fwSaABV5wQx1UHqVMouLojU7kIoUknvnoElFtJluebRGlr1xRhTl-n0ase-126r9ctDQwEy6KdV5VVGQrlkrA8hbXZ9Ul3a2z_BhinLNKxyCpbOaSkL-VCib-haWY5Mw00Aw2TOJMw7GeVl2Y06MW9HsBxxDg_1ne1zsHtSaXzlYXgoeon-pgFKXDOVLj0rMpToxOvxNs8Bwo7f97TKjrRMcD4KLVnJwoRVzU0OQTINhJAuBTzKq7imP0qizorsC-DluBTiANCdSYfWUAgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❗️
لست‌دنس واقعی
🔴
مسیِ ۳۹ساله اگر نبود آرژانتین حتی از گروهشم صعود نمیکرد اما او یک‌تنه تیمش رو تا فینال جهان برد و تهش به هم‌تیمیای خودش باخت
🔵
تو خودت رو قبلا بارها ثابت کرده بودی لئو
ممنونیم ازت که حتی در آخرین نمایشت هم درخشان بودی و مثل همیشه روی طرفدارانت رو سفید کردی
❤️‍🩹
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/Futball180TV/101210" target="_blank">📅 01:57 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101209">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M7WEJK-vJ7ihUGtDw7jkcM-n4BAnfrO2qVoDMnfy0ATbqIFzWxADFJgyAdnpFCm9w9o9ZuRJqkLMyrWpWBefn4_s_MHBd1VLIueWGEM43OGLisinnZXpWbdH8xungA6Xja9We5Bj70i-gTa_7Z7llgpo1qelVYehqxYDHx9bdSow4JsbHJvmQoI_svvE0W3D-IbKR_2ozK9WT0ZKGKyUH0SXhX39Ats1aaSXogQlG4wUAopmCGkvek56m57zw4JaKngeaftGceP-VOrzYVzeF5l9pB0uVWZXngAULblVjmoiNomWOKjsPa8pKGzQz_uc_g0m5hz38jljZDeFS-kahg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شکست، تنها عددی بر تابلوی مسابقه است؛ اما عظمتِ مسی، روایتی است که از حافظهٔ فوتبال هرگز پاک نخواهد شد. برای لئوی افسانه‌ای...
❤️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/Futball180TV/101209" target="_blank">📅 01:55 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101208">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q1Ex35YgaYN3hbmBdE1F-biu6OCsItY67l0LLBdsBl5qaJOzGZLfeR7OUTJAuxrJj9WGflBYQ5lBuF8H10QEznMnagIdLvCXqErMldZ59lxIbQfekIaqKSmUEE32xzDWTX9FGv2HEgu94GhLsERX_ZJFuUR2eMHxOgeCGsQSysrnJqyLHL4P3ZDXjXtUPw2LID8CNHuWa_DyD7gJqJdBhN8nU2t8KYALdGTDXzfUBjutyZbDZnwS--MyeE00Bp-PvzPqFcsloxpNqzCJMy_WZsYSqR_-fvDhlMzSZcS34LyS2MP7WwYaGO6RszIAjuBBARjeJhx3yZTwSi_tJKwc2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
رئال‌مادرید قهرمانی جام‌جهانی رو تبریک گفت
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/Futball180TV/101208" target="_blank">📅 01:54 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101207">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nATPxneBhnpNGh5g6PXjP82pFtpl391RKJdIRyOwCp8IhYDZnqog1jFg4aUVwa4bmic5xV9EpmRf9tLDFSvjeNS6u3UKqrDUXKgqpKA4HG0bRgT4rfpOpWINvr8RWC1Ffebb3w_KkCbgf8O7EijnSrQ-wL2F9cdzvAQTmS-vKcK0-WRBTX7lUbMCtkXIjcTnyWhPO61oTJtwEQUTY587J6ffYf20mKSat7YgOuqX4HmECZUQhZQVIWT-MQ1cZ1ZfFXWRrkcw-1ZjuFHiNibBlrqxSpoeEAz4G0KxhZRYpHooeCgpzNxawQezSdN4Dhz92MOb06ZLbDL-rEyJjKtq3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
فران تورس و جایزه بهترین بازیکن زمین.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/Futball180TV/101207" target="_blank">📅 01:52 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101206">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C8XTY94tT_-GEqyt15Zc51hbaDfKZg-M1wTei_NnmPIPG3HKFxoMlaoV9yPdX4rXIKf3nY5A9AYh6Uyi3wCFbpRnasUFXms4oy-iWs5_iaGcig8IKmp4svPXlNq2cCLtHPD8FcGk9DISn2R9ayTHA1RsfpNf-abPxsKQB76NpQtz9WxA7LX7zcNryjssnSPeV8b4qJsxdSxJZPjH5NsgqhQ_nIfq93-lBCNKRYnzxFDPZMy7QqmTNNEjGC5cOd1yHIZJY0Hi9WnK0fUXKxMRk_0diPqY-b173s_3ub0vT2nQZ-oiayUeHu0TUPN61YLIN2HAYJMWXnj4qu2iZhA2BQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شات جذاب برای رئالی ها
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/Futball180TV/101206" target="_blank">📅 01:51 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101205">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ba340362b1.mp4?token=v6ku9vF0PpA_BsrXWMY9SnUkTzuJ8fANzemmSmHcxwkpeVNc4QHMBo8uMcAxnab0WeY2jHdCjZQkOupuw_dNaTUhS_NMWsD5U3eJaedy_mTjTl2W7tdFmrCKYgNgt0toJ4AUX8HT1vMKR4li-Myt35L2CAHHADWg92C-TZC4Luow1hKItgfpauzQnBLMMKKL3VUQmT9k-ymZxtufC9o3nA0dvVBptvY7-Jba5M_mubdGPXTsCDog-lMpinpFoDvwfB66T1lGXffd37sJwx_a4BP7Q4ShKzXYKLb_FV_OdyCWCKBeCFa6aPm11sveIBi2xOibQdGwwBRlXjQ5rUxSlA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ba340362b1.mp4?token=v6ku9vF0PpA_BsrXWMY9SnUkTzuJ8fANzemmSmHcxwkpeVNc4QHMBo8uMcAxnab0WeY2jHdCjZQkOupuw_dNaTUhS_NMWsD5U3eJaedy_mTjTl2W7tdFmrCKYgNgt0toJ4AUX8HT1vMKR4li-Myt35L2CAHHADWg92C-TZC4Luow1hKItgfpauzQnBLMMKKL3VUQmT9k-ymZxtufC9o3nA0dvVBptvY7-Jba5M_mubdGPXTsCDog-lMpinpFoDvwfB66T1lGXffd37sJwx_a4BP7Q4ShKzXYKLb_FV_OdyCWCKBeCFa6aPm11sveIBi2xOibQdGwwBRlXjQ5rUxSlA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
زد و خورد شدید پاردس، اریک گارسیا و گاوی بعد بازی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/Futball180TV/101205" target="_blank">📅 01:50 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101204">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hvmKr74Eydr7IYqbkAMq3j48dLcTGSV_JTreYcxANAfFk2l9h8-Si2S4S5HWqSV3wZqCo4QtUkk0fHm88s7T4cbuqJ_e4XJK2XjqJ0IsB0XUwkbZiX-rgIPtWaoZfCi9ymM4sAjx0MJqQHV_FxMlJrZfKRLM2G0339kFnMYwpafPssRfYSCGXPjrHPF3HrqngWEEhEomLcEoxOGSN7eHDbMTCmYfNBEWF6-4DS_ud_QpHVbHNnddJiNNTzFI3y05AeS4qsO37ttpcccXroBOSQ41guyp-agMW8GYwahlnzT3HUoh6e9E5Ynqz3n3xG_h2QtSTGgCVwYKAsrAOkbypg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
فران تورس و جایزه بهترین بازیکن زمین.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/Futball180TV/101204" target="_blank">📅 01:49 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101203">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fmOonw5jpnj1k19oZaOI1ykO82JCjZksZyjBFDrEDhU-uI91NE6A3UW9XZ3oAOJeTNI2ckSPc3ovGJfm7G_6Pk9PWRLnvki5ty26d5q3JRMcqCMzaqrQdfw1h3UMaIlNBBKqP2_ByWWlHyytfQP_iyebKA9nD1KrJ_0bK2msTCBVyCdPUT1GjHVljn9qYS0lJxyg2-0PzPbpQJana7D2UPSjrY5Rpzba9Z3u-X3o93Ruau1mCjjkeDkaj2kzzsY-12h3bi5-Es51CL6hsPT4q4nKFZJ2Ajd7QOn4LYjnEPs8wre2_yjvQ3rBANC4Td6F4FoiLCrMuZrwl5STGTcbgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🚨
‼️
کنایه سنگین تونی‌کروس ستاره سابق رئال به آرژانتیی‌ها: فوتبال برنده شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/Futball180TV/101203" target="_blank">📅 01:46 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101202">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nG0A30FAgRgKlF5RG5xOIEfwAJZz1F4rqe-BuDWk_IPU4gFOtNPaXx7b4EykQ9iBbA2DKvzuPJkxp1UFZFCzTnAK04hRImbQpFCdQNfR0Xj7v59Jn8m85uDZ4Ih1LvrTGGUjW3dxSNIMRwrhToGjyerKrU4ag-tD1eIF4lbzU_U3A7a4iGRc352EmAnx6rHXAeO7HzZ42hQLtrfI1_77-LbYcr2chLTJ8IeFdi5u7b-EHzn6qHGDuxYKg62uSyNJolAv2Q5kh8yTJfGAhD_y2SM8BRm2rmHf-KCRGjKNkxmj1iYMTeuMzI3LuDcoyNkAPP2xwjEtzPovOopgFg7R4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تعظیم برای بهترین هافبک فعلی دنیا
🫡
🥶
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/Futball180TV/101202" target="_blank">📅 01:45 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101201">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JYkLA5mE1RPyKgQKIdGxS6dSdcNn8_J5eldevfPkdqGGwCvTuGcEYXyVzh_nzPVhTfATvH22LlbvBDTO7gHyfY_Qlo2bg2HkWMbyK07W0KbdBjsFUjbch35lFfwBInwjOm8xAuM0J-jzwg3q0xwOdPxK5ov9Vd1u0I7d8i83WfmSYeQKOLa3EeriuqvbvnD-tHpePSxYB7Zqu96J6IBSXgg9vMp2OIj57U88hwl4tqNh8UISgqCEtvh2ZOBYry5MszitYIc-nSGYPUUN_PypDOl3DGEy3hBC15b7ccgxO5WHlO7MuWvtUYOr5JBlTr3KYlMQNzZb8b29_yrtsZfDPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙️
🔻
فران تورس: وقتی مسی در تیم حریف حضور دارد، طبیعتا نسبت به حضورش احساس استرس و نگرانی می‌کنید.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/Futball180TV/101201" target="_blank">📅 01:44 · 29 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
