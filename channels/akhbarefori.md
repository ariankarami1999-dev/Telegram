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
<img src="https://cdn4.telesco.pe/file/tdTmhAtoY087R3ehIomqW-t5lWjSSd-RkzI0yefhIMRQAuroPMVLWNEWEU6br1prKDX84l9-_ALdKRnn-EjmcYCAO-S9-rSFsgXSkG2wEOs6-VzFxiZLb5chsSeQ0e8okwU-W5xm1Q1YhK9ITe-nfOuhOee5meOXqFCDDt3HveNNrgZwquOGibjSEBmlxz3WFYcoTuMjEg94YCQFllHR52a6QR-ruXThF-7P0n8ZpDFPOr8YMBxBE6VK1khOmCrsMEMf9ZVqwid26WkI6xCtzMcqLqWbT-U8OxdwyIpeoqO0Z8ZKlk32OesTeciseJuLo86aVxi2bUTlakWXYDJSdg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرفوری</h1>
<p>@akhbarefori • 👥 4.32M عضو</p>
<a href="https://t.me/akhbarefori" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽تبلیغ درکانال خبرفوری@ads_foriارتباط مستقیم با ادمین تبلیغ@newsadminجهت رزرو تبلیغ تماس بگیرید. 09018373801؛ارتباط با ما@Ertebat_baforiiتبلیغ در ۳۰۰کانال تلگرام@Maino_marketer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-06 03:00:22</div>
<hr>

<div class="tg-post" id="msg-693565">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rnWqptSo1Vno7hMR7oVhUyOXFA4Wzqs3xitpQ7kSQ01IXivt1iY0srCLoI1WWSg7JJwI-EyK6GvyrYY2ApqQ_FLLOw5MloRKaucq_BPZiUD2K6Dx_84pJkws0JSI66zmCVCvv35HTr8RpsSaXE_qIIVm8zi8vaZoZ82MDye-AVQvjyvDiBvd6jmLtgxBzXePJXrFI6txFHBK378pBTzSps97BCbkya-f5ihqB3Syw76QX8mkDaKmGrtUjU_S7y1iwcb5RTdLuJ22ILryH9VmH9XxKFJAoQDhQop2yYgo-5hnzrgz08jWTW1vr-6D-ze3ObFG0RRcxn1yOjEeSCHeGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
یکی بخر، دوتا ببر! پکیج ویژه خودرو
🔥
مینی جارو شارژی
AS-228
+
🎁
هولدر موبایل
YB20-3
✨
مکش قدرتمند ۴۰۰۰–۴۵۰۰ پاسکال
✨
باتری لیتیومی ۲۰۰۰ میلی‌آمپر قابل تعویض
✨
مناسب تمیزکردن خشک و مرطوب خودرو، منزل و محل کار
✨
هولدر با چرخش ۳۶۰ درجه و نصب بدون چسب
🚗
یه جارو جمع‌وجور + یه هولدر کاربردی، مخصوص داخل خودرو!
✅
امکان  پرداخت درب منزل و پرداخت قسطی
🔴
قیمت 1,298,000 تومان
خرید
👇
https://memarket24.ir/product/fast/63781/180124/</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/akhbarefori/693565" target="_blank">📅 00:30 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693564">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b16889c96f.mp4?token=rOBZKC9ae_iTqKayR-3MhfobnUIkUR1CAaH3Uu-vp71IOWGyGebumXKBGPLtQI6B_7hal6ameBd9LC9A1zFniAXNQTWk3NMwVtt-NoZpJzM0kX2JXhoocsDBudt3eoldQhV6aoTE40N3cMjeJT7H7o4MgbZGtzu9KImeBYNB8AoPT3JHbpYvf3iGoaESDCo2IcQYqw5uoRjr_C6SMhxC9BozLtcbkkSKfcWnBlhb5NL8UImIfUXekNWYWqZWgX_Mggg1GcfTQPvF6n4uTwe2wcFjgZj8ajm0vjNoZ7JqWt64SAfMZGk24JHCSCT70tzPkcXAcT6y7n2jBrEyft1xGQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b16889c96f.mp4?token=rOBZKC9ae_iTqKayR-3MhfobnUIkUR1CAaH3Uu-vp71IOWGyGebumXKBGPLtQI6B_7hal6ameBd9LC9A1zFniAXNQTWk3NMwVtt-NoZpJzM0kX2JXhoocsDBudt3eoldQhV6aoTE40N3cMjeJT7H7o4MgbZGtzu9KImeBYNB8AoPT3JHbpYvf3iGoaESDCo2IcQYqw5uoRjr_C6SMhxC9BozLtcbkkSKfcWnBlhb5NL8UImIfUXekNWYWqZWgX_Mggg1GcfTQPvF6n4uTwe2wcFjgZj8ajm0vjNoZ7JqWt64SAfMZGk24JHCSCT70tzPkcXAcT6y7n2jBrEyft1xGQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اینطوری از هر درختی می‌تونید نهال بگیرید
🌱
🌳
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/akhbarefori/693564" target="_blank">📅 00:24 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693563">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a5eed1c3cc.mp4?token=NlMl46Wcj9atmnIkbYi90T4UdmH7gi9ZFwNg66wirnjf0Xygf9kSE7vbHQN1IXfhC7zoEKaY0ctLo1gL5sRTMO8xGRKmB_W9a-AynTdp-I0ZaZ41zYD9Ly2AdNUHCUsiJUSyOmlbZ2XcO73gmdSCpw_nF_nhdOl8DXOnjhvti-S82GGOQQsxA7zlF3kjXXos2L07zxHA-mkZ86z6CYas6s8_UBDZcgp3KHTqCsG29sN6d2L8r8ybO9QbKfbPQM9The7xOqW0Y2ZaFgC25yBYvWc9tlA6J2Q7YaoSRhJaEJHToxp_2TjJb_DNBC1f0MpUDKH-yckMGclcQrje2tLoskvJIGwO-x99rkDqZLgWjI4y7SJNaBo6dmGS5Q5WOJhWR23g5QyARmV_fUBy5u8tDdCDqVfb7i-az7DNJ2OyPFkE5CNrw8KqlQr-Ovg4whxtb9J4KeZWcom0LyGt3u6FdaRCwSr_cUcUt9zT9f_L9u4jiCtTS83LgdRHEu_CRT8Jhxx8k5LghkbZHRW6BsBAU7DBxd1_UitFkcNUf7eKJSb1meP1LxQnn8YqKa9Tqmi-jSmTWH5-Qpsn0_ehmaeRtGi5w8WVhR_0aqxcMUfaF4h95kjGt7oKREoL635EQOojCisFCWaidzaTuoOTHObdEO-NIwbjuVZcY2XUTsJDap8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a5eed1c3cc.mp4?token=NlMl46Wcj9atmnIkbYi90T4UdmH7gi9ZFwNg66wirnjf0Xygf9kSE7vbHQN1IXfhC7zoEKaY0ctLo1gL5sRTMO8xGRKmB_W9a-AynTdp-I0ZaZ41zYD9Ly2AdNUHCUsiJUSyOmlbZ2XcO73gmdSCpw_nF_nhdOl8DXOnjhvti-S82GGOQQsxA7zlF3kjXXos2L07zxHA-mkZ86z6CYas6s8_UBDZcgp3KHTqCsG29sN6d2L8r8ybO9QbKfbPQM9The7xOqW0Y2ZaFgC25yBYvWc9tlA6J2Q7YaoSRhJaEJHToxp_2TjJb_DNBC1f0MpUDKH-yckMGclcQrje2tLoskvJIGwO-x99rkDqZLgWjI4y7SJNaBo6dmGS5Q5WOJhWR23g5QyARmV_fUBy5u8tDdCDqVfb7i-az7DNJ2OyPFkE5CNrw8KqlQr-Ovg4whxtb9J4KeZWcom0LyGt3u6FdaRCwSr_cUcUt9zT9f_L9u4jiCtTS83LgdRHEu_CRT8Jhxx8k5LghkbZHRW6BsBAU7DBxd1_UitFkcNUf7eKJSb1meP1LxQnn8YqKa9Tqmi-jSmTWH5-Qpsn0_ehmaeRtGi5w8WVhR_0aqxcMUfaF4h95kjGt7oKREoL635EQOojCisFCWaidzaTuoOTHObdEO-NIwbjuVZcY2XUTsJDap8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
محسن خباز، تهیه کننده تور ایرانم علیرضا قربانی در ایران: امیدواریم اجرای علیرضا قربانی در خراسان بزرگ هم برگزار شود / این اجرا نیازمند همراهی دستگاه‌های مختلف استان است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/akhbarefori/693563" target="_blank">📅 00:21 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693561">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/O5hFLK2D-2OJk-aAd4WHiE_jMJn17RgyKBMWd_3dv7dXYkfvDtlGrKgVaLBSEwN92Gk99iZ-UvqRed_wIj_3u-d2Hs8aFNS1Er3RBAwKkf4LmH-wjACJRv_Hx9O7l0M5uHC2Hc8UHFeXHGLKqmqarLp2Xa6WNOX_KdfXKRnuaFtxOz-GPtju03C_OJjDXcntm9MX_SWmU4TY4NYB0vNQgCsUkA1xYu_2vLDZR21wBpQIWSMnSXnu8XMoP0WgKpbeCBg4fVOu28ZE3aWOoCsxAgbDtru6pGnUI7WSiqAXqKlRiAjV8RwtSc2lvie8M8uEOen-ml51pyqGVVBlypaHqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VaNoSZcAzanchgU8XdPb8sL-3AchXrFZieYePRuIIpq60OJSevDQ4OcYaJV1_SB1uM-jc2J0A0QbBppOEDx8oTxbYUD4Pb8wwG6l5A1RVpvqZa0RUFIc6SyzNK2Gi_67LAyKfroiLufALjJW-oanks0oV6RLxvUUwpfWUlE9wroILijxAubhUvsSjgEHbxHME7evy_rqdJNZbjafhk4NOFohK1HQ-Ifid-Ucq0VfEeqs5Mf2aluvENpwitvN_mz7Y2nmOvGoOnQUia0ZonCztfwMheUy7Qyiqe8B1zeDORudBwKogJvqHs1euLeOs2UP4tiiItbv5qgSZrVXjXPFKw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
میدونستید تو چت جی پی تی میتونید حیون خونگی داشته باشید
🔹
از این راه فعالش کنید
ChatGPT → Settings → Personalization → Pet → Select pet
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/akhbarefori/693561" target="_blank">📅 00:14 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693560">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7659ca5aac.mp4?token=KMYQLBVEq1ESbzFzQtClv6SDUjtjFbBXic0HqS1H_p2FLqyUQff_3OgxTG4BNhUcBa1YuQFerx5g6mIDhDe_gXOHwmHaR1gWTPgGMyLstWFVAQZG8BMrTtZL3c5PYvm9f0HKSRTD3xLz3w4hX69pOonSr0PWIuJIpPPgj27vvec4EMKfke9A0GBpg6B3G4ac2rMt_08W5xjTvynXpM8HbMChvvpgTbdIV0gPQQ4DditnQ9E2JSuVil9B1hm0969wDig4gUw5OzM-Kgu51a--PSmeO9i0gsgxx6VCZXdTReGH1eCxJl6ePnsXDvntruIWhW2ratMyN8qs5kogMlqQWw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7659ca5aac.mp4?token=KMYQLBVEq1ESbzFzQtClv6SDUjtjFbBXic0HqS1H_p2FLqyUQff_3OgxTG4BNhUcBa1YuQFerx5g6mIDhDe_gXOHwmHaR1gWTPgGMyLstWFVAQZG8BMrTtZL3c5PYvm9f0HKSRTD3xLz3w4hX69pOonSr0PWIuJIpPPgj27vvec4EMKfke9A0GBpg6B3G4ac2rMt_08W5xjTvynXpM8HbMChvvpgTbdIV0gPQQ4DditnQ9E2JSuVil9B1hm0969wDig4gUw5OzM-Kgu51a--PSmeO9i0gsgxx6VCZXdTReGH1eCxJl6ePnsXDvntruIWhW2ratMyN8qs5kogMlqQWw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حسین صمصامی، نماینده مجلس: احمدی‌نژاد در دوره دوم ۱۸۰ درجه عوض شد / به نظر من برای رضای خدا کار نکرد و عاقبت‌بخیر نشد
حسین صمصامی، نماینده مجلس در
#گفتگو
با خبرفوری:
🔹
احمدی نژاد در دوره اول خوب عمل کرد و ایشان را با شهید رجایی مقایسه میکردند، اما در دوره بعدی ۱۸۰ درجه تغییر کرد.
به نظرم احمدی نژاد برای رضای خدا کار نکرد و عاقبت به خیر هم نشد.
🔹
من خواهرزاده پرویز داودی نیستم، اما ایشان را از دایی ام بیشتر دوست دارم و مرتب برای ایشان فاتحه می‌خوانم.
#فوکوس
@Tv_Fori</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/akhbarefori/693560" target="_blank">📅 00:11 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693557">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">🔹
از داغ‌ترین خبرهای امروز جانمانید
🔹
🔹
بعد از انتخابات آمریکا "جنگ بزرگ" رخ می‌دهد؟
👇
khabarfoori.com/fa/tiny/news-3248205
🔹
معمای رد پیشنهاد ۷ روزه؛ آمریکا چه می‌خواهد؟ | مسیر بعدی ترامپ چیست؟
👇
khabarfoori.com/fa/tiny/news-3248252
🔹
همه‌چیز درباره محکومیت یک نماینده مجلس به زندان | شاکی کیست؟
👇
khabarfoori.com/fa/tiny/news-3248230
🔹
هوش مصنوعی چطور جایگزین نیروی کار می‌شود؟
👇
khabarfoori.com/fa/tiny/news-3248284
🔹
خبر مهم برای کارگران؛ توافق اولیه برای افزایش دوباره حقوق | رقم جدید مزد چه زمانی اعلام می‌شود؟
👇
khabarfoori.com/fa/tiny/news-3248171
🔹
خبرهای داغ امروز را هر لحظه اینجا دنبال کنید
🔹
khabarfoori.com/hottest-news</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/akhbarefori/693557" target="_blank">📅 00:04 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693556">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1e62f34627.mp4?token=iVPrfBEWSpAs4gN77LV8YJNROQR8juR-VAqLC7MXKp5I5FKO7FvTh9VGoPQFIk6tg9HBlVAHVX5ODPLXdUugruvSfcTzsxBfQ3WrF7Qfc9QnF-8wrYRbo7If_KGGdHWwzt2kt4GUgUnexPa9r-GvyogQdLDF6oC_rEy2ypncUhbZkaG2Ne-y8UOsUnU_ycTY-5bgQMGHQzzS2hE1tMJxevUo540c3hBFQinouW_6Dg3DJjnjT_CGFhpuqwX7j408xhcJxscCHjEDcdwN1iY9ynpdbQCudy5yx3-fbdKFNCT2mxjrktdiBhEvqGO00nJWv7IOjsahDZ4RYC9l6J7R_g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1e62f34627.mp4?token=iVPrfBEWSpAs4gN77LV8YJNROQR8juR-VAqLC7MXKp5I5FKO7FvTh9VGoPQFIk6tg9HBlVAHVX5ODPLXdUugruvSfcTzsxBfQ3WrF7Qfc9QnF-8wrYRbo7If_KGGdHWwzt2kt4GUgUnexPa9r-GvyogQdLDF6oC_rEy2ypncUhbZkaG2Ne-y8UOsUnU_ycTY-5bgQMGHQzzS2hE1tMJxevUo540c3hBFQinouW_6Dg3DJjnjT_CGFhpuqwX7j408xhcJxscCHjEDcdwN1iY9ynpdbQCudy5yx3-fbdKFNCT2mxjrktdiBhEvqGO00nJWv7IOjsahDZ4RYC9l6J7R_g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
جیرجیرک غول‌پیکر مالزیایی یکی از بزرگ‌ترین حشرات شناخته‌شده در جهان است؛ اما برخلاف بسیاری از جیرجیرک‌ها، شکارچی و گوشت‌خوار است
🦗
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/akhbarefori/693556" target="_blank">📅 00:02 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693555">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZvqWaAFAB4UlzMvoPCafEj8GDOPrdMoG9PXjrzQP0hRbgWo4l5GBal1QEr6tfksigj1atWdfIql4Jmv1FwM-4yfnoQZs7gkF6Q9jSjwEojPo88j1K8Q-6pVABe3CdcFIxhwrXMROiWXnHxVk0ntAuKWYG9-UMEIVle6TXTivp_eWyjRGNGdg7l5RKB-Ql0qErm2ffjH7Hly15-rB8KRKkeeSurK1uj0Sd6bb-zQ9GVNQlKGBGxhdIGwv5b3W1LKhAZFPygB0Ijih25DHNcNZWrE0KIlLkwPdB7rf_JQRSArg8EIgrgLKxMcn0QpQlbcUheBRynr6zSaBOSEMJVd6iQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👟
کفش اسپرت نایک V2K Run | سبک و راحت
🔥
مناسب پیاده‌روی، استفاده روزمره و استایل اسپرت
✨
رویه مشبک + زیره نرم و راحت
📏
سایز ۴۱ تا ۴۴ | ۴ رنگ
🔴
قیمت: ۲,۱۹۸,۰۰۰ تومان
💳
امکان پرداخت درب منزل و پرداخت قسطی
✅
ضمانت تعویض ۳ روزه کالا
خرید از سایت
👇
https://memarket24.ir/product/brief/63638/180124/</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/akhbarefori/693555" target="_blank">📅 00:00 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693554">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromخبرفوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nUCtfVzUGZh78Rf7t6cGAiXJrs2iukg-Ic0rClibZpWcY8F55iELPSVejtVxcxbd_0bbt71IB90gODCQsc-od6nLAZ6Onv04f9nNgynbyyRhRkHMj-uOhhv3FsDYfvQVg56UzQdnnDH71hujq2Qllm-klf14cYlhVEhn5z18es5wDV8YdvXufvAw-Z9fFaDolh80KltsW1VKU4mZhcuuQU4BE57u_paUfLkIxAvPjkMBXXJwTetFQmXLq_EOeqFs3MJs5CKwe4N2XoC7s535grSoE8k45HsRvVLiGNmkM0TVfyp-EkcVXsJj_Dox1tpBgks08zSWni0FH2JvhukQPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
با هم دعای فرج را برای سلامتی و فرج آقا امام زمان(عج) می‌خوانیم
🔹
با قرائت دعای فرج به این جمع میلیونی بپیوندیم
@AkhbareFori</div>
<div class="tg-footer">👁️ 6.27K · <a href="https://t.me/akhbarefori/693554" target="_blank">📅 00:00 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693553">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5d6611008e.mp4?token=pGsYyEXGJt9gFNpsYzLnxReEy_VENcnyt6GcdryZJCGOlPNnZxuRRXK32lk0BMwxRIzbclosPu7Ucz4TvH8BKN6dT6OJNthdX7H2K1FWQ9hv27LS10u5f55H2xDWqqFpCTbdQy8hwNckzSmWYSu0ItdWoy3U_JFTWxGKGslkXFAJqhR94Umwv6iHqAg5VwBINcv8TnCF3F5TddaBwBojPA4pFMv_n7uYNbFp7GBVrr-YR7evgafWUTPMBcRQTl1SD48XGfw6eUMivlJQET6iMx4z8BrFd5F7FaRrWttbOzVH0W7TM8eeeid6G4CV9tDCwQ2grccoUhsft7x_RGfuYw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5d6611008e.mp4?token=pGsYyEXGJt9gFNpsYzLnxReEy_VENcnyt6GcdryZJCGOlPNnZxuRRXK32lk0BMwxRIzbclosPu7Ucz4TvH8BKN6dT6OJNthdX7H2K1FWQ9hv27LS10u5f55H2xDWqqFpCTbdQy8hwNckzSmWYSu0ItdWoy3U_JFTWxGKGslkXFAJqhR94Umwv6iHqAg5VwBINcv8TnCF3F5TddaBwBojPA4pFMv_n7uYNbFp7GBVrr-YR7evgafWUTPMBcRQTl1SD48XGfw6eUMivlJQET6iMx4z8BrFd5F7FaRrWttbOzVH0W7TM8eeeid6G4CV9tDCwQ2grccoUhsft7x_RGfuYw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
نوباوه بابت ادعای «دستکاری» تبرئه نشده است
🔹
بررسی حکم دادگاه نشان می‌دهد نوباوه تبرئه نشده، بلکه بابت استفاده از واژه «جعل» به توهین محکوم شده است.
🔹
در ادامه، بازنشر این ادعا در هفته‌نامه «۹ دی» به محکومیت ۱۰ ماهه حمید رسایی منجر شده است.
🇮🇷
✊
@AkhbareFori…</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/akhbarefori/693553" target="_blank">📅 23:55 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693552">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UMaEeXlACQKFGInwZjRrVBTtorGtWoOhUKAP_VrHstPNIaTnRYkWf9e3SmP_-6ku9TMGp_jFq077YaV9StverUJ0tBPliIKFZ5VhZ92-6CKttXRwdNCSQWfDXQwGeD3ih9GeCvLNId4qB_DnszqCgq2Q-L124uNMd_kxR7nh536H0Q5VEngZp6IHLcw_16F35iIiBpuaG0tBPPpeHcpdtiF3R8FtTAPxORiUzH86oXIDNCFy9nEGuNsv3eeLbY0UhS1nxiESR7qFRzVRbSZXoYetISxs3HiREABInyvQ_KODZT6Y2HSaGQB8zhszCJJlB3MMvVt7bcVhQJY7dRqaQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ترامپ بار دیگر نام تنگه هرمز را به "تنگه ترامپ" تغییر می‌دهد و قطر و بحرین را از روی نقشه حذف می‌کند
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/akhbarefori/693552" target="_blank">📅 23:53 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693551">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f-Nrk-CLhtbsniDhISfeGzEg6bYAeRPIwfu8EMk9Zkry_iEdn5X9UPx03UvRUd8BaYTiIg2FPZBpxOS82JcQDa9i02MtaMRKjzXkM_XTFHvI3ZnjCL8hVUf8hMUhFzkW7okRlw9e2sMGUB300fk2KragMssJZwjbBPp3cIGzebT3S52xSlrWLUgNXfhb3FfaYb7zBMQkDzkqcBqaGPj8-uOVks1ixREhkNDUJACj5xFzhTNsVKL8de313ge2t_NsekwOypPg2DJQfWnL8lKywqQTDry4VauxA9-B4_JiOQm6mZwz9W3iwC-UCoC_SYMI3QCNz-JA9m-MmBIwmzSrow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ادعای بسنت: تنها ۱۵ میلیون بشکه دیگر از نفت ایران روی آب باقی‌مانده است؛ ایران دیگر چیزی نخواهد داشت که در ازای آن بتواند چیزی مبادله کند
🔹
ایرانی‌ها می‌گویند اگر توافقی حاصل شود، تنگه‌ها را باز خواهند کرد. تنگه‌ها باز هستند.
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/akhbarefori/693551" target="_blank">📅 23:50 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693550">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">♦️
وزیر خارجه عراق: خروج نیروهای آمریکایی از عراق به‌طور کامل پایان یافت
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/akhbarefori/693550" target="_blank">📅 23:48 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693548">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">♦️
قایق‌سواری در خیابان‌های سیل زده در لانگ بیچ تاون‌شیپ در نیوجرسی آمریکا
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/akhbarefori/693548" target="_blank">📅 23:23 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693547">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">♦️
ادعای بسنت: تنها ۱۵ میلیون بشکه دیگر از نفت ایران روی آب باقی‌مانده است؛ ایران دیگر چیزی نخواهد داشت که در ازای آن بتواند چیزی مبادله کند
🔹
ایرانی‌ها می‌گویند اگر توافقی حاصل شود، تنگه‌ها را باز خواهند کرد. تنگه‌ها باز هستند.
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/akhbarefori/693547" target="_blank">📅 23:20 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693546">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1a3215fd10.mp4?token=Ge6l4ta2f4d44Bsey_TYZrHN0wzt3vZPC-HVw_m8Ekz7pTIy8MifvFbYWRH4Aqq4bwaeym85VR2HoXlkxIbi1okyaDfpiP1y-xsrClEeTqUCtp6q_r1qHsWmxyGQyI2inHFQwrwGRWWdLatjgsLQE-jMgEQv-WB8-7AUoEktyEAJvlGNwi9cMQUV_WRT5glVYEW95jNVJ38m1P8OpRdb6voWcLt-M-Ox7ORIyNpKqglu8rIPkGdHrJQZ7N5uX8F0gj22B_3nqV7WYMEkbtKtklCWEq7tUN6USGUsMfntWW3UKC2u4aTuN-EPSq8BX5D16FHUIq_aC4JuLddRufjKwkBQ0VDULU2X-PKr03regzo2GeIIZ-qXIEhR7shAQuEoV0zRAKbCrz57GA0mFJq1Gx_wiVlV6-7lMQDirh0rsAewQdnUHZv5jMs0HVT8zAOVpM97AR2w-LZHBvnZi1uNBzrZph8QSvyLfNEL2r2eu4BhK6wnCu7mgdRaVTkgqNs4CDvQUUM-AAQ-QTRnaBiQqR-yMvHoJkieQOC--XRDcOZfDO0po4LsRPRqvtsyVH1ZMd3y13Tbuq52NtZfmias2pyMwY3apEbe6CGJDOK_P14zE8HyPKFIozp0uP2R2btI8kRUoSsp72AoEakTL3Kj9oLvh88n_4lJAukqbiKN058" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1a3215fd10.mp4?token=Ge6l4ta2f4d44Bsey_TYZrHN0wzt3vZPC-HVw_m8Ekz7pTIy8MifvFbYWRH4Aqq4bwaeym85VR2HoXlkxIbi1okyaDfpiP1y-xsrClEeTqUCtp6q_r1qHsWmxyGQyI2inHFQwrwGRWWdLatjgsLQE-jMgEQv-WB8-7AUoEktyEAJvlGNwi9cMQUV_WRT5glVYEW95jNVJ38m1P8OpRdb6voWcLt-M-Ox7ORIyNpKqglu8rIPkGdHrJQZ7N5uX8F0gj22B_3nqV7WYMEkbtKtklCWEq7tUN6USGUsMfntWW3UKC2u4aTuN-EPSq8BX5D16FHUIq_aC4JuLddRufjKwkBQ0VDULU2X-PKr03regzo2GeIIZ-qXIEhR7shAQuEoV0zRAKbCrz57GA0mFJq1Gx_wiVlV6-7lMQDirh0rsAewQdnUHZv5jMs0HVT8zAOVpM97AR2w-LZHBvnZi1uNBzrZph8QSvyLfNEL2r2eu4BhK6wnCu7mgdRaVTkgqNs4CDvQUUM-AAQ-QTRnaBiQqR-yMvHoJkieQOC--XRDcOZfDO0po4LsRPRqvtsyVH1ZMd3y13Tbuq52NtZfmias2pyMwY3apEbe6CGJDOK_P14zE8HyPKFIozp0uP2R2btI8kRUoSsp72AoEakTL3Kj9oLvh88n_4lJAukqbiKN058" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حسین صمصامی، نماینده مجلس: فشار سیاست‌های غلط اقتصادی بر مردم، بیشتر از تحریم‌های آمریکاست/ امروز در شرایط بن‌بست قرار نداریم
حسین صمصامی، نماینده مجلس در
#گفتگو
با خبرفوری:
🔹
اعتقادم این است سیاست‌های دی ماه، سیاست اشتباهی بود که اگر آن را اجرا نمی‌کردید بعد از جنگ، مردم این‌ همه دچار مضیقه نمی‌شدند.
🔹
نمیخواهم بگویم جنگ تاثیر تورمی ندارد، اما نکته این جاست سیاست‌های غلط شما آسیب بیشتری دارد. با اصلاح سیاست‌های اقتصادی میتوانیم جلوی تورم های فزاینده را بگیریم.
#فوکوس
@Tv_Fori</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/akhbarefori/693546" target="_blank">📅 23:19 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693545">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/10c7483d4e.mp4?token=HEfKjrSzVo0FCU9aQKFiRNOPW4TYenVswzvQqDc2N81XwYRvXJiBKIEzLEIV7T_TWBELgpkPbNlPugl4kVmClgycwecniC4r04ThRIS6C2t6WUGYN1cFWlRY-MWlwlPGCSNogLVuVqnBq1J7fkipHuXXrrUFzzEOP0WF3dO9TovR-S9KB6OYW5hn5FTk1lMDMu46imxROmE4Nxom2YYE_y2-zzXMuf_xk_NiisxoYwNbboHEIgFRemIeFpMrUonsxTkD6e_4G1RsE0eb8xFpLDj-V_jvNeWPUMGmdEgJuCz4Cg0E3REkQgk1mf1I7ybVFAfRjKPu89OkGlL9ZtbIhQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/10c7483d4e.mp4?token=HEfKjrSzVo0FCU9aQKFiRNOPW4TYenVswzvQqDc2N81XwYRvXJiBKIEzLEIV7T_TWBELgpkPbNlPugl4kVmClgycwecniC4r04ThRIS6C2t6WUGYN1cFWlRY-MWlwlPGCSNogLVuVqnBq1J7fkipHuXXrrUFzzEOP0WF3dO9TovR-S9KB6OYW5hn5FTk1lMDMu46imxROmE4Nxom2YYE_y2-zzXMuf_xk_NiisxoYwNbboHEIgFRemIeFpMrUonsxTkD6e_4G1RsE0eb8xFpLDj-V_jvNeWPUMGmdEgJuCz4Cg0E3REkQgk1mf1I7ybVFAfRjKPu89OkGlL9ZtbIhQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ویدیویی از لحظه تصادف سنگین در جاده چالوس
#اخبار_مازندران
در فضای مجازی
👇
@akhbarmazandaran</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/akhbarefori/693545" target="_blank">📅 23:13 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693544">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">♦️
منابع محلی از شلیک کروز دریایی به یک کشتی متخلف در مسیر غیرمجاز تنگۀ هرمز خبر می‌دهد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.2K · <a href="https://t.me/akhbarefori/693544" target="_blank">📅 23:09 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693543">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">♦️
خبرنگار cbs: یک مقام ایرانی به من گفته که مذاکرات روز دوشنبه میان ایران و آمریکا لغو شده است
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 32.1K · <a href="https://t.me/akhbarefori/693543" target="_blank">📅 23:06 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693542">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j1BdLAqauaGOBVAGFp6fvDGSVVBMXjtri8IzVNoLtsIDtSBk3tzbsU6KPSZ8W-e9jNgGJMv_hQAw_Eg9V617SWfDBvVAeWeTOdHwkE_nnQm08WTCJWrrlkQFCUflDmsPyln33P9b6A_WfQUXDX8ak-aprqSOo9XMKlTI9pNxlFVAZt6yqVTEPBNteCVLQ6-W9TzjcNV7OixiByP4gC_x_CswyuWc8w5RHU4uDZdeasNe6Ze5hEF57GH2DA1o8RSXYWz1tndYQALcU7Bj8DULrZwTpBNhn76fNfstza1EZb_ATbQk4Hp4XjzouXxDtJ393Q3WtzOjuXeQ9GR8BIEfEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
فعال‌رسانه‌ای آمریکایی: ایران هر کاری دلش بخواهد می‌کند؛ اصلاً ذره‌ای برایش مهم نیست ترامپ چه می‌گوید یا چه کار می‌کند
🔹
ترامپ بهتر است یک‌بار برای همیشه بزرگ شود، این غرور نحیف و شکننده‌اش را کنار بگذارد و آخرین پیشنهاد ایران را قبول کند
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/akhbarefori/693542" target="_blank">📅 23:04 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693541">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g2PHYNWZc36-ISlQ3H_o2V3_O5aohCYB4dUudP6BYX6mVtLXQBC9sZNc7HRFFEuXuXm7cYJmYjQa9ioLrQ8fyt8cYH3rVBH75ve7ZfjUuvZovLZHPvgS_tZsTGzZdze24EZe8uOT2hTgZ2BkAU4vQOogqTd6sW8I27bBAsbqFjIG93_zlCsucNeHhUhDgVHk6cyCWnMntXjUS4TGlDhQrM_vgiv-hTXuTgup8Xot4gmtOdErmRdii5XFq-GxJZv_k3Mxd0gLvjclEtmtPsxkDHxa-zfrk7rw0BxJ1ANJ3fG0V1lwb9aJJ7gkPeDWTqm-rG1CuQueK8xb3Ay4JFAVkw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
عراقچی: غنی‌سازی ۶۰ درصدی قانونی است
🔹
غنی‌سازی ۶۰ درصدی در چارچوب NPT و برنامه هسته‌ای صلح‌آمیز ایران قرار دارد.
🔹
ایران برای ادامه مذاکرات، آزادی دارایی‌های مسدودشده و پایان محاصره اقتصادی را خواستار است.
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 31.3K · <a href="https://t.me/akhbarefori/693541" target="_blank">📅 23:03 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693540">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">♦️
بررسی برنامه پروازی شهر فرودگاهی امام خمینی (ره) حاکی از آن است که امروز ۵ مهرماه ۴۰۵ شرکت‌های هواپیمایی داخلی حداقل ۲۴ پرواز خروجی و ورودی به ۱۱ مقصد خارجی انجام داد‌ه‌اند./ تسنیم
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/akhbarefori/693540" target="_blank">📅 22:57 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693539">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/921f1bf341.mp4?token=r7FAV341diCH8rbnKvOCT0ymmLTaXdOxbOM0D4VAPZ2cxwNOsIiCWw1GsHqG9EuAW_0WEASKQ_4h014WhDAZHHG8P0ZLrIoeEB415f8ywylZSMtuSgNkBsTszZ7Zl4kbFFGQ-FWzi9IQ_hZKy6zX1UlMnOk76Wngn91NHkRIg3jl6Vf32Eej1Hrt8ESWwNSFMRijprG5ujswYxlAlz37VlDkaXvNO5SnOSQ7B7b9dvnUaTUxfxfSam_APV3y9u2PYXr_L0KPBTMnRcPKGY3pEtcGZ_KjLrpHanbKeB-QbrQgyDi83_CPx8UmJQSi13ROtRfZPsE9tT7f_C_7eh_mOg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/921f1bf341.mp4?token=r7FAV341diCH8rbnKvOCT0ymmLTaXdOxbOM0D4VAPZ2cxwNOsIiCWw1GsHqG9EuAW_0WEASKQ_4h014WhDAZHHG8P0ZLrIoeEB415f8ywylZSMtuSgNkBsTszZ7Zl4kbFFGQ-FWzi9IQ_hZKy6zX1UlMnOk76Wngn91NHkRIg3jl6Vf32Eej1Hrt8ESWwNSFMRijprG5ujswYxlAlz37VlDkaXvNO5SnOSQ7B7b9dvnUaTUxfxfSam_APV3y9u2PYXr_L0KPBTMnRcPKGY3pEtcGZ_KjLrpHanbKeB-QbrQgyDi83_CPx8UmJQSi13ROtRfZPsE9tT7f_C_7eh_mOg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
آیا می‌توان از ابتلا به آب مروارید چشم پیشگیری کرد؟
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.1K · <a href="https://t.me/akhbarefori/693539" target="_blank">📅 22:56 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693538">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">♦️
آخرین وضعیت زائران عتبات پس از توقف پروازهای بغداد و نجف
🔹
پس از توقف پروازهای بغداد و نجف، معاون عتبات سازمان حج و زیارت از انتقال زمینی زائران و عودت مابه‌التفاوت هزینه خبر داد. به گفته او مرزهای زمینی باز هستند و پیگیر بازگشایی فرودگاه نجف هستیم./ ایسنا…</div>
<div class="tg-footer">👁️ 32.8K · <a href="https://t.me/akhbarefori/693538" target="_blank">📅 22:50 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693537">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">♦️
رسانه‌های عبری: نتانیاهو امروز برای دیدار با محمد بن زاید به امارات سفر می‌کند
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.5K · <a href="https://t.me/akhbarefori/693537" target="_blank">📅 22:45 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693536">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5e6a91c17b.mp4?token=CpRU6vGe6h5KIsUDJntI9asqw-MvyjjTHTqYkVLTcGzCkJ26uhLDdTjsk7k5X1ZSDSVzhmR6J5l3kLwEuTbLZw7pmw_s__G7PfK-C2IKHpoxSzzFdSOh9zdMcII4d6ZptVb0fSGXkpPAr5uskfZFBWqfR6tna-0ShUftSmH8JZ6-nsSo9f7qeyHn0JEQyL2nsQCf1hW20EG3AZyOD5mcnNL-jW19rj6e-Vg0TYIwnF_b69_Y8nhpZh6SpEJ1dIzbr927GbQkGcbrh-6hznTu9v6x6U-bAIZ1-t6dgIJ1GDIfoSPJ_0ZV8E_J_t3x9YlHQz5Y3XEH4KS2KKKr6Bpe3g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5e6a91c17b.mp4?token=CpRU6vGe6h5KIsUDJntI9asqw-MvyjjTHTqYkVLTcGzCkJ26uhLDdTjsk7k5X1ZSDSVzhmR6J5l3kLwEuTbLZw7pmw_s__G7PfK-C2IKHpoxSzzFdSOh9zdMcII4d6ZptVb0fSGXkpPAr5uskfZFBWqfR6tna-0ShUftSmH8JZ6-nsSo9f7qeyHn0JEQyL2nsQCf1hW20EG3AZyOD5mcnNL-jW19rj6e-Vg0TYIwnF_b69_Y8nhpZh6SpEJ1dIzbr927GbQkGcbrh-6hznTu9v6x6U-bAIZ1-t6dgIJ1GDIfoSPJ_0ZV8E_J_t3x9YlHQz5Y3XEH4KS2KKKr6Bpe3g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ماجرای خرید ۴.۵ میلیارد دلاری بانک مرکزی چیست؟
🔹
دارابی، دستیار ارزی رئیس کل بانک مرکزی: بعد از
اصلاحات ارزی دی ماه ۱۴۰۴،
کاملاً طبیعی بود که کشور با مازاد عرضه ارز روبه‌رو شود.
🔹
بانک مرکزی با پیش‌بینی احتمال وقوع جنگ و محاصره اقتصادی، از این فرصت بهره برد و
حجم ذخایر ارزی خود را تقویت نمود.
🔹
این اقدام به‌موقع سبب شد تا در شرایط حساس جنگی،
مسیر تأمین کالا بی‌وقفه و مستمر در جریان باشد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.4K · <a href="https://t.me/akhbarefori/693536" target="_blank">📅 22:42 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693535">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/349fc46bcb.mp4?token=AO0xLuiSHQiMY0ilbt9_tC2IyQosqlbH-EOevJH7UvHKgH8eMfVzFPm45YCCl0MS_-kA2wDsk11RjrZI4Q8yxCVWkwmiKAGQufxkEMB3gSXoLl6UKtYMfK7hfzo_u_PsfBRFbYyizc6hnZGE4LGcJpuO9o9oEBplSHtR4f4O3_DuBxPIh5pOoUeu1WvofWltDVfJ9zCd8s-6L5gDS8U33eM3bsx2X36-eLt743oB0oQnetfZq1FK9TvXr3pCAeewD4ApSWNgilmTw09B3p49XnjDRWvcWRJhb7U2I7GAsT1THYCDV8NnIFk0i-nvrJ8Osgb7nGnFYjpuC07tumRsqg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/349fc46bcb.mp4?token=AO0xLuiSHQiMY0ilbt9_tC2IyQosqlbH-EOevJH7UvHKgH8eMfVzFPm45YCCl0MS_-kA2wDsk11RjrZI4Q8yxCVWkwmiKAGQufxkEMB3gSXoLl6UKtYMfK7hfzo_u_PsfBRFbYyizc6hnZGE4LGcJpuO9o9oEBplSHtR4f4O3_DuBxPIh5pOoUeu1WvofWltDVfJ9zCd8s-6L5gDS8U33eM3bsx2X36-eLt743oB0oQnetfZq1FK9TvXr3pCAeewD4ApSWNgilmTw09B3p49XnjDRWvcWRJhb7U2I7GAsT1THYCDV8NnIFk0i-nvrJ8Osgb7nGnFYjpuC07tumRsqg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
جزئیات شکار دومین زهپاد آمریکایی
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 32.1K · <a href="https://t.me/akhbarefori/693535" target="_blank">📅 22:39 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693534">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ce8af71c1f.mp4?token=oIs6Jn8rxstR-jwIx6xexzX_Wi3cQ657F89_lJnRVOvMs2pCBBRSzoYxdh01SucrOS5is393AGE6hro-YmLsIwlRqTRIDicwLziwYwp67FRRYCTQOKRD_Iye1tOUHYY4JkxDngUHGv1t2Cu7krd3p2CdlRJWmu2skJkJ19TUWwPWpzkleaqVo1grI88SR1Qfp0iltZ1uDl4HEUv5rHms1TAIpXVwiA3AWj3HCzv2YXgPSmkKbfarDPWp6zuDphvNwgV6VBt9xqVWltaNUJ9mnT5zYcXSijhgJfASBRXb9J2NruIoBSUO24xh0a5G1zWJ9kvVo8xg1hLSa_5eBoA2TA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ce8af71c1f.mp4?token=oIs6Jn8rxstR-jwIx6xexzX_Wi3cQ657F89_lJnRVOvMs2pCBBRSzoYxdh01SucrOS5is393AGE6hro-YmLsIwlRqTRIDicwLziwYwp67FRRYCTQOKRD_Iye1tOUHYY4JkxDngUHGv1t2Cu7krd3p2CdlRJWmu2skJkJ19TUWwPWpzkleaqVo1grI88SR1Qfp0iltZ1uDl4HEUv5rHms1TAIpXVwiA3AWj3HCzv2YXgPSmkKbfarDPWp6zuDphvNwgV6VBt9xqVWltaNUJ9mnT5zYcXSijhgJfASBRXb9J2NruIoBSUO24xh0a5G1zWJ9kvVo8xg1hLSa_5eBoA2TA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ویدیوی وایرال شده از حلزون‌تراپی برای شفافیت پوست
🐌
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.4K · <a href="https://t.me/akhbarefori/693534" target="_blank">📅 22:35 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693533">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2187d0c12c.mp4?token=ed-lL7Qb9FN7q54ynr-TgUjG4ioabdDsd2uuEYgEGQ2KOIYFzU4C6i8TXFALkOfcTJq6ze0-zQnSdGSHoasz0kjK-gMOEmgAiTvH4N0jJeRhV--98VueS6aiqYnJKyM6XXbGYssCOZlfRD_RTWZZNgv5Vft8dy_YZs7YfgyxLnuFHvH9tbJlDY7v4bWOtIxDrKrLrsYR3wNjI5EXH4yfUyYA75SnEiIJkXLB_LzVxS0GgiG0yL2-1txe0wxHidmGi42bAMgV2PLOk7HWTHvkeFJ9PkVBfnWwQNe5uEj9R8nmL__ICV2fzv2hFmkPU9fPhP7m3GTRURu_K2A92fpkjhcLnEB7GIoNB25GVWDz8WDE1CBaASloeN5pMyII2fegHgGYWgNwSCr22TzvlcNSQGnwmMR10Z3NT5rxpQYPvOM9pHHTsT7j_DgNPxNH9Vvhn7ddd1UY26Ocz35UAXLIRTbOIzOc6_iNRBwXnYIwCIVE78FmuYlO4fcbG90qzNcMCYEEOsYnSggQeiOohsyOsXurpWy2D1xV1Icp6fKpHte-rPCPblDbl9zmtDTI6n8Ybl2X3ha6L1n5OHfEGV77U9ms2xjRXfdQ1jyu1pr_KSPwhuR_D4u-8HtEZ4ogslmg7Q9_ATL2apAtLCWFpMI8h_m2C9EFqvscXnEt7XCTVPk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2187d0c12c.mp4?token=ed-lL7Qb9FN7q54ynr-TgUjG4ioabdDsd2uuEYgEGQ2KOIYFzU4C6i8TXFALkOfcTJq6ze0-zQnSdGSHoasz0kjK-gMOEmgAiTvH4N0jJeRhV--98VueS6aiqYnJKyM6XXbGYssCOZlfRD_RTWZZNgv5Vft8dy_YZs7YfgyxLnuFHvH9tbJlDY7v4bWOtIxDrKrLrsYR3wNjI5EXH4yfUyYA75SnEiIJkXLB_LzVxS0GgiG0yL2-1txe0wxHidmGi42bAMgV2PLOk7HWTHvkeFJ9PkVBfnWwQNe5uEj9R8nmL__ICV2fzv2hFmkPU9fPhP7m3GTRURu_K2A92fpkjhcLnEB7GIoNB25GVWDz8WDE1CBaASloeN5pMyII2fegHgGYWgNwSCr22TzvlcNSQGnwmMR10Z3NT5rxpQYPvOM9pHHTsT7j_DgNPxNH9Vvhn7ddd1UY26Ocz35UAXLIRTbOIzOc6_iNRBwXnYIwCIVE78FmuYlO4fcbG90qzNcMCYEEOsYnSggQeiOohsyOsXurpWy2D1xV1Icp6fKpHte-rPCPblDbl9zmtDTI6n8Ybl2X3ha6L1n5OHfEGV77U9ms2xjRXfdQ1jyu1pr_KSPwhuR_D4u-8HtEZ4ogslmg7Q9_ATL2apAtLCWFpMI8h_m2C9EFqvscXnEt7XCTVPk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ادعای نماینده مجلس درباره خرید ارز و طلا توسط شرکت‌های دولتی
حسین صمصامی، نماینده مجلس در
#گفتگو
با خبرفوری:
🔹
یکی از دلایل از بین رفتن ارزش پولی به خاطر رفتارهای مردم است که رفتارهای مردم نیز تحت تأثیر سیاست‌های اقتصادی دولت است.
🔹
در حال حاضر میدانید چه میزان ارز و طلا توسط خود شرکت‌های دولتی خریداری می‌شود؟ وقتی مردم می‌بینند که دولت هر روز ارز را تضعیف و تورم را تحمیل می‌کند، چنین رفتاری بروز می‌دهند. اصلاح سیاست‌های اقتصادی باید توسط دولت انجام شود نه مردم.
#فوکوس
@Tv_Fori</div>
<div class="tg-footer">👁️ 33.4K · <a href="https://t.me/akhbarefori/693533" target="_blank">📅 22:33 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693531">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">♦️
آخرین وضعیت زائران عتبات پس از توقف پروازهای بغداد و نجف
🔹
پس از توقف پروازهای بغداد و نجف، معاون عتبات سازمان حج و زیارت از انتقال زمینی زائران و عودت مابه‌التفاوت هزینه خبر داد. به گفته او مرزهای زمینی باز هستند و پیگیر بازگشایی فرودگاه نجف هستیم./ ایسنا…</div>
<div class="tg-footer">👁️ 34K · <a href="https://t.me/akhbarefori/693531" target="_blank">📅 22:28 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693530">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">♦️
تصاویر منتشرنشده از لحظه شهادت سید حسن نصرالله در ضاحیه لبنان
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35.1K · <a href="https://t.me/akhbarefori/693530" target="_blank">📅 22:26 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693529">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/635f76368c.mp4?token=HM5kTFDTlFg-uuKQfmXn2b1vfZTq-LIdTN-ZaecYIwVlmTZdYC0h7ZDfyvfwVfXrfz4gUXCMKEPpRHOgav4hCpP_o3Iio2VtIyhbxxMiVn3y6z0GTo1cfmA9gVhWAunY6IKO5-OWgKds2GZjDJ76UYdA8BNaKj7X9xvmGT98Hoix1igZpzyHsx5I4AeieEIlbXuDP7d0hFPpskR3BSNtYGGQDnVzy59iY1NNt7yPaOXqrPaQ0F-XjLIj7jhXhPWgPCPIT2k4ftvmTHlJbYMjcNFlxZ1Op-VpLe-RmdY2s8hEL5kRiis2jEPo5ck3V2UqHIlwHcD8C1HCI0Mu3DGkRQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/635f76368c.mp4?token=HM5kTFDTlFg-uuKQfmXn2b1vfZTq-LIdTN-ZaecYIwVlmTZdYC0h7ZDfyvfwVfXrfz4gUXCMKEPpRHOgav4hCpP_o3Iio2VtIyhbxxMiVn3y6z0GTo1cfmA9gVhWAunY6IKO5-OWgKds2GZjDJ76UYdA8BNaKj7X9xvmGT98Hoix1igZpzyHsx5I4AeieEIlbXuDP7d0hFPpskR3BSNtYGGQDnVzy59iY1NNt7yPaOXqrPaQ0F-XjLIj7jhXhPWgPCPIT2k4ftvmTHlJbYMjcNFlxZ1Op-VpLe-RmdY2s8hEL5kRiis2jEPo5ck3V2UqHIlwHcD8C1HCI0Mu3DGkRQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
فراخوان جنبش نجباء برای تحصن در مقابل فرودگاه نجف
🔹
در ادامه واکنش‌های منفی به تصمیم دولت عراق در توقف پروازها با ایران، رئیس شورای اجرایی جنبش نجباء خواهان برگزاری تحصن گسترده در مقابل فرودگاه بین‌المللی نجف اشرف شد.
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 34.4K · <a href="https://t.me/akhbarefori/693529" target="_blank">📅 22:25 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693528">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GzdC4vJs0wYg1IrFW4x02j3XAok3nYufkJ8TEnznxDbo-KnhEgrY8KMZwQVrBvXqGFlr79HwEC3YSvjueBna3Js4kdpftrWCJFj0rR3F4n70DsDQg3VtjatPwrPp4njZIPTfhzoO9L5YE2HpfBd1hQ-4yPJnsKQgElIyfv1Sws-rpvCDCZosy99WFO2WdZ8Lxrz4vupc9vQKE7-zPmcKJij2pmblnwb5Od7Dk1txRy55ckuaTN2CpJhN7xa3tOrFzG2tK-GuIPhlNShBQpVE5CJOV7fJRHc1NvsLreEEUWbrpJatAVxzbYOk0zvO32juypi9XKTziwV2Bv-XXtI8Aw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
آیا می‌دانستید نوعی موز به نام «موز آبی» وجود دارد که پوست آن به رنگ آبی روشن است و طعمی شبیه وانیل دارد؟
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.6K · <a href="https://t.me/akhbarefori/693528" target="_blank">📅 22:19 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693527">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromآمارفکت</strong></div>
<div class="tg-poll">
<h4>📊 مهم‌ترین مانع شما برای داشتن یک کسب‌وکار خانگی چیست؟</h4>
<ul>
<li>✓ نداشتن ایده</li>
<li>✓ کمبود سرمایه</li>
<li>✓ کمبود مهارت</li>
<li>✓ جذب مشتری و فروش</li>
<li>✓ مشکلات اداری</li>
<li>✓ کمبود وقت</li>
<li>✓ نیازی به این کار نمی‌بینم</li>
<li>✓ کسب‌وکار خانگی دارم</li>
</ul>
</div>
<div class="tg-footer">👁️ 33.3K · <a href="https://t.me/akhbarefori/693527" target="_blank">📅 22:17 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693526">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">♦️
معاون اقتصادی وزارت تعاون: کالابرگ مرداد و شهریور کسانی که نیازمند احراز محل سکونت بودند فردا واریز می‌شود
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.8K · <a href="https://t.me/akhbarefori/693526" target="_blank">📅 22:11 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693525">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b216d7d76b.mp4?token=RlMCKm-N8haXGImezNszpkrjOem8LsajOBEgjyvRRqBTaU5p7E32uFU6DYwqZA17xZYhoWLqT8lNiheVpK2GDKHp2Opso9I-q1P-78NO6nhxSeHQhQEWvMRSh74uEWNRzhqM8Mq9Mz3TLCvAF5li8KEwyaeBxaE7UCv2eBQhtOiDpBlKqiyYsQxdBYkKIrQh789bdyLCwuViN-SNe-aQaE_SEiWk-89I6UxnZJQ3j21OIFFO1jKJUM0cjYJvRnCG4uymtD9LSJUEGBSoP5R_2cbP5QIs7z2qE5YdUTZp44XxihTGxd4adpKuuhqoIfHfcxBiiAXX2fDSM6RX7LGvzA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b216d7d76b.mp4?token=RlMCKm-N8haXGImezNszpkrjOem8LsajOBEgjyvRRqBTaU5p7E32uFU6DYwqZA17xZYhoWLqT8lNiheVpK2GDKHp2Opso9I-q1P-78NO6nhxSeHQhQEWvMRSh74uEWNRzhqM8Mq9Mz3TLCvAF5li8KEwyaeBxaE7UCv2eBQhtOiDpBlKqiyYsQxdBYkKIrQh789bdyLCwuViN-SNe-aQaE_SEiWk-89I6UxnZJQ3j21OIFFO1jKJUM0cjYJvRnCG4uymtD9LSJUEGBSoP5R_2cbP5QIs7z2qE5YdUTZp44XxihTGxd4adpKuuhqoIfHfcxBiiAXX2fDSM6RX7LGvzA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
بیل گیتس: هوش مصنوعی به طرز دیوانه‌واری از انسان باهوش‌تر خواهد شد
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 37.8K · <a href="https://t.me/akhbarefori/693525" target="_blank">📅 21:55 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693523">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7e5686e768.mp4?token=sw0007YW4_SQQBd04TIyL0GVdxASruevYdgRU-90mE_hzQNQSJSe7URNtL9URxO1pR6k07aBaMP4-guMKgNMNHiMtB143c5XfbHtr0D267tKR2b1BKvyGNvJEMNh7QDl2dtExh3oBQbcUcpMvx5E1qW1qa0wZDBGK0wekQUcLZTvKh5DM7PB5OekdLQq3P2Lq11eGu0IQlDPh0PodNeVspBTVMJM4FzrhgLitiTe66Cz6guMVueUIizoFopq-5nJk8Y_CQCc471Xdt6_825M6MO2Md5ous-E0LiLWTT-0huGYkfrKSb8BNbdNNuCUJYb896TUF7WlRXXSW3VAzrWog" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7e5686e768.mp4?token=sw0007YW4_SQQBd04TIyL0GVdxASruevYdgRU-90mE_hzQNQSJSe7URNtL9URxO1pR6k07aBaMP4-guMKgNMNHiMtB143c5XfbHtr0D267tKR2b1BKvyGNvJEMNh7QDl2dtExh3oBQbcUcpMvx5E1qW1qa0wZDBGK0wekQUcLZTvKh5DM7PB5OekdLQq3P2Lq11eGu0IQlDPh0PodNeVspBTVMJM4FzrhgLitiTe66Cz6guMVueUIizoFopq-5nJk8Y_CQCc471Xdt6_825M6MO2Md5ous-E0LiLWTT-0huGYkfrKSb8BNbdNNuCUJYb896TUF7WlRXXSW3VAzrWog" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ویدئوهای وایرال شده از پارک پردیسان
#اخبار_تهران
در فضای مجازی
👇
@akhbartehran</div>
<div class="tg-footer">👁️ 37.5K · <a href="https://t.me/akhbarefori/693523" target="_blank">📅 21:50 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693522">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">♦️
انتشار تصاویر دیده‌ نشده‌ای از شهید نصرالله در جبهه‌های نبرد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36.9K · <a href="https://t.me/akhbarefori/693522" target="_blank">📅 21:46 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693521">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7ede84d092.mp4?token=BPID5mv4mgti896924b9JyETkqQzlayBoygPYQxJgn9czRHPZ6qwf5rwfYkGzmAe0rplEJFLpctse7FO9NgJZR9CC2ILRphqTcpm_7rPWGNM4nh9RDVeT33s0rkimZ5Fpn7j4_trdGoTbeltLNcDskAzp7zxni-KJqzNoMuQ3AB9ggtwBVOUMMIafs5vsXS8GzhqPuO4Jx8-nEKjH_LmgHdv3TLX3Lwol8iYGmoB8W6VE_HY2iyYoMreHcVNY_dwx37LoGLIUx_GzoaKrS12DoYjcWMykirN_89d5rBaEThn9rk-3lYtaUMjeffM96Uen8KQd1Dtm1Q3GqgsOu3fvj-n-LsLC6O04y7yDj8aVHymnCwI7zs5Fnxzzs_Z_cQLUSuMAHo58VVNFQXEYSMqhOeta05oT-JcpMemwleovRElZr_0EWSB_cpEOVEpu-3R5EFZeOE9RYgOhgIebjflT7BnrZ8WFJ_gBVxhUMfmdQanhnmy3MY-pfOGCTqdqQ6tGD1gsJ6Ng-TdOzTiYfRBOGQO-4AFD_-7gKROhPJFfW394DttyZAJXE3mj4LV5eNIr91YiMCE9mmU0gLdjySO_dVDI8H5Ujn_wZ_oyCrJhNIXj2C9jwyqra_WYOOh1OGsz3Q84nzUQaK3-iB1IpCSd5i4uMgiR5LCMY5E4d6r-l8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7ede84d092.mp4?token=BPID5mv4mgti896924b9JyETkqQzlayBoygPYQxJgn9czRHPZ6qwf5rwfYkGzmAe0rplEJFLpctse7FO9NgJZR9CC2ILRphqTcpm_7rPWGNM4nh9RDVeT33s0rkimZ5Fpn7j4_trdGoTbeltLNcDskAzp7zxni-KJqzNoMuQ3AB9ggtwBVOUMMIafs5vsXS8GzhqPuO4Jx8-nEKjH_LmgHdv3TLX3Lwol8iYGmoB8W6VE_HY2iyYoMreHcVNY_dwx37LoGLIUx_GzoaKrS12DoYjcWMykirN_89d5rBaEThn9rk-3lYtaUMjeffM96Uen8KQd1Dtm1Q3GqgsOu3fvj-n-LsLC6O04y7yDj8aVHymnCwI7zs5Fnxzzs_Z_cQLUSuMAHo58VVNFQXEYSMqhOeta05oT-JcpMemwleovRElZr_0EWSB_cpEOVEpu-3R5EFZeOE9RYgOhgIebjflT7BnrZ8WFJ_gBVxhUMfmdQanhnmy3MY-pfOGCTqdqQ6tGD1gsJ6Ng-TdOzTiYfRBOGQO-4AFD_-7gKROhPJFfW394DttyZAJXE3mj4LV5eNIr91YiMCE9mmU0gLdjySO_dVDI8H5Ujn_wZ_oyCrJhNIXj2C9jwyqra_WYOOh1OGsz3Q84nzUQaK3-iB1IpCSd5i4uMgiR5LCMY5E4d6r-l8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حسین صمصامی، نماینده مجلس: حتی کالابرگ ۱۰ میلیونی هم گرانی‌ها را جبران نمی‌کند/ سیاست پرداخت پول نقد از اساس اشتباه است
حسین صمصامی، نماینده مجلس در گفتگو با
#خبر_فوری
:
🔹
این موضوع منابعی را می‌طلبد که وقتی بخواهیم آن را تامین کنیم، آثار تورمی آن بیشتر از پولی است که بخواهیم به مردم بدهیم؛ این را در سال‌های ۱۳۸۸،۱۳۸۹،۱۴۰۱ و ۱۴۰۴ امتحان کردیم.
🔹
آدم عاقل از یک سوراخ دوبار گزیده نمیشود، اما ده بار گزیده شدیم و باز هم انگشتمان را در همان سوراخ میکنیم.
#فوکوس
@Tv_Fori</div>
<div class="tg-footer">👁️ 37.7K · <a href="https://t.me/akhbarefori/693521" target="_blank">📅 21:44 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693520">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cfcf3a3452.mp4?token=Ye2aJmvSAHxaVrZhKK-Boqvh_PBEL4MV7ZD3GAKdlPVAGc3MN1QsUHK_U1e_22ShjsCZOCOjBH9hisI1iYidm85miUNRaRjbdX3n2hErGKXAGU6r72_EE6HVkqcrkHYoJ_D7_XYqrMYvzdeDGP62YqiuQtmz4rvjQNzEPicA0g9XT2MeoARponuy1ZZsNan3ri33vn6cscmBk3o4Vufzr2eqXZiifWeF49Th3Tzel9qDd3gI0oPs15Z3bYGKVetwPZGZKxcDYjh6qYB_afYYSP1t-LGaq9JjHtVaFWNiVRG33KCSnDRhnKVWlRAN1FtbPWPR4Fn1w1fju-di98pn1Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cfcf3a3452.mp4?token=Ye2aJmvSAHxaVrZhKK-Boqvh_PBEL4MV7ZD3GAKdlPVAGc3MN1QsUHK_U1e_22ShjsCZOCOjBH9hisI1iYidm85miUNRaRjbdX3n2hErGKXAGU6r72_EE6HVkqcrkHYoJ_D7_XYqrMYvzdeDGP62YqiuQtmz4rvjQNzEPicA0g9XT2MeoARponuy1ZZsNan3ri33vn6cscmBk3o4Vufzr2eqXZiifWeF49Th3Tzel9qDd3gI0oPs15Z3bYGKVetwPZGZKxcDYjh6qYB_afYYSP1t-LGaq9JjHtVaFWNiVRG33KCSnDRhnKVWlRAN1FtbPWPR4Fn1w1fju-di98pn1Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تصویری زیبا از ماه کامل امشب  #اخبار_تهران در فضای مجازی
👇
@akhbartehran</div>
<div class="tg-footer">👁️ 36.9K · <a href="https://t.me/akhbarefori/693520" target="_blank">📅 21:41 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693519">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">♦️
آناتولی: توافق ۵ رهبر مخالف نتانیاهو برای هماهنگی کارزار انتخاباتی با هدف کنار زدن دولت او
🔹
رهبران این «بلوک تغییر» در خانه یائیر لاپید، رهبر مخالفان، در تل‌آویو دیدار کردند
🔹
این پنج رهبر متعهد شدند بلافاصله پس از انتخابات و پیروزی برای تشکیل دولت آینده با یکدیگر همکاری کنند
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 38.3K · <a href="https://t.me/akhbarefori/693519" target="_blank">📅 21:29 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693518">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">♦️
روایت تلخ همسر شهید باصر بهرام نژاد (محافظ رهبر شهید انقلاب) از زیارت پیکر مطهر شهید آیت‌الله خامنه‌ای
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 39.2K · <a href="https://t.me/akhbarefori/693518" target="_blank">📅 21:26 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693517">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">♦️
پزشکیان: استخاره روز بازگشایی مدارس خیلی خوب آمد   واکنش رئیس‌جمهور به حواشی پیرامون استخاره روز بازگشایی مدارس:
🔹
هنگامی که قرآن را باز کردم آیه «وَأَطِيعُوا اللَّهَ وَرَسُولَهُ وَلَا تَنَازَعُوا فَتَفْشَلُوا وَتَذْهَبَ رِيحُكُمْ  وَاصْبِرُوا  إِنَّ اللَّهَ…</div>
<div class="tg-footer">👁️ 39.6K · <a href="https://t.me/akhbarefori/693517" target="_blank">📅 21:16 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693516">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">♦️
تنگۀ هرمز نفتکش‌های کهنه را گران‌تر از نو کرد
فایننشال‌تایمز:
🔹
اختلال در تردد نفتکش‌ها از تنگۀ هرمز، کرایۀ حمل نفت را به روزانه ۱.۲ میلیون دلار رسانده و قیمت نفتکش‌های دست‌دوم را از نو بیشتر کرده است.
🔹
نفتکش‌های قدیمی هفته گذشته بیش از ۱۵۰ میلیون دلار معامله شدند؛ درحالی‌که قیمت نفتکش نو حدود ۱۳۵ میلیون دلار است.
🔹
دلیل: زمان‌بر بودن ساخت کشتی جدید و تمایل مالکان به نگه‌داشتن نفتکش‌ها برای کسب کرایۀ بیشتر.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 41K · <a href="https://t.me/akhbarefori/693516" target="_blank">📅 21:14 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693515">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f17b5f0f74.mp4?token=SDShwsLMd4cofVZwVlx8tsDHt-ly-V3mZxbw8ITVHXzSusFEGIXjyANHFW_6IMX8_VVx1A97Px7gYX8DvbxsRsJr8Trxiy7GIh0pPBL2WDv_bAC5eoueIp0LtCoTKA-dV5zvEmTi6va3IFI-Sk4FilOxI0-PnN_Wn-uHSc4E6buyaW2SRFQFcVLgRNi5oYHtc6VJE43b56PjPeRCQ_209YLd10i1sZ_GT3wP9yhTSGYW2dEWqmAVHv5lPUHN2MPL6wubkN1mjXRYSmNbkPv9IEXrrp7UR4x1VEvzrnDyo6mdV8BpfFTzvjdYA92GofnjWciInDGW5M2tx4LuiP4yrQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f17b5f0f74.mp4?token=SDShwsLMd4cofVZwVlx8tsDHt-ly-V3mZxbw8ITVHXzSusFEGIXjyANHFW_6IMX8_VVx1A97Px7gYX8DvbxsRsJr8Trxiy7GIh0pPBL2WDv_bAC5eoueIp0LtCoTKA-dV5zvEmTi6va3IFI-Sk4FilOxI0-PnN_Wn-uHSc4E6buyaW2SRFQFcVLgRNi5oYHtc6VJE43b56PjPeRCQ_209YLd10i1sZ_GT3wP9yhTSGYW2dEWqmAVHv5lPUHN2MPL6wubkN1mjXRYSmNbkPv9IEXrrp7UR4x1VEvzrnDyo6mdV8BpfFTzvjdYA92GofnjWciInDGW5M2tx4LuiP4yrQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
وقتی سوسک تصمیم می‌گیره تبدیل به یک بدلکار هالیوودی بشه!
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 39.2K · <a href="https://t.me/akhbarefori/693515" target="_blank">📅 21:13 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693514">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">♦️
حادثه امنیتی در نزدیکی پایگاه هوایی آمریکا در انگلیس
🔹
پلیس انگلیس از وقوع یک «حادثه بزرگ» در نزدیکی پایگاه هوایی آمریکا در فیرفورد و بازداشت چند نفر به ظن نقض قوانین مواد منفجره خبر داد.
🔹
ساکنان مناطق اطراف نیز به‌دلیل این حادثه تخلیه و به یک مرکز تفریحی…</div>
<div class="tg-footer">👁️ 37.6K · <a href="https://t.me/akhbarefori/693514" target="_blank">📅 21:10 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693512">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/569e289c22.mp4?token=JXaZC5JUAuSOAJTYOd3ed1hFXSyLZs1n_Haf3COnzLmN50GTFq2tsteyniFcnHIdINrwu2hxgUHYgUuxO7MWW8xjzy53e_m4DiE7uhluSeewnvlXeRY4wWe-eRBjZaMzlo0eRhfTZDhp2s56MrfE6Jllg2PHr-IRv015GQMp0okLNNSbqVf3QRdUsmhJnHTcDngeuLq0fQDOPYTgn5rt5IT9tZUWf1pabHrbWgq5VnDnJekhUc0OLKfAy7YPuhUJfJdm8XVYA0nSZWFjdTNq6hzC_ztLmZDWa_juNqhm4MzC_o13V7-UrKhQ7gSQkYN5cIQHuMFx2nN5HXCrRP8EM4WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/569e289c22.mp4?token=JXaZC5JUAuSOAJTYOd3ed1hFXSyLZs1n_Haf3COnzLmN50GTFq2tsteyniFcnHIdINrwu2hxgUHYgUuxO7MWW8xjzy53e_m4DiE7uhluSeewnvlXeRY4wWe-eRBjZaMzlo0eRhfTZDhp2s56MrfE6Jllg2PHr-IRv015GQMp0okLNNSbqVf3QRdUsmhJnHTcDngeuLq0fQDOPYTgn5rt5IT9tZUWf1pabHrbWgq5VnDnJekhUc0OLKfAy7YPuhUJfJdm8XVYA0nSZWFjdTNq6hzC_ztLmZDWa_juNqhm4MzC_o13V7-UrKhQ7gSQkYN5cIQHuMFx2nN5HXCrRP8EM4WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حسین صمصامی، نماینده مجلس درباره ادعای «جاسوسی روحانی»: اسناد و مدارکی که این ادعا را ثابت کند، ندیده‌ام / عملکرد اقتصادی او را درست نمی‌دانم
حسین صمصامی، نماینده مجلس در
#گفتگو
با خبرفوری:
🔹
سیاست‌های جهانگیری چندان درست نبود به جز اطلاعیه شماره یک که در فروردین ماه ۱۳۹۷ در بحث ارز داشتند که اگر پشت اجرای آن سیاست گرفته می‌شد الان شاهد این بلبشو نبودیم.
🔹
عملکرد اقتصادی حسن روحانی درست نبوده اگر چه اعترافات خوبی کرد.
به طور مثال در بحث سیاست ارزی گفتند که اقتصاد دانان به ما گفته‌اند که اگر ارز را ۳هزار تومان کنیم چه اتفاقات بزرگی رخ خواهد داد.
#فوکوس
@Tv_Fori</div>
<div class="tg-footer">👁️ 37.9K · <a href="https://t.me/akhbarefori/693512" target="_blank">📅 21:07 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693510">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c7f8d7b440.mp4?token=RUXmLhrKXfW_FNXvFwJI_VCSLqZhFKy36eH02I5-lSd8QSRrAVbB5DGs5DqhQkFeoYqA7HZP6mzS4fwysGWAkzDqCiFuC2Bfnc5p4EdLhZvHAq0evkk2EA12kE5RaxsZDaLWEcXbCtbvNDyohL9dDAEwunTcQOWwgdMQNZLOlxxbcn2_MH5BOoKySQpJJZKNn0NtAd64qi2Hn-YXk2QV2PQuiAN2c-wu7sYh0SKe7QV2gBK8os8yyb-aPid7AHYBNBKPRBpqrJzAhOjWVZeRusYxliIUmig7s5v0DQnYfBe8Ewqi3R-lq7uhMF5ETPdLC1sIQhgLNa8fVp06T2qSWg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c7f8d7b440.mp4?token=RUXmLhrKXfW_FNXvFwJI_VCSLqZhFKy36eH02I5-lSd8QSRrAVbB5DGs5DqhQkFeoYqA7HZP6mzS4fwysGWAkzDqCiFuC2Bfnc5p4EdLhZvHAq0evkk2EA12kE5RaxsZDaLWEcXbCtbvNDyohL9dDAEwunTcQOWwgdMQNZLOlxxbcn2_MH5BOoKySQpJJZKNn0NtAd64qi2Hn-YXk2QV2PQuiAN2c-wu7sYh0SKe7QV2gBK8os8yyb-aPid7AHYBNBKPRBpqrJzAhOjWVZeRusYxliIUmig7s5v0DQnYfBe8Ewqi3R-lq7uhMF5ETPdLC1sIQhgLNa8fVp06T2qSWg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تصاویر ماهواره‌ای از آتش‌سوزی در انبار نفت آرامکو
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35K · <a href="https://t.me/akhbarefori/693510" target="_blank">📅 21:06 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693509">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YTrb_-2z0Is4_6yXPgVCurjJamstYCjh8CMUPEVg29nGTaQN3ujUZR5GHrBdNZbc5-2MrEdKsE3SjK2NUMb06plh_bRxTG1XHgayhLINH2TbU0VDFLFKYRFw4c9Agoi1ZPtxx3n5hLrlWppxMBLcZgURSkYZ8IBX6L2F5gi5zFX2QMMN75ye6JBewKi81921J2w3f2Rcj2ycuQUC7RaaJYBr5La5y74E-xi9OhxO87d9xiR6x9Lhx_Pf1zvLIxrHeQD_m-qSAmNdVQg4Y7btePUAwrHoHFN6VcrEzV_6LqY3FELmh4dO4JAV-cNIkixoGooc77jONd6bA59asVL_mg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بادی کلن سورملینا ترکیبی از بادی اسپلش و ادکلن
😍
تازه خیلی هم به صرفه و اقتصادیه
چون هر پک دو عدد اسپری 250 میلی لیتری با رایحه سرد و شیرین داره
✅
😎
قبل از ثبت سفارش هم مشاوره رایگان بهت میدن
شمارت رو بزن تا موجودیش تموم نشده
👇🏻
https://yeklinks.ir/bodytele?utm_source=bhr&utm_medium=foritel
https://yeklinks.ir/bodytele?utm_source=bhr&utm_medium=foritel
پرداخت درب منزل+ارسال رایگان</div>
<div class="tg-footer">👁️ 35.6K · <a href="https://t.me/akhbarefori/693509" target="_blank">📅 21:02 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693508">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Dk3YYMG0Lf2I4gCULcOyFycytOfFXD_rdsMFzkbgZ5XMPHTPLPaPmBVMoSN0D-rGZLT6xDwegT9yF1p7PWYIOBvG1fmUv0ZqlCuljIbzlEX7WgWsiKoQOSitwlOXC97zSHb7rYpcC_CcqN7TAMnNZlWBJo6RcbC0Eo56rUzDhirilI--AIRl_VrCV0j9wVCjS95ojE847rQYXPwXUIxrTgitdsLgScpoXX7pQ-oU6VLvShRAXqIrRZTyo6obTGLoKy02RTAt6VExtlxJBBA7pedrWL2jHyeC18smgaRe0onvUskWmKfoEv1TCaSChC3dlXBKQBo3XRsoTHnEMDavyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خطوط تلفن سازمانی ۴ و ۵ رقمی نکسفون، راهکاری برای حرفه‌ای‌تر شدن ارتباط تلفنی کسب‌وکارها هستند:
🔢
شماره‌ای کوتاه و آسان برای به خاطر سپردن
📞
نمایش شماره ۴ یا ۵ رقمی سازمان در تماس‌های ورودی و خروجی
⭐
امکان انتخاب شماره دلخواه از میان شماره‌های قابل ارائه
🏷️
فرصت ویژه شهریورماه برای خرید خطوط ۴ و ۵ رقمی نکسفون با تخفیف‌های ویژه
🔎
دریافت مشاوره و بررسی شماره‌های قابل ارائه:
https://isp.nexfon.ir/khabarfori</div>
<div class="tg-footer">👁️ 35.4K · <a href="https://t.me/akhbarefori/693508" target="_blank">📅 21:01 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693507">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2ac08963c6.mp4?token=Vk1vbOUs5GVVY_HwaeEK1GUYYMFTiIlceJ2P259DSYA5320Xhkl6GFdg9b5NPKF8BPixsSP7Zg1EqoqXxLnbI4k1_-K-ZubxG3rEFyyUcq2U66qzgAKSZOjHdBN2LuxiduAHSduMr05O0cfa4h1evkqoasK8QHfUHuu14pm9HWr0gJTarqeueuLFl5JaoChuecJGXkLKfSDFM6JICxhxmyVQ5eM9hMiEBGVK4z6S1vJAb5i2YjuLmS9D3gg23aEC4o2meMpW2kHghaD1lPMJkkDtlhxGaSwqbuB7N0QM6B8dpeMhhio-dJWKz1G7_EZ7VSJlEejCkYHzkSQ0via0SA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2ac08963c6.mp4?token=Vk1vbOUs5GVVY_HwaeEK1GUYYMFTiIlceJ2P259DSYA5320Xhkl6GFdg9b5NPKF8BPixsSP7Zg1EqoqXxLnbI4k1_-K-ZubxG3rEFyyUcq2U66qzgAKSZOjHdBN2LuxiduAHSduMr05O0cfa4h1evkqoasK8QHfUHuu14pm9HWr0gJTarqeueuLFl5JaoChuecJGXkLKfSDFM6JICxhxmyVQ5eM9hMiEBGVK4z6S1vJAb5i2YjuLmS9D3gg23aEC4o2meMpW2kHghaD1lPMJkkDtlhxGaSwqbuB7N0QM6B8dpeMhhio-dJWKz1G7_EZ7VSJlEejCkYHzkSQ0via0SA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پس از طوفانی شدید، نیویورک شاهد «باران عروس‌های دریایی» بود
🪼
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36.6K · <a href="https://t.me/akhbarefori/693507" target="_blank">📅 20:51 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693506">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromروزنامه دیجیتال خبرفوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Fg1NrmeSqsGC2S54lZaeX5DrsEMBWHNXMS9rSvygYcToBkksaUnStPLiuITcPy-qtkIU6Ql3yDiHLIg--kua3KtZx7XVvNG-RA9D0LgZkT9YJ8HRALa-0iZ8MiUpKbP9UG1N3i5iLwgMOworVixwGkqoLKY918ys_t-C8aG5H_vw-W12hguosHdFKszUw5KLRsKJ52qMUzgeTocylgDvJK_HTpnzmywKoUkvlPl2Upio-J6lop0aFTaV_-LgUnsOx_wsOUS4UoTk4zqOX5bnN8Cbk0E-33tk12DnCGgEAs0_h57YMxK8W6jOcx-QQahnqzWdmUSpKz-jBzyQ3b_mPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
زهر چشم
🔹
بعد از اظهارات شب گذشته ترامپ، نیروی دریایی سپاه طی یک اقدام هماهنگ و پیچیده با اشراف اطلاعاتی و جنگ الکترونیک، توانست یک فروند زهپاد پیشرفتهٔ ارتش آمریکا را که به منظور جاسوسی در تنگهٔ هرمز فعالیت داشت، به دام بیندازند. سپاه پیش از این نیز یک فروند از همین زهپادها را به غنیمت گرفته بود. نیروی دریایی سپاه با قاطعیت اعلام کرد که تنگهٔ هرمز مسدود است و در برابر تحرکات خطرناک و تردد از مسیرهای غیرمجاز در تنگهٔ هرمز، با اقتدار و بی‌وقفه در حال برخورد هستیم.
🔹
هشتصدوهفتادویکمین شماره جلد یک خبرفوری
#تیتر_یک
@rozname_fori</div>
<div class="tg-footer">👁️ 38.3K · <a href="https://t.me/akhbarefori/693506" target="_blank">📅 20:45 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693505">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9fa6d0f45f.mp4?token=tRwScDMLWOVGuTybXH1kU4i__JV5lxF69pAXGGOc36UsHSlF1oIHg8cHJEGYT81w_pOqhXHYy5Xgvl6qfhwHNXo3Kg2OhUisfic5Wkq4JHxn1SI-EW3j7F_aHU8ZzNogXG3YObcHpwo94H35DuAaLA25cdTmCkupi0j0jRtH4FNybBBxSsrVQjclYWgOKRVV3BJMulx0Ju6yGdceHQSA93cbRLBsLoaO1OQMLlXMSoXQJlXeZdntSAZz8e7Q4f4ldi7JbbX4tcZkW6XEzCZruUjfEzT4ZR8S0VMbSTBeNYchKWc_fApf-YESDFNKui1-UEkyWivX76hKtMEgn77YIA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9fa6d0f45f.mp4?token=tRwScDMLWOVGuTybXH1kU4i__JV5lxF69pAXGGOc36UsHSlF1oIHg8cHJEGYT81w_pOqhXHYy5Xgvl6qfhwHNXo3Kg2OhUisfic5Wkq4JHxn1SI-EW3j7F_aHU8ZzNogXG3YObcHpwo94H35DuAaLA25cdTmCkupi0j0jRtH4FNybBBxSsrVQjclYWgOKRVV3BJMulx0Ju6yGdceHQSA93cbRLBsLoaO1OQMLlXMSoXQJlXeZdntSAZz8e7Q4f4ldi7JbbX4tcZkW6XEzCZruUjfEzT4ZR8S0VMbSTBeNYchKWc_fApf-YESDFNKui1-UEkyWivX76hKtMEgn77YIA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
زیرسطحی REMUS 600 چه ویژگی‌هایی دارد؟
🔹
یک زیرسطحی خودکار پیشرفته و بدون‌سرنشین آمریکایی است که برای مأموریت‌های شناسایی زیرآبی، نقشه‌برداری بستر دریا، کشف و طبقه‌بندی مین، جمع‌آوری داده‌های محیطی و جست‌وجوی اهداف زیرسطحی طراحی شده است.
🔹
این سامانه می‌تواند…</div>
<div class="tg-footer">👁️ 38.4K · <a href="https://t.me/akhbarefori/693505" target="_blank">📅 20:40 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693503">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RDh0bmECEWDhsl682S4KxfKCXZgDKNiiLN7LppDmPJzuRwMvThK7lt35t0RC1aNdcDaSdoZpvZEe28B-_6m1xrQsQk8kazLypoXR8vO6R_xOOsAO8WNxg48pvKtltcvUfxS1N18Pjry5FlUOtJkLHECmCjQ7exCK_P4vT6Ayk-jX2r4V6jek6G-W_oqZObuE2_gdnSIgL4JjW03rRht_McjiN04cpYoVvS_tY4KkFO1c4YbUxRcXFpWWGxQaP1jzHMrF800M8WNb8B7Bu-R3P7bw-vtWuDImbwjwfx8SKZPxAQq5fDeeqtumi1BLAx1CjEJvIpfxIv2ZTG8w5d9-Ng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
همه چیز درباره مذاکرات و امکان توافق ایران و آمریکا / امکان توافق از بین رفت؟/ باید منتظر جنگ باشیم؟
🔹
اختلاف بنیادین دو طرف بر سر تنگه هرمز و ترتیب لغو تحریم‌ها، چشم‌انداز توافق جامع در کوتاه‌مدت را همچنان مبهم نگه داشته است. ترامپ نیز اعلام کرده که امکان بازگشت به تفاهم قبل با ایران وجود ندارد. با این حال، اکنون سوال اینجاست: آیا توافق ایران و آمریکا در آینده نزدیک نامیسر است؟
در خبرفوری بخوانید و نظر بدهید
👇
khabarfoori.com/fa/tiny/news-3248085</div>
<div class="tg-footer">👁️ 39.8K · <a href="https://t.me/akhbarefori/693503" target="_blank">📅 20:34 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693502">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HTRuTNQnCe5oA7ohgdqdELtx5kLrRV_hQVA-QKPN9H47RuB-NHpO3xxwo5le-eI6bgMtVSh3QzpEcb0s0tii1o5zapTQj6u0AWSE5LNVlHUhW2tQUw4Oy9-rkExawIFC0-sDFCSe42EHEi80qjL8EtpDw4YPU-2MTj2wqSpZJ0CrYHfH6Mts7xDH3pbVHoM-6mTkjb6rWeRHI1qto6VjjpWiXWhZw7IIe7EwVH5A25sJHZ37WQfCD4gOBTHpcSqMv30phaFTghZ4oZvDEwlTQ8rFCXWQJxz8f3I-ao6uiBlvubXY2dG3uQKNAG6_h7cK-w1O_oaKhpLMYrwfvWWsYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
یا بازار نفت احمق است یا آمریکا دروغ می‌گوید؛ همه ‌می‌دانند اولی درست نیست
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 38.7K · <a href="https://t.me/akhbarefori/693502" target="_blank">📅 20:31 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693501">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/073f5f7715.mp4?token=FQ_HoaZujTIcs3_T76bpMH-ghvxKSiRICOLKN4S4150MXJ5KHYbLBOiZWw_f5Fu5MOXZvO-3ghxModTJ_hlWqHF1eNRkIgOxD_suGYPS0vtGcU-hiMUNdFBSo-aAEmFe_4JivRiupSt3hHBJGjI_KFFWRcNuyiQcH-f0mK-bwQsjAOyBaLuuBDmgn8pbgnT42Se9LMoArsVUQ1gnKSZHnNdfOB9CHMsoj7GED_vwukRMkdgaCX5ToT_TqWjCXJmuLOBJ_t2f01psGDR9xkIi5StrpylT4wZpJOrOxejfShP6M9MmJSpr3_YmqXitmwursepTas57rHFKVsz6t-JZZw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/073f5f7715.mp4?token=FQ_HoaZujTIcs3_T76bpMH-ghvxKSiRICOLKN4S4150MXJ5KHYbLBOiZWw_f5Fu5MOXZvO-3ghxModTJ_hlWqHF1eNRkIgOxD_suGYPS0vtGcU-hiMUNdFBSo-aAEmFe_4JivRiupSt3hHBJGjI_KFFWRcNuyiQcH-f0mK-bwQsjAOyBaLuuBDmgn8pbgnT42Se9LMoArsVUQ1gnKSZHnNdfOB9CHMsoj7GED_vwukRMkdgaCX5ToT_TqWjCXJmuLOBJ_t2f01psGDR9xkIi5StrpylT4wZpJOrOxejfShP6M9MmJSpr3_YmqXitmwursepTas57rHFKVsz6t-JZZw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
۶ ترفند تمیزکاری آشپزخونه که قطعا به کارت میاد! #ترفند_فوری
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 39.7K · <a href="https://t.me/akhbarefori/693501" target="_blank">📅 20:27 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693500">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/73786a91c2.mp4?token=s81in4qNV9XoP1gG3eaAyDzfB5ELXCTV1osrvs8mU8S6HimsV4zs46xzUwUV8McDT3xxG6z5XtIaZZ1cY743dS_DC0Jg8XDNFjHmierTVEZWMNVkFk-OczBlSjnBzy1cALQ7wpLqI2TynREEJat6AVCRaC1vYQxH4aN5uQ8qrmws0VLqOu0LhX3YNhsR13Ie1aFpxLuBSyVnq3Iyr282fysNfAE56kyOQ6AplBsCRhbdk2-hRsPriKQNG__PLlYqMQ5NY2T4x9hsmrSo8tqKAH2EkCSFiiM_toN34cj5ZfNz5OZ8e_RC-BSyXDhX_PDZO6O14g5yySV4yRW2tE-4CQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/73786a91c2.mp4?token=s81in4qNV9XoP1gG3eaAyDzfB5ELXCTV1osrvs8mU8S6HimsV4zs46xzUwUV8McDT3xxG6z5XtIaZZ1cY743dS_DC0Jg8XDNFjHmierTVEZWMNVkFk-OczBlSjnBzy1cALQ7wpLqI2TynREEJat6AVCRaC1vYQxH4aN5uQ8qrmws0VLqOu0LhX3YNhsR13Ie1aFpxLuBSyVnq3Iyr282fysNfAE56kyOQ6AplBsCRhbdk2-hRsPriKQNG__PLlYqMQ5NY2T4x9hsmrSo8tqKAH2EkCSFiiM_toN34cj5ZfNz5OZ8e_RC-BSyXDhX_PDZO6O14g5yySV4yRW2tE-4CQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ریما رامین‌فر و پسرش روی فرش قرمز جشنواره فیلم ونیز
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 39.1K · <a href="https://t.me/akhbarefori/693500" target="_blank">📅 20:21 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693499">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">♦️
فرشاد مومنی: ۸۰ درصد ظرفیت صنعت لوازم خانگی بلااستفاده است؛ چرا باز هم از واردات می‌گوییم؟
فرشاد مومنی، اقتصاددان، با انتقاد از درخواست ۴۰ نماینده مجلس برای آزادسازی واردات لوازم خانگی گفت:
🔹
در شرایطی که حدود ۸۰ درصد ظرفیت تولید صنعت لوازم خانگی بلااستفاده مانده و کشور برای تأمین ارز دارو، واکسن و مواد اولیه تولید با محدودیت مواجه است، چگونه می‌توان برای واردات کالاهای نهایی خارجی اولویت ارزی قائل شد؟
🔹
وی همچنین نسبت به گسترش واردات از مسیرهایی مانند کولبری و ته‌لنجی انتقاد کرد و گفت این سیاست‌ها می‌تواند تولید داخلی، اشتغال و سرمایه‌گذاری را تحت فشار قرار دهد.
🔹
به گفته مومنی، مسئله فقط واردات لوازم خانگی نیست؛ بلکه انتخاب میان تقویت تولید و اشتغال داخلی یا بازتولید وابستگی به کالاهای ساخته‌شده خارجی است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 38.3K · <a href="https://t.me/akhbarefori/693499" target="_blank">📅 20:20 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693498">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/37e1f47427.mp4?token=QPsBH-AaVG8OXyB6Nl7IfqZ7W84UMVjuO41ffLkdmtTU4MsiqgjV1Cs_PpRnfIWoOcPpa8ePoPiZnu_6mfyicNePlXGTGic9GpqPK5WXJDIunpBVH2yMqtTWPjQnXVsZue9b4uP_Z5TPE1-WQ_H7agVuQdSwdG6o1E-7NEdLzkuvrSn7DO4IA0YyTp2Fg65ixR1JZrNeQ-73X-7T0zJrVoFl4Z4ly7xYYFHKyhsTPukgemVQdTl1ILBtk4cb6LbSX0TuqFFri7mSGv8zkUYZGFm-I2KRvpNvXSwHujWskTYPpBu0khUkSqStuIENuRAUDObzBA9SxG469j_JYq98Aw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/37e1f47427.mp4?token=QPsBH-AaVG8OXyB6Nl7IfqZ7W84UMVjuO41ffLkdmtTU4MsiqgjV1Cs_PpRnfIWoOcPpa8ePoPiZnu_6mfyicNePlXGTGic9GpqPK5WXJDIunpBVH2yMqtTWPjQnXVsZue9b4uP_Z5TPE1-WQ_H7agVuQdSwdG6o1E-7NEdLzkuvrSn7DO4IA0YyTp2Fg65ixR1JZrNeQ-73X-7T0zJrVoFl4Z4ly7xYYFHKyhsTPukgemVQdTl1ILBtk4cb6LbSX0TuqFFri7mSGv8zkUYZGFm-I2KRvpNvXSwHujWskTYPpBu0khUkSqStuIENuRAUDObzBA9SxG469j_JYq98Aw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
کارشناس صداوسیما: ژاپن انتقام نگرفت و باخت؛ مردم نمی‌خواهند مثل ژاپن باشیم
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 38.7K · <a href="https://t.me/akhbarefori/693498" target="_blank">📅 20:14 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693497">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vh2df7OPa5JK0fcpUms6NyJmNIoysET9j2C9RaS5DnACNA3uQq8mhh5qw0l7KUICYwEXK7UxMxRgFmFjLVM0rUvoo_PeGRAswPXaFtVrM7TTYiUZvAmeFhq_A1c2Vo6TX-c18UeFXA9zquHeOFCJmiQpjJIKG2l7u_SAdzoo37M_GAjX1IlRbB-afE0QEcA5ZHx5a_AgrW8AjwSAE99qy7-Wd65qu0DYJibrX5y1ibDW-2a4Mkw5D_P43LyZb7X9UAvaLqd5CiqTIKtwMeghCbWXRgxGYnEBc3AiikvAFLuRL5Tk7vG6Zt3EVlqJYOfvT3pXc58iUbLi11Pbhq3iAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
بسته‌بندی موش و فروش آن دانه‌ای ۲۰۰ هزارتومان
!
🔹
این موش‌ها برای تغذیه سگ و گربه توسط مردم تهیه می‌شود.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 37.9K · <a href="https://t.me/akhbarefori/693497" target="_blank">📅 20:13 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693496">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">♦️
مدیرعامل شرکت فرودگاهی امام خمینی: پروازها به ترکیه، مالزی، چین، پاکستان برقرار است
🔹
به‌ جز پروازهای لغوشده از جمله امارات، عراق، عمان و گرجستان هیچ مسیر جدیدی برای لغو پروازها اعلام نشده است. پرواز به عربستان از قبل محدودیت‌هایی داشت.
🇮🇷
✊
@AkhbareFori…</div>
<div class="tg-footer">👁️ 37.1K · <a href="https://t.me/akhbarefori/693496" target="_blank">📅 20:13 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693495">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">♦️
مهلت ۴۸ ساعتۀ عشایر بصره به دولت عراق  یکی از شیوخ عشایر عراق در بصره:
🔹
۴۸ ساعت به دولت عراق مهلت می‌دهیم تا از لغو پروازهای ایران عقب‌نشینی کند.
🔹
اگر دولت از تصمیم خود کوتاه نیاید وارد فرودگاه بصره می‌شویم و از تمامی پروازها جلوگیری می‌کنیم.
🇮🇷
✊
@AkhbareFori…</div>
<div class="tg-footer">👁️ 37.2K · <a href="https://t.me/akhbarefori/693495" target="_blank">📅 20:13 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693494">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromSnappBox | اسنپ‌باکس📲🛵</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/on4bagN_KMJ-iqwwyRWiHhpwMnEGRfnkTSxbIC_ulyJ7jcYxsk9VRoaiLh4sf3KXnStr223QgjkLEpy7CS1j2h29mcRjn4NKMwrrvxU2bf8S15-NYoFfuYv3U6tsJpNvh-7q3Jq2wi7bRLGMqQ6LKkSC_aUxhupqy6XaLd-GTL55NArxnKnoH631ZBiNKkzL77uhSBgdHb5HPtO3o_0pZlT5cdsB6fM69n1ZHkqGfH1J3KyDh__l5YL9BNfXYReE4RGDTQ7ozoiy_rt-QoALIxRZkGRXxqJ7jmkZloxVTel9F-izmzbcLJVy7uSvEnJv5ut_S4pI95AUuJeNg8CPFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این باکس جادو می‌کنه!
🎁
✨
با اسنپ‌باکس هم
۵۰ هزار تومن تخفیف
بگیر، هم شانس برنده شدن
۵۰ میلیون تومن
رو داشته باش!
💚
تا پایان مهرماه، موقع ثبت درخواست اسنپ‌باکس کد
JADOO
رو وارد کن و وارد قرعه‌کشی شو.
📦
برای تخفیف‌های بیشتر کانال اسنپ‌باکس رو دنبال کن:
https://t.me/snappbox</div>
<div class="tg-footer">👁️ 36.3K · <a href="https://t.me/akhbarefori/693494" target="_blank">📅 20:08 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693493">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9f765024f5.mp4?token=O6viXceAolNX4y917MYvZ3WR6inBTUMCZhabaG68wgRV94CnP2XaATyRBWUzKFKQB3DVV-x3e2MyM94BplZ0bcPptmkemcO4XqYVXnc52fVzHXKmVXLQQLVCl-qFDaAynTjt_F9jB_t52AAeSYbpi3Lww9r4nu4LPaf4j1IHT8jHy_hn12yV6ZETQejnTNBfecTsLTvwNXBl33HHR3P0TW0OAIiCclvD91lvTdgf9BJIKCetTH9Zvv1Atb6gxrIyuvgnWZ0RvsS_t1UDalJ3AwmuvPWOVzf_bHsKibvLEmSMbgv28CK0yja32tWMGEnTXiS5lTjm2VAo2EDOWU3Daw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9f765024f5.mp4?token=O6viXceAolNX4y917MYvZ3WR6inBTUMCZhabaG68wgRV94CnP2XaATyRBWUzKFKQB3DVV-x3e2MyM94BplZ0bcPptmkemcO4XqYVXnc52fVzHXKmVXLQQLVCl-qFDaAynTjt_F9jB_t52AAeSYbpi3Lww9r4nu4LPaf4j1IHT8jHy_hn12yV6ZETQejnTNBfecTsLTvwNXBl33HHR3P0TW0OAIiCclvD91lvTdgf9BJIKCetTH9Zvv1Atb6gxrIyuvgnWZ0RvsS_t1UDalJ3AwmuvPWOVzf_bHsKibvLEmSMbgv28CK0yja32tWMGEnTXiS5lTjm2VAo2EDOWU3Daw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
بیل گیتس: هوش مصنوعی به طرز دیوانه‌واری از انسان باهوش‌تر خواهد شد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 37.7K · <a href="https://t.me/akhbarefori/693493" target="_blank">📅 20:07 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693492">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oSbjIdIGUXrMOZkoP-qZOTmX0-zy8snH_9tysK3Euy4kwXo8EfJ2u8A1pUXCwmGxDL0pCoHusDG4Dk0VZbH8M8WXyaLXucTw_emEElR9NxMvRtvy_AF8cNgph50GEwsMHZPU_T_t0FBMQ2Yrm2zyq5iKwISamSGm8rbz9kMG6u2WWM_txCgswqXhyTuw41TcDI4v4LJKsGNboyCqPrNZ2U1QRKh59QxxbDqt0SBsuRVpcG5DDnThnAPye5eVAmxiQg4po0Ak06Cejas4yg72nsF3_OUMthevc0O9WVHhUCEAD7E1ttRsH6hOd7AvygCEca-GCKCXXbaTriMKoOYhQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
علی قلهکی: «همه‌ی شرایط در منطقه» شبیه به «بهمنِ ۱۴۰۴» است
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 38.7K · <a href="https://t.me/akhbarefori/693492" target="_blank">📅 20:06 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693491">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">♦️
شیخ نعیم قاسم، دبیرکل حزب‌الله: اینکه اکنون اسرائیل تحرکاتش محدود شده حاصل مقاومت و همچنین تفاهم اسلام آباد است
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 37.8K · <a href="https://t.me/akhbarefori/693491" target="_blank">📅 20:04 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693490">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LDvZxyXnqv1o6UlTTKfwB95Xc8yOnbQ8C1YSVwt53LzVag5khrdWRAes2CMQubcZ_v_5V7j8gm_kV3sjKrgS2Z58hrIi3u6alBedMnB2Sbqo_w8TenOl9l_e9n_lXp2qpbsYoDla6hrlJHftDgUWiGBSxwgLGsF9obWYKdZCQUttp55v7AFeLBmA89BKE9hhDR6hJi_5O-EWaGp9TasV1zP3O6JdKFH3HPiSw6qyONNCuwZ0esa7_B7Fei2XUzVEE641paCxlYhyHxjRuZmFWseu4CCWmuTqDw1Lpd4gB4SeIdQ-7iaOmo83Rb9TdJtMbDfuVTYVXhuoM5BSdw2kiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
انواع جرائم مهم مالیاتی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 38.5K · <a href="https://t.me/akhbarefori/693490" target="_blank">📅 20:02 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693488">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/53bab596ba.mp4?token=nPYFb2MpHRMKGUEigk5z7KWpYfqH1ZTqJbcB84XpCYeDHDi7HCzcQNgQFRcvTwbiI9ZhDjP2XIafMjekSiLH3clfe1qjIwM_ZzgGeUeSUCeXV2yWOeWW2Rgqh9i8hUjfH9YdYZZ5I7oB7yDqqqZDtEUB0b2WR5jmZVenyFKPOPNeQmHQ5iHsAh4frlq8wVAroU57fAdI4yVqqdd754cKpW7yId-FAm7rBEHT7h57hFJlVdwW2LdqHFeIU2S7PqTqriZLhTBOoLeGZlGliuqSEotbueaT6Rq4t4sHj9-naLXej0dbSi8XZY0vRRJP-paP1pXva9hFb2YB1JupSemSAJMrRsRrc8qjgrJLnejxu5W4Z5cuSq4p-2EXL5fTJ6aAAk59PDbOOsRmGy2xd2CbTa5h9RXs03RgM36tq3uak02crM4nn1Xwc1plwWpYN8thS26QbIzt7GhlVMo7-Ix5xDn1DGpbkF3Nu_EZkKt3jn9Yy3V81rVmVGPipVgPepK2e5M333n6PKybT2dXUj89qlRKLm6EZvL2S-oP7RhrXsqIJZb-yBjQ5ySzMA0qWgwe6nKr12KQKafXIzLHIulKjneJzL0JmJOGCzIoS3MoCtebJEotRdPgCV8B8DCtDKJ4ocwYtdXni_w5hot0FAluh5VIy7yIhSgp6l8m1l90Ylo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/53bab596ba.mp4?token=nPYFb2MpHRMKGUEigk5z7KWpYfqH1ZTqJbcB84XpCYeDHDi7HCzcQNgQFRcvTwbiI9ZhDjP2XIafMjekSiLH3clfe1qjIwM_ZzgGeUeSUCeXV2yWOeWW2Rgqh9i8hUjfH9YdYZZ5I7oB7yDqqqZDtEUB0b2WR5jmZVenyFKPOPNeQmHQ5iHsAh4frlq8wVAroU57fAdI4yVqqdd754cKpW7yId-FAm7rBEHT7h57hFJlVdwW2LdqHFeIU2S7PqTqriZLhTBOoLeGZlGliuqSEotbueaT6Rq4t4sHj9-naLXej0dbSi8XZY0vRRJP-paP1pXva9hFb2YB1JupSemSAJMrRsRrc8qjgrJLnejxu5W4Z5cuSq4p-2EXL5fTJ6aAAk59PDbOOsRmGy2xd2CbTa5h9RXs03RgM36tq3uak02crM4nn1Xwc1plwWpYN8thS26QbIzt7GhlVMo7-Ix5xDn1DGpbkF3Nu_EZkKt3jn9Yy3V81rVmVGPipVgPepK2e5M333n6PKybT2dXUj89qlRKLm6EZvL2S-oP7RhrXsqIJZb-yBjQ5ySzMA0qWgwe6nKr12KQKafXIzLHIulKjneJzL0JmJOGCzIoS3MoCtebJEotRdPgCV8B8DCtDKJ4ocwYtdXni_w5hot0FAluh5VIy7yIhSgp6l8m1l90Ylo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
چه کسی مانع تسویه با مشتریان میلی گلد است؟
🔹
میلی‌گلد اعلام کرده است که ۹۶۵ کیلوگرم طلا به صورت فیزیکی در خزانه‌های امن و بانکی موجود دارد.
🔹
اما دسترسی میلی‌گلد به این خزانه فیزیکی طی روزهای گذشته توسط برخی نهادها مسدود شده است.
🔹
طبق آمارهای منتشر شده توسط میلی‌گلد، این پلتفرم در ۳۰ روز گذشته ۷ هزار میلیارد ریال با کاربران خود تسویه انجام داده است و ۳۶ کیلوگرم طلا را نیز تحویل داده است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 38.9K · <a href="https://t.me/akhbarefori/693488" target="_blank">📅 19:57 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693485">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4c21c35167.mp4?token=T8N6fzK5xBwIHvAEJaOVysGJ1HsQXixVpYrvT2M2vywxkzDRDorQzi0zbkk5EdUWtbUox9x0G3Nb9e9Oxm70boo0XsC5JXdFtGGWjT57Vh934mOodE9r6xfgnawVN-jn2Lrs1vWvoWIrEFiRyMuq8qOwnqEz8WZRCF4XTeU76DBLU-GN8z_UsWOavpdwZRaR3TsNlx97yQpvjJzu1dklrF7dp6DwoKG4-aw2mUU5ThBE-SRTglL3YWc0vnHxY872YK4O6Tx3aDSEF75htF-56h-pebnqkgq3urJIeFsF5ME7MmIRJNnR5Ww32JOldshB6h260KYhHh87nSJxjUsAhk-KYHcVT_WBY_RypLyWdyurD1DB0BHmq_z1EawLvCGG-ZAOc0unofQ4SDo9SS-3HIy2lWpbaqFXS5YSYUZZCv1SfeqXYvtaHQBxdonJ1KfaQ965twImkjwvpc5rtzR0TF8IpKKjSrQXJwQMMypsJ8-i5e2f4k71j65fktwj61WUc-Hshr8BtMOBTMhFHnENlNQ6dZ778v_tsZc75F8F_YjjIS6fEYCfIeUG7_Mkxp8wQLySs4ojPNgZDXiXwI1g4_zKRTxRObxyW6RbU069vnliBOhCSOOaThFc8glEdyP7vHWWHkGJwxc-PvBj0bXj5p5mz2-JtYlLLm3QqOY8Zns" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4c21c35167.mp4?token=T8N6fzK5xBwIHvAEJaOVysGJ1HsQXixVpYrvT2M2vywxkzDRDorQzi0zbkk5EdUWtbUox9x0G3Nb9e9Oxm70boo0XsC5JXdFtGGWjT57Vh934mOodE9r6xfgnawVN-jn2Lrs1vWvoWIrEFiRyMuq8qOwnqEz8WZRCF4XTeU76DBLU-GN8z_UsWOavpdwZRaR3TsNlx97yQpvjJzu1dklrF7dp6DwoKG4-aw2mUU5ThBE-SRTglL3YWc0vnHxY872YK4O6Tx3aDSEF75htF-56h-pebnqkgq3urJIeFsF5ME7MmIRJNnR5Ww32JOldshB6h260KYhHh87nSJxjUsAhk-KYHcVT_WBY_RypLyWdyurD1DB0BHmq_z1EawLvCGG-ZAOc0unofQ4SDo9SS-3HIy2lWpbaqFXS5YSYUZZCv1SfeqXYvtaHQBxdonJ1KfaQ965twImkjwvpc5rtzR0TF8IpKKjSrQXJwQMMypsJ8-i5e2f4k71j65fktwj61WUc-Hshr8BtMOBTMhFHnENlNQ6dZ778v_tsZc75F8F_YjjIS6fEYCfIeUG7_Mkxp8wQLySs4ojPNgZDXiXwI1g4_zKRTxRObxyW6RbU069vnliBOhCSOOaThFc8glEdyP7vHWWHkGJwxc-PvBj0bXj5p5mz2-JtYlLLm3QqOY8Zns" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏
♦️
جاسوس‌های ایرانی‌ و لبنانی در ترور سید حسن نصرالله نقش داشتند؟!
🔹
روایت فرزند شهید نصرالله به مناسبت دومین سالگرد شهادت دبیر کل حزب الله لبنان
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 40K · <a href="https://t.me/akhbarefori/693485" target="_blank">📅 19:48 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693484">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">♦️
عراقچی: به‌دلیل ملاحظات امنیتی و تهدیدات مستقیم آمریکا، تصاویر رهبر ایران منتشر نمی‌شود، اما دستورات و دیدگاه‌های ایشان به‌طور مستمر دریافت و اجرا می‌شود
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 40.7K · <a href="https://t.me/akhbarefori/693484" target="_blank">📅 19:43 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693483">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">♦️
۶ عامل که می‌توانند به ستون فقرات آسیب بزنند
🔹
شکم بزرگ، خواب نامناسب، بغل‌کردن نادرست کودک، نشستن طولانی در وضعیت نامناسب، ایستادن طولانی و بلندکردن اجسام سنگین از عوامل مؤثر بر فشار و آسیب به ستون فقرات هستند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 41.3K · <a href="https://t.me/akhbarefori/693483" target="_blank">📅 19:42 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693482">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d6c5e80ae3.mp4?token=bmaRCzRsLBVYWImawKjA6MC4VGkxIb1JZbQQA80sXiQnDeICXpdjOQN9Hm1hGb6xaQxY-ALGPEw14ru_8bKkyQrgH5YAezP81YQbDWGCq5bSE6UMpstJa6huo7hVUnxHQ136M_0lWRehiWAQBSF8oX_NNPJ889ssuCTHJsl08CS2k_gBFs-QM3rUZTUc5_--qlcjwFOnvzjjM2-Eo1J99cpZKzxtgrkw6Bn-_CNmh25FytR_VexSwXkKKk0GZl3602CTpsr8nXRVsJuFeXHx-BOy04sZwR7oJV0zLws6BwUjKlZM3pU-Kufwlwb57zzIoTaxmr40b-tysAi_r9NAdg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d6c5e80ae3.mp4?token=bmaRCzRsLBVYWImawKjA6MC4VGkxIb1JZbQQA80sXiQnDeICXpdjOQN9Hm1hGb6xaQxY-ALGPEw14ru_8bKkyQrgH5YAezP81YQbDWGCq5bSE6UMpstJa6huo7hVUnxHQ136M_0lWRehiWAQBSF8oX_NNPJ889ssuCTHJsl08CS2k_gBFs-QM3rUZTUc5_--qlcjwFOnvzjjM2-Eo1J99cpZKzxtgrkw6Bn-_CNmh25FytR_VexSwXkKKk0GZl3602CTpsr8nXRVsJuFeXHx-BOy04sZwR7oJV0zLws6BwUjKlZM3pU-Kufwlwb57zzIoTaxmr40b-tysAi_r9NAdg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
عراقچی: به‌دلیل ملاحظات امنیتی و تهدیدات مستقیم آمریکا، تصاویر رهبر ایران منتشر نمی‌شود، اما دستورات و دیدگاه‌های ایشان به‌طور مستمر دریافت و اجرا می‌شود
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 40.9K · <a href="https://t.me/akhbarefori/693482" target="_blank">📅 19:41 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693481">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">♦️
مقام آمریکایی به سی‌بی‌اس: ما می‌خواهیم تعهدات مرتبط با هسته‌ای در پیشنهاد ایران گنجانده شود
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 40.2K · <a href="https://t.me/akhbarefori/693481" target="_blank">📅 19:38 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693480">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">♦️
سفر وزیر خارجه عراق به واشنگتن
الحدث:
🔹
دستورکار کلیدی این سفر، پیگیری برای دریافت «استثنائات» جهت لغو تعلیق پروازهای ایران به فرودگاه‌های عراق است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 40.2K · <a href="https://t.me/akhbarefori/693480" target="_blank">📅 19:35 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693479">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/65deb07bf4.mp4?token=tktyHW3LpsKF6N-Ok-4XVku1EgJlnUmwWktip1160yhL1x85ccSjyySR9XklMB49EVfVSTS2giqSjf7B4JWU0Lx90ACKm7rZXnGO6S_NhN2C7DfCtVBz8o4kKcp0vln8mDdQZWxJpuGAQGb6JKCASIG48tPzjn-MQJgn6JrvVGNo9nT2lUsGFjGXNRwlCxU5343HoE_5UY8H3KA2zwZhRCOxXqBzWlzc21NUEzABAhPgUyKnoXBXRz0tRdihTsteeQwSCNNlZVb9pRA1rRIrQISduZ1kv_iwSsQP6pN881VynQQAStjASMhmeTgAP3ZW6f0A8RsUIkKUbR8UWxoEww" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/65deb07bf4.mp4?token=tktyHW3LpsKF6N-Ok-4XVku1EgJlnUmwWktip1160yhL1x85ccSjyySR9XklMB49EVfVSTS2giqSjf7B4JWU0Lx90ACKm7rZXnGO6S_NhN2C7DfCtVBz8o4kKcp0vln8mDdQZWxJpuGAQGb6JKCASIG48tPzjn-MQJgn6JrvVGNo9nT2lUsGFjGXNRwlCxU5343HoE_5UY8H3KA2zwZhRCOxXqBzWlzc21NUEzABAhPgUyKnoXBXRz0tRdihTsteeQwSCNNlZVb9pRA1rRIrQISduZ1kv_iwSsQP6pN881VynQQAStjASMhmeTgAP3ZW6f0A8RsUIkKUbR8UWxoEww" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
مهلت ۴۸ ساعتۀ عشایر بصره به دولت عراق
یکی از شیوخ عشایر عراق در بصره:
🔹
۴۸ ساعت به دولت عراق مهلت می‌دهیم تا از لغو پروازهای ایران عقب‌نشینی کند.
🔹
اگر دولت از تصمیم خود کوتاه نیاید وارد فرودگاه بصره می‌شویم و از تمامی پروازها جلوگیری می‌کنیم.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 41.7K · <a href="https://t.me/akhbarefori/693479" target="_blank">📅 19:33 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693478">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S5YovrsJ8V3PGHHrp9Z2AV_MQ-awSYSPulIB7lkI28dLcnGat5CtIi6-wiGdZwC5ZWKPYmxRc0R-a-a4Y5AK2qWiGZ1EX-Sew47O2IFin8d7syKDHzpF4BMUjf67R-ipZAuIVhD8HZ0rPKc1sB7TRE42hH6iqq_-N_AJJriJsEEEbyu_ON2X1sOe0FCnCEtMgZ2KZqjDcVXH4vs7gZSobgEu7RsSH-TCKjznWLBbROLivKuag8snoa71v--vV1wiBL9cRrb1Uvzbf5syG4WPoJV0tOvfcftHuVhcq0c1A1rc8A4hgxPk08yqXs1O7I6l72pkcSwrimJreplx0U8jeA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
بنزین یک‌ساله رایگان برای خودروهای وارداتی!
🔹
یکی از شرکت‌های عرضه‌کننده خودروهای وارداتی، در شرایط فروش چند مدل، هزینه بنزین یک سال خودرو را نیز به‌عنوان بخشی از خدمات فروش پرداخت می‌کند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 40.5K · <a href="https://t.me/akhbarefori/693478" target="_blank">📅 19:28 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693477">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c5f4121d3c.mp4?token=nlNizXIi11JXiHtmOLeR_0LK5cQ5xnGGL8rO7MRriwZw7H1ej2DNMPx3jyfHU179mtDcRMFlsVqMYFFO-vOAeX2_3H8cMGrGEpRF6n1YVp0wD4FEbBNtDXqzVIJJ4cU_bEsKQVkHOXiS24CymvscKfkmlNljaaGqkzt5cPOsMO0Y9NQfDZh7Di6nHXdRyy5MFd9UJX0wo5xPn3qGhb_aGU8W3kXFN8qIb1j5y1LQifPc4ATVtgPqbRl9eNu3uRT7-1HUCc4ehe6YJlRQpweLSodNz-2yX2U9EwETGtJK0l3wp_NQmwhCS_RhkqT7e0X-3oKOau4GNvR8sfbl5zJxqw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c5f4121d3c.mp4?token=nlNizXIi11JXiHtmOLeR_0LK5cQ5xnGGL8rO7MRriwZw7H1ej2DNMPx3jyfHU179mtDcRMFlsVqMYFFO-vOAeX2_3H8cMGrGEpRF6n1YVp0wD4FEbBNtDXqzVIJJ4cU_bEsKQVkHOXiS24CymvscKfkmlNljaaGqkzt5cPOsMO0Y9NQfDZh7Di6nHXdRyy5MFd9UJX0wo5xPn3qGhb_aGU8W3kXFN8qIb1j5y1LQifPc4ATVtgPqbRl9eNu3uRT7-1HUCc4ehe6YJlRQpweLSodNz-2yX2U9EwETGtJK0l3wp_NQmwhCS_RhkqT7e0X-3oKOau4GNvR8sfbl5zJxqw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ویدیویی پر بازدید از لحظه‌ تفاُلِ امروز پزشکیان به قرآن و واکنش قابل تامل او
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 42K · <a href="https://t.me/akhbarefori/693477" target="_blank">📅 19:21 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693476">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">♦️
ادعای وزیر خزانه‌داری آمریکا: به احتمال زیاد، اقتصاد ایران در دو هفته آینده فرو خواهد پاشید
🔹
انزوای اقتصادی ایران به صورت مرحله‌ای اجرا می‌شود و ارزهای دیجیتال، هوانوردی و حمل‌ونقل دریایی را در بر می‌گیرد.
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 41.6K · <a href="https://t.me/akhbarefori/693476" target="_blank">📅 19:16 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693475">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">♦️
ادعای وزیر خزانه‌داری آمریکا: به احتمال زیاد، اقتصاد ایران در دو هفته آینده فرو خواهد پاشید
🔹
انزوای اقتصادی ایران به صورت مرحله‌ای اجرا می‌شود و ارزهای دیجیتال، هوانوردی و حمل‌ونقل دریایی را در بر می‌گیرد.
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 43.3K · <a href="https://t.me/akhbarefori/693475" target="_blank">📅 19:05 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693474">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">♦️
طائب، رئیس سازمان بسیج: همان دشمنی که در ۱۸ و ۱۹ دی آدم کشت، مدافع حقوق ما شده است
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 43.5K · <a href="https://t.me/akhbarefori/693474" target="_blank">📅 19:04 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693472">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromآمارفکت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p-5vco08w1z6wa9dzMdUNP5XH9d0JRagN3AT6XYa7kS_K2NNAftI4dv2BitYeGkHSfU333I-13Yrf2VaXEaI8Bd91bSKvH5nX22HMiebk5zxeCK_7ZHYbkdHCnpXbZtYYSJ-UKCtWgu-V3bxKDLlKo5-AuplcStKrU-Fo3hpmBmuqQAlkYACSKNmAp89C7WqaLxH5I7w8LKcmziqgQ03BDap_QV4Qio1DGzuTv5nldBTmZBNL19szn481WTTMxj4Ow0YgcW8GtFTDjrC2tj_r1QHsTI6Ra99cg59t34Ov5OZ6_ywwxnG4WESdxcOJkBnowVnB2exWUABCQ4qXwrN4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مهم‌ترین مشکل بیمه تکمیلی از از دید افکار عمومی
🔸
در این نظرسنجی بیش از ۲۶ هزار نفر شرکت کردند که سهم روبیکا حدود ۵۷ درصد، تلگرام حدود ۱۸ درصد و بله ۲۵ درصد بوده است.
🔸
بیش از ۳۳ درصد شرکت‌کنندگان پوشش ناکافی خدمات و حدود ۲۰ درصد هم هزینه بالای بیمه را به عنوان بزرگترین مشکلات بیمه تکمیلی عنوان کرده‌اند.
🔸
طبق نظر کارشناسان نیز، افزایش هزینه‌های درمان، محدودیت پوشش‌ها و چالش در پرداخت خسارت از مهم‌ترین مشکلات فعلی بیمه‌های تکمیلی است.
@amarfact</div>
<div class="tg-footer">👁️ 44.5K · <a href="https://t.me/akhbarefori/693472" target="_blank">📅 19:00 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693469">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">♦️
ادعای ترامپ متوهم: به ازسرگیری حملات علیه ایران فکر می‌کنم
🔹
ارتش آمریکا عبور نفت از تنگه هرمز را تسهیل می‌کند./ خبرفوری #Devil
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 43.1K · <a href="https://t.me/akhbarefori/693469" target="_blank">📅 18:48 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693468">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3823d044b9.mp4?token=uKX8hs-sLzxIaE-hRJeoJvPKt-Akp7pRaz0SgnWavh1JXbkIWhbKKui_wzuqOQxszMFgZhq7rBITUHBjX842RKmBQdjHInDxEcJdI66jIitEvMJPmzo5-IOgsBnQ-2BIGqgJdmzOJS5GlTzOWoqE3VmjEEdfvzCMMI2MsLJefCTAIUHsFaNY91wtLg7lznN0YRWdQ7jPwAGmj__ouMlBzjgMYxG-VOI4YNTvsVp1SMgvKUGekmsyViXQbbPsLjvuM3Hwr4p_b4aw4hnFPuiaN9ANwGI9TMhcjGnQIr1A5wpbTZdz5nT8x7Gti4uUgOCvaeeQxwPgVhTct9qt3T0low" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3823d044b9.mp4?token=uKX8hs-sLzxIaE-hRJeoJvPKt-Akp7pRaz0SgnWavh1JXbkIWhbKKui_wzuqOQxszMFgZhq7rBITUHBjX842RKmBQdjHInDxEcJdI66jIitEvMJPmzo5-IOgsBnQ-2BIGqgJdmzOJS5GlTzOWoqE3VmjEEdfvzCMMI2MsLJefCTAIUHsFaNY91wtLg7lznN0YRWdQ7jPwAGmj__ouMlBzjgMYxG-VOI4YNTvsVp1SMgvKUGekmsyViXQbbPsLjvuM3Hwr4p_b4aw4hnFPuiaN9ANwGI9TMhcjGnQIr1A5wpbTZdz5nT8x7Gti4uUgOCvaeeQxwPgVhTct9qt3T0low" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
عوارض نزدیک بودن موبایل در هنگام خواب!
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 44.2K · <a href="https://t.me/akhbarefori/693468" target="_blank">📅 18:47 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693467">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">♦️
ادعای الجزیره: منابعی در تهران از ادامه مذاکرات غیرمستقیم میان ایران و آمریکا در نیویورک خبر می‌دهند
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 42.2K · <a href="https://t.me/akhbarefori/693467" target="_blank">📅 18:42 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693466">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">♦️
ادعای ترامپ به آکسیوس: انتظار دارد مذاکره‌کنندگان آمریکایی این هفته گفت‌وگوهای بیشتری با ایران داشته باشند/ خبرفوری #Devil
🌍
تازه‌ترین خبرهای ایران و جهان را به زبان انگلیسی دنبال کنید
👇
@AkhbareFori_En</div>
<div class="tg-footer">👁️ 43.2K · <a href="https://t.me/akhbarefori/693466" target="_blank">📅 18:37 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693465">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">♦️
ادعای ترامپ به آکسیوس: انتظار دارد مذاکره‌کنندگان آمریکایی این هفته گفت‌وگوهای بیشتری با ایران داشته باشند
/ خبرفوری
#Devil
🌍
تازه‌ترین خبرهای ایران و جهان را به زبان انگلیسی دنبال کنید
👇
@AkhbareFori_En</div>
<div class="tg-footer">👁️ 43.1K · <a href="https://t.me/akhbarefori/693465" target="_blank">📅 18:35 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693462">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/716ced5d0f.mp4?token=e3E7xM80Hz_miVhJe-lLjCWZHXbmuAVJktarxqO626J8wT1xchLP786leI2EDrjallKpkhE9Ths82u-0He5Fp-EFUYtgjfcKgwz9YSG3vzrCdvWZNTSoo6Llm8SxGJhkqHl-ONVMZFfZnSuulDD5AdNmiO6mKfHJd-Ru_2j1jovGafSHP56J6XVoOP597s2ywHsNyJn8g3JFfKo2S9PnjPu5etgEpwxU9zxz9wjSAo_kjhjWozu9a3Bj-x3iEFWhgv4B2yIe6YvCn1RzgzrO1yRABIwtwm7-FWbChhzLc2UFNzT_zggQy_VHE0rQ1pFCk7mb7j_Kcd7UGV3yP9hlLg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/716ced5d0f.mp4?token=e3E7xM80Hz_miVhJe-lLjCWZHXbmuAVJktarxqO626J8wT1xchLP786leI2EDrjallKpkhE9Ths82u-0He5Fp-EFUYtgjfcKgwz9YSG3vzrCdvWZNTSoo6Llm8SxGJhkqHl-ONVMZFfZnSuulDD5AdNmiO6mKfHJd-Ru_2j1jovGafSHP56J6XVoOP597s2ywHsNyJn8g3JFfKo2S9PnjPu5etgEpwxU9zxz9wjSAo_kjhjWozu9a3Bj-x3iEFWhgv4B2yIe6YvCn1RzgzrO1yRABIwtwm7-FWbChhzLc2UFNzT_zggQy_VHE0rQ1pFCk7mb7j_Kcd7UGV3yP9hlLg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ادعای وزیر خزانه‌داری آمریکا: چین کمک‌های خود به ایران را کاهش داده است/ خبرفوری
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 46.4K · <a href="https://t.me/akhbarefori/693462" target="_blank">📅 18:32 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693461">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">♦️
شیخ نعیم قاسم خطاب به مخالفان حزب‌الله: ۲ سال تمام جان کندید تا سلاح را بگیرید و نتوانستید؛ حالا چرا این توقع را از ارتش لبنان دارید؟ اصلاً سلاح چه ربطی به شما دارد؟
دبیرکل حزب‌الله:
🔹
در خواب ببینید که ارتش لبنان ابزار دست شما شود. ارتش لبنان، ارتشی ملی است و مردم لبنان خودشان با هم کنار می‌آیند؛ شما کاره‌ای نیستید که بخواهید خواسته‌هایتان را دیکته کنید.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 41.1K · <a href="https://t.me/akhbarefori/693461" target="_blank">📅 18:30 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693460">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">♦️
عراقچی: اگر آمریکا اقدامات مشخصی انجام دهد، آماده‌ایم تنگه هرمز را بازگشایی کنیم  وزیر امورخارجه در گفتگو با ان‌بی‌سی:
🔹
می‌خواهیم به جنگ پایان داده شود و خواستار آزادسازی پول‌ها و دارایی‌های خود هستیم که به‌طور غیرقانونی مسدود شده‌اند.
🔹
ما اهمیتی به انتخابات…</div>
<div class="tg-footer">👁️ 40.3K · <a href="https://t.me/akhbarefori/693460" target="_blank">📅 18:28 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693459">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromآمارفکت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sPllV7EaL7eH7kpIol28YW4i2Xnx7_OnZozRQ_u20GvIrlfxCrKCbwmRMXIEPVveRY0uJpDrH-K9yTzGyDyxhOkr3W1awjRVC7Qxmnltr6AKliTrVqVEctLStJ8WbQhsK_PYblq_5G_2h7i8Ea0gw_X2hAMI855RZbP7-3gh7RAFZQ937HISgmMJ6jBoIYJP8NZMHxtpgQusOXvpr6T9WkGGC_LZfDtYjwjnol42UDfAX7kSgquntHP3QVX0m_45XK3PRtcPFax1gKuJxJ7XdwsxtTPp3KN4BEzXzckSxTYheQpYBfSTjpQqzdGaVjB4oZGu3OuhnlujDAPqm_UDww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دسترسی به گاز شهری در غرب آسیا چگونه است؟
🔹
مقایسه دسترسی به گاز در ۶ کشور غرب آسیا نشان می‌دهد که ایران با پوشش ۹۵.۱ درصدی جمعیت (۹۸.۶ درصد شهری و ۸۶.۱ درصد روستایی)، در زمره بالاترین نرخ‌های دسترسی به گاز خانگی در جهان قرار دارد.
🔹
برخلاف شبکه لوله‌کشی گسترده در ایران و ترکیه (۸۵ درصد)، کشورهایی نظیر عراق، امارات، عربستان و قطر برای مصارف خانگی و پخت‌وپز به‌شدت به کپسول‌های گاز (LPG) وابسته‌اند.
📊
آمارفکت | مرجع تخصصی آمار در ایران
@amarfact</div>
<div class="tg-footer">👁️ 40.8K · <a href="https://t.me/akhbarefori/693459" target="_blank">📅 18:24 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693458">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TS4zW6S5fZzoJ2U_Gi5wprQ2Tm6XVQeK_rh1B6Znnf7_EfytDhx_FegclcTEiLFASVQHR2vqnmL7JIWbwoeQyATN52Ry5GKwCO9bodVDZP4N3cvFfgoA8WHB6Mya0q0NOBP2k-87WCdttahI9Vg9u_eM8i5LLcV0fWBBixR7I8YwFPgiRsxmcbiKoAv2nbZLBGVNUnCr2aE0C42VLcopHtuXWvlfoRgbDYoeYcQiAp5NKKvlIR4E2XF-AG-iqgXNcxCofemQvLpTe3qBqYFQagv4AsqJ7YWxLSQkp5abWgmoS5bT-4VIduj1otRqch10tS1h_y3byoeBCsNCPhpFAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
حمید رسایی، نماینده مردم در مجلس: عجیب بودن این حکم به دلیل وقوع چند تخلف از روال معمول قضایی است
🔹
جزای نقدی به‌جای حبس در نشر اکاذیب:  اساسا برای اتهام نشر اکاذیب جریمه مالی صادر می‌شود و با وجود پیش‌بینی حبس در قانون، روال بر حبس نیست. بنده شخصاً از آقای…</div>
<div class="tg-footer">👁️ 38.5K · <a href="https://t.me/akhbarefori/693458" target="_blank">📅 18:20 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693456">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sGPSarYaLDJ_M0hBGELpIXteD7jAVlC4jIqG4CJ2V1y7knQnngDbGxWqIEYLHKeHPl96d6SAje9EetFS2BT14NDBS0hwqmDIG9iwL6g_fdCMwpwlNIQ7YOs-p7K_87chYV7Di5kgx1fTQliSFGy5P7F3gQLYv-g1Rjx-rX8D2j3n4QWtkt8WUP4i6wkoYFQq5_wvSqodyjJ7a5LJsOl2DHVK3PDb_2ft0Owhb6Dk9jUljMrc6G9Z824Bnoh3mW9WVjc27cf_PSJGxc2OV6wN1b6J0io6WqjqKKJBxSRtqFM1NIfroz4rj7ATmD8uYESzKfCoEVwFaiW_Im-8kDzQlw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
یک مسیر تازه در خبرفوری آغاز شد
🔹
«آوید» جایی برای یادگیری، تجربه و ساختن مهارت‌های آینده.... @AkhbareFori</div>
<div class="tg-footer">👁️ 52K · <a href="https://t.me/akhbarefori/693456" target="_blank">📅 18:11 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693451">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ClZzq1_07VB_95SC4w2zjnnAUZO1ObuTHfwyBnVN0RAfz_Z5v_DPlPEQC0hOAouvS86WviQc5CBIsZaoZ13PAW0lpHpEtWgyX9M4Nr-MhaXThUUQB7WyAOaBMmHYV_h48IZ-U37toNfcZav_rSaK75gYYaohRoBimTRuzwHBlDAEVew9pTv1zBcUbx5XIghfILV6uwmoRJDSjqNQpAO9_X3vIzJjZjVFDBQNNm6mEWk4oqDLMz96XN899v6l4Fm2rpeznrxOXVPEVRJ3Owf6zFvE-EQ112VtdBdKYelg5F2pF9LnhbHz_ZjGDRyqBLAlA7umSkiWo-ZGc746RIEvbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mhRm0woFun0yRkg6ecCnkNFRgZcu3xTpcTbtVU1YojrAzAYeOpgR6ZfpOJh5DhMQB8PSQ5GV-ZN_PJOALEn0_DffMqFXldN6b9LKBSbIr5MrI0fgbnxZ5z4pt1MHSJ5dM4LD9nrjoCo0h2qW_CjdwvTp_wYphLL6_Sg57Z5WaMDdGJGNmjRPlM0Afl_WPi0pqrueDegku6oGYnhB-ZNcZUSw6D-PaIIZMJYbFoslpXowTj4G_NuLk38INN3hqi-9FabJMHqKRHgZTHusyADf_o8inzD9HbVZD3ad-0EGnRU18sMgIbDsvNg-nXpWv5vNyDvBME8hobrFdSBqrS5NdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jHVZRCQ4UehBBBrbwhp5i6r0K20T9kHGFX09IAgTzi1MtodjSdCis9feTsNRrxc9EIWMKv8jOIbYtJ1lasPAvaoELaqdS0ElDx_3QscVXsVemqJAkIP9e7o4KLd_p_VC7sOm3UlgPR7eMRxHthX8MBu-dRqKlPQxxXKhRGSTwhzun6kL-UkWQ4dUIf3TH5V42dTXWHDTaK-P5T3Iguy45MumzPYCoGMCoycHFn8L5mie1E39O2f3D1mFTl67k96QIicy3DrAZRKd99GPe53MyB6xQ_Nmoks4MlzWzRET8gWxTl9Gn-e79HqzJRtdXURaNlflvnO8Vu8v2LTVWmlKAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/c6sB7UsnSNfx60dBwipA-Nr1NIak3_U_5-b7PIxrkinj3t-ll-uaL2VC3bwIwFrgPWj_gXSj3lZD9hc-FPiEGnFJQEjQd0K2qZMU5ED8hz_h5FKgU9NG0G3c64jLlL8CRS2WdVMHpL77n6JJhXIq7Nw5A59BYEcSSTKKp4mFrBs93hooy43pwluaP6WA-8J9bKWg9bIlnhnVvfDzXEhhBfI_w4ZHrGPIpsuU-QAGtUXOHlQgW4Gvy9meIhI8-5l26ApqwIqXTHlrJsyNflT_I9evI80glAXQ7h_OOa_mJGKcAqKxVGCQxjezTtb9NOo-W_458yUU5DrU_M5U7rwe1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/v5DhKZwqy6dhLB3r7XbPAUPe1QMV6In_09YpGVwQ-K2V8jp-kw_vXFrI3P-gcSgoiJdKABt8JRvwJQskuyeNy75dpdV0_sxsgYUESO5SYM6YziGDc-CD0KYun6E-jUlIp4968vgYX_EWkidjHGjQbJ7Nkil5j4wQJCAZrpw2lC8CgCkr86q-gL_3zucTrh72UIJDN9r_gWDK_xPNXC-2ZHarMZlfs6R00f1z-ZTc2hHAag72MmsalXTEUz4awQd01X6BxMPnTRZrjwp91ZOhkKeQ8mu-2xRtz6zXhsFL8J7wx0kjAAoZklGXNkQFoeXG73jaZn-SRFTxjLobe0oLSw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
بسیار کاربردی؛ ۱۲ ماه سال به انگلیسی
🔹
۱۱ دی (۳۱ روز): January
🔹
از ۱۲ بهمن (۲۸ روز): February
🔹
از ۱۰ اسفند (۳۱ روز): March
🔹
از ۱۲ فروردین(۳۰ روز): April
🔹
از ۱۱ اردیبهشت (۳۱ روز): May
🔹
از ۱۱ خرداد(۳۰ روز): June
🔹
از ۱۰ تیر (۳۱ روز): July
🔹
از ۱۰ مرداد…</div>
<div class="tg-footer">👁️ 38.2K · <a href="https://t.me/akhbarefori/693451" target="_blank">📅 18:10 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693449">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">♦️
خبرنگار cbs: یک مقام ایرانی به من گفته که مذاکرات روز دوشنبه میان ایران و آمریکا لغو شده است
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 39.9K · <a href="https://t.me/akhbarefori/693449" target="_blank">📅 18:06 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693446">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SedWj9wpy2JBdpGePJHXy2ZnpeM4ZDSuiOxK5UW-N9eTQDEJRlQZfX_wDCrYb19dcfctxSQ2AojoyNA-orskB4v2s0F7W-H86kyhAt0Vcrezj73Jx2BELrbQkLpIqf2EHw09xxv97Bkzg1sL3nYeCXlf0S-rgjUsnc-0lf4OyZDMLTvggBb3z00b9zUriHCzNTk9ltkutcUus4_fppiA_Gbm4F8AFg4yoWSsAOhyi11-H-M5Ysrw5ZK8yvctQeqW4Tu--o5-F916bQQDgMg4Eo-XChkcCpEjwTlIcFX3jBV2GFfCl36Iu5c5zIMMoRgbgKKwN128_k7csPPgwfWgQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uHzq6shVfmTQgmfpynTycu8BkPwFABCJFgl0s5LBOR2myGxHY35P6f1S84VWHbKXZiqU8W0_4AGgj4iWKJ1g3Hr0xcN6W4W3ddZkCmV9eF3xtCXzJSUfamVKnF31rLiqE4sRNG9aqq2MsLoukav8hcKJcom9glYFG5YHcsjk-cy2m4ltSF6es3HuSLKCuYswX3bDgTGIjV6h4Y8FwOct1olylwCieKZfnkl_DivjWUrMscnZHHJVxdjbPsKIrS793Fs7qB_4HosPHdPBex19gsiknhdkXFFFgdOGM-yMTAOzvG1KjGC8fUKG6SRfLyzEd9ctSXq9kOjxsyXEAAZnFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/X7uK1zv531UCJTp_LbhGF_3NzP2_Q96aJAC_wcyFhl355A6jaBEC5oqTUdMuDQ1x_AVfgHjwQ1eeQ-W23C0mJeT7g2pttQ3RZPh1L-gYflyzUEHZChmUzn6fa_A-gHd0hJkTE29JFgk_eT0L_3era6zF4SvgKmNCtw2rlB0K56MXbUDyXb6R09mjt6bYJ9OXAWypqKspYngKYA34fF1WD3jx_76sx1SggvNYwJ4m1rrnGvmzlBt94RXpWzyMgX0lP_ijJYw7sjp01c7jmzQgRo4JVW-ydXfnqXfjuV88KQbHpobQ1fJvfKEvd5RVV_wVEDypPnDw89KjmgC37oy21Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
سنگ در غذای دانشجویان دانشگاه علوم پزشکی بهبهان!
🔹
تاکنون توضیح رسمی از سوی دانشگاه درباره این ادعا منتشر نشده است.
#اخبار_خوزستان
در فضای مجازی
👇
@akhbar_khozestan</div>
<div class="tg-footer">👁️ 40.9K · <a href="https://t.me/akhbarefori/693446" target="_blank">📅 18:00 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693445">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">♦️
ادعای وزیر خزانه‌داری آمریکا: چین کمک‌های خود به ایران را کاهش داده است/ خبرفوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 41.7K · <a href="https://t.me/akhbarefori/693445" target="_blank">📅 17:56 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693444">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">♦️
ماجرای عجیب برنج‌هایی که بدون اسناد و مدارک وارد شدند و اسناد تعلق آن به بازرگان وارد کننده در کانتینر پیدا شد از زبان رئیس قوه قضائیه
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 42.8K · <a href="https://t.me/akhbarefori/693444" target="_blank">📅 17:54 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693442">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/157770ffed.mp4?token=NHAGNJpXZ726tqR3zSFs1sVaqnI0XuX2k62TIF4kXraNivfkFO33eVAMnke2Vgnw-SaeAN9fou4Q0QsE8XzzfoJA4F8Pqr7UTSgKoMATSuHaRqX_svXQ2ZP2OR-qr8jiSd1GmlzAO85_l-bVRKPVP7uXzuFzi-VnUYEp1CCe0W_dma8wwy1qR29hnZZyrMHKNz2SAwYUZDa_C736DZDxW4W7N-4Kb4PpbP86eFDYdlv_pt5G0WnnOcoK3TmWhbL3AGxc-yJUuOluj8PIW644iR1MTSsOs5CzZUmy6CaM9wJS0W4JGKYfMGLvnj13HXkOaEjNxFA4iCHrhjHrFl6Gyg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/157770ffed.mp4?token=NHAGNJpXZ726tqR3zSFs1sVaqnI0XuX2k62TIF4kXraNivfkFO33eVAMnke2Vgnw-SaeAN9fou4Q0QsE8XzzfoJA4F8Pqr7UTSgKoMATSuHaRqX_svXQ2ZP2OR-qr8jiSd1GmlzAO85_l-bVRKPVP7uXzuFzi-VnUYEp1CCe0W_dma8wwy1qR29hnZZyrMHKNz2SAwYUZDa_C736DZDxW4W7N-4Kb4PpbP86eFDYdlv_pt5G0WnnOcoK3TmWhbL3AGxc-yJUuOluj8PIW644iR1MTSsOs5CzZUmy6CaM9wJS0W4JGKYfMGLvnj13HXkOaEjNxFA4iCHrhjHrFl6Gyg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
هوش مصنوعی؛ از ۲۰۲۱ تا ۲۰۲۶
🤖
🚀
🔹
مقایسه نسل‌های هوش مصنوعی از سال ۲۰۲۱ تا ۲۰۲۶؛ جهشی از مدل‌های اولیه تا سامانه‌های پیشرفته‌ای مانند GPT-6 Astra و Claude Opus 5.5.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 43.2K · <a href="https://t.me/akhbarefori/693442" target="_blank">📅 17:42 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693441">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">♦️
سی‌بی‌اس به نقل از یک منبع آگاه مدعی شد: مذاکرات آمریکا و ایران با وجود رد پیشنهاد توسط ترامپ، هفته آینده برگزار می‌شود
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 41.2K · <a href="https://t.me/akhbarefori/693441" target="_blank">📅 17:37 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693440">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">♦️
عراقچی: اگر آمریکا اقدامات مشخصی انجام دهد، آماده‌ایم تنگه هرمز را بازگشایی کنیم
وزیر امورخارجه در گفتگو با ان‌بی‌سی:
🔹
می‌خواهیم به جنگ پایان داده شود و خواستار آزادسازی پول‌ها و دارایی‌های خود هستیم که به‌طور غیرقانونی مسدود شده‌اند.
🔹
ما اهمیتی به انتخابات میان‌دوره‌ای آمریکا نمی‌دهیم؛ آنچه برای ما اهمیت دارد منافع ملی‌مان است.
🔹
همان‌قدر که برای مقابله با هرگونه تجاوز، حتی اگر به یک جنگ ویرانگر منجر شود، آماده‌ایم، برای مذاکره نیز آماده‌ایم.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 43.1K · <a href="https://t.me/akhbarefori/693440" target="_blank">📅 17:33 · 05 Mehr 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
