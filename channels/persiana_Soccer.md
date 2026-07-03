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
<img src="https://cdn4.telesco.pe/file/sY03fOO74UUqHjBwbIYUHnNakDRd_FWvEc3vMxQWpkj93fGTSGMN6vRgHYzTKCR5bZSoPIw45Dcr1iO9XknY9TmLARE62SAylc7G1tQgTTkjPsgZJ7TB9-DrkDfW8ULn3A5SsrC9cijMMOHJ8qRMiYSNOj5P0L58VX2KILWL99yM8BOqIBYqmea4WY-JnYIVUVUW8Pfsz8l1_Cgahn6nF4MRNM_eZu8GV4TvQoiCBs1cs8xGHvObU3hHGWzRDCu2HL421TSTJo16cNhU7Fl4esKuoKTM3yvphoHXKrqxsdmdsxf_H8CvYk_bkmnpMZq0D2t407-vBp2iYBMlr-pLdw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Persiana Soccer</h1>
<p>@persiana_Soccer • 👥 360K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@ads_Persianaaپیج اینستاگرام:Instagram.com/Persiana_Soccer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-13 00:05:52</div>
<hr>

<div class="tg-post" id="msg-24890">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pGaaE2O5eSUqc61cgNXsuyARlieWXVdUPfvKDETzhgebqZQzj2baLQTYe8gy1vCxWvEic56t64t_jRajmUR6xRnDzRV7AS-Rr0ofIlqaq-S44jtQqRlPJ_csw67IEM6eRnUg6dOXaYVKJh4tM0g01HSThD-K7HL0FxXqmnDAvBfzuvP0BLY__kO4SnLbgX4HPU3u2x9LgHXQldGOPyngOZgsdrsdQg72EA3EpFhAxN_9drEjv6Ba5rogeYgUkuiXAwmfKUkJWLrIuynDQUh8llqmG0c-t_W6M1nsbElpgkB2IDH9Z98T2pnSrkrB0n4WI2-pOI78qmpziG_HDireZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
باشگاه‌استقلال بزودی خبر تمدید قرارداد علیرضا کوشکی بمدت سه فصل دیگر رو منتشر خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 5.05K · <a href="https://t.me/persiana_Soccer/24890" target="_blank">📅 23:59 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24889">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RsUElJ4kEmDTovOTQvhYxD41_rLQNv1wiGk_FKfWn59-urN8mi6mnHK7VnzkUHuu66hcbDvJMTpv13B-xOasbTzk19LrbQJ7KSGIIi7QnOxhqAhOL2EyiK0BIiCTj5jiqKQUPyUFdA69zdpwDEx9rNTUtCxs_EoIqarFlRFN0jweEmgSv9yflR8u4eW5DWmmdcIC1qU2BhfmPKoBjvIMBSU0VPlFMLojoWPhRqx14yFv4Azo7nJHxeneCY3cP4jIrAOWgEXwGEwT1mH4_nLgsAgu_J6cXtN45u5-rPXkrxxQerXBQUzOVKdBMeYcKKWXpmbFUeomPph18hJ9watvvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
#اختصاصی_پرشیانا #فوری؛ نماینده رسمی دراگان اسکوچیچ در تماس با مدیریت باشگاه پرسپولیس اعلام‌کرده که تا 48 ساعت به این باشگاه فرصت‌میدهند تامشکل اسکوچیچ رو برطرف کنند و این سرمربی کروات همراه کادرش به ایران بیاید.  درصورتی پیش پرداختی توسط باشگاه به این…</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/persiana_Soccer/24889" target="_blank">📅 23:40 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24888">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tO_8rJU3qwUeqycduwFJI1-4oF03sB1krJqGnDakoKHjIYf9OTNPAbaRbedzoo1YkUTls9Sy1SfWyqNhGXbAUEgkI3Mb_Cmblz73Nwnyd1CHgCB5l5Ov1kYI9boOOgA2BoXEs0fM6DdOWeOpc5twGJAfIrKdSgdlDY50Ey5MJkKHlSevXUvWRrmsP-wEdaaD0vQoY5ZyJdmY9_LYS5UWEMItH0y-VFmfj20CYfe2PaxwL8UDdfEzSqXGxOpRoeHFmEojU6dOAXDr99Ayby0Je80kxG3BBbsoeJ_hdaGATLQYqz5Gz_W_GwDNCnj2geWviE3A2D_lDhnOVpPaHyQ8Eg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
همانطور که در روزهای اخیر بارها گفتیم؛ دراگان اسکوچیچ سرمربی سابق تراکتور پیش نویس قرارداد خودرا باپرسپولیس‌امضا کرد اما اومدن او به ایران منوط به پیش پرداختی ازسوی بانک شهر است که بارها گفتیم یکی از اعضای هیات مدیره بانک شهر مخالف جذب اسکوچیچ بااون‌شروط…</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/persiana_Soccer/24888" target="_blank">📅 23:28 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24887">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r48c7rKX2P0D9KML4NLF4PeBd8Ykvxqkompp17-A5s9kmR2N4NM36RXFpaziQI4VU8AdCDaoG9tZT5gptKbpfZ3gETet51Vl8oY2F-VAQr07RYNT-av97h7t88q-1Xop2vLEbpoBQSrJnAgXMtXqHdI2aYtPcneaxd0-8LQ7V75vSBkABVQW7je-A__e_0HWlzn4fDlrjRBAToJH3koUx2JIIrCwj9fWqT2mc0z3PniJAmyYRGhMazc0mO29sRg9HLMID8Mz_csAMRNRUCQPrue4tUthc9X6PdIwU5FpWQ9lrtObKNRPgB5-y4z67Nh8-VbtgrBd9908UZuvbzQ9bg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
🇪🇸
تیم‌ملی‌اسپانیا بابرتری ارزشمند سه بر صفر اتریش رو شکست داد و به مرحله یک هشتم نهایی جام حذفی راه پید کرد؛ حریف بعدی لاروخا از بین یاران کریس رونالدو و یاران مودریچ خواهد بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/persiana_Soccer/24887" target="_blank">📅 23:28 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24886">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBetegram</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CHTwD5F0k3TC5lLObNGIGmLs4oF2SHrbBzmRkywxIsuw6Wq1_rESuGoUn-G46LWs8W2j-qZ_cqZNZDKE-ICrbA1OpTPpkTZmUDljX_UVFuqM0ghn0hPtDXohKg1ToC7GpeFDf097gUE0DWYckSw2eWZZJBZQKeyfKrQDvddzq77SX91Czib747bOrt5femvg3aHux3Tr8UWrq3JyJxBAbmVJhpOzvrryKHX7Qk24Z7tYPC6a51Zd5zK8btHYcqc8PDQHSdveh56jXXBAvCA9wr5vn8CCK-wIv-vcJ7xoNGx-YypTgMNi6Vy2_c6cTxh2h8-2qzKAoTNGS7N9kHKhIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دیگه لازم نیست بین انتخاب‌های تصادفی یا تحلیل‌های زیاد سردرگم بشی…
🎖️
همه‌چیز برات به‌صورت پکیج‌های آماده با ریسک و سود متفاوت آماده شده.
🔝
فقط
پکیج مخصوص خودت
رو انتخاب کن و وارد همون بخش شو.
🏆
ویژه مسابقات جام جهانی فوتبال ۲۰۲۶ | ۱۲ تیر
⸻
🟢
CORE
📊
انتخاب‌های کم‌ریسک و مطمئن
🔗
ورود به پکیج:
https://betegram.com/share/betslip/ZKTRF62467
⸻
🟡
PRO
📊
پیش‌بینی‌های متعادل با سود بهتر
🔗
ورود به پکیج:
https://betegram.com/share/betslip/VGPXN72923
⸻
🔴
ELITE
📊
پیش‌بینی‌های ویژه با بیشترین پتانسیل سود
🔗
ورود به پکیج:
https://betegram.com/share/betslip/DACCB49184</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/persiana_Soccer/24886" target="_blank">📅 23:28 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24885">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r_-D9cQgTTkYv3kUsbiyAag7xF5uxj1ph2pU9D5seGWTqYM-6uO9y_B8rWPXb9lIjFElQyQU_RahdEJ34RW18V1HkuB-ooKLaoL55NASpfFEnYdiZyp6VHIN_LCl6fkww2ILO66UwoAujrWwwzYcrlB-eBAdqSg41ovtmD-X2WdgRFjLvMK-_x16SQF0gik5PUAbgX5TeEqtG_q4KNd8oUI41TGJBsGV0xil7aTYuDb40r24c8-yGntYZ_DHORK77UD-eetdwjH_2WzviOOdpM5QuFU9B2mqmrzk9fnd_aIQ1Oz7u-p2c5KDjONSGhh9Zz2bhGuhNEbgHQoKkT-wsw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
طبق آخرین اخبار دریافتی‌رسانه پرشیانا؛ وکیل ایتالیایی باشگاه استقلال عصرامروز با ارسال ایمیلی به باشگاه باردیگر اعلام کرده که ظرف دو هفته آینده پنجره آبی ها قطعاباز خواهد شد. وکیل آبی‌ها در این حد از بازشدن پنجره‌مطمئن‌است که به تاجرنیا اعلام کرده اگه پنجره‌بازنشود…</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/persiana_Soccer/24885" target="_blank">📅 22:54 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24884">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KBWr_Tiw8MWnk1ZRGpCYIimhAm472eTGswDYhBWyv35b4OWBXCklfaivUvp944RjGcTSPP91hqAH31N4c4G0Z4ytQN2tWeJdkRCiMR5GMTdkMwZ2ytJZMNO6UBJgOkJRsMknS2JFqRflKhYOoNhBaJzH1iQQFmiaM9Lk1E7HGNxoWr2ptd8HgqJof51_50QPpeMmrvZKnCI39Cq8qZG7oieGHtxeBi5edwGE4z0-8z5u4x1hkigZSlPAt7ifWbGt06ulycyAjUBXJ7F-w25w89-2xwrUGweQI2AnleXfEekc4mxsH6iY_wgM_Wkvuq1JB9Pwv42U2u25CkzLwditMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
هلدینگ خلیج فارس و باشگاه استقلال برای پرونده بازشدن پنجره نقل و انتقالاتی آبی‌ها روی هم 850 هزار دلار هزینه کرده اند. وکیل ایتالیایی آبی‌ها هم‌امروز ظهر ایمیل جدید به باشگاه فرستاده و گفته شما تموم کارهای‌نقل‌وانتقالاتی‌خودتون روانجام بدید فیفا پنجره نقل‌وانتقالاتی…</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/persiana_Soccer/24884" target="_blank">📅 22:35 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24883">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fee6a7d4a2.mp4?token=rN7n9BFrkI5Mcp05D_AcN09g4up1DA2drSSbT6eueeK7Jpq_d1i5q9Ffqwjt5Q6abGNTZV7t043Q2Xvzms-RjxTMdyxYEC1P6wFipr_AxG5B1hGVDzMLqferNy9g7h1p--F20A0Vgwr6TYe0yd_BTiKadCDvxTAN9w74ED0qGZRx4o0vFcUNCwXtTR_CjeFyKB4WY8Nn6loFZcv4zsuiFQfxqMMNJI6YzDXDlhK9NmauMwkb8g9eN9Y7X8q4MIsLRUvrZF8ZXFUQCEc97deq8v_IMGwQE1ozd-FcVhZVZAp7jj8cJ6q5o1F9y_jhfHAu4fdZLTVhYaU8KqnD2s8PeQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fee6a7d4a2.mp4?token=rN7n9BFrkI5Mcp05D_AcN09g4up1DA2drSSbT6eueeK7Jpq_d1i5q9Ffqwjt5Q6abGNTZV7t043Q2Xvzms-RjxTMdyxYEC1P6wFipr_AxG5B1hGVDzMLqferNy9g7h1p--F20A0Vgwr6TYe0yd_BTiKadCDvxTAN9w74ED0qGZRx4o0vFcUNCwXtTR_CjeFyKB4WY8Nn6loFZcv4zsuiFQfxqMMNJI6YzDXDlhK9NmauMwkb8g9eN9Y7X8q4MIsLRUvrZF8ZXFUQCEc97deq8v_IMGwQE1ozd-FcVhZVZAp7jj8cJ6q5o1F9y_jhfHAu4fdZLTVhYaU8KqnD2s8PeQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👤
بامدادامروز دربازی‌پرتغال-کرواسی‌شوت Cr7 به جایی برخوردکرد که شبکه 3 مجبور به سانسور شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 32.5K · <a href="https://t.me/persiana_Soccer/24883" target="_blank">📅 21:29 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24882">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PFO5eClSUwA3-Eyvjq4pK3-Jjlfrt_M6pHcuzVhBgHSPEESQI9f5FKRCafWZoHDXRuzD_RqbOlJIvLRWj8B5rT5BFB8q3k1YzKdOVTOeTuQfqQXbtM706x7Wa8lhRz9m2OvtkRFRKSH3JnZdo9vKjz5NVI6i9-pwuuhVHAn4XWefz5qHnWgcYMnjf1pZYTyrpT3YrIslzB4lh6a0F4Ok69LAe49q6VEUc2tOuRcRSSbOgOL38tTc44vlRKYYRv_NPjdJpptAoXWyZolLmvvad4KBS-MITBwdAEPLBkrMwoqion7PA3QlRS92oQ8ALi_5rzZaiyXaoOIPy_Qbq6eIYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🤩
رودریگو دی پائول:
یه بار لئومسی دیر به تمرین آرژانتین اومد و من‌بعدش به‌لیونل اسکالونی التماس کردم که مارو بخاطر زود اومدن به تمرین تنبیه کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 34.4K · <a href="https://t.me/persiana_Soccer/24882" target="_blank">📅 21:15 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24881">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IfPi4YxYvfEC9SrGLjRyrx06jCWgJTHrjoxHerPd20QLMFdJvAkgpqMpH6WXOiJ0uyONMzQsiZBid60AwyEsFRF6KZ_58c1Ba5BGeO5HBuM7mLV5Ase_W7QgyI2mEmTmznLDlcrxXupba43aRGjglyoOckgQabMswOQJUboucg8xV_VGGBb3INcAyUWkSzEkQQDjDM81zQcIdOI4D_QpQCC-a9Xusk9xcX1JHj7nA8luR2wM5dBwEop-d2hFGVrsjM7FVbDZ2XtIEr1eRtm0klKt3k-T0Wb3Ch8G5EpZi0U4fnlHWBODGn-LVeDbD4_r7CYcL2TDuc-6I3JM8ZfbzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👤
علیرضا فغانی داور دیدار انگلیس و مکزیک شد. به‌امیدموفقیت آقاعلی عزیز در این مسابقه حساس. ایشالا خبر سوت زدن بازی فینال هم منتشر بشه‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37K · <a href="https://t.me/persiana_Soccer/24881" target="_blank">📅 20:33 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24880">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FW3DUoUvCITgEOfWTmZHsMUvGRgSvZlOOwgxI37Hk2PaiGPjRoXH97MPQXfFekyxjD7UO2q-hhewAxinYRAf_5XeHkHgoxhYmwPanaKP1dox_mCQ709zt_nDQaPPwKzhSBjPDihTiDfGidn6ucsAXuTukfDBSulf9-D2e01-S9tICd2542imY1Xp4U2HUwdK22d09dcenrjS1oBVCP-Ya3MfYsO0eVWvxPIgvHzZaEfghwUhnKLEZrBBuYTbscuZxSXB8qV1J_c1uRLGVXYaW5AJrnVkX32eUkobH5TOC2SGfggTgLekU52r7yJO14eELZK3hjwZVhuNVDlcwA8VoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
سپهر حیدری رسما اعلام کرد از ملکه پاکدامنش جدا شده و دیگه رابطه ای بین این دو نفر نیست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.3K · <a href="https://t.me/persiana_Soccer/24880" target="_blank">📅 20:25 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24879">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9736fee745.mp4?token=XSHz6FjxGocusP3JX1b222ajkWyFQxa_PTy7T-a95xFWK2JuuyHe6ynV1I6VW6mByu_EHdjYYFfJrjPdJ-Gz0SlIqb1UQe5JWmnkIKard4tuv4gde9e9oH_3N_4TOFe82kt4ceXZSsX6FLIp1JgqISzrs1X0SPpy2wk4z2_NlREjkrPSYYCtwKksnYGGv_Kr9XwQn0SQWNmkBpr-owTbjhKr1RZbrGa071TTZq0JuV7W04k20fAjNoRrNr6EPv1NetzKfXCErdzD27XjbwP4CfUTq5BfQuSs5hlX0IwGAm0I3n5k7nu-uAnyNU07F3dOI4euMirXl85jG7GVa1vF1A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9736fee745.mp4?token=XSHz6FjxGocusP3JX1b222ajkWyFQxa_PTy7T-a95xFWK2JuuyHe6ynV1I6VW6mByu_EHdjYYFfJrjPdJ-Gz0SlIqb1UQe5JWmnkIKard4tuv4gde9e9oH_3N_4TOFe82kt4ceXZSsX6FLIp1JgqISzrs1X0SPpy2wk4z2_NlREjkrPSYYCtwKksnYGGv_Kr9XwQn0SQWNmkBpr-owTbjhKr1RZbrGa071TTZq0JuV7W04k20fAjNoRrNr6EPv1NetzKfXCErdzD27XjbwP4CfUTq5BfQuSs5hlX0IwGAm0I3n5k7nu-uAnyNU07F3dOI4euMirXl85jG7GVa1vF1A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇦🇷
🤩
وقتی‌قانون‌برای همه حتی لیونل مسی فوق ستاره تیم آرژانتین هم یکسانه؛ فقط خنده‌هاشون.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.8K · <a href="https://t.me/persiana_Soccer/24879" target="_blank">📅 20:17 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24878">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IB8Rb9Xp01oC1g3rswv_IwRZn2BfQe0HsT9xFkaw6OQ05jiFyY9hTy_1ZZSMi1nbaqC79SYvpyLDTQkUwFa-jMUBuiFb9z6nsUZefMj6dala7begcfad-tALL7E0W0xIruJTvI5S1pxaz6qrk0W3Qk_5un2pSHUzw-okxFdIhkkbcygQhFMFe_P7gd4KvsM2iTQWaXk2X2RI1TE_8vE14JSm-ZnpQEZFYLj-WrFLENP0nT9Z0Rpqj3bjNgT1J6tCTo4DgIdQ04pUy9K_gLf4R-KdcDz6jD8xXVmrmnBFoiVHOKP-EKBsJESSoXDsN6bxAiQFUNTQYDZAW5db6P8SwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
👤
طبق اخبار دریافتی پرشیانا
؛ کاوه رضایی ساعتی پیش با حضور در ساختمان باشگاه سپاهان قرارداد خود را به مدت یک فصل دیگر تمدید کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.7K · <a href="https://t.me/persiana_Soccer/24878" target="_blank">📅 19:46 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24877">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/459003d30a.mp4?token=njyodFnmz-zbJjlnvkYRxdranaG7G-DTA0B3l0VAZ6RWn2YIMvKZAd_ZN_WMPPnFbh2ulaq9TIQeNbTi1VxGxJpKdksxHJodoXWSTYSfi0YX9biQb8u8pbcdJNzYdEpfjjTZRu6XLMy_NiHde344Uq_i3X0WoVrvVQjDhyoXvCF4Yx4nl_r-LAUBG0a2faVHCj0Jz1ndslShF1ac1AQl1y4MtLuxZTEzyN8eueJH315ftUDFf7zT8r9OxST_lLdkFo8kCdI8KEAcN_xzJmc5itTeh2lvS2nhbM-gFr2e5DXexZtce4DhlXlbaYhPNbmOwUrAB74Z89l_piuxwmYs4A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/459003d30a.mp4?token=njyodFnmz-zbJjlnvkYRxdranaG7G-DTA0B3l0VAZ6RWn2YIMvKZAd_ZN_WMPPnFbh2ulaq9TIQeNbTi1VxGxJpKdksxHJodoXWSTYSfi0YX9biQb8u8pbcdJNzYdEpfjjTZRu6XLMy_NiHde344Uq_i3X0WoVrvVQjDhyoXvCF4Yx4nl_r-LAUBG0a2faVHCj0Jz1ndslShF1ac1AQl1y4MtLuxZTEzyN8eueJH315ftUDFf7zT8r9OxST_lLdkFo8kCdI8KEAcN_xzJmc5itTeh2lvS2nhbM-gFr2e5DXexZtce4DhlXlbaYhPNbmOwUrAB74Z89l_piuxwmYs4A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
طوری که‌‌ تیم‌های حاضر در مرحله 1/16 نهایی دارن بمرحله‌بعدی‌جام‌جهانی 2026 صعود میکنن.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.1K · <a href="https://t.me/persiana_Soccer/24877" target="_blank">📅 19:18 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24876">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KmSw7j-QyIUzaIXkDKrrxXZQMizGyBz_EoXAFZCUXKo8XDyg_aswwlKgJiDbyfrLLAD6G_-banJ9a7riEeBgHwsNHQR5LksHujkjMwOxrQ2zy8NtcwgWshukHsN_tsi6Aofdtr9iVCDSQgZyS2kMdIenqZG96Y1lhPQLhCxizStNdNzUx9CZsAU44hRljjfXVY4Nn4us3orRdlkIWTgFkhgFRWEhlHJ9it-N5UBOHFAHljTIeFFkycPZtbUFtCYGIKdZZZpPTEPwHRo2p17vWAmkLKp_0k0Ju7-aNoJgknWp5W7YN525NpjKP0Zy4tY1sPOcRVd06xA1BDwGO9uWxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📹
👤
شیدا مقصودلو همسر29ساله خوزه مورایس سرمربی 60 ساله سابق سپاهان و الوحده امارات.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.3K · <a href="https://t.me/persiana_Soccer/24876" target="_blank">📅 18:37 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24875">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/376f8db7a5.mp4?token=ICKjRezksHfdRw0iI1U8ocrPlnWw6D9Rsii0KUAkiI2FEfv-CeOFXAX5PxIJOkI1lGw2kR7wGCEkQI3g2hIMVcvNN8rKmwiWQ1lfa8r9DAY989UFd-DAI8GrZ9BffT_F9Kiym7DGhZyvfzHVFZENX3n_wiRyFhavjbrgLVcX9gj2ahvu0eO07zgMRQl0vXwGLHheAtN55HZAqharSJ0BkntbRyR8lWfopCasXE9bMiRpEAin_Mx6Z_mJJcgShNxZsUf4X847l64_e9qr5yhk2y8oeJF1lF2Zh_SOBILJG8wf6Cu98NPHsFCUTUgRcItIJJ5cY9DRTOud18xatbNCQw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/376f8db7a5.mp4?token=ICKjRezksHfdRw0iI1U8ocrPlnWw6D9Rsii0KUAkiI2FEfv-CeOFXAX5PxIJOkI1lGw2kR7wGCEkQI3g2hIMVcvNN8rKmwiWQ1lfa8r9DAY989UFd-DAI8GrZ9BffT_F9Kiym7DGhZyvfzHVFZENX3n_wiRyFhavjbrgLVcX9gj2ahvu0eO07zgMRQl0vXwGLHheAtN55HZAqharSJ0BkntbRyR8lWfopCasXE9bMiRpEAin_Mx6Z_mJJcgShNxZsUf4X847l64_e9qr5yhk2y8oeJF1lF2Zh_SOBILJG8wf6Cu98NPHsFCUTUgRcItIJJ5cY9DRTOud18xatbNCQw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇳🇴
​​
وقتی بعد دیدن بازی‌های‌تیم‌ملی نروژ و تشویقی وایکینگی‌شون‌میری‌باشگاه‌وحرکت قایقی رو میزنی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.7K · <a href="https://t.me/persiana_Soccer/24875" target="_blank">📅 18:10 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24873">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/97048a0557.mp4?token=EWRoVPcJf6sx1wpfACFXUx7Du2ek4Io3MbqAbISc05DiF5m0uae8Ap_59ZC-T-GoZWqQLOJBA6ZZzeygyvoJSv3qjcMWFE6gVR2fsEE8QeUXkJ5H8M9KO62RmK6-R7vYH--zSy2MdOcU5kAnvwyYzJIG8wPMF2ZWSZKM6c-cTJ3hDSmpQQUxZwZ0ZPN6wNoLIdd2ubnxdRUwa8ChbXXwXFIzmbsAhnKSPIBNKxemMXxQ1XeW8c8jr2ddifDhZNpM4U_pX4YBmORrqhKE_kR2ZElHY1WOVhy6AEtnnt1gEyRyKVpwTOvDcSgRdCbJIpqX88a8YqO7L1ky8SS6YxreWDbM7ZKY2gyMti410XKgvIccjhXo12oBxxIHZdEk-5MCCHmvvlt6T3sGFKIFklwXX0S03erjg-tCImFZME7vILBYH_3NYZ-OIdxyCxtElEOBuBiVYZ3MZrpuQ9Nqek8M2BAEtFhjHlx-j8Nl_UCj0SE5bQ_CCT7sgBIcLqaJhApbA0A3se8Q4WXCxjc-7eDHHbqL5cwlkKnmqWcim3X958RJ12nz3k7sTGiFmkf2TEJM1XVw_LpcKs2oI2UdXxnPz9CitO8ZMoNEYBTELZYLr6hUReaL8vT_d4DQ1koGzOfcbzghtq8ZAC2F2iHxJVOgRi19-BT2OfuKbuumRLDg2fg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/97048a0557.mp4?token=EWRoVPcJf6sx1wpfACFXUx7Du2ek4Io3MbqAbISc05DiF5m0uae8Ap_59ZC-T-GoZWqQLOJBA6ZZzeygyvoJSv3qjcMWFE6gVR2fsEE8QeUXkJ5H8M9KO62RmK6-R7vYH--zSy2MdOcU5kAnvwyYzJIG8wPMF2ZWSZKM6c-cTJ3hDSmpQQUxZwZ0ZPN6wNoLIdd2ubnxdRUwa8ChbXXwXFIzmbsAhnKSPIBNKxemMXxQ1XeW8c8jr2ddifDhZNpM4U_pX4YBmORrqhKE_kR2ZElHY1WOVhy6AEtnnt1gEyRyKVpwTOvDcSgRdCbJIpqX88a8YqO7L1ky8SS6YxreWDbM7ZKY2gyMti410XKgvIccjhXo12oBxxIHZdEk-5MCCHmvvlt6T3sGFKIFklwXX0S03erjg-tCImFZME7vILBYH_3NYZ-OIdxyCxtElEOBuBiVYZ3MZrpuQ9Nqek8M2BAEtFhjHlx-j8Nl_UCj0SE5bQ_CCT7sgBIcLqaJhApbA0A3se8Q4WXCxjc-7eDHHbqL5cwlkKnmqWcim3X958RJ12nz3k7sTGiFmkf2TEJM1XVw_LpcKs2oI2UdXxnPz9CitO8ZMoNEYBTELZYLr6hUReaL8vT_d4DQ1koGzOfcbzghtq8ZAC2F2iHxJVOgRi19-BT2OfuKbuumRLDg2fg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
و بازم‌هواداران تیم مکزیک؛ اونقدر ویدیو‌ها زیاده که باید هایلایت‌کنیم بعضی‌هاشو بذاریم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.6K · <a href="https://t.me/persiana_Soccer/24873" target="_blank">📅 17:50 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24872">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a06e45a5e8.mp4?token=JtyMMcQ_3HqP-xvF-AbNlbqrizvh2lF0pZv3swGi57N7B59jED7gsADx0MXGKjK2V4Xz6lox2OQ3-4mB5YrzZ_zXs_LO7w-BGehN97AuwKoQyxmZTAqrTrZ3-Na1fznuZsVxe8Mu_mNZ2oW2dpagYbSY2IpAIHghN-0qmMcGB5uK2fyFB_ggKlhVmeZIgSMXfZW7yrO8Q-g9NxWw5E45_1laoWOZ9N8Np0GIfWLQFZ3wQZiFwOfyom9odFNhtrxQbI1IJRIufCT3B0pl9Pr1MxiBYk5YN1ZfG2R_s4Rh2CJLw27_m5EFpk3Rty2RiGD5N8_cHIl_8aDSWtRZiD4NhZx-dkd6FMoIpJ87G9mpMMJAA-v-Oy5Tv_CfrpctKABWYnbckCqpl9m9A10PmnUpUsgumxuRKFVm_I6a5xV2vAv2SslD4w75W9BFDN8aY4UBJBGOEP1OjnaRvfq7JddyD8sXGrHcfCvp1q3nWMGyNgoNcQTGfMfiMI3H1ccddMmfWheTxCTOI_FKyzEbNJJIEglTMJcEPFbsDi00b_un6gL0SHLHddMpFhNtoRBotZaC1_HMwRyE45yM0iIseUS8IHtChxYd284tljKXeV_Zl2TLn1K2gj-PABcr6FDN3QoWfZqKPl74FrcYSz-cCTwjMImi3pv1bGl_neWdaaDXzeM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a06e45a5e8.mp4?token=JtyMMcQ_3HqP-xvF-AbNlbqrizvh2lF0pZv3swGi57N7B59jED7gsADx0MXGKjK2V4Xz6lox2OQ3-4mB5YrzZ_zXs_LO7w-BGehN97AuwKoQyxmZTAqrTrZ3-Na1fznuZsVxe8Mu_mNZ2oW2dpagYbSY2IpAIHghN-0qmMcGB5uK2fyFB_ggKlhVmeZIgSMXfZW7yrO8Q-g9NxWw5E45_1laoWOZ9N8Np0GIfWLQFZ3wQZiFwOfyom9odFNhtrxQbI1IJRIufCT3B0pl9Pr1MxiBYk5YN1ZfG2R_s4Rh2CJLw27_m5EFpk3Rty2RiGD5N8_cHIl_8aDSWtRZiD4NhZx-dkd6FMoIpJ87G9mpMMJAA-v-Oy5Tv_CfrpctKABWYnbckCqpl9m9A10PmnUpUsgumxuRKFVm_I6a5xV2vAv2SslD4w75W9BFDN8aY4UBJBGOEP1OjnaRvfq7JddyD8sXGrHcfCvp1q3nWMGyNgoNcQTGfMfiMI3H1ccddMmfWheTxCTOI_FKyzEbNJJIEglTMJcEPFbsDi00b_un6gL0SHLHddMpFhNtoRBotZaC1_HMwRyE45yM0iIseUS8IHtChxYd284tljKXeV_Zl2TLn1K2gj-PABcr6FDN3QoWfZqKPl74FrcYSz-cCTwjMImi3pv1bGl_neWdaaDXzeM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇦🇷
گنگ‌ترین همکاری‌تاریخ سینما؛ حضور غیرمنتظره مسی درتیزرفیلمSpider-Man: Brand New Day
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.3K · <a href="https://t.me/persiana_Soccer/24872" target="_blank">📅 17:29 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24871">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aY-UroLZkx0KzP_JwOHpGHwLFNZkBQ_3uxkOsJxW83JfdVllHsH250KxJ0RK0YyRHJlNFzL04RnAA_t3AvoO4sCDPAKUZJobFJIdrUKJoON30XjywATzPEm6kYKe9gzJMaWGBEbGYUUiZ7kN7UwT8BBZO6jyffcMWmhxxyqXmjJJdLBBhHqh9i_So6VSKsP55lYvPE4UjjKkS-BeLc7trUvE_JhntGSE4tmDFvfC5uEzIv0rvitH-V13W8UXrFz7F9UqiiGOaM570eESVltpOotN5dqVb5oPwTmqBolOWaPDllzAde1a8XWHZOXioZ-k6IGKQ4GBZWGBSpkyGxgEyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🤩
🤩
رسانه اسپورت: دیگو سیمئونه سرمربی اتلتیکو به‌سران‌ باشگاه گفته بزور نمیشه یه بازیکن رو راضی‌به‌موندن‌کرد.150 میلیون‌یورو ازبارسا بگیرید و آلوارز رو بهشون بفروشید یه مهاجم بهتر پیدا میکنم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.6K · <a href="https://t.me/persiana_Soccer/24871" target="_blank">📅 17:16 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24870">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2a0d41c219.mp4?token=gh9hdwss9RTKakFXFKtwSZv2Aew_iuO0qIoXojk9rMUCQH8ZMv5GwxRoxxfu-wkz2LvpQwOXG7WUemwVeB88SXnUEbNA1BqgLH3_7Qc-6VnxVYdpMsBweGyf4rg33FVgvpa4yJaHjRnWb7ozTawM7bfIgQpZFVKaDwmajgPhVVwJUIcwaENFwtsKSlCfQ1OTjh4ic1VhoPGLAUbyS-g-TviLWulXGB8QHaDVhQzZgzF6Orih5oPSDNbON56NgN-1oZqpwYJj0mQe7zV_MtGZHEc3-UAyhVzS3IC7J1rNpkjQxCTKnp0BgclMPlSMFLbEf-2SbY3DvCSBYP5F0drNBA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2a0d41c219.mp4?token=gh9hdwss9RTKakFXFKtwSZv2Aew_iuO0qIoXojk9rMUCQH8ZMv5GwxRoxxfu-wkz2LvpQwOXG7WUemwVeB88SXnUEbNA1BqgLH3_7Qc-6VnxVYdpMsBweGyf4rg33FVgvpa4yJaHjRnWb7ozTawM7bfIgQpZFVKaDwmajgPhVVwJUIcwaENFwtsKSlCfQ1OTjh4ic1VhoPGLAUbyS-g-TviLWulXGB8QHaDVhQzZgzF6Orih5oPSDNbON56NgN-1oZqpwYJj0mQe7zV_MtGZHEc3-UAyhVzS3IC7J1rNpkjQxCTKnp0BgclMPlSMFLbEf-2SbY3DvCSBYP5F0drNBA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
پدر آقای‌دسابره‌سرمربی‌تیم‌ملی‌کنگو در حین جام فوت شدن و به ایشون خبر ندادن، بعد یهو بعد باخت به‌‌تیم‌انگلیس وسط کنفرانس خبری یه خبرنگار بهش تسلیت میگه و این از همه جا بی‌خبر قفل میکنه که تسلیت چی؟ و با یه حالت شوکه تشکر میکنه.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.3K · <a href="https://t.me/persiana_Soccer/24870" target="_blank">📅 16:45 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24869">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d8337fefdb.mp4?token=OytFMgiMnjfHsr8cdy75rZ6poEAt1v3ka-BI6Q8G9WRjhhlsIOiFTk5QegOjRYPLHLn1QUfcY7KM3aDSbafV0JUfgOr5XLfbJGsY9Kg8kwGjLZaIQtO42wfr-YpiesaYtwkYxQygD2oy89-MQH2SxNy8R4FuDOm-yJGPdeLNBCzgiQwj-kCXkdqQG8tOWo0wgYtkHPrSyPRn-Ut4G-klaoSJJS64bha2phbk3-nTfckti-bLGaWj6i1t5AgDpUUgUDA5HOmtzHyIPJlBkvMbXvn-HQO6bVoWxU2ELKsqZUMhARrCavBe9QZpbJHQgTNBd4TECXENg_qk6XzqKRA9YA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d8337fefdb.mp4?token=OytFMgiMnjfHsr8cdy75rZ6poEAt1v3ka-BI6Q8G9WRjhhlsIOiFTk5QegOjRYPLHLn1QUfcY7KM3aDSbafV0JUfgOr5XLfbJGsY9Kg8kwGjLZaIQtO42wfr-YpiesaYtwkYxQygD2oy89-MQH2SxNy8R4FuDOm-yJGPdeLNBCzgiQwj-kCXkdqQG8tOWo0wgYtkHPrSyPRn-Ut4G-klaoSJJS64bha2phbk3-nTfckti-bLGaWj6i1t5AgDpUUgUDA5HOmtzHyIPJlBkvMbXvn-HQO6bVoWxU2ELKsqZUMhARrCavBe9QZpbJHQgTNBd4TECXENg_qk6XzqKRA9YA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇵🇹
🇵🇹
کریس رونالدو: خواهرم‌ گفته این‌آخر خطه و خداحافظی میکنم بعدجام؟ دیگه تصمیمای عجولانه و بی‌هدف نمیگیرم. بعداً تصمیم می‌گیرم، نه الآن.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.2K · <a href="https://t.me/persiana_Soccer/24869" target="_blank">📅 16:30 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24866">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8659ae843a.mp4?token=q3ktt_NlaTFhEv6LfnRs5fDyJ24A0yUH3uqZ0lC7oSK1bR5rLPXWC84yRAbGfAiQvPYG0I891UWMCv5Eyb3YcwFwH1cDCLGlNeALZgMpwd1EvW_fm8AAPHIdMoZ_7KnYt4CsPzQSCaDX6Psnyjh6a68qpH3Tm6-r93DQztD3GLsimN26vhDDffjwfq4ZZaZzIw02vm95Y_Sjxh2TeOvl-x2RFN0ShmYjObnkLiaCYQ81G6DME6GYjVN4nHDcDwdFeOQ_zQnv2A5tup5IHFPzVmfaHOpCqXliyO85hjfPqd7aWAgnSPX_-f0QOVgZLjZIxEhJH0y57GunN8LZp544QQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8659ae843a.mp4?token=q3ktt_NlaTFhEv6LfnRs5fDyJ24A0yUH3uqZ0lC7oSK1bR5rLPXWC84yRAbGfAiQvPYG0I891UWMCv5Eyb3YcwFwH1cDCLGlNeALZgMpwd1EvW_fm8AAPHIdMoZ_7KnYt4CsPzQSCaDX6Psnyjh6a68qpH3Tm6-r93DQztD3GLsimN26vhDDffjwfq4ZZaZzIw02vm95Y_Sjxh2TeOvl-x2RFN0ShmYjObnkLiaCYQ81G6DME6GYjVN4nHDcDwdFeOQ_zQnv2A5tup5IHFPzVmfaHOpCqXliyO85hjfPqd7aWAgnSPX_-f0QOVgZLjZIxEhJH0y57GunN8LZp544QQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
🇳🇴
ارلینگ‌ هالند ستاره 25 ساله نروژی باشگاه منچسترسیتی اگه درکشور‌های‌مختلف بدنیا میومد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/persiana_Soccer/24866" target="_blank">📅 16:20 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24865">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/et5SPxGSstU9yMwrVUohOuD81Tge1cyhqLfD-JCNwI6tYnpmxFiZVluFmZlLnEQjv8tJX6YHfE1j130WMaqQ_GXyvoqr8ZM4DuKzJ6rKNBX67AuurZXPVEWm5c7_69krUYmsKxVefWk1HkRF_p2DUJ-xYQIrq1pR63R4_x4I5RCJCqwLrI0ifCvovyVEE6z3ZlEd_-9CJ89KConZV2E31vgErIFzeqG_r9Q4vYZrCFRQpMp_F65IC_S1hLtLPI3pNQ59JXHHzdwWGncnvo4QlLxSQOUeUb2b4_IwRw6Y1wASM_Ru5YVyzggyKZ3_FU-5wF6HUaf-mKnLtZ6FZ-wFTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🇵🇹
کریس رونالدو: خواهرم‌ گفته این‌آخر خطه و خداحافظی میکنم بعدجام؟ دیگه تصمیمای عجولانه و بی‌هدف نمیگیرم. بعداً تصمیم می‌گیرم، نه الآن.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.2K · <a href="https://t.me/persiana_Soccer/24865" target="_blank">📅 15:42 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24864">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jKaG3wp4jIHgoNe8Z0mBdwfhgK1PcMxDBadN4L6nVCJDIC7Cm1ScDRzKJGLOwcZvQbJz1-k3idjSO5PscoOSMRkuIMfTkE0zQdfwBD3-0XjdlLUMMkUsLiWa5VQEjtD8EWTUf8Ds2SQ81rT9ChyF__UsGokf_CXTsM3X8eFPYH4tvZnmgP_dNOdclsiRu4nPT6zbaMfCK9YmCST6YInd2Z8hrvvVlwfpjzvm7H6s_IsyhTkVx526RTNnKKb0Lo56ymMdL_y_n1bZeHZn82vJ-lU1v3iSn3zBUdQlQ5ri9t04xUuiBVxKf7okeOYA1MJZOaDeYeJ_89Cw7vf84zJWRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
محمد خلیفه گلرآلومینیوم‌اراک: باشگاه استقلال باآلومینیوم به توافق نهایی نرسیده. الویتم حضور در لیگ برتره و دوس دارم که در تیم بزرگی بازی کنم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43K · <a href="https://t.me/persiana_Soccer/24864" target="_blank">📅 15:39 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24863">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Raw_V3scxhgMPK32d3vGN8DsVKKfyzX5EA1fALNuAMj4i-AaJwXwHaYJz-idojoKf39tGkiRTznG_j9Sf6P8_XmzHP5Y0wxa0HaZ0qOQjEI2pXrY7gJ5YjTg3asqaKhg9Aujpac3iAYUOF8upa0ohqzEKxMPjS6AHQj6pm1Wf6LuMqwqrMlXsf4eBVrcxY7GON04DxE5f18JKKgit4l-QEjDhqXVjubUbTZhkQVR3-u7PVKyeMZumLBjM3ih7e_AHo8oQ10eC_1rVFl-6Yk3pt2bchQGIvepW8O2_RPP0-KsAN8vInLWlHl0Mf4_9QnoL7Qt-J3HwjbCspr5sXJAtA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
#تکمیلی؛باشگاه استقلال دراین‌پنجره نقل و انتقالاتی بین‌علیرضا بیرانوند و محمد خلیفه یکی رو قطعی جذب خواهد کرد. با توجه به توافقات صورت گرفته بین‌ابی‌ها و مدیران الومینیوم ممکنه که محمد خلیفه بزودی قراردادی پنج‌ساله با استقلال امضا کند اما یک فصل قرضی در…</div>
<div class="tg-footer">👁️ 44.5K · <a href="https://t.me/persiana_Soccer/24863" target="_blank">📅 15:13 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24862">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gHduZ07EsXMH3c_rzFibHXTYw585b3mgj8TUKEAYx1waD8gYr6Cyy8F6QeReSBLZprKcnl09Gx7T6pztj0m41K7FDFo-mYWZlJA6ECAFvc-6mdza9bW74eHxLSy4ch-jMLU05V1R2IIYqHs-sZzQCSINco6-YVD2PPpSUWTlacCdRVPf8xXCiKuCJQRYqtb5xMlqc3rp2U4KpNnbM-kSN2fLFW9ZxawYEEK14_Ki3AZl0IaJ3QCfoSwU_LasrPDW_d9niKPHb3DsUZXaYYACdsUnVBii4W03w8PQ1rdlNPBZ2AP7yXWqrE2Dr3MKM62o1c4tI5ieqVHzEJVM1x4_4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🇵🇹
دو تصویر متفاوت از کریستیانو رونالدو در دوسن 21 سالگی و 41 سالگی تعداد گل‌های CR7 در کل دوران حرفه‌‌ای خود به 976 رسید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.7K · <a href="https://t.me/persiana_Soccer/24862" target="_blank">📅 14:48 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24861">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vhvUGUReSA2Icn4DCwdAKCHRn2JsEe5B6NVuoO8tlLwRP-unpp1MGDivSHFtjDz0W7-9UF-aE5g_gDx7987CPuGHhs2tjJiIYUCutuNmBtzhPw5DU7CxZNxj-2HvmQX3QbDugmrnR4EHjhh1Z3BwTloy8RsxL2L9lmAkDCTLLtio9nrh0E6Finj9tupOsies2uHOfGaWOzqUr2tCDOpi0HBj9y6B0Sy9LHxwLIGhzHDeOl7d0YTrFIwdUvenqyz8wdaZRc8jSb3AuEA87rZO2aNXzmxMvEEgiK1JhkA9sFKdz1L363kGUOoOQT4Mxcz6B_5JqtIflafgvbpNKPR7nA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇳🇱
🇩🇪
#نقل‌وانتقالات
|
مارک آندره تراشتگن با عقد قراردادی‌قرضی‌تاسال ۲۰۲۷ راهی‌آژاکس خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.4K · <a href="https://t.me/persiana_Soccer/24861" target="_blank">📅 14:44 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24859">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nzK9tjm8ijbpG3UGBlluBRWppm3mmrM9ij9b_VauIOhYD0gpNSoDbjB5ApRPQwEklaBPZGPj-HZ1fU0CFFNb7iQ9EYsL3V_Oh4sw-cTpZ6BL9-KTgJjrGHeSZQbavhzCP8nzZSW-i1MevaMuU_rLls-yr-2CAu6icIqyrlDu6C-CyZJg3ZAKmAAEJdpTlUgzpCAXqD_BW-MUDFGNlD7wMaojpEk3c4Q-z8KajAFYJn-ty7iwKYcB2OjMJHJKRaIZWfFr90JXooG4UlaceFXQxDX58G1bZ_v1CfQfG6G4No85VOc6VhFLR-HPtm_U16D6VlRFaQI-9LI8N6cOTBPz8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0a322be112.mp4?token=vL_D0XeqzhxamSp4Ptk0dP-h0ihwgk3DTabnm3uJy6hCIE0uRf8TjdV4jcHQK5qGjcax4NwOxvIYHCiFpHpEw6ReummJd1_-Kcw6fYJlLyFjm7K1bim2L1FNeBsxXWp7Ys8TcTcI2Nb7DEL92OX58zLK1hYtrgz11hDOKyGSHjSsxhiOORvxHKxOJP8E3sc5pHkgXSlFnOYUXzgIZAKMnH_rWCE0Y0kcnDPanhi5XFo4zTgQeeyvGoyGmYBqG5YyRf_P2S81Sa04wIcJ4ULnfyBRXl0v1S2WH-wv5hCck1p17cYF7vnN_BskwC3lBuoAbqRhH9_njwwn7BIOJVc6sA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0a322be112.mp4?token=vL_D0XeqzhxamSp4Ptk0dP-h0ihwgk3DTabnm3uJy6hCIE0uRf8TjdV4jcHQK5qGjcax4NwOxvIYHCiFpHpEw6ReummJd1_-Kcw6fYJlLyFjm7K1bim2L1FNeBsxXWp7Ys8TcTcI2Nb7DEL92OX58zLK1hYtrgz11hDOKyGSHjSsxhiOORvxHKxOJP8E3sc5pHkgXSlFnOYUXzgIZAKMnH_rWCE0Y0kcnDPanhi5XFo4zTgQeeyvGoyGmYBqG5YyRf_P2S81Sa04wIcJ4ULnfyBRXl0v1S2WH-wv5hCck1p17cYF7vnN_BskwC3lBuoAbqRhH9_njwwn7BIOJVc6sA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
دربین‌تماشاگران‌بازی‌ اسپانیا
🆚
اتریش؛ کلی ستاره بود؛ از فوتبالیست گرفته تا بازیگر سینما و خواننده، اون عکس هم خانم روزالیا هستند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.5K · <a href="https://t.me/persiana_Soccer/24859" target="_blank">📅 14:04 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24858">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KcevOrDPKtSbAQ7cHxSHRTzCm81mwmIHs7ZXl9f_GugWj619JQ0U429LbImiNh2DUklhUmTu-Y-WfXKKIRd1J_DiP0p3b-hScCzd2KWdB0aKkwXTQPMYCMvBoox2KSakr2Nu1CELlyC7ieLp03DBynNZj1WnaZetmQ2w1pRpd3bAdGTPsmQcX4TWWVHLrMV72hxYeq5M-DY2fx-Zw0HIsj__2MzFaDjOVP__kEQmK2PfFPyPTcpTg7u3NEbxcTZRV9CvB-uDbt8eeDnDIVT1OEN03n7hvItsY7Hiiig3bnmZnnw61i1yLNWWnw4NtH3LpwcA0iIbOxsKVVALA6mMLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
این هوادار مکزیک گفته اگه این تیم انگلیس رو شکست بده به50خانواده‌مکزیکی کمک مالی میکنه.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/persiana_Soccer/24858" target="_blank">📅 13:31 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24857">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JRSl7x7bo8zqZysfbyp0sHOYVG4O2JCxcopm4Y18JoTPhPyKFTR2AoCbfymcY__Fj8wSEC6u_w2XnWsrHGRX2cZ4Qhs3f8yt85WI1nl1d0Tkp3Sz8jRBjnyYVMKWHZSkIyhCtv3-CXXT3rXqVr3pt7alEKekl23Aen3PXnRUXFaMGgZujVTd5QALgBimfRnhlOSbSonqJ9sPpFgrHV8oha2aRRJ0Zy1y5EEIlFqCXSO2N2mCTeU6o5lUrLq-IhdMeoGyMQvthsIXAERvOSlGpcnzbIGs-p5I-DZmNYsWfFixchEtCBzD14ETipYRbBpp0fA65rCZnAXF89xpSoOLNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
همانطور که در روزهای اخیر بارها گفتیم؛ دراگان اسکوچیچ سرمربی سابق تراکتور پیش نویس قرارداد خودرا باپرسپولیس‌امضا کرد اما اومدن او به ایران منوط به پیش پرداختی ازسوی بانک شهر است که بارها گفتیم یکی از اعضای هیات مدیره بانک شهر مخالف جذب اسکوچیچ بااون‌شروط…</div>
<div class="tg-footer">👁️ 47.4K · <a href="https://t.me/persiana_Soccer/24857" target="_blank">📅 13:10 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24856">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZqEHFfTF_Luyum-iYy7UBeIgMbh2FCczWXUJkCnofqVKOhSvVoNY2huHc7POZl55GSJLX0_4mO1UTLElJCc3bbtOfr5fJvdI4P2uTtpZWEhKNuEBU0UI6kL0vukPqAVpZWYJnBW0cOISYMwvy-V1kfwiWdIbbVjpKVR3fpJgQeeTdzBYA7uRzgG7bqbzN6wtJPXqnoAAnp0zqeG4xK2LY8cDft65j1NSnC77UBlhuG9mPG1YEfOC_u3ozvFI0LZIjBHkQhKTyUtilKag-qAC0i_AWOlCDoyNOkuZdLkunPul5tb2XA0xxuazOd954InAIuWEPLNfm06wAfM2ATEHAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی؛ طبق شنیده‌‌های پرشیانا؛ باشگاه تراکتور بامدیربرنامه‌های محمد دانشگر وارد مذاکره شده تا در صورت توافق مالی با این بازیکن قرار داد امضا کند. دانشگر در کنار مذاکرات باسایر باشگاه‌ها درتلاشه که با قراردادی خفن به استقلال برگرده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.9K · <a href="https://t.me/persiana_Soccer/24856" target="_blank">📅 12:20 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24855">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BhqwdVP7f9epjtHbBWvFAFpB3aqept9TLqIwluw54_sohdRd2cxo-bqDJ6sUaI7kuvguC0Ol_OhUWdoXr7P8ZFBSLGZjCWeDZx4iJ5D_lzTlTX9zObBBSCe_PEd4V22KyV_IqbuEo4vX9jltFMymRzvlmxExGNnH0-sUShZxzMBspd3XkeOhTuMEHncFhWxOxoKb6IOC96podfB-K5w9BRrJC2iAzEPoOu8p_4__ji8LdcnBcx5U2Jp_uGItzP9pLCmV_aQsJWSBDSCfER9FA9fIN6kQWkVrRC-cagpj0BeAjj9CEDj9fd0lzhdCYXZQcfZ21j6hQnlw-mF0IWJW9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
ماسیمیلیانو آلگری سرمربی فصل گذشته تیم آث میلان با عقد قراردادی 2 ساله سرمربی ناپولی شد.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.6K · <a href="https://t.me/persiana_Soccer/24855" target="_blank">📅 11:44 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24853">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XjhgvK8kvbb6JM22Y_Z_2vsexBlT29RCJndJ70dKo0i2qf-W2-dbgLMaMoyoifUk8VR-LVgLTH0UyKblvaI-XKG36gxQOnKR9R1VZi_zpoR2sgfmWmSWep547fv2lmW73M2DXCIoTNmUY6a-uDWa3N102AXMOyynAtXtsRIjoWd1ncpclzp2DFCTXQPfkRPhx8AMRT4JyxW8ZNpmYBFvi64vvt1YDEBhDZBfHonrWDjyQ5mp_tSe5cQhgkcI7Oclsk3YkMUOJB2SgB9LrkeC_0SFd3KVXXArYD1fJvg2Am2zjETIkoSHvXRA9hQIE3UgHjtOGW8fWJ1tCTh2TlS2Cg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kJ9vVu8EoXm-GXTXCptmzcGmHc9uCCkBIGqjAHiJ3sBHyvZyThnSjx8oKxnSV-hgGAH2WN0ksVW0PRTuSYgRcQQcTcT4WAmXAUYoD4WBRNIg2mVut9JCIwnc-c-Q8rphNXR-rQT-a02SUfHZS-ZMJYh5f9fKaCQSJ5H2Sa0S9c5G3JrzhmSNFgisKKfpBiXi27X_XbnXHKz3E-i8wxWYyrvJmQKK9kPsI2v9zyDEvslI1sci9GhGqiFi_11-2hLuU2Xitd8oEUc1s9rdhlPsol-pL5Ukx_YDKypaijG3mxwSUcvXPI47qPuVNL2sRXZaIvyfF-I8Hc6erxe_Jiu_3A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇵🇹
🇵🇹
به‌یـاد ژوتا عزیز؛ دیشب پرتغال درحالی که یک‌بر صفر از تیم‌ملی‌کرواسی عقب بود. کامبک زد و با گل های رونالدو و راموس تونست به مرحله بعدی بره. رونالدو هم به منظور سالگرد ژوتا  پیراهنش رو پوشید. تا خوشحالیش رو با اون شریک بشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.7K · <a href="https://t.me/persiana_Soccer/24853" target="_blank">📅 11:02 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24852">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/82f468b62e.mp4?token=s_2tmMV4vwwVI_MSmpBAhCIoElQmxyDttXZhXyDaVw1kIkhtAUh4S_oaf1XiQCqYDbqANX-nixcheOxIi91DUcAJ5Dm6efnNqSbJzQS5NZhZ_Sqh8SK-ETpKSTiOUr9Vm4P4tOrednp_-8HHT4kk0OWiwhXW7XtbHT2h4Tz7XKlAPJGIjVbx4aSM2Qh18Rfgg8d_zz10cxcRAcQT2hfV1u9byYrbRUmsZSIlrwo3qud-Sh7a6tstOUQVrtdKrxlNqABqE3IvwylHcUHz3mlnCZyhpZzjcI2xmMAjXzV_BFi8rkYLTs321VcXxGSCrSDK9OyttTynSW_voPjVDNhZQw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/82f468b62e.mp4?token=s_2tmMV4vwwVI_MSmpBAhCIoElQmxyDttXZhXyDaVw1kIkhtAUh4S_oaf1XiQCqYDbqANX-nixcheOxIi91DUcAJ5Dm6efnNqSbJzQS5NZhZ_Sqh8SK-ETpKSTiOUr9Vm4P4tOrednp_-8HHT4kk0OWiwhXW7XtbHT2h4Tz7XKlAPJGIjVbx4aSM2Qh18Rfgg8d_zz10cxcRAcQT2hfV1u9byYrbRUmsZSIlrwo3qud-Sh7a6tstOUQVrtdKrxlNqABqE3IvwylHcUHz3mlnCZyhpZzjcI2xmMAjXzV_BFi8rkYLTs321VcXxGSCrSDK9OyttTynSW_voPjVDNhZQw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇧🇪
از دو شهروند بلژیکی پرسیدن که حاضر بودین به جای زندگی در بلژیک در ایران زندگی میکردین؛ خودتون پاسخشون رو ببینید‌. چقدر تلخ بود‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.4K · <a href="https://t.me/persiana_Soccer/24852" target="_blank">📅 10:42 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24851">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9e81e75283.mp4?token=Xapxi2jt7sAliOLKXnl5ILozEfjM350vrgjAPtPoVdEi8EwN4dj4AjuPLVgQY788rw2169iQ7gZIEa-Z145narhdDmRI9ye_tsxaOnHKh2BQzpPChYQsQ1iv3x37g7RnSJQ2WPqVuZDN78F2-DBDDNyfPaUkors269wSElRAuwsGj8g-HULFPQcLSx8rPrOOfbHv5aZFs-sirc-hYWK3P8X9lqiI7TO26HhO5o_Wz-0FqX9Riwro9x76oFoR9BgVj8oAo6xwoiYXDI9GVl27ZS7WLF2G5uAtnitowcwQFmSp7kSCkTONH1lWn7mZ2lpqzj1_yH41kUQp6SORgeEWGw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9e81e75283.mp4?token=Xapxi2jt7sAliOLKXnl5ILozEfjM350vrgjAPtPoVdEi8EwN4dj4AjuPLVgQY788rw2169iQ7gZIEa-Z145narhdDmRI9ye_tsxaOnHKh2BQzpPChYQsQ1iv3x37g7RnSJQ2WPqVuZDN78F2-DBDDNyfPaUkors269wSElRAuwsGj8g-HULFPQcLSx8rPrOOfbHv5aZFs-sirc-hYWK3P8X9lqiI7TO26HhO5o_Wz-0FqX9Riwro9x76oFoR9BgVj8oAo6xwoiYXDI9GVl27ZS7WLF2G5uAtnitowcwQFmSp7kSCkTONH1lWn7mZ2lpqzj1_yH41kUQp6SORgeEWGw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇵🇹
🇵🇹
به‌یـاد ژوتا عزیز؛ دیشب پرتغال درحالی که یک‌بر صفر از تیم‌ملی‌کرواسی عقب بود. کامبک زد و با گل های رونالدو و راموس تونست به مرحله بعدی بره. رونالدو هم به منظور سالگرد ژوتا  پیراهنش رو پوشید. تا خوشحالیش رو با اون شریک بشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.3K · <a href="https://t.me/persiana_Soccer/24851" target="_blank">📅 10:42 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24850">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B42rBsp0JGdN3eNIHIjf-4iCU0YjrLWXw8_Oh4zVW0U6mNxRU0uB2_ZjASmSA_gB9CPfaPJ15nMFe1Pqi6lG0robeF2cmCSMMYhcM2MIn0MuGNT6gY5oAMuTsxTlucBRJmcUuoh7oW4D6CcjCHd5X6caSRNk4skWGZVtlOfjKCRhfZqY41OEdSIKqESZvG8UAn8y4812_b17MlbuQSd_yLuHCd8Km2fJM7rDr6zL9Ql-ltk2MGEVBH16suyzn6U16bxaC-Obc_vTnBDb_R3lmy8XvkHnjfNGlDT0NmcXYrKudm2qFAYZojHEosXWDHaKa0ZGRTAk3uNJNc8am916NQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
تجربه پیشبینی مطمئن با
🅰️
🅰️
🅰️
شارژ اضافی و ریسک خیلی پایین در
#بت_اینجا
رو از دست نده
❌
🛍
ازاین‌لحظه‌به‌ازای هر 1,000,000 تومان واریز بهتون 1,200,000 تومان شارژ میده
💰
🤩
🤩
درصد برگشت وجه در  صورت باخت
⌛
همه بونوس ها بی قیدوشرطن:
🌐
betinja.bet
🌐
betinja.bet
کانال بونوس های رایگان
r12
@betinjabet</div>
<div class="tg-footer">👁️ 46.6K · <a href="https://t.me/persiana_Soccer/24850" target="_blank">📅 10:42 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24849">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c2ZaZdng9RmIdspCVJCk4pbwT_n9ppCw54Tse4KWzNThg1zcqHKZ2jj7SuCZpek7RMWGy5fuMxgs2wDcMaSTGeQ9RdZ-WKDiWV1QsCNSZUxUBaczUEcTmIAEB0np30Fkn-Ft4Kd616L9HCIStq7KoMv25WgosFBbmAaVR5hnolw-MeTy2SnMJAz7W1VFl1djLbSoo0HzlQ0Iyiu4TZjLUgEdBUvMDvoWsieK9o0TuAhVsukVNCrv_Fh6lGrzLcEaC9UsJrxdfazuNJUUcLO65BiDDtaTVkC4Jl5IN0j8RhaPfE7vPQi4F1X-u4FuuOrrMo86eRYA3nVV24LU4_WEeA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
اگه سنگ اندازی های عضو هیات مدیره بانک شهر تموم‌شه باشگاه‌پرسپولیس‌از اسکوچیچ رونمایی میکنه. پیش‌پرداختی باید پرداخت شود تا اسکوچیچ وارد ایران شود. امروز پرداخت شه فردا میاد. پیش نویس امضا شده اما شرطش واریز پیش پرداختیه‌.
‼️
دلیل مخالفت اون عضو اینه که…</div>
<div class="tg-footer">👁️ 48.1K · <a href="https://t.me/persiana_Soccer/24849" target="_blank">📅 09:56 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24848">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d4a8e003dd.mp4?token=LX7C0Abx0G3VvMRx5gDxIFBuCnMVPaO-VLX8WxXoI8hfeN73zTiwgP566ZnGt4cs1W65lrX9nI0xD4_-TXX3AbJi833LGFfqwFXqhuTY9NaSMnmBXXeI8ZYP-8mVn8w0ufG3EPnejt3rgvJ__GSAOU5sec1iXwvttbjE16GaQP4nOqpOvq3HZA8bEgM1nA_me2jbUOhxPzUK9wGpzClV5hWXbovA_5SImkH_8GmmDz0OpVnHh3CNFRHZfD-uXokh_4hPD84J4JMKE4UWg3be2PkQQvFsrfN8Gzo1S5orc3Zsz2q_Smhdke0xrKNeMSvHld0Lq3xEFYVbSxFzAtcEXw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d4a8e003dd.mp4?token=LX7C0Abx0G3VvMRx5gDxIFBuCnMVPaO-VLX8WxXoI8hfeN73zTiwgP566ZnGt4cs1W65lrX9nI0xD4_-TXX3AbJi833LGFfqwFXqhuTY9NaSMnmBXXeI8ZYP-8mVn8w0ufG3EPnejt3rgvJ__GSAOU5sec1iXwvttbjE16GaQP4nOqpOvq3HZA8bEgM1nA_me2jbUOhxPzUK9wGpzClV5hWXbovA_5SImkH_8GmmDz0OpVnHh3CNFRHZfD-uXokh_4hPD84J4JMKE4UWg3be2PkQQvFsrfN8Gzo1S5orc3Zsz2q_Smhdke0xrKNeMSvHld0Lq3xEFYVbSxFzAtcEXw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
این‌بخش صحبت های فیروز کریمی هم عالیه؛
میگن الهویی دستیار امیر قلعه‌نویی گفته ما هفت تا پلن داشتیم برای جام جهانی؟ مگه فیلم هندیه اخه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.9K · <a href="https://t.me/persiana_Soccer/24848" target="_blank">📅 09:35 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24847">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rTMdpmrWcarX-J6fbnfzJo7x0Hy7R2_UedNifoWoXvodDsIm6l3y2afKJYah_IaTcokT0RUKgl8p7xobZceRPKwlr9_3DxZ5xG79TDcPKwfKT-lZAhhdFCCvsk8nuMetfJlCH3YEwxLI8L5j7-S3-syFIyYJsK18R7QdXJtk-UjNyE4_FAdat-MF6JHwoJ8LEcsT_Dvut_uduhTgoRwSEubTVD1MZThtqi8xq7cT84ne2mnDNqS2MBtu0_ivGqXbeoeY8Dhetn3kDmIUxpWxbuRjSkgCBCkCOwYfoGWoX6_mYMLpvEh_bkgAFlZ3_Fqr1PrDnvgZrllEslQLgN7VVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇩🇪
🇩🇪
اسکای‌اسپورت: کلوپ‌ سرمربی‌سابق لیورپول درآستانه عقدقراردادی چهار ساله با فدراسیون فوتبال المان برای پذیرفتن سکان هدایت‌تیم‌ملی‌این کشوره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.1K · <a href="https://t.me/persiana_Soccer/24847" target="_blank">📅 09:04 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24846">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lUSdhh3JDaeDpY7rR33BKpl-TYwME5byAhgmVP4_6toUeZLf1rJ1furMrE9DApEcO2BLFgXc0d-wJRLtjSirTxme9Z2fktPg37-n45QC-Z-26XQIVa8Qgc--Bizx5HsKseLR09WMjs3UJJJivosRAK_GH1S8xytAD1Kau2AT_RSElBqdZxL73Pf2lcilZIO1tngl42rpMs00-zNCPzT8Nqbt1KI2sQEvf87COUUREh1zRXdh1MSqywhg9NUQdAFn0XbVyyY7DSprohwmhd-pqDV3RZrpgUgvXEIU7PWSuot62LXfbJKDEuRtuErAGTywnKDBBYXIx-EUw54uf9s6qg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
🇵🇹
گل‌های دیدار تماشایی و مهیج بامداد امروز دو تیم پرتغال
🆚
کرواسی در جام جهانی 2026.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.1K · <a href="https://t.me/persiana_Soccer/24846" target="_blank">📅 09:01 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24844">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mZJH_DdQV4R3BEI8f_1c4yrnsa5qB31rX1HyE7fkniEJQ6fQKlrbE_TaFIREJ30Qz0r2Y7d5dWByGLkLqJQoylJ_FgBpRQSnmI6bEhGrVT1O7mgYHJ6dz8WwIYwDfjEpqkcIPdafPfAvgRdnEoLzpypdikcT-sL6vo-mtPOrYDJ48rJtJCtrr_LHPO2iivrlvARE23qmWF7Hi4JacLowz0mnDW9_Qp1d60vRaVD1v62rFJReWKhbNqAt9R8v9yEO2ERZ1Gnx18XxJNghro0MB_V5-bbMAun74lT2_W3wFpYg5VCO2WWQeRWALRkVhL2VVTBvOHB3ZLv-9KdOI4cu8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LrAkjQkc1xnMoRK-767r087oonlAHmBLSkN5vdbwByMspZ8OWXrbokIGWpk0OvkkNxBlxR0nVIoLhMRcjoSjxeqg9y07vOwbNE9EC1pxZ8Y1_92WjAy9pyhiAJhUxo9URbBdn__rXkmnIenZkgnC27_OdTeuD3QEEA3qJX8OYVxX2L5uaeM4YGEhx_QXC73yNkas4TWmTl7tCKM7aLdEDZyd6f4CvOxmoxU5oLR3dBIwGwigZi8e-ENqq7ACJBjECyHuUuf5PYEHI6q7ly7dBw_3BwMN3atLbZ06Xif7IJrD_Pl8BVLsVsTTRe-JsirrP9OPyZHSrJe61G3zElCQPg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🏆
🇵🇹
گل‌های دیدار تماشایی و مهیج بامداد امروز دو تیم پرتغال
🆚
کرواسی در جام جهانی 2026.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46K · <a href="https://t.me/persiana_Soccer/24844" target="_blank">📅 08:41 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24843">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fr7U3ar2gEYMgYUr2F_9mu8gby5XQlnE4KRXeS3XnOniyMt0_Hj-JIc649u7A8GgPtN_joEn1GkFkeo3EvdhD83iFSIRu3RKwajk7WI4TMNqeFfjNR8Mdm10M8K_WWbmFb4Hqdozhed1P_VA-ykY3h5SysRck9gl8Tzf0FouCImGlh7lxZUb7vOSr9HEJmP1AV_K05hxPjZMvuFio4p28eFSkUzOwgAPyTsogZQ2v76v-m7cRO_sedEwHaeLr5AuUfQphQjQjDgZzrsG_lyG2pE1RuNF4x9HuHSmfeM7S5_faskIS4x2SWSW85IRyRbWGK1oiJTdO6du_EzQUc4bCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
یک شانزدهم نهایی جام جهانی؛ پیروزی شیرین و ارزشمند پرتغال‌مقابل یاران لوکا مودریچ با درخشش فوق ستاره پرتغالی فوتبال جهان؛ یاران رونالدو حریف اسپانیا در مرحله یک هشتم شدند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.4K · <a href="https://t.me/persiana_Soccer/24843" target="_blank">📅 08:34 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24842">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3224dcb43c.mp4?token=PgTy1PR91JDNTIGH7jpwM4_aVrbI4fogBlabGGxqSiZEE_GuVPhZnp2EcPhEZG5H0h98aoSYc8mpFs6_IuAeawmr7B-2hFoKpxkFcpsTxu5IfTvEiJMV4zk7GvjNuytsVERhtkn--KOUIXOFMcFm-TCZVFr8Pxs_WgioUyoue_smPME49KRGESjjMmd3bd2Pkv8BUrMqI5VLl3Je0YNw4_F7QTMBszPFvWi1ClZdriCDXJa1jyWWphUrxXYVQKHlXDZ8xrS9sEPHqM7r5Y-KsTudKkinzzB67Q4o7XBd-OjJZYzSOTSYZtUGQBy0u-44-cZaro7gjeITBZefx-TLSEYlIMXlUyVlUcmWWsHKzu9F17QuFbHIhkSTQLyoxGK3MjEXyvXINuc3VHxuOvRLQMjeYjHW4H_wIObxUIUYkXT754vpE8A08tgA1krwf0ANy25CJ93KWZmWIgiDHzhYV1y53Xa3Vl-OmbCF1gtFl22PuG2k1S_feoVECfizfO19Jo7tfqnZ4A90-9Lod4K-0ER5qCP-HeeMPvcAKYAriQC5RZu1bzoT4K5ZcB6OPOyhNHEXpDwnp5VnsBoXfeICmmq6BjOSkm5TW4hSTj-80myyC-yxLk7LnFUdkaukDhzBRjAt33FAjzzE06T_8m5yyoALHoIW90LDX59rRSI0RKY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3224dcb43c.mp4?token=PgTy1PR91JDNTIGH7jpwM4_aVrbI4fogBlabGGxqSiZEE_GuVPhZnp2EcPhEZG5H0h98aoSYc8mpFs6_IuAeawmr7B-2hFoKpxkFcpsTxu5IfTvEiJMV4zk7GvjNuytsVERhtkn--KOUIXOFMcFm-TCZVFr8Pxs_WgioUyoue_smPME49KRGESjjMmd3bd2Pkv8BUrMqI5VLl3Je0YNw4_F7QTMBszPFvWi1ClZdriCDXJa1jyWWphUrxXYVQKHlXDZ8xrS9sEPHqM7r5Y-KsTudKkinzzB67Q4o7XBd-OjJZYzSOTSYZtUGQBy0u-44-cZaro7gjeITBZefx-TLSEYlIMXlUyVlUcmWWsHKzu9F17QuFbHIhkSTQLyoxGK3MjEXyvXINuc3VHxuOvRLQMjeYjHW4H_wIObxUIUYkXT754vpE8A08tgA1krwf0ANy25CJ93KWZmWIgiDHzhYV1y53Xa3Vl-OmbCF1gtFl22PuG2k1S_feoVECfizfO19Jo7tfqnZ4A90-9Lod4K-0ER5qCP-HeeMPvcAKYAriQC5RZu1bzoT4K5ZcB6OPOyhNHEXpDwnp5VnsBoXfeICmmq6BjOSkm5TW4hSTj-80myyC-yxLk7LnFUdkaukDhzBRjAt33FAjzzE06T_8m5yyoALHoIW90LDX59rRSI0RKY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
یک شانزدهم نهایی جام جهانی؛ پیروزی شیرین و ارزشمند پرتغال‌مقابل یاران لوکا مودریچ با درخشش فوق ستاره پرتغالی فوتبال جهان؛ یاران رونالدو حریف اسپانیا در مرحله یک هشتم شدند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.8K · <a href="https://t.me/persiana_Soccer/24842" target="_blank">📅 08:32 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24841">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ku2XTwix42_TjCTvUnI7Ju2G1ygIp4XpIxWkU5VpgJ1u--Lxggl8F_MJE68ucx3NRsNTni1vpiCtBqRbce7sf89-uc0ZnbWOkUhkjx9Gl0l7wqLOi1kP0r54lc7E4pL3dVg-RPfDVEDO8snlM1UlRoHF6nT_mU9xwjOUdoeqVtPrbtgryXO0hVDn_9AZoOGMpyqxgVlp3UPJ5D60jzRoXcUOXufY7oi6YMgyhtaX-JZXOdzO-ipSKBpn-OUFY5zGoUQivRapqsz7657valSi3Zt08HQbj7siSTBHq3WJHEcY8E3WxERc1FZ5rKM0s15TITRISr4l9Hpl2gg9jhXaWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
🇪🇸
تیم‌ملی‌اسپانیا بابرتری ارزشمند سه بر صفر اتریش رو شکست داد و به مرحله یک هشتم نهایی جام حذفی راه پید کرد؛ حریف بعدی لاروخا از بین یاران کریس رونالدو و یاران مودریچ خواهد بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.6K · <a href="https://t.me/persiana_Soccer/24841" target="_blank">📅 08:29 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24839">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OtSxbUQ-meSF_bH3itxDgpvw_R-ToM2lS3cOOeUHQUalVKH2nM-zFGf2JC_jeBKgMo6l4fuh2hELjPwR6L2luSxdzQdyM8RZuL-Iet9yWtd3hEPpt9Qn38giyv84-IYv2t8jFBRal2QcE7keyRPLRlk43KLpjuRThiWfsRYdLCC3lx7CY4-dZGSsMAVligMLMN9ARCf-KWiHu3Kj2qQKcBpgTrsMhAY0dcewMQFqao1fBIQWlTXE0afUtnGFQW7S4X0AvsddDFRU10DbDPGyiUzxomdIbAOPkuVbG8ckJqGAnYdhcmXl1TkqKqhDaYTQhrPXO-NZthyL0V4utA33-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🇵🇹
کریس‌رونالدو به‌تازگی و در اقدامی زیبا برای یه خانوم‌بنده‌خدایی‌خیلی‌یهویی یه رستوران خریده! حالا داستان چیه؟ عمو وقتی ۱۰ سالش بوده و وقتی از گشنگی ضعف میکرده این خانوم بهش رایگان غذا میداده واسه‌همین این‌حرکت‌خفنو براش اجرا کرده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/persiana_Soccer/24839" target="_blank">📅 01:24 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24837">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/swlr9SIaCrOQF4UWOreEPwTOScGoYV4mfQplUWCmdAG6kmQY5eEdMQO6EcTpGBPtJ-LC0PbaHxOE0FFlLD6gZPaug1g_y3p6fCc3bUR8GXZZeGlYEDKyVURd60m_574EXzCtIjmzJViOTvUQTDRAN2IcQ9Cni8joMovyvkK9omDEfPa5O2ot-vLUeHbOkXIkGCLs5XRFxi1QZRPvmQOaGv-NKOnrO3jsY75pfVrJjaSHbs_VpeywgFRrd0nNI1M8r_MWo3BRBJD5UJ9iwIGxL8w8nl4b092Ac4suMa7QNAWbV3ad-oLPXb_06FOQ6uVHMCijc-v58qzAOyRJ-uJJ0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZSszuRasUzDwaXcd5rvbUBMJnSKuIA2bWq4gT-H1VwRo8-y-G29EYc7KrFI-6SgFg2RKNakwr4IudiMMCP2c7b5XE_9EzZ2HV0gD69655uaZX-svIZRh2fe90STIjQ39OvpjoDP5HVsjWUD94_3CyaneU-aXpSBZHw1uh4LV8EvcB8-z6Gkp3xBUsaFBVwwgaU_f_kNXBhwImluhHW2PA0ldOfPuplZRpLGhS9z6WaPJTQBHqwbTmaux5CxwlM2cB1GO2M6v71Xqg1mC-p_lcXH6zPljGQ_giumfqwkWfq8ijVpG2IoHFPJ-toZIqHx_uOsGrlDN-NtyKP1Ft3Bukg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🏆
یک‌شانزدهم‌نهایی‌جام
‌
جهانی
؛شماتیک ترکیب دو تیم ملی پرتغال
🆚
کرواسی؛ ساعت 02:30
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.1K · <a href="https://t.me/persiana_Soccer/24837" target="_blank">📅 01:12 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24836">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nAfeiP4kxIpeeYR6X1XLz2c6GXLnHdCI4tNoSFwhtz3S_OkEMaRRVfYpzWZBFd9QmNLz3hC3B0KX-ih_g3XrqBEwIv3Z7JVas0l6yRG38IpFqEaTmX4-43I8YV1zKWz0nQSKqsssItSJCogMC8iDlNv1G_T7mGj30aznvb3mK6LVsygdfJuotAsCz-dN6tV154AknuyhzmYFiO3fR4qQqAvGz1x9-FsdkERjqnuQmwiUc6nsgO5g1OptlT1KSesPVeL96G70RRaTnRgarVe-7WRB0nL_JNlzgpjAKiuhlwfDJ5vuZORo9NmhyVCUZ_5o4YxxCK7pta2e6nT8rhMvnQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
رسول‌خطیبی درگفتگو باعادل: قلب محمدرضا زنوزی روتیغ‌بزنن روش‌نوشته رسول خطیبی
🙄
😂
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.3K · <a href="https://t.me/persiana_Soccer/24836" target="_blank">📅 01:05 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24835">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Zdu5OqhymOWgRzBUPoimAKZjcDQPLD-YeoTnFB1zBfhYqW9v0eHAdCzB5Z9G8X8poBGxXxhX5lFYTnT9zSmXoRDnokBxBdG_Ej9FwB7h5uOlIV4k7rVwqtVt5kj3aFJOgrtDxjmhFHqqbqOJUpIXp-RmhHPZhAuuaNueyTHOCd7e6Rfvcvvgkl4xvogK3kB-H5By4OJwAwQpJMzTVgRzD1ka_eTULAb3eNr5nD8v7xDFVRevvteP_bL79mQh3d_HG3FbJm_tiFJiVbiP11WhEoSR3EyMKUutTnjTUgtxWo7sn4-sre0lTfdMBp2WM5PLSlmN5D8cf1QCsGdcz_6fIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌‌ دیدارها‌ی‌‌ امروز؛
نبرد فوق‌العاده حساس و تماشایی یاران رونالدو
🆚
مودریچ در تورنتو
🔥
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.2K · <a href="https://t.me/persiana_Soccer/24835" target="_blank">📅 01:02 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24834">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SsOzX5sl-eIvWDIMX6lTaEWPBC9saHuuR6abTophciE-vLXRign_OEhz64hYQBlK64h9A1lupz2OAUM2FKS7jogGzMD_bqLGEbi22pdciklNyQ0ur1OLfRSzk53UQokb0Q31pdtpAr9nwFwRKZtJ_7LnUqe_t95TPp1I0T4KtlI9FC-i9ayv4_WQz3KW94T9hyKy7Uqh1A0Rq0lYrvHSgALcu69j-orBn5GxCs_b097IkYAjQ3Q88hSKBaCBBNhqAZaLmFmwd3fp9xtyI9Zg3Io7wMuBgn5ODkM23dL3Pbopdt1_RWfv5Wyjr80ZWIhgk77RO2iHWvAnI93dum7adg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج ‌دیدارهای‌دیروز؛
صعودمورد انتظار آمریکا و اسپانیا به مرحله یک‌هشتم‌نهایی جام‌جهانی 2026
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.1K · <a href="https://t.me/persiana_Soccer/24834" target="_blank">📅 01:02 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24831">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9e6a78bfe1.mp4?token=IcD9V6nMMthky_HFcnPlaqHx7EsS3mNLtNjKmRnlU39CFxZZ1_H6VhxNjWUB6fsLUep78YzPSVo8t-mbxiZiKrThs_zbePswaNB6nhzaddfNvIx9sXOKp4alaBSwsPcUmSD994HqpZpM0kj_cfvt96LaYz75QoeRlU5VVtJlfWiVCR5NfT3t5T5N-2T56U7vshEEpMwzGswHHzULBjYq9ziOFdAIvMFj7BE7twGUjJy9cuO2EaAbC3gReJaYEZsWFOZfqNwrUsaVNSud-GlCc0e8939rmYjoAEBFRY8OKBLbLsha2w2GKlZCB9-KiP9ZCrUm-qGYVplYyNIeZKa3rA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9e6a78bfe1.mp4?token=IcD9V6nMMthky_HFcnPlaqHx7EsS3mNLtNjKmRnlU39CFxZZ1_H6VhxNjWUB6fsLUep78YzPSVo8t-mbxiZiKrThs_zbePswaNB6nhzaddfNvIx9sXOKp4alaBSwsPcUmSD994HqpZpM0kj_cfvt96LaYz75QoeRlU5VVtJlfWiVCR5NfT3t5T5N-2T56U7vshEEpMwzGswHHzULBjYq9ziOFdAIvMFj7BE7twGUjJy9cuO2EaAbC3gReJaYEZsWFOZfqNwrUsaVNSud-GlCc0e8939rmYjoAEBFRY8OKBLbLsha2w2GKlZCB9-KiP9ZCrUm-qGYVplYyNIeZKa3rA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
بااعلام‌باشگاه‌تراکتور؛خدادادعزیزی همچنان به فعالیت خود به‌عنوان مدیرتیم ادامه می‌دهد. عزیزی بعداز عدم‌آسیایی شدن پرسپولیس از حضور در این تیم خودداری کرد و قید توافق با سرخ ها رو زد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.2K · <a href="https://t.me/persiana_Soccer/24831" target="_blank">📅 00:49 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24830">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Wb6GYARKXo_LeY6wv9QOoipbyFfYfKNzf-6bnlL87A5vJt9OgNrYAMMBubPVmRdr0Zd_fg1_1onCxB8pcnwrcSWsDrCVSLQ-Kgspga5K443xjNjlVRnfxSJ-7TPtaEtcifKtJX9kztSpqBFlI8ZHrAN96Ux3hCuqe7Ts4tjFBwHOuHDKFBaNfCB0Rs-4sM-vqt1Kn8yhXgUCmAPuyiIcr3gyog_BcptiSAcjdUJyP0_7nzJiSvikjRlOUW27X78iLxaOQgpJ6yykCUAliZhq81rD6hSUqHARmI29gL5OgH04P_hoIbqGof2kwW2xsn4UyoVG0rDD_s9fsEp_ofLWnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
نمودار مرحله حذفی رقابت‌های جام جهانی بعد از پیروزی سه گله اسپانیا مقابل اتریش. بین پرتغال و کرواسی یکیشون حریف بعدی لاروخاعه.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/persiana_Soccer/24830" target="_blank">📅 00:33 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24829">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a9kb44J2DriJowo-53AUA8WpRTGDfCVkB4974x4Cmq6kbply7vbqryVUMwYKgJ6ANS6zo-AuNeZc0MENISFT4rK-_tghGAmv5bGsRQCnkdl8OI9eRFbSGsZAGygSyVIxN8ujAc-RDVrpJZ9JuLRlXT2wLA_Y44cZ_1wMSX-ryAM4Pnh5QEs3032sHI2A46biExNi2pNqjZIw1Weoo0xJ0m-Ctm9FaeHkts87Ooormu0kQritn11SxQGxm6mnEZMBBAzvIh89Nr6u4dyz3tdWwPNTsKwJXRm9u3GVdxPYoCoSTYET0x5QNVX7FynmsMRF2p95cccd97XYdzT7ZNiI0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
درمراسم استقبال از کاروان تیم قلعه نویی؛ تو جمعیت و شلوغی گویا علی نعمتی یه لحظه غفلت کرده گوشی آیفون 17 پرومکسش رو دزدیدن.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.6K · <a href="https://t.me/persiana_Soccer/24829" target="_blank">📅 00:19 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24828">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KXnBcJGnelOGdz_nnVwMZqQfChHIv6bnDlQNQlKSFOvvLnm9OeBePQB4bf8RRcd8wgLRPBWq5c138qsAqdLPGu_H89G0jCITfV-svpHjT_xNwqvedkxiYW9DA1Ag-cvzWEUl172Y4ZC8SHGBqt3S747jMe_U75FAis8yZjtofLTD-aS-lMyJZTm4Cbc8E2U14NNkdea5aFGUGhZWK1r_I9TJZ5m0lR7JOEP8ZFdIf5ZDr6jZXiVTc5vDYLujzbJ5TmFxgEGq3VfnUxuh414VxzBs45VIBPYxfuc0c2x1ftkzvy588EbHXeavHWmgFQh2hf2xQHI6rmZItuvqkvL07g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#اختصاصی_پرشیانا #فوری؛طبق‌اخبار دریافتی پرشیانا؛ اگر اوضاع منطقه آرام باشد در جام ملت‌ های آسیا سرمربی خارجی روی نیمکت تیم ایران خواهد نشست. با امیر قلعه نویی قطع همکاری خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.8K · <a href="https://t.me/persiana_Soccer/24828" target="_blank">📅 00:09 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24827">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3237c767ed.mp4?token=Z1ldoiR5OgQtY4Hp_wBcn6q7QXCCpRwmeKV2aU5z4xlaGog8S61ukfOLKUN99IJDsntCQkkvtf5jg17Zw-eoKzZlf6S7rz_MZyB0rICUz0EqlWcezR-kBAVMdrTAPDruMhhCws4TmapIP372sq6MPjB_JZ5A-DGlSVX5AFv8DAIXzCQS_gZV-lLajQvyZUEkq4sfcsbWAxHNkYn3gr1TKo5VhF4Wyf0TWtEEXmOvdmO25r0XoOHotVpYmsfDfoC3TxKdpbcE2et6EpohLyrKjowyj0PW_ice8ymuVvnozyxky8kuIfa4IqoorOrEeQnR8kqpzedSxEtFEq0UxHDa6w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3237c767ed.mp4?token=Z1ldoiR5OgQtY4Hp_wBcn6q7QXCCpRwmeKV2aU5z4xlaGog8S61ukfOLKUN99IJDsntCQkkvtf5jg17Zw-eoKzZlf6S7rz_MZyB0rICUz0EqlWcezR-kBAVMdrTAPDruMhhCws4TmapIP372sq6MPjB_JZ5A-DGlSVX5AFv8DAIXzCQS_gZV-lLajQvyZUEkq4sfcsbWAxHNkYn3gr1TKo5VhF4Wyf0TWtEEXmOvdmO25r0XoOHotVpYmsfDfoC3TxKdpbcE2et6EpohLyrKjowyj0PW_ice8ymuVvnozyxky8kuIfa4IqoorOrEeQnR8kqpzedSxEtFEq0UxHDa6w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇮🇷
رونمایی‌از قانونی‌جدید درمستطیل سبز بنام "قانون شجاع" که توسط ابوطالب تصویب شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.9K · <a href="https://t.me/persiana_Soccer/24827" target="_blank">📅 23:42 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24826">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Qd3-pF0_v2y9x9_bW5cXJWdtuWR9Z9xlqE0jBDugKNfDo0mrqAGTqQ_D9d6PWnlYl72xFD1P-TZjVVHK2Q59Nfc_-hWqv2kX3rJRwMALx0d8ObUydqDogYBWbE4Cur7jSP5gO4HfAOpslTWkFdqXHHD7q7iUqKFoXo4SyrTmnYTUpPDloohu88dGjeqOoDaHfoxP7GesOJ8n6x6zQ3_K-kOqLmrHwuEUZUsCEArqitGT3Kfl6z_AxO6PFVq1IJoOtez_wLkG10qBY5by2iG9F-0qW3P2H9VRYygV-IhkD2bfEb6DCTYBwUbxeeHflj5QPfT3iVzkCh-OHhrMcVtonA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇪🇸
رسانه Smashi Sports مصری خیلی جدی اومده گفته ژاوی روایران‌میخوادجایگزین ژنرال کنه‌.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 48.2K · <a href="https://t.me/persiana_Soccer/24826" target="_blank">📅 23:11 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24825">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cffa11c70b.mp4?token=j7WpER2sDPr58Gh9B4YVNLCSQAy_bYiomDh1G23OEia72h9d_5VYAUP6nSY1vIZHCePJDztSPU-_FaVL9T9rM73oNX56p1LiSERZ0YEdmPvnipaPR0KFtBocdvAkzDdaFFuq9ZTcfba2BzbmqhkjZ0UfKo1314nDAY6KZysJjhSRGtIivkVjjv_LAMYXCd-VZQvtrBQUfAsnfJ6VaFOEaF66dfv15Pu5SXTTtLubCEadRavDlM7iOVoezCrN3TvVo-sAGpV1FwKfCqkWkzZuDmZo7UQ_VwLsd6FCRDZMR84FBd5xxvms7knhGJ1aD33hh11EP-hzxliJ6HxycJr3yw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cffa11c70b.mp4?token=j7WpER2sDPr58Gh9B4YVNLCSQAy_bYiomDh1G23OEia72h9d_5VYAUP6nSY1vIZHCePJDztSPU-_FaVL9T9rM73oNX56p1LiSERZ0YEdmPvnipaPR0KFtBocdvAkzDdaFFuq9ZTcfba2BzbmqhkjZ0UfKo1314nDAY6KZysJjhSRGtIivkVjjv_LAMYXCd-VZQvtrBQUfAsnfJ6VaFOEaF66dfv15Pu5SXTTtLubCEadRavDlM7iOVoezCrN3TvVo-sAGpV1FwKfCqkWkzZuDmZo7UQ_VwLsd6FCRDZMR84FBd5xxvms7knhGJ1aD33hh11EP-hzxliJ6HxycJr3yw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اسطوره کریستیانو رونالدو در یورو 2016: از برد مقابل کرواسی خوشحالم، اما چون برادرم لوکا مودریچ گریه می‌کرد، نتوانستم جشن بگیرم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/persiana_Soccer/24825" target="_blank">📅 23:01 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24824">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RncnpESqiSd8nyiM7nVB0A_4oB53N3ABu998fa7jwYI9kVa9yljpk8Bfvq0H_vYMPfVqnFPNW7irLidYpqRkpvjIR6p57fyF2FAMPtpOMj8EFNbpD6Yhu-CRuvLWmrPumwMdS-4lyJxfbXpBePi5PvdzvvaWJ6vN0pYEn5stHylGLSAsi-6ewl0lEf4s2_Eqo9p0ndnd8VNXrIPX8cK7PDF0ruiqM3qk4PU0EFPP2T9jQzaD_oHmjQG4JbkqpP1fmL2PSyjV9QgjWRRc99G1-Fkyv_FECE4bF0XNMK2koG28JF2wBi1vF4x8uFtse8ovCpEupQeiQNMqF3JWvCTf4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی؛ باشگاه پرسپولیس در قراردادش با خداداد عزیزی بند پاداش آسیایی 12 میلیارد تومانی گنجانده بود که بعد از اینکه سرخپوشان از صعود به مرحله گروهی سطح دو آسیا جاموندند عزیزی نیز به باتوجه به پیشنهاد بهتر زنوزی در تراکتور موند.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.2K · <a href="https://t.me/persiana_Soccer/24824" target="_blank">📅 22:40 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24823">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YC0ARqyvfJB4PMB2sL2Oqh2o4NZkzoi5NrNwCY3KZGZ-FZWH5_D6RCmKVXzLfN2D5k0vVVVHm1G3lOL6MM-6XiEEQh_iRM7bDrbvGfr-oxGZUjbEHjXBdHRmuF1eWI7pRMsrIlkW30EZK8mE64G5kIqlMfF7tCmrtPRlWn3df4m3ep5JwLmIyAYIYgOuL8RfsCNVDmufPi9xaipXuzcXQdHTC2ccfpHlP2haO5n3bkWgSthtEHsNLG7k_DyIOFb3A-01qimuQ3UswhZvaytsa4fMiJMnsJlB7n3uHOQCewBEvAo-3RsnttJheX7nq-26QeWu6cPlQsPrUOoXQGaxUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
🔴
مارکو یوهانسون دروازه27ساله سوئدی تراکتور برای فسخ‌قراردادش با این باشگاه به توافق رسید و بزودی از جمع پرشورها جدا خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.9K · <a href="https://t.me/persiana_Soccer/24823" target="_blank">📅 22:37 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24822">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p8glo_Jlj5ehxXjsWXcIr_JzM0n5G8_MpWt-4xO7imSEfsEdGXYeP2WIJa7KY-VbdjOnlO37Uvaa3KF9krQYgukRtvEscIPeMKlqkhV-ZXKGvCNw6lxFbU_TKByvRFE-BD5_B6EiU8OzUIfi9EPU6LA1oKe9cEOzlPyFsMb8P3hR-I5Tu5xVxH785ItOCMepRPQDgn73hSoFdkwyKVWiiPYYYoGYkUipcZzER1AcJfBKhZiy8TEl4rR38ditL9x0OciCzUAt0U9ZVC5v1VGtB2c_5Ya5ZEG87zbnEkfKZ4omXJ7UPY3OFucaxf69C0hsfwo_yA42s7PBAt_0YJJ4ZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🇵🇹
کریس‌رونالدو به‌تازگی و در اقدامی زیبا برای یه خانوم‌بنده‌خدایی‌خیلی‌یهویی یه رستوران خریده! حالا داستان چیه؟ عمو وقتی ۱۰ سالش بوده و وقتی از گشنگی ضعف میکرده این خانوم بهش رایگان غذا میداده واسه‌همین این‌حرکت‌خفنو براش اجرا کرده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.4K · <a href="https://t.me/persiana_Soccer/24822" target="_blank">📅 22:37 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24821">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBetegram</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Vmm1NZSc1wU-udqtAtPI8SLf7iPg9iQKoA-wx6B6HSQCcT1GNx7DQtNsK5-S00F6uEnE8QJ_u1ZLpUU2UCKCrD6nLm6Hvq7fc2VIbmGpV-PtOvtFuY1Itda0szcLwfwo-N5RYgmYG_F04tKsCtPEaQ3VNaG0-1psCEByOta9Mzd7fKqG_iSPkitN76S3GxUx4jgubFR-JJJ_dIKNWo96Uk4Ik3I3BIvZj1Spe35ccpZzj2ta4hclP__JOgCMx2BHDWhKp7FLwRwmRsetx0RS7CCaTKuvLOW8drS19UbeMzmyyKOUJgSpzPMxuSqvzdVz45qQPKew0GWOQqIi23PwAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📺
پخش آنلاین و بدون سانسور مسابقات منتخب جام جهانی
در کانال تلگرام Betegram
🎁
شرط رایگان ورزشی
🚀
100% بونوس
🪪
داراي لايسنس بين المللي
🌐
فعال در بيش از ٤٩ كشور
⚽
هر گل، هر لحظه و هر شگفتی را از دست ندهید.
🌍
http://betegram.com/affiliates?btag=3_l7</div>
<div class="tg-footer">👁️ 45.5K · <a href="https://t.me/persiana_Soccer/24821" target="_blank">📅 22:37 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24820">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hZ12uTII-7H6Qqrp86qKjxzHGcgKYgZdZJG3Abyk3-SZjgNFQ76XtKv9D6qJI6x2JX4CwDJMTA5MmsjZ9AqwBo3oLDUFe95C_qxK0MReJgonTS300TbfjtI5j0QavriuNWEn8-b-77DOshXXB9zVZRr7Vjzn-4q90rT2OnDuGypC8tZYf6miNefGifeh_k6K3B3e__eiWuYPDi5YX-uF50rVSQufqSzH4-GkCvz56AVGa4JlBgqHOL8BTgFzLQzUuVUiOysE8vh2XWjm_-FnvJCdT_BKMIn5-gT_F95rWY0J64GjhIS9LdRfFH7xnv47XdxJIrRKf6DFMUJKD-LEsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
طبق آخرین اخبار دریافتی رسانه پرشیانا؛ اوسمار ویرا 72 ساعت به‌باشگاه تراکتور فرصت داده تابه آفر مالی‌اوپاسخ بدهد. اگه‌پاسخ مثبت باشه ویرا بزودی بار دیگر به لیگ‌ایران بازخواهدگشت. همانطور که دیشب گفتیم قرارداد او با پرسپولیس فسخ شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.2K · <a href="https://t.me/persiana_Soccer/24820" target="_blank">📅 22:25 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24819">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g1xt3dFLpJdOY0hpi3hxlLukWKv64bcDmGDRKax_t_AKTRCscs5RgD3sqL55j3IQ88qQHLf3Ni6eN7CpFcvNxRjpkI8Ta65p6GZKGjHX_EgjI2Ted9EC-6tx2Vda3jXkCXZzXFcJe55QuXxsrYBnoso8i2vdiiCdZZfY1FlG7rK8PwrfdzUnarrXUONgKNRD06-7h3SLSo_UxdBEpsBlUVGuh3dAXSZxl9PPYomo7_Z64S7MMtLYhgiKQDnkoaMc7kHWUlkT-acD39nq6RW_yqHijQQ_5NczQOpr6_RjUcR5zTX7itc3bxWYC4VtYM0Z_zRtPivzA0h5bmbU7_Gy4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
حجت کریمی مدیرعامل سابق استقلال امروز به عنوان مدیرعامل جدید باشگاه تراکتور منصوب شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.5K · <a href="https://t.me/persiana_Soccer/24819" target="_blank">📅 22:05 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24817">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RB3OyePAf9Q-2F-XgFZSWNf67ZdO--5C1j84ADoIYb-o0TvoeeIN1TVRQZOpgohs_XLu6VGMU51FPqSMmzZGfrV59VJSUrKlk5pm2YwFWtXOyfHugpfHgVMgHjTBztsPAVMUyfBrN6djfWePwwdkUA7kE9kihkD3AhPb40RbfGj_WBRD52vQwoVlhsf7i476fo52PTut1WL7ovrcmcK3gzArEHnsBPUcN1a1dvjtnpcU4PtyQL48aSCX_AKr1Q9lnSl9LKqGsEfv4ph1oB7wkk0x6_wtR2o_jd-ZzEI_ssfQp7v0Q2ZtNMJrPFpIw86KR3I7phgzSbeBNKadzwXSTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
امشب یکی از این دو نفر آخرین بازیش تو ادوار جام جهانی و احتمالا آخرین مسابقه ملیش رو انجام میده. شب سخت‌برای‌هواداران باشگاه رئال مادرید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.7K · <a href="https://t.me/persiana_Soccer/24817" target="_blank">📅 21:31 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24816">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hl2hPSpSw0rSNy6-YOP93hHsQe1YYrfdJJtQNptIDF67PPQpa4jjdoIs7U2HCsXmMosHqcfm1-sROrx09C1mnt2x9LDswZGKm27BERCQTIIRRp79yjtsGcl8pLFQQE0gHr_Y3orLrMOA3CgJT70krBVDKcwqI2NRRpU-geoGBTufekEoSA58c3QzbInBRGxq1mz7Ys5_cZGlhjaGn0-4sQr3Yw6m8wjf-p_NJgtXSJw7huI5p82NH2Cm5mru_lzTTqY_2-kZ9etI_gFuQ0Qf3-83tWZlM3zLJqXHZ-sC2dRGGQ5lm7CQd-5cz5R0sEWCvTSem7S8ttj4wmXFaKWBBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇺
یوفاقانون‌کارت‌قرمز برای بازیکنانی که دهانشون رو میپوشونن رو وارد UCL و لیگ اروپا نمیکنه!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/persiana_Soccer/24816" target="_blank">📅 21:13 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24815">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iLpZ7AhzTLYZ4tw9x_sZL9pzlTox9wdCecrxuQ9BTCH9q5w7fRS_2azdnIRZZ4n3FpG7wd9QQ2LsmS3bRzt2APGXRO_d0X3XPKXgo7UFn3X4xQhS70e44zFXQbvdz1yxnXGb9cLvsr0-JLvYdx6ziP3Z-c_IcQCvaiciMEsQN8khwAbaIh1SNZR0y8c9hRtdg0jsT4EehE6ogjELOdmq7MkfjuP_gkQCXO5pMC6jEKa7VyYGGXDLu2rO5S12L8fDHbFjKC_TV28oDs1mv1IsY1YzfKAcBsX8qfbcQ2WfgfbDP2pOj9ashOu2GBLlHrFwgtbjSByz4VIUtGcWO943VQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🇵🇹
کریس‌رونالدو به‌تازگی و در اقدامی زیبا برای یه خانوم‌بنده‌خدایی‌خیلی‌یهویی یه رستوران خریده! حالا داستان چیه؟ عمو وقتی ۱۰ سالش بوده و وقتی از گشنگی ضعف میکرده این خانوم بهش رایگان غذا میداده واسه‌همین این‌حرکت‌خفنو براش اجرا کرده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.1K · <a href="https://t.me/persiana_Soccer/24815" target="_blank">📅 20:59 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24814">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UVv0BC--Bu-aD8RqON7t1KMOpBOrbieRAYM37DltO93-5mcHDWYwQf9F6mjwX4Ul-7YabsWBNRBPWG4MocVfLwJL9c9WuMtfjbW5PdTkoaEQ54wXV3LWZlbtMTyVnz6PdGdyMbC5axzAXym_R4rRwrb0RO08KwQ1T6gJ5RDgRoncNghcGi-IUiMZd9ILG9LDL_OTYQQfpyIaNM415dAaWXjJikBGbXzL9CkoULqMye9Reb-DDmHerJx9yOtbJTa60bMx87tuPI5yNYL0OvovPC32igq0faSpFi_n2Ln0AyhKDv9ru33c_c_W8d7w7kwrwqjxA2iQUhrnUfYS1VLoYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
یک‌شانزدهم نهایی جام‌جهانی
؛ شماتیک ترکیب اسپانیا برای دیدار امشب با اتریش؛ ساعت 22:30
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.7K · <a href="https://t.me/persiana_Soccer/24814" target="_blank">📅 20:45 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24813">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mhOZwRgAD237k9JB5rB_0ESLFUCzI27U9RnQYBmATS2o-k_igX_4la61mAaoda7z84cg5jU7_JfGk9fqzhTxyChSu6gjHTQy9DskUR4TNlrBeq1wNO9LIyRAOqCAuO2-AVRsISalAfU1rfJXAxy7rwryJc9RWSNM2aczmAIR_hthta9MhqmKHF3Ik9_hizvuen2-XmmlsRKaAF97RUQpIX7D3ZoUKmJwmyrd4MflJYlqiTcmhbD1FOT8-tZ0yLV8_n7MV5GwD9z44-kTp1MtL7mORblapbjw-0bnjHRUc7EqY9vjaVqoQDfn1x3rId8gkWjQDEn4Wg9VN0Gu85fPKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟠
امید حامدی‌فر هافبک سابق استقلال با عقد قراردادی دو ساله به تیم فولاد پیوست و قرار داد حامد لک با فولادی‌ها نیز تمدید شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.8K · <a href="https://t.me/persiana_Soccer/24813" target="_blank">📅 20:28 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24812">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GTemrAHHIKHE5EhIa_4eSPMwe_PubsbIR_Cy4RDVWcovjTiMv-8UdsMc_SEbiZZpqF_rjrbWDY8BPQOgidSaWUlnsgkUh81d24SVz0MkeoXDYDXwaS9vJGFHWzbvVFJISn3vzV9KutII0k9k5mhloUYP2VppDaJzyXMLXA96XHR-P6eih9sXQ_0iovjxkRND_po8-zuhhttN9dPau0wwxjSi4PW1q50OfGAcQfYH0TNWhVq6cd4c1KuJWcmxAZw--aZLsd25A8PtqLjlBrDotqn7CJwtnWBCmmI0ErbYQLH0aKbDeHkVknuLvKwTRVFL1lskC8LgPMPotNPtjTf94A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
نتایح مسابقات‌جام‌جهانی 2026 تا اینجای کار تا قبل از شروع رقابت‌های امشب مرحله یک شانزدهم
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/persiana_Soccer/24812" target="_blank">📅 20:05 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24811">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WlGBQ5P_lEMn-PJH2651gFoXI8wDjVlkl9y-eEp4LfVo60KuVX-BAxIzsNdvteccSVSIysWp8TNAKJOvze802XqHp7esmyW1Z96qv5L4lm8wy0rWk1QJ1qJjvB_5f2T3vkUOTgkxySUcBI4lbxsg91cj2dDRN4TEcA79dm47JRXwTMJ1IMPm8RShWGb3BLtN1fUW5q6zLQAXn4Bm37zXZBFl6tQ6gXk3Gu15_ksFMO_-kB7OOIVTTtEVZOdnNT1YPtqeyaUdY9FTTNe_kFiwBE77uy2pDKyewyS_RxTxAmlPA2xhX24HABWYPs-5PqpfTXh55NQuOq4fWZrCErX3Kg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
فیروز کریمی تو پخش زنده شبکه ورزش: تمام بچه‌ها زحمت کشیدن. آقای قلعه‌نویی گفت خدا سر سازگاری با ما نداشت و ما ۱، ۵ و ۱۰ سانت رو تحمل کردیم. حالا اگه به قول شما لپی بوده، مال ما لپی‌تر میشه؛ ۱ سانت، ۵ سانت،۱۰ سانت رو تحمل کرد، ولی ۳۰سانت رو دیگه قلعه‌نویی…</div>
<div class="tg-footer">👁️ 48.3K · <a href="https://t.me/persiana_Soccer/24811" target="_blank">📅 19:55 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24810">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o9GpTKJa8_gwvSQU18IYI8OGRug6K75SUK3e8h2kAHMFaht7kKKk8pmSW9ZNUOHkXpygHlbzxM8GZbCyK3Ax9nk3zwLwK-iD9hvdhY6vBX8rIwHiOE3Zt7_h42tAYPrpGVznPYCPsyjDT135FW0kY7LsD6iEeRkOidhHIbAuWNqj4iLdpx-H243eC3665fO-U6p5qbPX4Q93kS3lTgk_AwfcQ2dyypg72-ZYwzU7GDNRCj_5VhpV5QUPtX-XbeZGuKn2rMpsjGN_DfgeTl89IYHYz8iu5b83556xMfnJlSBneEqg-4TRnV0dpLjRgWeht_Fbegf9knKRIc35Hy7Vog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
طبق‌اخباردریافتی پرشیانا؛ باشگاه پرسپولیس تا پایان‌هفته‌از دراگان اسکوچیچ، مهدی تیکدری و کسری طاهری سه خرید جدید خود رونمایی خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.6K · <a href="https://t.me/persiana_Soccer/24810" target="_blank">📅 19:44 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24809">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AT1zX4u0NdJ229ubiWo-OZ0uTW2LSWXXHQsFEJAb43rbQu7hI-jGF4efwApEUvZXMKqTiNd97Vkx8AyN9J55yJpJVt4F9-6Z_9gU3PZ3bYiM4v0pk0HwocEjeqHEraDlUDq32mlWbSy4IemI0_Z1g4JLzIqIJRqzcQ8JXBi2veoQX-jXhuXBT8oluIusvoOPSLRA1b95iNM366YMsiFKGLgdocGwQwH0xNQMWqml7dhO1_UH75Nl9wZ03WE6BaN4WaN6QaIOxVtKrdxoEheQ1nqsauDvcoow_uJgD4waLCTH6uDUH0j6ttY9eqXfL1XjujcaguzgDWq1rTorAJ8P4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌‌ دیدارها‌ی‌‌ امروز؛ نبرد آمریکا مقابل یاران ادین ژکو و جدال لاروخا مقابل شاگردان رانگنیک.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.5K · <a href="https://t.me/persiana_Soccer/24809" target="_blank">📅 17:36 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24807">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZmXXRMGZktveaPdI779gdrtIWtaLAQ-lb5-A0syRTA-JreN3BV1NvHNyvBMeY9-sL9gB50PA1BkJS_NT-xLwehm7FQZY9BuvhGZEeXyMMgEVqYsf2twUpMFauQf17GvS7YdQDHTjZqxkYtioybhXEQRxeSubIrVbG9FHtAikdhIFw0AWzpSmkQveZ2K5BpseEwIZpcroEZvUS3sCv1SAhlPVY29za8FmR7BoG4E_Jb2SeU43l8Um53SlyHffCvYTOTUpuYNgGLqY4wGlOcxphGYW1m1V0ujh8avd9ahb66YVc_t-BGstp_ZJSK0UZ8Hi47TIVUmgTI1xVydzeLf_RQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RcM_T9kYPVXTjoUAyXl8FKSN6TuRg0XJQO6PyayTQZMW6Nun23MI81VYYoVOLPI54eTEKXrgqRbgfffnxfBAyE3pYFqryZ5u1e7OiqgF2a3yIO_PFMWH3EdQS8hpNh4tFXiv5_594fXimsRLf5o-7Ts-wAOb3UUEE3S6tjxeF57qKyiEgvGF2JEjqtNNohv7sfG3C-2r-qUL1sKZpDzSKVL5xcM7yN1eUgROiV4QGYrHfwHvDWMQkEZuinoBHGmsiT0d6N7C-Csu6vl4cA8qAegiFO-gwd8UlvsXhb-BzscpIekI4ocIs5bGmgS0BJONGM7ccKAcIR5EK87YwkD4Jg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🟠
امید حامدی‌فر هافبک سابق استقلال با عقد قراردادی دو ساله به تیم فولاد پیوست و قرار داد حامد لک با فولادی‌ها نیز تمدید شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52K · <a href="https://t.me/persiana_Soccer/24807" target="_blank">📅 16:27 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24806">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/35c080f226.mp4?token=koRN74pz6iE-nVv6QRYSE_WM9-0acfMJLHsUOEZctGtucTUD25osxfzsagW-h2-PQGgEhG8nuJYGT8BKsRDcUUuV1emUq419B-TP-sEy_nB04_oJSONfvcK3j8GkRje8_h02cfV71-n8EOoY5vcgxp_w7dzcDPwCbhnsrFYZZhLXv-Pr-Go6b1L5ek2pRLwn02_ReppilOjBOiGxeBmMBohUpYq3xaq6fbMbT2O0iCkyBcdszPg-L17nxmrUrjpahrcw8VbdkJZtAZ_9Mmppu0ISxpmpwNBfqS8PjWbtF1ZtvOZlZ8yCrINssB_QyuVcdt1Rig4PxFhtdnxanJhMfA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/35c080f226.mp4?token=koRN74pz6iE-nVv6QRYSE_WM9-0acfMJLHsUOEZctGtucTUD25osxfzsagW-h2-PQGgEhG8nuJYGT8BKsRDcUUuV1emUq419B-TP-sEy_nB04_oJSONfvcK3j8GkRje8_h02cfV71-n8EOoY5vcgxp_w7dzcDPwCbhnsrFYZZhLXv-Pr-Go6b1L5ek2pRLwn02_ReppilOjBOiGxeBmMBohUpYq3xaq6fbMbT2O0iCkyBcdszPg-L17nxmrUrjpahrcw8VbdkJZtAZ_9Mmppu0ISxpmpwNBfqS8PjWbtF1ZtvOZlZ8yCrINssB_QyuVcdt1Rig4PxFhtdnxanJhMfA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🏴󠁧󠁢󠁥󠁮󠁧󠁿
لوکاس برگوال ستاره تاتنهام به سرعت داره به یکی از مطرح‌ترین ستاره‌های فوتبال تبدیل میشه. این هافبک سوئدی‌که ۲۰ سال سن داره نه تنها بخاطر ورزش حرفه‌ای تو جام جهانی ۲۰۲۶ آمریکا معروف شده بلکه به خاطر صورت زیباش هم وایرال شده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.5K · <a href="https://t.me/persiana_Soccer/24806" target="_blank">📅 14:21 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24805">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K6MtE2QnWjOGsr3PN9KGkhR9frvaMgQkd8DkHz04k7cbr2S141WXzuGgmCG9ysdeHxBMW0usHnXPBPcWuAuGUzMsx3Vwk35nEEllXfY0QfkCsayM2fAFJ2UIbmG2U_VnuPp2K-qR78mcPI4_ATJRYnGZZL3VeyBPax7oBq758ryQvmPhp37bv4ml2kKWxu6MN-FY0007cmEqLqg29_AOqaqQt1g7wSAnBW_hULuaWFD9ZY3SnW1cvZ3Iw4MMdT2nUe_0UWHQBnZsjzvv6GJOidURfWO2ZMrUCnooXqWxib8RinshJrbTNqJpbW9W81luGKfAIgneeQOdygcYcMGU-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
بیشترین گل در یک فصل در تاریخ فوتبال:
🇦🇷
لیونل مسی فصل 2011/12: 82 گل
🏴󠁧󠁢󠁥󠁮󠁧󠁿
هری کین فصل 2025/26: 72 گل
🇵🇹
کریستیانو رونالدو فصل 2011/12: 69 گل
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.3K · <a href="https://t.me/persiana_Soccer/24805" target="_blank">📅 14:03 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24804">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f01ae4b17d.mp4?token=va0p1crClQPhu43vUAH6qZ4LpIc27inKgPHo20kDK5uDOSb6HeztaeW678TvHDIbG4nMgIP3zj79f2mC2dC1C7L3KOvsR2UTbc2L8T8-DCb7y0xHYhccPxnOnofFRiquAVF00chclo1G8D53eYAJwdAMz9DD5b-5mb3jlz5u9qht7o6Q_CN8ZVvh8rat3hnNZWUJOuJMSwdUe0YDlErOmOdqa25TIhLJaH6MBtSvWSveoSi2asaP1Kkc5Jv31oyYtz28D7JphcINF526xiXvphXXNee3LBeUGGT9Xmip8lczFTOP7OELeqJ_lSZniouNYWNpPxmhkbDZDFHlcMaTdQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f01ae4b17d.mp4?token=va0p1crClQPhu43vUAH6qZ4LpIc27inKgPHo20kDK5uDOSb6HeztaeW678TvHDIbG4nMgIP3zj79f2mC2dC1C7L3KOvsR2UTbc2L8T8-DCb7y0xHYhccPxnOnofFRiquAVF00chclo1G8D53eYAJwdAMz9DD5b-5mb3jlz5u9qht7o6Q_CN8ZVvh8rat3hnNZWUJOuJMSwdUe0YDlErOmOdqa25TIhLJaH6MBtSvWSveoSi2asaP1Kkc5Jv31oyYtz28D7JphcINF526xiXvphXXNee3LBeUGGT9Xmip8lczFTOP7OELeqJ_lSZniouNYWNpPxmhkbDZDFHlcMaTdQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
👤
بااعلام‌سازمان‌نظام‌وظیفه؛ علیرضا بیرانوند گلر تیم‌تراکتور از اواخر شهریور ماه مشمول خدمت سربازیه و باید تکلیف سربازی خود را مشخص کند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.7K · <a href="https://t.me/persiana_Soccer/24804" target="_blank">📅 11:10 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24803">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jYWUwYLSvRpbId-w-0S1yFlkSH_b-8bbWcU5Yy0n5jiBSzeHLR4wAH1zXhVBr8DtpMLdoJBB3BsJNppOdWO3rP32Bmcqbee-6lHImL3WMthkpNTWgD3kC40kwAMK7ruvrPGJBq-7ugZN3SIFRr1lmjum7t6E99PmdKd-tWv6UmWysQF9xT3QLJThbqUqWRuk_nPTlCdyAuA-f4tjyDvTTuUFCALi6503odqyFJJx0mYEoTOkHhn9fiE5imtO1Gu1sdQLG2KVk4zJWCoZ3pwO6oE8wX-XvZ-kyF-V2FOJVdNVPcLuhavxgErC8aivuyGYJzMjAiBJel8L8c07PRuEgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
ظرف‌چهار پنج روزگذشته بارها اعلام کار انتقال دراگان‌اسکوچیچ به‌باشگاه پرسپولیس نهایی و تمام شده و فقط‌پوستر رونمایی و اعلام‌خبررسمی آن توسط باشگاه باقی مونده اما یه عده تکذیب میکنند اماامروز خبرمیزنن‌که اسکوچیچ سرمربی پرسپولیس شد. زمستون هم بعنوان اولین…</div>
<div class="tg-footer">👁️ 53.9K · <a href="https://t.me/persiana_Soccer/24803" target="_blank">📅 09:46 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24802">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/291e94c0ab.mp4?token=v39czf4-vYoCOL2SLhl6ICbBLvzbWo8vXVBs-2b0bY2D87J5epiZj09Woq3uamyL4TC8uVOUh3e1W1ZET3VJncVBOLiFzrt1LAJ_TR6f1vxZ27fYhBER2mjnmk7-iKAXTE-cYRQLRq-bMgZqYaiBqD8n-PhwyyNsvEdBDiSB810c4DJaO7zXtIklfwqSrtnvvBmeWXppiuDq4cKfP_bkGrliUJeWgTe3LOpmHrmWpzXGUAdoS-NMEDZ_n79yUgwMbfDtQBB4Zr-zdglIvgV1qSqdmqXa42qeUoxM2qiK0YOK2Uts5f9QQQyC98XX_qD8Xrjuy6ywpX3O3H6qw0nshA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/291e94c0ab.mp4?token=v39czf4-vYoCOL2SLhl6ICbBLvzbWo8vXVBs-2b0bY2D87J5epiZj09Woq3uamyL4TC8uVOUh3e1W1ZET3VJncVBOLiFzrt1LAJ_TR6f1vxZ27fYhBER2mjnmk7-iKAXTE-cYRQLRq-bMgZqYaiBqD8n-PhwyyNsvEdBDiSB810c4DJaO7zXtIklfwqSrtnvvBmeWXppiuDq4cKfP_bkGrliUJeWgTe3LOpmHrmWpzXGUAdoS-NMEDZ_n79yUgwMbfDtQBB4Zr-zdglIvgV1qSqdmqXa42qeUoxM2qiK0YOK2Uts5f9QQQyC98XX_qD8Xrjuy6ywpX3O3H6qw0nshA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇩🇪
آقای تونی‌کروس عزیز؛ مگه تو چند نفر بودی که بعداز رفتنت نه آلمان روز خوش دید نه رئال مادرید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.3K · <a href="https://t.me/persiana_Soccer/24802" target="_blank">📅 08:47 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24801">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EBpbRjWeT9ny9zz7CUYikhizV2TopUqYzp4Bq3pBcgsxGXrG4CD4vBIlvozUNxqUCRuIqLSD1jb3lBoQP6HbI2b8LrPiROaHrnBLjyJG1NzXjyo8HBWVeJLYMRzZ8gDvwqVJ7kPXVIQT7o19ZCnBZP9wy0h6yaefYnwe3ZbDtz_zYjOwPE98uUYKB7N7Gwj3W8tikVp7vUi9sTgRZ0b8vLR2ZA3MLyJ2J01zUNUZM9CKhYGJEOEjh7UniFZ8LJOb8UYctAAC3eh8GObWXP5HmSN3veWOl3TZyhShOhOTJnXHYlJ-ynzj-SlSKrjtBSlEYZQpducdN77C8H_L13IRJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نمودار درختی مرحله حذفی جام جهانی ۲۰۲۶ در پایان چهارمین روز مرحله یک‌شانزدهم نهایی؛ آمریکا هم با شکست دوگله بوسنی صعود کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/persiana_Soccer/24801" target="_blank">📅 08:14 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24800">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ul76Apgl0IFqeq4z5GY7BUscpvZtwFowh-etbei2XupXikPvp7OHBanRNFotPTAgTFzXgT0Eapswk6xWZoZvKXa0S8ByEm5Xn4n8coRXPkZeidvZIKp_rUl9nf9OFCLZR1s1xD-DD1mgIcIaAuwuuluolZjAtEvN8eKusiIFSJ1ED9quXOAmoq0wxBvauKJFMfMvkRsRtUPaxC9BBWzd6D5k1o0BXKyTaE9kf8Uej_tZ2YUXWi28BEhnaZfVclisuyFQ0hMIryXxOYXY2PAgfpR1i-7Ro8FIdgXlV8HyZCp_T4t0DsoWZ0VDN6iQl4zrqTrsV6AOEcX5SsrIGXMJ2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
نمودار مرحله ⅛ نهایی جام جهانی که در حال تکمیله؛ بازی‌ها داره مرحله‌به‌مرحله جذاب‌تر میشه.
🔘
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.9K · <a href="https://t.me/persiana_Soccer/24800" target="_blank">📅 08:00 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24799">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X7nnRGyJYDVyXujtdmNj46ShJCn224f2UQstOzNhCg2JDIQ2YTsjkHqTUrnBOM4zWQ0uGdo6wnPE_D3HNqQTxTtkrwFG7R_-OAdZM9texONYsUan_DrDZWIlm8HOjnFp6Ytr9Tq9HY4y24Mz40Otr4JkyYhsOzKqhUGVMeG3ppJvV7T8QEBghauTc1_HzFuqNN2SpvDulBysNpeuCLIkyA5tDZY1jAM6I3xdCYOdqlyTiNTZtCoW7i7Ct7rlsID7v_3QmFUzF8pYNR-Dk3jENAnMEeNDSoZydQYG6LCl_fHBYKLI3GFlwyrf8ioqnZEevmWlW5Q4R1VIV9m93nY_5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
قرارداد عارف آیمن ستاره24ساله‌مالزیایی جوهر دارالتعظیم به‌پایان‌رسید و باتوجه به اینکه اون هفت ماه پیش دچار مصدومیت شدید شد مدیران این تیم هنوز برای تمدید قرارداد این بازیکن اقدام نکرده‌اند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.8K · <a href="https://t.me/persiana_Soccer/24799" target="_blank">📅 02:55 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24797">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/80ab6c75cd.mp4?token=XZvrzxk7-LE6g6-cpjJbbubSjpws9TLIxiroDPsau_lPIkK6njS8Sv6clZeFykTXnKsjJfnZ-9QEcPynAf7IGsvHRSjD600joPoaMFlwC_kxxcdK8OJVRvgLdvlDVzgfrcrqDnMjLbiLSrtXNqImYzNnH7NMAKrkshqnIJEiRFEBFL2-n4Bq9ygJk8n1oZRftamIqfxUAzRIN_lLdWux15u-pXYr-S2XedN5Wrohq4zKt0CK11VuHnBJ3tJKhmURftppeS_9o6aq20irIcbFKvossY9wuONH8Hh6hqKeLtJCISpRMJ2dEFVoyacw4QX4v-qtcp5SXEqi4GMMcf256g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/80ab6c75cd.mp4?token=XZvrzxk7-LE6g6-cpjJbbubSjpws9TLIxiroDPsau_lPIkK6njS8Sv6clZeFykTXnKsjJfnZ-9QEcPynAf7IGsvHRSjD600joPoaMFlwC_kxxcdK8OJVRvgLdvlDVzgfrcrqDnMjLbiLSrtXNqImYzNnH7NMAKrkshqnIJEiRFEBFL2-n4Bq9ygJk8n1oZRftamIqfxUAzRIN_lLdWux15u-pXYr-S2XedN5Wrohq4zKt0CK11VuHnBJ3tJKhmURftppeS_9o6aq20irIcbFKvossY9wuONH8Hh6hqKeLtJCISpRMJ2dEFVoyacw4QX4v-qtcp5SXEqi4GMMcf256g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
افشاگری‌جالب عادل از مصاحبه های ساختگی از اسطوره‌های‌فوتبال جهان از عملکرد تیم ایران در جام جهانی در رسانه های حکومتی: همش فیک بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.8K · <a href="https://t.me/persiana_Soccer/24797" target="_blank">📅 02:44 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24796">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uASA-_FrPG5IPgrzY4_rGAHyhRoGyGm6otlkGch3r8jznMY-vV23beGVO0Ei9K5ETODwB_J5fSCQDwce-oQTgmKtqoDnlSxQAtBc7IbCA1Ypbhq65lyFBqQbK-ZD4oDE2Yi4-b_DAfkYIvxIIp7kZzbjGhhZHVZaGKgAq2Kks69ElOkmamqNR_pkBgrEG067dkbT3Dj3KS6rQetowJOswuB1MN96VsoaDKzItM4EjDy4kbYVSoWKsWGsP8LbftxpdPS3DRa8nE0_4zvpt0TTEnV0E0kK9RnsY4a2lD4qyDpZuYk4GTUKv9gcYctOKParKopSpfCagrHtc3zk-sE8Mg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
یک‌شانزدهم نهایی جام جهانی؛ صعود سخت و دراماتیک شیاطین‌سرخ‌اروپا مقابل یاران سادیو مانه در سنگال؛ بلژیک به معنای واقعی کلمه مرد تا برد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.6K · <a href="https://t.me/persiana_Soccer/24796" target="_blank">📅 02:40 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24794">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jkOh_f0C7NIZqSbrZJ2eat2b0LipcLJr65c6832T-NA_42g1e-kHnH8Rk9XI_AiYkMsmFsDsbuDba-OsqbcWEzrYTkbN7a-gcDxDX1AY2xmixXDMZPWZXQY3HjYhRTihXkcZSE61-KyDp7pZQsMyaBjnnF1OLWJXlux3FY8uZfdux8AlZHy16TnF31x3FhN4IoXknjSVotoE6LhJiZ2KGwSqP6KZD8kcimqjhu2Dm3qaOXnPfAEze_bUHFvQ4CYtUT0RtDOh-Sob4hqktgD0Ifew9LKB_GYDtxVokIBWVPL1QupJ3tt9T4SU8Nq20p9UTNoHCFpcR5WN2kAXa2AbDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌‌ دیدارها‌ی‌‌ امروز؛
نبرد آمریکا مقابل یاران ادین ژکو و جدال لاروخا مقابل شاگردان رانگنیک.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.9K · <a href="https://t.me/persiana_Soccer/24794" target="_blank">📅 02:35 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24793">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sVIbSyWxXqrnNPjkExVO3nJ79TzJXjTq0ZjLyx3Xk6GCzqVjFIs_MgYSYzsWccYTCjvyRNZudHMy62_gApz354n778Q6gm5-0ARGJ7SOE31RoJDpqkUm7cKwViqtCiE5AUVUGrQgHJG40V9dvidf_4iGrgeuJHWpbQ7p98vlpnNAbW6MiZgEXiIHbi7NW9IsceMKQmHb5-AchNnsLnzvVxUI8uBDQwwWBSpEBNlHG-9CN7c68ZQiRFBr074mvIWTzIVgsLW_3Op976AyAmlmIXZAR_0kU834vQE4dtVqaVQBlKO6L2Hx5DYEqIwfV7AIlmJ8uOud1c_EVc-PLBG8Xw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌دیدارهای‌دیروز؛
از درخشش‌ادامه‌دار امباپه درفرانسه تاصعود دشوار انگلیس و بلژیک به دور بعد
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.6K · <a href="https://t.me/persiana_Soccer/24793" target="_blank">📅 02:35 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24791">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Cri0Kvpq0c8wOTSZmIUHa5lVFlMArpssSeA_B5Cra0WdapK3RubHvh4mmCjcvaivrmYhC_VXVVb1F_Ae8TPcDbf0LJ0rDLNCFx2M3rheBxH7A2Ktplnx7F9_GpSli_3hgvjHwMekx9YcvIpTzjgYubAypEPSovV7XHXpJz8C5qMrm26jy-_JPh7cUhi0zC-LlIYNG5yykmL4ptcDjCesIz8cFV6u9TQuLHDwkcxNK86QamzatFWyEAcFLAFPwderBPAMaYSzqa9MlUFx_5qoSv2q7gStiqcd0RFIwaX6JLM9-sxlX_0Rre9tjKt9n9autUrHBmAhpS2depDS_rev6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
عامل‌اصلی‌کامبک‌زدن‌بلژیک و مساوی کردن بازی برابرسنگال رو میتونید در تصویر مشاهده کنید. باید ببینیم در وقت‌های اضافه بازم به بلژبک کمک میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.7K · <a href="https://t.me/persiana_Soccer/24791" target="_blank">📅 02:20 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24790">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/daHzqoDD_MjHC1ebnjIDtcsfmj34BywFie8vKp02S8hiFt6n8_jtPM_9sb3SzH55IELs5wI0B20LScvxEUjyB6sPENptMx3334HAtbzA56ppGp3FxLIWtrtcrvhl0BoMpwVI0EQ9BQnyGi5v_vKoHTCQSSOOjO4_FQlTUSGOB79bn9kyYsyX18DiexkxhRXUCW_va__PkO4QSUh-MkGl8QRDJolCGQAVtWo2jG5AyIKo9Ok2jKAYS1r1A9tIBPZXMlXJeoE_SDyZQfFH5zAbJ864aYV_g8NJAMrwi1QbEIDn2S4DEGjCGGGXbS7gPsoPJrFgJyxXlvpgxFXA7QA5CQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
میزبانی بی‌نقص و خیره‌کننده مکزیک دررقابت های جام‌جهانی 2026؛ سال بعد همین موقع‌ها خبر میاد که جمعیت مکزیک دریک‌سال گذشته چند صد هزار نفر افزایش یافته است. اوضاع خیلی خیطه.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/persiana_Soccer/24790" target="_blank">📅 01:59 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24789">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DdpIcNke0j5UZT6Fq0yml_xehEtuMeugJosyL7f7WQroIJtTOPRYfQ-_bHSObOuGL9PkDWc__z13uITZ6IJ-l0ARpgTT1mowog6-coS0sMQzuwfVLqZymPA0LR1Vd1E7g9uVwrkrvZ2wBhp41LnGMUu9mp3zp0pHq4Bx7dBYY4EzAa7f5HQ1t39ILPWB9BTQ2U8aAy_4DJXY0RX8Ey3sEtn3txlDyTL7XqYsf2EXHeWGEFePs1m-0iXzeSv1vr9_jtoMqa9uupNddF7eTI87DnAMIVmwCwyqjIKQVKmIyH8mK3AAuZbFsvV92Fa86o_ELhvG4pLUBLLlFQxFKTVT1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
بعداز این‌پستی که زدیم گویا بلافاصله به غیرت بازیکنان بلژیک برخورده و در فاصله تنها سه دقیقه کامبک زدند و حالا بازی دو بر دو در جریان است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.5K · <a href="https://t.me/persiana_Soccer/24789" target="_blank">📅 01:37 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24788">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GLXPFqLHJKWYjrG-BI1gorGykpObmMtTvXR1NRthwYGuOHx1iIp_Kmh_6BUIyu9I4kONkSDrkIVr789KuU05dB98GnaDnQicXPU-FYJwYlCiCfD3HPoc035DlL4qvVq9be4fs9QSKcCsxqL56Xzr0Wm3HhC_JygAIgKkvmxHKb7_QBHzaQbmNVm3xgy4GbZB1-e6NssADlVS4uImieqYlGOBRXfd3AEzdPvbxNdVv4G_PEz86JuIz7Ml1byIBUXIbIpJimxtCGbeSXlQLurQs_jk-ZOhp8XVCazJC8DCkVkN0THp4ZgNoH2H7PEJG1P4j05gNlctUYKfmArVLIgW8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
وضع تیم‌ملی‌بلژیک رو می‌بینید؟ قلعه‌نویی داره از چی افتخار میسازه؟ از حذف‌شدن در «آسون‌ترین گروه‌ممکن». ‏سرگروهش‌هم‌درحد سید سه گروه‌های دیگه هم‌نبود.نیوزیلندیکی‌از ضعیف‌ترین تیم‌های کل جام. ‏جای مواخذه داره تقدیر می‌شه ازش!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.7K · <a href="https://t.me/persiana_Soccer/24788" target="_blank">📅 01:27 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24787">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UKOcpGdpnqtIQzrGWeVShDWmie5MI9UAxCs7hQLxOL43xAnn6rJdq7BXieikiT2DUvTnxRz7hJfgnf4Jd0Lev7Nl7HT6EGhkwAR2I3DKS2tSCgSQsP6c-qSWIDAAv3Epx9wp2d_7sEFQgVPPVuo7Il8ohmZz32lCofqP1NxqBgtSEN08bMiTXjiw8x0DOwub_EhpOwpuxBSL-YW9k8XaSPfnS71U38WSYfUjhtQQyz_cyE6Y9L7jvjYL0jZn4MP-ryoQCBb-2BTjAZ48euGeC-UHMTtrpwBDR6kWUaI3mNtUH2cmHTWUB0iHvyk0w2Dgrude3MbRMqdKi4NuNxsDZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
افشاگری‌جالب عادل از مصاحبه های ساختگی از اسطوره‌های‌فوتبال جهان از عملکرد تیم ایران در جام جهانی در رسانه های حکومتی: همش فیک بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/persiana_Soccer/24787" target="_blank">📅 01:10 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24786">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e3cccb9e5c.mp4?token=EmlbztiqbRDAeU639CDgApIvQAtyyd8WVlekkIloQIiI7pD-9R1W7AitoSAb8yx_OZeWSVQgwaDLZhqywX6Jj6pnckc05Mf96xmUjV5UwEx-AXQJipz74ZVcXaXFsZpIVbq1ph3P29tnROO_LbfZyPiz10VBWyRJqgS4k7XHtmufnqfCLR9G9bbdnPWm0eMVV_XQL4kjC6OPuEeYZXnDKOjqjNFnT8t8vF9vUZPFDpT3aHeqTyVpeJ6lajM7nRFd1qHDHVcE0tmKuOGOz9kaR8y1JPjGk337ouekea_-abq5eENX-ntzClH2cfRlYSWOqOBxAKgBmI9hlM4_VfEZt1lOO2lfAxlVcmvrgNkUwMRgTJuo51GJjcA8eHLfXBw_qkGFYt0Y6d0FbAbHy659dWVDoXbsIFB4dRGr94Z5OSFuKhAdEB3bHE521hp_pnmPyoDY_4GvXeP_6soUMw4c9NLM2GTPvgXcFyBHO3PyxeLH5Y2TaclQRpwbcSzeGqFc6fZ7icGyp43zeQa5IKFKsVQBdYoG-LJQ38IBJhs4vf4wB8FvwEt8DsPwETN0RDfpQhQdFe_x5c6toOqhh1bhJpDTqkGopRpVIsP5IngIUd3JewDcKwejA16siUAyi3AH7_pnPOKcLSRRTrJvHjdgz2CBpWUTFSUojDgUSUV45Pc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e3cccb9e5c.mp4?token=EmlbztiqbRDAeU639CDgApIvQAtyyd8WVlekkIloQIiI7pD-9R1W7AitoSAb8yx_OZeWSVQgwaDLZhqywX6Jj6pnckc05Mf96xmUjV5UwEx-AXQJipz74ZVcXaXFsZpIVbq1ph3P29tnROO_LbfZyPiz10VBWyRJqgS4k7XHtmufnqfCLR9G9bbdnPWm0eMVV_XQL4kjC6OPuEeYZXnDKOjqjNFnT8t8vF9vUZPFDpT3aHeqTyVpeJ6lajM7nRFd1qHDHVcE0tmKuOGOz9kaR8y1JPjGk337ouekea_-abq5eENX-ntzClH2cfRlYSWOqOBxAKgBmI9hlM4_VfEZt1lOO2lfAxlVcmvrgNkUwMRgTJuo51GJjcA8eHLfXBw_qkGFYt0Y6d0FbAbHy659dWVDoXbsIFB4dRGr94Z5OSFuKhAdEB3bHE521hp_pnmPyoDY_4GvXeP_6soUMw4c9NLM2GTPvgXcFyBHO3PyxeLH5Y2TaclQRpwbcSzeGqFc6fZ7icGyp43zeQa5IKFKsVQBdYoG-LJQ38IBJhs4vf4wB8FvwEt8DsPwETN0RDfpQhQdFe_x5c6toOqhh1bhJpDTqkGopRpVIsP5IngIUd3JewDcKwejA16siUAyi3AH7_pnPOKcLSRRTrJvHjdgz2CBpWUTFSUojDgUSUV45Pc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
افشاگری‌جالب عادل از مصاحبه های ساختگی از اسطوره‌های‌فوتبال جهان از عملکرد تیم ایران در جام جهانی در رسانه های حکومتی:
همش فیک بود
.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51K · <a href="https://t.me/persiana_Soccer/24786" target="_blank">📅 01:02 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24785">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CMg9Zw_xcpVe5ldPMBMclxa7UO9ZaP7U8ZccKkId9pdiS_6furDze6Bqi_fE7MqRhtLMrqQipmW7FlSJovl45Ztmi-BCGktb1496xERM3wZ1mfCG8ESrqE6tGwKqFh4nybsAHHjLBVb6m6LbMLcClTmR4cDTJgFrhqifqkwKEBJ88JXuGuzvmEiTiIRlXA8ZZGoLg2C12T23yhYJLxFG67mMpRA5Xkn-a-nmWF2aQwzBKyK-yJDD6X78PumBYRQBICj-ciU2uh8tLp32XGObg_sMWyxIQfjQBmd9vW3is3tIs54JmEZlJVei5xIuURj0qHjx8CazmT4nulFYT2cq-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
#فوری؛ نشریه مارکا: الساندرو باستونی مدافع میانی اینتر میلان درآستانه عقدقراردادی چهار ساله با رئال مادرید قرار گرفته. توافقات شخصی صورت گرفته و باپرداخت50الی60 میلیون یورو بند فسخ باستونی 27 ساله توسط افعی‌ها فعال خواهد شد.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.7K · <a href="https://t.me/persiana_Soccer/24785" target="_blank">📅 00:17 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24784">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZN3XhRdFBp_z-YhMdE1-4w1Ya5KrHWpx1J_xkFMV6fx8wwwZ66vnazd5xVG5JrZsKW1a61aGsc9a3skyZqL7MoPa9QzT6EKjC-xfp-QVma_FYBS5aczSirCcEjOGs7ubanT-b6tPVHhblDGXsDHtFR5IEbbscmqqIMqo48jUhlLCMoe6FapbYgA6ps7US70uRYUEkq047YbGxSJzYOQ-JYqliYTLjUkr6GrrAirss5wuF81Mxp2UT3WOY39DCM3wP0NMUAdko0NF16GH59ryPDhg0fRicAUV5haEu4CDsv6Sbipaec25WgBOu5LL0P4DBGinE3QE9fEizy54C5T8Sg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚪️
🇫🇷
#تکمیلی؛ ژوزه مورینیو سرمربی رئال به پرز گفته نیازی به حضور ادواردو کاماوینگا نداره و این بازیکن بزودی از جمع کهکشانی‌ها جدا خواهد شد.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.9K · <a href="https://t.me/persiana_Soccer/24784" target="_blank">📅 00:12 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24783">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/37e51a27aa.mp4?token=gUrWdm86CitDDScI1LarGzoUPeC80EAaR2f0boXNh2teG1DyeVhGmCCZH64MGPlDMkOuzoH7d9QIjIr8i4wj390MS7ETsRpdNq8hvofxuOubYkCciTK-MOHvOW59apJEPd-qdWciq8H4VAmPainQD-YU9Vr0ZlnEW9rSwOQOtbkzq_h7X6nAus6hqAPvri5GiDtJkcJ4cRBSCDruYqBqtfLxw0LnR9PDA_Lp4XCq2Zn-P5AVRYubQQKIzAEkEqrlMkfUR9r6rZ1U3WZEdLhFC1ISUQWmsNtyG0xaNo49oXo_wU4v6xNBEfYk4g1HKvMCYOpAf-l5gmwH7RfPlhspQg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/37e51a27aa.mp4?token=gUrWdm86CitDDScI1LarGzoUPeC80EAaR2f0boXNh2teG1DyeVhGmCCZH64MGPlDMkOuzoH7d9QIjIr8i4wj390MS7ETsRpdNq8hvofxuOubYkCciTK-MOHvOW59apJEPd-qdWciq8H4VAmPainQD-YU9Vr0ZlnEW9rSwOQOtbkzq_h7X6nAus6hqAPvri5GiDtJkcJ4cRBSCDruYqBqtfLxw0LnR9PDA_Lp4XCq2Zn-P5AVRYubQQKIzAEkEqrlMkfUR9r6rZ1U3WZEdLhFC1ISUQWmsNtyG0xaNo49oXo_wU4v6xNBEfYk4g1HKvMCYOpAf-l5gmwH7RfPlhspQg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
🏴󠁧󠁢󠁥󠁮󠁧󠁿
نجات‌توماس‌توخل در10دقیقه توسط ستاره سه شیرها؛ هری‌کین باگلزنی در دقایق 75 و 88 مانع شکست فاجعه بار انگلیس مقابل تیم ملی کنگو شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.1K · <a href="https://t.me/persiana_Soccer/24783" target="_blank">📅 23:45 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24782">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/brPZyJNttos4LN4Ghsngp9s2PLVU5aa42_Oz5VZT6pSLLs7g_s6pbDUEI1vlTmYf8ruXSc873j-g2kS6dqfmdj7fs3-S3VgTQQzhYB0eEwJGXPeSO2zZ_iVazyhxw2YU5f-qo3fkXfscNixT6pBouP0rVH-YpX0X-Ne_9XuR4dxk7aE-ynTDDqC9NLOAzsex3RZCxojjcOG4XOHUd6VFv7Yvv47bSFQr8HHvjZH9QPq5PPShWS1p-8C3CHbZt0LvB2LpYZAAVo2ZT8_XJVtkiCr9b5_dI_TzryGuCifeCZKmM7cCOB5fJwMi8u2W49R94GM976rnkFwbL3jobWDQFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
جدال‌جذاب جواد خیابانی
🆚
خداداد عزیزی در ویژه برنامه رقابت‌های جام جهانی 2026؛ سرپرست تراکتور میگه آقا جواد واقعا دیوانم کردی دیگه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.4K · <a href="https://t.me/persiana_Soccer/24782" target="_blank">📅 23:39 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24781">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q8wRscR-bRwtFlA9WoKrGqHg5f5voRhbCy14ljJ7blUd3pIPV5qBSG4RKri4dUO7Y95W8i-PpBQT5nDED98NaOvSzM7hvGumhASKvuQuJLIY_RCNZ9vI4__x_aUi_OovZyM9XZHJkdLkHDID7d4yAETuYA-dYhdbGIOI_iSfVijP_9f1fVV9sNP46hZeHWnNFYiK0yFmaLF1ZBPQo4d_dBgpKQUWA2e7bOKVbdz0CtksaxO_iXlSFB_QMPcgXbx75zww5VTe3spicN-u36m8fQEYcGROFzDqIxwSCWd0ELLzrc018pRZXwoGBforRsAoHoWOo96MB41vru0P7csHNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇫🇷
حمایت تمام قد امباپه و فرانسه از دشان؛ مادر سرمربی تیم ملی فرانسه درگذشت و او برای حضور در مراسم خاکسپاری، اردوی تیم را ترک کرد. دشان پس از مراسم، دوباره به اردوی فرانسه بازگشت تا هدایت تیمش را ادامه دهد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.1K · <a href="https://t.me/persiana_Soccer/24781" target="_blank">📅 23:39 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24779">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/32137f795e.mp4?token=cuCnLep7wd0_o4Fo4rFPQryzMjbRFwm0V0neV_I1gZrNj3wuDa05Vi7poL0dQVTRsvOvlN56IsYipLFWDenv51zAXONyWOK6ympnuNXfoTch2UYTlyWiHLagbrRreRhaHM-w96SWF6Ws48GDIFFcFqnn01SKu9wQpu03CVD7gFmJ8X-M-J86zT8ChF6Bbvndhonyq5qGc-puqwHH3uEAaDOOIwTIiqOPvtaWj7dNjpWviUVya8O3fOAGSnQ6s1AvfQZdy6vRlU-PYO5idJG5kPlXjMRuxaBuGn4QCTvaDCktgW4ADTjkiFxbEo4q3gI7sTnlfMcwAH4yIs7jjbINZg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/32137f795e.mp4?token=cuCnLep7wd0_o4Fo4rFPQryzMjbRFwm0V0neV_I1gZrNj3wuDa05Vi7poL0dQVTRsvOvlN56IsYipLFWDenv51zAXONyWOK6ympnuNXfoTch2UYTlyWiHLagbrRreRhaHM-w96SWF6Ws48GDIFFcFqnn01SKu9wQpu03CVD7gFmJ8X-M-J86zT8ChF6Bbvndhonyq5qGc-puqwHH3uEAaDOOIwTIiqOPvtaWj7dNjpWviUVya8O3fOAGSnQ6s1AvfQZdy6vRlU-PYO5idJG5kPlXjMRuxaBuGn4QCTvaDCktgW4ADTjkiFxbEo4q3gI7sTnlfMcwAH4yIs7jjbINZg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
شوخی جالب هوادار تیم ملی با امیر قلعه نویی و شجاع خلیل زاده سرمربی و مدافع تیم ایران
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.5K · <a href="https://t.me/persiana_Soccer/24779" target="_blank">📅 23:28 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24777">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i6htf_yOAFm7Wnk8bmnJp9aNvKT1sY7y3hI6ZF3BPpsrCzXsploz48v9m6r1FzwjqYEN8RSxwL-oW6q9RuKjsAciWnl4DrgkghcmXWnE8LRnKPh61xxH9_ZePHbFxS4cFvFLrW-VEZevsC-CWdxCifXNh2A5KNzLtybOgi8v-P5dYJOKhQrgTIFOT3KMBbMmlnEJU5WzTZhhkkD0iE_4XQFHFSK7ukeeF7D3RW37nlrxvMTRsXU6zsqf9pt1WaHDkqFY1rgETco4nYR756aj6Y_P44uu_TZoO4tjkTf8NIhwFLNw1opCMm98dND1N6rlkHTiiDOyPLDe6ubJ8nbaOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👤
تیکه‌های سنگین‌وداغ‌ عادل به فدراسیون: نکنه جدی‌جدی پس‌فرداصبح با سوییس بازی داریم که ما خبر نداریم اینا خبردارن که مراسم استقبال گذاشتن.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.9K · <a href="https://t.me/persiana_Soccer/24777" target="_blank">📅 23:15 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24776">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">👤
تیکه‌های سنگین‌وداغ‌ عادل به فدراسیون:
نکنه جدی‌جدی پس‌فرداصبح با سوییس بازی داریم که ما خبر نداریم اینا خبردارن که مراسم استقبال گذاشتن.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.2K · <a href="https://t.me/persiana_Soccer/24776" target="_blank">📅 23:03 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24774">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/310289702f.mp4?token=G6vC33T74FsT_OKkJi0SUeoaA81LJrvMfOeG9oN7b0-fTksnVf3rNO4XZ0GcCzftnj30khVzKxGTeOb3_FySC7FiAE7f3SIYcgXL5GPl8Kt-I_YNt7TkAbJgPBrW-Gp0Dcpouwn2uwKOKgmjly1kh3XqhHqqAN97J-qlnOuikK60pFcbvzv3W6H8IJRsaxMh51_2rYHAOvV90B6bdx6zcRnDXbwScNJYDbpvo0Yxrf8UTUhQ-k9hG9xZMRyEEDMhGFuDr1lFKoKo9qJ5e4bzOrdQbWIxSd-R0HuwBScZHfQVWZULGTQXTHajwqwEW8qWoqQeJ740Hv_WvsWTepZFMw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/310289702f.mp4?token=G6vC33T74FsT_OKkJi0SUeoaA81LJrvMfOeG9oN7b0-fTksnVf3rNO4XZ0GcCzftnj30khVzKxGTeOb3_FySC7FiAE7f3SIYcgXL5GPl8Kt-I_YNt7TkAbJgPBrW-Gp0Dcpouwn2uwKOKgmjly1kh3XqhHqqAN97J-qlnOuikK60pFcbvzv3W6H8IJRsaxMh51_2rYHAOvV90B6bdx6zcRnDXbwScNJYDbpvo0Yxrf8UTUhQ-k9hG9xZMRyEEDMhGFuDr1lFKoKo9qJ5e4bzOrdQbWIxSd-R0HuwBScZHfQVWZULGTQXTHajwqwEW8qWoqQeJ740Hv_WvsWTepZFMw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇫🇷
حمایت تمام قد امباپه و فرانسه از دشان؛
مادر سرمربی تیم ملی فرانسه درگذشت و او برای حضور در مراسم خاکسپاری، اردوی تیم را ترک کرد. دشان پس از مراسم، دوباره به اردوی فرانسه بازگشت تا هدایت تیمش را ادامه دهد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.8K · <a href="https://t.me/persiana_Soccer/24774" target="_blank">📅 22:45 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24773">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cArgN_VhIeDpWafFLWtpEB-W2a7qISoMyuVdSybleMdCNRwvTeFKMxesBtcfs7MgzO_ioPU1rIM5BpToIs6lsunC80bCkZGCywvCWzMsGNdHu27ccrkmYOEiyXlJdWka2UpVyE1-nbxZ1kYDmXffC4D-vOioRyz1l5TpBODqDSAQ6spcf4EHf-rXvtEGInKGl566Db8pZ4rxTa54hVIRMTfbS-1GvSE0tivA_szCm90CUEcq8by98GkBgsAlnWbA6OSNqqm7t6CbJPjyRHkkQU808sCAQM-bQ7ZKA9Zuh0LGnit72vvcW03x9hEQXQqv5zl7HmnIev9pNNVkLcGEKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
🇧🇷
این داداشمون کل بیخیال تماشای بازی برزیل مقابل ایسلند شده و کلاهدفش‌از اومدن به استادیوم یه چیز دیگه بوده که تو عکس مشخصه دیگه:)
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 51.9K · <a href="https://t.me/persiana_Soccer/24773" target="_blank">📅 22:12 · 10 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
